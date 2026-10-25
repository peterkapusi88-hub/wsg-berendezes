# Cam_02 KORREKCIÓ – olvashatóbb (megvilágított) semleges alapkép a lock v2b-1-k13 ellen. Geometria- és kameraváltozás NINCS.
# Claude, 2026-10-25. A Cam_12 v3 KORR (01_render_cam12v3.py) mintájára. A MÁSOLAT blendet NEM menti; sha256 előtte/utána naplózva.
import bpy, sys, os, json, time, hashlib, math, runpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
W = os.environ.get('CAM02_DIR'); OUT = os.path.join(W, os.environ.get('CAM02_OUT', 'vegleges')); PROBA = os.environ.get('CAM02_PROBA') == '1'
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
sha = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
log = dict(blender=bpy.app.version_string, fajl=bpy.data.filepath, sha256_elotte=sha(bpy.data.filepath), proba=PROBA, kepek=[], validator={}, vetites={})
CAM = bpy.data.objects['Cam_02_Nappali_terasz']
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
for c in bpy.data.collections:
    if c.name.startswith(('Stil_', 'VK_')) or c.name == 'A902_Villamos_TERV': c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects: o.hide_render = not o.name.startswith(MARAD)
for o in bpy.data.objects:
    if o.type == 'LIGHT': o.hide_render = True
r = sc.render; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
r.image_settings.file_format = 'PNG'; r.image_settings.color_mode = 'RGB'; r.film_transparent = False
r.engine = 'BLENDER_EEVEE'; ee = sc.eevee; ee.taa_render_samples = 32 if PROBA else 256
for k, v in (('use_raytracing', True), ('use_shadows', True), ('shadow_ray_count', 4), ('shadow_step_count', 16),
             ('fast_gi_method', 'GLOBAL_ILLUMINATION'), ('fast_gi_resolution', '1'), ('fast_gi_ray_count', 4), ('fast_gi_step_count', 16), ('fast_gi_quality', 0.75),
             ('fast_gi_distance', 4.0), ('ray_tracing_method', 'SCREEN')):
    try: setattr(ee, k, v)
    except Exception as e: log.setdefault('eevee_hiba', []).append(f'{k}: {e}')
try:
    ro = ee.ray_tracing_options; ro.resolution_scale = '1'; ro.use_denoise = True
except Exception as e: log.setdefault('eevee_hiba', []).append(f'rto: {e}')
vs = sc.view_settings; vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.gamma = 1.0; vs.exposure = float(os.environ.get('CAM02_EXPO', '0.0'))
nt = sc.world.node_tree; bg = nt.nodes['Background']
for l in list(nt.links):
    if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
bg.inputs['Color'].default_value = (0.78, 0.84, 0.93, 1); bg.inputs['Strength'].default_value = float(os.environ.get('CAM02_EG', '0.6'))
def area(nev, loc, rot, sx, sy, e, col=(1.0, 0.98, 0.96)):
    ld = bpy.data.lights.new(nev, 'AREA'); ld.shape = 'RECTANGLE'; ld.size = sx; ld.size_y = sy; ld.energy = e; ld.color = col
    o = bpy.data.objects.new(nev, ld); sc.collection.objects.link(o); o.location = loc; o.rotation_euler = rot
    try: ld.use_shadow_jitter = True; ld.shadow_jitter_overblur = 10.0
    except Exception: pass
    return o
EN = float(os.environ.get('CAM02_FENY', '220'))
# 1) északi üvegfal belső síkja (x 4,44–8,94; y ~7,95) – délre világít: a W01 TV-falat (normál +X) súrolja, a W04 sávot (normál −Y) nem → tónuskülönbség
area('JEL_nappali_eszaki_ablakfeny', (6.69, 7.95, 1.33), (math.radians(-90), 0, 0), 4.50, 2.35, EN)
# 2) gyenge derítés a kamera mögül/jobbról (délkelet), a TV-fal síkjára ferdén – a padló–fal és mennyezet–fal él elválik
area('JEL_derito_dk', (9.6, 3.0, 2.2), (math.radians(-60), 0, math.radians(-125)), 2.5, 2.0, EN * float(os.environ.get('CAM02_DERITO', '0.25')), (0.97, 0.98, 1.0))
# 3) nagyon gyenge mennyezeti derítés
area('JEL_derito_mennyezet', (6.2, 6.0, 2.86), (0, 0, 0), 5.0, 4.0, EN * 0.06, (0.97, 0.98, 1.0))
def setc(nev, rgb, rough=None):
    m = bpy.data.materials.get(nev)
    if not m: return
    b = m.node_tree.nodes.get('Principled BSDF')
    if b and not b.inputs['Base Color'].is_linked: b.inputs['Base Color'].default_value = (*rgb, 1)
    if b and rough is not None: b.inputs['Roughness'].default_value = rough
setc('Fal_feher', (0.78, 0.78, 0.775), 0.92); setc('Plafon_feher', (0.84, 0.84, 0.84), 0.95)
setc('v2b_belteri_ajtolap_vilagosszurke', (0.47, 0.48, 0.49), 0.5); setc('v2b_belteri_ajtotok_szurke', (0.30, 0.31, 0.32), 0.45)
fal = bpy.data.materials['Fal_feher']
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher': s.material = fal
vl.update(); sc.camera = CAM
# validátor – üres mód
os.environ['WSG_LOCK'] = os.path.join(W, 'forras', 'geometry_lock_A902_v2b.json'); os.environ['WSG_VILLAMOS'] = os.path.join(W, 'forras', 'A902_villamos.json')
VAL = os.path.join(W, 'forras', 'geometry_validator_v2.py')
log['validator_forras'] = dict(lock_sha=sha(os.environ['WSG_LOCK']), villamos_sha=sha(os.environ['WSG_VILLAMOS']), validator_sha=sha(VAL))
BUTOR = list(bpy.data.collections['A902_Butor'].objects)
for m in ('ures', 'referencia'):
    for o in BUTOR: o.hide_render = True if m == 'ures' else not o.name.startswith(MARAD)
    vl.update(); os.environ['WSG_REPORT_JSON'] = os.path.join(OUT, f'validator_cam02korr_{m}.json'); runpy.run_path(VAL)
    log['validator'][m] = json.load(open(os.environ['WSG_REPORT_JSON'], encoding='utf-8'))['summary']
for o in BUTOR: o.hide_render = not o.name.startswith(MARAD)
vl.update()
def px(P):
    p = world_to_camera_view(sc, CAM, Vector(P)); return [round(p.x * 1600, 1), round((1 - p.y) * 1000, 1), round(p.z, 3)]
PONTOK = {'W01 déli vége (x 3,67; y 4,05) alj/tető': [(3.67, 4.05, 0.0), (3.67, 4.05, 2.90)],
          'W01 × északi fal sarok (x 3,67; y 8,05) alj/tető': [(3.67, 8.05, 0.0), (3.67, 8.05, 2.90)],
          'üvegfal nyugati vége (x 4,44; y 8,0) alj': [(4.44, 8.0, 0.0), (4.44, 8.0, 2.53)],
          'üvegfal keleti vége (x 8,94; y 8,0) alj': [(8.94, 8.0, 0.0)],
          'TV-tengely (x 3,71; y 6,27; z 1,20)': [(3.71, 6.27, 1.2)]}
for k, ps in PONTOK.items(): log['vetites'][k] = [dict(P=P, px=px(P)) for P in ps]
r.filepath = os.path.join(OUT, os.environ.get('CAM02_FAJL', 'A902_Alap-v2b1k13_blender_02_nappali-terasz_KORR_semleges.png')); t = time.time()
bpy.ops.render.render(write_still=True); log['kepek'].append(dict(fajl=r.filepath, mp=round(time.time() - t, 1), sha256=sha(r.filepath)))
if os.environ.get('CAM02_BLOKK') == '1':
    # 1b: ugyanaz a kamera; a W01 TV-fal-zóna jelölő tömbje (4,00 × 2,90 m, legfeljebb 0,40 m mély) – csak hely és ferde perspektíva, nem anyag
    me = bpy.data.meshes.new('JEL_W01_TVfal_zona'); x0, x1, y0, y1, z0, z1 = 3.67, 4.07, 4.05, 8.05, 0.0, 2.885
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    me.from_pydata(v, [], [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]); me.update()
    ob = bpy.data.objects.new('JEL_W01_TVfal_zona', me); sc.collection.objects.link(ob)
    m = bpy.data.materials.new('JEL_TVzona'); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']; b.inputs['Base Color'].default_value = (0.20, 0.21, 0.23, 1); b.inputs['Roughness'].default_value = 0.7
    me.materials.append(m); vl.update()
    log['blokk_1b'] = dict(nev=ob.name, bbox=[x0, y0, z0, x1, y1, z1], px=[px((x0 + 0.40, y0, 0)), px((x0 + 0.40, y1, 0)), px((x0 + 0.40, y1, z1)), px((x0 + 0.40, y0, z1))])
    r.filepath = os.path.join(OUT, 'A902_Cam02_KORR_1b_TVfal_zona.png'); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(fajl=r.filepath, mp=round(time.time() - t, 1), sha256=sha(r.filepath)))
log['kamera'] = dict(loc=[round(v, 4) for v in CAM.matrix_world.translation], rot_rad=[round(a, 4) for a in CAM.rotation_euler], lens=CAM.data.lens,
                     shift=[CAM.data.shift_x, CAM.data.shift_y], sensor=[CAM.data.sensor_width, CAM.data.sensor_fit], res=[r.resolution_x, r.resolution_y])
log['render'] = dict(engine=r.engine, samples=ee.taa_render_samples, look=vs.look, exposure=vs.exposure, feny_W=EN)
log['sha256_utana'] = sha(bpy.data.filepath); log['mentve'] = False
json.dump(log, open(os.path.join(OUT, 'cam02_korr_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
result = dict(blokk=log.get('blokk_1b'), validator=log['validator'], kamera=log['kamera'], vetites=log['vetites'], kep=log['kepek'], sha_ok=log['sha256_elotte'] == log['sha256_utana'], eevee_hiba=log.get('eevee_hiba'))
