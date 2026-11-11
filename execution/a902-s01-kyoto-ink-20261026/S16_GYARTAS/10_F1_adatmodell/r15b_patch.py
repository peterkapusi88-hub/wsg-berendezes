#!/usr/bin/env python3
"""S16 R15B – a bal toronyajtó (T-DOOR-L) pántolhatósága: keretszár 31 → 50 mm mindkét oldalon.

forras_R15/ → forras_R15B/ (+ R15B_VALTOZASNAPLO.json). Az R15 érintetlen marad.

Ok (f2b_vasalat.py BLOKKOLÓ, 2026-10-30): a textilkazetta kivágása mellett a keretszár 31 mm, mögötte 21 mm-től a 12 mm-es
kazettahát (T-DOOR-L-BACK) – Ø35 kehely sehol nem fér el. Döntés (Péter: „a pántozást oldd meg, ahogy legjobbnak gondolod”,
2026-10-30, Claude javaslata, visszafordítható): a kazetta-szerkezetet mindkét oldalon befelé toljuk úgy, hogy a keretszár
50 mm legyen (szimmetrikus, a látvány arányos marad; a textilmező 350 → 312,5 mm). A lekerekítések sugara nem változik:
a bal fél +19 mm-rel, a jobb fél −18,5 mm-rel tolódik (a vízszintes szakaszok rövidülnek).
Érintett: T-DOOR-L kivágás és hátsó fényfalc, T-DOOR-L-BACK, TEXTILE, a jelenet TEXTILE-RECESSED-HOUSING/EMITTER objektumai.
Pánt: Blum CLIP top 110° rugó nélküli, inset (befekvő), csavaros 70T3750 + 177H3100E talp (az etalon km.dwg 71T3750 + 177H3100E
párosának rugó nélküli változata a TIP-ON miatt) – B = 3 mm: kehely 3…38 mm, kazettahát 62 mm-től (≥ 3 mm hézag),
kivágás 71 mm-től (12 mm falvastagság). Forrás: Blum katalógus / sfs.ch 71T3750 „inner hinge 110° screws”; 70T3750 = unsprung inset.
"""
from __future__ import annotations

import copy
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC, DST = HERE / "forras_R15", HERE / "forras_R15B"
sys.path.insert(0, str(HERE))
from s16_geom import build_solid, sha256  # noqa: E402

DOOR_X0 = 21.0                 # T-DOOR-L box x (globális)
CUT_L, CUT_R = 52.0, 402.0     # régi kivágás globálisan (helyi 31…381)
NEW_STILE = 50.0
SHIFT_L = DOOR_X0 + NEW_STILE - CUT_L            # +19
SHIFT_R = (DOOR_X0 + 412.5 - NEW_STILE) - CUT_R  # −18.5
XMID = (CUT_L + CUT_R) / 2                        # 227


def gx(X):
    return X + (SHIFT_L if X < XMID else SHIFT_R)


def main():
    parts = json.loads((SRC / "parts.json").read_text(encoding="utf-8"))
    zart = json.loads((SRC / "R15_ZART_JELENET_MM.json").read_text(encoding="utf-8"))
    P = {p["id"]: p for p in parts}
    log = []

    def L(pid, mezo, regi, uj, indok):
        log.append({"alkatresz": pid, "mezo": mezo, "regi": regi, "uj": uj, "indok": indok,
                    "forras": "Péter 2026-10-30 („a pántozást oldd meg”) – Claude döntés, visszafordítható", "statusz": "JAVITVA"})

    # 1. T-DOOR-L: kivágás (helyi x) és hátsó fényfalc (globális x)
    d = P["T-DOOR-L"]
    c = d["cutouts"][0]
    old = [min(a for a, _ in c["outline"]), max(a for a, _ in c["outline"])]
    c["outline"] = [[gx(a + DOOR_X0) - DOOR_X0, b] for a, b in c["outline"]]
    c["note"] = "Átmenő kivágás a süllyesztett textilkazettához; R15B: keretszár 50/50 mm a Ø35 pántkehely miatt."
    L("T-DOOR-L", "cutouts[0].outline x", old, [min(a for a, _ in c["outline"]), max(a for a, _ in c["outline"])],
      "keretszár 31 → 50 mm (pántkehely Ø35, B=3 + 12 mm fal)")
    rr = d["rear_light_rebate"]
    old = [min(a for a, _ in rr["outline_xz_mm"]), max(a for a, _ in rr["outline_xz_mm"])]
    rr["outline_xz_mm"] = [[gx(a), b] for a, b in rr["outline_xz_mm"]]
    L("T-DOOR-L", "rear_light_rebate x", old, [min(a for a, _ in rr["outline_xz_mm"]), max(a for a, _ in rr["outline_xz_mm"])],
      "a fényfalc a kivágással együtt tolódik (6 mm perem marad)")
    d.pop("mesh_mm", None)
    d["note"] = ("R15B: rugó nélküli inset Blum CLIP top 70T3750 + 177H3100E talp, mágneses TIP-ON; bal ajtó 6 pánt (B=3 mm). "
                 "Keretszár 50/50 mm. Pántoldali 24 V hajlításálló vezeték, oldható csatlakozó, húzásmentesítés; teljes nyitásnál vezetékpróba.")

    # 2. kazettahát és textil: kontúr (helyi) + box
    for pid in ("T-DOOR-L-BACK", "TEXTILE"):
        p = P[pid]
        x0 = p["box"][0]
        gl = [[a + x0, b] for a, b in p["outline"]]
        newx0 = gx(x0)
        newx1 = gx(x0 + p["box"][3])
        p["outline"] = [[gx(a) - newx0, b] for a, b in gl]
        if p.get("curve_vertices"):
            p["curve_vertices"] = [[gx(a + x0) - newx0, b, k] for a, b, k in p["curve_vertices"]]
        oldbox = list(p["box"])
        p["box"][0], p["box"][3] = round(newx0, 3), round(newx1 - newx0, 3)
        p["L"] = p["box"][3]
        p.pop("mesh_mm", None)
        L(pid, "box/outline", oldbox, p["box"], "a kazetta a kivágással együtt keskenyedik (szimmetrikus 19/18,5 mm)")

    # 3. jelenet: a módosított alkatrészek hálója a kontúrból újraépül, a két jelenetobjektum tolódik
    keep = []
    for o in zart["objects"]:
        if o["name"] in ("T-DOOR-L", "T-DOOR-L-BACK", "TEXTILE"):
            sol = build_solid(P[o["name"]], None)          # új zárt háló a módosított kontúrból (kivágás + fényfalc)
            assert sol.mesh is not None and sol.mesh.is_watertight, o["name"]
            o["vertices_mm"] = [[round(float(c), 4) for c in v] for v in sol.mesh.vertices]
            o["faces"] = [[int(i) for i in f] for f in sol.mesh.faces]
            o["r15b"] = f"újraépítve: {sol.method}"
        if o["name"] in ("TEXTILE-RECESSED-HOUSING", "TEXTILE-RECESSED-EMITTER"):
            o["vertices_mm"] = [[gx(v[0]), v[1], v[2]] for v in o["vertices_mm"]]
            L(o["name"], "vertices x", "42…412 / 47…407", "R15B tolás", "jelenetobjektum a kazettával együtt")
        keep.append(o)
    zart["objects"] = keep
    zart["source_note_R15B"] = "R15B: T-DOOR-L keretszár 50/50 mm (r15b_patch.py)"

    DST.mkdir(exist_ok=True)
    for name in ("materials.json", "drawers.json", "layout.json"):
        (DST / name).write_text((SRC / name).read_text(encoding="utf-8"), encoding="utf-8")
    (DST / "parts.json").write_text(json.dumps(parts, ensure_ascii=False, indent=1), encoding="utf-8")
    (DST / "R15_ZART_JELENET_MM.json").write_text(json.dumps(zart, ensure_ascii=False, indent=1), encoding="utf-8")
    (DST / "R15B_VALTOZASNAPLO.json").write_text(json.dumps({
        "revizio": "S16-R15B-GY", "datum": date.today().isoformat(), "generator": "r15b_patch.py",
        "alap": {f.name: sha256(f) for f in sorted(SRC.glob("*.json"))}, "valtozasok": log}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"R15B: {len(log)} változás → {DST.name}/ ; eltolás bal {SHIFT_L:+.1f} / jobb {SHIFT_R:+.1f} mm")


if __name__ == "__main__":
    main()
