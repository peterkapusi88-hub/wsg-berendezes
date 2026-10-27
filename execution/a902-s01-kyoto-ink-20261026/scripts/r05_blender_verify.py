import bpy,json,hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'R05'
def bb(o):
 vs=[o.matrix_world@Vector(v) for v in o.bound_box];return [min(v[i] for v in vs) for i in range(3)]+[max(v[i] for v in vs) for i in range(3)]
t=bpy.data.objects['R04_TV-01-R04A_visible_front_0'];base=bpy.data.objects['R05_TV-02_front1'];tv=bpy.data.objects['KI_KI-033']
result={'reopened_file':bpy.data.filepath,'sha256':hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest(),'mesh_count':sum(o.type=='MESH' for o in bpy.data.objects),'tower_bbox':bb(t),'first_lower_front_bbox':bb(base),'tv_bbox':bb(tv),'tower_alignment_pass':abs(bb(t)[1]-bb(base)[1])<.0001 and abs(bb(t)[4]-bb(base)[4])<.0001,'tower_camera_side_pass':bb(t)[1]<5,'whole_apartment_pass':False,'reason':'This readback tests saved front placement only; product shapes, artwork and earlier clearance issues remain open.'}
(O/'qa/blender_reopen.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
