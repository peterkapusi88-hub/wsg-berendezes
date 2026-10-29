from pathlib import Path
import bpy,json,math,hashlib
from mathutils import Vector,Matrix
O=Path(__file__).resolve().parents[1];parts=json.loads((O/'data/parts.json').read_text());drawers=json.loads((O/'data/drawers.json').read_text());reports=[]
for style in ['faerezet']:
 bpy.ops.wm.open_mainfile(filepath=str(O/'rajzok'/f'S16_R14_{style}.blend'))
 original={ob.name:ob.matrix_basis.copy()for ob in bpy.data.objects if ob.type=='MESH'}
 # The curved terminal cap is fully inside the TV field at z670..673; remove duplicate internal solid.
 duplicate=bpy.data.objects.get('DECK-CURVE-HIDDEN-END')
 if duplicate:bpy.data.objects.remove(duplicate,do_unlink=True)
 for id,hx,angle in [('T-DOOR-L',21,-90),('T-DOOR-R',849,90)]:
  pivot=Vector((hx/1000,.4,.573));rot=Matrix.Translation(pivot)@Matrix.Rotation(math.radians(angle),4,'Z')@Matrix.Translation(-pivot)
  names=[id]+(['TEXTILE','T-DOOR-L-BACK','TEXTILE-RECESSED-HOUSING','TEXTILE-RECESSED-EMITTER']if id.endswith('L')else[])
  for n in names:bpy.data.objects[n].matrix_basis=rot@bpy.data.objects[n].matrix_basis
 for d in drawers:
  if d['id']=='D3':
   for id in d['moving']:bpy.data.objects[id].location.y-=.3
 bpy.context.view_layer.update();errors=[];geometry=[]
 for p in parts:
  ob=bpy.data.objects[p['id']];v=[ob.matrix_basis@Vector(a)for a in ob.bound_box];b=p['box'];e=max([abs(min(q[k]for q in v)*1000-b[k])for k in range(3)]+[abs(max(q[k]for q in v)*1000-b[k]-b[k+3])for k in range(3)]);errors.append({'id':p['id'],'bbox_error_mm':e})
  verts=[tuple(round(v,6)for v in ob.matrix_basis@q.co)for q in ob.data.vertices];geometry.append([p['id'],verts])
 assert max(q['bbox_error_mm']for q in errors)<.001,errors
 hits=[]
 for x,z in [(100,400),(200,1500),(300,2600)]:
  hit,loc,normal,idx,obj,matrix=bpy.context.scene.ray_cast(bpy.context.evaluated_depsgraph_get(),Vector((-x/1000,1,z/1000)),Vector((0,-1,0)))
  hits.append({'object':obj.name if hit else None,'y_mm':loc.y*1000 if hit else None})
 assert all(q['object']=='TEXTILE'and abs(q['y_mm']-374)<.001 for q in hits),hits
 digest=hashlib.sha256(json.dumps(geometry,sort_keys=True).encode()).hexdigest()
 reports.append({'style':style,'primary_parts':len(parts),'max_bbox_error_mm':max(q['bbox_error_mm']for q in errors),'closed_geometry_sha256':digest,'visibility_rays':hits,'scope':'Saved Blender primary meshes and nominal closed poses. Not factory hinge, photometric or CNC certification.'})
 for n,m in original.items():
  if n in bpy.data.objects:bpy.data.objects[n].matrix_basis=m
 bpy.context.view_layer.update();bpy.ops.wm.save_as_mainfile(filepath=str(O/'rajzok'/f'S16_R14_{style}.blend'))
assert reports[0]['primary_parts']==len(parts)
(O/'audit/saved_models_readback.json').write_text(json.dumps(reports,ensure_ascii=False,indent=2));print('R14_SAVED_MODELS_AND_INSERT_OK',flush=True)

# Verify actual emitted geometry and unobstructed light paths in the saved scene.
scene=bpy.context.scene;dg=bpy.context.evaluated_depsgraph_get()
emit=bpy.data.objects['A1-OUTER-UP-CONCEALED']
ys=[(emit.matrix_world@v.co).y*1000 for v in emit.data.vertices]
assert max(abs(y-4) for y in ys)<.001,ys[:4]
checks=[]
for label,origin,direction,expected in [('right_outward',(-3.590,.0038,1.5),(0,-1,0),'TECHNICAL-WALL'),('upper_outward',(-2.0,.0038,2.865),(0,-1,0),'TECHNICAL-WALL'),('upward_gap',(-2.0,.015,2.8763),(0,0,1),'CEILING-DATUM'),('downwash_surface',(-2.0,.0309,2.866),(0,-1,0),'BG-FINISH')]:
 hit,loc,normal,idx,ob,ma=scene.ray_cast(dg,Vector(origin),Vector(direction))
 assert hit and ob.name==expected,(label,ob.name if ob else None)
 checks.append({'path':label,'first_surface':ob.name,'hit_mm':[round(v*1000,3)for v in loc]})
old=json.loads((O.parent/'R13_folytonos_kulso_feluletek/audit/saved_models_readback.json').read_text())[0]
new=json.loads((O/'audit/saved_models_readback.json').read_text())[0]
assert old['closed_geometry_sha256']==new['closed_geometry_sha256']
(O/'audit/saved_lighting_readback.json').write_text(json.dumps({'A1_emitter_y_mm':ys[0],'paths':checks,'main_geometry_matches_R13':True,'scope':'Geometric light-path checks, not calibrated illuminance or product validation'},ensure_ascii=False,indent=2))
print('R14_REAL_LIGHT_POSITIONS_AND_PATHS_OK',flush=True)
