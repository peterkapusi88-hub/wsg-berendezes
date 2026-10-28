"""Render actual AutoCAD STL exports, not a generative furniture picture."""
import bpy,json,struct,math
from pathlib import Path
from mathutils import Vector,Matrix
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
parts=json.loads((O/'data/parts.json').read_text());poses=json.loads((O/'data/view_poses.json').read_text())
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def mat(name,color):
 m=bpy.data.materials.new(name);m.diffuse_color=(*color,1);m.use_nodes=True;m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(*color,1);m.node_tree.nodes['Principled BSDF'].inputs['Roughness'].default_value=.65;return m
mats={'M01':mat('M01_grafit_sematikus',(.12,.115,.105)),'M02':mat('M02_nyomathordozo_sematikus',(.48,.39,.29)),'M03':mat('M03_korpusz_sematikus',(.65,.61,.53))}
red=mat('Nyitott_dontes_front_3_4',(.55,.25,.08));objs=[]
for p in parts:
 data=Path('/tmp/ki14_stls/'+p['id']+'.stl').read_bytes();n=struct.unpack_from('<I',data,80)[0];vs=[];fs=[]
 for i in range(n):
  vals=struct.unpack_from('<12fH',data,84+50*i)
  fs.append(tuple(range(len(vs),len(vs)+3)));vs.extend([tuple(v/1000 for v in vals[j:j+3]) for j in [3,6,9]])
 # AutoCAD STLOUT shifts negative axes into the positive octant. Reverse ONLY
 # that documented offset, then independently verify the assembly bounds.
 bb=p['assembly_box_mm'];shift=[(-bb[k]+.000001)/1000 if bb[k]<0 else 0 for k in range(3)]
 vs=[tuple(v[k]-shift[k] for k in range(3)) for v in vs]
 assert all(abs(min(v[k] for v in vs)*1000-bb[k])<.001 and abs(max(v[k] for v in vs)*1000-bb[k]-bb[k+3])<.001 for k in range(3)),p['id']
 me=bpy.data.meshes.new(p['id']);me.from_pydata(vs,[],fs);me.update();ob=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(ob)
 ob.data.materials.append(mats.get(p['material'][:3],mats['M03']));ob['source']='AutoCAD2027 native STL';ob['part_id']=p['id'];ob['revision']='R14';ob['holes']=p['hole_count'];objs.append(ob)
floor=mat('Hatterszin',(.78,.78,.76));bpy.ops.mesh.primitive_plane_add(size=200,location=(0,0,.0));bpy.context.object.data.materials.append(floor)
def aim(obj,where):obj.rotation_euler=(Vector(where)-obj.location).to_track_quat('-Z','Y').to_euler()
for loc,power,size in [((1,-6,8),1600,6),((-4,-1,5),1000,5),((4,4,6),1800,5)]:
 bpy.ops.object.light_add(type='AREA',location=loc);l=bpy.context.object;l.data.energy=power;l.data.shape='DISK';l.data.size=size;aim(l,(1.8,0,1.4))
bpy.ops.object.camera_add(location=(6,-10,6));cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=5.5;aim(cam,(1.65,0,1.42));bpy.context.scene.camera=cam
s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=24;s.cycles.use_denoising=True;s.render.resolution_x=1800;s.render.resolution_y=1250;s.render.resolution_percentage=100;s.world.color=(.5,.5,.5);s.view_settings.view_transform='AgX'
def render(name):s.render.filepath=str(O/'audit'/name);bpy.ops.render.render(write_still=True)
render('zart.png')
cam.location=(5,8,5);aim(cam,(1.65,.3,1.42));render('hatul.png')
cam.location=(6,-10,6);aim(cam,(1.65,0,1.42))
for ob in objs:
 pose=poses[ob.name];q=Vector(pose['pivot'])/1000;t=Vector(pose['translation'])/1000
 ob.matrix_world=Matrix.Translation(t)@Matrix.Translation(q)@Matrix.Rotation(math.radians(pose['rotation_deg']),4,'Z')@Matrix.Translation(-q)
 if any(pose['translation']):ob.data.materials[0]=red
render('belso.png')
bpy.ops.wm.save_as_mainfile(filepath=str(O/'rajzok/TV_R14_CAD_ellenorzokep.blend'))
for ob in objs:
 ob.matrix_world=Matrix.Translation(Vector(poses[ob.name]['exploded_translation'])/1000)
cam.data.ortho_scale=6.1;render('robbantott.png')
# Cup detail: exact STL, back of left tower front, isolated.
for ob in objs:ob.hide_render=ob.name!='KI12-TV01F-01';ob.matrix_world=Matrix.Identity(4)
cam.location=(.15,.35,2.85);aim(cam,(.0245,-.003,2.7785));cam.data.ortho_scale=.16
s.render.resolution_x=1000;s.render.resolution_y=800
render('pant_reszlet.png')
for ob in objs:
 ob.hide_render=ob.name not in ['KI12-TV02S-01','KI14-BAT-03','KI12-TV02H1-01','KI14-RAIL-01'];ob.matrix_world=Matrix.Identity(4)
cam.location=(.7,1.0,.8);aim(cam,(.10,.36,.44));cam.data.ortho_scale=.6
render('hatlap_reszlet.png')
print('CAD_NATIVE_STL_RENDER_COMPLETE',len(objs))
