import bpy,json
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];rows=[]
for o in bpy.context.scene.objects:
 if o.type!='MESH' or o.hide_render:continue
 ids=[str(o.get(k,'')) for k in ['element_id','item_id','instance_id']]
 if any(s in (o.name+' '+' '.join(ids)) for s in ['Lennon','KI-036','KI-037','KI-038','CF01','ST01','sofa','coffee','side_table']):
  v=[o.matrix_world@Vector(c) for c in o.bound_box]
  rows.append({'name':o.name,'properties':{k:str(v) for k,v in o.items()},'min':[min(p[k] for p in v) for k in range(3)],'max':[max(p[k] for p in v) for k in range(3)]})
(P/'R12_muhely/audit/room_obstacle_bounds.json').write_text(json.dumps(rows,indent=2))
print('READ_ONLY_BOUNDS',len(rows))
