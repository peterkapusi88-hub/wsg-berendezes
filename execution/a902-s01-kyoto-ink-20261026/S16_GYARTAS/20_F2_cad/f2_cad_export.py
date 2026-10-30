#!/usr/bin/env python3
"""S16 F2 – CAD-export a gyártási adatmodellből (egy építési terv → három kimenet).

Bemenet:  ../10_F1_adatmodell/parts_v1.json (+ a benne hivatkozott forras_R15 geometria)
Kimenet:
  S16_R15_szerkezet.lsp     AutoLISP (ActiveX nélkül, AutoCAD for Mac-kompatibilis parancsok + entmake):
                            alkatrészenként egy 3D tömör test, saját rétegen ($PART_<címke-ID>#<él-kód>),
                            valódi ívekkel (LWPOLYLINE bulge), megmunkálások kivonva, TECH_* rétegen külön testként is.
  S16_R15_elonezet.dxf      ugyanaz MESH-ként (bárhol megnyitható előnézet, nem gyártási modell)
  cad_terv.json             az építési terv (amiből mindkettő készül)
  cad_ellenorzes.md         a tervből Pythonban újraépített testek ↔ a QA által ellenőrzött testek (térfogat, befoglaló)

A .lsp-t az élő AutoCAD-ben kell lefuttatni (APPLOAD → (s16-build)), utána a (s16-readback) MASSPROP-pal
visszaolvassa minden test térfogatát és befoglalóját – ezt a f2_readback.py veti össze a tervvel.
"""
from __future__ import annotations

import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
F1 = HERE.parent / "10_F1_adatmodell"
sys.path.insert(0, str(F1))
from s16_geom import box_mesh, build_solid, load_json  # noqa: E402

SEG_MM = 1.0  # ív-mintavétel a Python-oldali ellenőrzéshez

COLORS = {"M01": 8, "M02": 250, "M03": 34, "M04": 41, "M05": 51, "M07": 42, "M08": 9, "M10": 254, "M11": 250, "M12": 1}


# ------------------------------------------------------------------ geometriai segédek

def bulge_points(cv, seg=SEG_MM):
    from ezdxf.math import bulge_to_arc
    pts, n = [], len(cv)
    for i in range(n):
        x0, y0, b = cv[i]
        x1, y1, _ = cv[(i + 1) % n]
        pts.append((x0, y0))
        if abs(b) > 1e-9:
            c, _, _, r = bulge_to_arc((x0, y0), (x1, y1), b)
            ang = 4 * math.atan(b)
            k = max(4, int(abs(ang) * r / seg))
            a0 = math.atan2(y0 - c.y, x0 - c.x)
            for j in range(1, k):
                a = a0 + ang * j / k
                pts.append((c.x + r * math.cos(a), c.y + r * math.sin(a)))
    return pts


def poly_area_ok(cv, outline, tol_mm=0.3):
    """Valódi ív (bulge) ↔ R14 sokszögelt kontúr: a két határvonal legnagyobb távolsága (Hausdorff) ≤ tol_mm."""
    from shapely.geometry import Polygon
    from s16_geom import largest_polygon
    a = largest_polygon(Polygon(bulge_points(cv, seg=0.2)))
    b = largest_polygon(Polygon(outline))
    h = a.exterior.hausdorff_distance(b.exterior)
    return h <= tol_mm, round(h, 3)


def dedupe(pts, tol=1e-3):
    out = []
    for p in pts:
        if not out or abs(p[0] - out[-1][0]) > tol or abs(p[1] - out[-1][1]) > tol:
            out.append((round(p[0], 4), round(p[1], 4)))
    if len(out) > 1 and abs(out[0][0] - out[-1][0]) <= tol and abs(out[0][1] - out[-1][1]) <= tol:
        out.pop()
    return out


# ------------------------------------------------------------------ építési terv

def make_plan(doc, src_parts, rules):
    src = {p["id"]: p for p in src_parts}
    tpl = rules.get("cad", {}).get("reteg_minta", "$PART_{cimke_id}#{el_kod}")
    plan, notes = [], []
    for r in doc["alkatreszek"]:
        pid = r["id"]
        p = src[pid]
        x, y, z, dx, dy, dz = p["box"]
        item = {"id": pid, "reteg": tpl.format(cimke_id=r["cimke_id"], el_kod=r["el_kod"], id=pid),
                "szin": COLORS.get(r["anyag"]["kod"], 7), "anyag": r["anyag"]["kod"], "test": None,
                "kivonas": [], "tech": []}
        if p.get("outline") and p["axis"] == "y":
            cv = p.get("curve_vertices")
            use_bulge = False
            if cv:
                ok, diff = poly_area_ok(cv, p["outline"])
                use_bulge = ok
                if not ok:
                    notes.append(f"{pid}: curve_vertices ellentmond a kontúrnak (max. eltérés {diff} mm) – a sokszögelt kontúr készül")
            prof = ({"tipus": "bulge", "pontok": [[round(a, 4), round(b, 4), round(c, 9)] for a, b, c in cv]} if use_bulge
                    else {"tipus": "poly", "pontok": [[a, b, 0.0] for a, b in dedupe(p["outline"])]})
            item["test"] = {"tipus": "extrude_y", "origo": [x, y, z], "T": dy, "profil": prof}
            for i, c in enumerate(p.get("cutouts", [])):
                if c.get("type") == "through_contour":
                    item["kivonas"].append({"tipus": "extrude_y", "origo": [x, y - 1, z], "T": dy + 2,
                                            "profil": {"tipus": "poly", "pontok": [[a, b, 0.0] for a, b in dedupe(c["outline"])]},
                                            "op": "ATMENO_KIVAGAS"})
            rr = p.get("rear_light_rebate")
            if rr:
                pts = [[a - x, b - z, 0.0] for a, b in dedupe(rr["outline_xz_mm"])]
                item["kivonas"].append({"tipus": "extrude_y", "origo": [x, rr["y_mm"][0] - 1, z],
                                        "T": rr["y_mm"][1] - rr["y_mm"][0] + 1,
                                        "profil": {"tipus": "poly", "pontok": pts}, "op": "HATSO_FENYFALC"})
            elp = p.get("edge_light_pocket")
            if elp:
                bx = list(elp["box_mm"])
                hi_y = bx[1] + bx[4]
                bx2 = [bx[0] - 1, bx[1], bx[2] - 1, bx[3] + 1, bx[4] + (1 if abs(hi_y - (y + dy)) < 1e-6 else 0), bx[5] + 1]
                item["kivonas"].append({"tipus": "box", "box": bx2, "op": "FENYCSATORNA_FALC"})
        else:
            item["test"] = {"tipus": "box", "box": [x, y, z, dx, dy, dz]}
            if p.get("assembly_rebate"):
                item["kivonas"].append({"tipus": "box", "box": list(p["assembly_rebate"]), "op": "KIMETSZES"})
        for k in item["kivonas"]:
            item["tech"].append({"reteg": f"TECH_{k['op']}_{r['cimke_id']}", **{kk: vv for kk, vv in k.items() if kk != "op"}})
        plan.append(item)
    return plan, notes


# ------------------------------------------------------------------ Python-oldali újraépítés (ellenőrzés + DXF)

def _extrude_mesh(spec):
    import shapely
    import trimesh
    from shapely.geometry import Polygon
    from s16_geom import largest_polygon
    pr = spec["profil"]
    pts = bulge_points(pr["pontok"]) if pr["tipus"] == "bulge" else [(a, b) for a, b, _ in pr["pontok"]]
    poly = largest_polygon(shapely.set_precision(largest_polygon(Polygon(pts)), 0.001))
    m = trimesh.creation.extrude_polygon(poly, height=spec["T"])
    v = m.vertices
    x, y, z = spec["origo"]
    g = np.column_stack([x + v[:, 0], y + v[:, 2], z + v[:, 1]])
    return trimesh.Trimesh(vertices=g, faces=m.faces[:, ::-1], process=True)


def _mesh(spec):
    return box_mesh(spec["box"]) if spec["tipus"] == "box" else _extrude_mesh(spec)


def rebuild(item):
    import trimesh
    m = _mesh(item["test"])
    for k in item["kivonas"]:
        m = trimesh.boolean.difference([m, _mesh(k)], engine="manifold")
    return m


# ------------------------------------------------------------------ AutoLISP

LSP_HEAD = r''';;; S16 R15 médiafal – 3D szerkezeti modell (generálva: {datum}, f2_cad_export.py)
;;; STÁTUSZ: TERVI MODELL – nem gyártási kiadás. Forrás: parts_v1.json ({rev}).
;;; ActiveX (vla-*) nélkül: csak parancs + entmake – AutoCAD for Mac-en is fut.
;;; Használat: APPLOAD → ezt a fájlt → parancssor: (s16-build)   majd ellenőrzés: (s16-readback "<mappa>")
;;; Egység: mm. KOORDINÁTA: Y_CAD = -Y_helyi (egyetlen tükrözés). Az R14 helyi rendszer (X jobbra a szobából, Y faltól a szoba
;;; felé, Z fel) balkezes; jobbkezes AutoCAD-ben e nélkül a bútor tükörképe épülne. Így a fal síkja Y=0, a front -Y felé néz,
;;; az AutoCAD FRONT nézet = szobából nézett homlokzat (torony bal oldalt).

(defun s16-env ()
  (setvar "CMDECHO" 0) (setvar "OSMODE" 0) (setvar "INSUNITS" 4) (setvar "DELOBJ" 1)
  (command "_.UCS" "_W"))

(defun s16-layer (name col)
  (if (not (tblsearch "LAYER" name)) (command "_.-LAYER" "_M" name "_C" (itoa col) "" "") (command "_.-LAYER" "_S" name ""))
  (setvar "CLAYER" name))

(defun s16-box (x y z dx dy dz)
  (command "_.BOX" (list x y z) (list (+ x dx) (+ y dy) (+ z dz)))
  (entlast))

;; zárt LWPOLYLINE a WCS XY síkban; pts = ((u v bulge) ...)
(defun s16-lwpoly (pts / d)
  (setq d (list '(0 . "LWPOLYLINE") '(100 . "AcDbEntity") '(100 . "AcDbPolyline") (cons 90 (length pts)) '(70 . 1)))
  (foreach p pts (setq d (append d (list (list 10 (car p) (cadr p)) (cons 42 (caddr p))))))
  (entmake d)
  (entlast))

;; profil (U=X, V=Z) kihúzása T-vel, X körüli +90°-os forgatás: (u v n) -> (u -n v), majd tolás (x0 y0 z0)
(defun s16-extrude-y (pts tt x0 y0 z0 / pl s)
  ;; y0 itt már CAD-koordináta (= -Y_helyi), a test y0-tt .. y0 között lesz
  (setq pl (s16-lwpoly pts))
  (command "_.EXTRUDE" pl "" tt)
  (setq s (entlast))
  (command "_.ROTATE3D" s "" "_X" '(0 0 0) 90)
  (command "_.MOVE" s "" '(0 0 0) (list x0 y0 z0))
  s)

(defun s16-sub (a b) (command "_.SUBTRACT" a "" b "") a)

(defun s16-copy (e / last) (setq last (entlast)) (command "_.COPY" e "" '(0 0 0) '(0 0 0)) (entlast))

(defun s16-safe (s / r i c)
  ;; fájlnévhez: $ és # → _ (vl-string-* nélkül, Mac-kompatibilis)
  (setq r "" i 1)
  (while (<= i (strlen s))
    (setq c (substr s i 1))
    (setq r (strcat r (if (member c '("$" "#")) "_" c)) i (1+ i)))
  r)

(defun s16-readback (dir / ss i e lay n)
  ;; minden $PART_ 3D test MASSPROP-ja külön fájlba: <dir>/<réteg>.mpr (AutoCAD tömegjellemző-szöveg, NEM woodWOP MPR)
  (setvar "FILEDIA" 0)
  (setq ss (ssget "_X" '((0 . "3DSOLID"))) i 0 n 0)
  (if ss
    (while (< i (sslength ss))
      (setq e (ssname ss i) lay (cdr (assoc 8 (entget e))))
      (if (= (substr lay 1 6) "$PART_")
        (progn (command "_.MASSPROP" e "" "_Y" (strcat dir "/" (s16-safe lay))) (setq n (1+ n))))
      (setq i (1+ i))))
  (setvar "FILEDIA" 1)
  (princ (strcat "\nS16 readback: " (itoa n) " test kiirva ide: " dir))
  (princ))

(defun s16-smoketest ( / a b c)
  ;; parancs-próba a teljes build előtt: hasáb, íves (bulge) kihúzás, kivonás – várt értékek a 30_eredmenyek-ben
  (s16-env)
  (s16-layer "$PART_SMOKE_BOX#0000" 3)
  (setq a (s16-box 0 -300 0 400 18 600))
  (s16-layer "$PART_SMOKE_ARC#0000" 4)
  (setq c (s16-extrude-y (list (list 0 0 0) (list 100 0 0.414213562) (list 200 100 0) (list 200 200 0) (list 0 200 0)) 18 600 -18 0))
  (s16-layer "$PART_SMOKE_SUB#0000" 5)
  (setq a (s16-box 1000 -300 0 400 18 600))
  (setq b (s16-box 1100 -310 100 200 38 400))
  (s16-sub a b)
  (command "_.ZOOM" "_E")
  (princ "\nS16 smoketest kesz: 3 test. Futtasd: (s16-readback \"<mappa>\")")
  (princ))
'''


def lsp_pts(pts):
    return "(list " + " ".join(f"(list {a:.4f} {b:.4f} {c:.9f})" for a, b, c in pts) + ")"


def lsp_shape(spec, var):
    # CAD-tükrözés: Y_CAD = -Y_helyi
    if spec["tipus"] == "box":
        x, y, z, dx, dy, dz = spec["box"]
        return f"(setq {var} (s16-box {x} {-(y + dy)} {z} {dx} {dy} {dz}))"
    x, y, z = spec["origo"]
    return f"(setq {var} (s16-extrude-y {lsp_pts(spec['profil']['pontok'])} {spec['T']} {x} {-y} {z}))"


def write_lsp(plan, path, rev):
    L = [LSP_HEAD.replace("{datum}", date.today().isoformat()).replace("{rev}", rev),
         "(defun s16-build ( / a b)", "  (s16-env)"]
    for it in plan:
        L.append(f"  ;; {it['id']}")
        for t in it["tech"]:
            L.append(f"  (s16-layer \"{t['reteg']}\" 1)")
            L.append("  " + lsp_shape(t, "b"))
        L.append(f"  (s16-layer \"{it['reteg']}\" {it['szin']})")
        L.append("  " + lsp_shape(it["test"], "a"))
        for k in it["kivonas"]:
            L.append(f"  (s16-layer \"{it['reteg']}\" {it['szin']})")
            L.append("  " + lsp_shape(k, "b"))
            L.append("  (s16-sub a b)")
    L += ["  (command \"_.ZOOM\" \"_E\")", f"  (princ \"\\nS16 R15: {len(plan)} alkatrész felépítve.\")", "  (princ))",
          "(princ \"\\nS16 betöltve: (s16-build) majd (s16-readback \\\"/Users/<te>/CAD/s16_readback\\\")\")", "(princ)"]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ DXF előnézet

def write_dxf(plan, meshes, path):
    import ezdxf
    doc = ezdxf.new("R2018", setup=True)
    doc.header["$INSUNITS"] = 4
    msp = doc.modelspace()
    for it in plan:
        lay = it["reteg"].replace("#", "_")
        if lay not in doc.layers:
            doc.layers.add(lay, color=it["szin"])
        m = meshes[it["id"]]
        e = msp.add_mesh(dxfattribs={"layer": lay})
        with e.edit_data() as md:
            md.vertices = [(float(v[0]), float(-v[1]), float(v[2])) for v in m.vertices]   # Y_CAD = -Y_helyi
            md.faces = [tuple(f[::-1]) for f in m.faces]                                  # tükrözés → körüljárás fordítás
    doc.saveas(path)


# ------------------------------------------------------------------ main

def main():
    doc = load_json(F1 / "parts_v1.json")
    rules = load_json(F1 / "gyartasi_szabalyok_v1.json")
    srcdir = F1 / doc["forras"]["mappa"]
    src_parts = load_json(srcdir / "parts.json")
    zart = {o["name"]: o for o in load_json(next(srcdir.glob("*_ZART_JELENET_MM.json")))["objects"]}

    plan, notes = make_plan(doc, src_parts, rules)
    (HERE / "cad_terv.json").write_text(json.dumps({"modell_revizio": doc["modell_revizio"], "datum": date.today().isoformat(),
                                                    "megjegyzesek": notes, "alkatreszek": plan}, ensure_ascii=False, indent=1), encoding="utf-8")
    write_lsp(plan, HERE / "S16_R15_szerkezet.lsp", doc["modell_revizio"])

    srcp = {p["id"]: p for p in src_parts}
    rows, meshes, worst = [], {}, 0.0
    for it in plan:
        m = rebuild(it)
        meshes[it["id"]] = m
        ref = build_solid(srcp[it["id"]], zart.get(it["id"]))
        rv = abs(ref.mesh.volume) if ref.mesh is not None else float(np.prod(ref.hi - ref.lo))
        dv = (abs(m.volume) - rv) / rv * 100 if rv else 0.0
        db = float(max(np.abs(m.bounds[0] - ref.lo).max(), np.abs(m.bounds[1] - ref.hi).max()))
        worst = max(worst, abs(dv))
        rows.append((it["id"], it["reteg"], it["test"]["tipus"] + ("/bulge" if it["test"].get("profil", {}).get("tipus") == "bulge" else ""),
                     len(it["kivonas"]), round(abs(m.volume)), round(rv), round(dv, 3), round(db, 3), m.is_watertight))
    write_dxf(plan, meshes, HERE / "S16_R15_elonezet.dxf")

    bad = [r for r in rows if abs(r[6]) > 0.5 or r[7] > 0.05 or not r[8]]
    L = [f"# S16 F2 – CAD-terv önellenőrzés ({doc['modell_revizio']})", "",
         f"Generálva: {date.today().isoformat()} · `f2_cad_export.py` · {len(plan)} alkatrész", "",
         "A `cad_terv.json`-ból Pythonban újraépített testet (ugyanaz a terv, amiből a .lsp készül) összevetem a QA által ellenőrzött "
         "testtel (R14/R15 zárt jelenet hálója vagy kontúr-extrudálás). Ez a terv helyességét bizonyítja; az AutoCAD-beli "
         "végrehajtást a `(s16-readback)` + `f2_readback.py` igazolja majd.", "",
         f"**Eredmény: {len(rows) - len(bad)}/{len(rows)} egyezik** (térfogat ≤ 0,5 %, befoglaló ≤ 0,05 mm, zárt test); legnagyobb térfogat-eltérés {worst:.3f} %.", ""]
    if notes:
        L += ["## Megjegyzések", ""] + [f"- {n}" for n in notes] + [""]
    if bad:
        L += ["## Eltérések", "", "| ID | térfogat terv | ref | Δ% | befoglaló Δ mm | zárt |", "|---|---|---|---|---|---|"]
        L += [f"| {r[0]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} | {r[8]} |" for r in bad] + [""]
    L += ["## Alkatrészek", "", "| ID | réteg | test | kivonás | térfogat mm³ | ref mm³ | Δ% | befoglaló Δ mm |", "|---|---|---|---|---|---|---|---|"]
    L += [f"| {r[0]} | `{r[1]}` | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |" for r in rows]
    (HERE / "cad_ellenorzes.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"terv: {len(plan)} · egyezik {len(rows) - len(bad)}/{len(rows)} · max Δ {worst:.3f}% · megjegyzés: {len(notes)}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
