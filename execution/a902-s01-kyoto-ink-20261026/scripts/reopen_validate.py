import bpy,json,hashlib
from pathlib import Path
P=Path('/Users/peterkapusi/Documents/ChatGPT/WSG – Stíluslabor/execution/a902-s01-kyoto-ink-20261026');s=bpy.context.scene
result=dict(file=bpy.data.filepath,sha256=hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest(),object_count=len(bpy.data.objects),revision=s.get('KI_revision'),custom_objects=sum(1 for o in bpy.data.objects if o.name.startswith('KI_')),status='SAVED_FILE_REOPENED_SUCCESSFULLY; technical approval not implied')
assert result['revision']=='KI-V33-R02';assert result['custom_objects']>100
s.camera=bpy.data.objects['Cam_11_Master_Panorama'];s.render.resolution_x=960;s.render.resolution_y=600;s.render.filepath=str(P/'blender/QA_Cam_11_Master_Panorama.png');bpy.ops.render.render(write_still=True)
r=json.loads((P/'blender/camera_runs_R02.json').read_text());o=s.camera;r=[x for x in r if x['camera_id']!=o.name];r.append(dict(camera_id=o.name,location=list(o.location),rotation_euler=list(o.rotation_euler),lens_mm=o.data.lens,shift_y=o.data.shift_y,image='blender/QA_'+o.name+'.png',status='rendered neutral dimensional study, identity/detail not final'))
(P/'blender/camera_runs_R02.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));(P/'blender/reopen_check_R02.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
