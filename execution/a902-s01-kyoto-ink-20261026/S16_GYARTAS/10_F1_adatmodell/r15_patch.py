#!/usr/bin/env python3
"""S16 R15 – dokumentált adatjavítás az R14 forrásból (az R14 másolat érintetlen marad).

forras_R14/  →  forras_R15/  (+ forras_R15/R15_VALTOZASNAPLO.json)

Minden változás itt, kódban, indokkal és forrással van leírva; a build és a QA ezután a forras_R15-ből fut.
Futtatás:  python3 r15_patch.py
"""
from __future__ import annotations

import copy
import json
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SRC, DST = HERE / "forras_R14", HERE / "forras_R15"
sys.path.insert(0, str(HERE))
from s16_geom import sha256  # noqa: E402

REV = "S16-R15-GY"
log = []


def L(pid, mezo, regi, uj, indok, forras, statusz="JAVITVA"):
    log.append({"alkatresz": pid, "mezo": mezo, "regi": regi, "uj": uj, "indok": indok, "forras": forras, "statusz": statusz})


def box_vertices_faces(box):
    x, y, z, dx, dy, dz = box
    v = [[x + a * dx, y + b * dy, z + c * dz] for a in (0, 1) for b in (0, 1) for c in (0, 1)]
    f = [[0, 1, 3, 2], [2, 3, 7, 6], [6, 7, 5, 4], [4, 5, 1, 0], [2, 6, 4, 0], [7, 3, 1, 5]]
    return v, f


def main():
    parts = json.loads((SRC / "parts.json").read_text(encoding="utf-8"))
    materials = json.loads((SRC / "materials.json").read_text(encoding="utf-8"))
    drawers = json.loads((SRC / "drawers.json").read_text(encoding="utf-8"))
    layout = json.loads((SRC / "layout.json").read_text(encoding="utf-8"))
    zart = json.loads((SRC / "R14_ZART_JELENET_MM.json").read_text(encoding="utf-8"))
    P = {p["id"]: p for p in parts}
    Z = {o["name"]: o for o in zart["objects"]}

    def set_box(pid, newbox, mezo_indok, forras):
        p = P[pid]
        old = list(p["box"])
        p["box"] = newbox
        ax = p["axis"]
        dx, dy, dz = newbox[3:]
        p["L"], p["W"], p["T"] = {"x": (dy, dz, dx), "y": (dx, dz, dy), "z": (dx, dy, dz)}[ax]
        v, f = box_vertices_faces(newbox)
        Z[pid]["vertices_mm"], Z[pid]["faces"] = v, f
        if p.get("mesh_mm"):
            p["mesh_mm"] = {"vertices": v, "faces": f}
        L(pid, "box", old, newbox, mezo_indok, forras)

    # ------------------------------------------------------------------ 1. fiókfenék besüllyesztés (Blum MOVENTO)
    BLUM = "https://ea.blum.com/en/building-a-movento-drawer/ – fenékbesüllyesztés min. 12 mm magas, max. 15 mm mély (lekérve 2026-10-30)"
    RECESS = 12
    for d in drawers:
        did = d["id"]
        side = P[f"{did}-BOX-L"]["box"]
        zb = side[2] + RECESS
        b = list(P[f"{did}-BOX-B"]["box"])
        set_box(f"{did}-BOX-B", [b[0], b[1], zb, b[3], b[4], b[5]],
                f"fiókfenék {RECESS} mm-rel feljebb (alsó síkja az oldal alsó éle fölött {RECESS} mm), hogy a MOVENTO sín takarva legyen", BLUM)
        top = side[2] + side[5]
        for k in ("F", "H"):
            fb = list(P[f"{did}-BOX-{k}"]["box"])
            z0 = zb + b[5]
            set_box(f"{did}-BOX-{k}", [fb[0], fb[1], z0, fb[3], fb[4], round(top - z0, 3)],
                    "fiók elő-/hátfala a felemelt fenékre ül, felső éle változatlan (az oldal tetejével egy síkban)", BLUM)
        old_in = d["inside"]
        d["inside"] = [old_in[0], old_in[1], round(top - (zb + b[5]), 3)]
        d["litres"] = round(d["inside"][0] * d["inside"][1] * d["inside"][2] / 1e6, 3)
        L(did, "drawers.inside/litres", old_in, d["inside"], "belső magasság a felemelt fenék miatt csökken", BLUM)

    # ------------------------------------------------------------------ 2. BG-1 / BG-FINISH nyers méret + szöveg
    for pid in ("BG-1", "BG-FINISH"):
        p = P[pid]
        old = (p["raw_L"], p["raw_W"], p["raw_rule"])
        p["raw_L"] = round(p["L"] + 30, 3)
        p["raw_W"] = p["W"]
        p["raw_rule"] = (f"Bal oldali 30 mm szerelési ráhagyás (helyszíni visszaillesztés a torony íve mögött). "
                         f"Kész L{p['L']} mm, nyers L{p['raw_L']} mm; magasság ráhagyás nélkül W{p['W']} mm. "
                         "A 100 mm magas felső fül a toronyív mögé nyúlik; az alsó él nem nyúlik a korpusz mögé.")
        L(pid, "raw_L/raw_W/raw_rule", old, (p["raw_L"], p["raw_W"], p["raw_rule"]),
          "R14: raw_W 2315 egy korábbi háttérmagasságból maradt (kész 2405), a szöveg kész L801-et írt az adat 811-ével szemben, "
          "a BG-FINISH a BG-1 szövegét örökölte. A szövegben rögzített 30 mm szerelési ráhagyást alkalmazzuk; magasságban nincs indokolt levonás.",
          "R14 parts.json raw_rule (BG-1) – szándék: 30 mm bal ráhagyás")

    # ------------------------------------------------------------------ 3. anyag/vastagság egyeztetés
    materials.append(["M10", "8 mm MDF léc (rejtett háttér-távtartó)",
                      "Falsín/távtartó a háttér mögött; nem látszik. Anyag javaslat: 8 mm MDF vagy rétegelt; helyszíni síkkorrekció alátéttel.",
                      "R15 javaslat – műhelyi megerősítésre", "#8a7f72"])
    materials.append(["M11", "12 mm festett MDF (M02 színben)",
                      "Süllyesztett ajtókazetta hátlapja; a 12 mm-es vastagság a kazetta mögötti 14 mm-es polcrést tartja.",
                      "R15 javaslat – műhelyi megerősítésre", "#332c26"])
    materials.append(["M12", "Fénytakaró / tálca / baffle profil – termék kiválasztandó",
                      "Rejtett LED-ágak takarói (R14 jelenet-segédobjektumokból felvéve). Anyag: alumínium vagy festett MDF/HDF – a LED-profil kiválasztásától függ.",
                      "R15 – termékválasztás nyitott", "#2a2622"])
    for i in range(1, 6):
        pid = f"BATTEN-{i}"
        L(pid, "material", P[pid]["material"], "M10", "8 mm vastag léc nem lehet 18 mm-es bútorlapból (M01)", "QA Q07 (F1)")
        P[pid]["material"] = "M10"
    L("T-DOOR-L-BACK", "material", P["T-DOOR-L-BACK"]["material"], "M11",
      "12 mm vastag kazetta-hátlap nem lehet 18 mm-es M02; a geometria (12 mm, 14 mm polcrés) marad, az anyag lesz 12 mm-es", "QA Q07 (F1)")
    P["T-DOOR-L-BACK"]["material"] = "M11"
    p = P["T-DOOR-L-BACK"]
    old = (p["raw_L"], p["raw_W"])
    p["raw_L"], p["raw_W"] = None, None
    L("T-DOOR-L-BACK", "raw_L/raw_W", old, None, "az R14 explicit nyers = kész ellentmondott a +10/+10 festett MDF szabálynak; a szabályfájl számol", "QA Q03 (F1)")

    # ------------------------------------------------------------------ 4. gyártandó fénytakarók felvétele a listába
    COVERS = ["TOP-WASH-COVER", "TOP-WASH-BAFFLE", "TOP-WASH-HIDDEN-END", "UPLIGHT-TRAY", "UPLIGHT-FRONT-VISOR",
              "UPLIGHT-REAR-VISOR", "DECK-CONTINUOUS-COVER", "DECK-CONTINUOUS-BAFFLE", "LOW-INTERNAL-LIGHT-VISOR"]
    for name in COVERS:
        o = Z[name]
        v = np.asarray(o["vertices_mm"], float)
        lo, hi = v.min(0), v.max(0)
        size = hi - lo
        ax = "xyz"[int(np.argmin(size))]
        box = [round(float(c), 3) for c in (*lo, *size)]
        LWT = {"x": (size[1], size[2], size[0]), "y": (size[0], size[2], size[1]), "z": (size[0], size[1], size[2])}[ax]
        parts.append({
            "id": name, "revision": REV, "name": f"Fénytakaró / tálca ({name})", "box": box, "axis": ax,
            "L": round(float(LWT[0]), 3), "W": round(float(LWT[1]), 3), "T": round(float(LWT[2]), 3),
            "material": "M12", "cost": None, "kind": "light_cover", "grain": "nincs", "outline": None, "cutouts": [],
            "note": "R15: az R14 jelenetben csak segédobjektum volt; valós gyártandó/beszerzendő elem. Méret a jelenetből, termék nyitott.",
            "status": "Tervi méret; nem gyártási kiadás", "raw_L": None, "raw_W": None, "raw_rule": "Profil/termék szerint.",
            "edge": "", "datum": "", "operations": "", "drawing": "R15 adatjavítás", "model": name,
        })
        o["role"] = "primary_part"
        L(name, "felvétel", "segédobjektum", "alkatrész (M12)", "valós takaró/tálca, eddig hiányzott az anyagjegyzékből", "QA Q16 (F1)")

    # 4b. az alsó belső fénytakaró a csukott ajtó kazetta-hátlapjába lóg (R15 QA Q11) → a kazetta mögé
    P_ = {p["id"]: p for p in parts}
    vb = list(P_["LOW-INTERNAL-LIGHT-VISOR"]["box"])
    cass_back_y = P_["T-DOOR-L-BACK"]["box"][1]          # 354
    new_y = cass_back_y - 6 - vb[4]                        # 6 mm szabad távolság a kazettától
    nb = [vb[0], new_y, vb[2], vb[3], vb[4], vb[5]]
    P_["LOW-INTERNAL-LIGHT-VISOR"]["box"] = nb
    Z["LOW-INTERNAL-LIGHT-VISOR"]["vertices_mm"], Z["LOW-INTERNAL-LIGHT-VISOR"]["faces"] = box_vertices_faces(nb)
    L("LOW-INTERNAL-LIGHT-VISOR", "box", vb, nb,
      f"csukott ajtónál a süllyesztett kazetta hátlapjával (Y{cass_back_y}..{cass_back_y + 12}) ütközött; 6 mm-rel a kazetta mögé tolva. "
      "A LED-profil és a fényirány a termékválasztásnál ellenőrzendő.", "QA Q11 (R15)", statusz="JAVASLAT")

    # ------------------------------------------------------------------ 5. BG-visszafordulások: tisztázandó, nem kitalált geometria
    layout.setdefault("r15_tisztazando", {})["BG-UPPER-HIDDEN-RETURN/BG-LOWER-HIDDEN-RETURN"] = (
        "A layout R14 'primary_changed' listája hivatkozza, de nincs ilyen test. A 130 mm (torony mögött, BG-1 X=740-től) "
        "és 100 mm (alsó sor mögött, BG Z=470-től) takart túlfutás a BG-1…4 geometriájában benne van; az 'Y20..38' "
        "hátsó átfedés viszont sehol nincs modellezve. Blender-jelenetben ellenőrizendő, addig NEM pótoljuk kitalált méretekkel.")
    L("BG-*-HIDDEN-RETURN", "tisztázás", None, layout["r15_tisztazando"], "nem rekonstruálható bizonyítékkal", "layout.json R14",
      statusz="NYITOTT")

    for p in parts:
        if p["revision"] != REV:
            p["revision"] = REV if any(e["alkatresz"] == p["id"] for e in log) else p["revision"]
    layout["revision"] = REV

    DST.mkdir(exist_ok=True)
    zart["source_note_R15"] = "R15: a fenti R14 export módosított másolata – fiókdobozok és 9 fénytakaró szerepe a r15_patch.py szerint"
    zart["primary_geometry_sha256"] = None
    out = {"parts.json": parts, "materials.json": materials, "drawers.json": drawers, "layout.json": layout,
           "R15_ZART_JELENET_MM.json": zart}
    for name, data in out.items():
        (DST / name).write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    (DST / "R15_VALTOZASNAPLO.json").write_text(json.dumps({
        "revizio": REV, "datum": date.today().isoformat(), "generator": "r15_patch.py",
        "alap": {f.name: sha256(f) for f in sorted(SRC.glob("*.json"))},
        "valtozasok": log}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"R15: {len(log)} változás → {DST.name}/")


if __name__ == "__main__":
    main()
