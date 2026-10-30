#!/usr/bin/env python3
"""S16 F1 – visszaolvasó QA a gyártási adatmodellre (parts_v1.json).

Súlyosság:
  BLOKKOLO  – kiadást tilt (negatív/nulla méret, modell↔lista eltérés, ütközés, ID-hiba, nyers < kész)
  HIBA      – gyártás előtt javítandó tervi/műszaki hiba
  FIGYELMEZTETES – műhelyi döntés vagy hiányzó adat
  INFO      – tájékoztató mérés

Futtatás:  python3 qa_parts_v1.py [--parts parts_v1.json]
Kimenet:   qa_report.md, qa_report.json; kilépési kód 2, ha van BLOKKOLO.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from datetime import date
from itertools import combinations
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s16_geom import LocalFrame, build_solid, load_json  # noqa: E402

SEV_ORDER = ["BLOKKOLO", "HIBA", "FIGYELMEZTETES", "INFO"]


class QA:
    def __init__(self):
        self.items = []

    def add(self, sev, kod, alkatresz, uzenet, **adat):
        self.items.append({"sulyossag": sev, "kod": kod, "alkatresz": alkatresz, "uzenet": uzenet, **adat})


def num_ok(v):
    return isinstance(v, (int, float)) and np.isfinite(v)


# ---------------------------------------------------------------- ellenőrzések

def q_meretek(doc, qa):
    for r in doc["alkatreszek"]:
        pid, m = r["id"], r["meret"]
        for kind in ("kesz", "elzaras_elotti", "nyers"):
            for k, v in m[kind].items():
                if v is None:
                    if kind == "nyers" and r["lap_alkatresz"] and r["anyag"]["kod"] != "M05":
                        qa.add("FIGYELMEZTETES", "Q01_NYERS_HIANYZIK", pid, f"nyers {k} nincs megadva")
                    continue
                if not num_ok(v) or v <= 0:
                    qa.add("BLOKKOLO", "Q01_NEM_POZITIV_MERET", pid, f"{kind}.{k} = {v} (nem pozitív méret)")
        box = r["befoglalo_globalis"]
        if any((not num_ok(b) or b <= 0) for b in box[3:]):
            qa.add("BLOKKOLO", "Q01_NEM_POZITIV_MERET", pid, f"befoglaló méret nem pozitív: {box[3:]}")


def q_nyers_vs_kesz(doc, rules, qa):
    for r in doc["alkatreszek"]:
        m = r["meret"]
        mat = rules["anyagok"][r["anyag"]["kod"]]
        for k in ("L", "W"):
            ny, el, ke = m["nyers"][k], m["elzaras_elotti"][k], m["kesz"][k]
            if ny is None or not num_ok(ny):
                continue
            if ny + 1e-6 < el:
                qa.add("BLOKKOLO", "Q02_NYERS_KISEBB_MINT_KESZ", r["id"],
                       f"nyers {k}={ny} < élzárás előtti {el} (kész {ke}) – a darab nem gyártható le ebből a szabásból",
                       forras=m["nyers_szabaly"])
        txt = m.get("r14_raw_rule") or ""
        mk = re.search(r"kész\s*L\s*(\d+(?:[.,]\d+)?)", txt)
        mn = re.search(r"nyers[^L]*L\s*(\d+(?:[.,]\d+)?)", txt)
        if mk and abs(float(mk.group(1).replace(",", ".")) - m["kesz"]["L"]) > 0.01:
            qa.add("HIBA", "Q03_SZOVEG_ADAT_ELTERES", r["id"],
                   f"R14 raw_rule szövege kész L={mk.group(1)} mm-t ír, az adat L={m['kesz']['L']} mm"
                   + (f"; nyers a szövegben {mn.group(1)}, adatban {m['nyers']['L']}" if mn else ""),
                   r14_raw_rule=txt)
        if m["nyers_szabaly"] and m["nyers_szabaly"].startswith("R14 explicit") and mat.get("rahagyas_L") is not None:
            pm = mat.get("elomaras_elenkent") or 0
            exp_L = m["elzaras_elotti"]["L"] + mat["rahagyas_L"]
            exp_W = m["elzaras_elotti"]["W"] + mat["rahagyas_W"]
            if pm == 0 and (abs(m["nyers"]["L"] - exp_L) > 0.01 or abs(m["nyers"]["W"] - exp_W) > 0.01):
                qa.add("FIGYELMEZTETES", "Q03_NYERS_SZABALY_ELLENTMONDAS", r["id"],
                       f"R14 explicit nyers {m['nyers']['L']}×{m['nyers']['W']} ≠ anyagszabály szerinti {exp_L}×{exp_W}",
                       r14_raw_rule=m.get("r14_raw_rule"))


def q_lwt_box(doc, qa, tol):
    for r in doc["alkatreszek"]:
        g, k = r["meret"]["geometriabol"], r["meret"]["kesz"]
        for a in ("L", "W", "T"):
            if num_ok(k[a]) and abs(g[a] - k[a]) > tol:
                qa.add("BLOKKOLO", "Q04_LISTA_BEFOGLALO_ELTERES", r["id"],
                       f"{a}: lista {k[a]} ≠ befoglalóból {g[a]} (helyi tengely {r['helyi_rendszer'][{'L': 'U', 'W': 'V', 'T': 'N'}[a]]})")


def q_modell_lista(doc, parts_src, zart, qa, tol):
    src = {p["id"]: p for p in parts_src}
    ids = {r["id"] for r in doc["alkatreszek"]}
    zprim = {o["name"]: o for o in zart["objects"] if o["role"] == "primary_part"}
    for pid in sorted(set(zprim) ^ ids):
        qa.add("BLOKKOLO", "Q05_MODELL_LISTA_HIANY", pid, "csak a modellben vagy csak a listában szerepel")
    for r in doc["alkatreszek"]:
        pid = r["id"]
        box = np.array(r["befoglalo_globalis"], float)
        lo, hi = box[:3], box[:3] + box[3:]
        if pid in zprim:
            v = np.asarray(zprim[pid]["vertices_mm"], float)
            d = max(np.abs(v.min(0) - lo).max(), np.abs(v.max(0) - hi).max())
            if d > tol:
                qa.add("BLOKKOLO", "Q05_MODELL_LISTA_ELTERES", pid, f"R14 zárt jelenet befoglalója {d:.3f} mm-rel eltér a listától")
        mm = src[pid].get("mesh_mm")
        if mm:
            v = np.asarray(mm["vertices"], float)
            d = max(np.abs(v.min(0) - lo).max(), np.abs(v.max(0) - hi).max())
            if d > tol:
                qa.add("BLOKKOLO", "Q05_MESH_LISTA_ELTERES", pid, f"parts.json mesh_mm befoglalója {d:.3f} mm-rel eltér")


def q_kontur(doc, qa, tol):
    for r in doc["alkatreszek"]:
        k = r["kontur"]
        if not k.get("van"):
            continue
        u0, v0, u1, v1 = k["bbox_uv"]
        L, W = r["meret"]["kesz"]["L"], r["meret"]["kesz"]["W"]
        d = max(abs(u0), abs(v0), abs(u1 - L), abs(v1 - W))
        if d > tol:
            qa.add("HIBA", "Q06_KONTUR_BEFOGLALO", r["id"], f"kontúr befoglalója ({u0},{v0})–({u1},{v1}) ≠ 0..{L} × 0..{W} (max {d:.3f} mm)")


def q_vastagsag(doc, rules, qa):
    for r in doc["alkatreszek"]:
        if not r["lap_alkatresz"]:
            if r["meret"]["kesz"]["T"] > 40:
                qa.add("INFO", "Q07_OSSZEALLITAS_NEM_LAP", r["id"],
                       f"{r['gyartasi_tipus']} – T={r['meret']['kesz']['T']} befoglaló, nem lapvastagság; nem írható ki egy lapként")
            continue
        nom = rules["anyagok"][r["anyag"]["kod"]]["nevleges_vastagsag"]
        T = r["meret"]["kesz"]["T"]
        if abs(T - nom) > 0.01:
            qa.add("HIBA", "Q07_VASTAGSAG_ANYAG_ELTERES", r["id"],
                   f"T={T} mm, de az anyag ({r['anyag']['kod']} – {r['anyag']['megnevezes']}) névleges vastagsága {nom} mm")


def q_id(doc, rules, qa):
    pat = re.compile(rules["cimke_azonosito"]["minta"])
    c1 = Counter(r["id"] for r in doc["alkatreszek"])
    c2 = Counter(r["cimke_id"] for r in doc["alkatreszek"])
    for k, n in c1.items():
        if n > 1:
            qa.add("BLOKKOLO", "Q08_DUPLIKALT_ID", k, f"{n}× szerepel")
    for k, n in c2.items():
        if n > 1:
            qa.add("BLOKKOLO", "Q08_DUPLIKALT_CIMKE_ID", k, f"{n}× szerepel")
        if not pat.match(k):
            qa.add("BLOKKOLO", "Q08_CIMKE_ID_FORMATUM", k, f"nem felel meg: {pat.pattern}")


def q_anyag(doc, materials, rules, qa):
    known = {m[0] for m in materials}
    for r in doc["alkatreszek"]:
        k = r["anyag"]["kod"]
        if k not in known or k not in rules["anyagok"]:
            qa.add("BLOKKOLO", "Q09_ISMERETLEN_ANYAG", r["id"], f"anyagkód {k} nincs a materials.json/szabályfájlban")


def q_lapmeret(doc, rules, qa):
    for r in doc["alkatreszek"]:
        if not r["lap_alkatresz"]:
            continue
        mat = rules["anyagok"][r["anyag"]["kod"]]
        sheet = mat.get("lapmeret")
        if not sheet:
            continue
        m = r["meret"]
        L = m["nyers"]["L"] or m["kesz"]["L"]
        W = m["nyers"]["W"] or m["kesz"]["W"]
        S_long, S_short = max(sheet), min(sheet)
        g = r["szalirany"]["helyi_tengely"]
        if mat.get("erezetes") and g:
            along, across = (L, W) if g == "U" else (W, L)
            if along > S_long or across > S_short:
                fits_rot = max(L, W) <= S_long and min(L, W) <= S_short
                qa.add("HIBA", "Q10_EREZET_LAPMERET", r["id"],
                       f"{L}×{W} mm, erezet a {g} tengely mentén ({along} mm) – becsült {S_long}×{S_short} táblából erezettel nem jön ki"
                       + ("; erezet nélkül/90°-kal kijönne" if fits_rot else "; semmilyen tájolásban nem fér ki"),
                       lapmeret_forras=mat.get("lapmeret_forras"))
        else:
            if max(L, W) > S_long or min(L, W) > S_short:
                qa.add("HIBA", "Q10_LAPMERET", r["id"], f"{L}×{W} mm nem fér ki a becsült {S_long}×{S_short} táblából",
                       lapmeret_forras=mat.get("lapmeret_forras"))


def _intersection_volume(a, b):
    import trimesh
    if a.mesh is None or b.mesh is None:
        lo = np.maximum(a.lo, b.lo)
        hi = np.minimum(a.hi, b.hi)
        return float(np.prod(np.clip(hi - lo, 0, None))), "bbox"
    try:
        m = trimesh.boolean.intersection([a.mesh, b.mesh], engine="manifold")
        return float(abs(m.volume)) if m is not None and len(m.faces) else 0.0, "mesh"
    except Exception as e:  # pragma: no cover
        return float("nan"), f"hiba:{e}"


def q_utkozes(doc, solids, rules, qa, label="zárt állapot", moved=None):
    vmin = rules["qa"]["utkozes_min_terfogat_mm3"]
    ids = list(solids)
    n = 0
    for a, b in combinations(ids, 2):
        sa, sb = solids[a], solids[b]
        if not sa.bbox_overlap(sb, tol=0.01):
            continue
        if moved is not None and a not in moved and b not in moved:
            continue
        vol, how = _intersection_volume(sa, sb)
        n += 1
        if not (vol <= vmin):
            qa.add("BLOKKOLO", "Q11_UTKOZES", f"{a} × {b}", f"{label}: átfedő térfogat {vol:.1f} mm³ ({how})")
    return n


def q_frontres(doc, solids, rules, qa):
    from shapely.geometry import box as sbox
    y0, y1 = rules["qa"]["front_sik_y"]
    nom, mn = rules["qa"]["front_res_nevleges_mm"], rules["qa"]["front_res_min_mm"]
    polys = {}
    for r in doc["alkatreszek"]:
        bx = r["befoglalo_globalis"]
        if bx[1] >= y1 or bx[1] + bx[4] <= y0:
            continue
        s = solids[r["id"]]
        if s.mesh is not None:
            sec = s.mesh.section(plane_origin=[0, (y0 + y1) / 2, 0], plane_normal=[0, 1, 0])
            if sec is not None:
                try:
                    p2, T = sec.to_2D(to_2D=np.array([[1, 0, 0, 0], [0, 0, 1, 0], [0, -1, 0, 0], [0, 0, 0, 1]], float))
                    pg = p2.polygons_full
                    if pg:
                        from shapely.ops import unary_union
                        polys[r["id"]] = unary_union(pg)
                        continue
                except Exception:
                    pass
        polys[r["id"]] = sbox(bx[0], bx[2], bx[0] + bx[3], bx[2] + bx[5])
    mov = {r["id"]: r["mozgo_egyseg"] for r in doc["alkatreszek"]}
    rows = []
    for a, b in combinations(polys, 2):
        if mov.get(a) and mov.get(a) == mov.get(b):
            continue
        if not (mov.get(a) or mov.get(b)):
            continue
        d = polys[a].distance(polys[b])
        if d > 10:
            continue
        # csak szemben álló élek: a két elem vetülete X-ben vagy Z-ben legalább 1 mm-en átfed (sarok-átló nem rés)
        ax0, az0, ax1, az1 = polys[a].bounds
        bx0, bz0, bx1, bz1 = polys[b].bounds
        ovx = min(ax1, bx1) - max(ax0, bx0)
        ovz = min(az1, bz1) - max(az0, bz0)
        if polys[a].intersection(polys[b]).area <= 0.01 and ovx < 1 and ovz < 1:
            continue
        if d > 0:
            from shapely.ops import nearest_points
            pa, pb = nearest_points(polys[a], polys[b])
            if abs(pa.x - pb.x) > 0.5 and abs(pa.y - pb.y) > 0.5:
                continue  # sarok-átló
        inter = polys[a].intersection(polys[b]).area
        rows.append((a, b, round(d, 2), round(inter, 2)))
        if inter > 0.01:
            qa.add("BLOKKOLO", "Q12_FRONT_ATFEDES", f"{a} × {b}", f"homlokzati átfedés {inter:.1f} mm² a front síkjában")
        elif d < mn:
            qa.add("HIBA", "Q12_FRONTRES_KICSI", f"{a} × {b}", f"mozgó front rése {d:.2f} mm < {mn} mm")
        elif abs(d - nom) > 0.05:
            qa.add("INFO", "Q12_FRONTRES_ELTER", f"{a} × {b}", f"rés {d:.2f} mm (névleges {nom})")
    return rows


def q_fiok(doc, drawers, solids, rules, qa):
    B = rules["qa"]["blum_movento"]
    parts = {r["id"]: r for r in doc["alkatreszek"]}
    for d in drawers:
        did = d["id"]
        src = B["forras"]
        if d["SKW"] != d["LW"] - B["SKW_eq_LW_minus"]:
            qa.add("HIBA", "Q13_BLUM_SKW", did, f"SKW {d['SKW']} ≠ LW {d['LW']} − {B['SKW_eq_LW_minus']}", forras=src)
        L, R = parts.get(f"{did}-BOX-L"), parts.get(f"{did}-BOX-R")
        CL, CR = parts.get(f"{did}-L"), parts.get(f"{did}-R")
        BB = parts.get(f"{did}-BOX-B")
        if not all((L, R, CL, CR, BB)):
            qa.add("BLOKKOLO", "Q13_FIOK_ALKATRESZ_HIANY", did, "hiányzó fiók-/korpuszalkatrész")
            continue
        lw_geo = CR["befoglalo_globalis"][0] - (CL["befoglalo_globalis"][0] + CL["befoglalo_globalis"][3])
        skw_geo = R["befoglalo_globalis"][0] - (L["befoglalo_globalis"][0] + L["befoglalo_globalis"][3])
        if did == "D6":
            # D6 jobb oldala ívelt héjba csatlakozik – a belső szélesség a drawers.json szerint
            pass
        if abs(lw_geo - d["LW"]) > 0.01:
            qa.add("HIBA", "Q13_LW_GEOMETRIA", did, f"korpusz belső szélesség geometriából {lw_geo} ≠ drawers.json LW {d['LW']}")
        if abs(skw_geo - d["SKW"]) > 0.01:
            qa.add("HIBA", "Q13_SKW_GEOMETRIA", did, f"fiók belső szélesség geometriából {skw_geo} ≠ SKW {d['SKW']}")
        side_len = L["meret"]["kesz"]["L"]
        if abs(side_len - (d["NL"] - B["fiokoldal_hossz_eq_NL_minus"])) > 0.01:
            qa.add("HIBA", "Q13_BLUM_OLDALHOSSZ", did, f"fiókoldal {side_len} ≠ NL {d['NL']} − {B['fiokoldal_hossz_eq_NL_minus']}", forras=src)
        t = L["meret"]["kesz"]["T"]
        if t > B["oldal_max_vastagsag"]:
            qa.add("HIBA", "Q13_BLUM_OLDALVASTAGSAG", did, f"fiókoldal {t} mm > {B['oldal_max_vastagsag']} mm", forras=src)
        recess = BB["befoglalo_globalis"][2] - L["befoglalo_globalis"][2]
        if recess < B["fenek_besullyesztes_min_magassag"]:
            qa.add("HIBA", "Q13_BLUM_FENEK_BESULLYESZTES", did,
                   f"fiókfenék alsó síkja az oldal alsó élétől {recess:.1f} mm-re van; MOVENTO-hoz ≥ {B['fenek_besullyesztes_min_magassag']} mm "
                   f"(max {B['fenek_besullyesztes_max_melyseg']} mm mély) besüllyesztés kell, hogy a sín takarva legyen",
                   forras=src)


def q_fiok_mozgas(doc, drawers, solids, rules, qa):
    import copy
    for d in drawers:
        moved = {}
        for pid in d["moving"]:
            s = copy.copy(solids[pid])
            off = np.array([0, d["stroke"], 0.0])
            s.lo, s.hi = s.lo + off, s.hi + off
            if s.mesh is not None:
                s.mesh = s.mesh.copy()
                s.mesh.apply_translation(off)
            moved[pid] = s
        # söpört térfogat közelítése: zárt és nyitott állapot + 4 közbenső
        hits = set()
        for frac in (0.25, 0.5, 0.75, 1.0):
            test = dict(solids)
            for pid in d["moving"]:
                s = copy.copy(solids[pid])
                off = np.array([0, d["stroke"] * frac, 0.0])
                s.lo, s.hi = s.lo + off, s.hi + off
                if s.mesh is not None:
                    s.mesh = s.mesh.copy()
                    s.mesh.apply_translation(off)
                test[pid] = s
            sub = QA()
            q_utkozes(doc, test, rules, sub, label=f"{d['id']} fiók {int(frac*100)}% nyitva", moved=set(d["moving"]))
            for it in sub.items:
                if it["alkatresz"] not in hits:
                    hits.add(it["alkatresz"])
                    qa.items.append(it)
        if not hits:
            qa.add("INFO", "Q14_FIOK_MOZGAS_OK", d["id"],
                   f"{d['stroke']} mm névleges kihúzás 25/50/75/100%-on ütközésmentes (csak tömör alkatrészek; sín, kábel, LED-profil nincs benne)")


def q_hianyzo(doc, layout, qa):
    ids = {r["id"] for r in doc["alkatreszek"]}
    for n in layout.get("current_changes", {}).get("primary_changed", []):
        if n not in ids:
            qa.add("HIBA", "Q16_HIVATKOZOTT_ALKATRESZ_HIANYZIK", n,
                   "a layout.json R14 'primary_changed' listája hivatkozza, de sem a parts.json-ban, sem a zárt jelenetben nincs ilyen test")
    for a in doc["segedobjektumok_R14_jelenetbol"]:
        if a["kategoria"].startswith("GYARTANDO"):
            qa.add("FIGYELMEZTETES", "Q16_GYARTANDO_ELEM_NINCS_A_LISTABAN", a["nev"],
                   f"R14 jelenet-segédobjektum (befoglaló {a['befoglalo']}) – valós takaró/tálca, anyagjegyzékbe és rétegrendbe veendő")
        elif a["kategoria"].startswith("BELSO_LED") or a["kategoria"].startswith("VASAROLT"):
            qa.add("INFO", "Q16_TERMEK_HELYFOGLALO", a["nev"], a["kategoria"])


def q_el(doc, rules, qa):
    allowed = set(rules["el_kod_jelek"]) - {"etalon_megfeleltetes"}
    for r in doc["alkatreszek"]:
        code = r["el_kod"]
        if len(code) != 4 or any(c not in allowed for c in code):
            qa.add("BLOKKOLO", "Q19_EL_KOD_FORMATUM", r["id"], f"érvénytelen él-kód '{code}'")
        for e, ed in r["elek"].items():
            if ed["szerep"] == "SZABAD_ELOL" and ed["jel"] == "0" and r["lap_alkatresz"]:
                qa.add("HIBA", "Q19_LATSZO_EL_KEZELETLEN", r["id"], f"{e} ({ed['irany_nev']}) szabad elülső él élkezelés nélkül")
        if r["anyag"]["kod"] == "M03" and "0" in code:
            qa.add("HIBA", "Q19_FRONT_EL_KEZELETLEN", r["id"], f"dekor front él-kódja {code}")


def q_muveletek(doc, rules, qa):
    nmin = rules["qa"]["falc_min_maradek_mm"]
    open_ops = Counter()
    for r in doc["alkatreszek"]:
        L, W, T = (r["meret"]["kesz"][k] for k in ("L", "W", "T"))
        for op in r["muveletek"]:
            if op.get("szerszam") is None:
                open_ops[op["op"]] += 1
            hb = op.get("helyi_doboz")
            if hb:
                u0, u1 = hb["u"]
                v0, v1 = hb["v"]
                n0, n1 = hb["n"]
                if u1 <= 0 or u0 >= L or v1 <= 0 or v0 >= W or n1 <= 0 or n0 >= T:
                    qa.add("HIBA", "Q20_MUVELET_KIVUL", r["id"], f"{op['op']} doboza az alkatrészen kívül esik: {hb}")
                maradek = T - (min(n1, T) - max(n0, 0)) if op["op"] != "KIMETSZES" else None
                if maradek is not None and maradek < nmin - 1e-6:
                    qa.add("HIBA", "Q20_FALC_MARADEK", r["id"], f"{op['op']}: maradó anyag {maradek:.1f} mm < {nmin} mm")
                if op["op"] in ("FALC", "FENYCSATORNA_FALC"):
                    qa.add("INFO", "Q20_FALC_MERES", r["id"], f"{op['op']}: mélység {min(n1, T) - max(n0, 0):.1f} mm, maradék {maradek:.1f} mm")
            if op["op"] == "HATSO_FENYFALC" and op.get("n_tartomany"):
                n0, n1 = op["n_tartomany"]
                maradek = T - (n1 - n0)
                if maradek < nmin - 1e-6:
                    qa.add("HIBA", "Q20_FALC_MARADEK", r["id"], f"HATSO_FENYFALC: maradó anyag {maradek:.1f} mm < {nmin} mm")
                else:
                    qa.add("INFO", "Q20_FALC_MERES", r["id"], f"HATSO_FENYFALC: mélység {n1 - n0:.1f} mm, maradék {maradek:.1f} mm, perem {op.get('perem_mm')} mm")
    for op, n in sorted(open_ops.items()):
        qa.add("INFO", "Q21_SZERSZAM_NINCS", op, f"{n} művelet szerszám-hozzárendelés nélkül – MPR nem generálható")


def q_geom_forras(doc, qa):
    for r in doc["alkatreszek"]:
        if r["geometria_forras"] == "bbox":
            qa.add("FIGYELMEZTETES", "Q22_CSAK_BEFOGLALO", r["id"], "zárt test nem építhető; ütközés csak befoglalóval vizsgálva")


def q_mennyezet(doc, rules, qa):
    zmax = max(r["befoglalo_globalis"][2] + r["befoglalo_globalis"][5] for r in doc["alkatreszek"])
    gap = rules["qa"]["mennyezet_nevleges"] - zmax
    sev = "INFO" if gap >= rules["qa"]["mennyezeti_res_min"] - 1e-6 else "HIBA"
    qa.add(sev, "Q18_MENNYEZETI_RES", "*", f"legmagasabb pont Z={zmax}, rés a névleges {rules['qa']['mennyezet_nevleges']} mm-es mennyezetig {gap} mm (helyszíni felmérés még nincs)")


# ---------------------------------------------------------------- futtatás

def run(parts_path: Path):
    doc = load_json(parts_path)
    rules = load_json(HERE / "gyartasi_szabalyok_v1.json")
    src = HERE / "forras_R14"
    parts_src = load_json(src / "parts.json")
    zart = load_json(src / "R14_ZART_JELENET_MM.json")
    materials = load_json(src / "materials.json")
    drawers = load_json(src / "drawers.json")
    layout = load_json(src / "layout.json")
    tol = rules["qa"]["mesh_tures_mm"]

    zobj = {o["name"]: o for o in zart["objects"]}
    src_by_id = {p["id"]: p for p in parts_src}
    solids = {}
    for r in doc["alkatreszek"]:
        p = dict(src_by_id.get(r["id"], {}))
        p.update({"id": r["id"], "box": r["befoglalo_globalis"], "axis": p.get("axis", "y")})
        solids[r["id"]] = build_solid(p, zobj.get(r["id"]))

    qa = QA()
    q_meretek(doc, qa)
    q_nyers_vs_kesz(doc, rules, qa)
    q_lwt_box(doc, qa, rules["qa"]["tures_mm"])
    q_modell_lista(doc, parts_src, zart, qa, tol)
    q_kontur(doc, qa, tol)
    q_vastagsag(doc, rules, qa)
    q_id(doc, rules, qa)
    q_anyag(doc, materials, rules, qa)
    q_lapmeret(doc, rules, qa)
    npairs = q_utkozes(doc, solids, rules, qa)
    front_rows = q_frontres(doc, solids, rules, qa)
    q_fiok(doc, drawers, solids, rules, qa)
    q_fiok_mozgas(doc, drawers, solids, rules, qa)
    q_hianyzo(doc, layout, qa)
    q_mennyezet(doc, rules, qa)
    q_el(doc, rules, qa)
    q_muveletek(doc, rules, qa)
    q_geom_forras(doc, qa)
    meta = {"alkatresz": len(doc["alkatreszek"]), "vizsgalt_utkozo_par": npairs,
            "frontres_sorok": front_rows, "geometria_forrasok": dict(Counter(s.method for s in solids.values()))}
    return doc, qa, meta


def write_report(doc, qa, meta, out_md: Path, out_json: Path):
    items = sorted(qa.items, key=lambda i: (SEV_ORDER.index(i["sulyossag"]), i["kod"], i["alkatresz"]))
    cnt = Counter(i["sulyossag"] for i in items)
    verdict = "BLOKKOLT – gyártási kiadás tilos" if cnt["BLOKKOLO"] else (
        "NEM KIADHATÓ – HIBA javítandó" if cnt["HIBA"] else "adatmodell konzisztens (műhelyi megerősítés még kell)")
    out_json.write_text(json.dumps({"datum": date.today().isoformat(), "modell_revizio": doc["modell_revizio"],
                                    "osszesites": dict(cnt), "itelet": verdict, "meta": meta, "tetelek": items},
                                   ensure_ascii=False, indent=1), encoding="utf-8")
    L = [f"# S16 F1 – QA-jelentés ({doc['modell_revizio']})", "",
         f"Generálva: {date.today().isoformat()} · `qa_parts_v1.py` · forrás: `parts_v1.json` ({meta['alkatresz']} alkatrész)", "",
         f"**Ítélet: {verdict}**", "",
         "| Súlyosság | db |", "|---|---|"]
    for s in SEV_ORDER:
        L.append(f"| {s} | {cnt.get(s, 0)} |")
    L += ["", f"Geometria-forrás: {meta['geometria_forrasok']} · vizsgált ütköző pár (befoglaló-átfedéssel): {meta['vizsgalt_utkozo_par']}", ""]
    for s in SEV_ORDER:
        sub = [i for i in items if i["sulyossag"] == s]
        if not sub:
            continue
        L += [f"## {s} ({len(sub)})", "", "| Kód | Alkatrész | Megállapítás |", "|---|---|---|"]
        for i in sub:
            msg = i["uzenet"].replace("|", "/")
            if i.get("forras"):
                msg += f" · forrás: {i['forras']}"
            L.append(f"| {i['kod']} | {i['alkatresz']} | {msg} |")
        L.append("")
    L += ["## Homlokzati rések mozgó elemek körül (front-sík, ≤ 10 mm)", "",
          "| A | B | rés mm | átfedés mm² |", "|---|---|---|---|"]
    for a, b, d, inter in sorted(meta["frontres_sorok"]):
        L.append(f"| {a} | {b} | {d} | {inter} |")
    L += ["", "## Hatókör – amit ez a QA NEM bizonyít", "",
          "- Valós pánt/sín kinematika, kábelpálya, LED-profilok és a 32 segédobjektum ütközése (csak a 120 fő alkatrész tömör geometriája).",
          "- Ajtónyitás (pánttípus és -oldal nincs véglegesítve) – 2. fázis gyári CLIP top geometriával.",
          "- Lapméret és élanyag: becsült értékek a `gyartasi_szabalyok_v1.json`-ból, termék nincs kiválasztva.",
          "- Gépi ütköztetés, nullpont, él-kód sorrend: az asztalos konvenciójának megerősítéséig javaslat.",
          "- Helyszíni felmérés nincs; a méretlánc tervi."]
    out_md.write_text("\n".join(L) + "\n", encoding="utf-8")
    return cnt


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--parts", default=str(HERE / "parts_v1.json"))
    ap.add_argument("--out", default=str(HERE / "qa_report"))
    a = ap.parse_args(argv)
    doc, qa, meta = run(Path(a.parts))
    cnt = write_report(doc, qa, meta, Path(a.out + ".md"), Path(a.out + ".json"))
    print(f"QA: {dict(cnt)}")
    return 2 if cnt.get("BLOKKOLO") else 0


if __name__ == "__main__":
    sys.exit(main())
