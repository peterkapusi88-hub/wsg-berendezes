from pathlib import Path
import html
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
P=Path(__file__).resolve().parents[1];O=P/'R10';W,H=landscape(A3);c=canvas.Canvas(str(O/'drawings/W01_R10.pdf'),pagesize=(W,H));pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));svg=[]
def text(x,y,t,size=11):
 c.setFillColorRGB(.12,.13,.13);c.setFont('A',size);c.drawString(x,y,t);svg.append(f'<text x="{x}" y="{H-y}" font-family="Arial" font-size="{size}">{html.escape(t)}</text>')
def rect(x,y,w,h,color):
 c.setFillColor(color);c.setStrokeColorRGB(.2,.2,.2);c.rect(x,y,w,h,stroke=1,fill=1);svg.append(f'<rect x="{x}" y="{H-y-h}" width="{w}" height="{h}" fill="{color.hexval()}" stroke="#333"/>')
def line(x,y,X,Y):
 c.setStrokeColorRGB(.2,.2,.2);c.line(x,y,X,Y);svg.append(f'<line x1="{x}" y1="{H-y}" x2="{X}" y2="{H-Y}" stroke="#333"/>')
from reportlab.lib.colors import HexColor
D=HexColor('#4b4b49');G=HexColor('#b5aea1');L=HexColor('#eeeeea');B=HexColor('#292b2b');scale=.16;x0=45;y0=230
text(40,800,'W01 / TV-01–03 · KI-R10 · Médiafal helyreállítási javaslat',20)
text(40,777,'2026-10-28 · mm · Tervi geometria alapján · FELMÉRÉSRE ÉS GYÁRTÓI EGYEZTETÉSRE VÁR',11)
for y,w in [(0,720),(840,690),(1530,690),(2220,690),(2910,690)]:rect(x0+y*scale,y0+150*scale,w*scale,400*scale,D)
rect(x0+720*scale,y0+150*scale,120*scale,400*scale,B)
rect(x0,y0+550*scale,720*scale,2330*scale,D);line(x0+360*scale,y0+550*scale,x0+360*scale,y0+2880*scale)
rect(x0+720*scale,y0+550*scale,120*scale,2330*scale,B)
for k in range(4):rect(x0+(840+k*690)*scale,y0+550*scale,690*scale,2330*scale,G)
# TV indicative existing screen position on same source wall: centre Y6.27.
rect(x0+(1920-726.45)*scale,y0+900*scale,1452.9*scale,834*scale,B)
line(x0,y0-18,x0+3600*scale,y0-18);text(x0+250,y0-36,'3600 teljes kompozíció')
for a,b,label in [(0,720,'720'),(720,840,'120'),(840,3600,'2760 = 4 × 690')]:
 line(x0+a*scale,725,x0+b*scale,725);line(x0+a*scale,718,x0+a*scale,732);line(x0+b*scale,718,x0+b*scale,732);text(x0+(a+b)*scale/2-12,739,label,10)
text(45,168,'Felülnézet / mélységek',13)
rect(45,87,720*scale,400*scale,D);rect(45+720*scale,87+364*scale,120*scale,18*scale,B);rect(45+840*scale,87+364*scale,2760*scale,36*scale,G)
text(45,67,'Torony:400 mély; panel:36; 120 széles visszahúzott sáv. A TV külön falikonzolon.',10)
notes=['TERVI ELHELYEZÉS','W01: Y4050–8050 =4000mm.','Bútor: Y4350–7950 =3600mm.','Marad: délen300 / északon100mm.','Nem helyszíni felmérésből származik.','','FŐ SZINTEK','Alsó bútor: Z150–550.','Felső mező: Z550–2880.','Torony felső rész:2330 magas.','Teljes látható torony:2730 magas.','A korábbi szöveg2500mm-e helyett','a kiválasztott célképre illesztett javaslat.','','OSZTÁS ÉS NYITÁS','Torony:2×360 felső ajtó,3mm hézag.','Alsó:720 +120 szervizbetét +4×690.','Felső panel:4×690,3mm munkahézag.','Az infill süllyesztett, levehető.','Nyitott frontok végleges söprése külön','gyártói ellenőrzést igényel.','','KÖLTSÉGSOROK','KI-030 panel/torony765500Ft becslés.','KI-031 alsó350000Ft becslés.','KI-032 szerelés135000Ft becslés.','KI-034 konzol és KI-114 fény külön.']
y=740
for t in notes:text(680,y,t,11);y-=20
text(40,30,'Nem gyártási kiadás. A sík grafika és a 120mm fényrés részlete külön mintázandó; nincs kőrelief.',10)
(O/'drawings/W01_R10.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 {W} {H}">'+''.join(svg)+'</svg>')
c.showPage();svg.clear();text(40,800,'W01 · Anyag, szerelési részlet és mintázás',20)
lines=[
'KI-030 / KI-031 – egyedi gyártás, ajánlatkérési specifikáció, nem végleges gyártási jóváhagyás.',
'',
'Korpusz:18mm bútorlap; hát8mm; front18mm;1mm ABS a látható éleken. Egységes matt grafit.',
'Javasolt dekor: EGGER U961 ST7 Graphite Grey. Valós gyártói dekor, fizikai minta és HU elérhetőség kell.',
'Torony: két felső front, oldalanként gyártó által méretezett pántkiosztás; süllyesztett fogás/élfogás.',
'Alsó tároló: lefelé nyíló vagy pántolt front végleges vasalatát a konzollal és a használati térrel kell egyeztetni.',
'Csak rejtett falikonzolos rögzítés, teherbíró falréteghez. Rögzítő méretét a helyszíni fal és terhelés dönti el.',
'',
'Panel:18mm stabil hordozó + névleges18mm szerelő/légrés, összes36mm. Leakasztható, rejtett kötés.',
'A nyomat matt sík nyomat; a finom rostos anyaghatás a hordozóból és a nyomtatott tónusból származik.',
'Gyártói hordozójelölt: DreamScape Terralon, finom szemcsés, digitálisan nyomtatható falburkolat.',
'Ez nem jóváhagyott szín-/textúraegyezés és nem magyar beszállítói ajánlat. Más igazolt hordozó is összevethető.',
'Panelél: a nyomat az élhez igazítva, szükséges nyomdai kifutással; a vágási jel a jóváhagyott panelrajzból készüljön.',
'A torony működő ajtóin nem hidalható át a hézag; a grafika közös koordinátából, külön panelenként készüljön.',
'Erezetirány: egyszínű lapnál nem alkalmazandó; nyomathordozó iránya és a grafika koordinátája egységes.',
'',
'120mm köztes sáv: grafit hátsó betét, oldható hozzáféréssel. A sáv nem egy fényesre festett frontcsík.',
'LED:2,76m felső /2,33m függőleges /3,60m alsó =8,69m. Rendelési keret10m, vágási és készletkorlát vizsgálandó.',
'Rejtett alumínium profil opál diffúzorral; tápegység a hozzáférhető, szellőző alsó rekeszben; D16 forrás egyeztetendő.',
'Kábelút a panel mögött, a TV mögötti pontok és konzol külön szerelősávban; bontás nélkül hozzáférhető fedél.',
'',
'Függöny: javasolt fali sín Z2840, textil felső él kb2810; padló felett 15mm, a belső padló felett; felmérésre vár.',
'A teljes textilhossz véglegesítése helyszíni padló/küszöb- és ráncolásmérés után. A modell nem szabásminta.',
'Fal/lintelmerev rögzítés, levehető konzol; a redőnyfedél nyitási útja és a hűtő-fűtő mennyezet helyzete ellenőrzendő.',
'',
'Minták: min.300×300mm grafitlap; kb500×500mm nyomat két hordozón; illesztett kétpaneles tusvonal-próba.',
'Vizsgálat: nappal és2700K alatt tónus, fényesség, rostosság; ajtórésen át folytonosság; ragasztás/él felválás.',
'Nyomdai profil, ragasztó és felületi védelem csak a választott hordozó/nyomtató dokumentációja szerint.',
'',
'Források (2026-10-28): www-static.egger-cdn.com/en/furniture-interior-design/decors/U961_7',
'dreamscapewalls.com/product/terralon/ – gyártói műszaki lehetőség; ár- és színjóváhagyás nem következik belőle.'
]
y=763
for t in lines:text(40,y,t,12);y-=21
c.save();print('PDF and editable SVG saved')
