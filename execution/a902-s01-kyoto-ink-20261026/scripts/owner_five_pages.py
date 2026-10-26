from pathlib import Path
import json,collections,io
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from PIL import Image
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1];O=P/'outputs/A902_Kyoto_Ink_tulajdonosi_bemutato_5oldal.pdf';R=json.loads((P/'data/elemek.json').read_text());C=json.loads((P/'data/cost_snapshot_R02.json').read_text());T=json.loads((P/'data/render_manifest.json').read_text());D=json.loads((P/'data/design_R02.json').read_text());G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text())
for font,file in [('A','Arial.ttf'),('AB','Arial Bold.ttf')]:pdfmetrics.registerFont(TTFont(font,'/System/Library/Fonts/Supplemental/'+file))
W,H=A4;M=34;CW=W-2*M;ink=HexColor('#243b37');muted=HexColor('#59665e');paper=HexColor('#f7f4ee');stone=HexColor('#e9e2d7');taupe=HexColor('#b2a38e');rust=HexColor('#a44c35');green=HexColor('#66836e')
c=canvas.Canvas(str(O),pagesize=A4);c.setTitle('A-902 Kyoto Ink - Tulajdonosi bemutató, öt oldal');c.setAuthor('A-902 Kyoto Ink projekt');transcript=[]
def text(x,y,s,size=11,bold=False,col=ink):c.setFillColor(col);c.setFont('AB' if bold else 'A',size);c.drawString(x,y,s)
def para(x,top,s,width=CW,size=11,leading=None,col=ink,bold=False):
 st=ParagraphStyle('p',fontName='AB' if bold else 'A',fontSize=size,leading=leading or size*1.35,textColor=col)
 p=Paragraph(s,st);ww,hh=p.wrap(width,1000);p.drawOn(c,x,top-hh);transcript.append(s.replace('<b>','').replace('</b>',''));return top-hh

def box(x,y,w,h,color=stone):c.setFillColor(color);c.roundRect(x,y,w,h,min(8,h/2),stroke=0,fill=1)
def rule(y):c.setStrokeColor(taupe);c.setLineWidth(.6);c.line(M,y,W-M,y)
def begin(n,tag,title,subtitle=None):
 c.setFillColor(paper);c.rect(0,0,W,H,fill=1,stroke=0);text(M,809,'A-902  /  KYOTO INK',9,True);c.setFont('A',9);c.drawRightString(W-M,809,tag.upper());rule(796)
 y=para(M,778,title,CW,25,29,bold=True)
 if subtitle:y=para(M,y-12,subtitle,CW,11,15,col=muted)
 text(M,24,'R02 tervállapot | 2026.10.26. | Tulajdonosi döntés-előkészítő',8,col=muted);c.setFont('AB',9);c.drawRightString(W-M,24,f'{n} / 5');return y

def photo(cam,x,y,w,h):
 t=next(t for t in T if t['camera']==cam);im=Image.open(P/t['project_path']).convert('RGB');im.thumbnail((1500,1000));buf=io.BytesIO();im.save(buf,format='JPEG',quality=90);buf.seek(0)
 iw,ih=im.size;dw=min(w,h*iw/ih);dh=dw*ih/iw;c.drawImage(ImageReader(buf),x+(w-dw)/2,y+(h-dh)/2,dw,dh)

def smallcard(x,top,w,num,title,body):
 text(x,top,num,22,True,col=rust);y=para(x,top-15,title,w,13,17,bold=True);return para(x,y-10,body,w,10.5,14)

# 1: the appeal of this particular project, without implying the render is already buildable.
begin(1,'A lakás karaktere','Egy nyugodt otthon,<br/>erős személyiséggel.')
photo('12',M,390,CW,326);text(M,378,'Kiválasztott V3.3 nappali célkép. A megvalósítás részletei még egyeztetés alatt állnak.',8.5,col=muted)
w=(CW-32)/3
smallcard(M,348,w,'01','A tusgrafika adja<br/>a karakterét.','A nagy falkép és a TV-fal egy közös vizuális nyelvet kap. Kevés, jól elhelyezett hangsúly elég ahhoz, hogy a lakás felismerhető legyen.')
smallcard(M+w+16,348,w,'02','Este is jó lesz<br/>hazajönni.','A meleg fény, a puha textil és a grafit felületek együtt adják a hangulatot. A rejtett világítást valódi profilokból és elérhető szerelési helyekkel tervezzük.')
smallcard(M+2*(w+16),348,w,'03','A rend is része<br/>a látványnak.','A gardróbok, az előtéri tároló és az egyedi bútorok a hétköznapi tárgyaknak adnak helyet. A szép összkép akkor működik, ha használat közben is rendezhető.')
box(M,70,CW,90);para(M+15,145,'A projekt az egész otthonról szól.',CW-30,13,17,bold=True)
para(M+15,121,'Három háló, konyha, nappali-étkező, fürdők, előtér, közlekedő, WC és a teljes kültér. A terasz önálló pihenő- és étkezőhelyet kap; a jakuzzi megvalósíthatóságát külön kell igazolni.',CW-30,10.5,14)
c.showPage()

# 2: non-overlapping cost groups, straight from the existing register.
begin(2,'A pénz helye','Miért ennyire drága?','A 20,55 millió Ft a teljes lakás és kültér berendezési, szerelési és átadási előirányzata. Sok külön feladat összege, nem egyetlen nappali ára.')
metrics=[('Fő változat','20,55 M Ft','+2,55 M a kerethez képest'),('Takarékos javaslat','19,90 M Ft','+1,90 M a kerethez képest'),('Alapkeret','18,00 M Ft','+2,00 M külön tartalék')]
ww=(CW-20)/3
for j,(a,b,d) in enumerate(metrics):
 x=M+j*(ww+10);box(x,604,ww,83);text(x+12,667,a,9.5,True);text(x+12,641,b,18,True);text(x+12,620,d,8.5,col=rust if j<2 else muted)
trade=collections.defaultdict(int)
for a in R:trade[a['szakma']]+=a['mennyiseg']*a['egysegar']+a['szallitas']+a['szereles']+a['egyeb']
groups=[('Egyedi bútor és asztalosmunka',trade['Asztalos']),('Készbútor, bel- és kültérre',trade['Bútor']),('Jakuzzi, kert és terasz szakági tételei',trade['Kert és terasz']),('Gépek és elektronika',trade['Gépek']+trade['Elektronika']),('Világítás és villamos munkák',trade['Villamos'])];groups.append(('Textil, felületek és kapcsolódó feladatok',C['main']-sum(v for _,v in groups)));assert sum(v for _,v in groups)==C['main']
y=578
for label,value in groups:
 text(M,y,label,10.5);c.setFont('AB',11);c.drawRightString(W-M,y,f'{value/1e6:.2f}'.replace('.',',')+' M Ft');box(M,y-18,CW,7,stone);box(M,y-18,CW*value/max(v for _,v in groups),7,taupe);y-=42
para(M,312,'Az utolsó csoportban: textilek 1,33 M; falak és művészet 0,90 M; víz, üveg, tervezés, logisztika és kiegészítők együtt 1,80 M Ft. A kültéri bútor a készbútor sorban szerepel. Minden tételt egyszer számoltunk.',CW,9,12,col=muted)
rule(260)
para(M,246,'Mi hajtja leginkább az árat?',CW,13,17,bold=True)
para(M,221,'<b>A sok egyedi elem:</b> 33 tervezett szerkezetnél az anyag mellé belső kialakítás, vasalat, megmunkálás és beépítés társul. <b>A teljes tartalom:</b> a jakuzzi és kapcsolódó munkái önmagukban 2,00 M Ft-ot képviselnek. <b>A készre szerelt állapot:</b> sín, varrás, táp, csatlakozó, felhordás és próbaüzem is pénzbe kerül.',CW,10.5,14)
box(M,63,CW,87,ink);para(M+15,136,'A legfontosabb szám most a bizonytalanság.',CW-30,12,16,col=white,bold=True)
para(M+15,113,'Ellenőrzött webshop-termékár: 1,757 M Ft. Írásos beszállítói ajánlat: 0 Ft. Még becsült rész: 18,797 M Ft. A fő változat indikatív sávja 17,74-27,13 M Ft; az alsó érték nem keretígéret. A külön 2 M Ft tartalék érintetlen.',CW-30,10,13,col=white)
c.showPage()

# 3: existing timetable + paired risks and mitigation.
begin(3,'Idő és kockázat','Miért kell hozzá 17 hét?','Az idő jelentős része felmérésre, döntésre, gyártásra és szállításra megy el. Több feladat párhuzamosan haladhat, de a beépítéshez a megfelelő dolgoknak egyszerre kell készen lenniük.')
text(M,674,'Jelenlegi, feltételes ütem a felmérés elindításától',12,True)
x0=238;span=W-M-x0
for k in [0,5,10,15,17]:text(x0+span*k/17-4,648,str(k),9,col=muted)
rows=[('Felmérés, minták, ajánlat, döntés',0,5),('Gyártói rajzok és jóváhagyás',4,6),('Beszerzés és egyedi gyártás',5,14),('Villamos/víz és falak előkészítése',6,10),('Beépítés, textilek, próba, átadás',12,17)]
for j,(name,a,b) in enumerate(rows):
 yy=620-j*34;para(M,yy+7,name,190,10,13);box(x0+span*a/17,yy-8,span*(b-a)/17,14,green if j==4 else taupe)
para(M,438,'A kanapé korábban jelzett 8-9 hetes átfutása és az egyedi bútorok feltételezett 6 hetes gyártása fontos függőség. Egyik sem visszaigazolt vállalási határidő. A végső próba és hibajavítás is része a 17 hétnek.',CW,10,14,col=muted)
text(M,369,'Mi jöhet közbe, és hogyan fogjuk meg időben?',14,True)
cards=[('A valós méret eltér.','A konyhai közlekedő jelenleg 84 cm. A kisebb hálóban az íróasztal és az erkélyajtó ütközik.','Korai felmérés és az elrendezés lezárása, még gyártás előtt.'),('A termék később érkezik.','A webshop készletjelzése még nem igazolt magyar kiszállítás. Egy hiányzó fődarab az összképet is késleltetheti.','Írásos átfutás és előre egyeztetett helyettesítő.'),('A minta élőben más.','A képernyőn látott taupe szín, textúra vagy tusnyomat a helyszíni fényben eltérhet.','Kárpit- és felületminta, próbanyomat, majd egyetlen lezárt választás.'),('A terasz feltétele nem adott.','A jakuzzi terhe, beemelése és bekötése még nem igazolt. Az időjárás is korlátozhatja a munkát.','Statikus és üzemeltető bevonása, korai logisztikai egyeztetés.')]
cw=(CW-16)/2
for j,(title,why,act) in enumerate(cards):
 xx=M+(j%2)*(cw+16);top=348-(j//2)*143;box(xx,top-132,cw,132)
 yy=para(xx+12,top-12,title,cw-24,11,15,bold=True);yy=para(xx+12,yy-7,why,cw-24,9.8,13);para(xx+12,yy-7,'<b>Teendő:</b> '+act,cw-24,9.5,12.5)
c.showPage()

# 4: value judgement grounded in use; do not invent financial ROI.
begin(4,'Érték és választás','Megéri ennyit rákölteni?','Akkor lehet jó döntés, ha a kialakítás a saját életeteket teszi tartósan kényelmesebbé, és a teljes költség vállalható. A render szépsége önmagában ehhez kevés.')
# Complete apartment plan, directly from the same R02 geometry and furnishing records.
sc=20.8;ox=82;oy=490
for rs in G['rooms'].values():
 for x,y,X,Y in rs:c.setFillColor(stone);c.rect(ox+x*sc,oy+y*sc,(X-x)*sc,(Y-y)*sc,fill=1,stroke=0)
for name,bb in G['walls'].items():
 if bb[2]>1 or name.startswith('Plafon'):continue
 c.setFillColor(ink);c.rect(ox+bb[0]*sc,oy+bb[1]*sc,(bb[3]-bb[0])*sc,(bb[4]-bb[1])*sc,fill=1,stroke=0)
for u in D['units']+D['items']:
 if u['room'] in ['09','10','WPC','13'] or u['z']>1:continue
 w,dep=u['w']/1000,u['d']/1000
 if u['rot']==90:w,dep=dep,w
 c.setFillColor(taupe);c.rect(ox+u['x']*sc,oy+u['y']*sc,w*sc,dep*sc,fill=1,stroke=0)
for u in D.get('fixed_existing',[]):
 bb=u['bounds'];c.setStrokeColor(ink);c.setFillColor(white);c.rect(ox+bb[0]*sc,oy+bb[1]*sc,(bb[3]-bb[0])*sc,(bb[4]-bb[1])*sc,fill=1,stroke=1)
for x,y,label in [(.4,2,'05.2'),(.7,7.6,'Master'),(4.5,5.4,'Nappali'),(7.7,7.6,'Étkező'),(8.9,2.1,'Konyha'),(6.6,1.35,'Előtér'),(3.6,3.25,'Közl.'),(5.65,3.0,'WC'),(3.8,2.1,'06.1'),(12,6,'05.3'),(14.8,6.7,'06.2')]:
 tw=pdfmetrics.stringWidth(label,'AB',7.5);c.setFillColor(paper);c.rect(ox+x*sc-2,oy+y*sc-3,tw+4,11,fill=1,stroke=0);text(ox+x*sc,oy+y*sc,label,7.5,True)
text(34,587,'Erkély',8,col=muted);text(190,683,'A terasz felé',8,col=muted)
text(M,467,'A teljes lakás vázlata. Felmérés és a kisebb háló elrendezésének lezárása még szükséges.',8,col=muted)
x=440;y=537;sc=.034
c.setFillColor(stone);c.rect(x,y,3300*sc,400*sc,fill=1,stroke=0);c.setFillColor(taupe);c.rect(x+2600*sc,y+400*sc,700*sc,2330*sc,fill=1,stroke=0);c.setFillColor(stone);c.rect(x,y+400*sc,2600*sc,2330*sc,fill=1,stroke=0);c.setStrokeColor(ink)
for k in range(1,4):c.line(x+k*650*sc,y+400*sc,x+k*650*sc,y+2730*sc)
c.setFillColor(ink);c.rect(x+580*sc,y+800*sc,1452.9*sc,834*sc,fill=1,stroke=0);text(x,522,'TV-fal: 3,30 m',8.5,True);text(x,509,'Vázlat az R02 tervből',7.5,col=muted)
text(M,448,'Amit érdemes megvédeni a döntések során',13,True)
y=para(M,425,'<b>A lakás karakterét:</b> a TV-fal, a nagy tusgrafika, az összehangolt felületek és a meleg esti fény együtt adják a Kyoto Ink lényegét. Ezeknél a részletek találkozása fontosabb, mint a márkanév önmagában.',CW,11,15)
y=para(M,y-11,'<b>A mindennapi használatot:</b> kényelmes ülés, jó matrac, működő tároló, használható munkahely és hozzáférhető szerelvények. Ezek előnyét naponta érzékelni lehet, nem csak a fotón.',CW,11,15)
y=para(M,y-11,'<b>A javíthatóságot:</b> elérhető tápegység, cserélhető fényforrás és hozzáférhető szifon. Egy szép felület mögött is karbantartható megoldásra van szükség.',CW,11,15)
rule(y-18)
y=para(M,y-32,'Mikor érdemes még megállni egy döntés előtt?',CW,13,17,bold=True)
y=para(M,y-10,'Ha a 18 millió Ft valódi felső határ, további tételes egyeztetés kell: a mostani takarékos javaslat csak 654 500 Ft-tal olcsóbb, és még 1,90 M Ft-tal keret felett van. Ha egy drága részletet alig használnál, kérj rá külön változatot, mielőtt elköteleződsz.',CW,11,15)
box(M,63,CW,78,stone);para(M+14,127,'A saját válaszod három kérdésből áll össze.',CW-28,12,16,bold=True);para(M+14,104,'Melyik három elemet szeretnéd minden nap használni vagy látni? Melyik kompromisszum zavarna tartósan? Mekkora összeg vállalható kényelmesen? Eladásiár-növekedést vagy pénzügyi megtérülést a jelen terv nem bizonyít.',CW-28,10,13)
c.showPage()

# 5: new owner-facing acceleration scenario, explicitly conditional and preserving scope.
begin(5,'Cselekvési terv','Hogyan lehet korábban kész?','A gyorsítás legjobb esélye a korai, összehangolt döntés. A gyártási időt, a száradást és az ellenőrzéseket nem rövidítjük le bizonyíték nélkül.')
box(M,611,CW,75,ink);text(M+15,661,'17 hét  →  15 hetes célváltozat',18,True,col=white);para(M+15,641,'Feltételes szervezési forgatókönyv, körülbelül 2 hét nyerési lehetőséggel. Nem vállalt átadási dátum; a beszállítói visszaigazolások döntik el, tartható-e.',CW-30,10.3,14,col=white)
actions=[('Ma / tulajdonos','Rögzíts három prioritást és a költségkeret valódi határát. Jelölj ki egy döntéshozót és heti 30 perc közös egyeztetést.'),('1. hét / tervező + szakemberek','Egy összehangolt felmérésen tisztázzák a konyhát, a kisebb háló munkahelyét, a kiállásokat, a küszöböt és a terasz feltételeit.'),('1-2. hét / beszerző + tulajdonos','A mintákat és az összehasonlítható ajánlatokat párhuzamosan készítsék elő. A hosszú átfutású fődarabokhoz kérjenek írásos szállítási időt.'),('3. hét / tulajdonos','Lezárt ár, változat és feltételek alapján dönts a kritikus beszerzésekről. Rendelés kizárólag külön engedéllyel; bizonytalan méretű egyedi bútort még ne indítsanak.'),('3-5. hét / gyártó + tervező','Zárják le a gyártói rajzokat és az anyagmintákat. A jóváhagyott részcsomagok előkészítése indulhat, ha műszakilag függetlenek a nyitott részektől.')]
y=584
for j,(when,action) in enumerate(actions,1):
 text(M,y,str(j).zfill(2),16,True,col=rust);yy=para(M+35,y+4,when,CW-35,10.5,14,bold=True);yy=para(M+35,yy-4,action,CW-35,10.3,13.5);y=yy-17
rule(y+4)
y=para(M,y-9,'Mitől jön ki a 15 hét?',CW,12,16,bold=True)
y=para(M,y-8,'A hosszú átfutású beszerzés az 5. helyett a 3. héten indulhat, így 9 hét esetén a 12. hétre érkezhet. A gyártói rajzok a 3-5., az egyedi gyártás az 5-11., az előkészítés az 5-9. héten haladhat. Beépítés: 11-13. hét, a megérkezett részekkel. Üveg és textilek: 13-14. hét. Próba, javítás, átadás: 14-15. hét.',CW,10.2,13.5)
y=para(M,y-8,'<b>A feltétel:</b> korán visszaigazolt gyártási és szerelési kapacitás, gyors mintadöntés, legfeljebb 1-2 hetes végső üveg/textil átfutás és nincs jelentős feltárási hiba. Ha ezek nem teljesülnek, a 17 hét is újratervezendő. A teljes tartalom megmarad; a tartalékot nem használjuk fel gyorsításra automatikusan.',CW,9.8,13)
# Compact source note also explains that this is a presentation update, not a changed implementation release.
para(M,61,'Forrás: R02 élő költségregiszter, rajzcsomag, ütemterv és Blender-ellenőrzés. Az ötlapos bemutató a korábbi egyoldalas tulajdonosi összefoglaló helyébe lép. A 15 hetes változat új javaslat, nem módosítja automatikusan a műszaki tervet vagy a rendelési státuszt.',CW,7.8,10,col=muted)
c.showPage();c.save();assert len(PdfReader(O).pages)==5
(P/'outputs/A902_Kyoto_Ink_tulajdonosi_bemutato_szoveg.txt').write_text('\n\n'.join(transcript),encoding='utf-8')
(P/'data/owner_five_pages_basis.json').write_text(json.dumps(dict(date='2026-10-26',design_revision='KI-V33-R02',source_budget=C,cost_groups=groups,base_duration_weeks=17,accelerated_target_weeks=15,accelerated_status='UNCONFIRMED_OWNER_ACTION_SCENARIO',procurement_authorized=False,scope_reduction=False,questions=['Miért ennyire drága?','Miért ennyi idő?','Mi jöhet közbe?','Mi lesz különleges és miért?','Megéri ennyit rákölteni?','Hogyan lehet hamarabb kész?']),ensure_ascii=False,indent=2))
print('Created',O,'5 pages')
