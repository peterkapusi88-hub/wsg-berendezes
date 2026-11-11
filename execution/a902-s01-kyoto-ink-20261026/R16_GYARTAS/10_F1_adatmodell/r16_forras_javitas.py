#!/usr/bin/env python3
"""R16 → forras_R16J: az R16 (ChatGPT) adatainak átvezetése a S16 gyártási lánc bemeneti formátumába, javításokkal.

Bemenet:  forras_R16/ (változatlan R16 másolat, git 251457939478f0786ef04337a372c13418ef6dd4, SHA256SUMS)
Kimenet:  forras_R16J/parts.json            R14/S16-formátum (id, box, axis, L, W, T, material, kind, grain, edge, outline, …)
          forras_R16J/materials.json        anyaglista [kód, megnevezés, …] – a parts.json minden kódjára
          forras_R16J/drawers.json          S16-formátum (moving, stroke, LW, SKW, NL, …)
          forras_R16J/layout.json           a lánc által olvasott minimális layout
          forras_R16J/R16J_ZART_JELENET_MM.json   üres (R16-ban nincs zárt háló-jelenet; a lánc befoglalóból/kontúrból épít)
          forras_R16J/javitasi_naplo.json   minden eltérés: mi volt, mi lett, miből

KOORDINÁTA (R16 → S16 konvenció):
  R16 rajzi rendszer: jobbkezes, X jobbra (szobából), Y a front síkjától (Y=0) a fal felé, Z fel.
  S16 konvenció:      X jobbra, Y a FALTÓL a szoba felé, Z fel (balkezes, a CAD-export egyszer tükröz).
  X_S16 = X_R16, Z_S16 = Z_R16, Y_S16 = FAL_Y_R16 − Y_R16.
  FAL_Y_R16 = 418 (FELTEVÉS): R16 materials.json M16-BRONZE: „frontY382; 18 mm szerelőtér a fal előtt” → a 18 mm-es sáv
  382..400, előtte 18 mm szerelőtér → fal = 418. Csak eltolás; méretet/alakot nem változtat. Helyszíni felmérés nincs.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
SRC = HERE / "forras_R16"
OUT = HERE / "forras_R16J"
FAL_Y = 418.0

AXIS_NAME = {(1, 0, 0): "+X", (-1, 0, 0): "-X", (0, 1, 0): "+Y", (0, -1, 0): "-Y", (0, 0, 1): "+Z", (0, 0, -1): "-Z"}


def load(n):
    return json.loads((SRC / n).read_text(encoding="utf-8"))


def box_s16(b):
    x, y, z, dx, dy, dz = b
    return [x, round(FAL_Y - (y + dy), 4), z, dx, dy, dz]


def vec_s16(v):
    return [v[0], -v[1], v[2]]


def axname(v):
    return AXIS_NAME[tuple(int(round(c)) for c in v)]


def modul_of(p):
    pid, t = p["id"], p["type"]
    if t.startswith("TV01") or pid in ("KI14-BAT-01", "KI14-BAT-02", "KI14-RAIL-06", "KI14-RAIL-07"):
        return "TORONY"
    if t in ("TV03-P", "GAP"):
        return "HATTER"
    if t == "TV02-CAP":
        return "ALSO_KERET"
    if pid.startswith("KI16-D"):
        return pid.split("-")[1]                       # D1..D6
    if pid.startswith("KI16-M6"):
        return "D6"
    n = p["name"]
    if n[:1] == "M" and n[1:2].isdigit():
        return "D" + n[1]                              # „M3 / …” → D3 (a S16 lap-csoportosítás D1–D6 neveivel)
    # BAT/RAIL modul a befoglaló X szerint a layout lower_modules-ból
    return None


def main():
    parts = load("parts.json")
    layout = load("layout.json")
    drawers = load("drawers.json")
    notches = load("notches.json")
    materials = load("materials.json")
    audit = load("audit_eredmeny_CLAUDE_ATADAS.json")
    mods = layout["lower_modules"]
    naplo = []

    def modul_by_x(x):
        for i, (x0, w) in enumerate(mods, 1):
            if x0 - 0.01 <= x < x0 + w - 0.01:
                return f"D{i}"
        return "EGYEB"

    notch_by_part = {}
    for n in notches:
        notch_by_part.setdefault(n["part"], []).append(n)

    out = []
    for p in parts:
        ab = p["assembly_box_mm"]
        dims = sorted(ab[3:])
        # vastagsági tengely: az R16 frame outward_A tengelye (a 18×18 léceknél csak így egyértelmű)
        oa = p["frame"]["outward_A"]
        ax_i = int(np.argmax(np.abs(oa)))
        axis = "xyz"[ax_i]
        T = ab[3 + ax_i]
        if abs(T - p["t"]) > 0.01:
            naplo.append({"id": p["id"], "mezo": "t", "volt": p["t"], "lett": T, "forras": "assembly_box_mm vastagsági tengelye"})
        listed = sorted([p["x"], p["y"], p["t"]])
        if any(abs(a - b) > 0.01 for a, b in zip(listed, dims)):
            naplo.append({"id": p["id"], "mezo": "x/y/t (listázott méret)", "volt": [p["x"], p["y"], p["t"]],
                          "lett": "a befoglalóból: " + "×".join(f"{d:g}" for d in ab[3:]),
                          "forras": "assembly_box_mm (R16 natív STL-visszaolvasással igazolt, audit max 1,9e-6 mm) – a listázott sor hibás",
                          "audit_egyezes": any(m["id"] == p["id"] for m in audit["parts_dimension_mismatches"])})
        box = box_s16(ab)
        mat_code = p["material"]
        if mat_code == "M03" and abs(T - 8) < 0.01:
            mat_code = "M03-8"
            naplo.append({"id": p["id"], "mezo": "material", "volt": "M03", "lett": "M03-8",
                          "forras": "ugyanaz az M03 kód 18 és 8 mm-es lapra – a 8 mm-es hátlap külön anyagkódot kap (vastagság a befoglalóból)"})
        rec = {
            "id": p["id"], "revision": "R16J", "r16_revision": p["revision"], "name": p["name"], "box": box, "axis": axis,
            "T": T, "material": mat_code, "kind": p["type"],
            "grain": None, "r16_grain": p["grain"],
            "r16_edge": p["edge"], "r16_frame": {"U": vec_s16(p["frame"]["U"]), "V": vec_s16(p["frame"]["V"]),
                                                  "outward_A": vec_s16(p["frame"]["outward_A"])},
            "r16_listed_xyt": [p["x"], p["y"], p["t"]],
            "note": p["note"], "status": "TERVI – R16J", "r16_status": p["status"],
            "raw_size_status": p["raw_size_status"],
            "modul": modul_of(p) or modul_by_x(ab[0] + 0.001),
        }
        g = (p["grain"] or "").lower()
        if g.startswith("x irány: magasság"):
            rec["grain_global"] = "Z"                     # R16 szöveg: „X irány: magasság” = a darab hossza függőleges
        elif g.startswith("hosszanti"):
            rec["grain_global"] = "LONG"
        # hátlap-sarokkivágások → kontúr (A=+Y nézet: u = X − x0, v = Z − z0)
        if p["id"] in notch_by_part:
            if axis != "y":
                raise SystemExit(f"{p['id']}: kivágás nem y-tengelyű lapon")
            from shapely.geometry import box as sbox
            x0, z0 = ab[0], ab[2]
            poly = sbox(0, 0, ab[3], ab[5])
            for n in notch_by_part[p["id"]]:
                nb = n["box"]
                if abs(nb[1] - ab[1]) > 0.01 or abs(nb[4] - ab[4]) > 0.01:
                    raise SystemExit(f"{n['id']}: nem a teljes vastagságon átmenő")
                poly = poly.difference(sbox(nb[0] - x0, nb[2] - z0, nb[0] - x0 + nb[3], nb[2] - z0 + nb[5]))
            from shapely.geometry.polygon import orient
            poly = orient(poly, 1.0)
            rec["outline"] = [[round(a, 4), round(b, 4)] for a, b in list(poly.exterior.coords)[:-1]]
            rec["cutouts"] = []
            rec["notches_r16"] = [{"id": n["id"], "box_r16": n["box"], "method": n["method"]} for n in notch_by_part[p["id"]]]
            naplo.append({"id": p["id"], "mezo": "outline", "volt": "befoglaló + notches.json (külön)", "lett": f"{len(rec['outline'])} pontos kontúr",
                          "forras": "notches.json – sarokkivágás a kontúrba építve (a CAD/QA lánc a kontúrt olvassa)"})
        out.append(rec)

    # anyagok: a parts.json minden kódja; az R16 materials.json csak az M16-* kódokat definiálja
    mat_r16 = {m[0]: m for m in materials}
    MAT = {
        "M01": ["M01", "18 mm MDF, matt bronzbarna 2KPU festés (alsó frontok, összefüggő fedő)",
                "R16 face_finishes.json / 00_OLVASD_EL: alsó front bronzbarna; kód az R12–R16 alkatrészlistából"],
        "M01+nyomat": ["M01+nyomat", "18 mm MDF, bronzbarna matt alap + tusgrafika nyomott/UV réteg (toronyajtók)",
                       "R16 materials.json M16-TOWER"],
        "M02": ["M02", "18 mm MDF hordozó + Vescom Bely+Print 1040.01 textilhatású burkolat (dekor panel)",
                "R16 materials.json M16-WALL"],
        "M03": ["M03", "18 mm laminált bútorlap (korpusz belső) – dekor nyitott",
                "R16 face_finishes.json: interior M03; R12 OLVASD_EL: tervezett 1 mm élzárás"],
        "M03-8": ["M03-8", "8 mm hátlap, M03 korpuszdekorban", "R16 parts.json: TV01-H/TV02-H2 M03 kóddal, t = 8 mm"],
        "BEECH18": ["BEECH18", "18×18 mm bükk léc (hátlaprögzítő)", "R16 parts.json"],
        "PLY18": ["PLY18", "18 mm rétegelt lemez merevítő keresztléc", "R16 parts.json"],
    }
    mats = []
    for code in sorted({p["material"] for p in out}):
        if code in mat_r16:
            mats.append(mat_r16[code])
        elif code in MAT:
            mats.append(MAT[code])
            naplo.append({"id": f"anyag:{code}", "mezo": "materials.json", "volt": "nincs definiálva az R16 materials.json-ban",
                          "lett": MAT[code][1], "forras": MAT[code][2]})
        else:
            raise SystemExit(f"ismeretlen anyag {code}")

    # fiókok S16-formátumban
    dr = []
    for d in drawers:
        dr.append({"id": d["id"], "front": d["front"], "moving": d["parts"] + [d["front"]], "stroke": d["NL"],
                   "stroke_forras": "FELTEVÉS: teljes kihúzás = NL (MOVENTO 760H3000S, NL 300)",
                   "LW": d["LW"], "SKW": d["SKW"], "NL": d["NL"], "runner": "Blum MOVENTO 760H3000S + T51.7601",
                   "tipon": d["motion_unit"], "r16": {k: v for k, v in d.items() if k not in ("parts",)}})

    OUT.mkdir(exist_ok=True)
    (OUT / "parts.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "materials.json").write_text(json.dumps(mats, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "drawers.json").write_text(json.dumps(dr, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "layout.json").write_text(json.dumps({"r16": layout, "fal_y_r16": FAL_Y,
                                                 "koordinata": "Y_S16 = 418 − Y_R16 (FELTEVÉS, lásd r16_forras_javitas.py)"},
                                                ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "R16J_ZART_JELENET_MM.json").write_text(json.dumps({"megjegyzes": "R16-ban nincs zárt háló-jelenet; a lánc a parts.json befoglalóiból/kontúrjaiból épít testet",
                                                               "objects": []}, ensure_ascii=False, indent=1), encoding="utf-8")
    (OUT / "javitasi_naplo.json").write_text(json.dumps({"forras": "forras_R16 (git 2514579)", "fal_y_r16": FAL_Y,
                                                         "valtozasok": naplo}, ensure_ascii=False, indent=1), encoding="utf-8")
    sums = [f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}" for f in sorted(SRC.iterdir()) if f.is_file() and f.name != "SHA256SUMS"]
    (SRC / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
    print(f"OK: {len(out)} alkatrész, {len(naplo)} naplóbejegyzés, {len(mats)} anyag, {len(dr)} fiók")


if __name__ == "__main__":
    main()
