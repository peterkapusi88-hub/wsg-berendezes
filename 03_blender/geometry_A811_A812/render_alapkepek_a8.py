# =====================================================================================
# A-811 / A-812 – bútor nélküli alapképek a rögzített kamerákból (Astra B fázis bemenete) + felülnézeti ellenőrző kép
# a kiállás-réteggel. 2026-10-24, Claude. Ugyanaz a „semleges” beállítás, mint az A-902 v2b alapképein:
# EEVEE, 1600 × 1000, AgX Medium High Contrast, expozíció +0,75, egyszínű égbolt (0,86/0,88/0,92, erősség 1,0),
# nap és belső lámpa nélkül. Csak a betöltött példányon módosít (láthatóság, felülnézeti színek); NEM MENT.
# Futtatás háttér-Blenderrel (5.2.3), CSAK KÉZZEL:
#   WSG_KEZI_FUTTATAS=1 <Blender> -b WSG_A811_alaprajz_ELOZETES_20261024.blend --python render_alapkepek_a8.py -- <kimeneti mappa>
# WSG_PROBA=1: beállítás-ellenőrzés renderelés nélkül.
# =====================================================================================
import os as _os
if _os.environ.get('WSG_KEZI_FUTTATAS') != '1':
    raise SystemExit('Csak kézi futtatás: WSG_KEZI_FUTTATAS=1')
import bpy, sys, os, json, time

args = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
OUT = args[0]; os.makedirs(OUT, exist_ok=True)
PROBA = _os.environ.get('WSG_PROBA') == '1'
sc = bpy.context.scene; r = sc.render; vs = sc.view_settings
L = sc.name.replace('WSG_', '')                      # A811 / A812 (a build szkript így nevezi a jelenetet)
assert L in ('A811', 'A812'), sc.name
def kep():
    if not PROBA: bpy.ops.render.render(write_still=True)
vk = bpy.data.collections[f'{L}_Villamos_TERV']; vk.hide_render = True
# semleges beállítás (a fájlban is így van; itt csak biztosítjuk)
r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
sc.eevee.use_raytracing = True; sc.eevee.taa_render_samples = 32
vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.exposure = 0.75; vs.gamma = 1.0
bg = sc.world.node_tree.nodes['Background']; bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0
for o in bpy.data.objects:
    if o.type == 'LIGHT': o.hide_render = True
KAM = [o.name for o in sorted(bpy.data.objects, key=lambda o: o.name) if o.type == 'CAMERA' and o.data.type == 'PERSP']
NEV = {'Cam_02': '02_nappali-erkely', 'Cam_03': '03_etkezo-konyha', 'Cam_04': '04_haloszoba', 'Cam_05': '05_haloszoba-2'}
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), lakas=L, kepek=[],
           beallitas=dict(motor=r.engine, sugarkovetes=sc.eevee.use_raytracing, mintak=sc.eevee.taa_render_samples, felbontas=[r.resolution_x, r.resolution_y], view=vs.view_transform, look=vs.look, expozicio=vs.exposure,
                          egbolt='egyszínű (0,86/0,88/0,92), erősség 1,0', fenyek='nincs'),
           rejtve=[f'{L}_Villamos_TERV'], bútor='nincs a modellben')
for cam in KAM:
    fn = f"{L}_Alap-v2_blender_{NEV[cam[:6]]}.png"
    sc.camera = bpy.data.objects[cam]; r.filepath = os.path.join(OUT, fn); t = time.time(); kep()
    log['kepek'].append(dict(kamera=cam, fajl=fn, mp=round(time.time() - t, 1)))
# felülnézet: mennyezet rejtve, kiállás-réteg látható, tárgyszínek (Workbench, lapos fény)
vk.hide_render = False
for o in bpy.data.collections[f'{L}_Falak'].objects:
    if o.name.startswith('Plafon'): o.hide_render = True
    else: o.color = (0.18, 0.18, 0.18, 1)
for o in bpy.data.collections[f'{L}_Nyilaszarok'].objects: o.color = (0.55, 0.62, 0.70, 1)
for o in bpy.data.collections[f'{L}_Padlo'].objects: o.color = (0.97, 0.97, 0.97, 1)
for o in bpy.data.collections[f'{L}_Erkely_ELOZETES'].objects: o.color = (0.85, 0.88, 0.85, 1)
r.engine = 'BLENDER_WORKBENCH'; sh = sc.display.shading; sh.light = 'FLAT'; sh.color_type = 'OBJECT'
vs.view_transform = 'Standard'; vs.look = 'None'; vs.exposure = 0.0
r.resolution_x, r.resolution_y = (1500, 1700) if L == 'A811' else (1300, 2100)
sc.camera = bpy.data.objects['Cam_06_Alaprajz_lakas']
fn = f'{L}_Alap-v2_blender_06_alaprajz-kiallasok.png'; r.filepath = os.path.join(OUT, fn); t = time.time(); kep()
log['kepek'].append(dict(kamera='Cam_06_Alaprajz_lakas', fajl=fn, mp=round(time.time() - t, 1), megjegyzes='Workbench, tárgyszín, mennyezet rejtve'))
json.dump(log, open(os.path.join(OUT, f'render_log_{L}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('RENDER KÉSZ', json.dumps(log, ensure_ascii=False))
