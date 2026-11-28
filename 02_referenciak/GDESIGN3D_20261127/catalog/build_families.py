#!/usr/bin/env python3
"""Build a portable, offline family browser. Does not modify index.html."""
import json, html, re
from pathlib import Path
from collections import Counter
HERE=Path(__file__).resolve().parent
SRC=HERE.parent/'facebook_full'
load=lambda n:json.loads((SRC/n).read_text())
cat=json.loads((HERE/'CATALOG.json').read_text()); albums={x['id']:x for x in cat['items']}; rows=[]
def add(id,title,ids,category,status='single',note='',companions=None,year='',image_indices=None):
 ids=list(dict.fromkeys(ids));comp=list(dict.fromkeys(companions or []))
 assert all(x in albums for x in ids+comp),(id,ids,comp)
 rows.append(dict(id=id,title=title,ids=ids,category=category,status=status,note=note,companions=comp,year=str(year),image_indices=image_indices))
A=load('PROJECT_FAMILIES_2023_2025.json')
fm={x['family_id']:x for x in A['residential_base_families']};mm={x['module_id']:x for x in A['standalone_room_modules']}
for x in A['residential_base_families']:
 ids=[m['album_id'] for m in x['members']];cs=[mm[m]['source']['album_id'] for m in x['proposed_companion_module_ids']]
 st='confirmed' if x.get('original_identity_verified') else ('proposed' if len(ids)>1 else 'single')
 add(x['family_id'],x['title_hu'],ids,'base',st,x['appearance_to_preserve_hu'],cs,albums[ids[0]]['year'])
for x in A['standalone_room_modules']:
 note=x['pairing_reason_hu']+' Javasolt alapok: '+', '.join(fm[f]['title_hu'] for f in x['compatible_base_families'])+'.'
 add(x['module_id'],x['title_hu'],[x['source']['album_id']],'module','single',note,year=albums[x['source']['album_id']]['year'],image_indices=x['source_image_indices'])
for x in A['commercial_and_hospitality']:
 ids=[m['album_id'] for m in x['members']]
 add(x['family_id'],x['title_hu'],ids,'commercial','single',x['appearance_hu']+' '+x['adaptation_scope_hu'],year=albums[ids[0]]['year'])
for x in A['non_design_or_incomplete_media_records']:
 add('ARCH_'+x['id'],x['classification_hu'],[x['id']],'archive','archive',year=albums[x['id']]['year'])
B=load('PROJECT_FAMILIES_2024.json')
for x in B['families']:
 ids=x['source_ids'];k='base' if x.get('base_source_ids') else 'module'
 if x['status']=='archived_exterior_reference':k='exterior'
 if x['id']=='GD24_F23':k='module'
 cs=[];notes=[x['basis']]
 if x.get('note'):notes.append(x['note'])
 for pair in B['proposed_creative_pairings']:
  if set(pair['base_sources'])&set(ids):cs+=pair['module_sources'];notes.append('Javasolt társítás: '+pair['reason_hu'])
 st='confirmed' if x['status'].startswith('confirmed') and len(ids)>1 else 'single'
 add(x['id'],x['label'],ids,k,st,' '.join(notes),cs,2024)
for x in B['non_album_records']:
 add('ARCH_'+x['id'],albums[x['id']]['title'],[x['id']],'archive','archive','Külön archivált borítókép vagy videó-előnézet; nem teljes enteriőrsorozat.',year=2024)
C=load('PROJECT_FAMILIES_2026.json');primaries={i for g in C['groups'] for i in g['primary']};mods={}
for x in C['groups']:
 k='base';rel=x['relationship']
 if rel=='special_room_module' or x['id'] in ['G26-05','G26-12']:k='module'
 if rel=='exterior_only':k='exterior'
 if x['id']=='G26-03':k='commercial'
 add(x['id'],x['title_hu'],x['primary'],k,'single',x.get('notes_hu','')+' '+'; '.join(x.get('variants_hu',[])),x['proposed_companions'],2026)
 for i in x['proposed_companions']:
  if i not in primaries:mods.setdefault(i,[]).append(x['title_hu'])
for i,parents in mods.items():
 add('M26_'+i,albums[i]['title'],[i],'module','single','Külön forrásalbum. Javasolt társítás: '+'; '.join(parents)+'. Az eredeti közös projekt azonossága nincs igazolva.',year=2026)
covered={i for r in rows for i in r['ids']+r['companions']};all_photo={i for i,a in albums.items() if a['kind']=='album'}
assert all_photo<=covered,sorted(all_photo-covered)
assert len(all_photo)==129,len(all_photo)
e=html.escape
labels={'base':'Lakóalapok','module':'Helyiségmodulok','commercial':'Kereskedelmi és szálláshelyi eredet','exterior':'Kültéri referenciák','archive':'Külön archivált bejegyzések'}
status={'confirmed':('ok','Igazolt közös projekt'),'proposed':('maybe','Javasolt közös család'),'single':('plain','Önálló forrás / album'),'archive':('plain','Előnézet vagy egyképes bejegyzés')}
def link(i):return f'<a class="album" href="index.html#{e(i)}">{e(i)} <span>· {len(albums[i]["photos"])} kép</span></a>'
def card(r):
 a=albums[r['ids'][0]];pic=a['photos'][0].get('thumbnail') if a['photos'] else None
 photo=f'<a href="index.html#{e(a["id"])}" tabindex="-1"><img src="../{e(pic)}" alt="{e(r["title"])}" loading="lazy"></a>' if pic else ''
 cl,st=status[r['status']];idx=f'<p class="meta">Forrásképek: {", ".join(map(str,r["image_indices"]))}.</p>' if r['image_indices'] else ''
 search=' '.join([r['title'],r['note'],*r['ids'],*r['companions']]).lower()
 return f'''<article class="card" data-year="{r['year']}" data-category="{r['category']}" data-search="{e(search,quote=True)}">{photo}<div class="body"><div class="eyebrow">{r['year']} · {e(r['id'])}</div><h3>{e(r['title'])}</h3><span class="badge {cl}">{st}</span><p>{e(r['note'])}</p><div class="links">{''.join(link(i) for i in r['ids'])}</div>{idx}{'<div class="pair"><strong>Javasolt külön forrású társak</strong><div class="links">'+''.join(link(i) for i in r['companions'])+'</div><small>Összeillő kreatív változat; nem igazolt eredeti összetartozás.</small></div>' if r['companions'] else ''}</div></article>'''
counts=Counter(r['category'] for r in rows)
sections=''.join(f'<section id="{k}"><div class="section-head"><h2>{v}</h2><span>{counts[k]} csoport / modul</span></div><div class="grid">'+''.join(card(r) for r in rows if r['category']==k)+'</div></section>' for k,v in labels.items())
directory=''.join(f'<a href="index.html#{e(i)}" data-year="{albums[i]["year"]}" title="{e(albums[i]["title"],quote=True)}"><strong>{e(i)}</strong><span>{e(albums[i]["title"])}</span></a>' for i in sorted(all_photo))
nav=''.join(f'<a href="#{k}">{v}</a>' for k,v in labels.items())
page='''<!doctype html><html lang="hu"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>G.Design · Projektcsaládok</title><style>
:root{--ink:#282a26;--paper:#f4f1e9;--line:#d8d3c6;--muted:#676c61;--gold:#9a763c}*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.5 system-ui,-apple-system,sans-serif}header,main,footer{max-width:1460px;margin:auto;padding:32px}header{padding-top:54px}small,.eyebrow{font-size:12px;letter-spacing:.06em}.eyebrow{color:var(--muted)}h1{font-size:clamp(32px,5vw,62px);font-weight:500;line-height:1.08;margin:18px 0}h2{font-size:27px;font-weight:500}h3{font-size:21px;line-height:1.2;margin:10px 0 16px}a{color:inherit;text-underline-offset:3px}p{margin:14px 0}.intro{max-width:900px;color:var(--muted);font-size:18px}.stats{display:flex;flex-wrap:wrap;gap:24px;border-top:1px solid var(--line);padding:22px 0}.stats b{font-size:28px;font-weight:500}.stats span{display:block;font-size:13px;color:var(--muted)}.legend{display:flex;flex-wrap:wrap;gap:12px}.badge{display:inline-block;border:1px solid var(--line);border-radius:20px;padding:5px 10px;font-size:12px}.ok{color:#245743;background:#e1eadc;border-color:#bad0b0}.maybe,.pair{background:#f3ead6}.plain{background:#eeece5}.pair{padding:14px;margin-top:20px;border-left:3px solid #b5904b}.pair strong{font-size:13px}.pair small{display:block;color:#706547}.links{display:flex;gap:7px;flex-wrap:wrap;margin:12px 0}.album{border:1px solid var(--line);padding:5px 9px;border-radius:4px;text-decoration:none;font-size:13px;background:#fffdfa}.album:hover{border-color:var(--gold)}.album span{color:var(--muted)}nav{display:flex;gap:8px;flex-wrap:wrap;margin:20px 0}nav a{padding:8px 12px;border:1px solid var(--line);text-decoration:none;border-radius:24px;font-size:13px}.controls{display:flex;gap:12px;flex-wrap:wrap;margin-top:25px}.controls input,.controls select{font:inherit;padding:11px 14px;border:1px solid var(--line);border-radius:6px;background:#fffdfa}.controls input{min-width:240px;flex:1}.grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:24px}.card{background:#fffdfa;border:1px solid var(--line);border-radius:8px;overflow:hidden}.card img{width:100%;height:240px;object-fit:cover;display:block}.body{padding:22px}.body p{font-size:14px;color:#596052}.meta{font-size:12px!important}.section-head{display:flex;align-items:baseline;justify-content:space-between;border-top:1px solid var(--line);margin:32px 0 20px;gap:20px}.section-head span{font-size:13px;color:var(--muted)}section{scroll-margin-top:20px}#directory .directory{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}.directory a{display:flex;flex-direction:column;text-decoration:none;padding:12px;border:1px solid var(--line);border-radius:5px;background:#fffdfa}.directory strong{font-size:12px;color:var(--gold)}.directory span{font-size:13px;margin-top:3px}.note{padding:20px;background:#e9e8df;border-left:3px solid #869477}.back{font-size:14px}.empty{color:var(--muted)}footer{color:var(--muted);font-size:13px}button{cursor:pointer}[hidden]{display:none!important}@media(max-width:1000px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}#directory .directory{grid-template-columns:repeat(3,minmax(0,1fr))}}@media(max-width:640px){header,main,footer{padding:22px}.grid{grid-template-columns:1fr}#directory .directory{grid-template-columns:repeat(2,minmax(0,1fr))}.card img{height:260px}.section-head{align-items:start;flex-direction:column;gap:0}.controls input{min-width:0;width:100%}}
</style><header><a class="back" href="index.html">← Vissza az összes eredeti képhez</a><div class="eyebrow" style="margin-top:30px">G.DESIGN · 2023–2026 · A811 / A812 / A902</div><h1>Projektek és<br>összeillő helyiségek.</h1><p class="intro">Az eredeti sorozatok megőrzik saját azonosságukat. A külön fürdők, hálók és előterek mellett látható, melyik lakóalaphoz javasoljuk őket. Ez a referenciaanyag rendszerezése; a saját lakások tervei a következő lépésben készülnek.</p><div class="stats"><div><b>129</b><span>teljes forrásalbum</span></div><div><b>__BASE__</b><span>lakóalap-csoport</span></div><div><b>__MODULE__</b><span>helyiségmodul</span></div><div><b>3</b><span>saját lakás</span></div></div><div class="legend"><span class="badge ok">Igazolt közös projekt</span><span class="badge maybe">Javasolt társítás</span><span class="badge plain">Önálló forrás / album</span></div><p class="meta">Az igazolt címke konkrét képi vagy eredeti szöveges bizonyítékot jelent. A javaslat anyag- és színösszhangon alapul; nem állít közös eredetet.</p><nav>__NAV__<a href="#directory">Mind a 129 album</a></nav><div class="controls"><input id="search" type="search" placeholder="Keresés: dió, fürdő, Ződ, GD034…" aria-label="Keresés"><select id="year" aria-label="Év"><option value="">Minden év</option><option>2026</option><option>2025</option><option>2024</option><option>2023</option></select><select id="category" aria-label="Csoport"><option value="">Minden csoport</option>__OPTIONS__</select></div><p id="result" class="meta" aria-live="polite"></p></header><main>__SECTIONS__<section id="directory"><div class="section-head"><h2>Mind a 129 teljes album</h2><span>Év és forrásazonosító szerint visszakereshető</span></div><p class="meta">Az alábbi teljes jegyzék a felső csoportszűrőktől függetlenül minden albumot megőriz.</p><div class="directory">__DIRECTORY__</div></section><p class="note">A referencia anyag- és bútorvilágot ad, a saját lakás geometriája marad. A teljes öltöztetés, tárolók és rétegzett meleg fény minden adaptáció része. A képi anyagleírások nem igazolt gyártói cikkszámok; a költségek és a kivitelezhetőség külön ellenőrzést kapnak.</p><p class="meta">Részletes családtérképek: <a href="../facebook_full/PROJECT_FAMILIES_2026.json">2026</a> · <a href="../facebook_full/PROJECT_FAMILIES_2024.json">2024</a> · <a href="../facebook_full/PROJECT_FAMILIES_2023_2025.json">2023 és 2025</a></p></main><footer>G.Design eredeti referenciái · Összerendezve: 2026. november 27. · Hordozható, internet nélkül is böngészhető csomag.</footer><script>
const $=id=>document.getElementById(id);function filter(){const q=$('search').value.toLocaleLowerCase('hu').trim(),y=$('year').value,c=$('category').value;let n=0;document.querySelectorAll('article.card').forEach(a=>{let show=(!q||a.dataset.search.toLocaleLowerCase('hu').includes(q))&&(!y||a.dataset.year===y)&&(!c||a.dataset.category===c);a.hidden=!show;if(show)n++});document.querySelectorAll('main>section:not(#directory)').forEach(s=>s.hidden=!s.querySelector('article:not([hidden])'));$('result').textContent=n+' csoport vagy modul a szűrésben';}['search','year','category'].forEach(i=>$(i).addEventListener('input',filter));filter();</script></html>'''
page=page.replace('__BASE__',str(counts['base'])).replace('__MODULE__',str(counts['module'])).replace('__NAV__',nav).replace('__OPTIONS__',''.join(f'<option value="{k}">{v}</option>' for k,v in labels.items())).replace('__SECTIONS__',sections).replace('__DIRECTORY__',directory)
(HERE/'families.html').write_text(page)
refs=re.findall(r'href="index.html#(GD[\w]+)"',page)
assert set(refs)<=set(albums)
assert all_photo<=set(refs)
for thumb in re.findall(r'<img src="([^"]+)"',page):assert (HERE/html.unescape(thumb)).exists(),thumb
index=(HERE/'index.html').read_text();assert 'location.hash' in index
assert all(('"id": "'+i+'"') in index or ('"id":"'+i+'"') in index for i in set(refs))
report={'status':'PASS','complete_albums':len(all_photo),'all_complete_albums_linked':True,'unique_linked_source_records':len(set(refs)),'album_link_occurrences':len(refs),'group_counts':dict(counts),'all_thumbnail_paths_exist':True,'all_targets_exist_in_catalog_index':True,'index_html_modified':False}
(HERE/'FAMILIES_CHECK.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
