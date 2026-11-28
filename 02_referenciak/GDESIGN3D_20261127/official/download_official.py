import urllib.request,json,hashlib,concurrent.futures
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent
BASE='https://www.gdesign.hu'
projects=json.loads((ROOT/'projects.source.json').read_text())
jobs=[]
for p in projects:
 slug=p['slug'];m=json.loads((ROOT/slug/'manifest.source.json').read_text());
 for im in m['images']:
  name=im['name'] if isinstance(im,dict) else im
  jobs.append((p,name,'gallery/'+name+'.webp'))
 jobs.append((p,'banner','banner-lg.webp'))
def one(job):
 p,name,rel=job; slug=p['slug']; url=f'{BASE}/images/projects/{slug}/{rel}'; path=ROOT/slug/(name+'.webp')
 try:
  if not path.exists(): path.write_bytes(urllib.request.urlopen(url,timeout=60).read())
  im=Image.open(path); im.load(); w,h=im.size
  return {'project':p['name'],'slug':slug,'reference_id':slug+'_'+name,'role':'banner' if name=='banner' else 'gallery','source_url':url,'project_url':f'{BASE}/hu/projekt.html?slug={slug}','path':str(path),'width':w,'height':h,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'status':'downloaded','verified_date':'2026-11-27'}
 except Exception as e:return {'slug':slug,'reference_id':slug+'_'+name,'source_url':url,'path':str(path),'status':'failed','error':str(e)}
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
 rows=list(ex.map(one,jobs))
(ROOT/'DOWNLOAD_MANIFEST.json').write_text(json.dumps({'source':'https://www.gdesign.hu/hu/munkaink.html','verified_date':'2026-11-27','coverage':'All 11 residential project galleries listed by the official portfolio, including banner; not a claim of exhaustive Facebook history.','projects':projects,'images':rows},ensure_ascii=False,indent=2))
for p in projects:
 r=[i for i in rows if i['slug']==p['slug']];print(p['name'],len(r),'images;',sum(i['status']=='failed' for i in r),'failed')
print('TOTAL',len(rows),'BYTES',sum(i.get('bytes',0) for i in rows))
