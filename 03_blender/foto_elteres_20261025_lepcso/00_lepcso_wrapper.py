# Cam_02 alapkép + BECSÜLT belső lépcső a nappali teraszüvegfala előtt (profi fotók 3659/3708/3726 alapján, 2026-10-25).
# NEM lock-módosítás: JELÖLT ELTÉRÉS ("FOTO_ELTERES"), a k13 blend MÁSOLATÁN, mentés nélkül. Claude.
import bpy, os, json, runpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector
H=float(os.environ.get('LEP_H','0.15')); Y0=float(os.environ.get('LEP_Y0','7.95')); Y1=8.21; X0=float(os.environ.get('LEP_X0','3.67')); X1=float(os.environ.get('LEP_X1','9.25'))
sc=bpy.context.scene
me=bpy.data.meshes.new('FOTO_ELTERES_lepcso_nappali_uvegfal')
v=[(X0,Y0,0),(X1,Y0,0),(X1,Y1,0),(X0,Y1,0),(X0,Y0,H),(X1,Y0,H),(X1,Y1,H),(X0,Y1,H)]
me.from_pydata(v,[],[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]); me.update()
ob=bpy.data.objects.new('FOTO_ELTERES_lepcso_nappali_uvegfal',me); sc.collection.objects.link(ob)
# padlóanyag újrahasznosítása
pm=bpy.data.materials.get('v2_parketta_GreyTreviso_EL2184_foto')
for o in ([] if pm else bpy.data.objects):
    if o.type=='MESH' and any(k in o.name.lower() for k in ('padlo','parketta','floor')) and o.material_slots and o.material_slots[0].material:
        pm=o.material_slots[0].material; break
if pm: me.materials.append(pm)
info=dict(H=H,Y0=Y0,Y1=Y1,X0=X0,X1=X1,anyag=pm.name if pm else None)
