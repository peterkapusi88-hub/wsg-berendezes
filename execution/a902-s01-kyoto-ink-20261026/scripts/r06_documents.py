import json,math,html,re,io
from PIL import Image
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,A3,landscape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1];O=P/'R06';D=json.loads((O/'data/design_R06.json').read_text());B=json.loads((O/'data/budget_R06.json').read_text());arts={x['id']:x for x in json.loads((O/'data/artwork_manifest.json').read_text())}
font='/System/Library/Fonts/Supplemental/Arial.ttf';pdfmetrics.registerFont(TTFont('A',font));pdfmetrics.registerFont(TTFont('AB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
BaseCanvas=canvas.Canvas
class VectorCanvas(BaseCanvas):
 def __init__(self,*a,**kw):
  super().__init__(*a,**kw);self.svg=[];self.svgpage=0;self.vector='R06_valtozott_szerkezetek' in str(a[0])
 def color(self,v):
  try:return '#%02x%02x%02x'%tuple(round(x*255) for x in v.rgb())
  except:return '#333333'
 def rect(self,x,y,w,h,stroke=1,fill=0):
  if self.vector:self.svg.append(f'<rect x="{x}" y="{self._pagesize[1]-y-h}" width="{w}" height="{h}" fill="{self.color(self._fillColorObj) if fill else "none"}" stroke="{self.color(self._strokeColorObj) if stroke else "none"}"/>')
  return super().rect(x,y,w,h,stroke,fill)
 def line(self,x,y,X,Y):
  if self.vector:self.svg.append(f'<line x1="{x}" y1="{self._pagesize[1]-y}" x2="{X}" y2="{self._pagesize[1]-Y}" stroke="{self.color(self._strokeColorObj)}" stroke-width="{self._lineWidth}"/>')
  return super().line(x,y,X,Y)
 def drawString(self,x,y,text,*a,**kw):
  if self.vector:self.svgtext(x,y,text,self._fontsize)
  return super().drawString(x,y,text,*a,**kw)
 def svgtext(self,x,y,t,size):self.svg.append(f'<text x="{x}" y="{self._pagesize[1]-y}" font-family="Arial" font-size="{size}" fill="#30332f">{html.escape(str(t))}</text>')
 def drawPath(self,path,stroke=1,fill=0,fillMode=None):
  if self.vector and fill:
   nums=[];parts=[]
   for token in ' '.join(path._code).split():
    try:nums.append(float(token));continue
    except:pass
    if token in ['m','l'] and len(nums)>=2:parts.append(('M' if token=='m' else 'L')+f'{nums[-2]},{self._pagesize[1]-nums[-1]}');nums=[]
    elif token=='h':parts.append('Z')
    elif token not in ['n']:nums=[]
   if parts:self.svg.append('<path d="'+' '.join(parts)+'" fill="'+self.color(self._fillColorObj)+'"/>')
  return super().drawPath(path,stroke,fill,fillMode)
 def showPage(self):
  if self.vector:
   self.svgpage+=1;w,h=self._pagesize;(O/f'drawings/R06_lap_{self.svgpage:02}.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="420mm" height="297mm" viewBox="0 0 {w} {h}">'+''.join(self.svg)+'</svg>');self.svg=[]
  return super().showPage()
canvas.Canvas=VectorCanvas
style=ParagraphStyle('p',fontName='A',fontSize=10,leading=14,textColor='#30332f')
def pretty(t):
 t=re.sub(r'(?<=\d),(?=\d{3}(?:\D|$))',' ',str(t))
 t=re.sub(r'(\d)(Ft|mm|cm|liter|millió|m²|m\b)',r'\1 \2',t)
 t=re.sub(r'\b(A|a|két|külön)(?=\d)',r'\1 ',t)
 return t
def para(c,text,x,y,w,size=10):
 text=pretty(text)
 if getattr(c,'vector',False):
  line='';yy=y-size
  for word in text.split():
   if pdfmetrics.stringWidth(line+' '+word,'A',size)>w:
    c.svgtext(x,yy,line,size);yy-=size*1.4;line=word
   else:line=(line+' '+word).strip()
  if line:c.svgtext(x,yy,line,size)
 st=ParagraphStyle('p',parent=style,fontSize=size,leading=size*1.4);p=Paragraph(html.escape(text).replace('\n','<br/>'),st);ww,hh=p.wrap(w,1000);p.drawOn(c,x,y-hh);return y-hh-10
def image(c,path,x,y,w,h):
 if Path(path).exists():
  im=Image.open(path).convert('RGB');im.thumbnail((1600,1600));b=io.BytesIO();im.save(b,format='JPEG',quality=90);b.seek(0);c.drawImage(ImageReader(b),x,y,w,h,preserveAspectRatio=True,anchor='c')
def txt(c,s,x,y,size=10,bold=False):c.setFont('AB' if bold else 'A',size);c.setFillColorRGB(.12,.14,.13);c.drawString(x,y,pretty(s))
def page(c,title,num,W,H,sub='R06 · 2026-10-27 · milliméter · ajánlatkérési / felmérési terv, nem gyártási kiadás'):
 c.setFillColorRGB(.94,.93,.89);c.rect(0,0,W,H,fill=1,stroke=0);txt(c,'KYOTO INK / A–902',35,H-35,12,True);txt(c,title,35,H-66,22,True);txt(c,sub,35,H-88,9);txt(c,f'{num:02d} / KI-R06',W-130,23,9)
def rect(c,x,y,w,h,fill='#b8ad99'):
 c.setFillColor(fill);c.setStrokeColorRGB(.2,.2,.18);c.setLineWidth(.65);c.rect(x,y,w,h,fill=1,stroke=1)
def dim(c,x,y,X,Y,label):
 c.setStrokeColorRGB(.25,.25,.25);c.setLineWidth(.5);c.line(x,y,X,Y);c.line(x-3,y-3,x+3,y+3);c.line(X-3,Y-3,X+3,Y+3);txt(c,label,(x+X)/2+4,(y+Y)/2+5,9)
def front(c,id,x,y,w,h):
 a=arts[id];sx=w/a['w_mm'];sy=h/a['h_mm'];rect(c,x,y,w,h,'#b7aa91')
 if id=='INK-W01':rect(c,x,y,700*sx,h,'#5a5146')
 c.saveState();path=c.beginPath();path.rect(x,y,w,h);c.clipPath(path,stroke=0)
 if getattr(c,'vector',False):
  cid='clip'+str(len(c.svg));c.svg.append(f'<defs><clipPath id="{cid}"><rect x="{x}" y="{c._pagesize[1]-y-h}" width="{w}" height="{h}"/></clipPath></defs><g clip-path="url(#{cid})">')
 for polys,color in [(a['polygons'],'#24211e'),(a.get('holes',[]),'#b7aa91')]:
  c.setFillColor(color)
  for poly in polys:
   if id=='INK-W01' and color=='#b7aa91':c.setFillColor('#5a5146' if sum(q[0] for q in poly)/len(poly)<700 else '#b7aa91')
   p=c.beginPath();p.moveTo(x+poly[0][0]*sx,y+h-poly[0][1]*sy)
   for xx,yy in poly[1:]:p.lineTo(x+xx*sx,y+h-yy*sy)
   p.close();c.drawPath(p,fill=1,stroke=0)
 c.restoreState()
 if getattr(c,'vector',False):c.svg.append('</g>')
def plan(c,x,y,s,room=None):
 for name,rs in D['rooms'].items():
  if room and name!=room.replace('.','_'):continue
  for X,Y,XX,YY in rs:
   rect(c,x+X*s,y+Y*s,(XX-X)*s,(YY-Y)*s,'#f7f4ec')
  if not room:
   X,Y,XX,YY=rs[0];txt(c,name.replace('_',' '),x+X*s+2,y+Y*s+8,5)
 for u in D['units']:
  if room and u['room']!=room:continue
  if not room and not(0<=u['x']<=16.4 and 0<=u['y']<8.95):continue
  w,d=u['w']/1000,u['d']/1000
  if u['rot']==90:w,d=d,w
  rect(c,x+u['x']*s,y+u['y']*s,w*s,d*s,'#b0a58c');txt(c,u['id'],x+u['x']*s+2,y+u['y']*s+4,6)
 for it in D['items']:
  if room and it['room']!=room:continue
  if not room and not(0<=it['x']<=16.4 and 0<=it['y']<8.95):continue
  rect(c,x+it['x']*s,y+it['y']*s,it['w']/1000*s,it['d']/1000*s,'#d9d2c5')
W,H=landscape(A3);c=canvas.Canvas(str(O/'drawings/R06_valtozott_szerkezetek.pdf'),pagesize=(W,H))
page(c,'Médiafal: a jóváhagyott kompozíció megőrzése',1,W,H)
front(c,'INK-W01',65,190,660,466)
for a in [140,270,400,530]:c.line(65+a,190,65+a,656)
rect(c,65,110,660,80,'#48433b')
for a in [140,270,400,530]:c.line(65+a,110,65+a,190)
rect(c,321,270,290.58,166.8,'#171918');dim(c,65,85,725,85,'3300 =700+4×650');dim(c,750,110,750,656,'2730 felső él; alsó z150')
y=650
for t in ['TV-01 / TV-02 / TV-03 · KI-030…032','A torony az étkező felőli700mm mezőben marad. A panelen és a toronyfronton folytonos tusmotívum fut.','Torony400mm mély; panel36mm; alsó bútor400mm mély/400mm magas/z150mm.4×650mm panelmező,3mm illesztések.','18mm korpusz,19mm front; 8mm hát. Kábelút a levehető hát mögött; a TV rögzítése teherbíró falhoz, nem csak dekorpanelhez.','A sötét torony színét külön mintán kell beállítani; a grafika itt újrarajzolt próbaváltozat, nem eredeti nyomdai master.','Felső/toronyoldali/alsó LED: külön alu profil, diffúzor és hozzáférhető tápegység. A korábbi világítási költségsorokban szerepel; nincs újraszámítva.','R05 belső kiosztás és szerelési lapok érvényben. Nyomtatás előtt 1:1 keresztillesztési próba a torony és a falsík között.'] :y=para(c,t,800,y,345,11)
c.showPage()
for num,uid,aid,count in [(2,'WN-01','INK-WN',6),(3,'WS-01','INK-WS',4)]:
 u=next(a for a in D['units'] if a['id']==uid);page(c,u['name']+' / külső és belső',num,W,H);s=.16;w=u['w']*s;h=2837*s;front(c,aid,55,175,w,h)
 for k in range(1,count):c.line(55+k*w/count,175,55+k*w/count,175+h)
 if uid=='WS-01':
  for k in range(count):rect(c,55+(k+1)*w/count-8,175+850*s,2,900*s,'#252523')
 dim(c,55,145,55+w,145,str(u['w'])+' teljes szélesség');dim(c,35,175,35,175+h,'2837 front')
 xx=590;ss=.16
 for bay in u['cp3_bays']:
  bx=xx+bay['offset']*ss;bw=bay['module_w']*ss;rect(c,bx,175,bw,2840*ss,'#ddd6c7')
  for z in bay['shelves_mm']:c.line(bx+3,175+z*ss,bx+bw-3,175+z*ss)
  for z in bay['rails_mm']:c.setLineWidth(2);c.line(bx+5,175+z*ss,bx+bw-5,175+z*ss);c.setLineWidth(.6)
  for z in bay['drawer_z']:rect(c,bx+5,175+z*ss,bw-10,140*ss,'#aaa28f')
  txt(c,bay['purpose'][:26],bx,650,8)
 y=125
 y=para(c,f"Kapacitás megőrizve: {u['capacity']['rail_m']}m akasztórúd / {u['capacity']['shelf_m2']}m² polc / {u['capacity']['drawer_l']}liter fióktér. Tervi nettó tér; nem garantált ruhadarabszám.",55,y,1050)
 para(c,'18mm korpusz,19mm hosszú MDF front,8mm hát. A2837mm ajtó nem szabható2800mm nyerslapból. Merevítő/pántszám és nulla benyúlású fióknyitás gyártói méretezést igényel. A belső világítás és lift R05 rekeszlapjai megmaradnak.',55,y,1050)
 c.showPage()
page(c,'BED-01 / felnyíló tárolóágy – ütközést kiváltó terv',4,W,H)
rect(c,80,250,505,450,'#e1d9c8');c.line(80,475,585,475);dim(c,80,225,585,225,'2020 külső hossz');dim(c,60,250,60,700,'1800 külső szélesség')
for yy in [280,505]:rect(c,100,yy,465,180,'#c8bea7');txt(c,'Tárolórekesz / közös fedél alatt',115,yy+85,12)
rect(c,670,260,404,60,'#ded4bf');rect(c,672,320,400,56,'#eee7d7');dim(c,650,260,650,376,'300váz+280matrac')
y=660
for t in ['KI-043 · előirányzat250000Ft + KI-044 matrac229900Ft','A célkép alacsony, világos kárpitozott teste megmarad. Az oldalfiókok helyett felfelé nyíló tároló teszi lehetővé a két éjjeli megtartását.','Javasolt szerkezet:18mm rétegelt lemez váz, középső hosszgerenda, egyetlen, kétoldalt vezetett közös emelőkeret, az180cm-es egybefüggő matrac alatt. Látható kárpit huzatmintából; szellőzőfenék.','Két tervezett840×1900×220mm tárolóüreg: összesen702liter geometriai tér, a vasalat levonása előtt. Tényleges kapacitás a választott mechanikával kisebb.','Emelővasalat SKU, gázteleszkóp erő, terhelés, becsípődésvédelem és nyitási görbe még nyitott. A fejvégnél szükséges előreemelő mozgást a gyártónak igazolnia kell. Ezek nélkül nem gyártható.','A580mm teljes alvómagasságot a tulajdonossal próbán ellenőrizni kell; fejvég és lámpahely ehhez igazodik.']:y=para(c,t,670,y,430,11)
c.showPage()
page(c,'Konyha / egységes kődekor és valós használati hely',5,W,H)
rect(c,90,260,292,124,'#beb4a1');rect(c,90,552,320,124,'#beb4a1');dim(c,430,384,430,552,'840 szabad munkasáv');rect(c,220,384,120,120,'#d2ab82');dim(c,450,504,450,552,'240 nyitott gép mellett')
rect(c,90,135,820,92,'#c7bfae')
for at in [292,612,792]:c.line(90+at,135,90+at,227)
txt(c,'4100×920×38 nyerslap:1460+1600+900+vágási ráhagyások; a darabok620mm mélyek',90,112,10)
y=680
for t in ['K-08/K-09 · EGGER F243 ST76 Candela márványhatású laminátum','A széles920mm lapot kell árazni. A kedvezőbb600mm lap nem éri el a620mm tervezett pultmélységet.','1460×620 és1600×620 pult,900×620 oldalzárás. A38mm él a renderben vékonyabbnak tűnhet: ez dokumentált eltérés.','Tervi szabásból három hossz3960mm; 4100mm táblán140mm marad a szélezésre és fűrészrésre. Erezetfordulás a vízesés-élnél nem automatikusan folytonos.','A mosogatógép teljesen nyitva nem hagy átjárót. Oldalról történő rakodás javasolt, nem egyidejű áthaladás. Megmarad a teljes pultmélység és a főzőlap helye.','A lap150000Ft csomagkeret:96750lap+53250szabás/kivágás/él előirányzat. Hátfal100000Ft. Kötések, főzőlap hővédelme, vízzárás gyártói ellenőrzésre vár.']:y=para(c,t,620,y,480,11)
c.showPage()
page(c,'06.2 fürdő / T07 részletek és geometriai határ',6,W,H)
rect(c,80,250,270,420,'#bc9e73')
for k in range(30):rect(c,80+k*6,250,3,420,'#927247')
c.line(260,250,260,670)
for z in [380,500,620]:c.line(260,z,350,z)
dim(c,80,225,350,225,'900 =600front+300fülke');dim(c,60,250,60,670,'1400; alsó él1300')
y=680
for t in ['B62-WC / KI-R06-01 · 220000Ft beépített előirányzat','900×200×1400mm;18mm nedvességálló korpusz,19mm front,10mm lamella,8mm hát. Zárt600mm rekesz3állítható polccal;300mm nyitott fülke.','Belső polc564×173mm,3db:0.293m². Fülke282×173mm,3szint:0.146m². Papír, tartalék kozmetikum, vendégtörölköző; nem nagy gép tárolására.','Táp száraz, levehető szervizhelyen. Fülkefény alu profilban, diffúzorral. A WC öblítőtartály szervizét sem ajtó, sem ragasztott burkolat nem zárhatja el.','Tálca a hiteles modellben északi1780×850mm. A javított1000mm üveg a déli él keleti részén,780mm névleges belépővel. Üveges felmérés szükséges.','A T07 ág mintás falának és akasztóinak pontos képi helye nem fér össze bizonyítottan a zuhanyzónával. Vízálló grafikai változat készülhet; padot és ruhát oda nem helyezünk el jóváhagyás nélkül.','ART-B62:110000Ft; RAD-B62:120000Ft előirányzat. Pontos radiátormodell és nyomtatott üvegrendszer még nem kiválasztott.']:y=para(c,t,520,y,580,11)
c.showPage()
page(c,'05.3 dolgozó / 180cm vendégágy megtartva',7,W,H)
s=110;ox=-10.7*s+70;oy=-4*s+220;plan(c,ox,oy,s,'05.3');dim(c,ox+12.31*s,oy+5.95*s,ox+12.31*s,oy+6.10*s,'150')
y=660
for t in ['Változás: ágyY4250→4150mm; székY6550→6700mm. ÉjjeliX14025,Y5920mm.','A1800mm fekvőszélesség és a1800mm gardrób nem csökken.600mm székkihúzás után150mm marad az ágyig; ez nem átjáró.','Az ágy, íróasztal és gardrób mérete megmarad; az éjjeli kikerül a szék hátrahúzási sávjából.','A futtatott Blender-vizsgálat eredménye külön naplóban. Az ajtókat mintavételezett mozgással vizsgáljuk; fogantyúk és tényleges tokméret felmérésre várnak.','A tervezési befoglaló és a gyártói névleges méret nem helyszíni felmérés. A rajz és az R06modell azonos koordinátákat használ.']:y=para(c,t,640,y,450,12)
c.showPage();c.save()
# Product and visual decision book, deliberately explicit about nonidentity.
c=canvas.Canvas(str(O/'products/R06_termek_es_latvany_egyeztetes.pdf'),pagesize=A4);W,H=A4
products=[('Lennon / KI-036','lennon_1.jpg','800000Ft · SKU DEQ21WES12329-168260','238×180×68cm; széles karok, szövött taupe. A modell fotó és gyári méret alapján készült, nem gyári3D. A képi párnázottság és szín nem garantált.'),('Toni160 / KI-028','toni_1.jpg','259990Ft · DEQ19WES60483-225182','160×90×75cm,25mm lap, két hajlított lapláb. A központi tömblábas változatot nem szabad renderelni.'),('Eamy / KI-029','eamy_1.jpg','6×75180Ft korábbiHUFár · C0100003HE12','55×53×75cm, ülés46cm. Kőris háttámla, szürke zsenília, fekete acél. A friss magyar szállítási ár nincs visszaigazolva.'),('Somar / KI-109','somar_1.jpg','260000Ft meglévő csomagelőirányzat · L00148FA05','Ø76×36cm búra. A tényleges laposabb, bordás forma legyen a renderen. Hue izzó befoglalása és fénypróbája szükséges.'),('Rondo / KI-117','rondo_1.jpg','2×10990Ft +24000Ft Hue-előirányzat','Ø20×20cm · 85264. Fehér talp, a célkép sötét talpához képest eltérés. Opálüveg; az izzó alakja/beférése ellenőrizendő.'),('Konyhai kőhatás / KI-011–012','worktop_1.jpg','250000Ft pult+hátfal csomagelőirányzat','F243 ST76 laminátum. Nem természetes kő; mintaismétlés, vágott élek és38mm vastagság dokumentált kompromisszum.')]
for j,(title,photo,price,desc) in enumerate(products,1):
 page(c,title,j,W,H,'R06 · konkrét jelölt, nem megrendelés');image(c,O/'products'/photo,45,340,505,360);txt(c,price,40,295,12,True);para(c,desc,40,265,510,12);para(c,'Forrásoldalak, lekérési idő és fájlhash: R06/sources/source_manifest.json. Webshopár nem írásos ajánlat, készletjelzés nem visszaigazolt magyar szállítás.',40,150,510,10);c.showPage()
c.save()
# Exactly5page owner brief.
c=canvas.Canvas(str(O/'owner/A902_R06_tulajdonosi_5oldal.pdf'),pagesize=A4);W,H=A4
page(c,'Egy karakteres, használható otthon',1,W,H,'Tulajdonosi összefoglaló · KI-R06 · 2026-10-27');image(c,O/'targets/T01_W01_nappali.png',35,410,525,315)
y=380
for t in ['A fő karaktert megtartjuk: a tusgrafikás médiafal, a nagy művészeti felület, az alacsony taupe kanapé, a meleg fény és a mennyezetig kihasznált gardróbok adják az összhangot.','A képeken látható hangulathoz konkrét bútorokat, anyagokat és saját gyártási megoldásokat rendeltünk. A kép nem méretbizonyíték: a konyhai és fürdőszobai eltérést a valós helyhez kell igazítani.','A mostani csomag előrelépés a kivitelezés felé, de még nem gyártásra jóváhagyott terv. A grafikák méretezett próbák, a modellek között fotó alapján felépített változatok is vannak.']:y=para(c,t,40,y,510,12)
c.showPage();page(c,'Miért ennyi az ára?',2,W,H)
y=710
for t in [f"Teljes várható összeg: {B['main']:,}Ft. Tételes takarékos változat: {B['economy']:,}Ft. A18milliós célhoz a teljes változatból még {B['gap']:,}Ft hiányzik.",f"Becsült sáv: {B['low']:,}–{B['high']:,}Ft. Ez nem statisztikai garancia, hanem a költségsorok bizonytalansági sávjainak összege. A külön2milliós tartalékból0Ft-ot használtunk fel.",'Nem csak a látható bútorokat fizetjük meg. A gardróbbelsők, vasalatok, fények, falelőkészítés, szerelés, gépek, teljes kültér és jakuzzi is a projekt része. Ezeket nem töröltük ki a keret kedvéért.','A friss matracár30100Ft-tal alacsonyabb. A kisebb gömblámpapár10000Ft-tal drágább; az új ágymechanika60100Ft, a déli magas front80000Ft többletbecslés. A T07fürdőrészletek450000Ft külön előirányzatot kaptak.','Webshopár státuszú sorok:2 372 340 Ft; írásos ajánlat:0 Ft; becslés és tájékoztató ár:22 110 550 Ft. A webshopáras csomagok szerelése és szállítása sem automatikusan fix. Az Excel külön mutatja az árforrásokat.','A18milliót most csak igazolatlan árcsökkentéssel lehetne kijelenteni. Először azonos műszaki tartalmú ajánlatokat kérjünk; tartalomelhagyásról csak utána döntsünk.']:y=para(c,t,40,y,510,12)
txt(c,'A tényleges terv egyszerűsített berendezési alaprajza',40,335,11,True);plan(c,40,50,27)
c.showPage();page(c,'Miért kell idő, és mi jöhet közbe?',3,W,H)
y=710
for t in ['A3–4hónap a felmérés, minták és rendelési jóváhagyások lezárásától értendő. Nincs még visszaigazolt gyártási vagy szállítási dátum.','1–2.hét: egy közös felmérés, elektromos/vizes ellenőrzés, szín- és kárpitminták, nyomtatási próba.2–4.hét: összehasonlítható ajánlatok és gyártói részletek lezárása.','4–10.hét: egyedi bútorok gyártása, készbútorok szállítása, helyszíni előkészítés.10–14.hét: beépítés, textilek, világítás és gépek beüzemelése.14–16.hét: hibajavítás és átadás.','Fő kockázat a hosszú gardróbajtók gyárthatósága, a felnyíló ágy vasalata, a színminták eltérése, valamint a terasz terhelési és bekötési feltétele. A jakuzzi sem méretben, sem szakágilag nincs végleg lezárva.','A konyha840mm sávja nyitott mosogatógéppel nem átjáró. A fürdő célképén száraznak mutatott felület a tervben zuhanyzónával találkozik. Ezeket a következő rendernek is őszintén kell mutatnia.']:y=para(c,t,40,y,510,12)
c.showPage();page(c,'Mi lesz benne különleges – és megéri?',4,W,H);image(c,O/'targets/T04_Master_eszak.png',35,430,525,290)
y=405
for t in ['A látványos rész a folytonos tusmotívum és a rétegzett, meleg fény. A mindennapokban a rejtett tárolás, a jól rendezett szekrénybelső és a következetes anyaghasználat ad értéket.','Az északi mastergardrób3.35m akasztórudat,2.036m² polcot és436.914liter tervi fiókteret ad. A déli sekély szekrény cipőnek, táskának és háztartási eszköznek marad;5.202m² polccal és96.4liter fiókkal.','A két külön tároló megmarad a korábbi kapacitásterv szerint: AT8-01 fagyasztó és tartalékkészlet; T-0-26 bicikli, bőrönd és ritkább holmik. Nem helyettesítik a napi lakáson belüli tárolást.','Megérheti, ha ezt a megjelenést és tárolási szintet hosszú távon használjátok. Ingatlanérték-növekedést vagy megtérülést nem igazoltunk; a drágább megoldás önmagában nem értékesebb.']:y=para(c,t,40,y,510,12)
c.showPage();page(c,'Hogyan lehet hamarabb kész?',5,W,H)
y=710
for t in ['Egyetlen közös felmérési alkalomra szervezzük az asztalos, villanyszerelő és vizes szakember kérdéseit. Minden kritikus falról, nyílásról, kiállásról és szervizfedélről készüljön méret és fotó.','A mintákat együtt kell nézni: nappali fényben és a tervezett esti fény mellett. A falgrafikából1:1 részletet, a frontból és kárpitból fizikai mintát kérjünk. Így nem a beépítéskor derül ki a színeltérés.','Azonos rajzrevíziót és tétellistát adjunk az ajánlattevőknek. A korán lezárt készbútorok szállítási idejét és a hosszú frontok nyersanyagát ellenőrizzük először. Ajánlatkérés és rendelés külön tulajdonosi engedéllyel történjen.','Három tulajdonosi döntés:1. A18milliós cél mellett mely látványelemek maradjanak érinthetetlenek?2. Elfogadható-e az oldalfiók helyett felnyíló masterágy?3. A fürdő geometriájához igazított vízálló grafika elfogadható-e a képi akasztós fal helyett?','Következő ellenőrzési pont: azonos tartalmú árajánlatok, felmérési lapok és minták után a költség és a gyárthatóság közös lezárása. Addig csak feltételes tervrender készülhet; a szebb képet nem tekintjük műszaki bizonyítéknak.']:y=para(c,t,40,y,510,12)
c.save();assert len(PdfReader(O/'owner/A902_R06_tulajdonosi_5oldal.pdf').pages)==5
print('Created7pageA3revision,6pageproductbook,5pageownerbrief')
