from pathlib import Path
import json,shutil,hashlib,csv
from PIL import Image,ImageChops
P=Path(__file__).resolve().parents[1];O=P/'CP3';Q=P/'sources/CP3_incoming/A902_CP3_TAROLO_MESTERCSOMAG';S=O/'sources';S.mkdir(exist_ok=True)
for rel in ['00_OLVASD_EL.txt','01_ASTRA_MESTERPROMPT.txt','02_KUTATAS/FORRASJEGYZEK.json','03_REFERENCIAK/Anyuka_eredeti_eszrevetelei_20261026.txt','03_REFERENCIAK/Legujabb_tulajdonosi_pontositasok.txt','03_REFERENCIAK/WGR1_meretezett_alaprajzok (1).pdf']:
 shutil.copy2(Q/rel,S/Path(rel).name)
proof=[]
for cam in ['02','12']:
 n=f'A902_S01_KyotoInk_Cam_{cam}__V33_C_v1.png';src=Q/'03_REFERENCIAK'/n;shutil.copy2(src,S/n);a=Image.open(src).convert('RGB');b=Image.open(P/'targets'/n).convert('RGB');proof.append(dict(camera=cam,primary=str((S/n).relative_to(P)),sha256=hashlib.sha256(src.read_bytes()).hexdigest(),previous=str((P/'targets'/n).relative_to(P)),previous_sha256=hashlib.sha256((P/'targets'/n).read_bytes()).hexdigest(),same_decoded_pixels=(a.size==b.size and ImageChops.difference(a,b).getbbox() is None),role='aesthetic target; no geometric proof'))
(S/'visual_source_receipt.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2))
photos=json.loads((O/'evidence/product_photo_manifest.json').read_text())
for ph in photos:
 ph['visual_review']='Product family and pictured colour checked; photo alone does not verify dimensions.'
 if ph['element']=='KI-048':ph['status']='ARCHIVED_ALTERNATIVE_NOT_SELECTED: PAX photo is not the CP3 custom WN-01 carcass.'
(O/'evidence/product_photo_manifest.json').write_text(json.dumps(photos,ensure_ascii=False,indent=2))
evidence=[['CONERO','https://www.kesseboehmer.com/stauraumloesungen/ankleide/conero-kleiderlifte','12 kg normál; rekeszhez választott szélességtartomány; HU teljes készlet/ár ajánlatra vár'],['MOVENTO','https://www.blum.com/hu/hu/products/runnersystems/movento/overview/','40/70 kg termékcsalád; pontos vezető és rögzítőkészlet gyártói egyeztetés'],['AMPEROS AC','https://www.blum.com/hu/hu/products/electronic-systems/amperos-ac/overview/','EU230V jelölt; mosdófiók / vizes zóna nem jóváhagyott'],['FYRESDAL20424362','https://www.ikea.com/fi/en/p/fyresdal-day-bed-frame-black-20424362/','2070×880×940; nyitva1630; nem kiválasztott, HU elérhetőség/ár nyitott, finn kifutójelzés'],['MALM20404806','https://www.ikea.com/hu/hu/p/malm-agynemutartos-agy-feher-20404806/','219900 Ft keret; 2100×1750×1000; ALT053, nem kiválasztott'],['Liebherr','https://www.liebherr.com/hu-hu/p/fnd-4625-3121280','289990 Ft gyártói tájékoztató ár; név/URL eltér, EAN egyeztetendő']]
evidence += [[x['sku'],x['url'],x['status']] for x in photos]
with (O/'evidence/forrasok_CP3.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['Termék / család','Elsődleges forrás','Bizonyíték korlátja','Ellenőrzés']);w.writerows([r+['2026-10-27'] for r in evidence])
(O/'README_CP3.txt').write_text('''A902 KYOTO INK / CP3-R03 / 2026-10-27
AKTUÁLIS ÁLLAPOT: ajánlatkérési és felmérési tervcsomag, nem gyártásra jóváhagyott terv.

A jóváhagyott helyiségfunkciók és a nagy tárolási igény átvezetve. A leltár és kész belméretek ismeretlenek, nem felmért adatként szerepelnek. Kiindulás: e7e824043d7100600daf56666a349c1998dfe98a; első CP3 mentés: f7b2d3f31a8d2d55ddb4521e1860ac8507f81566. R02 visszaállítás nem történt.

MIT NYISS MEG?
1. A902_CP3_tulajdonosi_osszefoglalo.pdf: egyoldalas aktuális döntési lap.
2. ../outputs/A902_Kyoto_Ink_elo_regiszter.xlsx: az egyetlen élő Excel,172 tétel/20 lap.
3. drawings/A902_CP3_egyedi_butorok.pdf:33 elem,66 A3 lap; azonos nevű önálló PDF-ek és SVG-k.
4. drawings/A902_CP3_egyezteto_rajzok.pdf:8 A3 lap, két tároló, egész lakás, konyha, kamraalternatívák, fürdőfiók és két kisebb háló alternatívái.
5. specifications/A902_CP3_szakagi_es_hasznalati_csomag.pdf:7 oldal; tervezési döntések, korlátok, ütemezés és ajánlatkérések.
6. blender/A902_Kyoto_Ink_CP3.blend: valóban megnyitott és mentett külön munkamodell; checks.json107 futtatott részvizsgálat,95 PASS,4 FAIL,5 OPEN,2 CONDITIONAL,1 OWNER_DECISION. Ezek külön tesztek, nem teljes lakásmegfelelés.
7. render_handoff/START_RENDER_OPERATOR_EN.txt: indítóprompt;28 helyiségnézet és21 belső funkcionális nézet, saját angol promptokkal és hash-es manifesttel.

MENNYISÉG ÉS ÁR
Master:3,030 m akasztás,8,594 m² polc,406,5 l fiók.05.2:1,437 m/4,250 m²/123,9 l.05.3:0,350 m/3,103 m²/83,5 l.25% szabad tartalék külön kezelve. A polc és alatta lelógó ruha terét nem szabad kétszer teljesen feltölteni.
73 belső fény,13 tápegység,3 liftjelölt. A Cycles terhelt fénypróba ténylegesen lefutott; nem hitelesített luxmérés.
Teljes fő előirányzat23 253 840 Ft; gazdaságos csereváltozat22 468 340 Ft. Indikatív sáv20 037 530–30 777 532 Ft. A18 M kerethez +5 253 840 Ft hiány; a2 M tartalék érintetlen.
Ellenőrzött webshopár2 352 790 Ft; írásos ajánlat0 Ft; becsült / nem végleges rész20 901 050 Ft. Nincs fix teljes kivitelezési ajánlat. Az új fagyasztó334 990 Ft kapcsolódó munkával a fő forgatókönyvben benne van. Jakuzzi és beemelés/bekötés2 M Ft továbbra szerepel.

MI ALKALMAS AJÁNLATKÉRÉSRE?
Az egyedi elemek befoglalói, belső kiosztása, anyag/vasalat-jelöltjei és fénycsoportjai; tárolók készpolcos és feltételes egyedi alternatívái; szakmánként5 előkészített RFQ. Az ajánlattevőnek a hiányzó műszaki feltételeket és kizárásokat tételesen jeleznie kell. A szabáslista előzetes, nem CNC vagy gyártási utasítás.

MI AKADÁLYOZZA A VÉGLEGES KIADÁST?
• Konyha840 mm munkaköz, nyitott mosogatógépnél240 mm: meglévő geometriai korlát.
• Master NORDLI fejvégi oldalfiókjai és éjjelik átfednek: alternatív bedside kialakítás még tulajdonosi/tervezési döntés.
•05.2 fő asztal/erkélyajtó és05.3 fő ágy/szék: külön ALT052/ALT053 rajz és vizsgálat van, nincs automatikus kiválasztás. FYRESDAL további, csak méretezett tervi opció.
• Tárolók kész belmérete, T-0-26 ajtója, kiállások, mennyezet, rögzítés, fürdő-villamosság, pontos vasalatkészletek és késztermékvariánsok még ellenőrzendők.
• V12/V13 eredeti gardróbkamerája túl közeli: BLOCKED_CAMERA_FRAMING; F01/F02 technikai belsőnézet használható. Új fotós kamera új azonosítót igényel.
• A modell több készterméket mérethelyes, egyszerűsített befoglalóval mutat. Nincs általános renderazonosság, teljes termékazonos3D vagy gyártási PASS. Végleges képkiadás ezért nincs.

KÖVETKEZŐ ELLENŐRZÉSI PONT
CP4: az alternatívák kiválasztása és közös helyszíni méret/kiállás-jegyzőkönyv után az érintett főváltozat frissítése; pontos gyártói vasalat és tételes ajánlat beépítése; költség újraszámítása; nyitáspróbák és első technikai render ismétlése. Addig nincs rendelés, RFQ-küldés vagy gyártási kiadás.14–16 hét csak a döntésekhez és igazolt átfutásokhoz kötött feltételes ütem,17. heti javítási mozgástérrel.

A korábbi5 oldalas R02 tulajdonosi ismertető megőrzött történeti dokumentum, költségét a jelen CP3 felülírja. A későbbi végleges, képes brosúra briefje elkészült, az elfogadott renderek után állítható össze. A S12 referencia stílusa és tartalma nem került átvételre.
''')
readme=P/'README.md';text=readme.read_text();marker='<!-- CP3_CURRENT -->'
if marker not in text:readme.write_text(marker+'\n## Aktuális CP3-R03 — 2026-10-27\n\nA legfrissebb tárolási és világítási csomag belépője: [CP3/README_CP3.txt](CP3/README_CP3.txt). Az élő Excel fő előirányzata **23 253 840 Ft**, a tartalék külön marad. A CP3 ajánlati/felmérési állapot; a régebbi fejezetek összegei történeti adatok.\n\n'+text)
print('CP3 források, árforrásjegyzék és átadási útmutató elmentve.')
