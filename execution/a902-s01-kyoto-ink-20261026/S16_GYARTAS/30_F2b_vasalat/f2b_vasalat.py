#!/usr/bin/env python3
"""S16 F2b – vasalat- és furatterv a gyártási adatmodellből (parts_v1.json, R15).

Mit generál (vasalat_terv.json):
  • TIPLI Ø8×35 minden T-kötésnél (A él → B lap), a geometriából számolt kötésvonal mentén:
      élfurat Ø8×25 az A alkatrész élébe (vízszintes fúrás), lapfurat Ø8×12 a B lapjába.
  • POLCTARTÓ furatok Ø5×10 a torony polcai alatt (3 magasság: −32 / 0 / +32 mm), elöl-hátul 37 mm-re.
  • PÁNT (Blum CLIP top 110°, típus/variáns nyitott): kehely Ø35×13 az ajtó B oldalán, 2× Ø8 (45 / 9,5 mm kiosztás),
    talplemez-furatok a korpuszoldalon 37 mm-re az elülső éltől, ±16 mm (32-es rendszer) – polcütközés-kerüléssel.
  • Ellenőrzés: minden furat az alkatrészen belül, mélység < anyag, falvastagság a furat mögött ≥ 5 mm,
    kehely nem metsz kivágást/kontúrt; ami nem fér el, az BLOKKOLÓ (nem rajzoljuk be kitalált helyre).

Források (lekérve 2026-10-30): Blum CLIP top fúrási adatok – Ø35 kehely, B = 3–6 mm fúrási távolság, Ø8 / 45 mm / 9,5 mm
kiosztás: https://static.richelieu.com/documents/docsGr/100/759/9/1007599/1394958.pdf ; 13 mm kehelymélység, 37 mm / 32 mm
rendszer: Blum általános szerelési adat – a pontos cikkszám kiválasztása után a gyári sablonnal ellenőrizendő.
Becslés (paraméter, műhelyi megerősítésre): polctartó-furat a polc alsó síkja alatt 6 mm-rel, Ø5×10.
"""
from __future__ import annotations

import json
import math
import re
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
F1 = HERE.parent / "10_F1_adatmodell"
sys.path.insert(0, str(F1))
from s16_geom import AXIS_VEC, LocalFrame, load_json  # noqa: E402

P = {
    "tipli": {"d": 8.0, "el_melyseg": 25.0, "lap_melyseg": 13.0, "hossz": 35, "veg_tav": 32.0, "max_koz": 192.0,
              "min_el": 60.0, "forras": "etalon km.dwg CONNOBJ_DOWEL_D8_L35_13-24: Ø8, lapba 13, élbe 25 mm; 32-es rendszer"},
    "tipli_el_el": {"d": 8.0, "melyseg": 17.5, "hossz": 35, "forras": "él-él illesztés (egymásra ülő oldallapok): Ø8×35, 17,5/17,5 – Claude döntés"},
    "tipli_keret": {"d": 6.0, "melyseg": 15.0, "hossz": 30, "forras": "18×18 festett MDF keretlécek tompa illesztése: 1 db Ø6×30 bükk tipli + ragasztás – Claude döntés"},
    "minifix": {"haz_d": 15.0, "haz_melyseg": 12.5, "B": 24.0, "csatorna_d": 8.0, "csap_d": 5.0, "csap_melyseg": 11.0,
                "forras": "Häfele Minifix 15 (262.26.174, az asztalos km.dwg/coo1.dwg CONNOBJ_MINIFIX_D15_AV18_L24 blokkja); B = 24 mm; furatmélységek Häfele adatlap szerint ellenőrizendők"},
    "movento": {"sin_jelolo_d": 2.5, "sin_jelolo_m": 3.0, "sin_furatok_eloltol": [37.0, 165.0, 261.0], "sin_magassag_fiokoldal_alatt": 6.5,
                "horog_d": 6.0, "horog_m": 10.0, "horog_alulrol": 7.0, "horog_kulso_oldaltol": 11.0,
                "forras": "Blum MOVENTO szerelési útmutató (wwhardware.com movento-2016.pdf): hátsó horog Ø6×10, 7/11 mm; elülső hézag 3 mm; "
                          "csavarpozíciók A/B NL300-hoz (763.3050M: 165/261) + 37 mm elülső rendszerfurat; zár (T51.7601) és TIP-ON sablonnal (T65.1000.02 / T65.1600.01)"},
    "polc": {"d": 5.0, "melyseg": 10.0, "elol": 37.0, "hatul": 37.0, "z_eltolas": -6.0, "lepes": [-32, 0, 32],
             "forras": "becslés – a polctartó (etalon: de_11090) típusától függ"},
    "pant": {"kehely_d": 35.0, "kehely_melyseg": 13.0, "B": 3.0, "csavar_d": 8.0, "csavar_melyseg": 11.5,
             "csavar_koz": 45.0, "csavar_eltolas": 9.5, "talp_elol": 37.0, "talp_koz": 32.0, "talp_d": 5.0,
             "talp_melyseg": 12.0, "veg_tav": 100.0, "talp_magassag": 50.0, "talp_kiallas": 12.0,
             "cikkszam": "Blum CLIP top 110° rugó nélküli, inset, csavaros 70T3750", "talp_cikkszam": "Blum CLIP talplemez 0 mm 177H3100E",
             "forras": "Blum CLIP top: Ø35, B 3–6 mm, Ø8 45/9,5 (richelieu.com Blum adatlap); 13 mm mélység, 37/32 rendszer; "
                       "71T3750 = inset 110° csavaros (sfs.ch), 70T3750 = rugó nélküli (TIP-ON) változat; etalon km.dwg: 71T3750 + 177H3100E"},
    "min_maradek": 5.0,
}

# a tornyokban a polcok és oldalaik (R14 geometria szerint)
POLC_REKESZ = {"T-L-S": ("T-L", "T-C"), "T-R-S": ("T-C", "T-R")}
# ajtók: pántoldal (javaslat: pillangó nyitás – bal ajtó balra, jobb ajtó jobbra) és darabszám (R14 előirányzat)
AJTOK = {"T-DOOR-L": {"oldal": "-X", "korpusz": "T-L", "db": 6}, "T-DOOR-R": {"oldal": "+X", "korpusz": "T-R", "db": 5}}


def frame_of(rec, rules):
    return LocalFrame(rec["befoglalo_globalis"], rec["helyi_rendszer"]["A_normal"], rules["koordinata_konvencio"]["nezetek"])


def vec(ax):
    return AXIS_VEC[ax]


def hole(part, cel, kozep, irany, d, melyseg, funkcio, kapcsolat=None, **kw):
    return {"alkatresz": part, "cel": cel, "start": [round(float(c), 3) for c in kozep],
            "irany": [round(float(c), 6) for c in irany], "d": d, "melyseg": melyseg, "funkcio": funkcio,
            "kapcsolat": kapcsolat, **kw}


def local_of(fr, p):
    return [round(float(c), 3) for c in fr.to_local(p)]


def main():
    doc = load_json(F1 / "parts_v1.json")
    rules = load_json(F1 / "gyartasi_szabalyok_v1.json")
    src = {p["id"]: p for p in load_json(F1 / doc["forras"]["mappa"] / "parts.json")}
    R = {r["id"]: r for r in doc["alkatreszek"]}
    FR = {k: frame_of(r, rules) for k, r in R.items()}
    holes, hardware, kotesek, problems = [], [], [], []

    def ok_part(r):
        return (r["lap_alkatresz"] and r["anyag"]["kod"] in ("M01", "M02") and r["meret"]["kesz"]["T"] >= 15
                and not r["mozgo_egyseg"])

    konnektorok = []          # CAD-blokkok (az asztalos CONNOBJ-konvenciója): {blokk, P, X, Z, kapcsolat}
    modbox = {}
    for r in R.values():
        lo = np.array(r["befoglalo_globalis"][:3], float)
        hi = lo + np.array(r["befoglalo_globalis"][3:], float)
        m0, m1 = modbox.get(r["modul"], (lo, hi))
        modbox[r["modul"]] = (np.minimum(m0, lo), np.maximum(m1, hi))

    def inner_dir(r):
        """a lap belső (rekesz felé néző) normálisa: a lap közepétől a modul befoglalójának közepe felé"""
        n = vec(r["helyi_rendszer"]["N"])
        lo = np.array(r["befoglalo_globalis"][:3], float)
        c = lo + np.array(r["befoglalo_globalis"][3:], float) / 2
        mc = (modbox[r["modul"]][0] + modbox[r["modul"]][1]) / 2
        sgn = np.sign((mc - c) @ n) or 1.0
        return n * sgn

    def segment(fa, e, b):
        L, W = fa.L, fa.W
        if e in ("E1", "E3"):
            a0, a1, fix = 0.0, L, (0.0 if e == "E1" else W)
        else:
            a0, a1, fix = 0.0, W, (L if e == "E2" else 0.0)
        blo = np.array(b["befoglalo_globalis"][:3], float)
        bhi = blo + np.array(b["befoglalo_globalis"][3:], float)
        k = 0 if e in ("E1", "E3") else 1
        cand = sorted([fa.to_local(blo)[k], fa.to_local(bhi)[k]])
        return max(a0, cand[0]), min(a1, cand[1]), fix

    def at(fa, e, s, fix, t):
        return fa.to_global([s, fix, t] if e in ("E1", "E3") else [fix, s, t])

    seen = set()
    from s16_geom import build_solid as _bs, contains_robust
    _zo = {o["name"]: o for o in load_json(next((F1 / doc["forras"]["mappa"]).glob("*_ZART_JELENET_MM.json")))["objects"]}
    _sc = {}

    def SOL(pid):
        if pid not in _sc:
            _sc[pid] = _bs(src[pid], _zo.get(pid))
        return _sc[pid]
    for aid, a in R.items():
        if not ok_part(a):
            continue
        fa = FR[aid]
        for e, ed in a["elek"].items():
            if ed["szerep"] != "CSATLAKOZO":
                continue
            d = vec(ed["globalis_irany"])
            for bid, frac in ed["szomszedok"].items():
                b = R.get(bid)
                if frac < 0.3 or not b:
                    continue
                shell = (b["gyartasi_tipus"] == "IVES_SZERELVENY" and b["anyag"]["kod"] == "M02")
                if not ok_part(b) and not shell:
                    kotesek.append({"A": aid, "el": e, "B": bid, "tipus": "NEM_TIPLIS",
                                    "ok": f"B ({b['gyartasi_tipus']}, {b['anyag']['kod']}) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés"})
                    continue
                s0, s1, fix = segment(fa, e, b)
                length = s1 - s0
                T = fa.T
                edge_edge = (not shell) and abs(abs(vec(b["helyi_rendszer"]["N"]) @ d) - 1) > 1e-6
                if edge_edge:
                    key = frozenset((aid, bid))
                    if key in seen:
                        continue
                    seen.add(key)
                    lec = max(min(a["meret"]["kesz"]["L"], a["meret"]["kesz"]["W"]), 0) <= 20 or min(b["meret"]["kesz"]["L"], b["meret"]["kesz"]["W"]) <= 20
                    tp = P["tipli_keret"] if lec else P["tipli_el_el"]
                    if lec:
                        pos = [(s0 + s1) / 2]
                    else:
                        tt = P["tipli"]
                        n = max(2, math.ceil((length - 2 * tt["veg_tav"]) / tt["max_koz"]) + 1)
                        pos = list(np.linspace(s0 + tt["veg_tav"], s1 - tt["veg_tav"], n))
                    for k, s_ in enumerate(pos):
                        pt = at(fa, e, s_, fix, T / 2)
                        tag = f"{aid}:{e}:{bid}:EE{k}"
                        # íves/kontúros darabnál a furat ne fusson ki: a mélység a testen belül maradó legnagyobb (min. 8 mm)
                        mb = tp["melyseg"]
                        sb = SOL(bid)
                        while mb >= 8 and not contains_robust(sb, np.array(pt) + d * np.arange(0.5, mb + 0.01, 0.5)[:, None]).all():
                            mb -= 1.0
                        if mb < 8:
                            problems.append({"sulyossag": "FIGYELMEZTETES", "alkatresz": bid, "uzenet": f"{tag}: tipli nem fér a kontúros darabba – ragasztott illesztés"})
                            continue
                        holes.append(hole(aid, f"él {e}", pt, -d, tp["d"], tp["melyseg"], "TIPLI_EL", tag, helyi=local_of(fa, pt)))
                        holes.append(hole(bid, "él", pt, d, tp["d"], mb, "TIPLI_EL", tag, helyi=local_of(FR[bid], pt)))
                        nm = f"TIPLI_D{tp['d']:.0f}x{tp['hossz']}"
                        hardware.append({"tipus": nm, "cikkszam": f"Ø{tp['d']:.0f}×{tp['hossz']} bordás bükk tipli (él-él)",
                                         "pozicio": [round(float(c), 3) for c in pt], "irany": [float(c) for c in d], "kapcsolat": tag,
                                         "geometria": {"d": tp["d"], "hossz": tp["hossz"], "el_melyseg": tp["melyseg"], "lap_melyseg": tp["melyseg"]}})
                        konnektorok.append({"blokk": f"CONNOBJ_DOWEL_D{tp['d']:.0f}_L{tp['hossz']}_EL", "P": pt.tolist(), "X": (-d).tolist(),
                                            "Z": None, "kapcsolat": tag, "melyseg": [tp["melyseg"], tp["melyseg"]], "d": tp["d"]})
                    kotesek.append({"A": aid, "el": e, "B": bid, "tipus": "TIPLI_EL_EL" + ("_KERETLEC" if lec else ""), "db": len(pos),
                                    "szakasz_mm": round(float(length), 1), "ok": tp["forras"]})
                    continue
                tp = P["tipli"]
                if length < tp["min_el"]:
                    problems.append({"sulyossag": "FIGYELMEZTETES", "alkatresz": aid, "uzenet": f"{e}→{bid}: kötésszakasz {length:.0f} mm < {tp['min_el']} – tipli nem fér, egyedi kötés"})
                    continue
                n = max(2, math.ceil((length - 2 * tp["veg_tav"]) / tp["max_koz"]) + 1)
                pos = np.linspace(s0 + tp["veg_tav"], s1 - tp["veg_tav"], n)
                for k, s_ in enumerate(pos):
                    pt = at(fa, e, s_, fix, T / 2)
                    tag = f"{aid}:{e}:{bid}:{k}"
                    holes.append(hole(aid, f"él {e}", pt, -d, tp["d"], tp["el_melyseg"], "TIPLI_EL", tag,
                                      helyi=local_of(fa, pt)))
                    holes.append(hole(bid, "lap", pt, d, tp["d"], tp["lap_melyseg"], "TIPLI_LAP", tag,
                                      helyi=local_of(FR[bid], pt)))
                    hardware.append({"tipus": "TIPLI_D8x35", "cikkszam": "Ø8×35 bordás tipli (etalon: CONNOBJ_DOWEL_D8_L35_13-24)",
                                     "pozicio": [round(float(c), 3) for c in pt], "irany": [float(c) for c in d], "kapcsolat": tag,
                                     "geometria": {"d": 8, "hossz": 35, "el_melyseg": tp["el_melyseg"], "lap_melyseg": tp["lap_melyseg"]}})
                    konnektorok.append({"blokk": "CONNOBJ_DOWEL_D8_L35_13-24", "P": pt.tolist(), "X": (-d).tolist(), "Z": None, "kapcsolat": tag,
                                        "melyseg": [tp["lap_melyseg"], tp["el_melyseg"]], "d": 8.0})
                kot = {"A": aid, "el": e, "B": bid, "tipus": "TIPLI", "db": int(n), "szakasz_mm": round(float(length), 1)}
                if shell:
                    # íves héjhoz: tipli + 2 Minifix 15 (bontható, a héj külső felülete érintetlen)
                    mp = P["minifix"]
                    nin = inner_dir(a)
                    mpos = []
                    for f_ in (0.25, 0.75):
                        sm = s0 + f_ * length
                        while any(abs(sm - q) < 22 for q in pos):
                            sm += 11
                        mpos.append(sm)
                    for k, sm in enumerate(mpos):
                        tag = f"{aid}:{e}:{bid}:MF{k}"
                        jp = at(fa, e, sm, fix, T / 2)                        # kötési sík, lapközép
                        hz = jp - d * mp["B"] + nin * (T / 2)                 # ház a belső lapon, B=24 mm a kötési síktól
                        holes.append(hole(aid, "lap (belső)", hz, -nin, mp["haz_d"], mp["haz_melyseg"], "MINIFIX_HAZ", tag, helyi=local_of(fa, hz)))
                        holes.append(hole(aid, f"él {e}", jp, -d, mp["csatorna_d"], mp["B"] + 1.0, "MINIFIX_CSATORNA", tag, helyi=local_of(fa, jp)))
                        holes.append(hole(bid, "héj belső lap", jp, d, mp["csap_d"], mp["csap_melyseg"], "MINIFIX_CSAP", tag, helyi=local_of(FR[bid], jp)))
                        hardware.append({"tipus": "MINIFIX_15", "cikkszam": "Häfele Minifix 15 ház 262.26.174 + csap (GEN_MFX_BOLT_24x5)",
                                         "pozicio": [round(float(c), 3) for c in hz], "irany": (-nin).tolist(), "kapcsolat": tag})
                        konnektorok.append({"blokk": "CONNOBJ_MINIFIX_D15_AV18_L24", "P": jp.tolist(), "X": (-d).tolist(), "Z": (-nin).tolist(),
                                            "kapcsolat": tag, "T": T})
                    kot.update({"tipus": "TIPLI+MINIFIX", "minifix": len(mpos), "ok": "íves héj: tipli + 2 Minifix 15 (bontható, rejtett) + ragasztás – Claude döntés"})
                kotesek.append(kot)

    # ---------------------------------------------------------------- 2. polctartó furatok
    pp = P["polc"]
    for pre, (lid, rid) in POLC_REKESZ.items():
        shelves = [r for k, r in R.items() if re.fullmatch(re.escape(pre) + r"\d+", k)]
        for s in shelves:
            x, y, z, dx, dy, dz = s["befoglalo_globalis"]
            for side_id, into in ((lid, "-X"), (rid, "+X")):
                side = R[side_id]
                sx0 = side["befoglalo_globalis"][0]
                sx1 = sx0 + side["befoglalo_globalis"][3]
                fx = sx1 if into == "-X" else sx0   # a rekesz felé néző lapsík
                for yy in (y + dy - pp["elol"], y + pp["hatul"]):
                    for dzz in pp["lepes"]:
                        zz = z + pp["z_eltolas"] + dzz
                        pt = np.array([fx, yy, zz])
                        dirv = vec(into)
                        holes.append(hole(side_id, "lap", pt, dirv, pp["d"], pp["melyseg"], "POLCTARTO", s["id"],
                                          helyi=local_of(FR[side_id], pt)))
                hardware.append({"tipus": "POLCTARTO", "cikkszam": "polctartó Ø5 csap – cikkszám az asztalostól (a de_11090 az etalonban konfirmát-jelölő)",
                                 "pozicio": [fx, y + dy / 2, z], "kapcsolat": s["id"], "db": 2})

    # ---------------------------------------------------------------- 3. pántok
    hp = P["pant"]
    shelf_z = sorted((r["befoglalo_globalis"][2], r["befoglalo_globalis"][2] + r["befoglalo_globalis"][5]) for k, r in R.items()
                     if re.fullmatch(r"T-[LR]-S\d+", k))
    for did, cfg in AJTOK.items():
        door = R[did]
        sd = src[did]
        x, y, z, dx, dy, dz = door["befoglalo_globalis"]
        hinge_x_edge = x if cfg["oldal"] == "-X" else x + dx
        sign = 1 if cfg["oldal"] == "-X" else -1           # a pántoldali éltől befelé
        cup_cx = hinge_x_edge + sign * (hp["B"] + hp["kehely_d"] / 2)
        # kivágás-ütközés: a kehely ne nyúljon a kivágásba / a kontúron kívülre
        from shapely.geometry import Point, Polygon
        from s16_geom import largest_polygon
        door_poly = largest_polygon(Polygon(sd["outline"])) if sd.get("outline") else None
        cut_polys = [largest_polygon(Polygon(c["outline"])) for c in sd.get("cutouts", [])]
        # az ajtó hátoldalára szerelt alkatrészek (pl. kazettahát) lenyomata az ajtó helyi U,V síkjában
        back_polys = []
        for oid, osrc in src.items():
            ob = osrc["box"]
            if oid == did or abs((ob[1] + ob[4]) - y) > 0.5:
                continue
            if ob[0] < x + dx and ob[0] + ob[3] > x and ob[2] < z + dz and ob[2] + ob[5] > z:
                pl = (Polygon([(a + ob[0] - x, b + ob[2] - z) for a, b in osrc["outline"]]) if osrc.get("outline") and osrc.get("axis") == "y"
                      else Polygon([(ob[0] - x, ob[2] - z), (ob[0] + ob[3] - x, ob[2] - z), (ob[0] + ob[3] - x, ob[2] + ob[5] - z), (ob[0] - x, ob[2] + ob[5] - z)]))
                back_polys.append((oid, largest_polygon(pl)))
        n = cfg["db"]
        vs = list(np.linspace(hp["veg_tav"], dz - hp["veg_tav"], n))
        corpus = R[cfg["korpusz"]]
        cx0 = corpus["befoglalo_globalis"][0]
        cface = cx0 + corpus["befoglalo_globalis"][3] if cfg["oldal"] == "-X" else cx0
        front_y = corpus["befoglalo_globalis"][1] + corpus["befoglalo_globalis"][4]
        placed = 0
        h0, w0 = len(holes), len(hardware)
        door_blocked = False
        pending = []
        for v in vs:
            # polcütközés kerülése (polc ±32 mm állíthatóság + talplemez fél magassága)
            gz = z + v
            for shift in (0, 32, -32, 64, -64, 96, -96):
                zz = gz + shift
                clear = all(not (lo - 32 - hp["talp_magassag"] / 2 - 5 < zz < hi + 32 + hp["talp_magassag"] / 2 + 5) for lo, hi in shelf_z)
                if clear and hp["veg_tav"] - 1 <= zz - z <= dz - hp["veg_tav"] + 1:
                    gz = zz
                    break
            else:
                problems.append({"sulyossag": "HIBA", "alkatresz": did, "uzenet": f"pánt v≈{v:.0f}: nem található polcütközés-mentes hely ±96 mm-en belül"})
            u = cup_cx - x
            vloc = gz - z
            cup = Point(u, vloc).buffer(hp["kehely_d"] / 2 + 1.0)
            bad = []
            if door_poly is not None and not door_poly.contains(cup):
                bad.append("kilóg a front kontúrjából")
            for cp in cut_polys:
                if cp.intersects(cup):
                    bad.append(f"metszi az átmenő kivágást (keretszár {cp.bounds[0]:.0f} mm széles a pántoldalon)")
            for oid, bp in back_polys:
                if bp.intersects(Point(u, vloc).buffer(hp["kehely_d"] / 2 + 2.0)):
                    bad.append(f"ütközik az ajtó hátoldali alkatrészével ({oid}, {bp.bounds[0]:.0f} mm-től)")
            if bad:
                door_blocked = True
                problems.append({"sulyossag": "BLOKKOLO", "alkatresz": did,
                                 "uzenet": f"Ø{hp['kehely_d']:.0f} pántkehely (B={hp['B']} mm) a z={gz:.0f} pozícióban: " + "; ".join(sorted(set(bad))) +
                                 " – szabványos CLIP top nem építhető be; keskeny keretes / csapos (pivot) pánt vagy szerkezetváltás kell"})
                continue
            # kehely + 2 csavar/dűbel furat az ajtó B oldalán (+Y irányba fúrva, y = front hátsó síkja)
            yb = y
            cup_pt = np.array([cup_cx, yb, gz])
            tag = f"{did}:PANT:{placed}"
            holes.append(hole(did, "B oldal", cup_pt, vec("+Y"), hp["kehely_d"], hp["kehely_melyseg"], "PANTKEHELY", tag, helyi=local_of(FR[did], cup_pt)))
            for s in (-1, 1):
                sp = np.array([cup_cx + sign * hp["csavar_eltolas"], yb, gz + s * hp["csavar_koz"] / 2])
                holes.append(hole(did, "B oldal", sp, vec("+Y"), hp["csavar_d"], hp["csavar_melyseg"], "PANT_DUBEL", tag, helyi=local_of(FR[did], sp)))
            # talplemez a korpuszoldalon: 37 mm-re az elülső éltől, ±16 mm
            into = "+X" if cfg["oldal"] == "-X" else "-X"
            for s in (-1, 1):
                tp_pt = np.array([cface, front_y - hp["talp_elol"], gz + s * hp["talp_koz"] / 2])
                holes.append(hole(cfg["korpusz"], "lap", tp_pt, -vec(into),
                                  hp["talp_d"], hp["talp_melyseg"], "PANTTALP", tag, helyi=local_of(FR[cfg["korpusz"]], tp_pt)))
            hardware.append({"tipus": "PANT_CLIPTOP_110", "cikkszam": hp["cikkszam"], "talp_cikkszam": hp["talp_cikkszam"],
                             "pozicio": [round(float(c), 3) for c in cup_pt], "ajto": did, "korpusz": cfg["korpusz"], "kapcsolat": tag})
            placed += 1
        if door_blocked:
            del holes[h0:]
            del hardware[w0:]
            placed = 0
        if placed < n:
            problems.append({"sulyossag": "BLOKKOLO" if placed == 0 else "HIBA", "alkatresz": did,
                             "uzenet": f"{placed}/{n} pánt helyezhető el szabványos CLIP top-pal"})

    # ---------------------------------------------------------------- 3b. fiók: Blum MOVENTO sín-jelölőfuratok + hátsó horog, vasalat-tételek
    mv = P["movento"]
    dfile = F1 / doc["forras"]["mappa"] / "drawers.json"
    for dr in (load_json(dfile) if dfile.exists() else []):
        m = dr["id"]
        sl, sr, bl, br = R.get(f"{m}-L"), R.get(f"{m}-R"), R.get(f"{m}-BOX-L"), R.get(f"{m}-BOX-R")
        if not (sl and sr and bl and br):
            continue
        front = sl["befoglalo_globalis"][1] + sl["befoglalo_globalis"][4]
        zb = bl["befoglalo_globalis"][2]
        for side, into in ((sl, "-X"), (sr, "+X")):
            fx = side["befoglalo_globalis"][0] + (side["befoglalo_globalis"][3] if into == "-X" else 0.0)
            zs = zb - mv["sin_magassag_fiokoldal_alatt"]
            if not (side["befoglalo_globalis"][2] + 8 <= zs <= side["befoglalo_globalis"][2] + side["befoglalo_globalis"][5] - 8):
                problems.append({"sulyossag": "HIBA", "alkatresz": side["id"],
                                 "uzenet": f"{m} sín (Z≈{zs:.0f}) a korpuszoldal ({side['id']}, Z {side['befoglalo_globalis'][2]}…) alatt van – a sín az íves sarokelemre esne: "
                                           "szerelőléc/távtartó vagy a korpuszoldal lefelé hosszabbítása kell (DÖNTÉS)"})
                continue
            for k, dy in enumerate(mv["sin_furatok_eloltol"]):
                pt = np.array([fx, front - dy, zb - mv["sin_magassag_fiokoldal_alatt"]])
                holes.append(hole(side["id"], "lap (belső)", pt, vec(into), mv["sin_jelolo_d"], mv["sin_jelolo_m"], "MOVENTO_SIN_JELOLO",
                                  f"{m}:SIN:{side['id']}:{k}", helyi=local_of(FR[side["id"]], pt)))
        for box, sgn in ((bl, 1), (br, -1)):
            x0 = box["befoglalo_globalis"][0] if sgn > 0 else box["befoglalo_globalis"][0] + box["befoglalo_globalis"][3]
            pt = np.array([x0 + sgn * mv["horog_kulso_oldaltol"], box["befoglalo_globalis"][1], box["befoglalo_globalis"][2] + mv["horog_alulrol"]])
            holes.append(hole(box["id"], "hátsó él", pt, vec("+Y"), mv["horog_d"], mv["horog_m"], "MOVENTO_HOROG", f"{m}:HOROG:{box['id']}",
                              helyi=local_of(FR[box["id"]], pt)))
        # fiókdoboz-kötés (15 mm nyír rétegelt): az oldalon át csavar az elő/hátlap végébe és a fenék élébe
        #   oldal: Ø4,5 átmenő (süllyesztve), a fogadó darab végében Ø2,5×20 előfúrás – az R16 fiókjaival azonos rendszer
        fb = R.get(f"{m}-BOX-B")
        for box, sgn in ((bl, 1), (br, -1)):
            bx = box["befoglalo_globalis"]
            xo = bx[0] if sgn > 0 else bx[0] + bx[3]          # külső lapsík
            xi = bx[0] + bx[3] if sgn > 0 else bx[0]          # belső lapsík
            into = vec("+X") * sgn
            for rid in (f"{m}-BOX-F", f"{m}-BOX-H"):
                r_ = R.get(rid)
                if not r_:
                    continue
                rb = r_["befoglalo_globalis"]
                yc = rb[1] + rb[4] / 2
                for f_ in (0.25, 0.75):
                    zc = rb[2] + rb[5] * f_
                    tag = f"{m}:DOBOZ:{box['id']}:{rid}:{f_}"
                    holes.append(hole(box["id"], "lap (külső)", np.array([xo, yc, zc]), into, 4.5, bx[3], "FIOK_DOBOZ_CSAVAR_ATMENO", tag,
                                      atmeno=True, helyi=local_of(FR[box["id"]], np.array([xo, yc, zc]))))
                    holes.append(hole(rid, "él (vég)", np.array([xi, yc, zc]), into, 2.5, 20.0, "FIOK_DOBOZ_CSAVAR_ELOFURAS", tag,
                                      helyi=local_of(FR[rid], np.array([xi, yc, zc]))))
                    hardware.append({"tipus": "CSAVAR_4x35", "cikkszam": "faforgácscsavar 4×35 süllyesztett fejű (fiókdoboz)", "kapcsolat": tag, "db": 1})
            if fb:
                fbb = fb["befoglalo_globalis"]
                zc = fbb[2] + fbb[5] / 2
                for f_ in (0.2, 0.5, 0.8):
                    yc = fbb[1] + fbb[4] * f_
                    tag = f"{m}:FENEK:{box['id']}:{f_}"
                    holes.append(hole(box["id"], "lap (külső)", np.array([xo, yc, zc]), into, 4.5, bx[3], "FIOK_DOBOZ_CSAVAR_ATMENO", tag,
                                      atmeno=True, helyi=local_of(FR[box["id"]], np.array([xo, yc, zc]))))
                    holes.append(hole(fb["id"], "él", np.array([xi, yc, zc]), into, 2.5, 20.0, "FIOK_DOBOZ_CSAVAR_ELOFURAS", tag,
                                      helyi=local_of(FR[fb["id"]], np.array([xi, yc, zc]))))
                    hardware.append({"tipus": "CSAVAR_4x35", "cikkszam": "faforgácscsavar 4×35 süllyesztett fejű (fiókdoboz)", "kapcsolat": tag, "db": 1})
        kotesek.append({"A": bl["id"], "B": f"{m}-BOX-F", "tipus": "FIOKDOBOZ_CSAVAR", "db": 2, "ok": "oldalon át 4×35 csavar + ragasztás"})
        kotesek.append({"A": br["id"], "B": f"{m}-BOX-F", "tipus": "FIOKDOBOZ_CSAVAR", "db": 2, "ok": "oldalon át 4×35 csavar + ragasztás"})
        kotesek.append({"A": bl["id"], "B": f"{m}-BOX-H", "tipus": "FIOKDOBOZ_CSAVAR", "db": 2, "ok": "oldalon át 4×35 csavar + ragasztás"})
        kotesek.append({"A": br["id"], "B": f"{m}-BOX-H", "tipus": "FIOKDOBOZ_CSAVAR", "db": 2, "ok": "oldalon át 4×35 csavar + ragasztás"})
        if fb:
            kotesek.append({"A": bl["id"], "B": fb["id"], "tipus": "FIOKDOBOZ_CSAVAR", "db": 3, "ok": "oldalon át 4×35 csavar + ragasztás"})
            kotesek.append({"A": br["id"], "B": fb["id"], "tipus": "FIOKDOBOZ_CSAVAR", "db": 3, "ok": "oldalon át 4×35 csavar + ragasztás"})
        for t, c, db in (("760H3000S", "Blum MOVENTO 760H3000S sínpár NL300 (csavarozva, sablon T65.1600.01)", 1),
                         ("T51.7601", "Blum MOVENTO frontrögzítő pár T51.7601 (sablonnal előfúrva Ø2,5×10, 75°)", 1),
                         ("TIP-ON", f"Blum TIP-ON BLUMOTION {dr.get('tipon', 'T60L7140')} (szerszám nélkül a sínre)", 1),
                         ("SZINKRON", f"{dr.get('sync', 'T60.1125W + 2×T60.000D')} – szinkronrúd vágási méret: {dr.get('sync_cut', '?')} mm", 1)):
            hardware.append({"tipus": t, "cikkszam": c, "kapcsolat": m, "db": db})

    # ---------------------------------------------------------------- 4. furat-ellenőrzés (alkatrészen belül, maradék anyag)
    from s16_geom import build_solid
    zobj = {o["name"]: o for o in load_json(next((F1 / doc["forras"]["mappa"]).glob("*_ZART_JELENET_MM.json")))["objects"]}
    solids = {}
    for h in holes:
        pid = h["alkatresz"]
        if pid not in solids:
            solids[pid] = build_solid(src[pid], zobj.get(pid))
        sol = solids[pid]
        st, di = np.array(h["start"]), np.array(h["irany"])
        # minta a furat tengelyén (0,5 mm-rel a felület alatt → mélység−0,5) és a fenék mögött min_maradek-kal
        inner = st + di * np.linspace(0.5, h["melyseg"] - 0.5, 5)[:, None]
        behind = st + di * (h["melyseg"] + P["min_maradek"] - 0.5)
        from s16_geom import contains_robust
        inside = contains_robust(sol, inner)
        if not inside.all():
            problems.append({"sulyossag": "BLOKKOLO", "alkatresz": pid, "uzenet": f"{h['funkcio']} furat ({h['kapcsolat']}) részben az anyagon kívül"})
        if h["funkcio"] not in ("TIPLI_EL",) and not h.get("atmeno") and not sol.contains(behind[None, :])[0]:
            problems.append({"sulyossag": "HIBA", "alkatresz": pid, "uzenet": f"{h['funkcio']} ({h['kapcsolat']}): a furat mögött < {P['min_maradek']} mm anyag marad (átfúrás veszélye)"})

    out = {"modell_revizio": doc["modell_revizio"], "datum": date.today().isoformat(), "generator": "f2b_vasalat.py",
           "parameterek": P, "pantoldal_javaslat": AJTOK, "furatok": holes, "vasalat": hardware, "kotesek": kotesek, "konnektorok": konnektorok,
           "problemak": problems, "statusz": "TERVI – vasalat típusok és pántoldal műhelyi/tulajdonosi megerősítésre"}
    (HERE / "vasalat_terv.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    fc = Counter(h["funkcio"] for h in holes)
    kc = Counter(k["tipus"] for k in kotesek)
    pc = Counter(p["sulyossag"] for p in problems)
    L = [f"# S16 F2b – vasalat- és furatterv ({doc['modell_revizio']})", "",
         f"Generálva: {date.today().isoformat()} · `f2b_vasalat.py` · státusz: TERVI", "",
         "| Furat-funkció | db |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(fc.items())] + [
         "", "| Kötés | db |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(kc.items())] + [
         "", f"**Problémák:** {dict(pc)}", "", "| Súlyosság | Alkatrész | Megállapítás |", "|---|---|---|"]
    order = {"BLOKKOLO": 0, "HIBA": 1, "FIGYELMEZTETES": 2}
    seen = set()
    for p in sorted(problems, key=lambda p: (order.get(p["sulyossag"], 9), p["alkatresz"])):
        key = (p["sulyossag"], p["alkatresz"], p["uzenet"].split(":")[0] if p["sulyossag"] == "BLOKKOLO" else p["uzenet"])
        if key in seen:
            continue
        seen.add(key)
        L.append(f"| {p['sulyossag']} | {p['alkatresz']} | {p['uzenet']} |")
    L += ["", "## Nem tiplis kapcsolatok (külön kötés kell)", "", "| A | él | B | típus | ok |", "|---|---|---|---|---|"]
    L += [f"| {k['A']} | {k.get('el', '')} | {k['B']} | {k['tipus']} | {k.get('ok', '')} |" for k in kotesek if k["tipus"] != "TIPLI"]
    L += ["", "## Paraméterek és források", "", "```json", json.dumps(P, ensure_ascii=False, indent=1), "```"]
    (HERE / "vasalat_jelentes.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("furatok:", dict(fc), "| kötések:", dict(kc), "| problémák:", dict(pc))


if __name__ == "__main__":
    main()
