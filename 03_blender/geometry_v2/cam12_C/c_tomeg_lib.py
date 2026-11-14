# C elrendezés (Péter 2026-10-25 04:08) végleges méretpróba-tömbjei + TV-fal-változatok + generikus konyha. Claude, 2026-10-25. NEM MENT.
import bpy, math
import tomeg_lib as T
# végleges C (elrendezes_C/c_hatarhelyzet.py): S01 kanapé XB 6,67, Toni 160 a 10 cm-rel délebbre; S02 XB 6,60, Anouk 180
C = {
 'S01': dict(kanape='L', XB=6.67, asztal=(8.00, 5.40, 8.90, 7.00), sz=0.55, mely=0.53,
             szekek=[(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]),
 'S02': dict(kanape='U', XB=6.60, asztal=(8.00, 5.35, 8.90, 7.15), sz=0.525, mely=0.55,
             szekek=[(8.00, 6.15, -1, 0), (8.00, 6.75, -1, 0), (8.90, 6.15, 1, 0), (8.90, 6.75, 1, 0), (8.45, 5.35, 0, -1), (8.45, 7.15, 0, 1)]),
}
ML04 = (8.549, 6.274)
BETOL = 0.18
def gyujt(sc, nev):
    c = bpy.data.collections.new(nev); sc.collection.children.link(c); return c
def konyha(sc):
    col = gyujt(sc, 'KONYHA_TOMEG'); rec = {}
    T.doboz(col, 'KONYHA_nyugati_sor_fozolap', (8.45, 2.35, 0), (9.05, 4.05, 0.90), 'tarolo', rec)
    T.doboz(col, 'KONYHA_keleti_sor', (9.95, 1.95, 0), (10.55, 4.65, 0.90), 'tarolo', rec)
    T.doboz(col, 'KONYHA_huto_oszlop_D13', (9.95, 4.65, 0), (10.55, 5.25, 2.20), 'tarolo', rec)
    T.doboz(col, 'KONYHA_deli_magas_elemek_suto_mikro', (9.05, 1.35, 0), (9.95, 1.95, 2.20), 'tarolo', rec)
    T.doboz(col, 'KONYHA_keleti_sor_deli_vege', (9.95, 1.35, 0), (10.55, 1.95, 0.90), 'tarolo', rec)
    T.doboz(col, 'KONYHA_sarok_elem', (8.45, 1.35, 0), (8.95, 2.25, 0.90), 'tarolo', rec)
    return col, rec
def szek(col, nev, cx, cy, nx, ny, sz, mely, rec):
    tx, ty = -ny, nx; a0 = -BETOL; a1 = -BETOL + mely
    s = lambda t, q: (cx + nx * t + tx * q, cy + ny * t + ty * q)
    p = [s(a0, -sz / 2), s(a0, sz / 2), s(a1, sz / 2), s(a1, -sz / 2)]
    T.doboz(col, nev + '_ules', (min(x for x, y in p), min(y for x, y in p), 0), (max(x for x, y in p), max(y for x, y in p), 0.46), 'etkezo', rec)
    b = [s(a1 - 0.06, -sz / 2), s(a1 - 0.06, sz / 2), s(a1, sz / 2), s(a1, -sz / 2)]
    T.doboz(col, nev + '_hat', (min(x for x, y in b), min(y for x, y in b), 0.46), (max(x for x, y in b), max(y for x, y in b), 0.80), 'etkezo', rec)
def elrendezes(sc, st):
    v = C[st]; col = gyujt(sc, 'C_' + st); rec = {}; XB = v['XB']
    if v['kanape'] == 'L': T.l_kanape_del_sarok(col, XB, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=rec, elotag='C_kanape')
    else: T.u_kanape(col, XB - 1.60, 4.975, XB, 7.825, D=0.95, log=rec, elotag='C_kanape')
    x0, y0, x1, y1 = v['asztal']
    T.doboz(col, 'C_etkezo_asztal_lap', (x0, y0, 0.72), (x1, y1, 0.75), 'etkezo', rec)
    T.doboz(col, 'C_etkezo_asztal_lab', ((x0 + x1) / 2 - 0.20, (y0 + y1) / 2 - 0.20, 0), ((x0 + x1) / 2 + 0.20, (y0 + y1) / 2 + 0.20, 0.72), 'etkezo', rec)
    for i, (cx, cy, nx, ny) in enumerate(v['szekek']): szek(col, f'C_etkezo_szek_{i}', cx, cy, nx, ny, v['sz'], v['mely'], rec)
    mx, my = ML04
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.22, location=(mx, my, 1.78)); g = bpy.context.active_object; g.name = 'C_ML04_fuggeszto_jel_' + st
    for c in g.users_collection: c.objects.unlink(g)
    col.objects.link(g); g.data.materials.append(T.anyag('JEL_t_mu', T.SZIN['mu'])); rec[g.name] = [mx - .22, my - .22, 1.56, mx + .22, my + .22, 2.0]
    T.doboz(col, 'C_ML04_kabel_' + st, (mx - .005, my - .005, 2.0), (mx + .005, my + .005, 2.9), 'tv', rec)
    return col, rec
def tv_fal(sc, mod):
    """TV40: 40 cm mély, 50 cm magas konzol (y 5,15–7,55) + fali képernyő.
    TV60M: két mennyezetig érő, 60 cm mély szekrény (y 4,25–5,05 és 6,85–7,65; a brief legmélyebb esete), köztük 4 cm-es panel, 40 cm-es alacsony konzol, fali képernyő."""
    col = gyujt(sc, 'TV_' + mod); rec = {}
    if mod == 'TV40':
        T.doboz(col, 'TV_konzol_40', (3.67, 5.15, 0), (4.07, 7.55, 0.50), 'tv', rec)
    else:
        T.doboz(col, 'TV_szekreny60_del', (3.67, 4.25, 0), (4.27, 5.05, 2.85), 'tarolo', rec)
        T.doboz(col, 'TV_szekreny60_eszak', (3.67, 6.85, 0), (4.27, 7.65, 2.85), 'tarolo', rec)
        T.doboz(col, 'TV_panel_4', (3.67, 5.05, 0), (3.71, 6.85, 2.85), 'panel', rec)
        T.doboz(col, 'TV_konzol_40', (3.71, 5.15, 0), (4.07, 6.75, 0.45), 'tv', rec)
    T.doboz(col, 'TV_kepernyo', (3.72, 6.20 - 0.83, 0.80), (3.77, 6.20 + 0.83, 1.75), 'kepernyo', rec)   # 75" (166×95), x 3,77 képernyősík
    return col, rec
def rot(theta, tilt=0.0):
    return (math.radians(90.0 - tilt), 0.0, math.radians(theta - 90.0))
