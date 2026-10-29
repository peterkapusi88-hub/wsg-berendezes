from pathlib import Path
import json,math,copy
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A3,A4,landscape
from reportlab.lib.units import mm
from reportlab.graphics.barcode.code128 import Code128
from pypdf import PdfReader,PdfWriter
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
def read(n):return json.loads((O/n).read_text())
parts=read('data/parts.json');holes=read('data/holes.json');programs=read('data/programs.json');hardware=read('data/hardware_bom.json');lights=read('data/lighting.json');alt=read('data/door_alternatives.json');loads=read('data/load_demands.json');cost=read('data/cost_allowance.json');notches=read('data/notches.json');pilot=read('pilot/pilot_manifest.json');sources=read('data/source_register.json')
pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('B','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
W,H=landscape(A3);out=O/'rajzok/TV_R15_szerelesi_es_alkatreszrajzok.pdf';c=canvas.Canvas(str(out),pagesize=(W,H));page=0;pageindex={};partpages={}
def text(x,y,s,size=11,b=False,col='#263331'):
 c.setFillColor(col);c.setFont('B' if b else 'A',size);c.drawString(x,y,str(s))
def wrap(x,y,s,width,size=11):
 buf=''
 for word in str(s).split():
  t=(buf+' '+word).strip()
  if pdfmetrics.stringWidth(t,'A',size)>width:text(x,y,buf,size);y-=size*1.4;buf=word
  else:buf=t
 if buf:text(x,y,buf,size);y-=size*1.4
 return y
def line(x,y,a,b,col='#61736b',lw=.6):c.setStrokeColor(col);c.setLineWidth(lw);c.line(x,y,a,b)
def dim(a,b,s):
 line(*a,*b);line(a[0]-3,a[1]-3,a[0]+3,a[1]+3);line(b[0]-3,b[1]-3,b[0]+3,b[1]+3);text((a[0]+b[0])/2+5,(a[1]+b[1])/2+5,s,10)
def hdr(key,title,sub=''):
 global page
 page+=1;pageindex[key]=page-1;c.setStrokeColor('#bdc7c0');c.rect(25,25,W-50,H-50)
 text(42,H-49,'KYOTO INK / A-902 / TV-MODUL / R15',12,True);text(42,H-79,title,23,True);text(42,H-101,sub,11)
 text(42,43,'TERVEZÉSI ÉS MŰHELYI EGYEZTETŐ KIADÁS - NEM GYÁRTÁSI JÓVÁHAGYÁS',10,True,'#a0492b');text(W-230,43,f'2026.10.29. / mm / {page:03d}',10)
def img(n,x,y,w,h):c.drawImage(str(O/'audit'/n),x,y,w,h,preserveAspectRatio=True,anchor='c',mask='auto')
def blocks(items,x=670,y=705,width=470,size=12):
 for title,body in items:text(x,y,title,size,True);y=wrap(x,y-21,body,width,size-1)-20
 return y
def table(headers,rows,x=50,y=700,widths=None,rowh=35,size=10):
 widths=widths or [1090/len(headers)]*len(headers);xx=x
 for h,w in zip(headers,widths):text(xx,y,h,size,True);xx+=w
 y-=25
 for row in rows:
  xx=x;end=y
  for cell,w in zip(row,widths):end=min(end,wrap(xx,y,str(cell),w-10,size));xx+=w
  y=min(y-rowh,end-10);line(x,y+5,x+sum(widths),y+5,'#dce1dc')
 return y
hdr('cover','A hat fejlesztési csomag egy összeállításban','75 beépülő lapalkatrész / 826 valódi furat / 12 hátlapkivágás / 73 aktív fúrási MPR-tervezet')
img('robbantott.png',40,165,760,535)
blocks([('Konkrét szerkezeti előrelépés','Camar függesztők helye és furatai; Monarch panelklipszek; külön TV-rögzítési út; új hátlapszellőzés és szerelőtálca.'),('Tényleges rajz és ellenőrzés','A fa alkatrészek natív AutoCAD-testek, kivont furatokkal és sarkokkal. A kék/sárga vasalatok helyfoglaló modellek: nem gyári részletességű vagy mozgásszimulált testek.'),('Látható külső','A 3600 mm szélesség, frontok és panelosztás megmaradt. A polcok 30 mm-rel sekélyebbek. Az anyagszínek az ábrákon csoportszínek, nem elfogadott dekor- vagy nyomatminták.'),('Két nyitási alternatíva','A: kisebb, elfordított asztal + nyílóajtók. B: eredeti asztal + leemelhető frontok. A főmodell egyikre sem váltott át tulajdonosi döntés nélkül.')],x=830,width=305)
wrap(45,110,'Ez a csomag már tartalmaz tényleges megmunkált CAD-et, cikkszámos rendszereket, nyitásvizsgálatot, méretezett részleteket, költséget és próbacsomagot. A felmérést, a fal teherbírását és a műhelyi géppróbát nem helyettesíti. Nincs rendelés vagy CNC-végrehajtás.',1090,12);c.showPage()
hdr('elevation','Összeállítási méretlánc és azonosítók','Elölnézet / X jobbra, Y a fal felé, Z felfelé / névleges tervméretek')
ox,oy,sc=75,160,.19
for p in parts:
 x,y,z,w,d,h=p['assembly_box_mm'];c.setFillColor('#d8d2c6');c.setStrokeColor('#77847a');c.rect(ox+x*sc,oy+z*sc,w*sc,h*sc,fill=0)
for i,(x,w) in enumerate(zip([0,840,1530,2220,2910],[720,690,690,690,690])):text(ox+(x+70)*sc,oy+45,'M'+str(i+1),12,True)
for i,x in enumerate([840,1530,2220,2910]):text(ox+(x+70)*sc,oy+1650*sc,'P'+str(i+1),14,True)
dim((ox,oy),(ox+3600*sc,oy),'3600');dim((ox-30,oy),(ox-30,oy+2880*sc),'2880')
blocks([('Változatlan külső lánc','720 torony + 120 süllyesztett sáv + 4 × 690. Alsó zóna Z150–550. Felső zóna Z550–2880. Frontok külső síkja Y−21; panelhát Y400; feltételezett fal Y418.'),('R15 rejtett változások','Hátlap Y354–362, 20 mm-rel beljebb. Polcok Y20–310, mélység 290 mm. Toronyosztó 354 mm mély. Merevítők a függesztők alá kerültek.'),('Ami helyszínen eldől','Fal ferdesége, padló lejtése, plafon és emelési hézag. A 3600 mm egybefüggő fedlap felhordhatósága. A szomszédos függöny, kiállások és redőnyszerviz pontos helye.'),('Mérettűrési keret - javaslat','Darab kész U/V: ±0,3 mm; furatköz: ±0,2 mm; korpuszátló-eltérés legfeljebb 1 mm. Ezek műhelyi egyeztetési célértékek, nem gyártó által automatikusan elfogadott tűrések.')],x=810,width=330)
c.showPage()
hdr('hanger','D15-01 / Camar 807 IN beépítés','Gyári furatkép + tervezett elhelyezés / 6 pár / minden korpusz saját falfüggesztést kap')
img('fuggeszto.png',45,370,510,330)
ox,oy,s=95,190,2.6
# Side YZ section: upper right rear area of M5.
c.setFillColor('#e4ddd1');c.rect(ox,oy,110*s,150*s,fill=1)
for yy in [330,362]:
 for zz in [438,502]:c.setStrokeColor('#ae4934');c.circle(ox+(yy-290)*s,oy+(zz-400)*s,5*s)
dim((ox+40*s,oy+115*s),(ox+72*s,oy+115*s),'32');dim((ox+88*s,oy+38*s),(ox+88*s,oy+102*s),'64')
text(75,135,'Y = 330 / 362; Z = 438 / 502 mm (alsó modulok)',11);text(75,113,'Ø10 ×12, az oldallap belső felületéről. Felső visszaállás: 30.',11)
blocks([('Vasalat és furatkép','80702Z1INSX / 80702Z1INDX; 897ASZ11212 anti-drop lemez. 4 × Ø10, 12 mm mély furat oldalanként. A gyári 32 ×64 mm osztást megtartottuk. A 30 mm felső visszaállás elkerüli a fedlap kötőfuratait.'),('Torony koordinátái','Ugyanez Y330/362, Z2768/2832. A 18 mm oldallapban 6 mm marad a furat mögött. A magas toronyra való alkalmazhatóságot a tényleges tömeg és a Camar alkalmazási feltételei szerint jóvá kell hagyatni.'),('Szabad hely és hátlap','A függesztő helyfoglalása 10 ×68 ×102 mm. A hátlapon oldalanként 22 ×126 mm nyitott sarok. Két egyenes fűrészvágással készíthető; nincs rejtett belső marási rádiusz. Az MPR-ek ezeket a kivágásokat nem tartalmazzák.'),('Hozzáférés és teherátadás','Front felől hozzáférhető állítás, bontható takarás. Oldallap → függesztő → anti-drop lemez → szilárd távtartó és méretezett horgony → teherhordó fal. A hátlap és a dekorpanel nem a falfüggesztés teherhordó eleme.'),('Fali beállítási feltétel','A rajzi lemez hátsíkja Y387, a feltételezett fal Y418: névleges 31 mm távtartás. A kampó tényleges helyzetét és állítását 1:1 próbán kell ellenőrizni, mielőtt falra fúrnak.')],x=620,width=520)
c.showPage()
hdr('loads','Falrögzítés: kiszámított igény, külön jóváhagyandó kapacitás','700 kg/m³ számítási lapsűrűség / furatok levonása nélküli tömeg / 5 kg vasalati tartalék modulonként')
table(['Modul','Lapok kg','Tartalom kg','Összes kg','Függőleges N/pár','Nyomaték Nm'],[[x['module'],f"{x['blank_mass_kg_at700']:.1f}",x['planned_contents_kg'],f"{x['service_mass_kg']:.1f}",f"{x['pair_vertical_service_N']:.0f}",f"{x['overturning_moment_Nm_e0_20']:.1f}"] for x in loads],widths=[100,150,150,150,220,220],rowh=42,size=12)
blocks([('Ez nem megengedett terhelés','A táblázat igényoldali számítás. A 0,20 m excentricitás feltételezés. Nem osztjuk el egyszerűen a teljes terhet a falcsavarok darabszámával: a távtartás, húzás/nyírás, csoporthatás és falanyag együtt számít.'),('Konkrét feltételes horgonycsalád','Fischer SXRL 10×120 T, 522700: csak megfelelő ETA-aljzat, beágyazás, perem/tengelytáv és csatlakozóvastagság esetén jelölt. Gipszkartonra önmagában nem választott megoldás. A fal feltárása és szakági méretezés nélkül nincs végleges horgonydarabszám vagy falba fúrási program.'),('Az asztalosnak átadandó faladat','Falszerkezet és vastagság; burkolat/vakolat vastagsága; vezetékkeresés; síkeltérés; szilárd távtartó anyaga; rögzítési magasságok. A falilemez furatait a tényleges gyári sablonhoz kell kötni.'),('Külön terhek','A TV 16,7 kg névleges készülék + konzol külön falteher. A négy dekorpanel külön klipszrendszeren függ. A torony és alsó korpusz nem egymás bizonytalan terhelésén keresztül kapja a fő függesztést.')],x=55,y=385,width=1080)
c.showPage()
hdr('panel','D15-02 / Levehető dekorpanel és klipszkiosztás','MF375 / 4 panel ×12 klipsz / 96 csavar-előfurat / 4 vízszintes fali sín')
ox,oy,sc=80,155,.21
c.setFillColor('#d9c9b5');c.rect(ox,oy,687*sc,2330*sc,fill=1)
for z in [650,1350,2050,2750]:
 for x in [60,343.5,627]:
  c.setFillColor('#4b899d');c.rect(ox+(x-25.4)*sc,oy+(z-550-9.525)*sc,50.8*sc,34.93*sc,fill=1)
dim((ox,oy-25),(ox+687*sc,oy-25),'687');dim((ox-25,oy),(ox-25,oy+2330*sc),'2330')
text(270,650,'Panelenkénti X a bal éltől:',12,True);text(270,626,'60 / 343,5 / 627 mm',12)
text(270,580,'Közös összeállítási Z:',12,True);text(270,556,'650 / 1350 / 2050 / 2750 mm',12)
text(270,510,'Csavarok a klipszközéptől:',12,True);text(270,486,'X ±16,002; Y400; Ø2,5×12',12)
blocks([('Rétegek és kiemelés','18 mm hordozó, hátul MF375 pár névleges összes6,353 mm projekció. A 18 mm teljes falrésből 11,647 mm névleges kiegyenlítés marad. A klipsz 9,525 mm-t emelve oldható; a gyártó 12,7 mm felső szabad helyet kér.'),('Mennyezet és fény','A 2880 mm panel fölött legalább 25 mm tervezett szabad szerelési/fénykilépési sávot vizsgálunk. Ez csak akkor fér el, ha a felmért plafon ezt engedi. A ragasztott, hozzáférhetetlen felső lezárás nem elfogadható.'),('Csavar és hordozó','3,5×16 pan-head csavar tervezve, a klipsz 3,175 mm anyaga alatt kb.12,825 mm beülés. A Ø2,5×12 pilot próbafúrási érték. A gyártói klipszterhelési adat nem igazolja automatikusan a mi18 mm hordozónkat.'),('Grafika és szerelési sorrend','A tusgrafika panelenként, közös koordinátával osztandó. A jelen revízió nem rajzol új motívumot. Teljes méretű illesztési próbanyomat → hátoldali fúrás → klipsz → száraz összeállítás → végleges felület. A kész grafikus felületet nem lehet korlátlanul utólag fúrni.')],x=620,width=520)
c.showPage()
hdr('tv','D15-03 / TV, konzol és kábelút','Vogel TVM3605 / Samsung QE65Q7FAAUXXH / önálló falrögzítés')
ox,oy,s=80,240,.4
c.setFillColor('#c8c3b8');c.rect(ox,oy,1452.9*s,834*s,fill=1)
c.setFillColor('#4f8799');c.rect(ox+(1452.9-675)/2*s,oy+(834-428)/2*s,675*s,428*s,fill=1)
dim((ox,oy-25),(ox+1452.9*s,oy-25),'1452,9 TV');dim((ox-25,oy),(ox-25,oy+834*s),'834')
text(105,425,'400 ×300 VESA - készülékhez igazítandó',12,True)
blocks([('Rögzített választás','TVM3605, cikkszám3836050, 675×428×22 mm befoglaló. A TV készülékmérete1452,9×834×60,6 mm. A rajzi képernyőközép X2220, Z1450; az adott TVVESA függőleges eltolása még mérendő.'),('Mit nem találtunk ki','A gyári konzol falfuratainak végleges helyét és a TV-be menő csavar hosszát a tényleges konzol/TV útmutatóhoz kell lezárni. A befoglaló téglalap nem fúrási sablon.'),('Teherút','A konzol és szilárd távtartó a teherhordó falhoz kapcsolódik. A dekorpanelen csak szabad átvezetés legyen, a csavar ne szorítsa össze a nyomathordozót. A falcsavar és távtartó együttes ellenőrzése szükséges.'),('Szerviz','A konzol kioldása és a TV leemelése elölről legyen elérhető. Az AV-rekesz Ø60 nyílásán a csatlakozók átférnek; a TV mögötti kábelkilépés pozíciója a készülék csatlakozóihoz igazítandó. 230V és jelkábel külön vezetendő.')],x=730,width=410)
c.showPage()
def plan(tablebox,withsweep):
 ox,oy,s=70,600,.23
 def rect(b,col):c.setStrokeColor(col);c.setFillColor(col);c.rect(ox+b[0]*s,oy+b[1]*s,b[3]*s,b[4]*s,fill=0)
 rect([0,0,0,3600,382,550],'#556c60');rect(tablebox,'#248475')
 for ob in read('data/room_obstacles.json'):
  if 'SO' in ob['id']:rect(ob['box'],'#b4b0a5')
 for x in [1531.5,2221.5]:
  if withsweep:
   p=c.beginPath()
   for a in range(111):
    X=ox+(x+687*math.cos(math.radians(a)))*s;Y=oy+(-12-687*math.sin(math.radians(a)))*s
    if a:p.lineTo(X,Y)
    else:p.moveTo(X,Y)
   c.setStrokeColor('#b9623d');c.drawPath(p)
 rect([1531.5,-21,151.5,687,18,397],'#b9623d');rect([2221.5,-21,151.5,687,18,397],'#b9623d')
 text(90,710,'TV-fal',12,True);text(520,345,'Kanapé / heverőrész',11)
hdr('altA','Nyitási A változat / nyílófrontok, kisebb asztal','Külön tulajdonosi döntés / a főmodellben még nincs átvezetve')
plan(alt['coffee_A'],True)
blocks([('Mit változtatunk?','A két687×397 mm front megmarad; mindkettő2Blumpánttal és1rövidTIP-ON-nal nyílik. Az asztal700×350×350 mm, hosszában a TV-fallal párhuzamos, X1900–2600,Y−1088..−738.'),('Számított eredmény','0,1° lépéssel0–110° között nincs ütközés a vizsgált kanapé/asztal/oldalasztal befoglalóival. A forgási burkolat és az asztal között38,9 mm névleges hely marad; a heverőrész felé300 mm.'),('Kompromisszum','Az asztal felülete22,2%-kal kisebb a700×450 mm tervnél. Helye és aránya láthatóan változik. A nyílófrontok használatához a köztes térnek szabadnak kell maradnia.'),('Költség és bizonyíték','Becsült nettó projektváltozás +35 000 Ft, sáv15–75ezer. Külön24 új pánt/adapterfurat koordinátája az alternatív jegyzékben. A tényleges Blumkinematika, a kéz/láb és a felmért kanapéméret még próbálandó.')],x=920,width=220,size=11)
c.showPage()
hdr('altB','Nyitási B változat / eredeti asztal, leemelhető front','Ritkán használt tárolóhoz / a főmodellben még nincs átvezetve')
plan(alt['coffee_original']['box'],False)
blocks([('Mozgás','4KEKUAS klipszpár/front, belső rögzítőléceken. Először30 mm kihúzás, utána220 mm emelés; a front alja371,5 mm-re kerül, a350 mm asztal fölött21,5 mm névleges hely marad.'),('Az eredmény határa','A kétlépcsős panelmozgás a vizsgált tárgyakba nem ütközik. Ez nem a kezelő kezének és testének modellje, nem klipszerőpróba. A front kb.3,44 kg, a megfogását valódi anyagon próbálni kell.'),('Vasalat és funkció','Häfele262.50.359 panelrész +262.50.368 keretrész. A gyártó legalább4párt és legfeljebb600 mm osztást ír elő. A pontos rögzítőléc/működő klipszgeometria a kiválasztás utáni1:1próbával zárható; a jelenlegi MPR-ek nem tartalmaznak ilyen furatot.'),('Kompromisszum','A külső zárt látvány és az asztal marad. A rekesz hozzáférése körülményesebb, nem napi fiók/ajtó. Becsült többlet45 000 Ft, sáv22–80ezer. A SaliceS10 külön harmadik lehetőség marad, nagyobb belső átalakítással.')],x=920,width=220,size=11)
c.showPage()
hdr('lighting','E15-01 / Három fényág, konkrét komponensekkel','68,8 W szalag / 24 V / 151,2 W tápegység / a védelem és helyszíni bekötés villanyszerelői feladat')
table(['Ág','Profil mm','LED mm','Teljesítmény W','Áram A','Kábel m','Esés V'],[[q['id'],q['profile_mm'],q['LED_mm'],f"{q['W']:.2f}",f"{q['A']:.3f}",q['cable_m_oneway'],f"{q['voltage_drop_V']:.3f}"] for q in lights['circuits']],widths=[90,145,145,170,140,140,170],rowh=38,size=12)
for i,(t,wid) in enumerate([('Meglévő230V kiállás',195),('LPV-150-24',180),('3×DC2A +3×DIM',250),('L01 /L02 /L03',210)]):
 x=60+i*280;c.setStrokeColor('#55766b');c.rect(x,450,wid,55);text(x+10,473,t,12,True)
 if i<3:line(x+wid,477,x+270,477,'#b07b2b',2)
blocks([('Fényforrás és vezérlés','LEDlinePRIME476821:24V,2700K,8W/m,Ra90,8mm,50mmvágás. HáromSunricherSR-ZG9101FA-DIM CV PWM egység, egységenkéntCH1. A gyári útmutató HueBridge-et említ; a helyi párosítás még nincs kipróbálva.'),('Vágás és rendelés','2×5m szalag:3550+2750+2300 mm beépített. A2300 mm ág2250+50 mm, forrasztott vezetékes híddal. Profil4×3m:3000+600,2760,2330; nettó8690 mm. Végzáróknak és forrasztásnak fenntartott hely.'),('Kábelezési számítás','2×0,75mm²Cu, 3/5/4m egyirányú nyomvonalbecslés; meleg réz0,0225Ωmm²/m. A táblázat csak a tápvezeték esése, a szalag belső esését nem számítja. A kábelterhelhetőség, zárlatvédelem és szerelési mód külön ellenőrzés.'),('Jelenetek és próba','Este:25/35/20%; film:8/10/5%; takarítás:100/100/100%. Kiinduló beállítások,1:1mintán finomítandók.2órás maxfényű hőpróba; kis fényen villogás, áramkimaradás és kézi vezérlés próbája.')],x=55,y=405,width=1080)
c.showPage()
hdr('tray','D15-04 / AV-szerviztálca és szellőzés','Második alsó rekesz / front felől kiszerelhető / pontos befoglalók, külön kábelzónák')
img('villamos.png',45,360,570,350)
ox,oy,s=70,135,1.05
c.setStrokeColor('#547468');c.rect(ox,oy,430*s,240*s)
for h in read('data/hardware_geometry.json'):
 if h['id'] in ['PSU','DIM-1','DIM-2','DIM-3','EL-PARTITION']:
  x,y,z,w,d,hh=h['box'];c.setFillColor('#c9af75');c.rect(ox+(x-890)*s,oy+(y-60)*s,w*s,d*s,fill=1);text(ox+(x-890)*s+3,oy+(y-60)*s+10,h['id'],10,True)
dim((ox,oy-20),(ox+430*s,oy-20),'430');dim((ox-20,oy),(ox-20,oy+240*s),'240')
blocks([('Szerkezet','430×240×2 mm acél tálca,17 mm szigetelő távtartókon,4×3,5×30 csavarral. A rögzítőfuratok a fenéklapban vannak. A bal230V zónát válaszfal választja el a jobb oldali dimmerektől; érintésvédett kötődoboz és húzásmentesítés szükséges.'),('Komponensek','Tápegység191×63×37,5 mm. A három vezérlő170×53,4×28 mm. Ezek névleges gyári befoglalók, nem a csatlakozóvezetékek teljes mozgástere. A tálca felett gépet egymásra rakni nem tervezünk.'),('Hátlap','Két48darabosØ10 szellőzőbank, bankonként37,70cm². Alsó Z195/210/225/240; felső460/475/490/505. X1035..1200,15mm osztás. KülönØ20 erősáram ésØ12SELV átvezető, továbbá megmarad aØ60AV átvezetés.'),('Karbantartás','Áramtalanítás → frontnyitás → tálcarögzítő4csavar → hozzáférés a kötődobozhoz/ágvédelemhez. A fix hátlapot ehhez nem kell levenni. A fali légrés szabad be- és kilépése, illetve az üzemi hőmérséklet helyszíni feltétel.')],x=650,width=490)
c.showPage()
for pi in range(2):
 hdr('bom'+str(pi),'Vasalat- és szerelvényjegyzék / '+str(pi+1),'Nettó mennyiség / vásárolható cikkszám és tervezési specifikáció megkülönböztetve')
 table(['ID','Gyártó / SKU','Megnevezés','Menny.','Feltétel'],[[h[0],h[1]+' / '+h[2],h[3],h[4],h[5]] for h in hardware[pi*16:(pi+1)*16]],widths=[65,255,260,65,445],rowh=32,size=10)
 c.showPage()
hdr('assembly','Szerelési sorrend és ellenőrzési pontok','Az ID-k az alkatrészlapon, az Excelben, a DWG-rétegen és a címkén azonosak')
items=[('01 / Felmérés','3600×2880 elférés, plafonhézag, falanyag, kiállások és szolgáltatáskeresés. A helyszíni méretjegyzőkönyv nem készült el digitális következtetésből.'),('02 / Minta','18/8 mm tényleges lap, dekor/él, nyomat és ragasztás. Próbafúrás a2,5mm pilothoz és12mm mélyCamardübelhez.'),('03 / Pilot','Az M5modult először szárazon összerakni. Ellenőrizni a kétoldali oldallapokat, a pántot, a távtartást és az18csapot.'),('04 / Korpuszok','Oldal/fenék/fedlap csapozás; a hátsó keresztlécek az újR15helyen. Átlók mérése, ragasztás és szorítás a választott anyag/ragasztó adatlapja szerint.'),('05 / Hátlapok','Bükk rögzítőlécek,22×126nyitott sarokkivágások, szellőzők és átvezetések. Hátlapok hátulról csavarozva; a fal elé állítás előtt ellenőrizni.'),('06 / Függesztés','Camar és anti-drop lemezek próbája; jóváhagyott horgony/távtartó-rendszer. Minden alsó modul külön függesztve, torony külön felső függesztéssel.'),('07 / Panel és TV','Faloldali sínek síkba állítása, panelklipszek és emelési hely. TV-konzol saját falteherúttal. A panelt ne a TV csavarjai terheljék.'),('08 / Világítás','Tálca, szigetelt kötés, ágak, profilok, fedél/végzáró. Villanyszerelői ellenőrzés után párosítás és hőpróba.'),('09 / Frontok','16 meglévő pánthely,5TIP-ON.3–4front a kiválasztott változat szerint külön kiadásban. Hézagok, nyomás, szomszédos bútorok és hozzáférés próbája.'),('10 / Átadás','Terhelési/elsődarab jegyzőkönyv, beállítások, tisztítás, kábelazonosítók, tartalék LED és alkatrészlista. Módosítás esetén új revízió, régi címke/program elkülönítve.')]
blocks(items,x=55,width=1080,y=710,size=12);c.showPage()
hdr('shop','Műhelyi tájolás és címke-adatkapcsolat','WOF211 homag - a tulajdonos által megadott gépjel / woodWOP5.0 / tényleges gépazonosítás még szükséges')
ox,oy=100,420;c.setFillColor('#ded8cb');c.rect(ox,oy,420,220,fill=1)
for a,b,t in [((ox,oy-25),(ox+420,oy-25),'E1 / V=0'),((ox+430,oy),(ox+430,oy+220),'E2 / Umax'),((ox,oy+240),(ox+420,oy+240),'E3 / Vmax'),((ox-25,oy),(ox-25,oy+220),'E4 / U=0')]:dim(a,b,t)
text(ox+40,oy+110,'A nézet / U jobbra / V felfelé',13,True)
blocks([('Nyersméret a készmérettől elkülönítve','NyersU = készU −E2−E4 +Uráhagyás. NyersV = készV −E1−E3 +Vráhagyás. Ez csak a készméretre élzárt megmunkálási sorrendhez tartozó javasolt szabály; a műhely technológiáját jóvá kell hagyni.'),('B oldal és szálirány','Bfordítás azU tengely körül:V’=Vmax−V,W’=−t−W. Nem azonos a gép valamelyik ütközőjével. Szálirány/dekorpozíció a darablapon; egyszínű korpusznál nincs kitalált erezetkényszer.'),('C címkekód','A tulajdonos szerint élzárás és vastagság. A konkrét C→anyag/vastagság megfeleltetés még hiányzik, ezért nem írtunk önkényes műhelykódot. A kézi R14mezőket megőriztük.'),('Kereső és adatbázis','R15:darabID → SQLite → rajz/MPR útvonal +SHA256. Más revízió és módosult fájl esetén leáll. CSVexport és kitölthetőműhelyprofil mellékelve. Ez működő helyi kereső, nem bizonyítottan telepített woodWOP/Livewood adatbázis-integráció.')],x=650,width=490)
wrap(55,275,'Az aktív MPR-ek EN=1 / ??=1 állapotú fúrási tervezetek. A F_=STANDARD nem egy ellenőrzött műhelyszerszám. A szerszámigény átmérő, irány és mélység szerint összegezve van; szerszámID, befogó, ráállás és fordulat nem található ki a gép tényleges adatai nélkül.',1080,12)
wrap(55,190,'A sarokkivágásokat két egyenes fűrészes műveletként specifikáltuk. Ez végrehajtható műhelyi technológiai alternatíva, de nem nevezzük kész CNC-maróprogramnak. AØ60AV-nyíláshoz külön megmunkálási módot kell kijelölni; a fúrásmakró csak a névleges geometriát írja le.',1080,12);c.showPage()
hdr('pilot','M5 / Teljes reprezentatív próbacsomag','10 alkatrész / 84 furat / 11 aktív MPR / két külön sarokvágás / helyszíni végleges fedlap nélkül')
img('pilot.png',45,370,570,330)
blocks([('Mi van benne?','Két oldal, fenék, polc, front, hátlap, két rögzítőléc, egy merevítő és egy690mm próbafedlap. A fedlap kizárólag a3600mm végleges lap utolsó szakaszát utánozza: nem új beépülő bútorelem.'),('Melyik rendszer próbája?','18db8×30csap;2Blumpánt és talp;1TIP-ON;1párCamarIN és fali lemez;4polctartó;6léc- és6hátlapcsavar. A vasalat és program közös darabID-hoz kötött.'),('A próbával eldönthető','Tényleges lap/élméret; furat és csap illesztés; pánt/TIP-ON működés;Camar hozzáférés; hátlap és léc szerelhetősége; címke visszakeresése. A teljes lakás helyszíni mérete ettől még külön felmérés.'),('Amit még nem futtattunk','woodWOP5megnyitás, gépszimuláció, marószerszám- és befogóellenőrzés, próbagyártás, terhelési próba. A következő lapon üres mérési és elfogadási mezők vannak, nem előre kitöltött PASS.')],x=690,width=450)
table(['Próbadarab','Névleges méret','Furat'],[[p['id'],f"{p['x']}×{p['y']}×{p['t']}",p['hole_count']] for p in read('pilot/data/parts.json')],x=60,y=335,widths=[300,190,70],rowh=15,size=9)
c.showPage()
hdr('measurement','Elsődarab-mérőlap / M5','Műhely: ____________________   Gép/kezelő: ____________________   Dátum: ____________________')
measure=[['Oldallap kész U/V/t','382×382×18 / saját lap szerint','±0,3mm U/V;vastagság mintához','____________','____________'],['Front készméret','687×397×18','±0,3mm U/V','____________','____________'],['Camar osztás és mélység','32×64;Ø10×12','közép±0,2;mélység±0,2mm próbacél','____________','____________'],['Pántcsésze','Ø35×13;éltől23','gyári csészéhez illeszkedjen','____________','____________'],['Csapfuratpár','Ø8;22+12mm','8×30csappal száraz illesztés','____________','____________'],['Sarokkivágás / hátlap','2×22×126;652×362×8','vasalat elfér,nincs repedés','____________','____________'],['Összeállítás','690széles;403mély fronttal','átlóeltérés≤1mm próbacél','____________','____________'],['Front körüli hézag','1,5/3mm tervlánc','nem szorul,pushnyitás működik','____________','____________'],['Szerszám/befogás','műhelyprofil szerint','forgásirány,leszorító,áttörés ellenőrizve','____________','____________'],['Nyitás/terhelés','asztalos által jóváhagyott próba','jegyzőkönyv csatolandó','____________','____________']]
table(['Vizsgálat','Névleges adat','Elfogadási alap','Mért eredmény','Aláírás'],measure,widths=[200,265,300,160,165],rowh=45,size=11)
wrap(55,180,'A tűrések tervezői egyeztetési célok. A műhely a kiválasztott anyag, vasalat és technológia alapján erősíti meg őket. Eltérés esetén az érintett alkatrészt/programot javítani és újraellenőrizni kell; a jóváhagyást nem a táblázat előre kitöltése adja.',1080,12)
text(55,105,'Gyártási kiadás: NEM KIADOTT       Asztalos: ____________________       Tulajdonosi változat: __________',12,True);c.showPage()
hdr('cost','Költség és kapcsolat az élő projektregiszterrel','Bruttó HUF / minden R15 ár becslés / 2026.10.29. / nincs megrendelés vagy beérkezett ajánlat')
table(['Tétel','Tartalom','Menny.','Alsó Ft','Várható Ft','Felső Ft'],[[r[0],r[1],f'{r[2]:g} {r[3]}',f'{r[2]*r[4]:,.0f}',f'{r[2]*r[5]:,.0f}',f'{r[2]*r[6]:,.0f}'] for r in cost],widths=[65,495,125,125,125,125],rowh=28,size=10)
tot=[sum(r[2]*r[j] for r in cost) for j in [4,5,6]]
text(55,135,'Kiválasztott részrendszerek együtt: '+f'{tot[1]:,.0f} Ft; sáv {tot[0]:,.0f}–{tot[2]:,.0f} Ft',13,True)
wrap(55,105,'Ez nem adható hozzá egyben a teljes projekthez. A KI-032 (135000),KI-034 (30000),KI-114 (150000) előirányzat összesen315000Ft-ot már tartalmaz. További93000Ft átfedése a bútor/logisztika soraival ajánlatból tisztázandó.',1080,10);c.showPage()
hdr('closure','Mit lehet átadni, és mi marad külső ellenőrzés?','Az ajánlatkérési műszaki tartalom és a gyártásra kiadás két külön állapot')
table(['Terület','Tényleges átadás','Még szükséges'],[
 ['Vasalat / rögzítés','Kiválasztott rendszerek,pozíciók,furatok,teherút és terhelési igény','Faladat,horgony/távtartó-méretezés,Camaralkalmazáspróba'],
 ['3–4front','Két konkrét összehasonlítható megoldás és mozgásvizsgálat','TulajdonosiA/Bválasztás,gyári kinematika és használópróba'],
 ['Rajz / szerelés','ÚjmegmunkáltDWG,robbanás,metszetek,minden lap és furat','Felmérés,anyag/él/nyomatminta,tűrések elfogadása'],
 ['Világítás','Konkrét szalag/táp/vezérlő,nyomvonal,tálca,költség','Kiállás,védelem,hőmérés,Huepárosítás'],
 ['Műhelyintegráció','Revíziós kereső,hash,CSV,Excel,címke ésműhelyprofil','ValósC-kód,ütköző,szerszámadatbázis/importséma'],
 ['Pilot','10darab/84furat/11MPR és mérőlap','woodWOP5elfogadás,szimuláció,elsődarab és aláírás']],widths=[180,440,470],rowh=58,size=12)
wrap(55,245,'Az élő Excel visszaolvasott főösszege24 673 390Ft. A315000Ft egyértelmű régi részcsomag kiváltásával, a802800Ft új részcsomaggal a konzervatív tervezési összeg25 161 190Ft. Ha a93000Ft közös munkatartalom már a bútorárban van, ebből levonandó. Ez továbbra is becslés, nem elfogadott keretemelés; a2millió tartalék érintetlen.',1080,12)
wrap(55,145,'Az R14 külön126946Ft rejtett szerkezeti előirányzatának korábbi bútorárba való beépülése sem igazolt. Nem adjuk hozzá automatikusan még egyszer: az ajánlatban a teljes75alkatrészes szerkezetet kell egy összegként, a vasalatot és szerelést elhatárolva beárazni. A18milliós teljes célkeret ebben az állapotban nem teljesül.',1080,12);c.showPage()
hdr('sources','Gyári források és bizonyítékok','A gyári méretrajz nem azonos egy visszaigazolt magyar szállítási ajánlattal')
y=710
for s in sources:
 text(55,y,s['id']+' / '+s['title'],12,True);y=wrap(55,y-18,s['url'],1080,9);y=wrap(55,y,s['evidence'],1080,10)-14
c.showPage()
# Complete per-part sheets, including notch geometry and explicit datum/edges.
cap=next(p for p in read('pilot/data/parts.json') if p['id']=='KI15-PILOT-CAP-M5')
allparts=parts+[cap];allholes=holes+[h for h in read('pilot/data/holes.json') if h['part']==cap['id']]
allprograms=programs+[q for q in read('pilot/data/programs.json') if q['part']==cap['id']]
for p in allparts:
 hs=[h for h in allholes if h['part']==p['id']];groups=[hs[i:i+24] for i in range(0,len(hs),24)] or [[]];partpages[p['id']]=[]
 for gi,group in enumerate(groups):
  hdr(p['id']+'_'+str(gi),p['id']+' / '+p['name'],f"{p['x']} × {p['y']} × {p['t']} mm / {p['material']} / {gi+1}/{len(groups)} / {len(hs)} furat")
  partpages[p['id']].append(page-1)
  rot=p['x']>p['y']*1.5;xx=p['y'] if rot else p['x'];yy=p['x'] if rot else p['y'];sc=min(450/xx,440/yy);ox,oy=90,230
  def xy(u,v):return (ox+(p['y']-v)*sc,oy+u*sc) if rot else (ox+u*sc,oy+v*sc)
  c.setFillColor('#e5dfd3');c.setStrokeColor('#4e6057');c.rect(ox,oy,xx*sc,yy*sc,fill=1)
  for n in [n for n in notches if n['part']==p['id']]:
   b=n['box'];f=p['frame'];pts=[]
   for X,Z in [(b[0],b[2]),(b[0]+b[3],b[2]),(b[0]+b[3],b[2]+b[5]),(b[0],b[2]+b[5])]:
    q=[X-f['origin'][0],362-f['origin'][1],Z-f['origin'][2]];pts.append(xy(*[sum(q[k]*f[a][k] for k in range(3)) for a in ['U','V']]))
   path=c.beginPath();path.moveTo(*pts[0]);[path.lineTo(*q) for q in pts[1:]];path.close();c.setFillColor('#ffffff');c.setStrokeColor('#c34d6b');c.drawPath(path,fill=1)
  for h in hs:
   u,v,w=h['local_UVW'];a=h['local_axis'];x,y=xy(u,v);col='#b74432' if a[2]<0 else '#316ca1' if a[2]>0 else '#2f8755';c.setStrokeColor(col)
   if a[2]:c.circle(x,y,h['diameter']*sc/2)
   else:line(x,y,*xy(u+a[0]*h['depth'],v+a[1]*h['depth']),col)
  dim((ox,oy-22),(ox+xx*sc,oy-22),str(xx));dim((ox-24,oy),(ox-24,oy+yy*sc),str(yy))
  # Datum axes are drawn, not merely mentioned in text.
  a=xy(0,0);u=xy(min(p['x'],80),0);v=xy(0,min(p['y'],80));line(*a,*u,'#9f492e',1.4);line(*a,*v,'#2d6896',1.4);text(u[0]+4,u[1]+4,'U',10,True);text(v[0]+4,v[1]+4,'V',10,True)
  text(65,180,'E1:V0 / E2:Umax / E3:Vmax / E4:U0',11)
  wrap(65,158,'Szál/dekor: '+p.get('grain','egyeztetendő')+'; A/B rajzi tájolás, nem gépi ütköző. C műhelykód és nyersméret az Excelben külön.',495,10)
  if any(n['part']==p['id'] for n in notches):wrap(65,112,'Két22×126mm nyitott sarok; fűrészes művelet, az aktív fúrási MPR-en kívül.',495,10)
  cols=[610,665,740,810,870,925,985,1045]
  for x,t in zip(cols,['Furat','U','V','W','Ø','Mély.','Oldal','Tengely']):text(x,705,t,10,True)
  y=682
  for h in group:
   a=h['local_axis'];side='A' if a[2]<0 else 'B' if a[2]>0 else 'ÉL';vals=[h['id'],*[f'{v:g}' for v in h['local_UVW']],h['diameter'],h['depth'],side,','.join(map(str,a))]
   for x,v in zip(cols,vals):text(x,y,v,10)
   line(607,y-5,1135,y-5,'#d9dfd9');y-=18
  y=min(225,y-10);f=p['frame'];y=wrap(610,y,f"O={f['origin']}; U={f['U']}; V={f['V']}; A={f['outward_A']}. Összeállítási XYZ,mm.",520,10)-8
  y=wrap(610,y,'MPR: '+', '.join(Path(q['path']).name for q in allprograms if q['part']==p['id']) if hs else 'Nincs fúrási MPR; további szerelési művelet ettől még lehet.',520,10)-8
  wrap(610,y,'Furatfunkció és forrás: Excel Furatok. AØ2,5pilot tervezői próbaérték. Élzárás után/közben a választott műhelyfolyamat koordinátáit ellenőrizni kell.',520,10)
  c.showPage()
c.save()
# Independent pilot book is an actual subset plus pilot cap, not another task list.
reader=PdfReader(out);writer=PdfWriter();selected=[pageindex[k] for k in ['hanger','assembly','shop','pilot','measurement']]
for id in pilot['parts']:selected+=partpages[id]
for i in selected:writer.add_page(reader.pages[i])
with (O/'pilot/M5_elso_modul_probacsomag.pdf').open('wb') as f:writer.write(f)
# One label set includes75 main parts plus the unique pilot cap.
lc=canvas.Canvas(str(O/'cimkek/TV_R15_cimkek_A4.pdf'),pagesize=A4)
manual={r[0]:r for r in read('audit/R14_excel_snapshot.json')['sheets']['Darabok'][5:] if r and r[0]}
for i,p in enumerate(allparts):
 if i and i%10==0:lc.showPage()
 x=(5+105*(i%2))*mm;y=(297-23.5-((i%10)//2+1)*50)*mm;lc.setStrokeColor('#aaaaaa');lc.rect(x,y,95*mm,50*mm)
 C=manual.get(p['id'],[None]*16)[15] or 'NYITOTT'
 for dy,t,size,bold in [(44,p['id'],11,True),(38,'R15 / '+p['material']+(' / CSAK PILOT' if p==cap else ''),9,True),(32,f"{p['x']} ×{p['y']} ×{p['t']} mm KÉSZ TERV",10,False),(26,'A/B: rajz / E1=V0 / E4=U0',9,False),(21,'C élkód: '+str(C),9,False),(16,'AKTÍV FÚRÁSI TERV / NEM GYÁRTÁSI KIADÁS',7,True)]:lc.setFont('B' if bold else 'A',size);lc.setFillColor('#222');lc.drawString(x+3*mm,y+dy*mm,t)
 Code128('R15:'+p['id'],barWidth=.18*mm,barHeight=8*mm,humanReadable=False).drawOn(lc,x+2*mm,y+5*mm);lc.setFont('A',6);lc.drawString(x+3*mm,y+1.7*mm,'R15:'+p['id'])
lc.save();(O/'audit/pdf_page_index.json').write_text(json.dumps({'sections':pageindex,'parts':partpages,'main_pages':len(reader.pages),'pilot_pages':len(selected),'labels':len(allparts)},ensure_ascii=False,indent=2));print(len(reader.pages),'main pages',len(selected),'pilot pages',len(allparts),'labels')
