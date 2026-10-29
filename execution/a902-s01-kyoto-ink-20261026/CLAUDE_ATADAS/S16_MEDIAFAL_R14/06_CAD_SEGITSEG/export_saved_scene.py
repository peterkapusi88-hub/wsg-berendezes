import bpy,json,math,hashlib
from pathlib import Path
from mathutils import Vector,Matrix
O=Path(__file__).resolve().parents[1];R=O/'01_VEGSO_TERV/R14_kulso_feny_helyreallitasa'
bpy.ops.wm.open_mainfile(filepath=str(R/'rajzok/S16_R14_faerezet.blend'))
parts=json.loads((R/'data/parts.json').read_text());drawers=json.loads((R/'data/drawers.json').read_text())
for id,hx,angle in [('T-DOOR-L',21,-90),('T-DOOR-R',849,90)]:
 pivot=Vector((hx/1000,.4,.573));rot=Matrix.Translation(pivot)@Matrix.Rotation(math.radians(angle),4,'Z')@Matrix.Translation(-pivot)
 for n in [id]+(['TEXTILE','T-DOOR-L-BACK','TEXTILE-RECESSED-HOUSING','TEXTILE-RECESSED-EMITTER']if id.endswith('L')else[]):bpy.data.objects[n].matrix_basis=rot@bpy.data.objects[n].matrix_basis
for d in drawers:
 if d['id']=='D3':
  for id in d['moving']:bpy.data.objects[id].location.y-=.3
bpy.context.view_layer.update();errors=[];geo=[]
for p in parts:
 ob=bpy.data.objects[p['id']];v=[ob.matrix_basis@Vector(a)for a in ob.bound_box];b=p['box'];errors.append(max([abs(min(q[k]for q in v)*1000-b[k])for k in range(3)]+[abs(max(q[k]for q in v)*1000-b[k]-b[k+3])for k in range(3)]))
 geo.append([p['id'],[tuple(round(v,6)for v in ob.matrix_basis@q.co)for q in ob.data.vertices]])
digest=hashlib.sha256(json.dumps(geo,sort_keys=True).encode()).hexdigest();expected=json.loads((R/'audit/saved_models_readback.json').read_text())[0]['closed_geometry_sha256'];print('GEOMETRY_CHECK',digest,expected,'max_mm',max(errors),flush=True);assert max(errors)<.001
inv=bpy.data.objects['LOCAL_TO_BLENDER_X_MIRROR'].matrix_world.inverted();ids={p['id']for p in parts};objects=[]
for ob in bpy.context.scene.objects:
 if ob.type!='MESH':continue
 transform=inv@ob.matrix_world
 names=[m.name for m in ob.data.materials if m]
 role='primary_part'if ob.name in ids else 'environment'if ob.name in ['TECHNICAL-WALL','TECHNICAL-FLOOR','CEILING-DATUM']else 'auxiliary_scene_object_VERIFY_PURPOSE'
 objects.append({'name':ob.name,'role':role,'materials':names,'vertices_mm':[[round(c*1000,6)for c in transform@v.co]for v in ob.data.vertices],'faces':[list(p.vertices)for p in ob.data.polygons],'render_visible':not ob.hide_render,'modifiers':[(m.name,m.type)for m in ob.modifiers]})
E=O/'06_CAD_SEGITSEG';E.mkdir(exist_ok=True)
(E/'R14_ZART_JELENET_MM.json').write_text(json.dumps({'units':'mm','axes':'X balrol jobbra, Y faltol elore, Z felfele; eredeti helyi alkatrész-koordináták, Blender-tükrözés visszafordítva','source':'S16_R14_faerezet.blend','source_modified':False,'primary_geometry_sha256':digest,'max_primary_bbox_error_mm':max(errors),'scope':'Mentett alaphálók névleges zárt állapotban. A nem fő alkatrész objektumok lámpafelületeket, segéd-/környezeti elemeket is tartalmaznak; nem automatikus alkatrészlista, nem gyártási CAD. Modifierek nincsenek alkalmazva.','objects':objects},ensure_ascii=False,separators=(',',':')))
print('S16_EXPORT_OK',len(objects),digest,flush=True)
