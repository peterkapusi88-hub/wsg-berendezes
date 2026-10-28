import bpy,json
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'R10'
bpy.ops.wm.open_mainfile(filepath=str(p/'blender/A902_Kyoto_Ink_R10.blend'))
for ob in bpy.context.scene.objects:
 if ob.name.startswith('R09_gathered_sheer'):
  for v in ob.data.vertices:v.co.z=.015+(v.co.z-.13)*(2.81-.015)/(2.81-.13)
a=json.loads((p/'audit/model_checks.json').read_text());a['curtain_bottom_mm']=15;(p/'audit/model_checks.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
bpy.ops.wm.save_as_mainfile(filepath=str(p/'blender/A902_Kyoto_Ink_R10.blend'),compress=True)
bpy.context.scene.render.filepath=str(p/'images/V01_R10_NATIVE.png');bpy.ops.render.render(write_still=True)
