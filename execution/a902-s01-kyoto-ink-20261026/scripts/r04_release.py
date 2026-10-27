from r04_drawing_book import *
import csv,zipfile,shutil
# The existing live workbook is preserved byte-for-byte; this is an unselected design scenario.
wb=P/'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx'
base=json.loads((CP/'data/cost_snapshot_CP3.json').read_text())
rows=[
 ['WN belső', 'KI-050',-40000,-40000,-40000,'5 polc×6500 + 1 fix rúd×7500 elmarad. A polckapacitás csökkenése külön döntés.'],
 ['WN szélesebb fiókok', 'KI-050',60000,20000,120000,'8 fiók×7500 Ft szélességi/vasalati felár-előirányzat. Nem beszállítói ár.'],
 ['WN teljes magasságú front', 'KI-051',120000,40000,240000,'6 magas front merevítése, pántolása és mintázása: 6×20000 Ft többletkeret. A régi 250000 Ft csomag fölötti javaslat.'],
 ['WN belső lámpa', 'KI-CP3-L01',-20450,-20450,-20450,'12×5490 helyett 7×6490 Ft. A táp/kábel csomagot nem vonjuk le igazolás nélkül.'],
 ['WN lámpaszerelés','KI-119',-7500,-7500,0,'5-tel kevesebb lámpa×1500 Ft előirányzati munkadíj; új érzékelési próba módosíthatja.'],
 ['Médiafal új felület/front', 'KI-030 / KI-031',300000,50000,550000,'Ideiglenes különbözeti keret: 60000 frontmerevítés + 160000 felületi többlet + 80000 grafikai/minta többlet. Az eredeti 450000+260000 Ft nem kerül újra hozzáadásra. Pontos műszaki árbontás nélkül nem bizonyított felár.'],
 ['Mosdó oldalankénti osztás', 'KI-092',20000,0,60000,'Két fiók marad; 20000 Ft egyszeri új osztó/szifon/vasalat illesztési felár-előirányzat.'],
 ['Biciklitartó és rögzítés','R04-BIKE',70000,35000,120000,'45000 Ft tartókeret + 25000 Ft falrögzítés/munkadíj becslés. Nincs kiválasztott SKU.'],
 ['Több tárolódoboz','KI-CP3-S04',36000,27000,54000,'21 tervezett doboz a korábbi 12 helyett: 9×4000 Ft különbözet. 3000–6000 Ft/db érzékenység; típus még nincs.']]
expected=base['main']+sum(x[2] for x in rows);low=base['low']+sum(x[3] for x in rows);high=base['high']+sum(x[4] for x in rows)
cost={'status':'UNSELECTED_R04_PROPOSAL_ESTIMATE','date':'2026-10-27','baseline':base,'delta_rows':rows,'expected':expected,'low':low,'high':high,'budget':18000000,'reserve':2000000,'reserve_used':0,'workbook_sha256_preserved':hashlib.sha256(wb.read_bytes()).hexdigest(),'limitations':'A feltételes felárak nem igazolt árak; az eredeti becslések műszaki tartalmát ajánlatban egyeztetni kell. A teljes R04 változat nincs az élő Excel főösszegébe választva.'}
(O/'data/R04_koltsegforgatokonyv.json').write_text(json.dumps(cost,ensure_ascii=False,indent=2))
d,g=sheet('R04 / a tárolási és külső változat költsége','Külön, még ki nem választott forgatókönyv. Az élő Excel kézi módosításait és főösszegét megőriztük.','Ft bruttó / becslés','C01')
txt(g,14,251,f"CP3: {base['main']:,.0f} Ft  →  R04 javaslat: {expected:,.0f} Ft".replace(',',' '),4.5,True)
txt(g,14,241,f"Különbözet: +{expected-base['main']:,.0f} Ft; 18 M keret felett: {expected-18000000:,.0f} Ft; külön tartalék: 2 M Ft, felhasználás 0 Ft.".replace(',',' '),3)
yy=228
for label,ids,price,lo,hi,note in rows:
 txt(g,14,yy,label,3,True);txt(g,403,yy,f'{price:+,} Ft'.replace(',',' '),3,True,anchor='end')
 yy=wrap(g,14,yy-5,ids+' / '+note,386,2.55,3.6)-7
wrap(g,14,43,f"A teljes érzékenységi sáv kb. {low/1e6:.2f}–{high/1e6:.2f} M Ft. Nem valószínűségi konfidenciasáv és nem kivitelezői ajánlat. Sem a polcfelület csökkenése, sem a felárak nincsenek tulajdonosi döntésként rögzítve.",388,2.8,4)
save(d,'C01_koltseg','R04','költségforgatókönyv')
# Clear cover/status: prior CP3 layouts are comparison inputs, not the selected new front design.
d,g=sheet('R04 / rajzcsomag használata','Új rajzi szerkesztés, külön képi cél, tárgyelhelyezés és műszaki feltételek.','rajzjegyzék / státusz','00')
blocks=[
 ('Mi az új?', '33 korábbi szerkezet újraszerkesztett színes nézete, belső rajza, metszete és specifikációja; külön WN, TV és B62 frontváltozatok; két tároló, biciklis elrendezés; rekeszenkénti használati és mennyiségi lapok; 5 referencia-/anyaglap; 5 oldalas tulajdonosi útmutató.'),
 ('Mi határozza meg a külsőt?', 'A korábban választott render, a médiafalnál a 2026-10-27-én választott VISUAL_RESCUE kép. A M01–M04 lapok az eredeti képet mutatják. A másik lakás bútorterve csak rajzi minőségi referencia. A képi cél nem felmért méret.'),
 ('Melyik rajzot használja az asztalos?', 'Az R04A jelű WN-01, TV-01, TV-02 és B62-01 lap a megújított, még egyeztetendő változat. A sima WN-01 / TV-01 / TV-02 / B62-01 lap CP3 összehasonlítás: nem alternatívákon átívelő gyártási utasítás. W01/03 mutatja a teljes médiafalat.'),
 ('Mi alkalmas ajánlat egyeztetésére?', 'A feltüntetett befoglalók, rekeszfunkciók, anyagtechnológiai változatok és tételkódok előzetes, összehasonlítható ajánlat alapjai. Színkód, tusgrafikai master, teljes vasalati rendszer és helyszíni méret nélkül nem fix gyártási árat kérünk.'),
 ('Mi nincs lezárva?', 'A végleges tusminta és szín; a nagy ajtók pántolása/merevsége; gardróblift-mozgás; mosdó/szifon; a 05.3 ágy–szék és master éjjeli–ágyfiók konfliktus; konyhai használati sáv; tárolók ajtaja és a bicikli kiemelése. Nem adtunk gyártásra jóváhagyott státuszt.'),
 ('Ár és render státusz', f'A régi Excel 23,25 M Ft-os főösszege nem igazolja az új felületeket. Külön R04 forgatókönyv: {expected/1e6:.2f} M Ft, becslésekkel. A Blenderben 8 natív ellenőrzőkép készült; a sima színezés és hiányzó grafikai master miatt ezek nem végleges látványok.')]
yy=249
for title_,body in blocks:
 txt(g,14,yy,title_,3.5,True);yy=wrap(g,14,yy-7,body,388,3,4.5)-10
save(d,'00_R04_rajzjegyzek_statusz','all','kiadási státusz')
# Assemble the new update first, baseline comparison last; avoid stale archive files in the main route.
idx=[]
for name in ['drawing_index.json','storage_drawing_index.json','supplement_index.json']:idx+=json.loads((O/'data'/name).read_text())
idx+=SHEETS
ordered=[next(s for s in idx if s['pdf'].endswith('00_R04_rajzjegyzek_statusz.pdf'))]
ordered += [s for s in idx if s['pdf'].split('/')[-1].startswith('M')]
ordered += [s for s in idx if '-R04A_' in s['pdf'] or 'W01_03' in s['pdf']]
ordered += [s for s in idx if s['unit'] in ['AT8-01','T-0-26']]
ordered += [s for s in idx if s['pdf'].split('/')[-1].startswith(('U','C01'))]
ordered += [s for s in idx if s not in ordered]
w=PdfWriter()
for s in ordered:w.append(str(O/s['pdf']))
w.compress_identical_objects(remove_duplicates=True,remove_unreferenced=True)
w.write(str(O/'drawings/A902_R04_rajz_es_hasznalati_csomag.pdf'))
(O/'data/complete_sheet_index.json').write_text(json.dumps([dict(page=i+1,**s) for i,s in enumerate(ordered)],ensure_ascii=False,indent=2))
# Separate concise technical inspection report and render handoff constraints.
checks=json.loads((O/'blender/checks.json').read_text())
(O/'BLENDER_ELLENORZES.txt').write_text('KI-R04 — tényleges futtatás és korlátai\n\nKülön .blend munkamásolat, 156 új objektum, 8 natív Workbench kontrollkép.\nA CP3 forrásfájl változatlanságát hash-ellenőrzés igazolta.\nA PASS csak a megnevezett algebrai rekesz- és frontszélesség-vizsgálatra vonatkozik.\n\n'+'\n'.join(c['result']+' | '+c['check']+' | '+c['scope'] for c in checks)+'\n\nA korábbi teljes lakás ütközési eredményeit nem írtuk felül. Az új fájlban nincs jóváhagyott tusgrafika, gyártói liftkinematika vagy fotometriai igazolás.\n')
(O/'RENDER_ATADAS_R04.txt').write_text('R04 CONDITIONAL UPDATE — NOT A FINAL CONSTRUCTION RENDER\n\nUse the existing CP3 view manifest and camera identities; do not rename a new perspective as an old camera.\nFor WN-01, TV-01, TV-02 and B62-01, use the R04A proposal dimensions only if that proposal is explicitly selected. The other CP3 geometry remains subject to its open issues.\nThe chosen media-wall image is the exterior target, not dimensional evidence. Use M01 and W01/03 together. Do not restore the old split upper tower or old lower-front widths.\nThe R04 native closed/cutaway images are dimension studies; no approved ink master or calibrated material exists. Do not call an AI-painted texture verified.\nFor T-0-26, retain both BROR units, move T-R2 50 mm left, place the vertical bicycle envelope at local x1750,y50,w700,d1150 mm. Door and extraction remain unverified.\nAT8-01 retains two JONAXEL racks and the second freezer candidate. Do not conceal opening or ventilation conflicts.\nAttach the relevant M reference sheet, R04A drawing, native Blender control image and cost-scenario status in that order. First produce one technical trial only; stop on front count, shape, material or object-identity mismatch. No bulk generation authorized by this update.\n')
print('Sheets',len(ordered),'R04 estimated',expected,'range',low,high)
