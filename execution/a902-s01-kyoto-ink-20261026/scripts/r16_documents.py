from pathlib import Path
import json,math
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A3,A4,landscape
from reportlab.lib.units import mm
from reportlab.graphics.barcode.code128 import Code128
from shapely.geometry import Polygon,box
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok'
def r(n):return json.loads((O/n).read_text())
ps=r('data/parts.json');hs=r('data/holes.json');art=r('data/artwork.json');ds=r('data/drawers.json');light=r('data/lighting.json');cost=r('data/cost.json');mats=r('data/materials.json');notches=r('data/notches.json')
pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('B','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
W,H=landscape(A3);c=canvas.Canvas(str(O/'rajzok/TV_R16_asztalos_tervcsomag.pdf'),pagesize=(W,H));page=0

def text(x,y,s,size=11,b=False,col='#322a23'):
 c.setFillColor(col);c.setFont('B' if b else 'A',size);c.drawString(x,y,str(s))
def wrap(x,y,s,w,size=11):
 buf=''
 for word in str(s).split():
  t=(buf+' '+word).strip()
  if pdfmetrics.stringWidth(t,'A',size)>w:text(x,y,buf,size);y-=size*1.4;buf=word
  else:buf=t
 if buf:text(x,y,buf,size);y-=size*1.4
 return y

def hdr(title,sub=''):
 global page
 page+=1;text(40,H-42,'KYOTO INK / A-902 / MÉDIAFAL / R16',13,True);text(40,H-77,title,22,True);text(40,H-100,sub,10)
 c.setStrokeColor('#b8ab9e');c.line(40,H-113,W-40,H-113)
 text(40,28,'TERVI EGYEZTETÉS / NEM GYÁRTÁSRA JÓVÁHAGYOTT / 2026.10.29. / MÉRETEK mm',10,True);text(W-100,28,str(page),10)
def block(x,y,title,s,w=500):text(x,y,title,13,True);return wrap(x,y-22,s,w,11)-22
def dim(a,b,label):
 c.setStrokeColor('#716558');c.setLineWidth(.5);c.line(*a,*b)
 for x,y in [a,b]:c.line(x-3,y-3,x+3,y+3)
 text((a[0]+b[0])/2+4,(a[1]+b[1])/2+5,label,10)
def poly(g,ox,oy,sc):
 for sh in list(g.geoms) if hasattr(g,'geoms') else [g]:
  if sh.is_empty or sh.geom_type!='Polygon':continue
  p=c.beginPath()
  for ring in [sh.exterior]+list(sh.interiors):
   pts=list(ring.coords);p.moveTo(ox+pts[0][0]*sc,oy+pts[0][1]*sc)
   for x,y in pts[1:]:p.lineTo(ox+x*sc,oy+y*sc)
   p.close()
  c.setFillColor('#29231d');c.drawPath(p,fill=1,stroke=0,fillMode=0)
def elevation(ox,oy,sc,tv=True):
 for p in ps:
  if p['type'] not in ['TV01-F','TV02-F1','TV02-F2','TV03-P','GAP']:continue
  x,y,z,w,d,h=p['assembly_box_mm'];c.setFillColor('#b4a087' if p['type']=='TV03-P' else '#63503d');c.setStrokeColor('#352d25');c.setLineWidth(.5);c.rect(ox+x*sc,oy+z*sc,w*sc,h*sc,fill=1)
 for q in art['ink_polygons']:poly(Polygon(q['outer'],q['holes']),ox,oy,sc)
 if tv:c.setFillColor('#171817');c.rect(ox+1493.55*sc,oy+1033*sc,1452.9*sc,834*sc,fill=1,stroke=0)
 c.setStrokeColor('#dfa84a');c.setLineWidth(2);c.line(ox+729*sc,oy+565*sc,ox+729*sc,oy+2865*sc)

hdr('A kért látványból szerelhető terv','6 magas fiók / 200 mm matt bronzbarna betét / oldalsó LED / nyitásra működő belső fény')
elevation(55,130,.185)
y=690
for title,body in [('A most rögzített működés','Minden alsó front egyetlen magas fiók. A magas torony két nyílóajtós marad. Alsó frontosztás:720+450+450+1080+450+450. Nincs középső vízszintes osztás.'),('A betétsáv valódi anyag','200mm széles,18mm hordozójú matt bronzbarna panel. A torony jobb oldalán rejtett45fokos LEDprofil ezt világítja meg; nem üres fekete hézag és nem új tusmotívum.'),('Mi kész ténylegesen?',f'{len(ps)} lapalkatrész, {len(hs)} kidolgozott szerkezeti furat, vektoros tusgrafika, zárt/nyitott DWG, alkatrészrajzok, címkék és költségmelléklet.'),('Mi nem állítható még?','A kép nem felmérés. A MOVENTO pontos sablonfuratai, a gépi próba, anyagminta, nyomatminta és falrögzítés nincs jóváhagyva. Ez nem kész gépre kiadott gyártási csomag.')]:y=block(790,y,title,body,350)
c.showPage()
hdr('Elölnézet: közös méretlánc és frontsorrend','Az arányok a képből értelmezett,3600mm tervkeretbe illesztett megoldást mutatják.')
elevation(75,120,.22)
for a,b in [(0,720),(720,1170),(1170,1620),(1620,2700),(2700,3150),(3150,3600)]:dim((75+a*.22,135),(75+b*.22,135),str(b-a))
dim((75+720*.22,770),(75+920*.22,770),'200')
y=690
for t,b in [('Felső lánc','720 torony +200 betét +4x670 névleges panel. Négy valódi panel:667x2330x18,3mm köztes osztással.'),('Alsó frontok','M1:717x397; M2:447x397; M3:447x397; M4:1077x397; M5:447x397; M6:447x397. Mind18mm.'),('Kép és terv különbsége','A forrás perspektivikus, részben takart. Nem állítunk fényképből bizonyított gyártási méretet. A középső vízszintes képi vonalat az explicit tulajdonosi döntés szerint elhagyjuk.'),('Tűrés és felmérés','Készméret javasolt±0,3mm, furatköz±0,2mm; műhelyegyeztetési cél. Plafon, padló, fal, nyílások és szerelési hézagok helyszíni ellenőrzése szükséges.')]:y=block(910,y,t,b,240)
c.showPage()
hdr('D16-01 / bronzbetét és oldalról érkező fény','Vízszintes metszet / a betétnek önálló hordozója és rögzítése van')
ox,oy,s=70,300,.55
# X horizontal, Y toward wall shown upward.
for x,y,w,d,col in [(680,0,40,382,'#746a5c'),(720,382,200,18,'#63503d'),(921.5,382,667,18,'#b4a087'),(720,330,18,18,'#dda546')]:
 c.setFillColor(col);c.setStrokeColor('#41372b');c.rect(ox+(x-680)*s,oy+y*s,w*s,d*s,fill=1)
c.setStrokeColor('#ddd');c.line(ox,oy+418*s,ox+920*s,oy+418*s)
dim((ox+40*s,oy+450*s),(ox+240*s,oy+450*s),'200 betét')
for dx in [90,150,220]:c.setStrokeColor('#d8a043');c.line(ox+58*s,oy+348*s,ox+dx*s,oy+382*s)
y=690
for title,body in [('Felület','Azonos matt bronzbarna színminta az alsó frontokkal. NCS S7005-Y20R csak induló mintaszín,5–10GU60° cél. Nem digitális képből véglegesített RAL/NCS-megfelelés.'),('LED','2300mm aktív vonal,24V2700K8W/m.18x18mm45°felületi sarokprofil a toronyoldalon; opál diffúzor, belátásgátló perem. Nem marjuk gyengére a18mm teherhordó oldalt.'),('Rögzítés','4MF375 pár a bronzbetéten:középX820; Z650/1350/2050/2750. PanelhátY400; fali sík418:18mm szerelőtér. Klipsz6,353 +11,647névleges szilárd kiegyenlítés.8pilotØ2,5x12.'),('Szerviz és próba','A panel felfelé oldható; a12,7mm gyári kiemelési igény miatt legalább25mm felső tervi szerelősáv. Oldalfény-vakítás és bronzreflex 1:1mintán. A fénycsík a különAMB-BRONZEkörön dimmelhető.')]:
 y=block(650,y,title,body,480)
# Above blocks need their own page for legibility.
c.showPage()
hdr('D16-02 / hat magas fiók: belső kiosztás és vasalat','Fa fiókdoboz / 15mm nyír / NL300 / teljes kihúzás / külön nyitásérzékelő')
y=690
heads=['Fiók','Frontmm','Belső W×D×Hmm','Liter','Üres kg*','TIPON','Tartalom kg*']
xs=[50,125,265,470,560,680,895]
for x,h in zip(xs,heads):text(x,y,h,11,True)
y-=32
for d in ds:
 row=[d['id'],f"{d['width']-3}×397",'×'.join(map(str,d['inside'])),f"{d['litres']:.1f}",f"{d['empty_mass_estimate_kg']:.1f}",d['motion_unit'],f"≤{d['contents_limit_estimate_kg']:.1f}"]
 for x,q in zip(xs,row):text(x,y,q,12)
 y-=38
for title,body in [('Kinematika és csillapítás','Blum760H3000S +T51.7601 bal/jobb +TIPONBLUMOTION S0 vagyS1 a valódi tömeghez +T60.1125W szinkron +ZS7M400MU stabilizátor. A40kg sínterhelhetőség nem jelenti azt, hogy a rövidS0/S1nyitó40kg-mal működik.'),('Mit lehet beletenni?','D1 takarók és könnyű társasjáték; D2/D3 távirányító,kábelek,játékkonzol-kiegészítők; D4 széles,lapos társasjáték/textil; D5/D6 könnyű dekor és tartalék. A nagy térfogat nem korlátlan könyvterhelés.'),('Miért van csillag a tömegnél?','700kg/m³ lapsűrűségből és1,1kg mozgóvasalatból becsültük. Az üres fiók lemérése és a minimális/maximális terhelésű nyitáspróba választja végleg azS0/S1egységet. A jelen terv nem ígér minden rekeszre40kg hasznos terhet.'),('A még ki nem adott műveletek','A sínkapocs/kampó/stabilizátor gyári sablonfuratai és az alsó hátsó TIPONhelykimunkálás külön nyitott tétel. Az MPR-ben csak a ténylegesen megadott furatok vannak; nincs kitalált szerszám vagy gyári furatkép.')]:y=block(50,y-5,title,body,1090)
c.showPage()
hdr('D16-03 / fiókdoboz metszet és csavarkötések','A mozgó fiók mélysége290mm; a hátulsó szerviztér szabad marad.')
ox,oy,sc=100,280,1.05
for y,z,dep,h,col in [(0,197,290,250,'#d0b684'),(0,210,290,15,'#b99b67'),(0,225,15,222,'#c0a778'),(275,225,15,222,'#c0a778'),(-21,151.5,18,397,'#63503d')]:c.setFillColor(col);c.setStrokeColor('#705b3c');c.rect(ox+(y+30)*sc,oy+(z-150)*sc,dep*sc,h*sc,fill=1)
dim((ox+30*sc,oy-30),(ox+320*sc,oy-30),'290');dim((ox+340*sc,oy+47*sc),(ox+340*sc,oy+297*sc),'250');text(70,225,'Fenék alsó síkja Z210; oldal alsó síkja Z197 →13mm visszaállás.',12)
y=690
for t,b in [('Szélességi összefüggés','LW=modulszélesség−36; SKW=LW−42. Oldalak15mm: külső fiókszélességSKW+30, korpuszhoz6mm hézag oldalanként.'),('Dobozkötés','OldalakonØ4,5 átmenő +fenék/elő-hátélbenØ2,5×20pilot.4×35csavar. Fenékkötés Y50/145/240,Z217,5; elő/hátkötés Y7,5/282,5,Z270/400. Próba szükséges15mm rétegelt lemezhez.'),('Dekorfront','4×30csavar a15mm belső előlapból,3mm távtartón át,12mm a18mm dekorfrontba. Két Xhely:modulkezdet+100 és modulvég−100; Z270/400. FrontonØ2,5×12; belső előlapØ5átmenő.'),('Gyári helyigény','A rajzban a sín egyszerű helyfoglalás, nem hiteles gyári mozgó geometria. A faalj13mm visszaállása a gyári12–15mm tartományon belül van. Hátsó kampó és TIPONalsó kivágás a kiválasztott sablonnal zárandó.')]:y=block(600,y,t,b,530)
c.showPage()
hdr('D16-04 / nyitásvizsgálat és dohányzóasztal','Futott geometriai vizsgálat:0..300mm kihúzás,1mm lépések / névleges téglatestek')
if (O/'audit/R16_fiokok.png').exists():c.drawImage(str(O/'audit/R16_fiokok.png'),40,270,690,440,preserveAspectRatio=True,anchor='c')
y=690
for t,b in [('Jelenlegi asztalhely','A középső fiók teljes kihúzása akadályba fut. A régi asztalhelyet ezért nem jelöljük megfelelőnek.'),('Külön elhelyezési javaslat','Az asztal200mm-rel távolabb kerül a médiafaltól, mérete és formája nem változik. A teljesen kihúzott front és az asztal között37mm névleges hézag marad.'),('Korlát','A37mm tárgyütközési hézag, nem közlekedési út. Az asztal és a kanapé között330mm névleges tér marad. Kéz- és testhelyzet, takaró, szőnyeg és valós bútorforma helyszíni próbát igényel.'),('Döntés','Az asztal eltolását nem hagytuk jóvá a tulajdonos helyett. Ha nem használható, az elhelyezést vagy a kihúzási rendszert kell módosítani; nem rejtjük el a konfliktust a renderen.')]:y=block(770,y,t,b,370)
wrap(50,160,'A teljes nyitási jegyzőkönyv:audit/drawer_sweep.json. Ez a vizsgálat nem helyettesíti a gyári vasalat mozgásszimulációját vagy a helyiség felmérését.',1050,12);c.showPage()
hdr('D16-05 / belső és külső világítás','6fiók +2toronyajtó:nyitva világít,zárva kikapcsol / külön a hangulatfénytől')
y=690
for q in light['circuits']:
 text(50,y,q['id'],11,True);text(200,y,f"{q['length_mm']} mm",11);text(330,y,f"{q['watts']:.2f} W",11);text(450,y,q['control'],11);y-=24
for t,b in [('Teljesítmény',f"Külső és belső fény együtt{light['power_W']:.1f}W. LPV15024:151,2W; névleges terhelés{light['power_W']/151.2:.1%}. Ez a névleges teljesítményvizsgálat, nem hőtechnikai jóváhagyás."),('Érzékelés és bekötés',light['cable']),('Szerelés',light['service']+' '+light['space_loss']),('Átadási próba','Mind a8nyitási kör külön:0/30/300mm fiókállás, csukottajtó, sötét/napfényes környezet, szenzortakarás. Legalább30perc teljes fényterhelés utáni hőellenőrzés; végleges eljárás a villanyszerelőé.')]:y=block(50,y-5,t,b,1090)
c.showPage()
hdr('D16-06 / anyagok, tusgrafika és nyomdai illesztés','A grafika látható részei a mellékelt képből visszavetített vektorok.')
y=690
for row in mats:y=block(50,y,row[0]+' / '+row[1],row[2]+' '+row[3]+' '+row[4],1090)
wrap(50,y,'A TV és tárgyak mögött nem ismert az eredeti minta. Ezeken a területeken nincs kitalált „eredeti” folytatás. A vektor1:1méretű; a forráskép pixelrészletessége ettől nem lesz nagyobb. A látványjóváhagyás teljes méretű próbanyomaton történjen.',1090,12)
c.showPage()
hdr('Felületi mennyiségek és próbanyomat','A nettó felület nem egyenlő a rendelendő tekercsmennyiséggel.')
y=690
for t,b in [('Főpanelmező','4 × 667 × 2330 mm = 6,21644 m² nettó. Nyomati kifutóval 4 × 687 × 2350 mm = 6,4578 m². A 1340 mm széles Bely+Print tekercsre két 687 mm széles nyomat nem fér egymás mellé.'),('Rendelési előirányzat','Négy 2350 mm magas sáv = 9,4 folyóméter. További 0,6 fm mintázási/kezdési kerettel: 10,0 fm × 1,34 m = 13,4 m² rendelési felület. A végleges nyomdai kiosztást ellenőrizni kell.'),('Toronygrafika','2 × 357 × 2327 mm = 1,661478 m² nettó. A matt bronzbarna front bevonatrendszerén tapadás- és karcpróba szükséges; nem automatikusan ugyanaz a hordozó, mint a tapétázott panelen.'),('Bronzbetét és frontok','Betét: 200 × 2330 mm = 0,466 m². Alsó frontok együtt: 3582 × 397 mm = 1,422054 m². A torony látszó külső oldala és teteje, valamint a folytonos fedlap azonos bronzbarna mintát kap; a korpuszbelső M03 marad.'),('Minták és élképzés','Legalább 300 × 300 mm bronz-/nyomatminta, egy illesztést tartalmazó 1:1 csík, és a valódi LEDprofil melletti fénypróba. A grafika közös koordinátán vágandó. A kifutó nem automatikus élre visszahajtási méret. Az ICC-profilt, ragasztót, lakkot és MDF-alapozót a gyártási rendszerhez kell jóváhagyni.')]:y=block(50,y,t,b,1090)
c.showPage()
hdr('D16-07 / rögzítés, szerviz és gyártási sorrend','Az R15 változatlan toronyrészletei az új összeállításhoz kapcsolódnak.')
y=690
for t,b in [('Falfüggesztés','Torony +6alsó modul:7pár Camar80702Z1INSX/DX,897ASZ11212 falilemezekkel. Oldallapon4×Ø10×12,32×64osztás. AlsóY330/362,Z438/502. ToronyZ2768/2832. Távtartók, falanyag és horgony méretezése külön ellenőrzés.'),('Hátlapkivágások','14nyitott sarok:22×126mm. Két egyenes fűrészes vágás, nem kiadott marópálya. A kivágásokat az alkatrész nézeti ábrája és a notches.json tartalmazza.'),('Panel és bronzbetét','4főpanel×12klipsz +4bronzklipsz. MF375 50,8mm, páros32,004mm csavartáv. Gyári kiemelés és18mm falhátsó tér; szilárd síkbeállítás. A TV különVogelTVM3605konzolon teherhordó falhoz rögzül.'),('Szervizlemez','Két300×300×2mm bontható lemez a torony alsóhátsó rekeszeiben. Y278..280, gyári eszközökY282-től. M4átmenő rögzítés széles alátéttel, névleges74mm távtartás a hátlapig; pontos csavarhossz és hátlapteher próbaszereléssel.'),('Sorrend','Felmérés → gyári vasalati mintadarab/sablon → egy fiók és egytoronyajtó próbája → bronz/nyomat/fény mintafal → teljes száraz összeállítás → grafika illesztése → végleges felület → falra szerelés → nyitás- és fénypróba.'),('Program és címke','R16kulcs ésR16állományok. A régiR15alsó ajtóprogramokat nem keverjük az új fiókos revízióba. Saját MPRvisszaolvasás ≠ woodWOP5elfogadás. Szerszám/ütköző/címkeimport és elsődarab műhelyi ellenőrzés kell.')]:y=block(50,y,t,b,1090)
c.showPage()
hdr('D16-08 / költséghatás és asztalosnak átadandó kérdések','Minden itt szereplő ár becslés; nem beszállítói ajánlat.')
y=690
for row in cost['rows']:
 text(50,y,row[0],10,True);y2=wrap(100,y,row[1],610,10);text(740,y,f"{row[2]*row[5]-row[3]:+,.0f} Ft",12);y=min(y-36,y2-12)
for t,b in [('Projektösszeg',f"R15feltételes összeg25 161 190Ft. R16változás{cost['increment_expected']:,.0f}Ft. Új feltételes előrejelzés{cost['conditional_expected']:,.0f}Ft; a18Mkeret felett{cost['conditional_expected']-18000000:,.0f}Ft. A2Mtartalék érintetlen."),('Becslési sáv',f"Ha csak azR16változások sávját mozgatjuk:{cost['conditional_lower']:,.0f}–{cost['conditional_upper']:,.0f}Ft. Az egész lakás további bizonytalan költségei ezt még módosíthatják. A régiKI030/KI031csomagokat levontuk, nem kétszer számoltuk."),('Az ajánlatban külön kérendő','A megnevezett vasalat pontos cikkszáma és teherpróbája; faminőség; frontfelület; nyomtatás/lakk; teljes szerelés; elektromos nyitásfény; falrögzítés és logisztika. A végleges sablonfuratokért felelős gyártó neve és rajzrevíziója.')]:y=block(50,y,t,b,1090)
c.showPage()
# Every part has one readable A3 sheet; long bore lists continue on another sheet.
for p in ps:
 part_h=[h for h in hs if h['part']==p['id']];chunks=[part_h[i:i+30] for i in range(0,len(part_h),30)] or [[]]
 for ci,chunk in enumerate(chunks):
  hdr(p['id']+' / '+p['name'],f"Készméret {p['x']}×{p['y']}×{p['t']}mm / {p['material']} / Aoldal / "+('furatlista folytatás' if ci else 'rajzi referenciarendszer'))
  sx,sy=70,250;sc=min(480/p['x'],430/p['y']);c.setFillColor('#cbb99d');c.setStrokeColor('#5c5143');c.rect(sx,sy,p['x']*sc,p['y']*sc,fill=1)
  for h in part_h:
   u,v,w=h['local_UVW'];a=h['local_axis'];c.setStrokeColor('#b84b37' if a[2]<0 else '#426c9c' if a[2]>0 else '#4b7a48');c.setLineWidth(.6)
   if a[2]:c.circle(sx+u*sc,sy+v*sc,max(1,h['diameter']/2*sc))
   else:c.line(sx+u*sc,sy+v*sc,sx+(u+a[0]*h['depth'])*sc,sy+(v+a[1]*h['depth'])*sc)
  for n in notches:
   if n['part']!=p['id']:continue
   f=p['frame'];b=n['box'];points=[]
   for X,Z in [(b[0],b[2]),(b[0]+b[3],b[2]),(b[0]+b[3],b[2]+b[5]),(b[0],b[2]+b[5])]:
    q=[X-f['origin'][0],354-f['origin'][1],Z-f['origin'][2]];points.append([sum(q[k]*f[uv][k] for k in range(3)) for uv in ['U','V']])
   c.setStrokeColor('#a33a8d');path=c.beginPath();path.moveTo(sx+points[0][0]*sc,sy+points[0][1]*sc)
   for u,v in points[1:]:path.lineTo(sx+u*sc,sy+v*sc)
   path.close();c.drawPath(path)
  dim((sx,sy-25),(sx+p['x']*sc,sy-25),str(p['x']));dim((sx-25,sy),(sx-25,sy+p['y']*sc),str(p['y']))
  text(sx,sy-65,'E1:V=0 / E4:U=0 / nem igazolt gépi ütköző',10)
  yy=690;text(610,yy,'Furat / U / V / irány / Ø × mélység',11,True);yy-=23
  for h in chunk:
   u,v,w=h['local_UVW'];a=h['local_axis'];side='A' if a[2]<0 else 'B' if a[2]>0 else str(a)
   text(610,yy,f"{h['id']} | {u:.2f} | {v:.2f} | {side} | {h['diameter']}×{h['depth']}",9);yy-=17
  yy=block(50,170,'Felület / él / szerelés',f"Anyag:{p['material']}. Erekézet:{p.get('grain','egyeztetendő')}. Él:[{','.join(map(str,p['edge']))}]mm tervi érték E1–E4 szerint; kézi műhelykód azExcelben. {p['note']}",1090)
  wrap(50,yy,'A MOVENTO sablonfuratok külön nyitott műveletek. A furatlista és a hozzá tartozó DXF/MPR azonosR16adatból készül; a teljes fiók gyártása előtt gyári vasalati próba kell.',1090,10);c.showPage()
c.save()
# Artwork: overview plus six actual-size panel sheets, with 10mm bleed.
c=canvas.Canvas(str(O/'artwork/INK_W01_R16_1az1_probanyomat.pdf'),pagesize=landscape(A3));page=0
hdr('Tusgrafika / nyomdai próbafájl','Ez nem végleges ICC-profilos nyomdai leadás; a következő lapok1:1méretűek.')
elevation(60,110,.22,False);wrap(900,680,'A hat képi mező közös koordinátán készül. A bronzbetét200mm széles, grafika nélkül. A forráskép árnyékai és a TV mögötti takarás nem kerültek kitalált mintává alakításra. Kifutó10mm; fizikai minta és színprofil a nyomdával zárandó.',240,12);c.showPage()
for p in art['panels']:
 x,z,w,h=p['X'],p['Z'],p['W'],p['H'];c.setPageSize(((w+20)*mm,(h+20)*mm))
 for q in art['ink_polygons']:poly(Polygon(q['outer'],q['holes']).intersection(box(x-10,z-10,x+w+10,z+h+10)),(10-x)*mm,(10-z)*mm,mm)
 c.setStrokeColor('#aaaaaa');c.setLineWidth(.2);c.rect(10*mm,10*mm,w*mm,h*mm)
 text(12*mm,3*mm,p['part']+' / TRIM '+str(w)+'x'+str(h)+'mm / SCALE100%',8);c.showPage()
c.save()
# Labels: revision-specific barcodes, no oldR15 manufacturing identity.
(O/'cimkek').mkdir(exist_ok=True);c=canvas.Canvas(str(O/'cimkek/TV_R16_cimkek_A4.pdf'),pagesize=A4)
for i,p in enumerate(ps):
 k=i%10
 if i and k==0:c.showPage()
 x=(10+(k%2)*100)*mm;y=(247-(k//2)*54)*mm;c.setStrokeColor('#999');c.rect(x,y,95*mm,49*mm)
 text(x+3*mm,y+42*mm,p['id'],10,True);text(x+3*mm,y+35*mm,f"{p['x']} × {p['y']} × {p['t']} mm / {p['material']}",9)
 text(x+3*mm,y+29*mm,'R16 / TERV - NEM GYÁRTÁSI KIADÁS',8,True);text(x+3*mm,y+23*mm,'A/B a rajzon; E1 V0 / E4 U0; Ckód:Excel',8)
 bc=Code128('R16:'+p['id'],barWidth=.22*mm,barHeight=10*mm);bc.drawOn(c,x+2*mm,y+8*mm);text(x+3*mm,y+3*mm,'R16:'+p['id'],7)
c.save();print('PDFs created',page,len(ps))
