import bpy,json
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];rows=[]
for o in bpy.context.scene.objects:
 if o.type!='MESH' or o.hide_render or not o.visible_get():continue
 pts=[o.matrix_world@Vector(v) for v in o.bound_box]
 b=[min(v[i] for v in pts) for i in range(3)]+[max(v[i] for v in pts) for i in range(3)]
 rows.append(dict(name=o.name,bounds=b,collections=[c.name for c in o.users_collection],props={k:str(o[k]) for k in o.keys()}))
(P/'R06/data/visible_R05_bounds.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
for r in rows:
 if any(t in r['name'].lower() for t in ['wc','mosdo','b62','tukor','torol']) and not r['name'].startswith(('CP3','R04')):print(r['name'],[round(x,3) for x in r['bounds']])
