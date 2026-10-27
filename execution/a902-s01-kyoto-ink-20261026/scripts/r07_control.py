import bpy,json,hashlib
from pathlib import Path
P=Path(__file__).resolve().parents[1];O=P/'R07_render_trial';s=bpy.context.scene;src=Path(bpy.data.filepath);h=hashlib.sha256(src.read_bytes()).hexdigest();cam=bpy.data.objects['Cam_02_Nappali_terasz'];s.camera=cam
for v in s.view_layers:v.material_override=None
s.use_nodes=False;s.render.engine='CYCLES';s.cycles.samples=16;s.render.resolution_x=1600;s.render.resolution_y=1000;s.render.resolution_percentage=100;s.render.image_settings.file_format='PNG';s.view_settings.view_transform='AgX';s.view_settings.exposure=0
for o in s.objects:
 if o.type=='LIGHT':o.hide_render=True
s.world=bpy.data.worlds.new('R07 neutral geometry and material control');s.world.use_nodes=True;s.world.node_tree.nodes.get('Background').inputs[0].default_value=(.7,.7,.7,1);s.world.node_tree.nodes.get('Background').inputs[1].default_value=.7
from mathutils import Vector
l=bpy.data.lights.new('R07 technical fill - NOT proposed installed light','AREA');l.energy=700;l.shape='DISK';l.size=4;ob=bpy.data.objects.new(l.name,l);s.collection.objects.link(ob);ob.location=(7.5,5.5,2.65);ob.rotation_euler=(Vector((5.4,6,1))-ob.location).to_track_quat('-Z','Y').to_euler()
s.render.filepath=str(O/'controls/V01_R06_native_camera_control.png');bpy.ops.render.render(write_still=True)
(O/'controls/camera_source.json').write_text(json.dumps({'source_blend':str(src),'sha256':h,'source_unchanged':hashlib.sha256(src.read_bytes()).hexdigest()==h,'camera':cam.name,'location':list(cam.location),'rotation_euler':list(cam.rotation_euler),'lens_mm':cam.data.lens,'shift_x':cam.data.shift_x,'shift_y':cam.data.shift_y,'resolution':[1600,1000],'lighting':'neutral technical control with temporary studio fill, not a proposed installed light or final evening scene','status':'conditional geometry; product reconstruction and site gates remain'},indent=2))
