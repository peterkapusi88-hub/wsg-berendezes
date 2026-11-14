import runpy,json,os
D=os.environ['CAM02_DIR']
g0=runpy.run_path(D+'/00_lepcso_wrapper.py')
g=runpy.run_path(D+'/01_render_cam02_korr.py')
import bpy
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector
sc=bpy.context.scene; CAM=sc.camera; i=g0['info']
pts={k:[round(c,1) for c in ((lambda p:(p.x*1600,(1-p.y)*1000))(world_to_camera_view(sc,CAM,Vector(P))))] for k,P in {'lepcso_front_x4.44_teto':(4.44,i['Y0'],i['H']),'lepcso_front_x8.94_teto':(8.94,i['Y0'],i['H']),'lepcso_front_x8.94_alj':(8.94,i['Y0'],0)}.items()}
res=g['result']; res['lepcso']=i; res['lepcso_px']=pts
json.dump(res,open(os.path.join(D,os.environ['CAM02_OUT'],'result.json'),'w'),ensure_ascii=False,indent=1)
