from pathlib import Path
import bpy,bmesh,json
from mathutils import Vector
O=Path(__file__).resolve().parents[1];parts=json.loads((O/'data/parts.json').read_text());changed=json.loads((O/'audit/change_scope.json').read_text())['primary_changed']
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def solid(p):
 b=p['box'];mm=p.get('mesh_mm')
 if mm:vv=mm['vertices'];ff=mm['faces']
 elif p.get('outline') and p['axis']=='y':
  pts=[]
  for v in p['outline']:
   if not pts or sum(abs(v[k]-pts[-1][k]) for k in [0,1])>1e-7:pts.append(v)
  if sum(abs(pts[0][k]-pts[-1][k])for k in [0,1])<1e-7:pts.pop()
  n=len(pts);vv=[(b[0]+x,y,b[2]+z) for y in [b[1],b[1]+b[4]] for x,z in pts];ff=[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n)for i in range(n)]
 else:
  bpy.ops.mesh.primitive_cube_add(size=1,location=[(b[k]+b[k+3]/2)/1000 for k in range(3)]);o=bpy.context.object;o.dimensions=[x/1000 for x in b[3:]];bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.name=p['id'];return o
 me=bpy.data.meshes.new(p['id']);me.from_pydata([[a/1000 for a in v]for v in vv],[],ff);me.update();o=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(o)
 bm=bmesh.new();bm.from_mesh(me);bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bmesh.ops.triangulate(bm,faces=list(bm.faces));bm.to_mesh(me);bm.free();return o
reports=[]
for p in parts:
 if p['id']not in changed:continue
 # On rerun, keep only the intended contour, then reconstruct its rebates.
 p.pop('mesh_mm',None);o=solid(p)
 cuts=[]
 if p.get('assembly_rebate'):cuts.append(p['assembly_rebate'])
 if p['id']=='TV-FIELD':cuts.append(p['edge_light_pocket']['box_mm'])
 for i,b in enumerate(cuts):
  tool=solid({'id':'CUT','box':b});m=o.modifiers.new('concealed_rebate','BOOLEAN');m.operation='DIFFERENCE';m.solver='EXACT';m.object=tool;bpy.context.view_layer.objects.active=o;bpy.ops.object.modifier_apply(modifier=m.name);bpy.data.objects.remove(tool,do_unlink=True)
 if p.get('scribe_to'):
  template=dict(next(a for a in parts if a['id']==p['scribe_to']));template.pop('mesh_mm',None);tool=solid(template);m=o.modifiers.new('scribed_to_cap','BOOLEAN');m.operation='DIFFERENCE';m.solver='EXACT';m.object=tool;bpy.context.view_layer.objects.active=o;bpy.ops.object.modifier_apply(modifier=m.name);bpy.data.objects.remove(tool,do_unlink=True)
 bm=bmesh.new();bm.from_mesh(o.data);bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));vol=abs(bm.calc_volume());assert vol>0,(p['id'],vol);assert all(e.is_manifold for e in bm.edges),p['id'];bm.to_mesh(o.data);bm.free()
 p['mesh_mm']={'vertices':[[round(v*1000,7)for v in o.matrix_world@q.co]for q in o.data.vertices],'faces':[[i for i in f.vertices]for f in o.data.polygons]}
 reports.append({'id':p['id'],'volume_mm3':vol*1e9,'closed_manifold':True,'rebates':cuts})
(o if False else O/'data/parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2));(O/'audit/changed_meshes.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2));print('R14 geometry reconstructed:',len(reports),flush=True)
