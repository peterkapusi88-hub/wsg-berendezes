import bpy,math
from pathlib import Path
from mathutils import Matrix,Vector
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
bpy.ops.wm.open_mainfile(filepath=str(O/'rajzok/TV_R14_CAD_ellenorzokep.blend'))
keep=['KI12-TV02S-01','KI14-BAT-03','KI12-TV02H1-01','KI14-RAIL-01']
for ob in bpy.data.objects:
 if ob.type=='MESH':
  ob.hide_render=ob.name not in keep
  if ob.name in keep:ob.matrix_world=Matrix.Identity(4)
for name,color in [('KI14-BAT-03',(.55,.32,.10)),('KI14-RAIL-01',(.12,.35,.30)),('KI12-TV02H1-01',(.48,.51,.52)),('KI12-TV02S-01',(.58,.52,.43))]:
 ob=bpy.data.objects[name];m=bpy.data.materials.new(name+'_azonosito');m.use_nodes=True;m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value=(*color,1);ob.data.materials.clear();ob.data.materials.append(m)
bpy.data.objects['KI12-TV02H1-01'].matrix_world=Matrix.Translation((.16,.10,0))
bpy.data.objects['KI12-TV02S-01'].matrix_world=Matrix.Translation((-.05,0,0))
s=bpy.context.scene;cam=s.camera;cam.location=(-.7,.9,.8);cam.rotation_euler=(Vector((.08,.38,.38))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=.75
s.render.resolution_x=1400;s.render.resolution_y=1100;s.cycles.samples=32;s.render.filepath=str(O/'audit/hatlap_reszlet.png');bpy.ops.render.render(write_still=True)
