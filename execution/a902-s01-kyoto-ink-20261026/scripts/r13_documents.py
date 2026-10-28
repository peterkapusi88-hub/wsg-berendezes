from pathlib import Path
import json,math,collections
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A3,A4,landscape
from reportlab.lib.units import mm
from reportlab.graphics.barcode.code128 import Code128
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1];O=P/'R13_muhely';parts=json.loads((O/'data/parts.json').read_text());holes=json.loads((O/'data/holes.json').read_text());prog=json.loads((O/'data/programs.json').read_text())
pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('B','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
W,H=landscape(A3);c=canvas.Canvas(str(O/'rajzok/TV_R13_reszletes_rajzkonyv.pdf'),pagesize=(W,H));page=0
def txt(x,y,s,size=11,b=False,color='#263331'):
 c.setFillColor(color);c.setFont('B' if b else 'A',size);c.drawString(x,y,str(s))
def wrap(x,y,s,width,size=11):
 line=''
 for word in s.split():
  nxt=(line+' '+word).strip()
  if pdfmetrics.stringWidth(nxt,'A',size)>width:txt(x,y,line,size);y-=size*1.4;line=word
  else:line=nxt
 if line:txt(x,y,line,size);y-=size*1.4
 return y
def line(x,y,u,v,color='#465854',lw=.6):c.setStrokeColor(color);c.setLineWidth(lw);c.line(x,y,u,v)
def hdr(title,subtitle=''):
 global page
 page+=1;c.setStrokeColor('#bdc7c0');c.rect(25,25,W-50,H-50);txt(42,H-49,'KYOTO INK / A-902 / TV-MODUL / R13',12,True);txt(42,H-79,title,23,True)
 if subtitle:txt(42,H-101,subtitle,11)
 txt(42,43,'TERVEZÉSI ÉS MŰHELYI EGYEZTETŐ KIADÁS / NEM GYÁRTÁSRA JÓVÁHAGYOTT',10,True,'#9a492e');txt(W-230,43,f'2026.10.28. | mm | {page:02d}',10)
def img(name,x,y,w,h):c.drawImage(str(O/'audit'/name),x,y,w,h,preserveAspectRatio=True,anchor='c',mask='auto')
def dim(a,b,label,dy=0):
 x,y=a;u,v=b;line(x,y,u,v);line(x-3,y-3,x+3,y+3);line(u-3,v-3,u+3,v+3);txt((x+u)/2+6,(y+v)/2+6+dy,label,10)
hdr('Az asztalosnak átadható új modell','54 lapalkatrész | 293 tényleges CAD-furat | 34 aktív MPR-tervezet | 54 darabazonosító')
img('belso.png',36,142,780,570)
y=700
for s in ['A kép a natív AutoCAD DWG-ből exportált megmunkált testekből készült. Nem generatív látványterv.', 'A színek anyagcsoportot jelölnek. A tusgrafika és a jóváhagyott színminta nem része ennek a megmunkálási ábrának.', 'A két narancsszínű alsó front kiemelt szerelési helyzetben van. Nem állítjuk, hogy ebben a helyzetben használható a szobában.', 'A többi nyitott ajtó ellenőrző póz; nem a Blum-pánt tényleges kinematikai modellje.', 'Első megnyitás: TV_R13_belso.dwg. Minden lap külön ID-rétegen, saját KYOTO_INK azonosítóval.']:
 y=wrap(845,y,s,300,12)-22
txt(42,102,'A furatokat az AutoCAD kivonta; a számított és natív nettó térfogat: 362 409 016,9693 mm³.',12,True)
c.showPage()
hdr('Összeállítás, szerelési sorrend és méretlánc')
img('robbantott.png',35,200,720,510)
y=700
for title,body in [('01 / Rögzített méretlánc','Szélesség 3600. Torony 720 + köztes sáv 120 + 4×690. Alsó zóna Z150-550, felső Z550-2880. A paneles falsík 418 mm-ig ér; a frontos alsó bútor 403 mm mély.'),('02 / R12 javítása','A frontok 3 mm-rel előrébb kerültek a nyomási hézaghoz. Az alsó köztes sáv új 117×380×18 mm betétet kapott. Az előző 53 azonosító megmaradt; egy új ID került hozzá.'),('03 / Előszerelés','Oldal/fenék/tető csapos kötései: J01-J26, 78 db Ø8×30 csap, 156 páros furat. Tíz toronypolc és négy alsó polc: 56 polctartó-hely.'),('04 / Sorrend','Korpuszok száraz összepróbája; pánttalp, polctartó, front próbaszerelése; falrögzítési rendszer lezárása; végső helyszíni beépítés. A 3600 mm fedlap felhordását és gépútját előre ellenőrizni kell.'),('05 / Még nem teljes','A falfüggesztők, hátlaprögzítések, LED-szerelvények és a vasalatok teljes 3D testmodellje még nincs lezárva. Ezeket a lapmodell nem helyettesíti.')]:
 txt(790,y,title,12,True);y=wrap(790,y-20,body,350,11)-17
txt(50,151,'A robbantott nézet eltolt alkatrészeket mutat; méretet az összeállítási adatból és alkatrészlapból vegyél.',11)
c.showPage()
hdr('Pánt, csap és polctartó: konkrét fúráskép')
img('pant_reszlet.png',45,340,515,350)
y=710
for title,body in [('Pánt','Blum 70T3550.TL, rugó nélküli 110°; talp 173H7100, 0 mm. Torony: 5 db/ajtó; alsó 1., 2., 5. front: 2 db/ajtó. Összesen 16 pánt és 16 talp a jelenlegi fúrt változatban.'),('Csésze és ráütés','Ø35, mélység 13; TB 5,5; csészeközép az éltől 23; névleges ráütés 16,5. Rögzítőcsavarok: 45 középtávolság, 9,5 eltolás. Talp: 37 mm az első korpuszéltől, 32 mm furattávolság.'),('Előfúrási javaslat','A Ø2,5×10 csavar-előfurat tervezői próbaérték. Nem a gyártó által minden lapanyagra jóváhagyott furat. A tényleges csavar, lap és forgácsolási beállítás próbája szükséges.'),('Polctartó','Ø5×8 vakfurat, polconként 4 hely; kétoldalt fúrt 18 mm középosztónál 2 mm maradó középanyag. A polctartó felfekvési geometriáját és terhelhetőségét beszerzés előtt egyeztetni kell.'),('Nyomásra nyitás','Toronyhoz 2 hosszú TIP-ON 956A1004 + 956A1201 adapter; a három kijelölt alsó nyílóajtóhoz rövid változat. A nyitók pontos rögzítőfuratai még nem szerepelnek a 293 furatban.')]:
 txt(600,y,title,12,True);y=wrap(600,y-20,body,540,11)-18
wrap(45,280,'Forrás: Julius Blum termékadatlap 70T3550.TL; Catalogue2022/2023 75,146,172-173. https://www.hpponline.co.uk/DocumentHandler/1459757/70t3550-tl-product-data-sheet.pdf ; https://publications.blum.com/2022/catalogue/en/75/',1070,10)
wrap(45,220,'A képen valódi CAD-kivonás látható. A pántdarabszám és a kötés terhelési alkalmassága továbbra is a tényleges fronttömeg, hordozóanyag és műhelyvizsgálat alapján zárható le. A furat létezése nem teherbírási bizonyíték.',1070,12)
c.showPage()
hdr('Alsó 3-4. rekesz: a tolóajtós megoldás méretezett vizsgálata','AJÁNLATKÉRÉSI ALTERNATÍVA / nincs beépítve a fő DWG-be vagy az élő projektfőösszegbe')
# Front / section diagram from S10 dimensional chain.
x0=65;y0=480;sc=.47
c.setFillColor('#d9d3c5');c.setStrokeColor('#4a4a43');c.rect(x0,y0,1380*sc,400*sc,fill=1)
for xx in [1.5,692]:c.setFillColor('#746e65');c.rect(x0+xx*sc,y0+1.5*sc,686.5*sc,397*sc,fill=1)
dim((x0,y0-22),(x0+1380*sc,y0-22),'1380 mm teljes páros modul')
txt(x0+80,y0+90,'686,5 ×397 ×18',12,True,'#ffffff');txt(x0+400,y0+90,'686,5 ×397 ×18',12,True,'#ffffff')
txt(x0+270,y0+205,'4 mm középső hézag',11)
txt(65,412,'Névleges méretlánc a gyártói képletekkel',13,True)
rows=[('Belső szélesség LI','1380 -2×18 =1344'),('Frontszélesség TL','(1344 -4)/2 +16,5 =686,5'),('Belső magasság LHI','397 -18 -44 -16,5 =318,5'),('Középosztó','18 mm; felső első kivágás 70×80, belső R20'),('Alsó vasalat helye','230 mm mély fenéktér; szerelési hozzáférés és alátámasztás'),('Nyitás feltétele','Középen elhelyezett fogás; fogantyú nélküli működés nem igazolt')]
y=380
for a,b in rows:txt(65,y,a,11,True);txt(265,y,b,11);y-=32
ys=700
for s in ['Salice Slider S10: egy síkban záródó, oldalra eltolható pár. A 687 mm-es eredeti frontokhoz képest darabonként 0,5 mm eltérés; a középső rés 3 helyett 4 mm.', 'A gyári rendszerhez két önálló korpusz helyett közös páros szerkezet, megemelt fenék és bevágott középosztó szükséges. A polcokat új szélességre kell szabni.', 'A 18 mm-es, 686,5×397 mm-es front becsült laptömege 700 kg/m³ feltételezéssel 3,43 kg, a mechanika 10 kg/ajtó határa alatt. Ez nem tényleges mérés.', 'Az asztal felé 100 mm-es feltételezett teljes mozgási sávval a jelenlegi modellben 37 mm marad. A gyári teljes kinematikát és a fogás helyigényét még igazolni kell; nincs funkcionális PASS.', 'A mechanika alsó takarása és a fényvonal összehangolása szükséges. Ha ez rontja a kívánt lebegő megjelenést, más nyitási változatot kell választani. Nem adunk helyette rejtett látványkompromisszumot.']:
 ys=wrap(790,ys,s,350,11)-19
wrap(65,145,'Forrás: Salice S10 szerelési útmutató, 3. és7-9. oldal. sources/Salice_S10_gyartoi_szereles.pdf. Ez méretezett alternatíva; a végleges profilrendelés, furatkiosztás és beépítési ár még nincs kiadva.',1060,11)
c.showPage()
hdr('Műhelyi adatkapcsolat és gyártási lezárás')
y=705
for a,b in [('Darab és revízió','A közös darabazonosítók megmaradtak. A címke új kulcsa R13:darabID, a program neve darabID_R13_A vagy _B. Így az R12 befoglalóprogram nem keveredik az új fúrásokkal.'),('Aktív MPR','A felhasználó kérésére 34 fájl 293 furatművelete EN=1 és ??=1. Saját visszaolvasó ellenőrizte a koordinátákat és az aktiválást. Ez nem woodWOP5 megnyitási vagy NC-szimulációs bizonyíték.'),('A/B befogás','A B oldal a rajzi U-tengely körüli fordítás: V_B = szélesség -V_A. A két program külön befogás. A gépi nullpont, ütköző, vákuumos alátámasztás és lehetséges átfordítás ellenőrizendő.'),('Furat vs. marás','A fájlok fúrási makrókat tartalmaznak. A Ø60 AV átvezetés tényleges fúróval vagy kontúrmarással készítendő; nincs ellenőrzött marószerszám vagy megírt marópálya. F_=STANDARD a gép saját adatbázisára támaszkodik.'),('Helyi keresés','SQLite adatbázis + címkekereső: a beolvasott revíziós ID-hez a megfelelő DXF és MPR-tervezet tartozik. Ismeretlen ID-re leáll. Nem történt Livewood/woodWOP adatbázis-import és gépre küldés.'),('Felmérés','A3600/2880/403 méretek tervadatok. A fal síkja, sarkai, padlószint, kiállások, szerelési hozzáférés és felhordási út nincs újra felmérve. Ezeket a műhelynek tételesen vissza kell mérnie.'),('Minták','Grafit lap/él; panelhordozó és nyomat; ragasztó/lakk kompatibilitás; fényprofil-próba. A CAD sematikus színe nem anyagminta-jóváhagyás.'),('Rögzítés és költség','Falfüggesztési rendszer és hátlaprögzítés nincs lezárva; teljes teherátadási terv nélkül nincs gyártási kiadás. Ebben a csomagban nincs új igazolt beszállítói ár, ezért a18 milliós teljes projektkeret teljesülése nem bizonyított.')]:
 txt(50,y,a,12,True);y=wrap(245,y,b,880,12)-26
c.showPage()
# Part sheets: every face and actual hole coordinates, no invented machining program approval.
for p in parts:
 hs=[h for h in holes if h['part']==p['id']]
 groups=[hs[i:i+24] for i in range(0,len(hs),24)] or [[]]
 for gi,group in enumerate(groups):
  hdr(p['id']+' / '+p['name'],f'{p["x"]} × {p["y"]} × {p["t"]} mm | {p["material"]} | lap {gi+1}/{len(groups)} | {len(hs)} furat')
  rot=p['x']>p['y']*1.5;xx=p['y'] if rot else p['x'];yy=p['x'] if rot else p['y'];s=min(470/xx,460/yy);ox=90;oy=210
  def xy(u,v):return (ox+(p['y']-v)*s,oy+u*s) if rot else (ox+u*s,oy+v*s)
  c.setFillColor('#e6e1d7');c.setStrokeColor('#4a5955');c.rect(ox,oy,xx*s,yy*s,fill=1)
  for h in hs:
   u,v,w=h['local_UVW'];x,y=xy(u,v);a=h['local_axis'];col='#ad3e30' if a[2]<0 else '#3266a2' if a[2]>0 else '#298153';c.setStrokeColor(col)
   if a[2]:c.circle(x,y,h['diameter']*s/2,fill=0)
   else:line(x,y,*xy(u+a[0]*h['depth'],v+a[1]*h['depth']),col,1)
  dim((ox,oy-22),(ox+xx*s,oy-22),f'{xx}');dim((ox-24,oy),(ox-24,oy+yy*s),f'{yy}')
  txt(70,156,'A felület vetülete. Piros: A; kék: B átvetítve; zöld: élirány.',10)
  txt(70,136,'A rajz illesztett arányú. A DXF 1:1 mm. U/V/W a táblázat szerint.',10)
  txt(70,116,'Vastagság: '+str(p['t'])+' mm; élkód és nyersméret műhelyben zárandó.',10)
  cols=[610,658,730,801,863,917,967,1037]
  for x,t in zip(cols,['Furat','U','V','W','Ø','Mélység','Oldal','Tengely']):txt(x,706,t,10,True)
  y=684
  for h in group:
   a=h['local_axis'];side='A' if a[2]<0 else 'B' if a[2]>0 else 'ÉL'
   vals=[h['id'],*[f'{v:g}' for v in h['local_UVW']],f'{h["diameter"]:g}',f'{h["depth"]:g}',side,','.join(map(str,a))]
   for x,v in zip(cols,vals):txt(x,y,v,10)
   line(607,y-6,1130,y-6,'#d9dfda',.3);y-=18
  y=min(y-15,235)
  f=p['frame'];y=wrap(610,y,f'O={f["origin"]}; U={f["U"]}; V={f["V"]}; A normál={f["outward_A"]}. Összeállítási XYZ, mm.',515,10)-10
  y=wrap(610,y,'MPR: '+', '.join(Path(q['path']).name for q in prog if q['part']==p['id']) if hs else 'Ehhez a darabhoz nincs kiadott fúrási makró. Ez nem bizonyítja, hogy nincs további művelet.',515,10)-10
  wrap(610,y,'Furatforrás: data/furatjegyzek.csv. Pánt/polctartó/csap és AV funkció soronként az Excelben. A tervadatok és az aktív program tervezési státuszúak.',515,10)
  c.showPage()
c.save()
# Labels include revision to prevent retrieving an obsolete R12 program.
lc=canvas.Canvas(str(O/'cimkek/TV_R13_cimkek_A4.pdf'),pagesize=A4)
for i,p in enumerate(parts):
 if i and i%10==0:lc.showPage()
 x=(5+105*(i%2))*mm;y=(297-23.5-((i%10)//2+1)*50)*mm;lc.setStrokeColor('#aaaaaa');lc.rect(x,y,95*mm,50*mm)
 for dy,t,n,b in [(44,p['id'],12,True),(38,'R13 | '+p['material'],10,True),(32,f'{p["x"]} ×{p["y"]} ×{p["t"]} mm KÉSZ TERV',10,False),(26,'A/B tájolás: alkatrészlap szerint',9,False),(21,'C élkód: NYITOTT',9,False),(16,'AKTÍV MPR-TERV / NEM GYÁRTÁSI KIADÁS',7,True)]:
  lc.setFont('B' if b else 'A',n);lc.setFillColor('#222222');lc.drawString(x+3*mm,y+dy*mm,t)
 Code128('R13:'+p['id'],barWidth=.18*mm,barHeight=8*mm,humanReadable=False).drawOn(lc,x+2*mm,y+5*mm)
 lc.setFont('A',6);lc.drawString(x+3*mm,y+1.7*mm,'R13:'+p['id'])
lc.save()
print(json.dumps({'drawing_pages':len(PdfReader(O/'rajzok/TV_R13_reszletes_rajzkonyv.pdf').pages),'label_pages':len(PdfReader(O/'cimkek/TV_R13_cimkek_A4.pdf').pages)}))
