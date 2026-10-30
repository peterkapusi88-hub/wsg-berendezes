#!/usr/bin/env python3
"""
Paraméteres bútorlap-szekrény generátor (ezdxf).
Kimenet: 2D gyártási rajz (DXF), 3D mesh modell (DXF), natív 3D solid script (SCR),
szabásjegyzék (CSV) és PNG előnézet. Minden méret mm-ben.
"""
import csv, math, sys, pathlib
import ezdxf
from ezdxf import units
from ezdxf.enums import TextEntityAlignment
from ezdxf.render import forms
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
from ezdxf.addons.drawing.config import Configuration, BackgroundPolicy
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ------------------------------------------------------------------ PARAMÉTEREK
W, H, D = 800, 2000, 600          # külső szélesség, teljes magasság (lábazattal), korpusz mélység
T = 18                            # bútorlap vastagság
TB = 8                            # hátfal (HDF)
HP = 100                          # lábazat magasság
PLINTH_FRONT_SETBACK = 50         # lábazat előlap visszahúzása
PLINTH_SIDE_SETBACK = 20
N_SHELVES = 4                     # állítható polcok
SHELF_FRONT_SETBACK = 10
GAP = 3                           # ajtó rés középen
GAP_EDGE = 1.5                    # ajtó rés szélen, fent, lent
DOOR_T = 18
NAME = f"szekreny_{W}x{H}x{D}"
OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".")
OUT.mkdir(parents=True, exist_ok=True)

HC = H - HP                       # korpusz magasság
INNER_W = W - 2 * T
CLEAR_H = HC - 2 * T
bay = (CLEAR_H - N_SHELVES * T) / (N_SHELVES + 1)
shelf_z = [round(HP + T + (i + 1) * bay + i * T) for i in range(N_SHELVES)]  # polc alsó síkja
DOOR_W = (W - 2 * GAP_EDGE - GAP) / 2
DOOR_H = HC - 2 * GAP_EDGE
SHELF_D = D - TB - SHELF_FRONT_SETBACK - 12

# ------------------------------------------------------------------ 3D DOBOZOK (x: szélesség, y: mélység hátra, z: magasság)
# (név, x, y, z, dx, dy, dz, réteg)
boxes = []
pw = W - 2 * PLINTH_SIDE_SETBACK
pd = D - PLINTH_FRONT_SETBACK
boxes += [
    ("Lábazat előlap", PLINTH_SIDE_SETBACK, PLINTH_FRONT_SETBACK, 0, pw, T, HP, "LABAZAT"),
    ("Lábazat hátlap", PLINTH_SIDE_SETBACK, D - T, 0, pw, T, HP, "LABAZAT"),
    ("Lábazat oldal", PLINTH_SIDE_SETBACK, PLINTH_FRONT_SETBACK + T, 0, T, pd - 2 * T, HP, "LABAZAT"),
    ("Lábazat oldal", W - PLINTH_SIDE_SETBACK - T, PLINTH_FRONT_SETBACK + T, 0, T, pd - 2 * T, HP, "LABAZAT"),
    ("Oldallap", 0, 0, HP, T, D, HC, "KORPUSZ"),
    ("Oldallap", W - T, 0, HP, T, D, HC, "KORPUSZ"),
    ("Fenéklap", T, 0, HP, INNER_W, D - TB, T, "KORPUSZ"),
    ("Tetőlap", T, 0, H - T, INNER_W, D - TB, T, "KORPUSZ"),
    ("Hátfal", 0, D - TB, HP, W, TB, HC, "KORPUSZ"),
]
for z in shelf_z:
    boxes.append(("Polc", T, SHELF_FRONT_SETBACK, z, INNER_W, SHELF_D, T, "POLC"))
boxes += [
    ("Ajtó", GAP_EDGE, -DOOR_T, HP + GAP_EDGE, DOOR_W, DOOR_T, DOOR_H, "AJTO"),
    ("Ajtó", GAP_EDGE + DOOR_W + GAP, -DOOR_T, HP + GAP_EDGE, DOOR_W, DOOR_T, DOOR_H, "AJTO"),
]

# ------------------------------------------------------------------ DXF ALAP
def new_doc():
    doc = ezdxf.new("R2018", setup=True)
    doc.units = units.MM
    doc.header["$INSUNITS"] = 4
    doc.header["$LTSCALE"] = 10
    for name, color, lt in [("KORPUSZ", 7, "Continuous"), ("POLC", 3, "Continuous"),
                            ("AJTO", 5, "Continuous"), ("LABAZAT", 8, "Continuous"),
                            ("TAKART", 8, "DASHED"), ("MERET", 1, "Continuous"),
                            ("SZOVEG", 2, "Continuous"), ("SRAFF", 7, "Continuous"),
                            ("AXO", 6, "Continuous"), ("3D", 4, "Continuous")]:
        doc.layers.add(name, color=color, linetype=lt)
    doc.styles.add("ARIAL", font="arial.ttf")
    doc.dimstyles.new("BUTOR", dxfattribs={
        "dimtxt": 30, "dimasz": 25, "dimexo": 12, "dimexe": 15, "dimgap": 8,
        "dimdec": 0, "dimzin": 8, "dimtad": 1, "dimtih": 0, "dimtoh": 0,
        "dimclrd": 1, "dimclre": 1, "dimclrt": 2, "dimtxsty": "ARIAL"})
    return doc

doc = new_doc()
msp = doc.modelspace()

def rect(x, y, w, h, layer, hatch=False):
    pts = [(x, y), (x + w, y), (x + w, y + h), (x, y + h)]
    msp.add_lwpolyline(pts, close=True, dxfattribs={"layer": layer})
    if hatch:
        hp = msp.add_hatch(color=8, dxfattribs={"layer": "SRAFF"})
        hp.set_pattern_fill("ANSI31", scale=6)
        hp.paths.add_polyline_path(pts, is_closed=True)

def text(s, x, y, h=40, layer="SZOVEG", align=TextEntityAlignment.LEFT):
    msp.add_text(s, height=h, dxfattribs={"layer": layer, "style": "ARIAL"}).set_placement((x, y), align=align)

def dim_h(x1, x2, y, base_y):
    msp.add_linear_dim(base=(x1, base_y), p1=(x1, y), p2=(x2, y), dimstyle="BUTOR",
                       dxfattribs={"layer": "MERET"}).render()

def dim_v(y1, y2, x, base_x):
    msp.add_linear_dim(base=(base_x, y1), p1=(x, y1), p2=(x, y2), angle=90, dimstyle="BUTOR",
                       dxfattribs={"layer": "MERET"}).render()

# ------------------------------------------------------------------ A) ELÖLNÉZET AJTÓK NÉLKÜL (origó 0,0)
ax0, ay0 = 0, 0
rect(ax0 + PLINTH_SIDE_SETBACK, ay0, pw, HP, "LABAZAT")
rect(ax0, ay0 + HP, T, HC, "KORPUSZ", hatch=False)
rect(ax0 + W - T, ay0 + HP, T, HC, "KORPUSZ")
rect(ax0 + T, ay0 + HP, INNER_W, T, "KORPUSZ")
rect(ax0 + T, ay0 + H - T, INNER_W, T, "KORPUSZ")
for z in shelf_z:
    rect(ax0 + T, ay0 + z, INNER_W, T, "POLC")
dim_h(ax0, ax0 + W, ay0 + H, ay0 + H + 180)
dim_h(ax0 + T, ax0 + W - T, ay0 + H, ay0 + H + 90)
dim_v(ay0, ay0 + HP, ax0 + W, ax0 + W + 120)
dim_v(ay0 + HP, ay0 + H, ax0 + W, ax0 + W + 120)
dim_v(ay0, ay0 + H, ax0 + W, ax0 + W + 260)
chain = [HP + T] + shelf_z + [H - T]
for a, b in zip(chain[:-1], chain[1:]):
    dim_v(ay0 + a, ay0 + b, ax0, ax0 - 120)
text("A  ELÖLNÉZET – ajtók nélkül", ax0, ay0 - 220, 50)

# ------------------------------------------------------------------ B) OLDALNÉZET, METSZET (u = mélység, elöl balra)
bx0, by0 = 1500, 0
u = lambda y: bx0 + DOOR_T + y          # ajtó -18..0 -> bx0..bx0+18
rect(u(0), by0 + HP, D, HC, "TAKART")                       # távoli oldallap kontúr
rect(u(0), by0 + HP, D - TB, T, "KORPUSZ", True)            # fenék
rect(u(0), by0 + H - T, D - TB, T, "KORPUSZ", True)         # tető
rect(u(D - TB), by0 + HP, TB, HC, "KORPUSZ", True)          # hátfal
for z in shelf_z:
    rect(u(SHELF_FRONT_SETBACK), by0 + z, SHELF_D, T, "POLC", True)
rect(u(PLINTH_FRONT_SETBACK), by0, T, HP, "LABAZAT", True)
rect(u(D - T), by0, T, HP, "LABAZAT", True)
rect(u(-DOOR_T), by0 + HP + GAP_EDGE, DOOR_T, DOOR_H, "AJTO", True)
dim_h(u(0), u(D), by0 + H, by0 + H + 90)
dim_h(u(-DOOR_T), u(D), by0 + H, by0 + H + 180)
dim_h(u(SHELF_FRONT_SETBACK), u(SHELF_FRONT_SETBACK + SHELF_D), by0 + shelf_z[-1], by0 + shelf_z[-1] - 120)
dim_h(u(0), u(PLINTH_FRONT_SETBACK), by0, by0 - 90)
dim_v(by0 + HP + GAP_EDGE, by0 + HP + GAP_EDGE + DOOR_H, u(-DOOR_T), u(-DOOR_T) - 120)
text("B  OLDALNÉZET – metszet", bx0, by0 - 220, 50)

# ------------------------------------------------------------------ C) FELÜLNÉZET, METSZET (v = mélység, elöl lent)
cx0, cy0 = 0, -1500
v = lambda y: cy0 + (D - y)             # hátfal felül (v=cy0), ajtó elöl (v=cy0+D..+618)
rect(cx0, v(D), W, TB, "KORPUSZ", True)                        # hátfal
rect(cx0, v(D - TB), T, D - TB, "KORPUSZ", True)                # bal oldal
rect(cx0 + W - T, v(D - TB), T, D - TB, "KORPUSZ", True)        # jobb oldal
rect(cx0 + T, v(SHELF_FRONT_SETBACK + SHELF_D), INNER_W, SHELF_D, "POLC")
rect(cx0 + GAP_EDGE, v(0), DOOR_W, DOOR_T, "AJTO", True)
rect(cx0 + GAP_EDGE + DOOR_W + GAP, v(0), DOOR_W, DOOR_T, "AJTO", True)
dim_h(cx0, cx0 + W, v(-DOOR_T), v(-DOOR_T) + 180)
dim_h(cx0 + GAP_EDGE, cx0 + GAP_EDGE + DOOR_W, v(-DOOR_T), v(-DOOR_T) + 90)
dim_h(cx0 + GAP_EDGE + DOOR_W + GAP, cx0 + W - GAP_EDGE, v(-DOOR_T), v(-DOOR_T) + 90)
dim_v(v(D), v(-DOOR_T), cx0 + W, cx0 + W + 120)
text(f"C  FELÜLNÉZET – metszet   (ajtórés középen {GAP} mm, szélen {GAP_EDGE} mm)", cx0, cy0 - 220, 50)

# ------------------------------------------------------------------ D) AXONOMETRIA (drótváz, ajtók nélkül)
def iso(x, y, z):
    return ((x - y) * math.cos(math.radians(30)), (x + y) * math.sin(math.radians(30)) + z)
dx0, dy0 = 2900, 300
def iso_box(x, y, z, dx, dy, dz, layer):
    c = [(x, y, z), (x + dx, y, z), (x + dx, y + dy, z), (x, y + dy, z),
         (x, y, z + dz), (x + dx, y, z + dz), (x + dx, y + dy, z + dz), (x, y + dy, z + dz)]
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]
    p = [iso(*pt) for pt in c]
    for a, b in edges:
        msp.add_line((dx0 + p[a][0], dy0 + p[a][1]), (dx0 + p[b][0], dy0 + p[b][1]), dxfattribs={"layer": layer})
for (name, x, y, z, dx, dy, dz, layer) in boxes:
    if name != "Ajtó":
        iso_box(x, y, z, dx, dy, dz, "AXO")
text("D  AXONOMETRIA – drótváz, ajtók nélkül", dx0 - 500, -220, 50)

# ------------------------------------------------------------------ SZABÁSJEGYZÉK
parts = {}
for (name, x, y, z, dx, dy, dz, layer) in boxes:
    dims = sorted([dx, dy, dz])
    t, w, l = dims
    mat = "HDF 8 mm" if t == TB else f"bútorlap {int(t)} mm"
    key = (name, l, w, t, mat)
    parts[key] = parts.get(key, 0) + 1
edge_rule = {"Oldallap": "1 hosszú él", "Fenéklap": "1 hosszú él", "Tetőlap": "1 hosszú él",
             "Polc": "1 hosszú él", "Ajtó": "körben 4 él", "Lábazat előlap": "1 hosszú él"}
rows = []
area = 0.0
for (name, l, w, t, mat), qty in parts.items():
    rows.append([name, qty, int(round(l)), int(round(w)), int(round(t)), mat, edge_rule.get(name, "-")])
    if "bútorlap" in mat:
        area += qty * l * w / 1e6
rows.sort(key=lambda r: (-r[2] * r[3], r[0]))
csv_path = OUT / f"{NAME}_szabasjegyzek.csv"
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f:
    wr = csv.writer(f, delimiter=";")
    wr.writerow(["Alkatrész", "db", "Hossz (mm)", "Szélesség (mm)", "Vastagság (mm)", "Anyag", "Élzárás (ABS 1 mm)"])
    wr.writerows(rows)
    wr.writerow([])
    wr.writerow(["Bútorlap nettó", f"{area:.2f} m²", "", "", "", "2800x2070 tábla:", f"{math.ceil(area * 1.15 / (2.8 * 2.07))} db (15% hulladékkal)"])
    wr.writerow(["Vasalat", "", "", "", "", "kivetőpánt 110°", f"{2 * 4} db (ajtónként 4)"])
    wr.writerow(["Vasalat", "", "", "", "", "polctartó", f"{N_SHELVES * 4} db"])
    wr.writerow(["Vasalat", "", "", "", "", "fogantyú", "2 db"])

# szabásjegyzék a rajzlapra is
tx, ty = 1500, -300
text("SZABÁSJEGYZÉK  (hossz × szélesség × vastagság, mm)", tx, ty, 45)
for i, r in enumerate(rows):
    text(f"{r[1]} db   {r[0]:<16} {r[2]} × {r[3]} × {r[4]}   {r[5]}   élzárás: {r[6]}", tx, ty - 80 - i * 70, 36)
text(f"Bútorlap nettó: {area:.2f} m²  →  {math.ceil(area * 1.15 / (2.8 * 2.07))} db 2800×2070 tábla (15% hulladékkal)",
     tx, ty - 80 - len(rows) * 70 - 40, 36)
text(f"SZEKRÉNY {W}×{H}×{D + DOOR_T} mm  –  bútorlap {T} mm, hátfal HDF {TB} mm  –  méretek mm-ben, M 1:1",
     0, H + 420, 60)
doc.saveas(OUT / f"{NAME}_2D.dxf")

# ------------------------------------------------------------------ PNG ELŐNÉZET
fig = plt.figure(figsize=(22, 14), dpi=130)
ax = fig.add_axes([0, 0, 1, 1])
ctx = RenderContext(doc)
Frontend(ctx, MatplotlibBackend(ax), config=Configuration(background_policy=BackgroundPolicy.WHITE)).draw_layout(msp, finalize=True)
fig.savefig(OUT / f"{NAME}_elonezet.png", facecolor="white")

# ------------------------------------------------------------------ 3D MESH DXF
doc3 = new_doc()
msp3 = doc3.modelspace()
for (name, x, y, z, dx, dy, dz, layer) in boxes:
    m = forms.cube(center=False)
    m.scale(dx, dy, dz)
    m.translate(x, y, z)
    m.render_mesh(msp3, dxfattribs={"layer": layer})
doc3.saveas(OUT / f"{NAME}_3D_mesh.dxf")

# ------------------------------------------------------------------ NATÍV 3D SOLID SCRIPT (AutoCAD-ben futtatva valódi 3DSOLID-ok)
lines = [f"; {NAME} – natív 3D solid modell. Futtatás: húzd a fájlt az AutoCAD rajzterületére, vagy SCRIPT parancs.",
         "_.OSMODE", "0", "_.UCS", "_W", "_.UNDO", "_BEGIN"]
for layer, color in [("KORPUSZ", 7), ("POLC", 3), ("AJTO", 5), ("LABAZAT", 8)]:
    lines += ["_-LAYER", "_M", layer, "_C", str(color), layer, ""]
cur = None
for (name, x, y, z, dx, dy, dz, layer) in boxes:
    if layer != cur:
        lines += ["_.CLAYER", layer]
        cur = layer
    lines += ["_.BOX", f"{x:g},{y:g},{z:g}", f"{x + dx:g},{y + dy:g},{z + dz:g}"]
lines += ["_.UNDO", "_END", "_.VPOINT", "1,-1,1", "_.VSCURRENT", "_C", "_.ZOOM", "_E", ""]
(OUT / f"{NAME}_3Dsolid.scr").write_text("\n".join(lines), encoding="utf-8")

print("Polcok alsó síkja (mm):", shelf_z, "| ajtó:", DOOR_W, "x", DOOR_H, "| bútorlap:", f"{area:.2f} m²")
for p in sorted(OUT.iterdir()):
    print(p.name, p.stat().st_size, "B")
