# Kerek, hatszemélyes asztal Blender-méretpróbája a C elrendezésben (Péter 2026-10-25 04:39) – v2b-1-k13 blenden, NEM MENT.
# Esetek a ../elrendezes_C/c_kerek2.py eredményéből. Validátor (Stil_ réteg), Cam_12 v3 / Cam_03 K1 / Cam_02 tömbképek.
import bpy, sys, os, json, math, hashlib, runpy
W = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, W)
import tomeg_lib as T, c_tomeg_lib as L
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('e01170d3'), SHA
ESETEK = {
 'R1_S01_Nealy150_TVsik':   dict(st='S01', XB=6.11, D=1.50, c=(8.25, 6.20), rot0=0, tv='TV4'),
 'R2_S02_O140_TVsik':       dict(st='S02', XB=5.91, D=1.40, c=(8.15, 6.35), rot0=0, tv='TV4'),
 'R3_S02_O130_TV40':        dict(st='S02', XB=6.27, D=1.30, c=(8.35, 6.35), rot0=0, tv='TV40'),
}
K = L.konyha(sc)
def kerek(nev, e):
    col = L.gyujt(sc, 'Stil_TOMEG_KEREK_' + nev); rec = {}; XB = e['XB']
    if e['st'] == 'S01': T.l_kanape_del_sarok(col, XB, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=rec, elotag='C_kanape')
    else: T.u_kanape(col, XB - 1.60, 4.975, XB, 7.825, D=0.95, log=rec, elotag='C_kanape')
    cx, cy = e['c']; r = e['D'] / 2
    bpy.ops.mesh.primitive_cylinder_add(vertices=64, radius=r, depth=0.03, location=(cx, cy, 0.735)); o = bpy.context.active_object; o.name = 'C_etkezo_kerek_lap'
    bpy.ops.mesh.primitive_cylinder_add(vertices=32, radius=0.25, depth=0.72, location=(cx, cy, 0.36)); o2 = bpy.context.active_object; o2.name = 'C_etkezo_kerek_lab'
    for ob in (o, o2):
        for c in ob.users_collection: c.objects.unlink(ob)
        col.objects.link(ob); ob.data.materials.append(T.anyag('JEL_t_etkezo', T.SZIN['etkezo']))
    rec['C_etkezo_kerek_lap'] = [cx - r, cy - r, 0.72, cx + r, cy + r, 0.75]
    sz, mely = (0.55, 0.53) if e['st'] == 'S01' else (0.525, 0.55)
    for i in range(6):
        a = math.radians(e['rot0'] + 60 * i); nx, ny = math.cos(a), math.sin(a)
        L.szek(col, f'C_etkezo_szek_{i}', cx + nx * r, cy + ny * r, nx, ny, sz, mely, rec)
    if e['tv'] == 'TV40': T.doboz(col, 'TV_konzol_40', (3.67, 5.15, 0), (4.07, 7.55, 0.50), 'tv', rec)
    else: T.doboz(col, 'TV_panel_4', (3.67, 4.85, 0), (3.71, 7.45, 2.85), 'panel', rec)
    T.doboz(col, 'TV_kepernyo', (3.72, 6.25 - 0.74, 0.80), (3.77, 6.25 + 0.74, 1.65), 'kepernyo', rec)
    mx, my = L.ML04
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.22, location=(mx, my, 1.78)); g = bpy.context.active_object; g.name = 'C_ML04_jel_' + nev
    for c in g.users_collection: c.objects.unlink(g)
    col.objects.link(g); g.data.materials.append(T.anyag('JEL_t_mu', T.SZIN['mu']))
    col.hide_render = True
    return col, rec
TOM = {k: kerek(k, e) for k, e in ESETEK.items()}
log = dict(sha256=SHA, esetek=ESETEK, tomeg={k: v[1] for k, v in TOM.items()}, validator={})
os.environ['WSG_LOCK'] = W + 'lock_k13/geometry_lock_A902_v2b.json'; os.environ['WSG_VILLAMOS'] = W + 'A902_villamos.json'
for o in bpy.data.collections['A902_Butor'].objects: o.hide_render = True
for k, (col, rec) in TOM.items():
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    col.hide_render = False; os.environ['WSG_REPORT_JSON'] = OUT + f'/validator_v2b1k13_kerek_{k}.json'
    runpy.run_path(W + 'geometry_validator_v2.py')
    log['validator'][k] = json.load(open(OUT + f'/validator_v2b1k13_kerek_{k}.json', encoding='utf-8'))['summary']
    col.hide_render = True
T.alap_beallitas(sc); sc.render.resolution_percentage = 50; K[0].hide_render = False
CAMS = {n: bpy.data.objects[n] for n in ('Cam_12_Nappali_Hero', 'Cam_03_Etkezo_konyha', 'Cam_02_Nappali_terasz')}
for k, (col, rec) in TOM.items():
    col.hide_render = False; vl.update()
    for cn, c in CAMS.items():
        sc.camera = c; sc.render.filepath = os.path.join(OUT, f'kerek_{k}_{cn}.png'); bpy.ops.render.render(write_still=True)
    col.hide_render = True
json.dump(log, open(OUT + '/kerek_meretproba_log.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', json.dumps(log['validator'], ensure_ascii=False))
