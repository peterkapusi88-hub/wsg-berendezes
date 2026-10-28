import bpy,json,hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'R08_pilot';S=bpy.context.scene
src=Path(bpy.data.filepath);sha=hashlib.sha256(src.read_bytes()).hexdigest()
lock=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text())
C=bpy.data.collections.new('KI_R08_ARCHITECTURE_RESTORATION');S.collection.children.link(C)
def mat(n,c):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;m.node_tree.nodes.get('Principled BSDF').inputs['Base Color'].default_value=(*c,1);return m
white=mat('R08 existing white window frames',(.82,.82,.78));wood=bpy.data.materials.get('R06 natural oak sample pending') or white
glass=mat('R08 clear existing glazing',(.95,.98,1));bs=glass.node_tree.nodes.get('Principled BSDF');bs.inputs['Transmission Weight'].default_value=1;bs.inputs['Roughness'].default_value=.03;bs.inputs['IOR'].default_value=1.45
checks=[]
def box(n,b,m,status):
 x,y,z,X,Y,Z=b;bpy.ops.mesh.primitive_cube_add(size=1,location=((x+X)/2,(y+Y)/2,(z+Z)/2));o=bpy.context.object;o.name='R08_'+n;o.dimensions=(X-x,Y-y,Z-z);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 for c in list(o.users_collection):c.objects.unlink(o)
 C.objects.link(o);o.data.materials.append(m);o['source_status']=status;return o
for n,b in lock['openings'].items():
 if not n.startswith(('Uvegfal_','Erkelyajto_')):continue
 for old in list(bpy.data.objects):
  if n in old.name:old.hide_render=True;old.hide_set(True)
 o=box(n,b,glass if n.endswith('_uveg') else white,'GEOMETRY_LOCK_V2B_NOT_SITE_MEASURED')
 bpy.context.view_layer.update();pts=[o.matrix_world@Vector(v) for v in o.bound_box];actual=[min(v[i] for v in pts) for i in range(3)]+[max(v[i] for v in pts) for i in range(3)];err=max(abs(a-c) for a,c in zip(actual,b));checks.append({'object':o.name,'max_error_m':err,'result':'PASS_LOCK_MATCH' if err<1e-5 else 'FAIL','scope':'source plan bounds only; not site survey'})
box('living_threshold_PHOTO_PROVISIONAL_100mm',(4.44,8.00,0,8.94,8.21,.10),wood,'PHOTO_CONFIRMS_PRESENCE_HEIGHT_100MM_PROVISIONAL_SITE_MEASUREMENT_REQUIRED')
# The source placement and procurement envelopes are deliberately retained.
# No speculative outdoor product is presented as an approved selection.
for o in S.objects:
 if o.type=='LIGHT':o.hide_render=True
for v in S.view_layers:v.material_override=None
S.use_nodes=False;S.render.engine='CYCLES';S.cycles.samples=24;S.render.resolution_x=1600;S.render.resolution_y=1000;S.render.resolution_percentage=100;S.render.image_settings.file_format='PNG';S.view_settings.view_transform='AgX';S.view_settings.exposure=0
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];cam=S.camera
S.world=bpy.data.worlds.new('R08 neutral control world');S.world.use_nodes=True;S.world.node_tree.nodes.get('Background').inputs[0].default_value=(.7,.7,.7,1);S.world.node_tree.nodes.get('Background').inputs[1].default_value=.45
l=bpy.data.lights.new('R08 technical fill NOT installed fixture','AREA');l.energy=450;l.shape='DISK';l.size=4;ob=bpy.data.objects.new(l.name,l);S.collection.objects.link(ob);ob.location=(7.5,5.5,2.65);ob.rotation_euler=(Vector((5.4,6,1))-ob.location).to_track_quat('-Z','Y').to_euler()
bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_R08.blend'),compress=True)
S.render.filepath=str(O/'images/V01_R08_NATIVE_CONTROL.png');bpy.ops.render.render(write_still=True)
audit={'source_blend_sha256':sha,'source_unchanged':hashlib.sha256(src.read_bytes()).hexdigest()==sha,'camera':cam.name,'location':list(cam.location),'rotation':list(cam.rotation_euler),'lens':cam.data.lens,'checks':checks,'threshold':'presence photo-proven; 100mm height provisional','lighting':'technical fill, not installed or photometrically validated','outdoor':'unchanged provisional envelopes; exact products unresolved','status':'CONDITIONAL_CONTROL_NOT_FINAL_RENDER'}
(O/'audit/model_checks.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2));print('R08_COMPLETE',len(checks))
