import bpy,json
from pathlib import Path
P=Path(__file__).resolve().parents[1];O=P/'R05'
rows=[]
for ob in bpy.data.objects:
 if ob.type in ('MESH','CAMERA','LIGHT'):
  rows.append(dict(name=ob.name,type=ob.type,hide=ob.hide_render,location=list(ob.location),dimensions=list(ob.dimensions),props={k:str(v) for k,v in ob.items()}))
(O/'qa/blender_source_inventory.json').write_text(json.dumps(rows,indent=2))
print('Inventory saved',len(rows),'objects')
