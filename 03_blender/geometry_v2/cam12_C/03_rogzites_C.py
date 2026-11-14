# v2b-1-k12 v2 → v2b-1-k13 KAMERACSOMAG C JAVASLAT: csak a Cam_03_Etkezo_konyha (K1) és a Cam_12_Nappali_Hero (v3) paraméterei változnak;
# mentés ÚJ fájlba (copy=True). Falak, nyílások, padlók, bútor- és stílusrétegek, a többi kamera és a render-beállítás változatlan.
# Claude, 2026-10-25 (Péter 04:08). Futtatás: Blender -b <v2b1k12 v2.blend> --python 03_rogzites_C.py -- <kimenet.blend>
import bpy, sys, math, hashlib, json
OUT = sys.argv[sys.argv.index('--') + 1]
assert hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest().startswith('66172d43')
elotte = {o.name: (tuple(round(v, 5) for v in o.matrix_world.translation), tuple(round(v, 5) for v in o.rotation_euler)) for o in bpy.data.objects}
c3 = bpy.data.objects['Cam_03_Etkezo_konyha']; c12 = bpy.data.objects['Cam_12_Nappali_Hero']
assert c3.parent is None and c12.parent is None
c3.location = (9.45, 7.55, 1.50); c3.rotation_mode = 'XYZ'; c3.rotation_euler = (math.pi / 2, 0.0, -math.pi)
c3.data.lens = 20.0; c3.data.shift_x = 0.0; c3.data.shift_y = -0.08
c12.location = (4.40, 7.88, 1.60); c12.rotation_mode = 'XYZ'; c12.rotation_euler = (math.pi / 2, 0.0, math.radians(-138.0))
c12.data.lens = 22.0; c12.data.shift_x = 0.0; c12.data.shift_y = -0.05
bpy.context.view_layer.update()
valt = [n for n, (l, r) in elotte.items() if (tuple(round(v, 5) for v in bpy.data.objects[n].matrix_world.translation), tuple(round(v, 5) for v in bpy.data.objects[n].rotation_euler)) != (l, r)]
assert sorted(valt) == ['Cam_03_Etkezo_konyha', 'Cam_12_Nappali_Hero'], valt
assert bpy.context.scene.camera.name == 'Cam_04_Master'
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=True)
print('MENTVE', OUT, json.dumps(valt))
