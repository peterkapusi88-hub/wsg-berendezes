#!/usr/bin/env python3
"""S16 F1 – R14 parts.json → gyártási adatmodell (parts_v1.json + parts_v1.csv).

Bemenet: forras_R14/ (változatlan R14 másolat, SHA-256-tal) + gyartasi_szabalyok_v1.json.
Kimenet: parts_v1.json (egyetlen igazság-forrás a gyártási réteghez), parts_v1.csv (gyors nézet).

Futtatás:  python3 build_parts_v1.py
Függőségek: numpy, trimesh, shapely, manifold3d (pip install --break-system-packages ...)

A parts_v1.json-t kézzel NEM szerkesztjük: minden változás a szabályfájlban vagy az R14 geometriában történik,
és a szkript újrafuttatásával kerül át.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from s16_geom import (IRANY_NEV, LocalFrame, build_solid, load_json, neg,  # noqa: E402
                      sha256)

import os
SRC = HERE / os.environ.get("S16_FORRAS", "forras_R15" if (HERE / "forras_R15").is_dir() else "forras_R14")
RULES = HERE / "gyartasi_szabalyok_v1.json"
OUT_JSON = HERE / "parts_v1.json"
OUT_CSV = HERE / "parts_v1.csv"

MODEL_REV = "S16-R15-GY-v1" if SRC.name == "forras_R15" else "S16-GY-F1-v1"


def modul_of(pid: str) -> str:
    m = re.match(r"^(D[1-6])-", pid)
    if m:
        return m.group(1)
    for pre, mod in (("T-", "TORONY"), ("TEXTILE", "TORONY"), ("BG-", "HATTER"), ("BATTEN", "HATTER"),
                     ("FRAME-T", "TORONY_KERET"), ("CURVE-T", "TORONY_KERET"), ("FRAME-B", "ALSO_KERET"),
                     ("CURVE-B", "ALSO_KERET"), ("TV-", "TV")):
        if pid.startswith(pre):
            return mod
    return "EGYEB"


def cimke_id(pid: str, rules) -> str:
    s = re.sub(r"[^A-Z0-9_-]", "_", pid.upper())
    return f"{rules['cimke_azonosito']['elotag']}_{s}"


def mozgo_egysegek(drawers):
    m = {}
    for d in drawers:
        for pid in d["moving"]:
            m[pid] = f"{d['id']}-FIOK"
    for pid in ("T-DOOR-L", "TEXTILE", "T-DOOR-L-BACK"):
        m[pid] = "T-AJTO-BAL"
    m["T-DOOR-R"] = "T-AJTO-JOBB"
    return m


def a_normal_for(part, rules):
    exc = rules["a_oldal"]["kivetelek"].get(part["id"])
    if exc:
        return exc["irany"]
    return rules["a_oldal"]["alapertelmezes_tengely_szerint"][part["axis"]]


def r14_grain_to_local(grain: str):
    g = (grain or "").lower()
    if g.startswith("v"):
        return "V"
    if g.startswith("u"):
        return "U"
    return None


def edge_roles(pid, frame, solids, rules, moving):
    """Élenként: szomszéd-érintkezés (a többi zárt testtel), irány, szerep."""
    tol = rules["elszabalyok"]["erintkezes_tures_mm"]
    thr = rules["elszabalyok"]["erintkezes_kuszob_arany"]
    me_unit = moving.get(pid)
    out = {}
    for e, gdir in frame.edge_dirs().items():
        length, pts = frame.edge_samples(e, offset=tol)
        hit = np.zeros(len(pts), bool)
        neigh = {}
        lo, hi = pts.min(0) - 1, pts.max(0) + 1
        for oid, s in solids.items():
            if oid == pid:
                continue
            if not (np.all(s.lo < hi) and np.all(lo < s.hi)):
                continue
            # mozgó egység nem "csatlakozik" a vázhoz (pl. front a kerethez) – csak saját egységén belül
            if moving.get(oid) != me_unit and (me_unit or moving.get(oid)):
                continue
            c = s.contains(pts)
            if c.any():
                neigh[oid] = round(float(c.mean()), 3)
                hit |= c
        frac = float(hit.mean())
        if frac >= thr:
            szerep = "CSATLAKOZO"
        elif gdir == "+Y":
            szerep = "SZABAD_ELOL"
        else:
            szerep = "SZABAD_EGYEB"
        out[e] = {
            "el": e, "helyi": {"E1": "V=0", "E2": "U=max", "E3": "V=max", "E4": "U=0"}[e],
            "globalis_irany": gdir, "irany_nev": IRANY_NEV[gdir], "hossz_mm": round(length, 2),
            "szerep": szerep, "erintkezes_arany": round(frac, 3),
            "szomszedok": dict(sorted(neigh.items(), key=lambda kv: -kv[1])),
        }
    return out


def edge_sign(part, edge, rules):
    """Él-jel + opcionális élanyag-felülírás + indok."""
    szerep, gdir = edge["szerep"], edge["globalis_irany"]
    exc = rules["elszabalyok"]["id_kivetelek"].get(part["id"], {})
    if szerep in exc:
        return exc[szerep], None, exc.get("ok")
    for r in rules["elszabalyok"].get("irany_felulbiralas", []):
        if part["material"] not in r["anyag"] or gdir != r["irany"] or szerep not in r["szerep"]:
            continue
        if r.get("ha_mezo") and not part.get(r["ha_mezo"]):
            continue
        if "also_sik_z" in r and abs(part["box"][2] - r["also_sik_z"]) > 0.01:
            continue
        jel = r["jel"]
        if part["material"] == "M02" and jel == "V":
            jel = "F"
        return jel, r["elanyag"], r["ok"]
    return rules["elszabalyok"]["anyag"][part["material"]][szerep], None, None


def contour_info(part):
    o = part.get("outline")
    if not o:
        return {"van": False}
    a = np.asarray(o, float)
    per = float(np.sum(np.linalg.norm(np.diff(np.vstack([a, a[:1]]), axis=0), axis=1)))
    mn, mx = a.min(0), a.max(0)
    return {"van": True, "pontok": len(o), "kerulet_mm": round(per, 1),
            "bbox_uv": [round(float(mn[0]), 3), round(float(mn[1]), 3), round(float(mx[0]), 3), round(float(mx[1]), 3)],
            "geometria": f"{SRC.name}/parts.json#{part['id']}.outline"}


def operations(part, frame, drawers_by_front):
    ops = []
    pid = part["id"]

    def side_of(globalis_irany):
        return "A" if frame.a_normal == globalis_irany else ("B" if frame.a_normal == neg(globalis_irany) else "?")
    if part.get("outline"):
        ops.append({"op": "KONTUR_MARAS", "oldal": "A", "melyseg": "atmeno",
                    "geometria": f"{SRC.name}/parts.json#{pid}.outline", "szerszam": None,
                    "statusz": "NYITOTT – szerszámtábla hiányzik"})
    for i, c in enumerate(part.get("cutouts", [])):
        a = np.asarray(c["outline"], float)
        ops.append({"op": "ATMENO_KIVAGAS", "oldal": "A", "melyseg": "atmeno",
                    "bbox_uv": [*a.min(0).round(3).tolist(), *a.max(0).round(3).tolist()],
                    "geometria": f"{SRC.name}/parts.json#{pid}.cutouts[{i}].outline",
                    "megjegyzes": c.get("note", ""), "szerszam": None,
                    "statusz": "NYITOTT – szerszámtábla hiányzik"})
    if part.get("assembly_rebate"):
        lb = frame.box_to_local(part["assembly_rebate"])
        n0, n1 = max(lb["n"][0], 0.0), min(lb["n"][1], frame.T)
        ops.append({"op": "KIMETSZES" if (n0 <= 0 and n1 >= frame.T) else "FALC",
                    "oldal": "A" if n1 >= frame.T else "B", "helyi_doboz": lb,
                    "melyseg_mm": round(n1 - n0, 3), "forras": "R14 assembly_rebate (globális doboz)",
                    "megjegyzes": part.get("note", ""), "szerszam": None, "statusz": "NYITOTT – szerszámtábla hiányzik"})
    if part.get("edge_light_pocket"):
        p = part["edge_light_pocket"]
        lb = frame.box_to_local(p["box_mm"])
        ops.append({"op": "FENYCSATORNA_FALC", "oldal": "A", "helyi_doboz": lb,
                    "melyseg_mm": p.get("depth_mm"), "maradek_mm": p.get("rear_remaining_mm"),
                    "megjegyzes": p.get("note", ""), "szerszam": None, "statusz": "NYITOTT – LED-profil kiválasztása után"})
    if part.get("rear_light_rebate"):
        r = part["rear_light_rebate"]
        a = np.asarray(r["outline_xz_mm"], float)
        # globális X,Z → helyi U,V (A=+Y nézet: U=X-x0, V=Z-z0)
        x0, z0 = part["box"][0], part["box"][2]
        y0 = part["box"][1]
        ops.append({"op": "HATSO_FENYFALC", "oldal": "B",
                    "bbox_uv": [round(float(a[:, 0].min() - x0), 3), round(float(a[:, 1].min() - z0), 3),
                                round(float(a[:, 0].max() - x0), 3), round(float(a[:, 1].max() - z0), 3)],
                    "melyseg_mm": round(r["y_mm"][1] - r["y_mm"][0], 3),
                    "n_tartomany": [round(r["y_mm"][0] - y0, 3), round(r["y_mm"][1] - y0, 3)],
                    "perem_mm": r.get("lip_mm"),
                    "geometria": f"{SRC.name}/parts.json#{pid}.rear_light_rebate.outline_xz_mm (globális X,Z)",
                    "szerszam": None, "statusz": "NYITOTT – LED-profil kiválasztása után"})
    if part.get("recess_opening"):
        ops.append({"op": "SULLYESZTETT_KAZETTA_NYILAS", "oldal": "A",
                    "geometria": f"{SRC.name}/parts.json#{pid}.recess_opening",
                    "megjegyzes": "azonos a cutouts[0] átmenő kivágással – egyszer gyártandó",
                    "szerszam": None, "statusz": "NYITOTT"})
    # vasalat – csak az R14-ben megnevezett rendszer, koordináta nélkül (nincs kitalált furatkép)
    d = drawers_by_front.get(pid)
    if d:
        ops.append({"op": "FRONTRÖGZÍTÉS_FURAT", "oldal": "B", "vasalat": d["runner"], "nyito": d["tipon"],
                    "koordinatak": None, "statusz": "NYITOTT – Blum gyári furatkép + pontos cikkszám kell"})
    if re.match(r"^D[1-6]-(L|R)$", pid):
        belso = "+X" if pid.endswith("-L") else "-X"
        ops.append({"op": "SIN_RÖGZÍTÉS_FURAT", "oldal": side_of(belso), "belso_irany": belso,
                    "vasalat": "Blum MOVENTO 760H (R14 drawers.json)",
                    "koordinatak": None, "statusz": "NYITOTT – gyári furatkép"})
    if re.match(r"^D[1-6]-BOX-(L|R|H)$", pid):
        ops.append({"op": "SIN_KAPCSOLAT_MEGMUNKALAS", "oldal": "B", "vasalat": "Blum MOVENTO 760H + T51.7601",
                    "koordinatak": None, "statusz": "NYITOTT – hátfal-kivágás/furat a gyári adat szerint"})
    if pid in ("T-DOOR-L", "T-DOOR-R"):
        ops.append({"op": "PANTKEHELY", "oldal": "B", "vasalat": "Blum CLIP top (R14 megjegyzés: rugó nélküli, inset) – darabszám/variáns nyitott",
                    "koordinatak": None, "statusz": "NYITOTT – pánt variáns, darabszám, tömeg alapján"})
    if pid in ("T-L", "T-R"):
        belso = "+X" if pid == "T-L" else "-X"
        ops.append({"op": "PANTTALP_FURAT", "oldal": side_of(belso), "belso_irany": belso,
                    "vasalat": "Blum CLIP talp – variáns nyitott",
                    "koordinatak": None, "statusz": "NYITOTT – pántoldal (bal/jobb ajtó) R14-ben nincs rögzítve"})
    if pid == "T-C":
        ops.append({"op": "PANTTALP_FURAT", "oldal": "nyitott", "vasalat": "Blum CLIP talp – csak ha az ajtó a középosztóra pántolt",
                    "koordinatak": None, "statusz": "NYITOTT – pántoldal döntés"})
    return ops


def size_block(part, frame, codes, edges, mat, rules):
    L, W, T = part["L"], part["W"], part["T"]
    et = mat.get("elvastagsag") or 0.0
    pm = mat.get("elomaras_elenkent") or 0.0
    banded = {e: codes[e] == "V" for e in codes}
    # E2/E4 a hosszt (U), E1/E3 a szélességet (V) határolja
    elotti_L = L - et * (banded["E2"] + banded["E4"])
    elotti_W = W - et * (banded["E1"] + banded["E3"])
    nyers_L = nyers_W = None
    szabaly = None
    if mat.get("rahagyas_L") is not None:
        nyers_L = elotti_L + pm * (banded["E2"] + banded["E4"]) + mat["rahagyas_L"]
        nyers_W = elotti_W + pm * (banded["E1"] + banded["E3"]) + mat["rahagyas_W"]
        szabaly = (f"nyers = kész − élvastagság({et}) × élzárt él + előmarás({pm}) × élzárt él + ráhagyás"
                   f"({mat['rahagyas_L']}/{mat['rahagyas_W']})")
    if part.get("raw_L") is not None:
        nyers_L, nyers_W = part["raw_L"], part["raw_W"]
        szabaly = "R14 explicit raw_L/raw_W (forrásból átvéve – QA ellenőrzi)"
    return {
        "kesz": {"L": L, "W": W, "T": T},
        "elzaras_elotti": {"L": round(elotti_L, 2), "W": round(elotti_W, 2)},
        "nyers": {"L": None if nyers_L is None else round(nyers_L, 2), "W": None if nyers_W is None else round(nyers_W, 2)},
        "nyers_szabaly": szabaly,
        "r14_raw_rule": part.get("raw_rule"),
        "geometriabol": {"L": round(frame.L, 3), "W": round(frame.W, 3), "T": round(frame.T, 3)},
    }


def main():
    rules = load_json(RULES)
    parts = load_json(SRC / "parts.json")
    materials = {m[0]: m for m in load_json(SRC / "materials.json")}
    drawers = load_json(SRC / "drawers.json")
    zart = {o["name"]: o for o in load_json(next(SRC.glob("*_ZART_JELENET_MM.json")))["objects"]}
    moving = mozgo_egysegek(drawers)
    drawers_by_front = {d["front"]: d for d in drawers}

    solids = {p["id"]: build_solid(p, zart.get(p["id"])) for p in parts}
    nezetek = rules["koordinata_konvencio"]["nezetek"]
    gtipus = rules["gyartasi_tipus"]

    out_parts = []
    for p in parts:
        pid = p["id"]
        a_n = a_normal_for(p, rules)
        fr = LocalFrame(p["box"], a_n, nezetek)
        mat = rules["anyagok"][p["material"]]
        gt = gtipus["id"].get(pid) or gtipus.get(p["kind"]) or gtipus["alapertelmezes"]
        is_sheet = gt not in gtipus["nem_lap_tipusok"]
        edges = edge_roles(pid, fr, solids, rules, moving)
        codes = {}
        for e in edges:
            jel, anyag_felul, ok = edge_sign(p, edges[e], rules)
            codes[e] = jel
            edges[e]["jel"] = jel
            edges[e]["elanyag"] = anyag_felul or (mat["elanyag"] if jel == "V" else rules["el_kod_jelek"][jel])
            if ok:
                edges[e]["indok"] = ok
            edges[e]["elvastagsag_mm"] = mat.get("elvastagsag", 0.0) if codes[e] == "V" else 0.0
            edges[e]["gepi_utkozo"] = e in rules["gepi_utkozo"]["alapertelmezes"]
        felul_g = rules.get("alkatresz_anyag_felulbiralas", {}).get(pid, {})
        grain_ax = felul_g.get("szalirany") or r14_grain_to_local(p.get("grain"))
        grain_glob = None
        if grain_ax:
            grain_glob = fr.u_ax if grain_ax == "U" else fr.v_ax
        nyitott = []
        felul = rules.get("alkatresz_anyag_felulbiralas", {}).get(pid)
        if felul:
            nyitott.append(f"Anyagkivitel döntés: {felul['kivitel']} ({felul['dontes']}). Nyitott: {felul['nyitott']}.")
        if gt in ("IVES_SZERELVENY", "OSSZEALLITAS"):
            nyitott.append("Összeállítás – a 2. fázisban lapalkatrészekre/rétegekre bontandó; nem egy darab lap.")
        if p.get("outline"):
            nyitott.append("Kontúros alkatrész: az E1–E4 a befoglaló oldalait jelöli; ívelt élszakasz élzárása (min. rádiusz) műhelyi kérdés.")
        if solids[pid].method == "bbox":
            nyitott.append("Zárt test nem építhető – érintkezés/ütközés csak befoglalóval vizsgálva.")
        rec = {
            "id": pid,
            "cimke_id": cimke_id(pid, rules),
            "modell_revizio": MODEL_REV,
            "forras": {"r14_id": pid, "r14_revizio": p["revision"], "r14_kind": p["kind"]},
            "modul": modul_of(pid),
            "megnevezes": p["name"],
            "gyartasi_tipus": gt,
            "lap_alkatresz": is_sheet,
            "db": 1,
            "mozgo_egyseg": moving.get(pid),
            "anyag": {"kod": p["material"], "megnevezes": materials[p["material"]][1],
                      "tipus": mat["tipus"], "nevleges_vastagsag": mat["nevleges_vastagsag"],
                      "latszo_felso_felulet": p.get("exposed_top_finish"),
                      "alternativak": p.get("material_alternatives"),
                      "kivitel": felul["kivitel"] if felul else None},
            "meret": size_block(p, fr, codes, edges, mat, rules),
            "befoglalo_globalis": p["box"],
            "helyi_rendszer": {
                "A_normal": a_n, "U": fr.u_ax, "V": fr.v_ax, "N": fr.n_ax,
                "nullpont_globalis": [round(float(c), 3) for c in fr.origin],
                "leiras": nezetek[a_n]["leiras"],
            },
            "lapoldal": {"A": f"{a_n} ({IRANY_NEV[a_n]})", "B": f"{neg(a_n)} ({IRANY_NEV[neg(a_n)]})"},
            "elek": edges,
            "el_kod": "".join(codes[e] for e in ("E1", "E2", "E3", "E4")),
            "gepi_utkozo": rules["gepi_utkozo"]["alapertelmezes"],
            "szalirany": {"r14": p.get("grain"), "helyi_tengely": grain_ax, "globalis": grain_glob, "felulbiralva": felul_g.get("dontes")},
            "kontur": contour_info(p),
            "muveletek": operations(p, fr, drawers_by_front),
            "geometria_forras": solids[pid].method,
            "r14_megjegyzes": p.get("note", ""),
            "statusz": "TERVI ADATMODELL – nem gyártási kiadás",
            "nyitott": nyitott,
        }
        out_parts.append(rec)

    aux = []
    for name, o in zart.items():
        if o["role"] == "primary_part":
            continue
        v = np.asarray(o["vertices_mm"], float)
        lo, hi = v.min(0), v.max(0)
        size = hi - lo
        n = name.upper()
        if o["role"] == "environment":
            kat = "KORNYEZET"
        elif "EMITTER" in n or "CONCEALED" in n or n.startswith("A8-") or n == "A2-UNDERSIDE" or float(size.min()) < 1e-6:
            kat = "FENYFORRAS_FELULET (render; valós LED-szalag/profil kiválasztandó)"
        elif n.startswith(("TV-SCREEN", "TV-CONSOLE", "PSU")):
            kat = "VASAROLT_KESZULEK / HELYFOGLALO"
        elif n.startswith("I-") or "HOUSING" in n or "DIFFUSER" in n:
            kat = "BELSO_LED_PROFIL (helyfoglaló – termék kiválasztandó)"
        else:
            kat = "GYARTANDO_TAKARO/TALCA (anyagjegyzékből hiányzik)"
        aux.append({"nev": name, "kategoria": kat, "befoglalo": [*lo.round(2).tolist(), *size.round(2).tolist()],
                    "render_lathato": o.get("render_visible")})

    doc = {
        "modell": "S16 R14 médiafal – gyártási adatmodell",
        "modell_revizio": MODEL_REV,
        "generalva": date.today().isoformat(),
        "generator": "build_parts_v1.py",
        "statusz": "TERVI ADATMODELL – nem gyártási kiadás; műhelyi konvenciók megerősítésre várnak",
        "forras": {
            "mappa": SRC.name,
            "git_ag": "execution/a902-s01-kyoto-ink-design-to-budget-20261026",
            "git_commit": "251457939478f0786ef04337a372c13418ef6dd4",
            "fajlok": {f.name: sha256(f) for f in sorted(SRC.glob("*.json"))},
            "szabalyfajl": {RULES.name: sha256(RULES)},
        },
        "koordinata_konvencio": rules["koordinata_konvencio"],
        "el_kod_jelek": rules["el_kod_jelek"],
        "alkatreszek": out_parts,
        "segedobjektumok_R14_jelenetbol": aux,
    }
    OUT_JSON.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    cols = ["cimke_id", "id", "modul", "megnevezes", "gyartasi_tipus", "lap", "anyag", "T", "kesz_L", "kesz_W",
            "elzaras_elotti_L", "elzaras_elotti_W", "nyers_L", "nyers_W", "szalirany", "A_oldal", "el_kod",
            "E1", "E2", "E3", "E4", "utkozo", "kontur", "muveletek", "mozgo"]
    with OUT_CSV.open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(cols)
        for r in out_parts:
            m = r["meret"]
            w.writerow([r["cimke_id"], r["id"], r["modul"], r["megnevezes"], r["gyartasi_tipus"],
                        "igen" if r["lap_alkatresz"] else "nem", r["anyag"]["kod"], m["kesz"]["T"], m["kesz"]["L"],
                        m["kesz"]["W"], m["elzaras_elotti"]["L"], m["elzaras_elotti"]["W"], m["nyers"]["L"],
                        m["nyers"]["W"], r["szalirany"]["helyi_tengely"] or "", r["helyi_rendszer"]["A_normal"],
                        r["el_kod"], *[f"{r['elek'][e]['jel']}:{r['elek'][e]['szerep']}" for e in ("E1", "E2", "E3", "E4")],
                        "+".join(r["gepi_utkozo"]), "igen" if r["kontur"]["van"] else "",
                        ",".join(o["op"] for o in r["muveletek"]), r["mozgo_egyseg"] or ""])
    print(f"OK: {len(out_parts)} alkatrész, {len(aux)} segédobjektum → {OUT_JSON.name}, {OUT_CSV.name}")


if __name__ == "__main__":
    main()
