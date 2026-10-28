from pathlib import Path
import json,math,zipfile,xml.etree.ElementTree as ET
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4,landscape
from reportlab.graphics.barcode.code128 import Code128
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1];O=P/'R12_muhely';parts=json.loads((O/'data/parts.json').read_text());joint=json.loads((O/'data/joints.json').read_text())
pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('B','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
W,H=landscape(A4);c=canvas.Canvas(str(O/'rajzok/TV_modul_R12_muhelyrajz.pdf'),pagesize=(W,H));pg=0
def text(x,y,s,n=11,b=False,col='#263331'):
 c.setFillColor(col);c.setFont('B' if b else 'A',n);c.drawString(x,y,str(s))
def wrap(x,y,s,width=350,n=11):
 row=''
 for word in s.split():
  if pdfmetrics.stringWidth(row+' '+word,'A',n)>width:text(x,y,row,n);row=word;y-=n*1.45
  else:row=(row+' '+word).strip()
 if row:text(x,y,row,n);y-=n*1.45
 return y
def header(title):
 global pg
 pg+=1;c.setStrokeColor('#b6c1bb');c.setLineWidth(.6);c.rect(22,22,W-44,H-44)
 text(38,H-47,'KYOTO INK / TV-MODUL / R12',12,True);text(38,H-76,title,18,True)
 text(38,41,'TERVEZÉSI / MŰHELYI EGYEZTETŐ KIADÁS - NEM GYÁRTÁSRA JÓVÁHAGYOTT',9,True,'#9a442d')
 text(W-185,26,f'2026.10.28. | {pg:02d} | mm',8)
def line(x,y,X,Y,col='#263331',lw=.7):c.setStrokeColor(col);c.setLineWidth(lw);c.line(x,y,X,Y)
def dim(x,y,w,label):
 line(x,y,x+w,y);line(x,y-4,x,y+4);line(x+w,y-4,x+w,y+4);text(x+w/2-20,y+6,label,10)
header('Áttekintés és javított szerkezet')
text(40,490,'53 külön azonosított lapalkatrész + 26 csomópont',13,True)
def iso(x,y,z):return (50+x*.10+y*.13,145+z*.10+y*.07)
for p in sorted(parts,key=lambda p:p['assembly_box_mm'][1],reverse=True):
 if p['type'] in ['TV01-F','TV02-F1','TV02-F2','TV03-P','GAP']:continue
 x,y,z,w,d,h=p['assembly_box_mm'];v=[iso(x+a*w,y+b*d,z+e*h) for a,b,e in [(0,0,0),(1,0,0),(1,1,0),(0,1,0),(0,0,1),(1,0,1),(1,1,1),(0,1,1)]]
 for a,b in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:line(*v[a],*v[b],lw=.45)
text(40,107,'Nyitott axonometria: frontok/panelek elrejtve. Nem fotorealisztikus látvány.',9)
y=462
for s in ['A DXF-ben az összes ismert R11 lap külön 3DSOLID test, az Excelben és címkén szereplő azonosítóval.', 'Javítás: alsó tiszta magasság 364 mm. Öt hátlap névleges magassága 346 helyett 364 mm.', 'Javítás: közös fedő mélysége 382 mm; a 18 mm-es fronttal együtt 400 mm. Az eredeti tető/front áthatolás megszűnt.', '53 test mérete visszaolvasva; 0 pozitív térfogatú áthatolás. Ez nem terhelési vagy használati igazolás.', 'Az MPR-ek csak befoglaló alapfájlok. A külön közölt furatközéppontok nincsenek megmunkálásként beléjük írva.']:
 y=wrap(475,y,s,325,11)-16
c.showPage()
for p in parts:
 header(p['id']+' | '+p['type']);text(40,493,p['name'],13,True)
 scale=min(330/p['x'],270/p['y']);x=70;y=150;w=p['x']*scale;h=p['y']*scale
 c.setFillColor('#eeeae1');c.setStrokeColor('#263331');c.rect(x,y,w,h,fill=1)
 line(x,y,x+w,y,'#b25c2a',2);line(x,y,x,y+h,'#38666e',2)
 dim(x,y-25,w,str(p['x'])+' mm');text(x+w+7,y+h/2,str(p['y'])+' mm',10)
 text(x+w/2-20,y-48,'E1 / Y=0',10,True);text(x+w/2-20,y+h+13,'E3',10)
 text(x+w+6,y+h-15,'E2',10);text(x-28,y+h/2,'E4',10,True)
 c.circle(x,y,3,fill=1);text(x-10,y-14,'O',10);line(x,y-65,x+70,y-65);text(x+75,y-68,'X',11);text(x+10,y+h/2,'A',16,True)
 yy=463
 rows=[('Kész tervezési méret',f'{p["x"]} × {p["y"]} × {p["t"]} mm'),('Anyag',p['material']+' - konkrét lap/nyomat minta még nem jóváhagyott'),('Felület',p['face']),('Mintairány',p['grain']),('Tájolóél','E1 és E4: rajzi javaslat; gépütközőként még nem jóváhagyott.'),('Élzárás E1/E2/E3/E4',' / '.join('NYITOTT' if v is None else str(v)+' mm' for v in p['edge'])),('C műhelykód','Nem ismert; nem helyettesíti az élvastagságot.'),('Méretforrás',p['note']),('Program',p['mpr']+' / nincs NC-mozgás')]
 for a,b in rows:text(490,yy,a,10,True);yy=wrap(490,yy-15,b,300,10)-10
 text(40,70,'Rajzi arány automatikusan illesztett; méretet a számból olvass. DXF kontúr 1:1 mm.',9)
 c.showPage()
header('D01 | Csapos kötések: két alkatrész, egy furatpár')
text(42,490,'26 kötés / 78 csap / 156 furatközép - tervezési javaslat',14,True)
# sectional construction diagram, not a cutter illustration
c.setFillColor('#e0d9c9');c.rect(90,250,72,180,fill=1);c.rect(162,304,230,72,fill=1)
line(114,340,250,340,'#a55b30',5);dim(90,220,72,'18');dim(114,280,48,'12');dim(162,280,88,'22')
text(95,446,'oldal / tető',11,True);text(225,392,'kapcsolódó lap vége',11,True)
text(90,180,'Séma nagyítva: Ø8 ×30 csap; 12+22=34 mm furathossz.',11)
y=455
for s in ['A 12 mm mély furat a lap felületébe; a 22 mm mély párfurat a kapcsolódó lap végébe kerül. A csap Ø8×30 mm, 4 mm összes elméleti fenékhely marad.', 'Azonos J-kód és párszám azonos összeállítási koordinátát jelent. A furatok tengelye ellentétes irányba mutat. A CSV az irányvektort és mélységet is megadja.', 'A kötés teherbírása nincs igazolva. A lebegő bútor falfüggesztése, a torony önálló rögzítése és a tényleges lapanyag vizsgálata külön szükséges.', 'A középvonalakhoz még hozzá kell rendelni a tényleges gépi oldalt, ütközőt, szerszámot és előtolást. Ezek a pontok nem közvetlenül futtatható CNC-koordináták.']:
 y=wrap(460,y,s,330,11)-15
c.showPage()
header('D02 | Kötésjegyzék és geometriai eredmény')
text(40,494,'Kód       1. alkatrész                     2. alkatrész                    Csap',11,True)
yy=474
for j in joint['joints']:
 text(40,yy,j['id'],9);text(100,yy,j['a'],9);text(300,yy,j['b'],9);text(505,yy,'3 db Ø8×30',9);yy-=14
wrap(600,470,'A furatpontok mindkét alkatrészen a közös összeállítási XYZ-rendszerben szerepelnek. A külön Kotopontok Excel-lap szűrhető a darabazonosítóra. A 156 furattengely mélysége a hozzá tartozó lap belsejében végződik. Furatonkénti palást- és szilárdságvizsgálat, valamint marószerszám- és befogásvizsgálat még nem történt.',190,11)
c.showPage()
header('D03 | Konkrét vasalatirány a fogantyú nélküli fronthoz')
text(40,491,'Torony: rugó nélküli pánt + mágneses nyomásra nyitás',14,True)
yy=459
for a,b in [('Pántjavaslat','Blum CLIP top 70T3550.TL, 110°, ráütődő, csavarozható, rugó nélküli. 5 db/ajtó tervezési kiosztás; a végleges darabszám a front tényleges súlyával igazolandó.'),('Szerelőtalp','Blum 173H7100, 0 mm távolság, 37/32 rendszer. A 18 mm oldalra és 1,5 mm szélső hézagra 16,5 mm ráütés a cél.'),('Nyitó','Blum TIP-ON 956A1004, hosszú mágneses változat; 956A1201 adapter. 2 magas ajtóhoz 2 készlet. Csavaros ellenlap, nem ismeretlen nyomatra ragasztott lemez.'),('Pántközép javaslat','Az ajtó aljától: 100 / 631,75 / 1163,5 / 1695,25 / 2227 mm. Ezek tervezési pozíciók; polc, hátlap és rögzítő ellenőrzendő.'),('Amit nem keverünk','A rugó nélküli TIP-ON-irányt nem helyettesíti automatikusan a rugós BLUMOTION pánt. A 71B3550 fúrásmélységét sem másoljuk át igazolás nélkül a 70T3550.TL modellre.'),('Nyitott geometria','A TIP-ON szükséges front/korpusz nyomási hézaga még nincs bevezetve a 400 mm-es mélységi láncba. Az alsó széles ajtók nyitása és vasalatkiosztása emiatt sem kiadott.'),('Forrás','Blum Catalogue 2022/2023: 74-75,146,172-173,706. Gyártói cikkszámok: publications.blum.com/2022/catalogue/en/74/ és /172/. Mai készlet vagy ajánlat nem igazolt.')]:
 text(40,yy,a,11,True);yy=wrap(210,yy,b,580,10)-15
c.showPage()
header('D04 | Mi bizonyított, mi kell még a gyártáshoz?')
yy=485
for a,b in [('ELKÉSZÜLT','53 darabazonosító; 53 külön ACIS térfogattest; 53 készméret-kontúr; Excel és címke; 26 csapos kötés 156 középponttal. A lapméretek visszaolvasási és áthatolási ellenőrzése lefutott.'),('MÉG NEM TELJES','Az alsó visszahúzott betét, szerelőlécek, falfüggesztők, LED-profilok, kábelkivágások és végleges vasalatfuratok nem szerepelnek teljes gyártási bontásban. A modell laptesteket, nem készre megmunkált alkatrészeket tartalmaz.'),('NYITÁSI TALÁLAT','R10 Blender-befoglalókkal, 1 fokos lépésben: a 3. és 4. alsó front útjában a KI_CF-01 asztal lehetséges akadály mindkét pántoldalnál (első találat 12-40 fok). Közelítő tengely és befoglalóteszt; nem gyártói kinematika.'),('MÉRET / KÜLALAK','Felmérés; falrögzítés; 3600 mm fedlap gépút/szállítás; nyomásra nyitási hézag; illesztési tűrés; szín- és nyomatminta szükséges. A vonalas modell nem felületjóváhagyás.'),('MŰHELY','Szerszámtár és méretei, forgásirány, befogás, gépi oldaltranszformáció. woodWOP 5.0 megnyitás, szimuláció, majd a műhely által ellenőrzött próbadarab/összeállítás.'),('ÁTADÁS','A tulajdonosnak nem egyetlen „minden jó” kijelentést kell adnia. Külön rögzítendő a külső/funkció választása, a felmért adatok, a műhely gyártási ellenőrzése és a minták elfogadása. Ez munkafolyamat-javaslat, nem jogi felelősségátruházás.')]:
 text(40,yy,a,11,True);yy=wrap(200,yy,b,590,11)-18
c.showPage();c.save()
# Exact printable snapshot, 95 x 50 mm, two columns and five rows per A4.
lc=canvas.Canvas(str(O/'cimkek/TV_modul_R12_cimkek_A4.pdf'),pagesize=A4)
for i,p in enumerate(parts):
 if i and i%10==0:lc.showPage()
 col=i%2;row=(i%10)//2;x=(5+105*col)*mm;y=(297-23.5-(row+1)*50)*mm
 lc.setStrokeColor('#999999');lc.rect(x,y,95*mm,50*mm)
 for dy,s,n,b in [(44,p['id'],12,True),(38,p['type']+' / '+p['material'],9,False),(32,f'{p["x"]} × {p["y"]} × {p["t"]} mm KÉSZ TERV',11,True),(26,'E1 lent / E4 bal; A felület felül',8,False),(21,'C élkód: NYITOTT | R12',9,False),(16,'NEM GYÁRTÁS / MPR: NINCS MEGMUNKÁLÁS',7,True)]:
  lc.setFont('B' if b else 'A',n);lc.setFillColor('#111111');lc.drawString(x+3*mm,y+dy*mm,s)
 bar=Code128(p['id'],barHeight=8*mm,barWidth=.21*mm,humanReadable=False);bar.drawOn(lc,x+2*mm,y+5*mm)
 lc.setFont('A',6);lc.drawString(x+3*mm,y+1.7*mm,p['mpr'])
lc.save()
assert len(PdfReader(O/'rajzok/TV_modul_R12_muhelyrajz.pdf').pages)==58
assert len(PdfReader(O/'cimkek/TV_modul_R12_cimkek_A4.pdf').pages)==6
print('PDF pages:58 / labels:6')
