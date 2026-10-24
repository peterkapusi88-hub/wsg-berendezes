# A-902 v2b-1-k10 → v2b-1-k11 JAVASLAT: kizárólag a Cam_11_Master_Panorama kamera hozzáadása; mentés ÚJ fájlba (copy=True).
# Falak, nyílások, padlók, bútor- és stílusrétegek, a többi kamera és a render-beállítás (scene.camera = Cam_04_Master) változatlan.
# Claude, 2026-10-24. Futtatás: Blender -b <v2b1k10.blend> --python 04_cam11_rogzites_v2b1k11.py -- <kimenet.blend>
import bpy, sys, math
OUT = sys.argv[sys.argv.index('--') + 1]
assert 'Cam_11_Master_Panorama' not in bpy.data.objects
cd = bpy.data.cameras.new('Cam_11_Master_Panorama'); co = bpy.data.objects.new('Cam_11_Master_Panorama', cd)
for c in bpy.data.objects['Cam_04_Master'].users_collection: c.objects.link(co)
cd.type = 'PERSP'; cd.lens = 20.0; cd.sensor_width = 36.0; cd.sensor_height = 24.0; cd.sensor_fit = 'AUTO'
cd.shift_x = 0.0; cd.shift_y = 0.0; cd.clip_start = 0.1; cd.clip_end = 200.0; cd.dof.use_dof = False
co.location = (3.20, 6.10, 1.20); co.rotation_mode = 'XYZ'; co.rotation_euler = (math.pi / 2, 0.0, math.pi / 2)
assert bpy.context.scene.camera.name == 'Cam_04_Master'
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=True)
print('MENTVE', OUT)
