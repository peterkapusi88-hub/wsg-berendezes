import csv, hashlib, json, pathlib, shutil, sys, urllib.request
from concurrent.futures import ThreadPoolExecutor
from PIL import Image, ImageOps, ImageDraw

ROOT = pathlib.Path(__file__).resolve().parent
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def process(album_id, bundle_path):
    index = {r['id']: r for r in csv.DictReader((ROOT/'ALBUM_INDEX.tsv').open(), delimiter='\t')}
    meta = index[album_id]
    target = ROOT/album_id
    target.mkdir(exist_ok=True)
    bundle_path = pathlib.Path(bundle_path)
    bundle = json.loads(bundle_path.read_text())
    shutil.copy2(bundle_path, target/('BUNDLE_'+bundle_path.parent.name+'.json'))
    found = {}
    for item in bundle.get('failures', []) + bundle.get('assets', []):
        found[item['name']] = item
    def save(item):
        dest = target/item['name']
        result = {'name':item['name'], 'source_url':item['url'], 'path':str(dest.relative_to(ROOT.parent)), 'retrieved':'2026-11-27'}
        try:
            if not dest.exists():
                if item.get('path') and pathlib.Path(item['path']).is_file():
                    shutil.copy2(item['path'],dest)
                else:
                    req = urllib.request.Request(item['url'], headers={'User-Agent':'Mozilla/5.0'})
                    with urllib.request.urlopen(req,timeout=40) as response:
                        data=response.read()
                    stage=dest.with_suffix(dest.suffix+'.part');stage.write_bytes(data)
                    with Image.open(stage) as im: im.verify()
                    stage.replace(dest)
            with Image.open(dest) as im:
                im.load();result['pixel_size']=list(im.size);result['format']=im.format
            result.update(status='VERIFIED',bytes=dest.stat().st_size,sha256=digest(dest))
        except Exception as exc:
            result.update(status='DOWNLOAD_FAILED',error=str(exc))
        return result
    with ThreadPoolExecutor(max_workers=4) as pool:
        items=list(pool.map(save,found.values()))
    verified=[i for i in items if i['status']=='VERIFIED']
    expected=int(meta['expected_photos'])
    result={'id':album_id,'post_date':meta['date'],'source_url':'https://www.facebook.com/photo/?fbid='+meta['first_photo_id']+'&set=pcb.'+meta['album_id'], 'album_id':meta['album_id'],'expected_photos':expected,'observed_full_carousel':'Parent browser workflow verified full cycle','downloaded':len(verified),'status':'COMPLETE' if len(verified)==expected else 'INCOMPLETE','retrieved':'2026-11-27','images':items}
    (target/'MANIFEST.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    columns=min(5,len(verified))
    if columns:
        rows=(len(verified)+columns-1)//columns;sheet=Image.new('RGB',(columns*300,rows*290),'#eee9df');draw=ImageDraw.Draw(sheet)
        for i,item in enumerate(verified):
            with Image.open(ROOT.parent/item['path']) as im: thumb=ImageOps.contain(im.convert('RGB'),(294,255))
            x=(i%columns)*300;y=(i//columns)*290;sheet.paste(thumb,(x+(300-thumb.width)//2,y+27));draw.text((x+5,y+7),album_id+' '+str(i+1),fill='black')
        sheet.save(target/'CONTACT.jpg',quality=85)
    return {'id':album_id,'expected':expected,'downloaded':len(verified),'status':result['status'],'errors':[x for x in items if x['status']!='VERIFIED']}

if __name__=='__main__':
    print(json.dumps(process(sys.argv[1],sys.argv[2]),ensure_ascii=False))
