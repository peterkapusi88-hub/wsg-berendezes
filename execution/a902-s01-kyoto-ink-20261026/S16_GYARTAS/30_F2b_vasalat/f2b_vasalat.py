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
    "tipli": {"d": 8.0, "el_melyseg": 25.0, "lap_melyseg": 12.0, "hossz": 35, "veg_tav": 32.0, "max_koz": 192.0,
              "min_el": 60.0, "forras": "etalon (km/coo1): Ø8×25/35 bordás tipli; 32-es rendszer"},
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

    # ---------------------------------------------------------------- 1. tiplik a T-kötéseknél
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
                if not ok_part(b):
                    kotesek.append({"A": aid, "el": e, "B": bid, "tipus": "NEM_TIPLIS",
                                    "ok": f"B ({b['gyartasi_tipus']}, {b['anyag']['kod']}) nem 18 mm-es korpuszlap – ragasztás/csavar/szerelvény, műhelyi döntés"})
                    continue
                if abs(abs(vec(b["helyi_rendszer"]["N"]) @ d) - 1) > 1e-6:
                    kotesek.append({"A": aid, "el": e, "B": bid, "tipus": "EL_EL_ILLESZTES",
                                    "ok": "két lap éllel ül egymáson (nem T-kötés) – összekötő vasalat/léc kell, tipli nem"})
                    continue
                # kötésvonal: A élének az a szakasza, amely B-n fekszik
                L, W, T = fa.L, fa.W, fa.T
                if e in ("E1", "E3"):
                    along, a0, a1, fix = fa.U, 0.0, L, (0.0 if e == "E1" else W)
                else:
                    along, a0, a1, fix = fa.V, 0.0, W, (L if e == "E2" else 0.0)
                blo, bhi = np.array(b["befoglalo_globalis"][:3], float), np.array(b["befoglalo_globalis"][:3], float) + np.array(b["befoglalo_globalis"][3:], float)
                # B kiterjedése az él irányában, A helyi koordinátájában
                ax_i = int(np.argmax(np.abs(along)))
                cand = sorted([fa.to_local(blo)[0 if e in ("E1", "E3") else 1], fa.to_local(bhi)[0 if e in ("E1", "E3") else 1]])
                s0, s1 = max(a0, cand[0]), min(a1, cand[1])
                length = s1 - s0
                tp = P["tipli"]
                if length < tp["min_el"]:
                    problems.append({"sulyossag": "FIGYELMEZTETES", "alkatresz": aid, "uzenet": f"{e}→{bid}: kötésszakasz {length:.0f} mm < {tp['min_el']} – tipli nem fér, egyedi kötés"})
                    continue
                n = max(2, math.ceil((length - 2 * tp["veg_tav"]) / tp["max_koz"]) + 1)
                pos = np.linspace(s0 + tp["veg_tav"], s1 - tp["veg_tav"], n)
                for k, s in enumerate(pos):
                    loc = [s, fix, T / 2] if e in ("E1", "E3") else [fix, s, T / 2]
                    pt = fa.to_global(loc)
                    tag = f"{aid}:{e}:{bid}:{k}"
                    holes.append(hole(aid, f"él {e}", pt, -d, tp["d"], tp["el_melyseg"], "TIPLI_EL", tag,
                                      helyi=local_of(fa, pt)))
                    holes.append(hole(bid, "lap", pt, d, tp["d"], tp["lap_melyseg"], "TIPLI_LAP", tag,
                                      helyi=local_of(FR[bid], pt)))
                    hardware.append({"tipus": "TIPLI_D8x35", "cikkszam": "Ø8×35 bordás tipli (etalon: TIPLI_D8_L25/35)",
                                     "pozicio": [round(float(c), 3) for c in pt], "irany": [float(c) for c in d], "kapcsolat": tag})
                kotesek.append({"A": aid, "el": e, "B": bid, "tipus": "TIPLI", "db": int(n), "szakasz_mm": round(float(length), 1)})

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
                hardware.append({"tipus": "POLCTARTO", "cikkszam": "polctartó Ø5 (etalon: de_11090) – típus nyitott",
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
        inside = sol.contains(inner)
        if not inside.all():
            problems.append({"sulyossag": "BLOKKOLO", "alkatresz": pid, "uzenet": f"{h['funkcio']} furat ({h['kapcsolat']}) részben az anyagon kívül"})
        if h["funkcio"] not in ("TIPLI_EL",) and not sol.contains(behind[None, :])[0]:
            problems.append({"sulyossag": "HIBA", "alkatresz": pid, "uzenet": f"{h['funkcio']} ({h['kapcsolat']}): a furat mögött < {P['min_maradek']} mm anyag marad (átfúrás veszélye)"})

    out = {"modell_revizio": doc["modell_revizio"], "datum": date.today().isoformat(), "generator": "f2b_vasalat.py",
           "parameterek": P, "pantoldal_javaslat": AJTOK, "furatok": holes, "vasalat": hardware, "kotesek": kotesek,
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
    L += [f"| {k['A']} | {k['el']} | {k['B']} | {k['tipus']} | {k['ok']} |" for k in kotesek if k["tipus"] != "TIPLI"]
    L += ["", "## Paraméterek és források", "", "```json", json.dumps(P, ensure_ascii=False, indent=1), "```"]
    (HERE / "vasalat_jelentes.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("furatok:", dict(fc), "| kötések:", dict(kc), "| problémák:", dict(pc))


if __name__ == "__main__":
    main()
