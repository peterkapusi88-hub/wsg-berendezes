import bpy,json,sys
from pathlib import Path
from mathutils import Vector
p=Path('/Users/peterkapusi/Documents/ChatGPT/WSG – Stíluslabor/execution/a902-s01-kyoto-ink-20261026')
def bounds(o):
 v=[o.matrix_world@Vector(c) for c in o.bound_box];return [min(x[i] for x in v) for i in range(3)]+[max(x[i] for x in v) for i in range(3)]
a={'blender':bpy.app.version_string,'file':bpy.data.filepath,'objects':[{'name':o.name,'type':o.type,'bounds':bounds(o),'collections':[c.name for c in o.users_collection],'location':list(o.location),'rotation':list(o.rotation_euler)} for o in bpy.data.objects]}
(p/'blender/source_inspection.json').write_text(json.dumps(a,ensure_ascii=False,indent=2));print('INSPECT_OK',len(a['objects']))
