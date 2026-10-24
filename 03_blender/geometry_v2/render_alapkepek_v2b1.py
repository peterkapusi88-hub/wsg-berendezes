# A-902 v2b-1 – bútor nélküli alapképek a KEP-004 képfázishoz: Cam_02, Cam_03, Cam_04 (semleges nappali fény, a v2b
# beállításokkal azonosan) + Cam_10 fürdő 06.2 (ablaktalan: csak műfény a meglévő ML10 ponton). Claude, 2026-10-24.
# Csak a betöltött példányon módosít, NEM MENT. Futtatás: <Blender> -b <v2b-1 + Cam_10 .blend> --python render_alapkepek_v2b1.py -- <kimenet>
import bpy, sys, os, json, time, hashlib
D = '/Users/peterkapusi/Downloads/WSG/_claude_kep004_alap_20261024/'; sys.path.insert(0, D)
from furdo06_2_beallitas import furdo06_2
OUT = sys.argv[sys.argv.index('--')+1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; r = sc.render; vs = sc.view_settings
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
for c in bpy.data.collections:
    if c.name.startswith('Stil_') or c.name.startswith('VK_') or c.name == 'A902_Villamos_TERV': c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    if not o.name.startswith(MARAD): o.hide_render = True
FAL_FEHER = bpy.data.materials['Fal_feher']; falanyag_csere = []
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher': falanyag_csere.append([o.name, s.material.name]); s.material = FAL_FEHER
r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
sc.eevee.taa_render_samples = 128
vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.gamma = 1.0; r.image_settings.file_format = 'PNG'
nt = sc.world.node_tree; bg = nt.nodes['Background']
for l in list(nt.links):
    if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0
for o in bpy.data.objects:
    if o.type == 'LIGHT': o.hide_render = True
vs.exposure = 0.75
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(),
           valtozat='semleges (Cam_02/03/04) + mufeny (Cam_10)', kepek=[], falanyag_csere=falanyag_csere,
           megtartott_szaniter=sorted(o.name for o in bpy.data.collections['A902_Butor'].objects if not o.hide_render),
           beallitas=dict(motor=r.engine, felbontas=[1600, 1000], minta=128, view='AgX', look=vs.look, expozicio=0.75,
                          egbolt='egyszínű (0,86/0,88/0,92), erősség 1,0; nap és belső lámpák nélkül'))
def cam(o): c = o.data; return dict(loc=[round(x, 4) for x in o.location], rot=[round(x, 4) for x in o.rotation_euler], lens=c.lens, sensor=[c.sensor_width, c.sensor_height], fit=c.sensor_fit, clip=[c.clip_start, c.clip_end])
CSAK_FURDO = os.environ.get('WSG_CSAK_FURDO') == '1'
for cn, fn in ([] if CSAK_FURDO else [('Cam_02_Nappali_terasz', 'A902_Alap-v2b1_blender_02_nappali-terasz.png'), ('Cam_03_Etkezo_konyha', 'A902_Alap-v2b1_blender_03_etkezo-konyha.png'),
               ('Cam_04_Master', 'A902_Alap-v2b1_blender_04_master.png')]):
    sc.camera = bpy.data.objects[cn]; r.filepath = os.path.join(OUT, fn); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cn, fajl=fn, kamera_parameterek=cam(sc.camera), mp=round(time.time() - t, 1)))
# fürdő 06.2 – ablaktalan
flog = furdo06_2(sc, MARAD); vs.exposure = 0.3
# az ablaktalan, kis fürdőben a visszavert fény döntő → Cycles (fizikai GI), azonos AgX-beállítással
r.engine = 'CYCLES'; sc.cycles.samples = int(os.environ.get('WSG_MINTA', '96')); sc.cycles.use_denoising = True
try:
    pr = bpy.context.preferences.addons['cycles'].preferences; pr.compute_device_type = 'METAL'; pr.get_devices()
    for d in pr.devices: d.use = True
    sc.cycles.device = 'GPU'
except Exception as e: print('GPU nem elérhető', e)
vs.exposure = float(os.environ.get('WSG_EXP', '0.0'))
flog['motor'] = f"Cycles {sc.cycles.samples} minta, denoise, eszköz {sc.cycles.device}, expozíció {vs.exposure}"

sc.camera = bpy.data.objects['Cam_10_Furdo_06_2']; fn = 'A902_Alap-v2b1_blender_10_furdo-06-2.png'; r.filepath = os.path.join(OUT, fn); t = time.time()
bpy.ops.render.render(write_still=True)
log['kepek'].append(dict(kamera='Cam_10_Furdo_06_2', fajl=fn, kamera_parameterek=cam(sc.camera), mp=round(time.time() - t, 1), expozicio=vs.exposure, furdo_beallitas=flog))
json.dump(log, open(os.path.join(OUT, 'render_log_furdo.json' if CSAK_FURDO else 'render_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('RENDER KÉSZ')
