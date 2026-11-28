from pathlib import Path
import json, html, hashlib
from PIL import Image, ImageOps

ROOT=Path(__file__).resolve().parents[1]
FB=ROOT/'facebook_full'
classes={e['id']:e for e in json.loads((FB/'CLASSIFICATION_2026.json').read_text())['entries']}
room_names={'living':'nappali','kitchen':'konyha','dining':'étkező','bedroom':'háló','master':'háló','bathroom':'fürdő','bath':'fürdő','hall':'folyosó','entry':'előtér','office':'dolgozó','study':'dolgozó','wardrobe':'gardrób','kids':'gyerekszoba','kidsroom':'gyerekszoba','library':'könyvtár','terrace':'terasz','wellness':'wellness','restaurant':'étterem','storage':'tároló','laundry':'mosókonyha'}
room_names.update({'bed':'háló','child':'gyerekszoba','bar':'bár','cafe':'kávézó','clinic':'rendelő','commercial':'üzleti tér','corridor':'folyosó','courtyard':'belső udvar','exterior':'kültér','garage':'garázs','gym':'edzőterem','lounge':'társalgó','media':'TV-fal','meeting':'tárgyaló','mixed':'több helyiség','play':'játszótér','reception':'recepció','shower':'zuhany','stair':'lépcső','vanity':'fésülködő','wc':'WC','gaming':'játék / dolgozó'})
items=[]
errors=[]
for mf in sorted(FB.glob('GD*/MANIFEST.json')):
 d=json.loads(mf.read_text()); ident=d.get('id',mf.parent.name)
 c=d.get('classification',classes.get(ident,{}))
 photos=d.get('photos',d.get('images',[]))
 title=c.get('title_hu') or c.get('visual_description_hu') or c.get('character_hu') or ident
 rooms=c.get('rooms',c.get('rooms_hu',[]))
 if isinstance(rooms,str):rooms=[r.strip() for r in rooms.split(',')]
 rooms=[room_names.get(r,r) for r in rooms]
 if not c.get('title_hu') and len(title)>100:title=', '.join(rooms).capitalize()+' · '+title.split(',')[0]
 category=c.get('category',c.get('category_visual','lakóenteriőr'))
 category={'lakóenterior':'lakóenteriőr','residential':'lakóenteriőr','video preview':'videó-előnézet','company_news':'céges hír','external_youtube_preview':'YouTube-előnézet','cover_collage':'borítókép','speciális-enterior':'speciális enteriőr','kültér-nem-enterior':'kültéri referencia','lakóenterior-modul':'lakóenteriőr-modul'}.get(category,category)
 if any(r in ['edzőterem','rendelő','üzleti tér','kávézó'] for r in rooms):category='kereskedelmi enteriőr'
 status=d.get('status','COMPLETE' if (d.get('complete') or d.get('cycle_verified')) else 'ELLENŐRZENDŐ')
 kind='single' if status.startswith('SINGLE') else 'video' if ('VIDEO' in status or 'YOUTUBE' in status) else 'album' if d.get('album_id') else 'info'
 if ident=='GD050':continue
 normalized=[]
 for n,p in enumerate(photos):
  path=p.get('path') or p.get('file')
  if not path:continue
  fp=Path(path)
  if not fp.is_absolute():
   fp=(ROOT/fp) if str(fp).startswith('facebook_full/') else mf.parent/fp
  if not fp.exists():errors.append(str(fp));continue
  size=p.get('pixel_size') or [p.get('width'),p.get('height')]
  with Image.open(fp) as im:
   im.verify()
  with Image.open(fp) as im:
   size=list(im.size)
   thumb=fp
  normalized.append({'path':str(fp.relative_to(ROOT)),'thumbnail':str(thumb.relative_to(ROOT)),'width':size[0],'height':size[1],'sha256':p.get('sha256'),'photo_url':p.get('photo_url') or p.get('source_url'),'room':p.get('room_type_visual')})
 date=d.get('date',d.get('post_date',''))
 source=d.get('source_url') or (photos[0].get('photo_url') if photos else None)
 if source and 'facebook.com/' in source and '/photo/' not in source and d.get('album_id') and photos and photos[0].get('photo_url'):source=photos[0]['photo_url']
 items.append({'id':ident,'date':date,'year':date[:4],'title':title,'description':c.get('visual_notes',c.get('character_hu',c.get('visual_description_hu',''))),'rooms':rooms,'category':category,'kind':kind,'status':status,'source_url':source,'official_match':c.get('official_portfolio_visual_match'),'photos':normalized,'adaptation':c.get('adaptation_hu',''),'expected':d.get('expected_photos'),'actual':len(normalized)})

data={'source':'https://www.facebook.com/gdesign3d','range':['2023-01-01','2026-11-27'],'generated':'2026-11-27','items':items,'photo_album_count':sum(i['kind']=='album' for i in items),'album_images':sum(i['actual'] for i in items if i['kind']=='album'),'missing_files':errors,'notes':['A képcsoportok az eredeti bejegyzéseket követik. Különböző posztok közös projektje csak igazolt vagy külön jelölt vizuális egyezés alapján társítható.','Az anyagleírások látvány szerinti megfigyelések, nem ellenőrzött gyártói termékazonosítók.','A videó-előnézet önállóan nem a teljes videó mentése.','A hivatalos honlap 228 képe külön kiegészítő gyűjtemény; lehet átfedés a Facebookkal.']}
(ROOT/'catalog'/'CATALOG.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
payload=json.dumps(data,ensure_ascii=False).replace('</','<\/')
page='''<!doctype html><html lang="hu"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>G.Design · 2023–2026 referenciaarchívum</title>
<style>:root{color-scheme:dark}*{box-sizing:border-box}body{margin:0;background:#171a19;color:#f3f0e8;font:16px/1.5 system-ui,sans-serif}header,main{max-width:1500px;margin:auto;padding:32px}header{padding-top:52px}small,.muted{color:#babcb4}h1{font-size:clamp(30px,5vw,58px);line-height:1.08;max-width:980px;font-weight:550;letter-spacing:-2px}a{color:#d1ddbd}button,input,select{font:inherit;border:1px solid #51564c;border-radius:8px;background:#252a26;color:#fff;padding:10px 14px}button{cursor:pointer}nav{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0}input{min-width:260px;flex:1}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:24px}.card{background:#232824;border:1px solid #3a4238;border-radius:14px;overflow:hidden}.cover{width:100%;height:230px;object-fit:cover;display:block;cursor:pointer}.body{padding:18px}h2{font-size:18px;line-height:1.35;margin:9px 0}.tags{font-size:13px;color:#cfdfbd}.badge{display:inline-block;background:#384034;padding:3px 8px;border-radius:6px;font-size:12px}.card p{font-size:14px;color:#c9c9c0}.sources{display:flex;gap:16px;font-size:13px}dialog{width:min(1400px,95vw);max-height:94vh;background:#1b201c;color:#eee;border:1px solid #68715e;border-radius:14px;padding:28px}dialog::backdrop{background:#000d}.close{float:right}.photos{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:14px;margin-top:22px}.photos img{width:100%;height:280px;object-fit:contain;background:#121512}.photos a{font-size:12px}.note{padding:18px;border-left:3px solid #a8ba91;background:#242a23}footer{padding:32px;color:#aab2a2}#count{font-variant-numeric:tabular-nums}</style>
<header><small>G.DESIGN · EREDETI REFERENCIÁK · 2023. JANUÁR 1. – 2026. NOVEMBER 27.</small><h1>Négy év enteriőrjei,<br>projektenként megőrizve.</h1><p id="intro"></p><p class="muted">Lakóterek, önálló fürdők és hálók, valamint külön jelölt üzleti és kültéri referenciák.</p><p><a href="families.html">Projektcsaládok és társítható helyiségek →</a></p><nav><input id="search" placeholder="Keresés: dió, fürdő, GD027…" aria-label="Keresés"><select id="year" aria-label="Év"><option value="">Minden év</option><option>2026</option><option>2025</option><option>2024</option><option>2023</option></select><select id="room" aria-label="Helyiség"><option value="">Minden helyiség</option></select><select id="kind" aria-label="Forrástípus"><option value="">Minden forrástípus</option><option value="album">Teljes képalbum</option><option value="single">Egyképes poszt</option><option value="video">Videó-előnézet</option></select></nav><div id="count"></div></header><main><div class="grid" id="grid"></div><p class="note">A geometria később a saját 811-es, 812-es és 902-es lakásból származik. A referenciák anyag- és bútorvilágot adnak; a nagy belmagasság, lépcső, nyílászáró vagy mennyezeti fényvályú nem másolható át automatikusan.</p><p><a href="../official/00_PROJECT_INDEX.html">A hivatalos honlap 11 projektje / 228 képe</a> · <a href="CATALOG.json">Részletes forrásjegyzék</a></p></main><dialog id="detail"><button class="close" onclick="document.getElementById('detail').close()">Bezárás ×</button><div id="detailbody"></div></dialog><footer>A leíró címek vizuális munkacímek. Az eredeti szerző: G.Design. A videó-előnézetek nem helyettesítik a teljes videókat.</footer>
<script>const data=PAYLOAD;const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));const $=id=>document.getElementById(id);$('intro').textContent=`${data.photo_album_count} teljes képalbum · ${data.album_images} albumfotó · eredeti forráslinkek és fájlméretek`;const rs=[...new Set(data.items.flatMap(x=>x.rooms))].sort((a,b)=>a.localeCompare(b,'hu'));rs.forEach(r=>$('room').insertAdjacentHTML('beforeend',`<option>${esc(r)}</option>`));function render(){const q=$('search').value.toLocaleLowerCase('hu');const items=data.items.filter(x=>(!$('year').value||x.year===$('year').value)&&(!$('room').value||x.rooms.includes($('room').value))&&(!$('kind').value||x.kind===$('kind').value)&&JSON.stringify(x).toLocaleLowerCase('hu').includes(q));$('count').textContent=`${items.length} képcsoport a szűrésben`;$('grid').innerHTML=items.map(x=>`<article class="card">${x.photos[0]?`<img class="cover" src="../${esc(x.photos[0].thumbnail)}" alt="${esc(x.title)}" loading="lazy" onclick="show('${x.id}')">`:''}<div class="body"><small>${x.id} · ${x.date}</small> <span class="badge">${x.actual} ${x.kind==='video'?'előnézet':'kép'}</span><h2>${esc(x.title)}</h2><div class="tags">${esc(x.rooms.join(' · '))}</div><p>${esc(x.category)}${x.official_match?' · Honlap: '+esc(x.official_match):''}</p><div class="sources"><button onclick="show('${x.id}')">Teljes képsor</button>${x.source_url?`<a target="_blank" rel="noopener" href="${esc(x.source_url)}">Eredeti forrás ↗</a>`:''}</div></div></article>`).join('')}function show(id){let x=data.items.find(x=>x.id===id);$('detailbody').innerHTML=`<small>${x.id} · ${x.date}</small><h2>${esc(x.title)}</h2><p>${esc(x.description)}</p><p>${esc(x.adaptation)}</p>${x.kind==='video'?'<p class="note">Csak az elérhető előnézet mentése. A teljes videófájl nincs ebben a csomagban.</p>':''}<div class="photos">${x.photos.map(p=>`<div><a href="../${esc(p.path)}" target="_blank"><img loading="lazy" src="../${esc(p.path)}" alt="${esc(x.id)} referencia">${p.width} × ${p.height} px · Eredeti fájl megnyitása</a>${p.photo_url?`<br><a target="_blank" rel="noopener" href="${esc(p.photo_url)}">Kép forrása ↗</a>`:''}</div>`).join('')}</div>`;$('detail').showModal()}['search','year','room','kind'].forEach(id=>$(id).addEventListener('input',render));render();</script></html>'''.replace('PAYLOAD',payload)
page=page.replace('render();</script>','render();if(location.hash&&data.items.some(x=>x.id===location.hash.slice(1)))show(location.hash.slice(1));</script>')
(ROOT/'catalog'/'index.html').write_text(page)
print(json.dumps({'albums':data['photo_album_count'],'album_images':data['album_images'],'groups':len(items),'missing_files':errors},ensure_ascii=False))
