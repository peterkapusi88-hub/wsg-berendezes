import json, pathlib, os, html, hashlib

ROOT = pathlib.Path(__file__).resolve().parent
WS = ROOT.parents[1]
ARCHIVE = WS / '02_referenciak/GDESIGN3D_20261127'
manifest = json.loads((ROOT / 'GENERATION_MANIFEST.json').read_text())
audit = json.loads((ROOT / 'sources/ORIGINAL_MODULE_CAMERA_COUNT_AUDIT.json').read_text())

def rel(path):
    return pathlib.Path(os.path.relpath(path, ROOT)).as_posix()

def img(path, label):
    u = html.escape(rel(path), quote=True)
    return f'<a href="{u}" target="_blank"><img loading="lazy" src="{u}" alt="{html.escape(label)}"><span>{html.escape(label)}</span></a>'

source_index = {}
for folder in (ARCHIVE / 'facebook_full').glob('GD*'):
    f = folder / 'MANIFEST.json'
    if not f.exists(): continue
    d = json.loads(f.read_text())
    source_index[folder.name] = {'album_id': folder.name, 'source_url': d.get('source_url'), 'images': [str(folder / p['file']) for p in d.get('photos', [])]}

rooms = []
for apt in ['A902', 'A812', 'A811']:
    if apt == 'A902':
        data = [('living_kitchen_dining','Nappali / konyha / étkező',['Cam_02','Cam_12','Cam_03','Cam_02_DAY'],False),('05.1','Külön szoba',['Cam_04','Cam_11c'],True),('06.2','Fürdő',['Cam_10'],False)]
    else:
        raw = json.loads((WS / f'05_promptok/S18_LAKE_FOREST_PLUS_20261123/{apt}/PROMPT_MANIFEST.json').read_text())
        grouped = {}
        for r in raw:
            if r['variant'] != 'A': continue
            room = r['room'].split(' · ')[0]
            grouped.setdefault(room, []).append(r['camera'])
        data = [(r,r,c,r.startswith('05.')) for r,c in grouped.items()]
    for physical,name,cameras,flex in data:
        rooms.append({'apartment':apt,'physical_room':physical,'name':name,'cameras':cameras,'function_options':['fő háló','gyerekszoba','dolgozó','gardróbszoba'] if flex else [name], 'status':'OWNER_REQUESTED_ALTERNATIVES_FIT_PENDING' if flex else 'FIXED_FUNCTION','rule':'Alternatives replace each other; do not create new physical rooms. Camera remains fixed; furniture function may change.'})
(ROOT/'ROOM_FUNCTION_CAMERA_MAP.json').write_text(json.dumps(rooms,ensure_ascii=False,indent=2))

for j in manifest['jobs']:
    req = ROOT/'prompts'/f"{j['id']}.request.json"
    if not req.exists(): continue
    args = json.loads(req.read_text())
    j['input_integrity'] = [{'path':p,'sha256':hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()} for p in args['referenced_image_paths']]
    j['prompt_sha256'] = hashlib.sha256(pathlib.Path(j['prompt']).read_bytes()).hexdigest()
    originals=[]
    for p in j['source_images']:
        pp=pathlib.Path(p)
        if pp.parent.name=='inputs' and pp.name.startswith('GD'):
            album,filename=pp.name.split('_',1)
            originals.append(str(ARCHIVE/'facebook_full'/album/filename))
        else: originals.append(p)
    j['original_source_images']=originals
    j['source_album_ids']=sorted(set(pathlib.Path(p).parent.name for p in originals))
    (ROOT/'qa'/f"{j['id']}.json").write_text(json.dumps(j,ensure_ascii=False,indent=2))
(ROOT/'GENERATION_MANIFEST.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))

pairs=[]
for pair in manifest.get('lighting_pairs',[]):
    a=next(j for j in manifest['jobs'] if j['id']==pair['day'])
    b=next(j for j in manifest['jobs'] if j['id']==pair['night'])
    pairs.append('<article><h3>'+pair['physical_camera']+' · nappal / este</h3><div class=pair>'+img(a['output'],'Nappali fény')+img(b['output'],'Esti fény')+'</div></article>')
cards=[]
for j in manifest['jobs']:
    if not j.get('output'): continue
    refs=''.join(img(p, pathlib.Path(p).parent.name+' · '+pathlib.Path(p).name.split('_')[0]) for p in j['original_source_images'])
    notes={'Cam_02':'A médiafal anyagkiosztása saját adaptáció. A forrás szabadon álló TV-je és belső fája nem került át.','Cam_12':'Az étkező és konyha az eredeti helyén maradt. A levélmotívumú műalkotás saját társítás.','Cam_03':'A forrás szigete helyett a meglévő konyhasorok kapták a zöld követ. A dekoráció egységesítése még szükséges.','Cam_04':'A meglévő szekrény kapott füstüvegfrontot. A kő és a növényi dekoráció kivitelezése feltételes.','Cam_11c':'Ugyanazon háló fordított nézete; a valódi ablakosztás, kilátás és meglévő tárolóhely maradt.','Cam_10':'A forrás tálmosdója süllyesztett mosdóra módosult. A meglévő burkolat maradt; a lámpa bekötése ellenőrizendő.','Cam_02_DAY':'A nappali világos változata, ugyanazzal a berendezéssel.'}.get(j['camera_id'],'')
    cards.append(f'<article class="job" data-apt="{j["apartment"]}" data-function="{j["function"]}" data-light="{j.get("lighting", "NIGHT")}"><header><span class="eyebrow">Ződ · GD111 + GD109 · igazolt forráscsalád</span><h2>{j["apartment"]} / {j["function"]}</h2><p>{j["camera_id"]} · {"nappali fény" if j.get("lighting")=="DAY" else "esti fény"} · fizikai helyiség: {j["physical_room"]} · jóváhagyásra vár</p></header><div class="pair"><section><h3>Ezekből a mintákból</h3><div class="refs">{refs}</div></section><section><h3>Ez lett a saját lakásban</h3>{img(j["output"],j["id"])}</section></div><p class="note">{notes}</p><details><summary>Korábbi lakásnézet és ellenőrzés</summary>{img(j["geometry_input"],"Korábbi kameraalap – nem mérettanúsítás")}<p>Vizuálisan ellenőrzött koncepció. Pontos méretek, termékek, elektromos megoldások és árak még nem igazoltak. A textil- és kőminták apró eltérései véglegesítés előtt egységesítendők.</p><a href="{rel(j["prompt"])}">Teljes képgenerálási leírás</a></details></article>')

families=[]
for b in audit['base_records']:
    ids=b['source_album_ids']; companions=b.get('candidate_module_source_ids',[])
    def albums(ids):
        result=[]
        for aid in ids:
            x=source_index.get(aid,{}); pictures=x.get('images',[])
            if pictures: result.append(img(pictures[0],aid))
        return ''.join(result)
    families.append(f'<details class="family"><summary>{html.escape(b["title_hu"])} · {b["id"]}</summary><p>Alapforrások: {", ".join(ids)} · eredeti kapcsolat: {b["source_relationship"]}</p><div class="albumstrip">{albums(ids)}</div><h4>A korábban kijelölt forrástársak</h4><p>{", ".join(companions) or "Nincs külön javasolt társforrás; a család saját helyiségképei használhatók."}</p><div class="albumstrip">{albums(companions)}</div><p>A társkijelölés nem jelenti automatikusan, hogy azonos eredeti projekt. Az eredeti társítási leírások és valamennyi albumfotó a teljes katalógusban megmaradnak.</p></details>')

table=''.join('<tr><td>'+r['apartment']+'</td><td>'+r['physical_room']+'</td><td>'+', '.join(r['function_options'])+'</td><td>'+', '.join(r['cameras'])+'</td></tr>' for r in rooms)
page='''<!doctype html><html lang="hu"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>G.Design → Péter lakásai · Forrás és adaptáció</title><style>
*{box-sizing:border-box}body{margin:0;background:#f3f1eb;color:#252820;font:16px/1.5 system-ui,sans-serif}main{max-width:1500px;margin:auto;padding:36px}h1{font-size:clamp(28px,4vw,52px);line-height:1.1;max-width:900px}h2{font-size:27px;margin:8px 0}h3{font-size:15px;text-transform:uppercase;letter-spacing:.08em}a{color:inherit}nav{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0}nav a,button{padding:10px 16px;border:1px solid #b3b7a5;border-radius:24px;background:white;color:#252820;cursor:pointer}article{background:white;border-radius:16px;padding:26px;margin:28px 0}.eyebrow{color:#697253;font-size:13px;text-transform:uppercase;letter-spacing:.09em}.pair{display:grid;grid-template-columns:1fr 1.5fr;gap:24px}.pair a,.albumstrip a,details>a{display:block;text-decoration:none}img{width:100%;display:block;border-radius:8px}.refs{display:grid;grid-template-columns:repeat(2,1fr);gap:12px}.refs a:first-child{grid-column:1/-1}.refs img{max-height:370px;object-fit:contain;background:#ecebe6}a span{font-size:12px;display:block;margin:6px 0;overflow-wrap:anywhere}.note{background:#f0f1ea;padding:15px;border-left:3px solid #677650}summary{cursor:pointer;font-weight:600;padding:14px 0}details>img,details>a{max-width:750px}.albumstrip{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,210px));gap:14px}.albumstrip img{aspect-ratio:1;object-fit:cover}table{border-collapse:collapse;width:100%;font-size:13px}td,th{text-align:left;border-bottom:1px solid #ccc;padding:12px}.family{border-bottom:1px solid #bfc4b6;padding:8px}.status{padding:16px;background:#e4e8db;border-radius:12px}.filters{display:flex;flex-wrap:wrap;gap:9px}.filters .active{background:#3d4b31;color:white}section#sources{margin-top:70px}.tablewrap{overflow:auto}@media(max-width:800px){main{padding:16px}.pair{grid-template-columns:1fr}article{padding:16px}.refs{grid-template-columns:repeat(3,1fr)}.refs a:first-child{grid-column:auto}h2{font-size:22px}}
</style><main><div class="eyebrow">WSG Stíluslabor · G.Design adaptációk</div><h1>Ugyanaz a karakter.<br>A saját lakásokban.</h1><p>Az eredeti tervek, a megőrzött forrástársak és a belőlük készülő lakásváltozatok együtt, visszakövethetően.</p><div class="status">Első munkacsomag: A902 · Ződ · 11/11 nézet elkészült, köztük öt nappali–esti pár. Tulajdonosi jóváhagyásra vár. A812, A811, a további stílusok és a funkcióalternatívák még hátravannak.</div><nav><a href="#adaptations">Forrás → saját lakás</a><a href="#sources">39 alapcsalád és forrástársak</a><a href="#rooms">Szoba / funkció / kamera</a><a href="../../02_referenciak/GDESIGN3D_20261127/catalog/families.html">Teljes csoportosított referenciaarchívum</a></nav><section id="adaptations"><h2>Forrás → saját lakás</h2><div class="filters"><button class="active" data-filter="">Összes elkészült nézet</button><button data-filter="nappali">Nappali</button><button data-filter="konyha">Konyha / étkező</button><button data-filter="háló">Háló / gardrób</button><button data-filter="fürdő">Fürdő</button><select id="light" aria-label="Fényváltozat"><option value="">Nappali és esti</option><option value="DAY">Nappali fény</option><option value="NIGHT">Esti fény</option></select></div>'''+''.join(cards)+'''</section><section id="lighting"><h2>Azonos nézet, két fényhelyzet</h2>'''+''.join(pairs)+'''</section><section id="sources"><h2>Megőrzött forráscsaládok és forrástársak</h2><p>A másik chatben összeállított csoportosítás változatlanul megmaradt. A társképek külön eredetét is őrizzük; egy anyagban illeszkedő párosítás nem válik igazolt projektazonossággá.</p><nav><a href="sources/PROJECT_FAMILIES_2023_2025.json">2023 + 2025 társításai</a><a href="sources/PROJECT_FAMILIES_2024.json">2024 társításai</a><a href="sources/PROJECT_FAMILIES_2026.json">2026 társításai</a><a href="../../02_referenciak/GDESIGN3D_20261127/catalog/index.html">Összes eredeti album és kép</a></nav>'''+''.join(families)+'''</section><section id="rooms"><h2>Meglévő szoba → választható funkció → kamera</h2><p>A száraz szobák funkcióváltozatai egymást helyettesítik. A902 egyetlen külön szobája is többféleképpen berendezhető, új helyiség létrehozása nélkül. Az alkalmasság helyiségenként ellenőrizendő; a vizes helyiségek és közlekedők funkciója kötött.</p><div class="tablewrap"><table><thead><tr><th>Lakás</th><th>Fizikai helyiség</th><th>Funkció / alternatívák</th><th>Rögzített kamerák</th></tr></thead><tbody>'''+table+'''</tbody></table></div></section><p>Koncepciók, nem kiviteli tervek. A korábbi geometria, mennyezeti korlátok és költségkeretek maradnak érvényben. A korábbi 1822-es bruttó képszám a kibővített funkciók miatt már nem végleges.</p></main><script>let chosen='';function filter(){const light=document.querySelector('#light').value;document.querySelectorAll('.job').forEach(x=>x.hidden=(!!chosen&&!x.dataset.function.includes(chosen))||(!!light&&x.dataset.light!==light));}document.querySelectorAll('[data-filter]').forEach(b=>b.onclick=()=>{chosen=b.dataset.filter;document.querySelectorAll('[data-filter]').forEach(x=>x.classList.toggle('active',x===b));filter();});document.querySelector('#light').onchange=filter;</script></html>'''
(ROOT/'00_FORRAS_ES_ADAPTACIO.html').write_text(page)
print(json.dumps({'review':str(ROOT/'00_FORRAS_ES_ADAPTACIO.html'),'images':len(cards),'source_families':len(families),'physical_room_records':len(rooms)},ensure_ascii=False))
