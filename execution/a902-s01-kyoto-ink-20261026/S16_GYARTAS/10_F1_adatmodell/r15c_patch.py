#!/usr/bin/env python3
"""S16 R15C – D6 fiók 35 mm-rel feljebb (Péter döntése, 2026-10-30 18:05: „Fiók 35 mm-rel feljebb”).

forras_R15B/ → forras_R15C/. Ok: a D6 jobb sínje (Z≈197…210) a rövid D6-R korpuszoldal (Z 230-tól) alá, az íves sarokelem
(CURVE-B-BOT) belső ívébe esett (max. ~9 mm átfedés); a korpuszoldal nem hosszabbítható (látszó, vágatlan héj). Megoldás: a
fiókdoboz alja 35 mm-rel feljebb, a teteje marad (Z 447) → a sín a D6-R-re kerül (Z ≈ 232…245), a belső magasság 210 → 175 mm.
A front (D6-FRONT) nem változik.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC, DST = HERE / "forras_R15B", HERE / "forras_R15C"
sys.path.insert(0, str(HERE))
from r15_patch import box_vertices_faces  # noqa: E402
from s16_geom import sha256  # noqa: E402

DZ = 35.0


def main():
    parts = json.loads((SRC / "parts.json").read_text(encoding="utf-8"))
    zart = json.loads((SRC / "R15_ZART_JELENET_MM.json").read_text(encoding="utf-8"))
    drawers = json.loads((SRC / "drawers.json").read_text(encoding="utf-8"))
    P = {p["id"]: p for p in parts}
    Z = {o["name"]: o for o in zart["objects"]}
    log = []
    for pid in ("D6-BOX-L", "D6-BOX-R", "D6-BOX-F", "D6-BOX-H", "D6-BOX-B"):
        p = P[pid]
        old = list(p["box"])
        x, y, z, dx, dy, dz = old
        if pid == "D6-BOX-B":
            new = [x, y, z + DZ, dx, dy, dz]          # fenék: 35 mm-rel feljebb (12 mm-es fenékhorony marad)
        else:
            new = [x, y, z + DZ, dx, dy, dz - DZ]     # oldal/elő/hát: alja fel, teteje marad
        p["box"] = new
        if pid != "D6-BOX-B":
            p["W"] = p["W"] - DZ                       # a függőleges méret (W) csökken
        p.pop("mesh_mm", None)
        if p.get("outline"):
            p.pop("outline", None)
            p.pop("curve_vertices", None)
        v, f = box_vertices_faces(new)
        if pid in Z:
            Z[pid]["vertices_mm"], Z[pid]["faces"] = v, f
        log.append({"alkatresz": pid, "mezo": "box", "regi": old, "uj": new,
                    "indok": "D6 sín a D6-R-re kerül (íves sarok ütközés megszűnik)", "forras": "Péter döntése 2026-10-30 18:05", "statusz": "JAVITVA"})
    for d in drawers:
        if d["id"] == "D6":
            old = list(d["inside"])
            d["inside"] = [old[0], old[1], old[2] - DZ]
            d["litres"] = round(d["inside"][0] * d["inside"][1] * d["inside"][2] / 1e6, 3)
            d["r15c"] = "fiókdoboz 35 mm-rel feljebb (belső magasság 210 → 175 mm)"
            log.append({"alkatresz": "D6", "mezo": "drawers.inside", "regi": old, "uj": d["inside"], "indok": "lásd fent",
                        "forras": "Péter döntése 2026-10-30 18:05", "statusz": "JAVITVA"})
    DST.mkdir(exist_ok=True)
    for name in ("materials.json", "layout.json"):
        (DST / name).write_text((SRC / name).read_text(encoding="utf-8"), encoding="utf-8")
    (DST / "parts.json").write_text(json.dumps(parts, ensure_ascii=False, indent=1), encoding="utf-8")
    (DST / "drawers.json").write_text(json.dumps(drawers, ensure_ascii=False, indent=1), encoding="utf-8")
    (DST / "R15_ZART_JELENET_MM.json").write_text(json.dumps(zart, ensure_ascii=False, indent=1), encoding="utf-8")
    (DST / "R15C_VALTOZASNAPLO.json").write_text(json.dumps({"revizio": "S16-R15C-GY", "datum": date.today().isoformat(),
        "alap": {f.name: sha256(f) for f in sorted(SRC.glob("*.json"))}, "valtozasok": log}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"R15C: {len(log)} változás → {DST.name}/")


if __name__ == "__main__":
    main()
