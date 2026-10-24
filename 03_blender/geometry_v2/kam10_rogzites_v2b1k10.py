# A-902 v2b-1 → v2b-1k10: Cam_10_Furdo_06_2 + a 06.2 DK-i akna/falblokk (KORR 2, 18. o.) hozzáadása; mentés ÚJ fájlba. Claude, 2026-10-24.
import bpy, sys, math, bmesh
OUT = sys.argv[sys.argv.index('--')+1]
assert 'Cam_10_Furdo_06_2' not in bpy.data.objects and 'Akna_06_2_EK_v2b1k10' not in bpy.data.objects
ref = bpy.data.objects['Akna_06_2']
me = bpy.data.meshes.new('Akna_06_2_EK_v2b1k10'); bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0); bm.to_mesh(me); bm.free()
o = bpy.data.objects.new('Akna_06_2_EK_v2b1k10', me)
for c in ref.users_collection: c.objects.link(o)
a, b = (15.45, 5.20, 0.0), (16.40, 5.81, 2.90)
o.location = [(a[i] + b[i]) / 2 for i in range(3)]; o.scale = [b[i] - a[i] for i in range(3)]
for s in ref.material_slots: me.materials.append(s.material)
bpy.context.view_layer.update(); o.data.transform(o.matrix_basis); o.matrix_basis.identity()   # alkalmazott transzformáció, mint a többi falon
cd = bpy.data.cameras.new('Cam_10_Furdo_06_2'); co = bpy.data.objects.new('Cam_10_Furdo_06_2', cd)
for c in bpy.data.objects['Cam_04_Master'].users_collection: c.objects.link(co)
cd.type = 'PERSP'; cd.lens = 16.0; cd.sensor_width = 36.0; cd.sensor_height = 24.0; cd.sensor_fit = 'AUTO'
cd.shift_x = 0.0; cd.shift_y = 0.0; cd.clip_start = 0.1; cd.clip_end = 200.0; cd.dof.use_dof = False
co.location = (14.50, 6.62, 1.50); co.rotation_mode = 'XYZ'; co.rotation_euler = (1.38, 0.0, -math.pi / 2)
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=True)
print('MENTVE', OUT)
