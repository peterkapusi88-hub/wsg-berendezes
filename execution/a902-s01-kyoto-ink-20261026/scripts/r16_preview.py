import bpy,json,struct,hashlib,math
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok'
parts=json.loads((O/'data/parts.json').read_text());hardware=json.loads((O/'data/hardware_geometry.json').read_text());drawers=json.loads((O/'data/drawers.json').read_text());art=json.loads((O/'data/art_triangles.json').read_text())
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def mat(n,c):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(*c,1);m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=.78;return m
bronze=mat('Bronzbarna / tervi szin, fizikai minta kell',(.19,.14,.105));panel=mat('Textilhatasu nyomtathato falburkolat / minta kell',(.52,.43,.32));wood=mat('Nyir15mm',(.70,.60,.43));inside=mat('Korpuszbelseje',(.6,.57,.52));metal=mat('Vasalati helyfoglalo',(.08,.32,.40));ink=mat('Tusgrafika',(.025,.022,.018));black=mat('TV',(.008,.009,.011));gold=mat('Profil LED',(.9,.48,.12));objs={};hs={};proof=[]
for p in parts:
 f=Path('/tmp/ki16v2_stls')/(p['id']+'.stl');raw=f.read_bytes();n=struct.unpack_from('<I',raw,80)[0];vs=[];faces=[]
 for i in range(n):
  a=struct.unpack_from('<12fH',raw,84+50*i);faces.append(tuple(range(len(vs),len(vs)+3)));vs.extend([tuple(v/1000 for v in a[j:j+3]) for j in [3,6,9]])
 bb=p['assembly_box_mm'];shift=[(-bb[k]+.000001)/1000 if bb[k]<0 else 0 for k in range(3)];vs=[tuple(v[k]-shift[k] for k in range(3)) for v in vs]
 err=max(max(abs(min(v[k] for v in vs)*1000-bb[k]),abs(max(v[k] for v in vs)*1000-bb[k]-bb[k+3])) for k in range(3));assert err<.001,(p['id'],err)
 me=bpy.data.meshes.new(p['id']);me.from_pydata(vs,[],faces);me.update();ob=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(ob)
 ma=panel if p['type']=='TV03-P' else wood if p['type']=='DRAWER' else bronze if p['type'] in ['TV01-F','TV02-F1','TV02-F2','GAP','TV02-CAP'] else inside
 ob.data.materials.append(ma)
 if p['type'] in ['TV01-S','TV01-T']:
  ob.data.materials.append(bronze)
  for face in me.polygons:
   coords=[me.vertices[v].co for v in face.vertices]
   if all(abs(v.x)<.000001 for v in coords) or all(abs(v.x-.720)<.000001 for v in coords) or all(abs(v.z-2.880)<.000001 for v in coords):face.material_index=1
 ob['part_id']=p['id'];ob['revision']='R16';ob['source']='native AutoCAD machined STL';objs[p['id']]=ob;proof.append({'id':p['id'],'sha256':hashlib.sha256(raw).hexdigest(),'bbox_error_mm':err})
for h in hardware:
 b=h['box'];bpy.ops.mesh.primitive_cube_add(size=1,location=[(b[k]+b[k+3]/2)/1000 for k in range(3)]);ob=bpy.context.object;ob.name=h['id'];ob.dimensions=[q/1000 for q in b[3:]];bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);ob.data.materials.append(black if h['id']=='TV-SCREEN' else gold if h['id'].startswith('LED') else metal);ob['geometry']='simplified envelope, not manufacturer model';hs[h['id']]=ob
for q in art:
 me=bpy.data.meshes.new('INK_'+q['part']);verts=[];faces=[]
 for tri in q['triangles']:
  faces.append(tuple(range(len(verts),len(verts)+3)));verts.extend([(x/1000,(q['Y']-.04)/1000,z/1000) for x,z in tri])
 me.from_pydata(verts,[],faces);me.update();ob=bpy.data.objects.new('INK_'+q['part'],me);bpy.context.collection.objects.link(ob);ob.data.materials.append(ink)
def aim(o,p):o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
for loc,pow,size in [((1,-5,7),1300,5),((-4,-2,5),1000,5),((4,3,6),1500,5)]:
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=pow;o.data.size=size;aim(o,(1.8,0,1.4))
bpy.ops.object.camera_add(location=(5,-9,5));cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=5.0;aim(cam,(1.8,0,1.45));s=bpy.context.scene;s.camera=cam;s.render.engine='CYCLES';s.cycles.samples=16;s.cycles.use_denoising=True;s.render.resolution_x=1600;s.render.resolution_y=1150;s.render.resolution_percentage=100;s.world.color=(.65,.65,.65);s.view_settings.view_transform='AgX'
for id,ob in hs.items():ob.hide_render=id!='TV-SCREEN' and not id.startswith('LED')
def render(n):s.render.filepath=str(O/'audit'/n);bpy.ops.render.render(write_still=True)
render('R16_zart.png')
for d in drawers:
 for id in [d['front']]+d['parts']:objs[id].location.y=-.3
render('R16_fiokok.png')
for d in drawers:
 for id in [d['front']]+d['parts']:objs[id].location.y=0
# Saved model opens closed, hardware envelopes hidden only in render, all objects accessible.
bpy.ops.wm.save_as_mainfile(filepath=str(O/'rajzok/TV_R16_koordinacio.blend'))
(O/'audit/blender_provenance.json').write_text(json.dumps({'parts':proof,'source':'TV_R16_megmunkalt.dwg STL exports','render_status':'technical preview, not a photoreal validated room render','wood_bbox_checked':True,'hardware_factory_geometry':False},indent=2))
