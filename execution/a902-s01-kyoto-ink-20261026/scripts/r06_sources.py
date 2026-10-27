from pathlib import Path
import urllib.request,json,re,html,hashlib,time
P=Path(__file__).resolve().parents[1];O=P/'R06'
urls={
'lennon':'https://www.westwing.hu/lennon-modularis-sarokkanape-hu-21wes12329.html?simple=DEQ21WES12329-168260',
'toni':'https://www.westwing.hu/toni-ovalis-alaku-fa-etkezoasztal-200-x-90-cm-hu-19wes60483.html?simple=DEQ19WES60483-225182',
'eamy':'https://www.dizajnove.sk/kreslo-eamy-svetlosiva-senilova-a-jasenova-dyha-s-prirodnou-povrchovou-upravou-a-cierny-kov/',
'somar':'https://www.dizajnove.sk/somar-75-visiaca-lampa/',
'rondo':'https://www.egloshop.hu/85264-eglo-rondo-asztali-lampa',
'worktop':'https://www.okftfaaruhaz.hu/ML-EGGER-F243-ST76-4100x600x38mm-munkalap',
'mattress':'https://www.ikea.com/hu/hu/p/vagstranda-zsakrugos-matrac-kemeny-vilagoskek-00450757/'
}
out=[]
for k,u in urls.items():
 rec={'id':k,'url':u,'checked':'2026-10-27','images':[]}
 try:
  f=O/'sources'/(k+'.html')
  if f.exists():s=f.read_text()
  else:
   with urllib.request.urlopen(u,timeout=30) as r:s=r.read().decode()
   f.write_text(s)
  rec['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
  js=[]
  for x in re.findall(r'<script[^>]*type=[\"\']application/ld\+json[\"\'][^>]*>(.*?)</script>',s,re.S):
   try:js.append(json.loads(x))
   except:pass
  (O/'sources'/(k+'_structured.json')).write_text(json.dumps(js,ensure_ascii=False,indent=2))
  ims=[]
  if k in ('lennon','toni'):
   sku='168260' if k=='lennon' else '225182'
   ims=list(dict.fromkeys(html.unescape(x).split('&')[0] for x in re.findall(r'https://cdn.shopify.com[^\s\"<>]+',s) if sku in x and '.jpg' in x))[:4]
  else:
   for j in js:
    if isinstance(j,dict):
     im=j.get('image',[])
     if isinstance(im,str):im=[im]
     if isinstance(im,list):ims +=[a for a in im if isinstance(a,str) and a.startswith('https:')]
   if not ims:ims=[html.unescape(x) for x in re.findall(r'<meta[^>]+property="og:image"[^>]+content="([^"]+)"',s)]
  for i,im in enumerate(ims[:3]):
   try:
    with urllib.request.urlopen(im,timeout=25) as r:b=r.read()
    dest=O/'products'/f'{k}_{i+1}.jpg';dest.write_bytes(b);rec['images'].append({'path':str(dest.relative_to(P)),'url':im,'sha256':hashlib.sha256(b).hexdigest()})
   except Exception as e:rec.setdefault('image_errors',[]).append(str(e))
  rec['status']='downloaded public product page; stock is not delivery confirmation'
 except Exception as e:rec['status']=str(e)
 out.append(rec);print(k,rec['status'],len(rec['images']),flush=True)
(O/'sources/source_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
