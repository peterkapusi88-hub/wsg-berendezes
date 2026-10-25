import runpy,json,os
g=runpy.run_path(os.environ['CAM02_DIR']+'/01_render_cam02_korr.py')
json.dump(g['result'],open(os.path.join(os.environ['CAM02_DIR'],os.environ['CAM02_OUT'],'result.json'),'w'),ensure_ascii=False,indent=1)
