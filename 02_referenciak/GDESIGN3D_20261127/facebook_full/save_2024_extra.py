import json, urllib.request, shutil, hashlib, concurrent.futures
from pathlib import Path
from PIL import Image, ImageDraw
P = Path(__file__).resolve().parent
idx = {r['id']: r for r in json.loads((P/'2024_EXTRA_INDEX.json').read_text())}
rows = json.loads((P/'2024_EXTRA_CAPTURE.json').read_text())
TMP = Path('/var/folders/89/glygsq9s4l59bmz5l2dlsc5r0000gn/T/browser-use/assets')
def save(r):
    d=P/r['id']; d.mkdir(exist_ok=True)
    b=json.loads((TMP/r['bundle']/'manifest.json').read_text())
    (d/'BROWSER_DOWNLOAD.json').write_text(json.dumps(b,ensure_ascii=False,indent=2))
    a=idx[r['id']]; photos=[]
    for n,(fbid,key) in enumerate(r['map'],1):
        candidates=[x for x in b['assets']+b['failures'] if x['name']==key or x['name'].startswith(key+'_')]
        assert len(candidates)==1,(r['id'],key,len(candidates))
        asset=candidates[0]; path=d/(r['id']+'_'+str(n).zfill(2)+'.jpg')
        try:
            if not path.exists():
                if asset.get('path') and Path(asset['path']).exists(): shutil.copy2(asset['path'],path)
                else: path.write_bytes(urllib.request.urlopen(asset['url'],timeout=60).read())
            im=Image.open(path); im.load(); w,h=im.size
            photos.append({'id':r['id']+'_'+str(n).zfill(2),'fbid':fbid,'photo_url':f'https://www.facebook.com/photo/?fbid={fbid}&set=pcb.{a["album_id"]}','source_url':asset['url'],'source_filename':asset['name'],'path':str(path),'width':w,'height':h,'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'status':'downloaded'})
        except Exception as e: photos.append({'fbid':fbid,'source_url':asset['url'],'path':str(path),'status':'failed','error':str(e)})
    m={**a,'verified_date':'2026-11-27','caption_note':'Observed public feed caption; whitespace normalized, emojis may be omitted by DOM; visible truncation retained. No personal comments saved.','cycle_confirmed':r['cycle'],'observed_count':len(r['map']),'downloaded_count':sum(x['status']=='downloaded' for x in photos),'images':photos}
    m['complete']=m['cycle_confirmed'] and m['downloaded_count']==m['observed_count']==a['expected_photos']
    (d/'MANIFEST.json').write_text(json.dumps(m,ensure_ascii=False,indent=2))
    print(r['id'],m['downloaded_count'],m['complete'],flush=True)
    return m
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as ex: results=list(ex.map(save,rows))
print('Saved',len(results),'albums',sum(r['downloaded_count'] for r in results),'images',sum(r['complete'] for r in results),'complete',flush=True)
sheet=Image.new('RGB',(1600,9*275),'white'); draw=ImageDraw.Draw(sheet)
for row,m in enumerate(results):
    draw.text((10,row*275+5),m['id']+' '+m['date'],fill='black')
    for n,p in enumerate(m['images']):
        if p['status']!='downloaded': continue
        im=Image.open(p['path']).convert('RGB'); im.thumbnail((218,230))
        sheet.paste(im,(n*228+5,row*275+30));draw.text((n*228+5,row*275+260),p['id'],fill='black')
sheet.save(P/'2024_EXTRA_CONTACT.jpg',quality=92)
