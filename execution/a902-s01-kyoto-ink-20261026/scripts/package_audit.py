from pathlib import Path
import json,hashlib,csv,shutil,zipfile
import openpyxl,pdfplumber
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1];REV='KI-V33-R02'
# Do not delete or replace original checkpoint records: archive superseded handoff documents.
for n in ['README.md','02_FOLYTATAS_ATADAS.md','03_ELLENORZESI_NYUGTA.md']:
 dest=P/'archive/CP1a'/n
 if not dest.exists():shutil.copy2(P/n,dest)
readme='''# A-902 Kyoto Ink S01 – R02 megvalósítási munkacsomag

2026-10-26. Státusz: **érdemi ajánlati és egyeztetési csomag; a teljes megvalósítás még nincs lezárva**. Nincs gyártási engedély, végleges render-PASS, megrendelés vagy elküldött ajánlatkérés.

Az eredeti CP0 és CP1a megmaradt. CP0: `884788f70bdcade7d603f5e90d2f4085c99b939c`; CP1a: `5c855e968b5005e0cac58d2befb64f8f421733d5`; V3.3 célátvétel: `af9906a5039e0fe7198ca8ae8397d53e49352ead`. A munka ugyanazon engedélyezett execution ágon folytatódik. A main és a kreatív ágak változatlanok.

## Kézzelfogható átadás

- [Egyoldalas tulajdonosi PDF](outputs/A902_R02_tulajdonosi_egyoldalas.pdf): pontosan egy A4, valódi tervből származó rajzokkal.
- [Élő Excel](outputs/A902_Kyoto_Ink_elo_regiszter.xlsx):159 sor, fő/gazdaságos számítás, források, lefedettség, ütemterv, eltérések,208 soros előzetes szabásjegyzék és külön05.2 alternatíva.
- [78 oldalas rajzcsomag](outputs/A902_R02_rajzcsomag.pdf):33 szerkezet saját lapja/specifikációja, alaprajzok, gardróbbelsők, TV/konyha/üveg részletek, ALT-052. Egyedi PDF-ek és szerkeszthető SVG-k a `drawings/` mappában.
- [17 oldalas szakági csomag](outputs/A902_R02_szakagi_egyezteto.pdf):világítás, víz/gép, felületek, textilek, kültér, ütemezés, nyitott kapuk.
- [39 oldalas teljes tételjegyzék](outputs/A902_R02_teljes_teteljegyzek.pdf) és [vizuális eltérések](outputs/A902_R02_vizualis_elteresek.pdf).
- [Tényleges Blender-munkafájl](blender/A902_Kyoto_Ink_R02.blend):elmentve és újranyitva;28 semleges kontrollkép, vizsgálati szkriptek és naplók. Méretmodellek, részben egyszerűsített formák; nem teljes gyári termékmodellek.
- [Renderoperátori indítóprompt](render_handoff/00_RENDEROPERATOR_INDITOPROMPT.txt),26 önálló angol prompt és [pontos manifest](render_handoff/manifest_R02.json). Végleges futtatásuk a dokumentált kapuk miatt blokkolt; generatív sorozat nem indult.
- `rfq/`:öt szakági ajánlatkérési tervezet, nincs elküldve.
- `targets/`:hat kiválasztott célkép tényleges PNG-je. Cam02/12 pontos V3.3, többi a korábbi kiválasztás. Régi nappali képek az `archive/renders/` alatt.

## Költség és bizonyíték

Fő előrejelzés **20 554 190 Ft**, takarékos javaslat **19 899 690 Ft**. A18M keret feletti előirányzati eltérés2 554 190, illetve1 899 690Ft. Külön2M tartalék érintetlen. Fő indikatív sáv17 740 028–27 132 689Ft, nem statisztikai vagy beszállítói garancia. Ellenőrzött webshop-termékár1 757 130Ft; írásos ajánlat0Ft; többi18 797 060Ft becslés. A megtakarítások részben becsült egyedi műszaki cserék, nem lekötött ajánlatok. Jakuzzi1,7M +emelés/bekötés0,3M megmaradt.

## Mi használható és mi maradt nyitva?

A fő anyag- és méretjavaslat, költségregiszter és rajzlapok **előzetes összehasonlító ajánlatkérésre/felmérésre** használhatók a nyitott feltételek feltüntetésével. Nem minden lap végleges gyártmányterv: teljes CNC/furatlista, vasalat SKU, minden késztermék, részletes gyári modell és szakági jóváhagyás hiányzik.

A konyhai folyosó840mm, a900mm célt nem teljesíti. Nyitott mosogatógép mellett nincs átjárás. A05.2 fő elrendezés íróasztala/széke ütközik az erkélyajtóval; külön ALT-052 integrált munkahely készült, korlátozott vizsgálatban0jelzéssel. Az alternatíva1380mm teljes magas gardróbot hagy2380mm helyett, +80000Ft±40000 becsült különbséggel; nincs elfogadva és nincs a főösszegben.

További lényeges nyitott tételek: pontos elszívó/mosogató/csap és kültéri főcsalád; teljes Hue/LED SKU és hozzáférés; textilek és minták; minden fiók és gépajtó használata; gyártói bútorazonosság; helyszíni szintek/küszöb/nyílások; elektromos, vizes, üveges és teraszstatikai feltételek. Végleges renderelés előtt a gyári termékfotókat/mesh-eket be kell csomagolni és a modellbe egyeztetni.

A korábbi12termékes korlátozás megszűnt. A folytatás a teljes lakásra vonatkozik; az R02 nem új CP0 és nem késznek nyilvánítás.
'''
(P/'README.md').write_text(readme)
(P/'02_FOLYTATAS_ATADAS.md').write_text('''# Folytatási állapot – R02, teljes lakás

A korábbi csak12termékes szakasz lezárult; régi átadó az archive/CP1a alatt. Induláskor a tényleges távoli ágat és az aktuális Excelt kell visszaolvasni. Ne futtasd a CP0 build_data.py/build_workbook.mjs generátorokat a frissített állományokra.

Az R02 tényleges fájljait a README sorolja. A design_R02.json a jelen méretezett javaslat közös adatforrása. A teljes költséghez az élő Excel az elsődleges; elemek.json/CSV dokumentált pillanatkép. Bármely módosítás előtt cellánként olvasd vissza és őrizd meg a kézi változásokat. Ne importálj újra régi JSON-t az Excelre ellenőrzés nélkül.

Következő ellenőrzési pont: CP3 – pontos beszerzési és gyártói adatlezárás. Első kapuk:05.2 főelrendezés vagy ALT-052 döntés; konyha840mm és elszívóút; külterek konkrét SKU és jakuzzi feltételei; Hue/LED teljes rendszer; minden lámpa/árnyékolás/textil tényleges modellje. Ezek után közös rajz–Excel–Blender revízió, teljes nyitási vizsgálat és gyári termékazonossági kontroll. Rendelési engedély ettől külön szükséges, jelenleg nincs.

A műszaki/költségkutatás továbbra is végezhető; semmi nem jogosít rendelésre, ajánlatkérések elküldésére vagy keretemelés elfogadására. A látványveszteséggel járó anyag-, lámpa- és tárolóváltozások tulajdonosi döntésre várnak. Nem indítható tömeges új generatív renderelés.

Blender: a korlátozott indítás Metal/GPU-detektálásnál összeomlott. Külön jóváhagyott háttérfolyamat működött. Csak a saját execution munkamásolat módosítható; élő felhasználói Blender-session és eredeti forrás nem.

Reprodukálás: a scripts/blender_validate.py a forrásból új R02 főmodellt készít; UTÁNA az alternative_052.py adja hozzá a rejtett alternatívát. A reopen_validate.py a mentett állományt ellenőrzi. A detail_drawings.py alap77oldalt készít; az alternative_052_drawing.py egyszer fűzi hozzá az ALT-052lapot, a végső csomag78oldal. Ezeket érvényes eredményen ne futtasd feleslegesen újra. A render_handoff.py manifestje az aktuális.blend SHA256-ját tartalmazza.
''')
(P/'05_R02_CHECKPOINT.md').write_text('''# R02 checkpoint: tényleges állományok, nyitott megvalósítás

Az R02 a V3.3 célátvétel utáni érdemi munkacsomag. A teljes mesterterv nem lezárt: a nyitott tervezési, termékazonossági és külső jóváhagyási feltételek miatt a végleges render/gyártás még nem engedhető ki.

Elkészült159soros költségregiszter;33egyedi szerkezet;78PDF rajzoldal és SVG-forrás;208soros előzetes alkatrészjegyzék; teljes helyiség×szakma mátrix; világítási/víz/üveg/fal/textil/terasz egyeztetés;17hetes feltételes ütemterv;5RFQ-tervezet; egyA4 tulajdonosi PDF;26 önálló renderprompt; ténylegesen megnyitható Blender és28kontrollkép.

A távoli mentés Git-blobjai a helyi fájlokból számított SHA1-gyel összevetendők; az adatcsomag SHA256 leltára a reports/FILE_MANIFEST_R02.json. A konkrét commit és visszaolvasási nyugta a GitHub-mentés után a reports/REMOTE_R02_VERIFICATION.json-ba kerül.
''')
(P/'reports/BLENDER_INDITAS.md').write_text('''# Blender-indítási hiba és tényleges próba

A felhasználó crash riportja EXC_CRASH/SIGSEGV-t mutatott. A verem releváns pontjai: supports_barycentric_whitelist, MTLBackend::metal_is_supported, GPU_backend_type_selection_detect. Ez nem egyszerű „fájlhozzáférés megtagadva” üzenet, hanem GPU/Metal felismerés közbeni összeomlás.

A korlátozott futtatás hibázott; az engedélyezett külön háttérfolyamat sikeresen megnyitotta a967objektumos eredeti forrást. Az R02 munkamásolatot elmentettük és újra megnyitottuk,28semleges kontrollkép készült. Bizonyíték: run_R02.log, reopen_R02.log, reopen_check_R02.json. A próba alapján a futtatási környezet korlátozása szerepet játszott; ez nem bizonyít általános macOS jogosultsághibát. Nem módosítottunk globális biztonsági beállítást, és nem adtunk indokolatlan teljes lemezhozzáférést.
''')
(P/'03_ELLENORZESI_NYUGTA.md').write_text('''# R02 ellenőrzési nyugta

Az eredeti CP1a nyugta változatlanul az archive/CP1a mappában. A géppel olvasható R02 eredmény: reports/ELLENORZES_R02.json.

- Excel:159elem, képlethiba0, fő20 554 190Ft, takarékos19 899 690Ft, sáv17 740 028–27 132 689Ft. Egy bemeneti+1000Ft a főösszeget pontosan+1000Ft-tal emelte; visszaállítva és újraexportálva.
- A frissítés előtti cellavisszaolvasás és a32szándékos termékadat-változás dokumentálva. Kézi adatok vak újragenerálása nem történt.
- PDF-ek:78rajzoldal,17szakági oldal,39tételjegyzék-oldal,3vizuális eltérésoldal, pontosan1A4 tulajdonosi oldal. A rajzcsomag összes oldaláról kontaktlap készült, a kritikus lapok és az egyoldalas PDF nagyított exportját megnyitottuk.
- Blender:forrás megnyitva, külön munkamásolat elmentve/újranyitva,28kontrollkép. Falszűrés0jelzés. Belső/erkélyajtók közül05.2 DS52/FLINTAN ütközik. A külön ALT-052 korlátozott vizsgálata0jelzést adott, elfogadás nincs.
- Hat étkezőszék37cm eltolása:0jelzés a vizsgált befoglalókon. Kanapé/asztal befoglalójelzés komponensenként nem átfedés. Minden fiók és gépajtó, teljes útvonal, termékazonosság, statika és szakági megfelelőség NINCS teljesen igazolva.
- Renderátadás:26önálló prompt, referencia/kamera/adatkapuk. Gyári termékfotók és modellek több helyen még hiányoznak; végleges sorozat blokkolt. Generatív sorozat nem indult.
- Rendelés, foglalás, elküldött ajánlatkérés:0.
''')
# Automated visible-text boundary check, not a substitute for opened exports.
boundary=[]
for f in (P/'outputs').glob('*.pdf'):
 with pdfplumber.open(f) as pdf:
  bad=[]
  for n,page in enumerate(pdf.pages,1):
   outside=[c for c in page.chars if c.get('text','').strip() and (c['x0']<0 or c['x1']>page.width+.5 or c['top']<0 or c['bottom']>page.height+.5)]
   if outside:bad.append({'page':n,'outside_chars':len(outside)})
  boundary.append({'file':f.name,'pages':len(pdf.pages),'outside_page':bad})
(P/'reports/PDF_LAYOUT_CHECK.json').write_text(json.dumps(boundary,indent=2));print('PDF boundary check',boundary)
# Precise links from every row to available objects/drawings/views; no fictional object for service-only rows.
rows=json.loads((P/'data/elemek.json').read_text());views=json.loads((P/'render_handoff/manifest_R02.json').read_text());mapping=[]
for r in rows:
 mapping.append(dict(element=r['elemkod'],sku=r['sku'],structure=r['szerkezet'],drawing=r['rajz'],blender_objects=r['blender_objektum'],views=[v['view_id'] for v in views if any(q['element']==r['elemkod'] for q in v['products']) or any(u['id'] in v['custom_structures'] and r['elemkod'] in u['cost'] for u in json.loads((P/'data/design_R02.json').read_text())['units'])],status='R02 proposal; technical gates remain'))
(P/'data/elem_rajz_blender_render_mapping.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2))
