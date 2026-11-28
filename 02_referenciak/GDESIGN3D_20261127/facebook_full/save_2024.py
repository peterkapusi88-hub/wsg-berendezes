import json,csv,urllib.request,shutil,hashlib,concurrent.futures
from pathlib import Path
from PIL import Image,ImageDraw
P=Path(__file__).resolve().parent
idx={r['id']:r for r in csv.DictReader((P/'ALBUM_INDEX.tsv').open(),delimiter='\t')}
rows=[]
for f in sorted(P.glob('2024_capture_batch*.json')): rows+=json.loads(f.read_text())
TMP=Path('/var/folders/89/glygsq9s4l59bmz5l2dlsc5r0000gn/T/browser-use/assets')
def save(r):
 d=P/r['id'];d.mkdir(exist_ok=True); b=json.loads((TMP/r['bundle']/'manifest.json').read_text());(d/'BROWSER_DOWNLOAD.json').write_text(json.dumps(b,ensure_ascii=False,indent=2));a=idx[r['id']]; photos=[]
 for n,(fbid,prefix) in enumerate(r['map'],1):
  candidates=[x for x in b['assets']+b['failures'] if x['name'].startswith(prefix+'_')]
  assert candidates,(r['id'],prefix)
  asset=candidates[0];path=d/(r['id']+'_'+str(n).zfill(2)+'.jpg');err=None
  try:
   if not path.exists():
    if asset.get('path') and Path(asset['path']).exists():shutil.copy2(asset['path'],path)
    else:path.write_bytes(urllib.request.urlopen(asset['url'],timeout=60).read())
   im=Image.open(path);im.load();w,h=im.size
   photos.append({'id':r['id']+'_'+str(n).zfill(2),'fbid':fbid,'photo_url':f'https://www.facebook.com/photo/?fbid={fbid}&set=pcb.{a["album_id"]}','source_url':asset['url'],'source_filename':asset['name'],'path':str(path),'width':w,'height':h,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'status':'downloaded'})
  except Exception as e:photos.append({'fbid':fbid,'source_url':asset['url'],'path':str(path),'status':'failed','error':str(e)})
 m={**a,'verified_date':'2026-11-27','caption':None,'caption_note':'Photo viewer had no project caption; no personal comments saved. Date and album identity from parent feed index.','cycle_confirmed':r['cycle'],'observed_count':len(r['map']),'downloaded_count':sum(x['status']=='downloaded' for x in photos),'images':photos};m['complete']=m['cycle_confirmed'] and m['downloaded_count']==m['observed_count']==int(a['expected_photos']);(d/'MANIFEST.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
 print(r['id'],m['downloaded_count'],m['complete'],flush=True)
 return m
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(save,rows))
print('Saved',len(results),'albums',sum(r['downloaded_count'] for r in results),'images',sum(r['complete'] for r in results),'complete',flush=True)
