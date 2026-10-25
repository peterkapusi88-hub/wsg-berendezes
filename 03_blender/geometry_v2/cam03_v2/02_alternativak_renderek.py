# Elrendezési alternatívák (R/A/B/C × S01/S02) tömbjei a Cam_12 hero, a Cam_02 kontroll és az új Cam_03 javaslat nézetéből, valamint felülnézetben.
# Alap: v2b-1-k12 v2 (PR #17, sha 66172d43). A Cam_03 javaslat paraméterei a parancssorból (JSON). Claude, 2026-10-25. NEM MENT.
import bpy, sys, os, json, time, hashlib, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T, elrendezes_tomeg_lib as L
a = sys.argv[sys.argv.index('--') + 1:]; OUT = a[0]; C3 = json.loads(a[1]); os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('66172d43'), SHA
T.alap_beallitas(sc); sc.render.resolution_percentage = 50
KCOL, KREC = L.konyha_tomeg(sc)
KULCS = ['S01_R', 'S01_A', 'S01_B', 'S01_C', 'S02_R', 'S02_A', 'S02_B', 'S02_C']
ALT = {k: L.alternativa_tomeg(sc, k) for k in KULCS}
jcol = L.gyujtemeny(sc, 'JEL_cam03_javaslat')
c3 = T.kamera('Cam_03_JAVASLAT', tuple(C3['loc']), L.rot(C3['theta']), lens=C3['lens'], col=jcol); c3.data.shift_y = C3['shift_y']
CAM = {'Cam_12': bpy.data.objects['Cam_12_Nappali_Hero'], 'Cam_02': bpy.data.objects['Cam_02_Nappali_terasz'], 'Cam_03uj': c3}
fc = T.kamera('JEL_felul_alt', (7.25, 5.25, 12.0), (0, 0, 0), col=jcol); fc.data.type = 'ORTHO'; fc.data.ortho_scale = 8.6
vl.update(); log = dict(blender=bpy.app.version_string, sha256=SHA, cam03_javaslat=C3, renderek={}, tomeg={k: v[1] for k, v in ALT.items()})
def renderel(cam, fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True); return round(time.time() - t, 1)
for k in KULCS:
    ALT[k][0].hide_render = False; vl.update()
    for cn, c in CAM.items(): log['renderek'][f'{k}_{cn}'] = renderel(c, f'alt_{k}_{cn}.png')
    ALT[k][0].hide_render = True
# felülnézet: a mennyezeti elemek nélkül
felso = [o for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render and min((o.matrix_world @ __import__('mathutils').Vector(cc)).z for cc in o.bound_box) >= 2.80]
for o in felso: o.hide_render = True
sc.render.resolution_x, sc.render.resolution_y, sc.render.resolution_percentage = 1000, 1000, 100
for k in KULCS:
    ALT[k][0].hide_render = False; vl.update(); log['renderek'][f'{k}_felul'] = renderel(fc, f'alt_{k}_felul.png'); ALT[k][0].hide_render = True
json.dump(log, open(os.path.join(OUT, 'alt_renderek_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ')
