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

import os
CODE = Path(__file__).resolve().parent
# WSG_GYARTAS=<…_GYARTAS mappa> esetén másik szekrényre fut (pl. R16_GYARTAS); kimenet: <mappa>/20_F2_cad
BASE = Path(os.environ["WSG_GYARTAS"]).resolve() if os.environ.get("WSG_GYARTAS") else CODE.parent
HERE = BASE / "20_F2_cad"
HERE.mkdir(exist_ok=True)
F1 = BASE / "10_F1_adatmodell"
sys.path.insert(0, str(CODE.parent / "10_F1_adatmodell"))
from s16_geom import box_mesh, build_solid, etalon_el_kod, load_json  # noqa: E402

PREFIX = "S16"
SZINES_DX = 0   # a műhelyi (típusszínes) másolat X-eltolása a modelltérben; main() állítja
SEG_MM = 1.0  # ív-mintavétel a Python-oldali ellenőrzéshez

# valós (render-) színek: a materials.json hex-értéke; ahol nincs (R16), KÖZELÍTŐ képernyőszín a leírásból – nem színminta
SZIN_KOZELITO = {"M01": "#5e5247", "M01+nyomat": "#5e5247", "M16-BRONZE": "#5e5247",   # matt bronzbarna, NCS S 7005-Y20R körül
                 "M02": "#7a6d5e", "M03": "#504942", "M03-8": "#504942", "BEECH18": "#cfae84",
                 "PLY18": "#c4af8b", "M16-DRAWER15": "#c4af8b"}
VASALAT_SZIN = "140,140,140"
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

# műhelyi típusszínek az asztalos coo1.dwg rétegszínei szerint (ACI): Oldal 40, Polc 145, Tető 173, Fenék 104, Front 81,
# Hátlemez 17, Kötő 153, Lábazat 51, Vosztó 93, Fiókfenék 65, Fiókhát 55 – kiegészítve: Fiókoldal 40, Keret 33, Burkolat 31, Fény 121
TIPUS_SZIN = [("Fiókfenék", 65, r"fiók ?fenék|fiókfenék"), ("Fiókhát", 55, r"dobozelő|fiókdoboz|fiók.*(hát|elő)"), ("Fiókoldal", 40, r"fiók.*oldal|fiókoldal"),
              ("Front", 81, r"front|ajtó"), ("Polc", 145, r"polc"), ("Tető", 173, r"tető|sapka|fedő"), ("Fenék", 104, r"fenék"),
              ("Hátlemez", 17, r"\bhát|hátlap|szervizfedél|háttérpanel|kazettahát|hordozópanel"), ("Kötő", 153, r"léc|merevítő|távtartó|falsín"),
              ("Lábazat", 51, r"lábazat|talp"), ("Vosztó", 93, r"osztó"), ("Oldal", 40, r"oldal"), ("Keret", 33, r"keret|sarok|záróelem"),
              ("Fény", 121, r"fény|tálca|baffle|visor"), ("Burkolat", 31, r"burkolat|szövet|textil|tv-mező|réteg|sáv")]


def tipus_of(r):
    import re
    name = r["megnevezes"].lower()
    for t, c, rx in TIPUS_SZIN:
        if re.search(rx, name):
            return t, c
    a = r["helyi_rendszer"]["A_normal"]
    if a in ("+X", "-X"):
        return "Oldal", 40
    if a in ("+Z", "-Z"):
        return "Polc", 145
    return ("Front", 81) if a == "+Y" else ("Hátlemez", 17)


def _rgb(hx):
    if not hx:
        return None
    return '"' + ",".join(str(int(hx[i:i + 2], 16)) for i in (1, 3, 5)) + '"'


def make_plan(doc, src_parts, rules):
    src = {p["id"]: p for p in src_parts}
    # etalon (km.dwg): $PART_<név>˙0˙0¨<élkód>˙0¨#0¨<azonosító>
    tpl = rules.get("cad", {}).get("reteg_minta", "$PART_{cimke_id}\u02d90\u02d90\u00a8{el_kod}\u02d90\u00a8#0\u00a8{num}")
    num0 = rules.get("cad", {}).get("azonosito_kezdet", 16001)
    plan, notes = [], []
    rgb = {}
    try:
        mats = load_json(F1 / doc["forras"]["mappa"] / "materials.json")
        for row in mats:
            hx = next((c for c in row if isinstance(c, str) and len(c) == 7 and c.startswith("#")), None)
            if hx:
                rgb[row[0]] = hx
    except Exception:
        pass
    for r in doc["alkatreszek"]:
        pid = r["id"]
        p = src[pid]
        x, y, z, dx, dy, dz = p["box"]
        num = num0 + len(plan)
        ek, _ = etalon_el_kod(r)
        tip, tcol = tipus_of(r)
        item = {"id": pid, "num": num, "reteg": tpl.format(cimke_id=r["cimke_id"], el_kod=ek, id=pid, num=num), "el_kod_etalon": ek, "tipus": tip, "tipus_szin": tcol,
                "szin": _rgb(rgb.get(r["anyag"]["kod"]) or SZIN_KOZELITO.get(r["anyag"]["kod"]))
                or COLORS.get(r["anyag"]["kod"], 10 + (sum(map(ord, r["anyag"]["kod"])) * 37) % 240), "anyag": r["anyag"]["kod"], "test": None,
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
  (if (not (tblsearch "LAYER" name))
    (if (= (type col) 'STR) (command "_.-LAYER" "_M" name "_C" "_T" col "" "") (command "_.-LAYER" "_M" name "_C" (itoa col) "" ""))
    (command "_.-LAYER" "_S" name ""))
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

;; henger két pont között (tengely), r sugár – furatokhoz, tiplikhez
(defun s16-cyl (x y z r x2 y2 z2) (command "_.CYLINDER" (list x y z) r "_A" (list x2 y2 z2)) (entlast))

;; blokk a megadott (a 0 rétegen, WCS-origóban épített) testekből; ha már létezik, a testeket törli
(defun s16-blk (name ents / ss)
  (setq ss (ssadd))
  (foreach e ents (if e (ssadd e ss)))
  (if (tblsearch "BLOCK" name) (command "_.ERASE" ss "") (command "_.-BLOCK" name '(0 0 0) ss ""))
  name)

;; blokkhivatkozás tetszőleges térbeli irányba: a blokk +Z tengelye = dir (WCS), a pont WCS-ben
(defun s16-ins (name lay pt dir rot xs)
  (entmake (list (cons 0 "INSERT") (cons 2 name) (cons 8 lay) (cons 10 (trans pt 0 dir))
                 (cons 41 xs) (cons 42 1.0) (cons 43 1.0) (cons 50 rot) (cons 210 dir))))

(defun s16-count-ins (name / ss) (setq ss (ssget "_X" (list (cons 0 "INSERT") (cons 2 name)))) (if ss (sslength ss) 0))

(defun s16-count (pre / ss i n e)
  (setq ss (ssget "_X" '((0 . "3DSOLID"))) i 0 n 0)
  (if ss (while (< i (sslength ss)) (setq e (ssname ss i)) (if (wcmatch (cdr (assoc 8 (entget e))) (strcat pre "*")) (setq n (1+ n))) (setq i (1+ i))))
  n)

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


def lstr(text):
    """AutoLISP-string: az AcCoreConsole a szkriptet Latin-1-ként olvassa → minden nem ASCII karakter \\U+XXXX."""
    out = []
    for ch in text:
        if ch in '"\\':
            out.append("\\" + ch)
        elif ord(ch) < 128:
            out.append(ch)
        else:
            out.append("\\U+%04X" % ord(ch))
    return '"' + "".join(out) + '"'


def lsp_pts(pts):
    return "(list " + " ".join(f"(list {a:.4f} {b:.4f} {c:.9f})" for a, b, c in pts) + ")"


CHUNK = 40  # AcCoreConsole kb. 4 KB-nál levágja a szkriptsort → a pontlista részletekben épül


def lsp_shape(spec, var):
    """Egy vagy több (soronként teljes) LISP-kifejezés '\n'-nel elválasztva. CAD-tükrözés: Y_CAD = -Y_helyi."""
    if spec["tipus"] == "box":
        x, y, z, dx, dy, dz = spec["box"]
        return f"(setq {var} (s16-box {x} {-(y + dy)} {z} {dx} {dy} {dz}))"
    x, y, z = spec["origo"]
    pts = spec["profil"]["pontok"]
    lines = ["(setq s16p nil)"]
    for i in range(0, len(pts), CHUNK):
        lines.append(f"(setq s16p (append s16p {lsp_pts(pts[i:i + CHUNK])}))")
    lines.append(f"(setq {var} (s16-extrude-y s16p {spec['T']} {x} {-y} {z}))")
    return "\n  ".join(lines)


def write_lsp(plan, path, rev):
    L = [LSP_HEAD.replace("{datum}", date.today().isoformat()).replace("{rev}", rev),
         "(defun s16-build ( / a b)", "  (s16-env)"]
    for it in plan:
        L.append(f"  ;; {it['id']}")
        for t in it["tech"]:
            L.append(f"  (s16-layer {lstr(t['reteg'])} 1)")
            L.append("  " + lsp_shape(t, "b"))
        L.append(f"  (s16-layer {lstr(it['reteg'])} {it['szin']})")
        L.append("  " + lsp_shape(it["test"], "a"))
        for k in it["kivonas"]:
            L.append(f"  (s16-layer {lstr(it['reteg'])} {it['szin']})")
            L.append("  " + lsp_shape(k, "b"))
            L.append("  (s16-sub a b)")
        if SZINES_DX:
            L.append(f"  (s16-layer {lstr('SZINES_' + it['tipus'])} {it['tipus_szin']})")
            L.append(f"  (command \"_.COPY\" a \"\" '(0 0 0) '({SZINES_DX} 0 0)) (command \"_.CHPROP\" (entlast) \"\" \"_LA\" {lstr('SZINES_' + it['tipus'])} \"\")")
    L += ["  (command \"_.ZOOM\" \"_E\")", f"  (princ \"\\n{rev}: {len(plan)} alkatrész felépítve.\")", "  (princ))",
          "(princ \"\\nS16 betöltve: (s16-build) majd (s16-readback \\\"/Users/<te>/CAD/s16_readback\\\")\")", "(princ)"]
    path.write_text("\n".join(L) + "\n", encoding="utf-8")
    # a s16-build törzse soronként (AcCoreConsole-szkripthez, hogy ne egy óriási sor legyen)
    out = []
    for x in L[2:]:
        for y in x.split("\n"):
            if y.startswith("  (") and not y.strip().startswith("(princ"):
                out.append(y.strip())
    return out


# ------------------------------------------------------------------ DXF előnézet

def write_dxf(plan, meshes, path):
    import ezdxf
    doc = ezdxf.new("R2018", setup=True)
    doc.header["$INSUNITS"] = 4
    msp = doc.modelspace()
    for it in plan:
        lay = it["reteg"].replace("#", "_")
        if lay not in doc.layers:
            doc.layers.add(lay, color=it["szin"] if isinstance(it["szin"], int) else 7)
        m = meshes[it["id"]]
        e = msp.add_mesh(dxfattribs={"layer": lay})
        with e.edit_data() as md:
            md.vertices = [(float(v[0]), float(-v[1]), float(v[2])) for v in m.vertices]   # Y_CAD = -Y_helyi
            md.faces = [tuple(f[::-1]) for f in m.faces]                                  # tükrözés → körüljárás fordítás
    doc.saveas(path)


# ------------------------------------------------------------------ AcCoreConsole-szkript (.scr)

def lisp_forms(text):
    """Felső szintű LISP-kifejezések, kommentek nélkül, egy sorba tömörítve (AcCoreConsole-hoz)."""
    forms, buf, depth, in_str, esc, i = [], [], 0, False, False, 0
    while i < len(text):
        c = text[i]
        if in_str:
            buf.append(c)
            if esc:
                esc = False
            elif c == "\\":
                esc = True
            elif c == '"':
                in_str = False
        elif c == ";":
            while i < len(text) and text[i] != "\n":
                i += 1
            buf.append(" ")
            continue
        elif c == '"':
            in_str = True
            buf.append(c)
        elif c == "(":
            depth += 1
            buf.append(c)
        elif c == ")":
            depth -= 1
            buf.append(c)
            if depth == 0:
                forms.append(" ".join("".join(buf).split()))
                buf = []
        elif depth > 0:
            buf.append(" " if c in "\r\n\t" else c)
        i += 1
    assert depth == 0 and not in_str, "kiegyensúlyozatlan zárójel"
    return forms


PRESENTATION = [
    # modelltér: délnyugati axonometria, realisztikus megjelenítés
    '(command "_.-VIEW" "_SWISO")',
    '(command "_.VSCURRENT" "_R")',
    '(command "_.ZOOM" "_E")',
    # áttekintő rajzlap 4 nézettel (elöl / bal / felül / axonometria)
    '(command "_.-LAYOUT" "_N" "S16_ATTEKINTES")',
    '(setvar "CTAB" "S16_ATTEKINTES")',
    '(command "_.ERASE" (ssget "_X" (list (cons 0 "VIEWPORT") (cons 410 "S16_ATTEKINTES"))) "")',
    '(command "_.MVIEW" "_4" "_F")',
    '(command "_.MSPACE")',
    '(setvar "CVPORT" 2) (command "_.-VIEW" "_FRONT") (command "_.VSCURRENT" "_H") (command "_.ZOOM" "_E")',
    '(setvar "CVPORT" 3) (command "_.-VIEW" "_LEFT") (command "_.VSCURRENT" "_H") (command "_.ZOOM" "_E")',
    '(setvar "CVPORT" 4) (command "_.-VIEW" "_TOP") (command "_.VSCURRENT" "_H") (command "_.ZOOM" "_E")',
    '(setvar "CVPORT" 5) (command "_.-VIEW" "_SWISO") (command "_.VSCURRENT" "_R") (command "_.ZOOM" "_E")',
    '(command "_.PSPACE")',
    '(entmake (list (cons 0 "TEXT") (cons 67 1) (cons 410 "S16_ATTEKINTES") (cons 10 (list 10.0 5.0 0.0)) (cons 40 3.5) '
    '(cons 1 "S16 R15 mediafal - szerkezeti 3D modell - TERVI, NEM GYARTASI KIADAS - 129 alkatresz")))',
]


def write_scr(lsp_path, calls, scr_path, dwg_path, presentation=None):
    forms = lisp_forms(lsp_path.read_text(encoding="utf-8"))
    forms = [f for f in forms if not f.startswith("(princ") and not f.startswith("(defun s16-build")]
    if presentation:
        calls = calls + presentation
    lines = ['(setvar "FILEDIA" 0)', '(setvar "CMDECHO" 0)'] + forms + calls + [
        f'(command "_.SAVEAS" "2018" "{dwg_path}")', '(princ "S16_SAVE_DONE")', "_.QUIT", "_Y"]
    scr_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(forms)


# ------------------------------------------------------------------ F2b: furatok (TECH_*) és vasalat ($ITEM_REF_*)

def _p(v):
    """helyi → CAD (Y tükrözés)"""
    return f"{v[0]:.3f} {-v[1]:.3f} {v[2]:.3f}"


# vasalat-blokkok az etalon (km.dwg) mintájára: név = cikkszám, réteg $ITEM_REF (tipli, pánt) / $ART_ (talp, polctartó, sín).
# Geometria: SEMATIKUS BURKOLÓ (befoglaló méret, nem gyári modell) – a gyári 3D a Blum/Häfele CAD-letöltésből cserélhető.
BLOKK_SABLON = {
    "TIPLI": lambda h: [f"(s16-cyl 0 0 0 4.0 0 0 {h})"],
    "POLC": lambda _: ["(s16-cyl 0 0 0 2.5 0 0 10)", "(s16-box -5 -3 -6 10 6 6)"],
    "PANT": lambda _: ["(s16-cyl 0 0 0 17.5 0 0 12.5)", "(s16-box -22 -12 -37 30 24 37)"],
    "TALP": lambda _: ["(s16-box -22.5 -25 -10 45 50 10)"],
    "SIN": lambda _: ["(s16-box 0 -150 -13 27 300 13)"],
    "CSAVAR": lambda h: [f"(s16-cyl 0 0 0 2.0 0 0 {h})"],
    "DOBOZ": lambda d: [f"(s16-box 0 0 0 {d[0]} {d[1]} {d[2]})"],
}
BLOKKOK = {}   # név → geometria-sorok (a futás tölti)


def _cad(v):
    return [float(v[0]), -float(v[1]), float(v[2])]


def _l(v):
    return "(list " + " ".join(f"{c:.3f}" for c in v) + ")"


def _cikk(text, n=0):
    import re
    m = re.findall(r"\b(\d{2,3}[A-Z]\d{3,4}[A-Z0-9.]*)", text or "")
    return m[n] if len(m) > n else None


def hardware_lines(vas, plan, doc=None, drawers=None):
    import re
    import numpy as np
    L, ins = [], []
    cur = None
    n = {}

    def lay(name, col):
        nonlocal cur
        if name != cur:
            L.append(f"(s16-layer {lstr(name)} {col})")
            cur = name

    def blk(name, kind, arg=None):
        if name not in BLOKKOK:
            BLOKKOK[name] = BLOKK_SABLON[kind](arg)
        n[name] = n.get(name, 0) + 1
        return lstr(name)

    for h in vas["furatok"]:
        st, d = np.array(h["start"]), np.array(h["irany"])
        en = st + d * h["melyseg"]
        lay(f"TECH_{h['funkcio']}_{PREFIX}_{h['alkatresz']}", 1)
        L.append(f"(s16-cyl {_p(st)} {h['d'] / 2} {_p(en)})")
    F = vas["furatok"]
    for w in vas["vasalat"]:
        t = w["tipus"]
        if t.startswith("TIPLI"):
            g = w.get("geometria") or {}
            hh = int(g.get("hossz") or re.search(r"x(\d+)", t).group(1))
            lm = float(g.get("lap_melyseg", 12.0))
            st, d = np.array(w["pozicio"], float), np.array(w["irany"], float)
            nm = blk(f"TIPLI_D8_L{hh}_BORD\u00c1S", "TIPLI", hh)
            ins.append(f"(s16-ins {nm} \"$ITEM_REF\" {_l(_cad(st - d * (hh - lm + 1)))} {_l(_cad(d))} 0.0 1.0)")
        elif t.startswith("CSAVAR") and w.get("pozicio") and w.get("irany"):
            hh = int(re.search(r"x(\d+)", t).group(1))
            nm = blk(t, "CSAVAR", hh)
            ins.append(f"(s16-ins {nm} \"$ITEM_REF\" {_l(_cad(w['pozicio']))} {_l(_cad(w['irany']))} 0.0 1.0)")
        elif t == "PANT_CLIPTOP_110":
            cup = np.array(w["pozicio"], float)
            kehely = next(h for h in F if h["funkcio"] == "PANTKEHELY" and h["kapcsolat"] == w["kapcsolat"])
            talp = [h for h in F if h["funkcio"] == "PANTTALP" and h["kapcsolat"] == w["kapcsolat"]]
            dur = next((h for h in F if h["funkcio"] in ("PANT_DUBEL", "PANT_CSAVAR") and h["kapcsolat"] == w["kapcsolat"]), None)
            rot = 0.0 if (dur is None or dur["start"][0] > cup[0]) else math.pi
            if w.get("kez") in ("L", "R"):
                rot = 0.0 if w["kez"] == "L" else math.pi
            nm = blk(_cikk(w["cikkszam"]) or "PANT_CLIPTOP_110", "PANT")
            ins.append(f"(s16-ins {nm} \"$ITEM_REF\" {_l(_cad(cup))} {_l(_cad(kehely['irany']))} {rot:.6f} 1.0)")
            if len(talp) == 2:
                c = (np.array(talp[0]["start"], float) + np.array(talp[1]["start"], float)) / 2
                tn = w.get("talp_cikkszam") and _cikk(w["talp_cikkszam"]) or _cikk(w["cikkszam"], 1) or "PANTTALP"
                nm = blk(tn, "TALP")
                ins.append(f"(s16-ins {nm} \"$ART_\" {_l(_cad(c))} {_l(_cad(talp[0]['irany']))} 0.0 1.0)")
        elif w.get("befoglalo_globalis") and str(w.get("kategoria", "")).startswith("BEFOGLALO"):
            x, y, z, dx, dy, dz = w["befoglalo_globalis"]
            nm0 = re.sub(r"[^A-Za-z0-9_.\-]", "_", t)[:40]
            nm = f"{nm0}_{dx:g}x{dy:g}x{dz:g}".replace(".", "p")
            nm = blk(nm, "DOBOZ", (dx, dy, dz))
            ins.append(f"(s16-ins {nm} \"$ART_\" {_l([x, -(y + dy), z])} (list 0.0 0.0 1.0) 0.0 1.0)")
    for h in F:
        if h["funkcio"] == "POLCTARTO":
            nm = blk("de_11090", "POLC")
            ins.append(f"(s16-ins {nm} \"$ART_\" {_l(_cad(h['start']))} {_l(_cad(h['irany']))} 0.0 1.0)")
    has_runner = any(w["tipus"].startswith("760H") for w in vas["vasalat"])
    if doc is not None and drawers and not has_runner:
        R = {r["id"]: r for r in doc["alkatreszek"]}
        for dr in drawers:
            m = dr["id"]
            sl, sr, bl = R.get(f"{m}-L"), R.get(f"{m}-R"), R.get(f"{m}-BOX-L")
            if not (sl and sr and bl and dr.get("NL")):
                continue
            front = sl["befoglalo_globalis"][1] + sl["befoglalo_globalis"][4]
            yc = front - 3 - dr["NL"] / 2
            zb = bl["befoglalo_globalis"][2]
            xl = sl["befoglalo_globalis"][0] + sl["befoglalo_globalis"][3]
            xr = sr["befoglalo_globalis"][0]
            for x, xs in ((xl, 1.0), (xr, -1.0)):
                nm = blk("760H3000S", "SIN")
                ins.append(f"(s16-ins {nm} \"$ART_\" {_l(_cad([x, yc, zb]))} (list 0.0 0.0 1.0) 0.0 {xs})")
    L.append(f"(s16-layer \"$ITEM_REF\" \"{VASALAT_SZIN}\")")
    L.append(f"(s16-layer \"$ART_\" \"{VASALAT_SZIN}\")")
    cur = None
    lay("0", 7)
    for name, geo in BLOKKOK.items():
        L.append(f"(s16-blk {lstr(name)} (list " + " ".join(geo) + "))")
    return L + ins, n


# ------------------------------------------------------------------ rajzlapok pecséttel (A4 fekvő, mint az etalon)

SHEETS = [
    ("S16_L01_ATTEKINTES", "Áttekintés – teljes médiafal", None, ("_FRONT", "_TOP", "_SWISO")),
    ("S16_L02_TORONY", "Bal torony – ajtók, polcok, ívek", ("TORONY", "TORONY_KERET"), ("_FRONT", "_LEFT", "_SWISO")),
    ("S16_L03_ALSO_SOR", "Alsó fiókos sor D1–D6", ("D1", "D2", "D3", "D4", "D5", "D6", "ALSO_KERET"), ("_FRONT", "_TOP", "_SWISO")),
    ("S16_L04_HATTER_TV", "Háttérpanelek, falsínek, TV-mező", ("HATTER", "TV"), ("_FRONT", "_LEFT", "_SWISO")),
]
VP_RECTS = [((-13, 33), (168, 198)), ((171, 100), (270, 198)), ((171, 33), (270, 97))]
VIEW_NAME = {"_FRONT": "ELÖLNÉZET (szobából)", "_LEFT": "OLDALNÉZET (balról)", "_TOP": "FELÜLNÉZET", "_SWISO": "AXONOMETRIA"}


def _ptxt(lay, x, y, h, txt):
    return (f"(entmake (list (cons 0 \"TEXT\") (cons 67 1) (cons 410 {lstr(lay)}) (cons 8 \"S16_PECSET\") "
            f"(cons 10 (list {x} {y} 0.0)) (cons 40 {h}) (cons 1 {lstr(txt)})))")


def _pline(lay, pts, closed=True):
    v = " ".join(f"(cons 10 (list {x} {y}))" for x, y in pts)
    return (f"(entmake (list (cons 0 \"LWPOLYLINE\") (cons 100 \"AcDbEntity\") (cons 67 1) (cons 410 {lstr(lay)}) (cons 8 \"S16_PECSET\") "
            f"(cons 100 \"AcDbPolyline\") (cons 90 {len(pts)}) (cons 70 {1 if closed else 0}) {v}))")


# SH_STAMP: az etalon pecsétblokkjával azonos név és attribútumok (SH_TITLE, SH_SUBSET, SH_PRNAME, SH_PRNUM, SH_DATE)
STAMP_ATTR = [("SH_TITLE", 3.0, 2, 29.0), ("SH_SUBSET", 2.5, 2, 20.5), ("SH_PRNAME", 2.0, 2, 12.5), ("SH_PRNUM", 2.0, 2, 7.0),
              ("SH_DATE", 1.5, 2, 2.0)]


def stamp_block_lines():
    L = ['(if (not (tblsearch "BLOCK" "SH_STAMP")) (progn',
         '(entmake (list (cons 0 "BLOCK") (cons 2 "SH_STAMP") (cons 70 2) (cons 10 (list 0.0 0.0 0.0))))',
         '(entmake (list (cons 0 "LWPOLYLINE") (cons 100 "AcDbEntity") (cons 8 "0") (cons 100 "AcDbPolyline") (cons 90 4) (cons 70 1) '
         '(cons 10 (list 0.0 0.0)) (cons 10 (list 125.0 0.0)) (cons 10 (list 125.0 35.0)) (cons 10 (list 0.0 35.0))))']
    for yy in (26.5, 18, 11, 5.5):
        L.append(f'(entmake (list (cons 0 "LINE") (cons 8 "0") (cons 10 (list 0.0 {yy} 0.0)) (cons 11 (list 125.0 {yy} 0.0))))')
    for tag, h, x, y in STAMP_ATTR:
        L.append(f'(entmake (list (cons 0 "ATTDEF") (cons 8 "0") (cons 10 (list {x}.0 {y} 0.0)) (cons 40 {h}) (cons 1 "####") '
                 f'(cons 3 "{tag}") (cons 2 "{tag}") (cons 70 0)))')
    L += ['(entmake (list (cons 0 "ENDBLK")))', '))']
    return [" ".join(L)]


def stamp_insert(lay, vals):
    L = [f'(entmake (list (cons 0 "INSERT") (cons 2 "SH_STAMP") (cons 66 1) (cons 67 1) (cons 410 {lstr(lay)}) (cons 8 "S16_PECSET") '
         f'(cons 10 (list 147.0 -5.0 0.0))))']
    for tag, h, x, y in STAMP_ATTR:
        L.append(f'(entmake (list (cons 0 "ATTRIB") (cons 67 1) (cons 410 {lstr(lay)}) (cons 8 "S16_PECSET") '
                 f'(cons 10 (list {147 + x}.0 {y - 5} 0.0)) (cons 40 {h}) (cons 1 {lstr(vals[tag])}) (cons 2 "{tag}") (cons 70 0)))')
    L.append('(entmake (list (cons 0 "SEQEND") (cons 8 "S16_PECSET") (cons 67 1)))')
    return L


def auto_sheets(doc):
    """Ha nincs kézi lapkiosztás (más szekrény): áttekintő + modulcsoportonként egy lap (max. 5)."""
    from collections import Counter
    mods = [m for m, _ in Counter(r["modul"] for r in doc["alkatreszek"]).most_common()]
    groups = [mods[i::4] for i in range(min(4, len(mods)))]
    out = [(f"{PREFIX}_L01_ATTEKINTES", "Áttekintés – teljes szekrény", None, ("_FRONT", "_TOP", "_SWISO"))]
    for k, g in enumerate(groups, 2):
        out.append((f"{PREFIX}_L{k:02d}_{'_'.join(g)[:20]}", "Modulok: " + ", ".join(g), tuple(g), ("_FRONT", "_LEFT", "_SWISO")))
    return out


def sheet_lines(doc, open_items, sheets, cim):
    import numpy as np
    parts = doc["alkatreszek"]
    L = ['(command "_.-VIEW" "_SWISO")', '(command "_.VSCURRENT" "_R")', '(command "_.ZOOM" "_E")',
         '(command "_.-LAYER" "_M" "S16_PECSET" "_C" "7" "" "")'] + stamp_block_lines()
    for no, (lay, title, mods, views, *rest) in enumerate(sheets, 1):
        dx = rest[0] if rest else 0
        sel = [r for r in parts if mods is None or r["modul"] in mods]
        lo = np.min([r["befoglalo_globalis"][:3] for r in sel], axis=0)
        hi = np.max([np.add(r["befoglalo_globalis"][:3], r["befoglalo_globalis"][3:]) for r in sel], axis=0)
        m = 0.06 * (hi - lo).max()
        x0, x1, z0, z1 = lo[0] - m + dx, hi[0] + m + dx, lo[2] - m, hi[2] + m
        y0, y1 = -(hi[1] + m), -(lo[1] - m)               # CAD-ban tükrözve
        L += [f'(command "_.-LAYOUT" "_N" {lstr(lay)})', f'(setvar "CTAB" {lstr(lay)})',
              f'(command "_.ERASE" (ssget "_X" (list (cons 0 "VIEWPORT") (cons 410 {lstr(lay)}))) "")', '(command "_.PSPACE")']
        for (a, b), view in zip(VP_RECTS, views):
            L.append(f'(command "_.MVIEW" (list {a[0]} {a[1]}) (list {b[0]} {b[1]})) (setq s16vp (cdr (assoc 69 (entget (entlast)))))')
            if view == "_FRONT":
                zw = f"(list {x0:.1f} 0 {z0:.1f}) (list {x1:.1f} 0 {z1:.1f})"
            elif view == "_LEFT":
                zw = f"(list 0 {y0:.1f} {z0:.1f}) (list 0 {y1:.1f} {z1:.1f})"
            elif view == "_TOP":
                zw = f"(list {x0:.1f} {y0:.1f} 0) (list {x1:.1f} {y1:.1f} 0)"
            else:
                zw = f"(list {x0:.1f} {y0:.1f} {z0:.1f}) (list {x1:.1f} {y1:.1f} {z1:.1f})" if dx else None
            vs = "_R" if view == "_SWISO" else "_H"
            zoom = f'(command "_.ZOOM" "_W" {zw})' if zw else '(command "_.ZOOM" "_E")'
            L.append(f'(command "_.MSPACE") (setvar "CVPORT" s16vp) (command "_.-VIEW" "{view}") (command "_.VSCURRENT" "{vs}") {zoom} (command "_.PSPACE")')
            L.append(_ptxt(lay, a[0] + 1.5, a[1] + 1.5, 2.2, VIEW_NAME[view]))
        L.append(_pline(lay, [(-15, -5), (272, -5), (272, 200), (-15, 200)]))
        L += stamp_insert(lay, {"SH_TITLE": cim, "SH_SUBSET": f"Lap {no}/{len(sheets)}: {title}",
                                "SH_PRNAME": "TERVI – NEM GYÁRTÁSI KIADÁS · Claude (AI) / Kapusi Péter",
                                "SH_PRNUM": f"Rev {doc['modell_revizio']} · mm · nézetek méretarány nélkül",
                                "SH_DATE": date.today().isoformat()})
        if dx:
            tips = sorted({(r_["tipus"], r_["tipus_szin"]) for r_ in rest[1]}, key=lambda t: t[0])
            L.append(_ptxt(lay, -12, 192, 2.6, "MŰHELYI NÉZET – alkatrész-típusszínek (mint a coo1.dwg); a gyártási rétegek ($PART_) a valós színeket viselik"))
            for k_, (t_, c_) in enumerate(tips):
                L.append(f'(entmake (list (cons 0 "TEXT") (cons 67 1) (cons 410 {lstr(lay)}) (cons 8 "S16_PECSET") (cons 62 {c_}) '
                         f'(cons 10 (list {-12 + 30 * (k_ % 5)} {186 - 4 * (k_ // 5)} 0.0)) (cons 40 2.4) (cons 1 {lstr("■ " + t_)})))')
        notes = [t for (sheet, t) in open_items if sheet in (lay, "*")]
        for k, t in enumerate(notes[:4]):
            L.append(_ptxt(lay, -12, 25 - 5 * k, 2.2, "MEGJEGYZÉS: " + t))
    # az etalonhoz hasonlóan a modelltérben nyílik (délnyugati axonometria, valós színek); a sablon üres lapjai törölve
    L += ['(setvar "CTAB" "Model")', '(command "_.-LAYOUT" "_D" "Layout1")', '(command "_.-LAYOUT" "_D" "Layout2")',
          '(setvar "CTAB" "Model")', '(command "_.-VIEW" "_SWISO")', '(command "_.VSCURRENT" "_R")', '(command "_.ZOOM" "_E")']
    return L


# ------------------------------------------------------------------ main

def main():
    global PREFIX
    doc = load_json(F1 / "parts_v1.json")
    rules_path = F1 / "gyartasi_szabalyok_v1.json"
    rules = load_json(rules_path if rules_path.exists() else CODE.parent / "10_F1_adatmodell" / "gyartasi_szabalyok_v1.json")
    PREFIX = doc["alkatreszek"][0]["cimke_id"].split("_")[0]
    srcdir = F1 / doc["forras"]["mappa"]
    src_parts = load_json(srcdir / "parts.json")
    zl = list(srcdir.glob("*_ZART_JELENET_MM.json"))
    zart = {o["name"]: o for o in load_json(zl[0])["objects"]} if zl else {}
    rev = doc["modell_revizio"]
    tag = f"{PREFIX}_{rev.split('-')[1]}"                       # pl. S16_R15B
    ver = os.environ.get("WSG_DWG_VER", "v4")

    global SZINES_DX
    plan, notes = make_plan(doc, src_parts, rules)
    xs = [r["befoglalo_globalis"][0] for r in doc["alkatreszek"]] + [r["befoglalo_globalis"][0] + r["befoglalo_globalis"][3] for r in doc["alkatreszek"]]
    SZINES_DX = int(round((max(xs) - min(xs) + 1500) / 100.0) * 100)
    (HERE / "cad_terv.json").write_text(json.dumps({"modell_revizio": rev, "datum": date.today().isoformat(),
                                                    "megjegyzesek": notes, "alkatreszek": plan}, ensure_ascii=False, indent=1), encoding="utf-8")
    lsp = HERE / f"{tag}_szerkezet.lsp"
    body = write_lsp(plan, lsp, rev)
    mac = os.environ.get("WSG_MAC_MAPPA") or rules.get("cad", {}).get("mac_mappa", "/Users/peterkapusi/CAD/S16_R15")
    write_scr(lsp, ['(s16-smoketest)', f'(s16-readback "{mac}/readback_smoke")'], HERE / f"{tag}_smoke.scr", f"{mac}/{tag}_smoke.dwg")
    vas_path = BASE / "30_F2b_vasalat" / "vasalat_terv.json"
    hw, nblk, open_items = [], {}, []
    if vas_path.exists():
        vas = load_json(vas_path)
        drw = srcdir / "drawers.json"
        hw, nblk = hardware_lines(vas, plan, doc, load_json(drw) if drw.exists() else None)
        for p_ in vas["problemak"]:
            if p_["sulyossag"] == "BLOKKOLO":
                open_items.append(("*", f"BLOKKOLÓ {p_['alkatresz']}: {p_['uzenet'][:90]}"))
        open_items.append(("*", "vasalat: cikkszámos blokk, SEMATIKUS burkoló geometria – gyári 3D-re cserélhető"))
        open_items.append(("*", "réteg-élkód: hossz1-hossz2-szél1-szél2 (V élzárt, F festett, L lakk, K kárpit, 0 nincs) – FELTEVÉS"))
    mods = {r["modul"] for r in doc["alkatreszek"]}
    sheets = [(a.replace("S16", PREFIX), b, c, d) for a, b, c, d in SHEETS if c is None or mods & set(c)]
    if len(sheets) < 3:
        sheets = auto_sheets(doc)
    sheets = sheets + [(f"{PREFIX}_L{len(sheets) + 1:02d}_MUHELYI_SZINES", "Műhelyi nézet – alkatrész-típusszínek", None,
                        ("_FRONT", "_TOP", "_SWISO"), SZINES_DX, plan)]
    cim = os.environ.get("WSG_CIM") or ("WSG A-902 · S16 médiafal (Kyoto Ink)" if PREFIX == "S16" else f"WSG A-902 · {PREFIX} szekrény")
    names = list(nblk) + ["SH_STAMP"]
    counts = ['(princ (list "S16_DARAB" "PART" (s16-count "$PART_") "TECH" (s16-count "TECH_") '
              + " ".join(f'{lstr(k)} (s16-count-ins {lstr(k)})' for k in names) + '))']
    write_scr(lsp, body + hw + [f'(s16-readback "{mac}/readback_{tag}_{ver}")'] + counts,
              HERE / f"{tag}_build.scr", f"{mac}/{tag}_szerkezet_{ver}.dwg", presentation=sheet_lines(doc, open_items, sheets, cim))
    (HERE / "vasalat_blokkok.json").write_text(json.dumps({"blokkok": nblk, "lapok": [s_[0] for s_ in sheets], "szines_dx": SZINES_DX,
                                                          "tipusok": sorted({(it["tipus"], it["tipus_szin"]) for it in plan})}, ensure_ascii=False, indent=1), encoding="utf-8")
    print("vasalat-sorok:", len(hw), "blokk-beillesztések:", nblk)

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
    write_dxf(plan, meshes, HERE / f"{tag}_elonezet.dxf")

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
