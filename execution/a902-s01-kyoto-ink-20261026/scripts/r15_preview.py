import bpy,json,struct,math,hashlib
from pathlib import Path
from mathutils import Vector,Matrix
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
parts=json.loads((O/'data/parts.json').read_text());hardware=json.loads((O/'data/hardware_geometry.json').read_text());poses=json.loads((O/'data/exploded_poses.json').read_text())
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def mat(n,c):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(*c,1);m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=.65;return m
mats={'M01':mat('Grafit / sematikus',(.12,.115,.105)),'M02':mat('Panelhordozo / sematikus',(.48,.39,.29)),'M03':mat('Korpusz / sematikus',(.65,.61,.53))};steel=mat('Vasalat helyfoglalas',(.12,.37,.49));elec=mat('Villamos komponens helyfoglalas',(.60,.42,.09));woods={};hwobs={};proof=[]
for p in parts:
 path=Path('/tmp/ki15_stls')/(p['id']+'.stl');data=path.read_bytes();n=struct.unpack_from('<I',data,80)[0];vs=[];fs=[]
 for i in range(n):
  vals=struct.unpack_from('<12fH',data,84+50*i);fs.append(tuple(range(len(vs),len(vs)+3)));vs.extend([tuple(v/1000 for v in vals[j:j+3]) for j in [3,6,9]])
 bb=p['assembly_box_mm'];shift=[(-bb[k]+.000001)/1000 if bb[k]<0 else 0 for k in range(3)];vs=[tuple(v[k]-shift[k] for k in range(3)) for v in vs]
 errors=[max(abs(min(v[k] for v in vs)*1000-bb[k]),abs(max(v[k] for v in vs)*1000-bb[k]-bb[k+3])) for k in range(3)];assert max(errors)<.001,(p['id'],errors)
 me=bpy.data.meshes.new(p['id']);me.from_pydata(vs,[],fs);me.update();ob=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(ob);ob.data.materials.append(mats.get(p['material'][:3],mats['M03']));ob['source']='AutoCAD2027 machined STL';ob['part']=p['id'];ob['revision']='R15';woods[p['id']]=ob;proof.append({'part':p['id'],'STL_sha256':hashlib.sha256(data).hexdigest(),'restored_shift_m':shift,'max_bbox_error_mm':max(errors)})
def box(name,b,material):
 bpy.ops.mesh.primitive_cube_add(size=1,location=tuple((b[i]+b[i+3]/2)/1000 for i in range(3)));ob=bpy.context.object;ob.name=name;ob.dimensions=tuple(v/1000 for v in b[3:]);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);ob.data.materials.append(material);return ob
for h in hardware:
 ob=box(h['id'],h['box'],elec if h['id'].startswith(('EL','PSU','DIM','TRAY')) else steel);ob['sku']=h['sku'];ob['geometry']='SIMPLIFIED_ENVELOPE_NOT_MANUFACTURER_MESH';hwobs[h['id']]=ob
floor=mat('Neutralis',(.78,.78,.76));bpy.ops.mesh.primitive_plane_add(size=200);bpy.context.object.data.materials.append(floor)
def aim(o,p):o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
for loc,power,size in [((1,-6,8),1600,6),((-4,-1,5),1000,5),((4,4,6),1800,5)]:
 bpy.ops.object.light_add(type='AREA',location=loc);ob=bpy.context.object;ob.data.energy=power;ob.data.size=size;aim(ob,(1.8,0,1.4))
bpy.ops.object.camera_add(location=(6,-10,6));cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=5.5;aim(cam,(1.65,0,1.42));s=bpy.context.scene;s.camera=cam;s.render.engine='CYCLES';s.cycles.samples=20;s.cycles.use_denoising=True;s.render.resolution_x=1600;s.render.resolution_y=1100;s.render.resolution_percentage=100;s.world.color=(.5,.5,.5);s.view_settings.view_transform='AgX'
def render(n):s.render.filepath=str(O/'audit'/n);bpy.ops.render.render(write_still=True)
for ob in hwobs.values():ob.hide_render=True
render('zart.png')
for ob in hwobs.values():ob.hide_render=ob.name in ['TV-SCREEN','TV-BRACKET'] or ob.name.startswith(('HINGE','TIP'))
for id,ob in woods.items():ob.matrix_world=Matrix.Translation(Vector(poses[id])/1000)
cam.data.ortho_scale=6;render('robbantott.png')
# Isolated M5 module. Covers removed purely for visibility, not a functional pose.
for id,ob in woods.items():
 ob.matrix_world=Matrix.Identity(4);p=next(p for p in parts if p['id']==id);ob.hide_render=not(p['assembly_box_mm'][0]>=2910 and p['assembly_box_mm'][2]<550 and p['type'] not in ['TV02-F2','TV03-P'])
for id,ob in hwobs.items():ob.hide_render=not id.startswith(('HG-5','WP-HG-5'))
cam.location=(2.7,-.6,.95);cam.data.ortho_scale=1.05;aim(cam,(3.25,.22,.35));render('pilot.png')
for id,ob in woods.items():ob.hide_render=id not in ['KI12-TV02S-09','KI14-BAT-11','KI14-RAIL-05']
for id,ob in hwobs.items():ob.hide_render=id!='HG-5-1'
cam.location=(3.3,-.1,.72);cam.data.ortho_scale=.33;aim(cam,(2.94,.33,.46));render('fuggeszto.png')
for id,ob in woods.items():
 p=next(p for p in parts if p['id']==id);b=p['assembly_box_mm'];ob.hide_render=not(b[0]>=840 and b[0]+b[3]<=1530 and b[2]<550 and p['type'] not in ['TV02-F2'])
for id,ob in hwobs.items():ob.hide_render=not id.startswith(('EL','PSU','DIM','TRAY'))
cam.location=(1.6,-.65,.85);cam.data.ortho_scale=.95;aim(cam,(1.15,.18,.28));render('villamos.png')
for ob in woods.values():ob.hide_render=False
for ob in hwobs.values():ob.hide_render=False
cam.location=(6,-10,6);cam.data.ortho_scale=5.5;aim(cam,(1.65,0,1.42))
bpy.ops.wm.save_as_mainfile(filepath=str(O/'rajzok/TV_R15_koordinacio.blend'))
(O/'audit/blender_provenance.json').write_text(json.dumps({'source_DWG_sha256':hashlib.sha256((O/'rajzok/TV_R15_megmunkalt.dwg').read_bytes()).hexdigest(),'wood_parts':proof,'hardware_meshes':'113 simplified envelopes, not manufacturer geometry','physical_load_approval':False},indent=2))
print('R15_ACTUAL_CAD_PREVIEW_COMPLETE',len(woods),len(hwobs))
