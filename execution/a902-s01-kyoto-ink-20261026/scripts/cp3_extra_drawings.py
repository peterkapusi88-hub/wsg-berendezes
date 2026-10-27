from cp3_drawings import *
from reportlab.graphics.shapes import Path as GPath
G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text())
stores=json.loads((O/'data/storage_CP3.json').read_text())
for st in stores:
 d=frame(st['id']+'  Külön tároló berendezése','Alaprajz + polcnézet · 1:10 A3-on · [J] grafikus tervolvasat; minden kész méret [H]')
 s=2.83465/10;x=65;y=160;sw=st['w'];sd=st['d'];r(d,x,y,sw*s,sd*s,None,INK,1.4)
 for it in st['items']:
  ix=x+it['x']*s;iy=y+it['y']*s;r(d,ix,iy,it['w']*s,it['d']*s,PALE)
  t(d,ix+4,iy+it['d']*s/2,it['id'],10,bold=True)
  if it['kind']=='freezer':
   hx=ix+it['w']*s;hy=iy+it['d']*s;rad=it['w']*s;ln(d,hx,hy,hx,hy+rad,BLUE,1,[4,3]);pts=[]
   for deg in range(90,181,5):pts.extend([hx+rad*math.cos(math.radians(deg)),hy+rad*math.sin(math.radians(deg))])
   d.add(PolyLine(pts,strokeColor=BLUE,strokeWidth=.7,strokeDashArray=[3,3]));t(d,ix,iy-15,'597×675 [D]',9)
 if st['pillar']:
  px,py,pw,pd=st['pillar'];r(d,x+px*s,y+py*s,pw*s,pd*s,colors.HexColor('#bab5aa'));t(d,x+px*s+4,y+py*s+pd*s/2,'PILLÉR [H]',9)
  # Earlier electrical diagram's 2 outlets are points to find, not invented coordinates.
  t(d,x+20,y+sd*s+30,'2 tervi dugalj: helyük / áramkörük bemérendő',11,BLUE)
  hx=x+2410*s;hy=y+sd*s;ln(d,hx-750*s,hy,hx,hy,colors.white,4);ln(d,hx,hy,hx,hy-750*s,BLUE,1,[4,3]);t(d,hx-190,hy+10,'750 ajtó [H]',10,BLUE)
 else:t(d,x+15,y-25,'Ajtónyílás helye a mellékelt tulajdoni lapon nem igazolt.',11,RED)
 dim(d,x,y-45,x+sw*s,y-45,str(sw)+' [J]');dim(d,x-25,y,x-25,y+sd*s,str(sd)+' [J]')
 yy=710
 notes=[('Forrás','WGR1 méretezett alaprajzok: AT8-01 a 2. lap térképi kontúrja és a 26–27. lap 4,57 m² módosítása; T-0-26 a 4. lap 4,00 m² helyisége. A grafikai leolvasat nem kész belméret.'),('Fontos eltérés','AT8-01 régebbi villamos rajza még a korábbi kontúrt mutatja. A két dugalj tervi tény; az ottani falhossz nem került át automatikusan.' if st['id']=='AT8-01' else 'A 2500×1600 mm feltételes elrendezési keret. Ajtó, belmagasság és falvastagság helyszíni felmérés előtt nem igazolt.'),('Bútorok','2× JONAXEL fehér 800×380×1600; 4 polcszint, 25 kg/polc; köztük 597×675×1455 fagyasztó.' if st['id']=='AT8-01' else '2× BROR fekete 850×550×1900; állítható polc; további 500×500 padlóhely bőröndnek. Teher a konkrét készlet gyártói adatával.'),('Használat','Nehéz készlet alul, élelmiszer zárt dobozban. A fagyasztó szellőzési és ajtónyitási gyári távolsága az EAN-azonosítás után ellenőrizendő.' if st['id']=='AT8-01' else 'Ritkán használt nagy tárgyak; a napi gardróbok nem csökkentek emiatt. Rögzítés és nedvességi viszonyok ellenőrizendők.'),('Magasság','2400 mm csak jelenetbefoglaló. Nem a lakás 2900 mm-es magasságának átvétele.'),('Költség','KI-CP3-S01–S04; fagyasztó külön F01/F02. Szerelés, dobozok és falrögzítés is szerepelnek.')]
 for title,txt in notes:t(d,835,yy,title,11,bold=True);yy=para(d,835,yy-17,txt,47,10)-5
 # Readable furniture elevation below/right of plan, independent scale.
 es=.10;ex=835;ey=115
 for j in range(2):
  r(d,ex+j*100,ey,80,160,None)
  for z in [10,53,104,158]:ln(d,ex+j*100,ey+z,ex+j*100+80,ey+z)
 t(d,835,285,'Készpolc elvi nézete; polcállások a készlettel.',9)
 output(d,'ST_'+st['id'])
# Full apartment overlay: source walls, actual CP3 furniture placement and PSU group labels.
d=frame('P-CP3  Teljes lakás - tárolás és belső fény','Tervi elhelyezés és azonosítók · 1:50 A3-on · Kiállások végleges helye felmérésre vár')
s=2.83465/50;ox=65;oy=175
for name,b in G['walls'].items():
 if name.startswith('Plafon'):continue
 x,y,z,X,Y,Z=b;r(d,ox+x*1000*s,oy+y*1000*s,(X-x)*1000*s,(Y-y)*1000*s,colors.HexColor('#d2d4cf'),GREY,.3)
for u in D['units']:
 w,dep=u['w'],u['d']
 if u['rot']==90:w,dep=dep,w
 xx=ox+u['x']*1000*s;yy=oy+u['y']*1000*s;r(d,xx,yy,w*s,dep*s,PALE);t(d,xx+2,yy+3,u['id'],7)
 if u['cp3_bays'] and any(b['lights_mm'] for b in u['cp3_bays']):d.add(Circle(xx+w*s/2,yy+dep*s/2,4,fillColor=GOLD,strokeColor=None))
for it in D['items']:
 if it['x']>17 or it['x']<0 or it['y']>9:continue
 w,dep=it['w'],it['d']
 if it['rot']==90:w,dep=dep,w
 xx=ox+it['x']*1000*s;yy=oy+it['y']*1000*s;r(d,xx,yy,w*s,dep*s,None,BLUE,.5);t(d,xx+2,yy+3,it['id'],6,BLUE)
for code,rects in G['rooms'].items():
 a,b,c,e=rects[0];t(d,ox+(a+c)/2*1000*s,oy+(b+e)/2*1000*s,code,10,BLUE)
para(d,65,135,'Arany jel: belső fénycsoport. A 73 lámpa / 13 tápegység pontos rekesz- és áramköri csoportja a CP3 belső fény és tápegység munkalapon. A vezeték a korpusz oldalsó csatornájában fut, nem a nyitófronton. Dugaljhely nincs helyszíni bizonyíték nélkül újként rárajzolva.',178,11)
para(d,65,80,'K-CP3 / ST lapok: külön használati korlátok. A két külső tároló külön koordinátatérben van; nem a lakás szobájaként számított terület.',175,10)
output(d,'P-CP3')
# Kitchen workflow on its true multi-row arrangement.
d=frame('K-CP3  Konyhai működés és kamra-alternatívák','Meglévő gép- és vízhelyek megőrzésével · 1:10 részlet · 840 mm munkaköz nyitott korlát')
s=.2;ox=55;oy=160
for u in D['units']:
 if not u['id'].startswith('K-'):continue
 w,dep=u['w'],u['d']
 if u['rot']==90:w,dep=dep,w
 xx=ox+(u['x']-8.45)*1000*s;yy=oy+(u['y']-1.35)*1000*s;r(d,xx,yy,w*s,dep*s,PALE);t(d,xx+5,yy+15,u['id'],10,bold=True)
dim(d,ox+620*s,oy+1750*s,ox+1460*s,oy+1750*s,'840 munkaköz')
yy=710
for title,txt in [('Használati sorrend','Hűtő K-02 → mosogató melletti kis lerakó → K-03 mosogató → átfordulás K-06 nagy előkészítőhöz → K-05 főzőlap → edénylerakó a szomszéd pulton → K-01 sütő/mikro. Többsoros konyha; nem egyetlen balról jobbra nézet.'),('Napi gépek','K-04 mosogatógép fölötti kb. 600 mm pult a kávé/pirító zónája. A felnyíló gépfedelek és felső szekrény közti távolság géptípus alapján ellenőrzendő. K-06 marad az előkészítésé.'),('Lerakó feltétel','A mosogató pontos mérete még hiányzik; a hűtő felőli kb. 300 mm lerakó csak kompakt medence és gyártói kivágás mellett alakítható ki. Nem igazolt, kész munkapultként nem számított.'),('Kamra A - 800 mm','800×600×2400, két 400 mm ajtó; öt belső fiók; felső bortartó és polcok. 420 000 Ft becsült teljes új elem, kiváltott K-06-rész után nettó felár ajánlattal. A 1000 mm előkészítő 200 mm-re fogy: nem javasolt főváltozat.'),('Kamra B - 300 mm','300×600×2400 keskeny kihúzható; 5 kosár. 160 000 Ft becsült új elem, kiváltott korpusz levonandó. 700 mm előkészítő marad: érdemi kompromisszum, nem automatikusan elfogadott.'),('Fő javaslat','K-01 felső szárazélelmiszer, K-07 napi készlet, K-06 alsó fiókok; ritka nehéz gép alul. AT8-01 csak tartalékkészlet. A kért teljes kamra még nem fér be tartalomveszteség nélkül.')]:
 t(d,570,yy,title,11,bold=True);yy=para(d,570,yy-17,txt,93,10)-4
output(d,'K-CP3')
# Dimensioned alternative pantry internal design, not selected in cost total.
d=frame('KP-800 / KP-300  Kamraszekrény alternatívák','Külön javaslatok, nem főváltozat · mm · 1:15 A3-on · Elhelyezés / költség jóváhagyásra vár')
s=2.83465/15;yy=170
for x,w,mode in [(80,800,'kétajtós'),(420,300,'kihúzható')]:
 r(d,x,yy,w*s,2400*s,PALE);dim(d,x,yy-25,x+w*s,yy-25,str(w));dim(d,x-20,yy,x-20,yy+2400*s,'2400')
 if mode=='kétajtós':
  for z in [100,320,540,760,980]:r(d,x+30*s,yy+z*s,740*s,180*s,None)
  for z in [1280,1480,1800,2100,2342]:ln(d,x+18*s,yy+z*s,x+782*s,yy+z*s)
  for j in range(6):d.add(Circle(x+(90+j*120)*s,yy+1380*s,45*s,fillColor=None,strokeColor=INK))
 else:
  for z in [100,520,940,1360,1780]:r(d,x+25*s,yy+z*s,250*s,170*s,None)
 t(d,x,670,mode.upper(),12,bold=True)
yy=700
for title,txt in [('KP-800 szerkezet','18 mm korpusz, 19 mm matt front, 8 mm hát, 30 mm szerviz; 764 mm nettó belszélesség. 5× 664×400×150 mm tervezett fiók: 199,2 l. 155° nulla-benyúlású pánt; 450 mm vezető. Belső fiókok és ajtók együtt próbálandók.'),('Ajtóbelső tároló','75 mm mély tea/fűszer kosarak csak a felső, fiókok fölötti ajtózónában: 1250–2000 mm. Nem a fiókok elé. A boros rész 330 mm mély, a palackhossz felmérendő. 6 palackos egy sor a rajzon; nem borhűtő.'),('KP-300 szerkezet','264 mm névleges belszélesség; kosár tényleges nettó mérete és a magas kihúzó terhelése konkrét vasalattól függ. 5 kosár 420 mm raszteren. Nem jelöltük 100%-ban kihasználható tömör térfogatként.'),('Fény és szerviz','KP-800 felső és fiókos rész frontközeli 24 V fénye; ajtóérzékelő, felső hozzáférhető meghajtó. KP-300 oldalsó profil, mozgó kosárszerkezet útján kívül. Fénykészlet és bekötés a kamra árajánlatának része.'),('Döntés','A rajzok tényleges alternatíva-kialakítások. A 840 mm munkaköz és az elvesző pult miatt nem kerültek észrevétlenül a fő lakásmodellbe vagy a költségösszegbe.')]:t(d,590,yy,title,12,bold=True);yy=para(d,590,yy-20,txt,85,11)-8
output(d,'KP_alternativak')
# Bathroom outlet routing / U drawer detail.
d=frame('B62-CP3  Hajápoló fiók és villamos szerviz','900×500×350 mm célbefoglaló · mm · 1:5 részlet · Vizes zóna és gyártói jóváhagyás szükséges')
s=.5;x=65;y=360;r(d,x,y,900*s,500*s,PALE);r(d,x+325*s,y+300*s,250*s,200*s,None,RED,1.5)
t(d,x+170,y+265,'Szifonmező 250×200 [J]',11,RED);dim(d,x,y-25,x+450,y-25,'900');dim(d,x-20,y,x-20,y+250,'500')
r(d,x+60*s,y+50*s,300*s,200*s,None,BLUE);t(d,x+35,y+65,'Hajszárító tárolómező',10)
r(d,x+730*s,y+80*s,80*s,80*s,None,RED);t(d,x+300,y+15,'EU aljzat [J]',10,RED)
yy=710
for title,txt in [('Fiókkialakítás','Felső fiók U alakú szifonkikerüléssel; alsó fiókban elkülönített hajszárító és tartozék. 450 mm névleges vezető tervezett. A 30 mm hátsó szervizsáv itt elmarad: kábel a felső / oldalsó hozzáférhető térben.'),('Jelölt rendszer','Blum AMPEROS AC, EU 230 V, ESS.B01FA.2 jelölt aljzat. Nem amerikai 120 V termék. Pontos 450 mm vezetőhöz tartozó kábelvezetés, kompatibilis fiókrendszer és rendelési lista gyártói egyeztetésre vár.'),('Bekötés','Meglévő, bemért kör → villanyszerelő által ellenőrzött védelem → fix bútorcsatlakozás → gyári mozgó kábelvezető → fiókaljzat. Laza hosszabbító és éles élen megtört kábel nincs a tervben.'),('Használat','Forró hajformázó nem zárható textilre. Használat nyitott fióknál, száraz kézzel; tárolás kihűlve, áramtalanítva. Kapcsolás / hővédelem és a készülék gyártói előírása a végleges szakági terv része.'),('Kapu / alternatíva','A fiókba integrált rendszer nem jóváhagyott. Ha nem fér el vagy a vizes zóna nem engedi: külön, hozzáférhető fix aljzat, ugyanazzal a tárolórekesszel. Fő előirányzat 145 000, gazdaságos fix megoldás 40 000 Ft; nem egyszerre összegezve.')]:t(d,590,yy,title,12,bold=True);yy=para(d,590,yy-19,txt,83,11)-6
para(d,65,290,'Metszeti elv: 19 mm front + 450 mm névleges vezető + 8 mm hát = 477 mm. A fennmaradó 23 mm nem automatikus szerelési megfelelés: a konkrét vasalat előírt korpuszmélysége és a vízcsatlakozás dönt. A rajz nem engedélyezi a mosdókerámia vágását.',75,11)
output(d,'B62-CP3')
# Alternatives retain the complete wardrobe and show both rest and use envelopes.
for room,title,origin in [('05.2','Gyerek / gardrób: változtatható napi tér',(0,0)),('05.3','Vendég / munka: azonos időben használható funkciók',(10.85,4.1))]:
 d=frame(room+'  '+title,'Összehasonlító alaprajz · 1:20 A3-on · Tulajdonosi döntésre váró alternatíva, nem kiválasztott főváltozat')
 sc=2.83465/20; ox=55;oy=160;bx,by=origin
 def rect(label,x,y,w,dep,col=PALE,dash=False):
  xx=ox+(x-bx)*1000*sc;yy=oy+(y-by)*1000*sc;r(d,xx,yy,w*sc,dep*sc,None if dash else col,BLUE if dash else INK,.8)
  t(d,xx+4,yy+dep*sc/2,label,9,BLUE if dash else INK)
 for a,b,c,e in (G['rooms'][room.replace('.','_')]+(G['rooms']['05_2_gardrob'] if room=='05.2' else [])):r(d,ox+(a-bx)*1000*sc,oy+(b-by)*1000*sc,(c-a)*1000*sc,(e-b)*1000*sc,None,GREY,.8)
 if room=='05.2':
  rect('W52: 2380',.02,2.72,2380,600);rect('asztal 750×350',.1,.05,750,350);rect('ülőke',.22,.43,450,450)
  rect('2070×880 nappal',1.48,.05,2070,880);rect('nyitva 2070×1630',1.48,.05,2070,1630,dash=True)
  dim(d,ox,oy-30,ox+3650*sc,oy-30,'3650 tervi');dim(d,ox-20,oy,ox-20,oy+2650*sc,'2650 tervi')
  notes=[('Megőrzött kapacitás','W52 változatlan: 1,437 m akasztás, 4,250 m² polc, 123,9 liter fiók; 1 gardróblift. Nem veszünk el szekrényt az ajtóütközés miatt.'),('A: meglévő ágy + kompakt asztal','A fő ágy helyén marad. ALT052_B: 750×350 mm lehajtható lap és 450×450 mm ülőke; az erkélyajtó mintavételezett nyitási próbája megfelelt. A lap magassága és a szék a gyerek korához igazítandó. Nem teljes felnőtt munkaállomás.'),('B: nappali / alvó átalakítás','FYRESDAL 204.243.62 fekete acél jelölt: 2070×880×940; nyitva 1630 mm széles, két 800×2000 matraccal. A rajzon nappali és éjszakai helyigény. A két állapot között 1,55 m² padló szabadul fel; ez nem új szobaterület.'),('Ár és látvány','Magyar ár/szállítás nincs igazolva; a finn oldalon kifutó jelölés. 180–260 ezer Ft komplett helyettesítési előirányzat, nem bekerült projektköltség. Nettó csereár az aktuális ágy+matrac+szállítás kiváltása után számítható. A fekete fém sziluett eltér a kárpitozott Kyoto Ink ágytól.'),('Modularitás és ellenőrzés','A gardrób rögzített külső mérete mellett 32 mm-es polcraszter, kivehető játékdobozok, cserélhető belső polcok. Gyerekbiztonság, kor, ablak- és függönyhely, asztalrögzítés és a nyitható ágy teljes mozgása még ellenőrzendő.'),('Forrás','IKEA Finland / FYRESDAL20424362, 2026-10-27. A B alternatíva méretezett tervi elhelyezés, nincs Blender PASS-ként kiadva.')]
 else:
  rect('W53 1800×450',10.9,4.15,450,1800);rect('MALM 2100×1750',12.225,4.15,2100,1750);rect('asztal 1200×700',12.95,7.3,1200,700)
  rect('szék munka',12.88,6.7,710,710);rect('600 kihúzás',12.88,6.1,710,710,dash=True)
  dim(d,ox+(12.88-bx)*1000*sc,oy+(5.9-by)*1000*sc,ox+(12.88-bx)*1000*sc,oy+(6.1-by)*1000*sc,'200')
  notes=[('Főváltozat hibája','NORDLI180 + jelenlegi munkaszék: 600 mm kihúzásnál 100 mm átfedés az ágy befoglalójával. Ezért a főváltozat nem kapott megfelelt státuszt.'),('Kidolgozott ALT053','MALM 204.048.06 fehér, 160×200 matrac; gyári befoglaló 2100×1750×1000. Az ágy és a széktér között 200 mm elválasztás marad. Ez nem külön közlekedősáv; a megközelítés nyugatról történik.'),('Futott vizsgálat','A szoba-, fürdő- és teraszajtó 2 fokonként / 100 sugárponttal vizsgált nyitása a négy berendezési befoglalóra megfelelt. A felemelt ágy, nyitott gardrób és valódi székalkatrészek vizsgálata még hiányzik.'),('Kapacitás és ár','W53 érintetlen: 0,350 m előre húzható rúd, 3,103 m² polc, 83,5 l fiók. Ágykeret 219 900 Ft a korábbi189 900 helyett: +30 000 Ft. A 160-as matrac pontos ára és szállítás külön tisztázandó, nem nulla.'),('Kompromisszum','A fekvőfelület 20 cm-rel keskenyebb; oldalfiókok helyett felnyíló ágyneműtartó. Világos sima front, eltérő fejvég. Az alternatíva nincs automatikusan kiválasztva az Excelben vagy a fő rendernézetekben.'),('Forrás','IKEA HU MALM20404806, 2026-10-27; forrásgeometria v2b; CP3 ALT053 kollekció és checks.json. Kész méret és matractömeg gyártói kapu.')]
 # Source door sweeps, retained rather than inferred from renders.
 for dn in (['Ajto_05_2','Erkelyajto_05_2'] if room=='05.2' else ['Ajto_05_3','Ajto_06_2','Uvegfal_05_3_terasz']):
  m=G['openings_meta'][dn];hx,hy=m['zsaner'];rad=m['r'];a,b=m['nyilas']
  if m['fal']=='y':vx=0;vy=(a-hy if abs(a-hy)>.001 else b-hy)/rad;ex=1 if m['irany']=='+x' else -1;ey=0
  else:vy=0;vx=(a-hx if abs(a-hx)>.001 else b-hx)/rad;ex=0;ey=1 if m['irany']=='+y' else -1
  pts=[]
  for deg in range(0,91,3):
   ang=math.radians(deg);xx=hx+rad*(vx*math.cos(ang)+ex*math.sin(ang));yy2=hy+rad*(vy*math.cos(ang)+ey*math.sin(ang));pts.extend([ox+(xx-bx)*1000*sc,oy+(yy2-by)*1000*sc])
  d.add(PolyLine(pts,strokeColor=BLUE,strokeWidth=.7,strokeDashArray=[3,3]));ln(d,ox+(hx-bx)*1000*sc,oy+(hy-by)*1000*sc,pts[-2],pts[-1],BLUE,.7)
 yy=710
 for heading,body in notes:t(d,640,yy,heading,12,bold=True);yy=para(d,640,yy-19,body,73,10)-9
 output(d,'ALT_'+room.replace('.',''))
w=PdfWriter()
for p in allpages:w.append(str(p))
w.compress_identical_objects(remove_identicals=True,remove_orphans=True);w.write(str(O/'drawings/A902_CP3_egyezteto_rajzok.pdf'))
print('8 kiegészítő egyeztető A3 rajz elkészült.')
