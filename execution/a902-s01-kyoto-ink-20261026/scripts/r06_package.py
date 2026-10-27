from pathlib import Path
import json,csv,hashlib,subprocess
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1];O=P/'R06'
# Editable vector pages exported from the inspected PDF, preserving exact dimensions/annotations.
assert len(list((O/'drawings').glob('R06_lap_*.svg')))==7
rows=[['T01','TV-01/02/03;KI-036;CF-01;ST-01','R06 médiafal + Lennon','Grafika újrarajzolt próba; kézi textúra/mintaszín és kárpit még nem igazolt','KI-030..032,036 meglévő keret','Fizikai próba szükséges'],['T02','ART-02;KI-028;KI-029','W02 teljes felület + Toni160/Eamy','Gyári asztalláb/székforma eltérhet a generált képtől; W02 ecsetkép próba','Korábbi tételkeretek','Szín- és nyomatpróba'],['T03','K-01..09;KI-109','F243 ST76 + Somar76','38mm laminátum nem vékony kő;840mm köz nem képi tágasság; Somar laposabb','Pult150000+hátfal100000Ft, változatlan','Felmérés/kivágás/fénypróba'],['T04','WN-01;HB-01;BED-01;KI-117','6magas front, felnyíló ágy, Rondo20','Kárpit és grafika próba; fehér lámpatalp; liftágy új mechanika','Ágy+60100;lámpa+10000;matrac−30100Ft','Vasalat/nyitás/színminta'],['T05','WS-01','4teljes magasságú ajtó, hosszú fekete fogás','A célkép takart széle nem bizonyítja az összes frontszámot;4front a2380mm tervhez igazodik','Fronttétel+80000Ft','Hosszú alapanyag/merevítés/pánt'],['T06','B62-01/02;GL-01','Meglévő grafit mosdóterv és javított üveg','A render aránya nem változtatja meg a900mm mosdóbútort; tálcaésüveggeometria elsődleges','Korábbi árak, kivágás/üvegajánlat nyitott','Víz/szifon/üveg felmérés'],['T07','B62-WC;ART-B62;RAD-B62','Lamellás WC-tároló és vízálló grafika javaslat','Akasztó/pad a zuhanyzónában nem igazolható. A kép teljes másolata így NEM teljesült.','+450000Ft becslés','Tulajdonosi alternatíva + szakági jóváhagyás']]
with(O/'data/vizualis_elteresjegyzek.csv').open('w',newline='')as f:
 w=csv.writer(f);w.writerow(['Cél','Elem','Megoldás','Eltérés','Költséghatás','Státusz']);w.writerows(rows)
cut=[]
for i,w in enumerate([483.5,483.5,484,484,483.5,483.5],1):cut.append(['WN-01',f'F{i}',w,2837,19,1,'MDF hosszú tábla / matt mintafestés / INK-WN','Tervi méret; pánt/merevítés után végleges'])
for i in range(4):cut.append(['WS-01',f'F{i+1}',592,2837,19,1,'MDF hosszú tábla / matt mintafestés / INK-WS','Hosszú fekete fogantyú900mm; felfogatás véglegesítendő'])
cut += [['B62-WC','Oldal',200,1400,18,2,'Nedvességálló lap, tölgyhatás','Élzárás és furatok vízzárása'],['B62-WC','Tető/fenék',864,200,18,2,'Nedvességálló lap','Tervi'],['B62-WC','Osztó',200,1364,18,1,'Nedvességálló lap','Tervi'],['B62-WC','Zárt polc',564,173,18,3,'Nedvességálló lap','Állítható'],['B62-WC','Fülkepolc',282,173,18,3,'Nedvességálló lap','LED hely és kábel egyeztetés'],['B62-WC','Hát',864,1364,8,1,'Nedvességálló hát','Szervizkivágás helyszínen'],['B62-WC','Ajtó',597,1397,19,1,'Tölgyhatású front +10mm lamella','Pántnyitás és súly ellenőrzés'],['BED-01','Oldalváz',2020,260,18,2,'Rétegelt lemez kárpitozva','Kötések és emelőkeret furatok csak kiválasztott vasalattal'],['BED-01','Végváz',1764,260,18,2,'Rétegelt lemez kárpitozva','Tervi'],['BED-01','Középgerenda',1984,260,18,2,'Duplázott rétegelt lemez','Statikai/vasalatgyártói jóváhagyás'],['K-08','Pult',1460,620,38,1,'EGGER F243 ST76','Kivágás gépsablon szerint'],['K-09','Pult',1600,620,38,1,'EGGER F243 ST76','Kivágás gépsablon szerint'],['K-09','Oldalzárás',900,620,38,1,'EGGER F243 ST76','Erezetfordulás próbán ellenőrizendő']]
with(O/'drawings/R06_elozetes_darabjegyzek.csv').open('w',newline='')as f:
 w=csv.writer(f);w.writerow(['Szerkezet','Darab','Szélességmm','Magassághosszmm','Vastagságmm','Db','Anyag','Státusz']);w.writerows(cut)
(O/'drawings/R06_felmeres_es_mintalap.txt').write_text('''KI-R06 — kitöltendő helyszíni és mintavételi lap
Név/dátum/mérőeszköz/fotóazonosító: __________________
Minden érintett fal: kész szélesség alul/középen/felül; belmagasság bal/közép/jobb; függőhiba; sarokszög; padlószint. Ajtó: tok, szárny, pánt, kilincs, nyitási ív. Nyílászáró: valódi nyíló rész, küszöb és redőnyszerviz. Kiállás: hely/magasság/típus; termosztát külön.
WN/WS: kész fülke, kétoldali hézag, magas front gyártói alapanyag és merevítés. BED-01: mechanika SKU, matracsúly, keret teherbírás, nyitási görbe és becsípődésvédelem. B62: tálca széle, lejtés, üveg rögzítés, szifon/fiók, WC szerviznyílás, radiátor kiállás/zóna.
AT8-01/T-0-26: belméretek, ajtó nyitás, szellőzés/dugalj; freezer gyári oldalsó/felső hézag; bicikli kivételi mozgás.
Minták: F243 lap és él; U702/U961 család; Lennon kárpit; Eamy fa/szövet; W01 textúra; W02 hordozó; mindkét gardrób nyomat; fürdő vízálló felület. Azonos fényben együtt vizsgálni.
Nyomat:1:1 részlet, legalább500×500mm a kereszteződésből, valamint kétfrontos illesztés. Fehér negatív foltokat végleges nyomdai knockoutként kezelni, ne fehér tintaként. ICCprofil, felbontás, lakkozás és tűz/vízállóság a tényleges gyártórendszer szerint. Jóváhagyó/aláírás/dátum: __________________
Üres mező nem jóváhagyás. Ez a lap nem helyettesíti a felmérést.
''')
report='''KI-R06 — 2026-10-27 — tényleges módosítási checkpoint
A hét most csatolt kép az új vizuális cél. Az eredeti fájlok és hash-ek a targets/ és data/target_manifest.json alatt. R05 és korábbi források megmaradtak.
ELKÉSZÜLT:177soros élő Excel;7lapos méretezett A3 módosítás PDF+SVG;6lapos termékkönyv;5oldalas tulajdonosi PDF;5 teljes méretű grafikai SVG/PDFpróba;232 új Blender mesh-rész és tényleges újranyitás;12 eltérő terjedelmű ellenőrzési bejegyzés;28 nézeti+21 funkcionális renderátadási rekord; előzetes darabjegyzék; vizuális eltérésjegyzék.
ÁR:24482890Ft teljes /24229890Ft takarékos, külön2000000Ft tartalékból0Ft felhasználva.18M cél nem teljesült. Nincs írásos beszállítói ajánlat. A becslési sáv20841595–32952998Ft.
EZ NEM TELJES MEGVALÓSÍTÁSI LEZÁRÁS. Nem teljesült a teljes képi azonosság és a18M keret együttes igazolása. Újrarajzolt grafikák, nem eredeti masterek. Fotó és gyári befoglaló alapján felépített készbútorok, nem gyári3Dmodellek. Egyes örökölt elemek továbbra is proxyk. Nincs minden mozgásra kiterjedő ütközésmentességi igazolás.
A05.3 ágy/szék elhelyezése javult:600mm székkihúzás után150mm névleges rés; három mintavételezett ajtóív nem ütközött a vizsgált bútorokkal. Ez nem általános akadálymentességi vagy használati minősítés. A konyhában nyitott mosogatógép mellett nincs átjárás.
T07: a grafikai fal akasztó/pad funkciója a zuhanyzóna miatt nem másolható bizonyítottan. Vízálló grafika javaslat és WC-tároló készült; pontos radiátor és nedves falrendszer nyitott. BED-01 felnyíló mechanikája tervezett megoldás, gyártói vasalat és mozgásjóváhagyás nélkül nem gyártható.
AJÁNLATKÉRÉSRE: tételes költség és módosítási lapok, megjelölt feltételekkel. GYÁRTÁSRA: nincs jóváhagyott R06kiadás. RENDELÉSRE: felmérés, minták, gép/vasalat kompatibilitás, szállítási visszaigazolás és költségdöntés szükséges.
A korábbi33egyedi szerkezet belső és szerelési lapjai változatlan részeken érvényben maradnak. Az R06lapok csak az érintett részeket váltják fel; a csomag nem törli a korábbi tárolóterveket.
Következő ellenőrzési pont: árazott gyártói alternatívák, felmérés és mintapróba közös egyeztetése; a18M célhoz6.483M teljesprojekt-csökkentés még nincs kidolgozva vagy igazolva. Sem rendelés, sem ajánlatkérés-küldés, sem tömeges új képgenerálás nem történt.
'''
(O/'00_R06_ELLENORZOTT_ALLAPOT.txt').write_text(report)
# PDF page count/size/text extraction + portable inventory.
qa=[]
for f in O.rglob('*.pdf'):
 reader=PdfReader(f);qa.append({'file':str(f.relative_to(P)),'pages':len(reader.pages),'bytes':f.stat().st_size,'text_chars':sum(len(p.extract_text()or'')for p in reader.pages)})
(O/'qa/pdf_checks.json').write_text(json.dumps(qa,ensure_ascii=False,indent=2))
print('R06 documentation/index completed',len(qa),'PDFs')
