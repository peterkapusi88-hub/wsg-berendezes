from pathlib import Path
import json,re,urllib.request,html,hashlib,concurrent.futures
import openpyxl
P=Path(__file__).resolve().parents[1];O=P/'CP3';dest=O/'evidence/product_photos';dest.mkdir(exist_ok=True)
w=openpyxl.load_workbook(P/'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx',data_only=True);rows=[]
for row in w['Elemregiszter'].iter_rows(min_row=2,values_only=True):
 if isinstance(row[10],str) and row[10].startswith('https://www.ikea.com/hu/hu/p/'):
  rows.append(dict(element=row[2],sku=row[9],url=row[10]))
def get(r):
 try:
  req=urllib.request.Request(r['url'],headers={'User-Agent':'Mozilla/5.0'});h=urllib.request.urlopen(req,timeout=25).read().decode('utf-8')
  tags=re.findall(r'<meta\b[^>]*>',h,re.I);tag=next(t for t in tags if 'og:image' in t);url=html.unescape(re.search(r'content=[\"\x27]([^\"\x27]+)',tag).group(1))
  if not url.startswith('https://www.ikea.com/') and not url.startswith('https://images.ikea.com/'):raise ValueError('Unexpected image host')
  data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'}),timeout=25).read();f=dest/(r['element']+'.jpg');f.write_bytes(data)
  return dict(**r,image_url=url,file=str(f.relative_to(P)),sha256=hashlib.sha256(data).hexdigest(),status='Exact product-page og:image retrieved; visual variant verification still required',date='2026-10-27')
 except Exception as e:return dict(**r,status='asset retrieval failed',detail=str(e))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(get,rows))
(O/'evidence/product_photo_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2));print(json.dumps(dict(requested=len(out),retrieved=sum('file' in r for r in out)),ensure_ascii=False))
