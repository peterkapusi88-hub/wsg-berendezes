import bpy,json
from pathlib import Path
P=Path(__file__).resolve().parents[1];O=P/'CP3';s=bpy.context.scene
alt=bpy.data.collections['CP3_ALT053_MALM_UNAPPROVED'];alt.hide_render=False
saved={o.name:o.hide_render for o in bpy.data.objects}
for o in bpy.data.objects:
 if o.name.startswith(('KI_KI-070','KI_KI-075')) or o.get('ceiling'):o.hide_render=True
cam=bpy.data.objects['CP3_ALT053_TOP'];cam.data.ortho_scale=6.6;s.camera=cam;s.render.engine='BLENDER_WORKBENCH';s.render.resolution_x=960;s.render.resolution_y=640;s.render.filepath=str(O/'blender/ALT053_top.jpg');bpy.ops.render.render(write_still=True)
for n,v in saved.items():bpy.data.objects[n].hide_render=v
alt.hide_render=True;s.camera=bpy.data.objects['Cam_12_Nappali_Hero'];bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_CP3.blend'),compress=True)
print('Final alternative camera framing saved; main cameras unchanged.')
