from pathlib import Path
import math,html,csv,json,base64,io,textwrap
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
P=Path(__file__).resolve().parents[1];O=P/'R11_butorterv';W,H=1683.78,1190.55
pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('B','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
c=canvas.Canvas(str(O/'pdf/Kyoto_Ink_R11_nappali_butorterv.pdf'),pagesize=(W,H));c.setTitle('Kyoto Ink R11 - Nappali részletes ajánlati bútorterv');svg=[];page=0
def color6(v):
 return '#'+''.join(x*2 for x in v[1:]) if isinstance(v,str) and len(v)==4 and v.startswith('#') else v
INK='#252727';GRAY='#e5e5df';GREIGE='#b6aa96';RED='#a04b34';GOLD='#b48e48';s=72/25.4/10

def line(x,y,X,Y,color=INK,width=.6,dash=False):
 color=color6(color);c.setStrokeColor(color);c.setLineWidth(width);c.setDash(4,3) if dash else c.setDash();c.line(x,y,X,Y);svg.append(f'<path d="M{x},{H-y} L{X},{H-Y}" stroke="{color}" stroke-width="{width}" fill="none"'+(' stroke-dasharray="4 3"' if dash else '')+'/>')
def rect(x,y,w,h,fill=None,color=INK,lw=.6):
 color=color6(color);c.setStrokeColor(color);c.setLineWidth(lw);c.setDash();
 if fill:fill=color6(fill);c.setFillColor(fill)
 c.rect(x,y,w,h,fill=bool(fill),stroke=1);svg.append(f'<rect x="{x}" y="{H-y-h}" width="{w}" height="{h}" fill="{fill or "none"}" stroke="{color}" stroke-width="{lw}"/>')
def txt(x,y,t,size=11,color=INK,b=False):
 color=color6(color);c.setFillColor(color);c.setFont('B' if b else 'A',size);c.drawString(x,y,str(t));svg.append(f'<text x="{x}" y="{H-y}" font-family="Arial" font-size="{size}" fill="{color}"'+(' font-weight="bold"' if b else '')+'>'+html.escape(str(t))+'</text>')
def note(x,y,t,w=410,size=11):
 # actual font-width wrapping
 words=t.split();row='';yy=y
 for word in words:
  if pdfmetrics.stringWidth(row+' '+word,'A',size)>w:
   txt(x,yy,row,size);yy-=size*1.45;row=word
  else:row=(row+' '+word).strip()
 if row:txt(x,yy,row,size)
 return yy-size*1.8

def dh(x,y,vals,scale=s,total=True):
 xx=x
 for v in vals:
  line(xx,y-5,xx,y+7);line(xx+v*scale,y-5,xx+v*scale,y+7);line(xx,y,xx+v*scale,y);line(xx-3,y-3,xx+3,y+3);txt(xx+v*scale/2-12,y+7,str(v),9);xx+=v*scale
 if total and len(vals)>1:dh(x,y-25,[sum(vals)],scale,False)
def dv(x,y,h,scale=s):
 line(x,y,x,y+h*scale);line(x-6,y,x+6,y);line(x-6,y+h*scale,x+6,y+h*scale);txt(x+8,y+h*scale/2,str(h),10)
def title(t,scale='1:10 / részletek jelölve'):
 global page,svg
 page+=1;svg=[];rect(22,22,W-44,H-44);txt(46,H-54,'WSG A-902  /  KYOTO INK',16,b=True);txt(46,H-83,t,24,b=True);txt(46,H-105,'R11 • R10 külső geometriából továbbvezetett ajánlati terv • minden méret mm • helyszínen nem felmért',11,RED)
 line(42,85,W-42,85);txt(46,62,'AJÁNLATKÉRÉSRE / FELMÉRÉSRE VÁR — NEM GYÁRTÁSI KIADÁS',12,RED,b=True);txt(46,42,'Méretforrás: R10 + geometry_lock_A902_v2b; belsők R11 tervezési javaslat. Nyomat/minta nem jóváhagyott.',9)
 txt(W-470,62,'2026.10.28.  |  '+scale,11);txt(W-470,42,f'KI-R11  |  N-{page:02d}  |  A2 fekvő, 100%-os nyomtatás',10)
def end():
 (O/f'svg/N-{page:02d}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="594mm" height="420mm" viewBox="0 0 {W} {H}">'+''.join(svg)+'</svg>');c.showPage()
def opening(x,y,w,h):line(x,y,x+w,y+h/2,dash=True);line(x+w,y+h/2,x,y+h,dash=True)
def hatch(x,y,w,h):
 rect(x,y,w,h,GRAY)
 for q in range(0,int(w+h),8):
  a=max(0,q-h);b=min(w,q);line(x+a,y+q-a,x+b,y+q-b,'#777',.35)
def img(im,x,y,w,h):
 buf=io.BytesIO();im.save(buf,format='PNG');data=buf.getvalue();c.drawImage(ImageReader(io.BytesIO(data)),x,y,w,h,mask='auto');svg.append(f'<image x="{x}" y="{H-y-h}" width="{w}" height="{h}" href="data:image/png;base64,{base64.b64encode(data).decode()}"/>')
mask=Image.open(P/'R06/artwork/INK-W01_mask.png').convert('L');printim=Image.new('RGB',mask.size,'#b6aa96');dark=Image.new('RGB',mask.size,'#292725');printim.paste(dark,mask=Image.eval(mask,lambda a:255-a))
# 1 overall front, directly dimensioned R10 geometry
x,y=100,220
title('Médiafal | színes homlokzat, frontosztás és grafika')
txt(100,1060,'A–A ELÖLNÉZET  1:10',13,b=True)
rect(x,y,3600*s,2880*s,'#faf9f5');
for off,w in [(0,720),(840,690),(1530,690),(2220,690),(2910,690)]:rect(x+off*s,y+150*s,w*s,400*s,'#454644')
rect(x+720*s,y+150*s,120*s,2730*s,'#222321')
for a,b in [(0,360),(360,720),(840,1530),(1530,2220),(2220,2910),(2910,3600)]:
 srcim=printim
 if a<720:
  srcim=Image.new('RGB',mask.size,'#6a655b');srcim.paste(dark,mask=Image.eval(mask,lambda a:255-a))
 crop=srcim.crop((int(a/3600*mask.width),0,int(b/3600*mask.width),mask.height));img(crop,x+(a+1.5)*s,y+551.5*s,(b-a-3)*s,2327*s);rect(x+(a+1.5)*s,y+551.5*s,(b-a-3)*s,2327*s)
opening(x+3*s,y+552*s,354*s,2324*s);opening(x+363*s,y+552*s,354*s,2324*s)
# screen center tied to panel; final bracket setting specified as proposed, not measured native
rect(x+1390*s,y+1000*s,1453*s,834*s,'#151719');txt(x+1500*s,y+1410*s,'TV 65″ / beállítási javaslat',12,'#ddd')
for xx,yy,X,Y in [(840,2865,3600,2865),(735,550,735,2880),(0,150,3600,150)]:line(x+xx*s,y+yy*s,x+X*s,y+Y*s,GOLD,2)
dh(x,y-24,[720,120,690,690,690,690]);dv(x-35,y,2880);dv(x+3600*s+22,y+150*s,400)
qx=1190;yy=1050
for h,t in [('01  LÁTVÁNY','A torony, a 120-as visszahúzás és a négy panelmező együtt3600. A világos felület nem kő: nyomtatott hordozó. A színek tájékoztatóak; mintával véglegesítendők.'),('02  FRONTOK','Torony2×357×2327; alsó1×717×397 +4×687×397. Névleges modulonként3mm hézag. Pántolás és ajtóvetemedés gyártói ellenőrzéssel.'),('03  GRAFIKA','R06 INK-W01_mask.png képi munkaforrás. R11-en folytonos koordinátával szemléltetve. Gyártási felbontás, vágójel, kifutó és ajtórés külön nyomdai jóváhagyás.'),('04  TV','1453×834mm befoglaló; a rajzi1000mm alsó él beállítási javaslat, nem az R10 képből felmért adat. A konzolhelyet ülőszemmagasság és gyári VESA alapján véglegesíteni kell.'),('05  KÖLTSÉGKÓD','KI-030:765500Ft; KI-031:350000Ft; KI-032:135000Ft. Összes1250500Ft becsült asztalos keret. Fény külön KI-114150000Ft. Új ajánlattal igazolandó.')]:
 txt(qx,yy,h,13,b=True);yy=note(qx,yy-24,t,420,12)-24
for i,(col,label) in enumerate([('#454644','M01 grafit jelölt'),(GREIGE,'M02 nyomathordozó'),('#e5dfd3','M03 belső világos lap')]):rect(1190+i*145,220,125,50,col);txt(1190+i*145,200,label,9)
end()
# 2 true interiors + plan
x,y=100,220;title('Médiafal | belső nézet, rekeszek és tárolókapacitás')
txt(100,1060,'A–A BELSŐ NÉZET  1:10',13,b=True)
rect(x,y+550*s,720*s,2330*s,'#f1eee7');
for off in [0,351,702]:hatch(x+off*s,y+550*s,18*s,2330*s)
for z in [550,2862]:hatch(x,y+z*s,720*s,18*s)
levels=[935,1320,1705,2090,2475]
for off in [18,369]:
 for z in levels:hatch(x+off*s,y+z*s,333*s,18*s)
 for k in range(6):txt(x+(off+20)*s,y+(650+k*385)*s,'polc / doboz',8)
for off,w in [(0,720),(840,690),(1530,690),(2220,690),(2910,690)]:
 rect(x+off*s,y+150*s,w*s,400*s,'#f1eee7')
 for dx in [0,w-18]:hatch(x+(off+dx)*s,y+150*s,18*s,382*s)
 for z in [150,532]:hatch(x+off*s,y+z*s,w*s,18*s)
 if off!=840:hatch(x+(off+18)*s,y+341*s,(w-36)*s,18*s)
 txt(x+(off+25)*s,y+250*s,'AV / szerviz' if off==840 else 'média / doboz',8)
rect(x+720*s,y+150*s,120*s,400*s,'#777');rect(x+840*s,y+550*s,2760*s,2330*s,'#fbfaf6');txt(x+1250*s,y+2200*s,'PANEL MÖGÖTT: KÁBELÚT / KONZOL',12)
line(x+1800*s,y+600*s,x+1800*s,y+1900*s,RED,1,True);rect(x+1650*s,y+600*s,300*s,200*s,None,RED);txt(x+1950*s,y+650*s,'levehető szervizablak: helye egyeztetendő',9)
dh(x,y-24,[720,120,690,690,690,690]);dh(x,y+2900*s,[18,333,18,333,18],s,False)
dv(x-35,y+550*s,2330);yy=1040
for h,t in [('T-01 / TORONY','2 rekesz,333mm elméleti tiszta szélesség;5-5 állítható polc. Polcméret331×320×18mm (2mm szerelési játék). A polcok10db,3,31folyóméter és1,059m² polcfelület; a fenéklap nincs beleszámolva.'),('A-01 / ALSÓ','5 önálló modul.1×684 és4×654mm tiszta szélesség. Első és utolsó3 modulban1-1 polc; az ablak felőli második helyett a840mm-nél kezdődő modul AV-szervizrekesz, polc nélkül.'),('HASZNÁLAT','Torony: könyvek, társasjáték, zárt tárolódoboz. Alsó: médiaeszköz és kábel, játékdoboz, távirányító. Tápegység mellett sem textil, sem papír nem tárolható.'),('NYITÁS','Torony kifelé nyíló két front. Alsó oldalra nyíló csillapított frontjavaslat. Ajtónyitás a kanapéval külön használati próbát igényel; nincs teljes használati PASS.'),('STÁTUSZ','Ezek R11 tényleges belső kiosztási javaslatok, még nem szerepelnek részletes alkatrészként az R10 Blender-modellben. A render nem mutatja a belsőt.')]:
 txt(1190,yy,h,13,b=True);yy=note(1190,yy-24,t,420,12)-23
end()
# 3 plan side, installation
x,y=100,735;title('Médiafal | alaprajz, oldalnézet és nyitási hely')
txt(100,1055,'B–B ALAPRAJZ / VÍZSZINTES METSZET  1:10',13,b=True)
rect(x,y+410*s,4000*s,90*s,'#777');
for off,w in [(0,720),(840,690),(1530,690),(2220,690),(2910,690)]:
 rect(x+off*s,y,w*s,400*s,'#deded8');line(x+off*s,y+18*s,x+(off+w)*s,y+18*s)
 # open front projected dashed, not arc certainty
 line(x+off*s,y,x+off*s,y-w*s,RED,1,True);line(x+off*s,y-w*s,x+(off+w)*s,y,RED,.6,True)
rect(x+720*s,y+180*s,120*s,220*s,'#484944');dh(x,y+550*s,[720,120,690,690,690,690]);dv(x-40,y,400)
txt(100,470,'Piros: nyitási helyigény sematikusan; a teljes modulfront sugara720 /690mm.',11,RED)
txt(100,450,'A rajz helyi bútoralaprajz, nem hitelesített lakásalaprajz. Falsík és falvég felmérendő.',11)
txt(1000,570,'C–C TORONY OLDALMETSZET  1:20',13,b=True)
# side smaller 1:20 to fit
ss=s/2;xx,yy=1020,135;rect(xx,yy+150*ss,400*ss,2730*ss,'#ece8df');hatch(xx,yy+550*ss,18*ss,2330*ss);line(xx+382*ss,yy+150*ss,xx+382*ss,yy+2880*ss)
for z in levels:line(xx+25*ss,yy+z*ss,xx+345*ss,yy+z*ss)
dv(xx-30,yy,2880,ss);dh(xx,yy-20,[382,18],ss);txt(220,350,'Oldalnézet kivételesen1:20',11)
for i,t in enumerate(['400mm teljes mélység =382mm korpusz +18mm front.','8mm hátfal süllyesztve / rögzítés gyártói részlettel.','320mm polcmélység: hely marad hátfalhoz és fogáshoz.','Torony külön falrögzítése; nem az alsó lebegő bútorra terheljük.','A statikus/asztalos határozza meg a konzolokat és a csavarokat.','Szállítás:3600mm fedlap1db vagy jóváhagyott illesztés;','lift/forduló ellenőrzés nélkül nem igazolt felhordhatóság.']):txt(220,325-i*22,t,11)
yy=1060
for h,t in [('FALHOZ IGAZÍTÁS','A modellfal4000mm; a kompozíció3600mm.300/100mm tervezett végmaradék nem szerelési tűrés. Mérendő3 magasságban szélesség, függő, derékszög, padló és ablakcsatlakozás.'),('NYITÁSI PRÓBA','Alsó frontok elé690–720mm forgási hely szükséges. A rajz ezt kijelöli, de nem állítja, hogy a kanapé mellett minden front teljesen nyitható. Ha ütközik: vasalatválasztás/oldalirány felülvizsgálat a külső osztás megőrzésével.'),('FÜGGÖNY','Fali sín Z2840; textil felső él2810, alsó15mm. A redőnyfedélhez hozzáférés és a csatlakozó torony/függöny gyűjtése helyszíni próba. Mennyezeti hűtő-fűtő mezőbe nincs engedélyezett rögzítés.')]:
 txt(1250,yy,h,13,b=True);yy=note(1250,yy-24,t,370,12)-28
end()
#4 details
title('Csomópontok | bonthatóság, fény és grafikai illesztés','1:2 / sematikus szerelési részletek')
ss=72/25.4/2
for xx,yy,label in [(100,680,'D01 / PANEL RÉTEGREND'),(900,680,'D02 / KÖZTES VISSZAHÚZÁS'),(100,260,'D03 / ALSÓ BÚTOR FÉNYE'),(900,260,'D04 / FRONT ÉS NYOMAT')]:txt(xx,yy+350,label,16,b=True)
# D01 cross
x,y=120,760;hatch(x,y,25*ss,150*ss);rect(x+25*ss,y,18*ss,150*ss,None);hatch(x+43*ss,y,18*ss,150*ss);line(x+61*ss,y,x+61*ss,y+150*ss,GREIGE,3);dh(x+25*ss,y-25,[18,18],ss)
for i,t in enumerate(['Meglévő fal: helyszíni teher-/anyagvizsgálat.','18mm szerelőlégrés; oldható rejtett függesztés.','18mm stabil hordozólap, matt kasírozott nyomat.','Kábelt nem szabad végleg befalazni / beragasztani.','Felső LED a profilban; nincs önálló világító panelél.']):txt(310,950-i*24,t,11)
#D02 depth reveal horizontal
x,y=910,830;rect(x,y,120*ss,18*ss,'#444');rect(x-45*ss,y,45*ss,120*ss,'#b2aaa0');rect(x+120*ss,y,100*ss,36*ss,GREIGE);rect(x+5*ss,y+18*ss,15*ss,15*ss,GOLD);dh(x,y-30,[120],ss);txt(1280,950,'FELÜLNÉZETI ELV',12,b=True)
for i,t in enumerate(['120mm látható sáv,','mélységi lépcső valós.','Oldható hátbetét.','LED profil15mm jelölt;','végleges profiladat kell.','Ragasztott fix takarás tilos','a szervizcsatlakozásnál.']):txt(1280,925-i*22,t,11)
#D03
x,y=120,280;hatch(x,y+150*ss,240*ss,18*ss);rect(x+200*ss,y+150*ss,18*ss,60*ss,'#444');rect(x+180*ss,y+137*ss,15*ss,13*ss,GOLD);line(x,y,x+240*ss,y);dv(x-30,y,150,ss)
for i,t in enumerate(['Bútor alsó él150mm a kész padlótól.','Alumínium profil + diffúzor: hőelvezetés.','Tápegység nem az alsó résbe szorítva,','hanem a hozzáférhető AV rekeszben.','Rögzítési méret statikai vizsgálattal.']):txt(510,550-i*25,t,11)
#D04
x,y=920,340;rect(x,y,95*ss,170*ss,GREIGE);rect(x+98*ss,y,95*ss,170*ss,GREIGE);line(x,y+60*ss,x+95*ss,y+130*ss,INK,7);line(x+98*ss,y+132*ss,x+193*ss,y+165*ss,INK,7);dh(x+95*ss,y-25,[3],ss)
for i,t in enumerate(['3mm hézag: a grafika megszakad.','Közös masterből kivágott nyomatok.','Élre fordulás / vágás mintázandó.','Fekete oldalél vagy grafit ABS jelölt.','Nyomdai kifutó: gyártó adja meg,','nem a3mm ajtórést kell kitölteni.']):txt(1240,580-i*24,t,11)
end()
#5 actual BOM not falsely precision
parts=[]
def part(id,what,n,a,b,t,mat,edge,note_='Tervezési darabméret; nem gyártási kiadás'):
 parts.append([id,what,n,a,b,t,mat,edge,note_])
part('TV01-S','Torony oldal/középosztó',3,2330,382,18,'M03','elöl1mm')
part('TV01-T','Torony tető/fenék',2,684,382,18,'M03','elöl1mm','Két szélső oldal közé; középosztó hossza végleges kötéstől függ!')
# correct middle should shorter
parts[0]=['TV01-S','Torony oldalak',2,2330,382,18,'M03','elöl1mm','Tető/fenék oldalak közé']
part('TV01-C','Torony középosztó',1,2294,374,18,'M03','elöl1mm')
part('TV01-P','Torony állítható polc',10,331,320,18,'M03','elöl1mm')
part('TV01-F','Torony front',2,2327,357,18,'M01+nyomat','körbe1mm','Nyomat és vetemedés gyártóval egyeztetendő')
part('TV01-H','Torony hátlap',1,2294,684,8,'M03','nem','Hátlap rögzítés és csatlakozás szerint pontosítandó')
part('TV02-S','Alsó oldalak',10,382,382,18,'M03','elöl1mm')
part('TV02-T1','720-as modul fenék',1,684,382,18,'M03','elöl1mm')
part('TV02-T2','690-es modul fenék',4,654,382,18,'M03','elöl1mm')
part('TV02-P1','720-as modul polc',1,682,320,18,'M03','elöl1mm')
part('TV02-P2','690-es modul polc',3,652,320,18,'M03','elöl1mm')
part('TV02-F1','Alsó front720',1,717,397,18,'M01','körbe1mm')
part('TV02-F2','Alsó front690',4,687,397,18,'M01','körbe1mm')
part('TV02-H1','Hátlap720',1,684,346,8,'M03','nem','Kötési mód szerint pontosítandó')
part('TV02-H2','Hátlap690',4,654,346,8,'M03','nem','AV modul hátlapja bontható, szellőzés méretezendő')
part('TV02-CAP','Összefüggő felső fedő',1,3600,400,18,'M01','látható1mm','Közös tető Z532..550; a382mm magas oldalakra ül. Nincs külön modultető.')
part('TV03-P','Dekor hordozópanel',4,2330,687,18,'M02','mintázandó')
part('GAP','Köztes sáv hátbetét',1,2330,120,18,'M01','körbe1mm')
title('Darabjegyzék | előzetes anyagkiírás és vasalatigény','Táblázat / nem szabásoptimalizált')
txt(60,1058,'A táblázat kész alkatrész-befoglalókat ad; élzárás levonása, horony, kötés és nyers szabás gyártói feladat.',12,RED)
cols=[60,200,580,635,715,795,865,1020];heads=['Azonosító','Megnevezés','Db','Hossz','Szél.','Vast.','Anyag','Él / megjegyzés']
for xx,h in zip(cols,heads):txt(xx,1040,h,12,b=True)
yy=1006
for r in parts:
 vals=[r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7]]
 for xx,v in zip(cols,vals):txt(xx,yy,v,10)
 line(60,yy-10,1600,yy-10,'#ccc');yy-=29
note(60,430,'Kiválasztott tetőelv:382mm magas oldalak +18mm közös tető =400mm teljes bútor. Fenéklap18mm; tiszta magasság346mm. Nincs külön modultető. A3600mm fedő illesztését és szállíthatóságát gyártó ellenőrizze; a névleges méretek felmérésig nem gyártási adatok.',1500,12)
for i,t in enumerate(['Vasalat:40db toronypolctartó +16db alsó polctartó, teherbírási jóváhagyással; rögzített tető/fenék kötése gyártói rendszer.','Frontok:2 magas +5 alsó ajtó; pánt/csillapító darabszám gyártói tömeg- és magasságtáblázatból, nem becsült csavarlista.','M01: grafit lap, EGGER U961 ST7 jelölt; M02: nyomathordozó a18mm lapon; M03: világos egyszínű belső laminált lap.','Polcfelület: torony1,059m²; alsó (682+3×652)×320=0,844m². Fenéklap, AV és köztes sáv nélkül.','A becsült1250500Ft asztalos keret új ajánlattal igazolandó. Nem bizonyított, hogy minden új belső részlet ezen belül elkészül.']):txt(60,340-i*30,t,12)
end()
#6 tables real cuts, three views
title('CF-01 + ST-01 | grafit asztalok, három nézet és szerkezet','1:5 / részletek 1:2')
ss=72/25.4/5
for x,w,d,h,id in [(100,700,450,350,'CF-01'),(1000,300,300,450,'ST-01')]:
 txt(x,1070,id+' / ZÁRT DOBOZTEST',16,b=True)
 yy=760;rect(x,yy,w*ss,h*ss,'#4c4d48');dh(x,yy-24,[w],ss);dv(x-30,yy,h,ss);txt(x,yy+h*ss+15,'ELÖLNÉZET',11,b=True)
 yy=385;rect(x,yy,w*ss,d*ss,'#52534e');dh(x,yy-24,[w],ss);dv(x-30,yy,d,ss);txt(x,yy+d*ss+15,'FELÜLNÉZET',11,b=True)
 xx=x+w*ss+65;yy=760;rect(xx,yy,d*ss,h*ss,'#3f413d');txt(xx,yy+h*ss+15,'OLDAL',11,b=True);dh(xx,yy-24,[d],ss)
 # inset feet schematic
 line(x+20*ss,760,x+(w-20)*ss,760,INK,3)
 for j,t in enumerate([f'Kész befoglaló{w}×{d}×{h}mm;18mm lap.',f'Tető1db:{w}×{d}; alj1db:{w-36}×{d-36}.',f'Hosszoldal2db:{w}×{h-18}; végoldal2db:{d-36}×{h-18}.','Lapillesztés: zárt doboz, rejtett kötés, körben1mm ABS.','Nem kő / nem valódi tömör fém. M01 grafit mintázandó.','Filctalp padlóvédelem; kész magasságba beleértendő.']):txt(x,290-j*23,t,11)
part('CF-T','CF tető',1,700,450,18,'M01','körbe1mm');part('CF-S','CF hosszoldal',2,700,332,18,'M01','látható1mm');part('CF-E','CF végoldal',2,414,332,18,'M01','látható1mm');part('CF-B','CF fenék',1,664,414,18,'M01','nem')
part('ST-T','ST tető',1,300,300,18,'M01','körbe1mm');part('ST-S','ST hosszoldal',2,300,432,18,'M01','látható1mm');part('ST-E','ST végoldal',2,264,432,18,'M01','látható1mm');part('ST-B','ST fenék',1,264,264,18,'M01','nem')
end();c.save()
with (O/'data/elozetes_alkatreszek.csv').open('w',encoding='utf-8-sig',newline='') as f:
 wr=csv.writer(f,delimiter=';');wr.writerow(['ID','Elem','Db','Hossz_mm','Szel_mm','Vast_mm','Anyag','Elzaras','Megjegyzes']);wr.writerows(parts)
(O/'data/kiadas.json').write_text(json.dumps({'revision':'KI-R11','scope':'nappali médiafal TV01/02/03 és CF01/ST01','source':'R10 + R06 ink master; a mintacsomag kizárólag formai referencia','pages':6,'status':'ajánlati/felmérési terv, nem gyártási kiadás','changes':'részletes belső javaslat, 3 nézet, metszet, csomópont, előzetes darabjegyzék','not_updated':'R10 Blender belső alkatrészei és élő Excel; új belső árak még nem igazoltak','open':['helyszíni felmérés','nyitási használati próba','vasalat/konzol méretezés','anyag/nyomat minta','közös fedlap illesztése és felhordhatósága']},ensure_ascii=False,indent=2))
print('R11 six sheets created')
