# Elrendezési alternatívák és generikus konyha tömbjei a KEP-004 kameravizsgálatokhoz (Claude, 2026-10-25). A .blend-et NEM menti.
import bpy, math, json, os
from mathutils import Vector
import tomeg_lib as T
HERE = os.path.dirname(os.path.abspath(__file__))
PAR = json.load(open(os.path.join(HERE, 'elrendezes_alt_A902_v1_parameterek.json'), encoding='utf-8'))
def rot(theta, tilt=0.0):
    """theta: nézési irány az +x tengelytől (fok; kelet 0, észak +90, dél −90); tilt: lefelé dőlés (fok)."""
    return (math.radians(90.0 - tilt), 0.0, math.radians(theta - 90.0))
def gyujtemeny(sc, nev):
    c = bpy.data.collections.new(nev); sc.collection.children.link(c); return c
def konyha_tomeg(sc):
    """A terv szerinti konyhasorok generikus tömbje (WGR1 18. o., mint a 2D méretpróbában): alsó sor 0,90, magas elemek 2,20."""
    col = gyujtemeny(sc, 'KONYHA_TOMEG'); rec = {}
    T.doboz(col, 'KONYHA_nyugati_sor_fozolap', (8.45, 2.35, 0), (9.05, 4.05, 0.90), 'tarolo', rec)
    T.doboz(col, 'KONYHA_keleti_sor', (9.95, 1.95, 0), (10.55, 4.65, 0.90), 'tarolo', rec)
    T.doboz(col, 'KONYHA_huto_oszlop_D13', (9.95, 4.65, 0), (10.55, 5.25, 2.20), 'tarolo', rec)
    T.doboz(col, 'KONYHA_deli_magas_elemek_suto_mikro', (9.05, 1.35, 0), (9.95, 1.95, 2.20), 'tarolo', rec)
    T.doboz(col, 'KONYHA_keleti_sor_deli_vege', (9.95, 1.35, 0), (10.55, 1.95, 0.90), 'tarolo', rec)
    T.doboz(col, 'KONYHA_sarok_elem', (8.45, 1.35, 0), (8.95, 2.25, 0.90), 'tarolo', rec)
    return col, rec
def szek_doboz(col, nev, cx, cy, nx, ny, sz, mely, betol, rec):
    """Betolt szék az asztal élétől: ülés 0–0,46, háttámla a külső oldalon 0,46–0,80."""
    tx, ty = -ny, nx
    a0 = -betol; a1 = -betol + mely
    def sarok(t, s): return (cx + nx * t + tx * s, cy + ny * t + ty * s)
    pts = [sarok(a0, -sz / 2), sarok(a0, sz / 2), sarok(a1, sz / 2), sarok(a1, -sz / 2)]
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    T.doboz(col, nev + '_ules', (min(xs), min(ys), 0), (max(xs), max(ys), 0.46), 'etkezo', rec)
    b = [sarok(a1 - 0.06, -sz / 2), sarok(a1 - 0.06, sz / 2), sarok(a1, sz / 2), sarok(a1, -sz / 2)]
    xs = [p[0] for p in b]; ys = [p[1] for p in b]
    T.doboz(col, nev + '_hat', (min(xs), min(ys), 0.46), (max(xs), max(ys), 0.80), 'etkezo', rec)
def alternativa_tomeg(sc, kulcs):
    v = PAR['valtozatok'][kulcs]; col = gyujtemeny(sc, 'ALT_' + kulcs); rec = {}
    XB = v['XB']
    if v['kanape'] == 'L':
        T.l_kanape_del_sarok(col, XB, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=rec, elotag='ALT_kanape')
    else:
        T.u_kanape(col, XB - 1.60, 4.975, XB, 7.825, D=0.95, log=rec, elotag='ALT_kanape')
    x0, y0, x1, y1 = v['asztal']
    T.doboz(col, 'ALT_asztal_lap', (x0, y0, 0.72), (x1, y1, 0.75), 'etkezo', rec)
    T.doboz(col, 'ALT_asztal_lab', ((x0 + x1) / 2 - 0.20, (y0 + y1) / 2 - 0.20, 0), ((x0 + x1) / 2 + 0.20, (y0 + y1) / 2 + 0.20, 0.72), 'etkezo', rec)
    s = v['szek']
    for i, (cx, cy, nx, ny) in enumerate(v['szekek']):
        szek_doboz(col, f'ALT_szek_{i}', cx, cy, nx, ny, s['sz'], s['mely'], v['betol'], rec)
    # TV-bútor (40 cm) és képernyő; generikus függeszték-jel az ML04 alatt
    T.doboz(col, 'ALT_tv_konzol_40', (3.67, 5.15, 0), (4.07, 7.55, 0.50), 'tv', rec)
    T.doboz(col, 'ALT_tv_kepernyo', (3.70, 6.35 - 0.725, 0.85), (3.75, 6.35 + 0.725, 1.68), 'kepernyo', rec)
    mx, my = PAR['ML04']
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.25, location=(mx, my, 1.75)); g = bpy.context.active_object; g.name = 'ALT_ML04_fuggeszte_jel'
    for c in g.users_collection: c.objects.unlink(g)
    col.objects.link(g); g.data.materials.append(T.anyag('JEL_t_mu', T.SZIN['mu'])); rec[g.name] = [mx - 0.25, my - 0.25, 1.50, mx + 0.25, my + 0.25, 2.00]
    T.doboz(col, 'ALT_ML04_kabel', (mx - 0.005, my - 0.005, 2.00), (mx + 0.005, my + 0.005, 2.90), 'tv', rec)
    col.hide_render = True
    return col, rec
