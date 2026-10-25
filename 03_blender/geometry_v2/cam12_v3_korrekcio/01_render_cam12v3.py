# Cam_12 v3 KORREKCIÓ – semleges (olvashatóbb) alapkép + S01/S02 tömbrender + validátor a lock v2b-1-k13 ellen.
# Claude, 2026-10-25. A betöltött MÁSOLAT blendet NEM menti; a forrás sha256-ját előtte/utána naplózza.
# Futtatás: Blender -b <MASOLAT.blend> --python 01_render_cam12v3.py -- <KIMENET> [proba]
import bpy, sys, os, json, time, hashlib, math, runpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
W = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, W)
import blokk_spec as BS
args = sys.argv[sys.argv.index('--') + 1:]; OUT = args[0]; PROBA = len(args) > 1 and args[1] == 'proba'
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
log = dict(blender=bpy.app.version_string, fajl=bpy.data.filepath, sha256_elotte=sha(bpy.data.filepath), proba=PROBA, kepek=[], validator={}, vetites={}, blokkok={})
CAM = bpy.data.objects['Cam_12_Nappali_Hero']
# ---------------------------------------------------------------- láthatóság (mint a k13 alap_beallitas: bútor, stílus, kiállás-jelölők ki)
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
for c in bpy.data.collections:
    if c.name.startswith(('Stil_', 'VK_')) or c.name == 'A902_Villamos_TERV': c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    o.hide_render = not o.name.startswith(MARAD)
for o in bpy.data.objects:
    if o.type == 'LIGHT': o.hide_render = True
# ---------------------------------------------------------------- render: Cycles, fizikai nappali fény az északi üvegfal felől
r = sc.render; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
r.image_settings.file_format = 'PNG'; r.image_settings.color_mode = 'RGB'; r.film_transparent = False
ENGINE = os.environ.get('CAM12_ENGINE', 'EEVEE')
cy = sc.cycles
if ENGINE == 'CYCLES':
    # megj.: a lock egymásba lógó falhasábjai (pl. W02 nyugati vége × W07, 10 cm) Cyclesben fekete csíkot adnak → alapból EEVEE
    r.engine = 'CYCLES'
    try:
        pr = bpy.context.preferences.addons['cycles'].preferences; pr.compute_device_type = 'METAL'; pr.get_devices()
        for d in pr.devices: d.use = True
        cy.device = 'GPU'
    except Exception as e:
        cy.device = 'CPU'
    cy.samples = 48 if PROBA else 384; cy.use_adaptive_sampling = True; cy.use_denoising = True
else:
    r.engine = 'BLENDER_EEVEE'; ee = sc.eevee
    ee.taa_render_samples = 32 if PROBA else 256
    for k, v in (('use_raytracing', True), ('use_shadows', True), ('shadow_ray_count', 4), ('shadow_step_count', 16), ('use_shadow_jitter_viewport', True),
                 ('fast_gi_method', 'GLOBAL_ILLUMINATION'), ('fast_gi_resolution', '1'), ('fast_gi_ray_count', 4), ('fast_gi_step_count', 16), ('fast_gi_quality', 0.75),
                 ('fast_gi_distance', 4.0), ('ray_tracing_method', 'SCREEN')):
        try: setattr(ee, k, v)
        except Exception as e: log.setdefault('eevee_hiba', []).append(f'{k}: {e}')
    try:
        ro = ee.ray_tracing_options; ro.resolution_scale = '1'; ro.use_denoise = True
    except Exception as e: log.setdefault('eevee_hiba', []).append(f'rto: {e}')
vs = sc.view_settings; vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.gamma = 1.0; vs.exposure = float(os.environ.get('CAM12_EXPO', '0.0'))
nt = sc.world.node_tree; bg = nt.nodes['Background']
for l in list(nt.links):
    if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
bg.inputs['Color'].default_value = (0.80, 0.85, 0.92, 1); bg.inputs['Strength'].default_value = 0.25
def area(nev, loc, rot, sx, sy, e, col=(1.0, 0.98, 0.96)):
    ld = bpy.data.lights.new(nev, 'AREA'); ld.shape = 'RECTANGLE'; ld.size = sx; ld.size_y = sy; ld.energy = e; ld.color = col
    o = bpy.data.objects.new(nev, ld); sc.collection.objects.link(o); o.location = loc; o.rotation_euler = rot
    try: ld.use_shadow_jitter = True; ld.shadow_jitter_overblur = 10.0
    except Exception: pass
    return o
# az északi üvegfal belső síkja előtt (y 7,99), x 4,44–8,94, z 0,15–2,50 – lefelé/délre világít; a kamera mögött van
EN = float(os.environ.get('CAM12_FENY', '220'))
area('JEL_nappali_eszaki_ablakfeny', (6.69, 7.99, 1.33), (math.radians(-90), 0, 0), 4.50, 2.35, EN)
# gyenge, nagy felületű derítés a mennyezet alatt (szórt égbolt-fény utánzat a mély konyhában), nem pontfény
area('JEL_derito_mennyezet', (7.6, 4.6, 2.86), (0, 0, 0), 6.5, 6.5, EN * 0.12, (0.97, 0.98, 1.0))
# ---------------------------------------------------------------- anyagok: fehér falak maradnak; enyhe tónuskülönbség
def setc(nev, rgb, rough=None):
    m = bpy.data.materials.get(nev)
    if not m: return
    b = m.node_tree.nodes.get('Principled BSDF')
    if b and not b.inputs['Base Color'].is_linked: b.inputs['Base Color'].default_value = (*rgb, 1)
    if b and rough is not None: b.inputs['Roughness'].default_value = rough
setc('Fal_feher', (0.78, 0.78, 0.775), 0.92)            # fehér fal (marad fehér)
setc('Plafon_feher', (0.84, 0.84, 0.84), 0.95)          # mennyezet: kissé világosabb, külön tónus
setc('v2b_belteri_ajtolap_vilagosszurke', (0.47, 0.48, 0.49), 0.5)   # világosszürke ajtólap (valós)
setc('v2b_belteri_ajtotok_szurke', (0.30, 0.31, 0.32), 0.45)         # tok sötétebb – a nyílás kerete olvasható
fal = bpy.data.materials['Fal_feher']
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher': s.material = fal
# ---------------------------------------------------------------- tömbök
_M = {}
def anyag(nev, rgb, rough=0.8):
    k = (nev, rgb, rough)
    if k in _M: return _M[k]
    m = bpy.data.materials.new('JEL_b_' + nev); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Roughness'].default_value = rough; _M[k] = m; return m
def doboz(col, nev, g, mat):
    x0, y0, z0, x1, y1, z1 = g; me = bpy.data.meshes.new(nev)
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    me.from_pydata(v, [], [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]); me.update()
    o = bpy.data.objects.new(nev, me); col.objects.link(o); me.materials.append(mat); return o
def ellipszis(col, nev, g, mat, n=64):
    cx, cy_, z0, rx, ry, z1 = g; me = bpy.data.meshes.new(nev)
    v = [(cx + rx * math.cos(2 * math.pi * i / n), cy_ + ry * math.sin(2 * math.pi * i / n), z) for z in (z0, z1) for i in range(n)]
    f = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))] + [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
    me.from_pydata(v, [], f); me.update(); o = bpy.data.objects.new(nev, me); col.objects.link(o); me.materials.append(mat); return o
def szek(col, nev, g, mat):
    cx, cy_, nx, ny, sz, mely, ul, h = g; tx, ty = -ny, nx; a0, a1 = -0.18, -0.18 + mely
    P = lambda t, q: (cx + nx * t + tx * q, cy_ + ny * t + ty * q)
    def bb(t0, t1):
        p = [P(t0, -sz / 2), P(t0, sz / 2), P(t1, sz / 2), P(t1, -sz / 2)]
        return min(x for x, y in p), min(y for x, y in p), max(x for x, y in p), max(y for x, y in p)
    x0, y0, x1, y1 = bb(a0, a1); o1 = doboz(col, nev + '_ules', (x0, y0, 0, x1, y1, ul), mat)
    x0, y0, x1, y1 = bb(a1 - 0.06, a1); o2 = doboz(col, nev + '_hat', (x0, y0, ul, x1, y1, h), mat)
    return [o1, o2]
GY = {}
for st in ('S01', 'S02'):
    cb = bpy.data.collections.new('Stil_BLOKK_' + st); sc.collection.children.link(cb)
    cf = bpy.data.collections.new('FELULET_BLOKK_' + st); sc.collection.children.link(cf)
    GY[st] = (cb, cf)
    for e in BS.K:
        if e['st'] != st: continue
        col = cb if e['reteg'] == 'butor' else cf; nev = e['id'].replace('-', '_'); mat = anyag(e['id'], tuple(e['szin']), e['rough'])
        obs = szek(col, nev, e['g'], mat) if e['tipus'] == 'chair' else [ellipszis(col, nev, e['g'], mat) if e['tipus'] == 'ell' else doboz(col, nev, e['g'], mat)]
        log['blokkok'][e['id']] = dict(objektumok=[o.name for o in obs])
    for c in (cb, cf): c.hide_render = True; c.hide_viewport = True
vl.update()
# ---------------------------------------------------------------- validátor (v2) a lock v2b-1-k13 ellen
os.environ['WSG_LOCK'] = W + 'forras/geometry_lock_A902_v2b.json' if os.path.exists(W + 'forras/geometry_lock_A902_v2b.json') else os.path.join(os.path.dirname(bpy.data.filepath), 'geometry_lock_A902_v2b.json')
os.environ['WSG_VILLAMOS'] = os.path.join(os.path.dirname(bpy.data.filepath), 'A902_villamos.json')
VAL = os.path.join(os.path.dirname(bpy.data.filepath), 'geometry_validator_v2.py')
log['validator_forras'] = dict(lock=os.environ['WSG_LOCK'], lock_sha=sha(os.environ['WSG_LOCK']), villamos_sha=sha(os.environ['WSG_VILLAMOS']), validator_sha=sha(VAL))
sc.camera = CAM
def mod(m):
    for st, (cb, cf) in GY.items():
        for c in (cb, cf): c.hide_render = (m != st); c.hide_viewport = (m != st)
    vl.update()
BUTOR = list(bpy.data.collections['A902_Butor'].objects)
for m in ('ures', 'referencia', 'S01', 'S02'):
    mod('ures' if m == 'referencia' else m)
    for o in BUTOR: o.hide_render = True if m != 'referencia' else not o.name.startswith(MARAD)
    vl.update(); os.environ['WSG_REPORT_JSON'] = os.path.join(OUT, f'validator_cam12v3korr_{m}.json')
    runpy.run_path(VAL)
    log['validator'][m] = json.load(open(os.environ['WSG_REPORT_JSON'], encoding='utf-8'))['summary']
for o in BUTOR: o.hide_render = not o.name.startswith(MARAD)
# ---------------------------------------------------------------- vetítés: a fix elemek képi helye (px) és takartsága
deps = bpy.context.evaluated_depsgraph_get()
def px(P):
    p = world_to_camera_view(sc, CAM, Vector(P)); return [round(p.x * 1600, 1), round((1 - p.y) * 1000, 1), round(p.z, 3)]
def renderben(ob):
    if ob.hide_render: return False
    return any(not c.hide_render for c in ob.users_collection)
def lathato(P):
    o = CAM.matrix_world.translation.copy(); d = (Vector(P) - o); L = d.length; n = d.normalized(); megtett = 0.0
    for _ in range(50):
        hit, loc, nor, idx, ob, mx = sc.ray_cast(deps, o, n, distance=L - megtett - 0.02)
        if not hit: return True
        if renderben(ob): return False
        step = (loc - o).length + 0.001; megtett += step; o = loc + n * 0.001
    return False
PONTOK = {
 '05.3 ajtó déli tok (y 6,05) alj/teteje': [(10.75, 6.05, 0.0), (10.75, 6.05, 2.10)],
 '05.3 ajtó északi tok (y 6,95) alj/teteje': [(10.75, 6.95, 0.0), (10.75, 6.95, 2.10)],
 'szemöldöksáv teteje (mennyezet) az ajtó fölött': [(10.75, 6.50, 2.90)],
 'akna-sarok (x 9,80; y 7,025)': [(9.80, 7.025, 0.0), (9.80, 7.025, 2.90)],
 'W03-a / K-csonk sarok (x 10,75→10,55; y 5,05)': [(10.75, 5.05, 0.0), (10.55, 5.05, 0.0), (10.55, 5.05, 2.90)],
 'K-pultfal déli vége (x 10,55; y 1,35)': [(10.55, 1.35, 0.0), (10.55, 1.35, 2.90)],
 'konyha déli fal nyugati vége (x 9,05; y 1,35)': [(9.05, 1.35, 0.0)],
 'mellvéd északi vége (x 8,35–8,45; y 4,05), teteje 0,85': [(8.45, 4.05, 0.85), (8.35, 4.05, 0.85), (8.45, 4.05, 0.0)],
 'átjáró szemöldök (x 7,30–8,45; z 2,10)': [(7.30, 4.05, 2.10), (8.45, 4.05, 2.10)],
 'W02 keleti vége (x 7,30; y 4,05)': [(7.30, 4.05, 0.0), (7.30, 4.05, 2.90)],
 'W02 nyugati vége (x 5,20; y 4,05)': [(5.20, 4.05, 0.0), (5.20, 4.05, 2.90)],
 'kapcsolóoszlop K10–K12/T01 (x 7,149)': [(7.149, 4.05, 1.10)],
 'W07 visszafordulás (x 5,20; y 2,75–4,05)': [(5.20, 2.75, 0.0), (5.20, 3.40, 1.40)],
 'ML04 (8,549; 6,274) mennyezet': [(8.549, 6.274, 2.90)],
 'ML05 (5,619; 6,274) mennyezet': [(5.619, 6.274, 2.90)],
 'FL01 konyhai fali pont (10,534; 3,149)': [(10.534, 3.149, 2.0)],
}
for k, ps in PONTOK.items():
    log['vetites'][k] = [dict(P=P, px=px(P), lathato=lathato(P)) for P in ps]
# blokkok képi befoglalója (S01, S02 külön)
def kepteri(o):
    pts = [world_to_camera_view(sc, CAM, o.matrix_world @ Vector(c)) for c in o.bound_box]; pts = [p for p in pts if p.z > 0]
    if not pts: return None
    b = [min(p.x for p in pts), min(1 - p.y for p in pts), max(p.x for p in pts), max(1 - p.y for p in pts)]
    if b[2] < 0 or b[0] > 1 or b[3] < 0 or b[1] > 1: return None
    return [round(max(0, b[0]) * 1600), round(max(0, b[1]) * 1000), round(min(1, b[2]) * 1600), round(min(1, b[3]) * 1000)]
for st, (cb, cf) in GY.items():
    mod(st); deps = bpy.context.evaluated_depsgraph_get()
    for o in list(cb.objects) + list(cf.objects):
        c = o.matrix_world @ (sum((Vector(v) for v in o.bound_box), Vector()) / 8)
        log['blokkok'].setdefault(o.name, {})
        log['blokkok'][o.name] = dict(bbox=[round(v, 3) for v in (min((o.matrix_world @ Vector(v))[i] for v in o.bound_box) for i in range(3))] + [round(v, 3) for v in (max((o.matrix_world @ Vector(v))[i] for v in o.bound_box) for i in range(3))],
                                      kep_px=kepteri(o), kozep_px=px(tuple(c)), kozep_lathato=lathato(tuple(c)))
# ---------------------------------------------------------------- render
def renderel(fajl):
    sc.camera = CAM; r.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(fajl=fajl, mp=round(time.time() - t, 1), sha256=sha(r.filepath)))
mod('ures'); renderel('A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png')
if not PROBA or os.environ.get('CAM12_MIND'):
    mod('S01'); renderel('A902_S01_Cam12v3_KORR_tombrender.png')
    mod('S02'); renderel('A902_S02_Cam12v3_KORR_tombrender.png')
log['kamera'] = dict(loc=[round(v, 4) for v in CAM.matrix_world.translation], rot_deg=[round(math.degrees(a), 4) for a in CAM.rotation_euler], lens=CAM.data.lens,
                     shift_y=round(CAM.data.shift_y, 4), sensor=[CAM.data.sensor_width, CAM.data.sensor_fit], res=[r.resolution_x, r.resolution_y])
log['render'] = dict(engine=r.engine, device=cy.device, samples=(cy.samples if r.engine == 'CYCLES' else sc.eevee.taa_render_samples), denoise=cy.use_denoising, view=vs.view_transform, look=vs.look, exposure=vs.exposure, feny_W=EN)
log['sha256_utana'] = sha(bpy.data.filepath); log['mentve'] = False; log['dirty_a_futas_vegen'] = bpy.data.is_dirty
json.dump(log, open(os.path.join(OUT, 'cam12v3_korr_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
open(os.path.join(OUT, 'KESZ.done'), 'w').write(json.dumps(log['validator'], ensure_ascii=False))
print('KESZ', log['validator'])
