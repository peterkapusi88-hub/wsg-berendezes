# A-902 v2b-1-k11b → v2b-1-k12 JAVASLAT v2: kizárólag a Cam_12_Nappali_Hero (ÉNy-i sarok, délkelet felé) hozzáadása; mentés ÚJ fájlba (copy=True).
# Falak, nyílások, padlók, bútor- és stílusrétegek, a többi kamera és a render-beállítás (scene.camera = Cam_04_Master) változatlan.
# Claude, 2026-10-25 (Péter 01:39, 01:58, 02:06). Futtatás: Blender -b <v2b1k11b.blend> --python 03_cam12_rogzites_v2.py -- <kimenet.blend>
import bpy, sys, math, hashlib
OUT = sys.argv[sys.argv.index('--') + 1]
assert hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest().startswith('9875cd57')
assert 'Cam_12_Nappali_Hero' not in bpy.data.objects
cd = bpy.data.cameras.new('Cam_12_Nappali_Hero'); co = bpy.data.objects.new('Cam_12_Nappali_Hero', cd)
for c in bpy.data.objects['Cam_04_Master'].users_collection: c.objects.link(co)
cd.type = 'PERSP'; cd.lens = 22.0; cd.sensor_width = 36.0; cd.sensor_height = 24.0; cd.sensor_fit = 'AUTO'
cd.shift_x = 0.0; cd.shift_y = -0.08; cd.clip_start = 0.1; cd.clip_end = 200.0; cd.dof.use_dof = False
co.location = (3.95, 7.90, 1.45); co.rotation_mode = 'XYZ'; co.rotation_euler = (math.pi / 2, 0.0, -3 * math.pi / 4)
assert bpy.context.scene.camera.name == 'Cam_04_Master'
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=True)
print('MENTVE', OUT)
