import pathlib,json
p=pathlib.Path(__file__).resolve().parent;m=json.loads((p/'MANIFEST.json').read_text())
pending=[j for j in m['jobs'] if j['status']=='PENDING' and not (p/j['output']).exists()]
def anchor(j):
 c=j['camera']
 if c=='Cam_03':return 'Cam_12'
 if c in ['Cam_12','Cam_02_DAY']:return 'Cam_02'
 if c in ['LIVING_WINDOW','KITCHEN_HERO']:return 'LIVING_HERO'
 if c=='Cam_11c':return 'Cam_04'
 if c.endswith('_MEDIA'):return c.replace('_MEDIA','_HERO')
 return None
jobs=[]
if pending:
 group=(pending[0]['apartment'],pending[0]['variant'])
 for j in pending:
  if (j['apartment'],j['variant'])!=group:continue
  a=anchor(j);f=p/'renders'/(j['apartment']+'_'+j['variant']+'_'+str(a)+'_v1.png')
  if a and not f.exists():continue
  j['prompt_text']=(p/j['prompt']).read_text()
  if a:
   j['inputs']=j['inputs'][:4]+[str(f)];j['prompt_text']+='\n\nCONTINUITY INPUT. Last image shows this exact new variant in another camera. Keep its exact furniture materials, art, pendant design and cabinetry details, with Image 1 governing camera and shell. Transfer only visible matching surfaces; never copy an opposite TV wall onto an art wall.'
  jobs.append(j)
  if len(jobs)==4:break
print(json.dumps(jobs))
