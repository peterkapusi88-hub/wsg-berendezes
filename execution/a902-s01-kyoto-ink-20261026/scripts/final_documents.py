from pathlib import Path
import json,csv,hashlib,textwrap
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak
from reportlab.lib.styles import ParagraphStyle
from pypdf import PdfReader
from xml.sax.saxutils import escape
P=Path(__file__).resolve().parents[1];D=json.loads((P/'data/design_R02.json').read_text());R=json.loads((P/'data/elemek.json').read_text());G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text());C=json.loads((P/'data/cost_snapshot_R02.json').read_text());B=json.loads((P/'blender/validation_R02.json').read_text());targets=json.loads((P/'data/render_manifest.json').read_text());pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('ArialB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
ink=HexColor('#263b39');taupe=HexColor('#bbae9e');red=HexColor('#a44a35');pale=HexColor('#f2efe8');num=lambda v:f'{v:,.0f}'.replace(',',' ')
# Explicit visual deviations, no unsupported similarity percentage.
raw=[('V01','Cam02/12 W01','TV-01/02/03','3300mm alsó,700mm magas,2600mm panel; valódi helyből méretezve, nem perspektívából','KI-030–032','Frontosztás és nyomat megváltozik; mintajóváhagyás kell'),('V02','Cam12 W02','ART-02','2100×2880,3×700 textilpanel; saját SVG tusgrafika','KI-123,131–133','A grafika újrarajzolt javaslat, nem pixelazonos; kapcsolósáv és sarokillesztés felmérendő'),('V03','Cam02/12 konyha','K-01…K-09','Kréta magas/felső, grafit alsó, betonhatású pult/hátfal','KI-006–027','Cam03 korábbi színanyagát egységesíteni;840mm folyosó, elszívó nincs lezárva'),('V04','Cam02 kanapé','Lennon DEQ21WES12329-168260','238×180 taupe; gyári kéz és modulforma még igazolandó','KI-036','L-befoglaló ellenőrzött, részletes kárpitmodell nincs'),('V05','Cam02 asztalok','CF-01/ST-01','Grafit egyedi700×450×350 és300×300×450','KI-037–038','A kerek/fehér DELIFE jelölt nem egyező; egyedi felületminta szükséges'),('V06','Cam12 étkező','Toni160 + Eamy C0100003HE12','Hat szék;37cm feltételezett kihúzás lefutott','KI-028–029','Kárpit tónusa és lábprofilja gyári fotóhoz/modelhez egyeztetendő'),('V07','Cam12 függeszték','Somar L00148FA05','76cm fehér búra; pontos függesztési magasság még nyitott','KI-109','Tényleges SKU mesh és fényforrás nincs modellezve'),('V08','Cam02 mennyezeti lámpa','Enrave M4115931P6','Ø38.1×8.4cm lapos opál','KI-113','Lényeges eltérés a célkép magas dobformájától; nincs automatikusan elfogadva'),('V09','Nappali szőnyeg','Nifelia X0100244JJ12','200×300cm bézs','KI-039','Anyagminta és szálirány; képernyőszín nem színjóváhagyás'),('V10','Master éjjelik','NT-L/NT-R + FADO800.963.72','Grafit egyedi30×42×45; opálgömbØ25H24','KI-047,117','Gömb nagyobb, talpa más, mint a célképen; Hue izzó beférés nem igazolt'),('V11','Master tároló','WN-01/WS-01','2920 és2380mm; egyedi belsők, sekély déli rúd','KI-048–052','PAX illeszkedése nincs igazolva; saját korpusz ajánlati javaslat'),('V12','Master fejvég','HB-01','2700×1500 két anyagmező;2700mm fényvonal','KI-046,118','Taupe/grafit kárpitminták és ragasztás/tűzvédelmi termékadatok kellnek'),('V13','Nem renderelt05.2','SLATTUM160 + W52/DS52','160cm fekvőfelület és munkahely tervjavaslat','KI-058–069','Erkélyajtó ütközés a DS52/FLINTAN elhelyezésével: nem elfogadható főelrendezés'),('V14','Nem renderelt05.3','NORDLI180 + W53/TROTTEN','180cm ágy megmarad; íróasztal északkeleti sarokban','KI-070–081','Új helyiségterv; sekély gardrób és használati hely owner döntés'),('V15','Cam10 fürdő','B62-01/02 és GL-01','Smyle megtartás, fix1000mm üveg','KI-091–097','Fotó hatszögburkolata elsődleges; szifon, üveg és méret még nem gyártható'),('V16','Terasz','Grafit lounge fő / NÄMMARÖ295.752.24 gazdaságos','Fő pontos család nincs lezárva; alternatíva akác190500Ft','KI-138–142','Akác váz jelentős anyageltérés; chaise más geometria; nincs jóváhagyva'),('V17','Teljes kültér','Jakuzzi + emelés/bekötés','1.7M+0.3M keret megtartva','KI-136–137','Típus, tömeg, statika és logisztika nyitott; nem eltüntetett költség'),('V18','Küszöb / szintek','SURVEY-THRESHOLD','Fotón látható fellépés; modell120mm jelölő','KI-003,149','Nem helyszíni méret; végleges renderben pontosítani kell')]
visual=[dict(id=a,target=b,solution=c,detail=d,cost_rows=e,deviation=f,approval='NINCS JÓVÁHAGYVA') for a,b,c,d,e,f in raw];(P/'data/vizualis_elteres_R02.json').write_text(json.dumps(visual,ensure_ascii=False,indent=2))
style=ParagraphStyle('body',fontName='Arial',fontSize=9,leading=12,spaceAfter=6);head=ParagraphStyle('head',parent=style,fontName='ArialB',fontSize=16,leading=20,spaceAfter=10,textColor=ink)
def para(s,st=style):return Paragraph(escape(str(s)).replace('\n','<br/>'),st)
def footer(c,doc):c.setFont('Arial',8);c.setFillColor(ink);c.drawString(30,20,'A902 Kyoto Ink R02 | 2026-10-26 | ajánlati / feltételes');c.drawRightString(565,20,str(doc.page))
def makepdf(name,story):SimpleDocTemplate(str(P/'outputs'/name),pagesize=A4,rightMargin=30,leftMargin=30,topMargin=30,bottomMargin=38).build(story,onFirstPage=footer,onLaterPages=footer)
story=[para('Vizuális eltérésjegyzék',head),para('A fő változat a V3.3 nappalihoz közelítő javaslat; a CP1a termékek kutatási jelöltek. Egyetlen sor sem jelent automatikus tulajdonosi elfogadást.')]
for x in visual:story += [para(x['id']+' / '+x['target'],head),para('Megoldás: '+x['solution']+'. '+x['detail']),para('Eltérés: '+x['deviation']),para('Költséghivatkozás: '+x['cost_rows']+'. A tételes fő és gazdaságos érték az Excelben; nem külön hozzáadandó felár. Jóváhagyás: '+x['approval'])]
makepdf('A902_R02_vizualis_elteresek.pdf',story)
# All159 real records in a portable readable catalog, including unresolved statuses.
story=[para('Teljes termék- és munkatételjegyzék',head),para('159 sor, a meglévő élő regiszter elemkódjaival. Késztermék, egyedi csomag és szakági előirányzat elkülönített státusszal. A link és gyári méret nem jelenti az ár, készlet vagy magyar szállítás visszaigazolását. A becsült költségek nem fix ajánlatok.')]
for r in R:
 total=r['mennyiseg']*r['egysegar']+r['szallitas']+r['szereles']+r['egyeb']
 story += [para(r['elemkod']+' | '+r['megnevezes'],head),para('Helyiség '+r['helyiseg']+' / '+r['szakma']+'; '+r['marka']+'; SKU '+r['sku']),para('Méret: '+r['meret']+'; szín/felület: '+r['szin']+'; anyag: '+r['anyag']),para(f"Mennyiség {r['mennyiseg']} {r['egyseg']}; egységár {num(r['egysegar'])}Ft; teljes {num(total)}Ft. Státusz: {r['arstatusz']}. Ellenőrzés: {r['datum']}."),para('Forrás: '+r['arforras']),para('Eltérés / döntés: '+r['egyezes']+' / '+r['jovahagyas']),para('Rajz: '+r.get('rajz','PENDING')+'; szerkezet: '+r.get('szerkezet','PENDING')),para('Beszerzés: '+r['atfutas']+'; '+r['szallithatosag']+'. Nyitott: '+r['ellenorzes'])]
makepdf('A902_R02_teljes_teteljegyzek.pdf',story)
# Owner exactly one A4, actual design-derived plan and TV composition.
c=canvas.Canvas(str(P/'outputs/A902_R02_tulajdonosi_egyoldalas.pdf'),pagesize=A4);W,H=A4
c.setFillColor(white);c.rect(0,0,W,H,fill=1,stroke=0)
def text(x,y,s,size=10,bold=False,color=ink):c.setFont('ArialB' if bold else 'Arial',size);c.setFillColor(color);c.drawString(x,y,s)
def wrap(x,y,s,width,size=9,lead=12):
 words=s.split();line=''
 for word in words:
  trial=(line+' '+word).strip()
  if pdfmetrics.stringWidth(trial,'Arial',size)>width:text(x,y,line,size);y-=lead;line=word
  else:line=trial
 if line:text(x,y,line,size);y-=lead
 return y
text(30,809,'A-902 · KYOTO INK',22,True);text(30,788,'R02 megvalósítási javaslat · tulajdonosi áttekintés · 2026.10.26.',10)
img=next(t for t in targets if t['camera']=='12');c.drawImage(str(P/img['project_path']),30,648,width=195,height=122,preserveAspectRatio=True,anchor='c');text(30,637,'V3.3 célkép – nem megvalósulási bizonyíték',8)
text(245,756,'Várható fő költség: '+num(C['main'])+' Ft',14,True);text(245,734,'Előirányzati sáv: 17,74–27,13 M Ft',11)
text(245,714,'18 M keret felett: +'+num(C['main']-18000000)+' Ft',10,True,color=red);text(245,695,'Takarékos javaslat: '+num(C['economy'])+' Ft',10)
text(245,678,'Külön tartalék: 2 000 000 Ft, érintetlen',10,True)
wrap(245,660,'Ellenőrzött webshopár: 1,757 M Ft; írásos ajánlat: 0 Ft; becslés: 18,797 M Ft. Az ársáv nem garancia.',315,9)
text(30,612,'Mit kapok? Teljes lakásra és kültérre készülő, összekötött tervcsomagot.',11,True)
# Plan area; coordinates from saved design, complete apartment, terrace represented above.
sc=25;ox=90;oy=365
for rs in G['rooms'].values():
 for x,y,X,Y in rs:c.setFillColor(pale);c.rect(ox+x*sc,oy+y*sc,(X-x)*sc,(Y-y)*sc,fill=1,stroke=0)
for n,b in G['walls'].items():
 if b[2]>1 or n.startswith('Plafon'):continue
 c.setFillColor(ink);c.rect(ox+b[0]*sc,oy+b[1]*sc,(b[3]-b[0])*sc,(b[4]-b[1])*sc,fill=1,stroke=0)
for u in D['units']+D['items']:
 if u['room'] in ['09','10','WPC','13'] or u['z']>1:continue
 ww,dd=u['w']/1000,u['d']/1000
 if u['rot']==90:ww,dd=dd,ww
 c.setFillColor(taupe);c.rect(ox+u['x']*sc,oy+u['y']*sc,ww*sc,dd*sc,fill=1,stroke=0)
for it in D.get('fixed_existing',[]):
 b=it['bounds'];c.setStrokeColor(ink);c.setFillColor(white);c.rect(ox+b[0]*sc,oy+b[1]*sc,(b[3]-b[0])*sc,(b[4]-b[1])*sc,fill=1,stroke=1)
labels=[(.7,1.9,'05.2'),(1.3,7.6,'Master'),(4.5,5.3,'Nappali'),(7.8,7.65,'Étkező'),(9.1,2.1,'Konyha'),(7.1,1.4,'Előtér'),(4,3.25,'Közl.'),(5.65,3,'WC'),(3.9,2.1,'06.1'),(12,5.9,'05.3'),(14.9,6.7,'06.2')]
for x,y,label in labels:
 tw=pdfmetrics.stringWidth(label,'ArialB',8);c.setFillColor(white);c.rect(ox+x*sc-2,oy+y*sc-3,tw+4,12,fill=1,stroke=0);text(ox+x*sc,oy+y*sc,label,8,True)
text(30,520,'Erkély',9);text(30,506,'megmarad',8);text(232,598,'Terasz: lounge + étkező + jakuzzi; zöldtető változatlan',9)
text(30,345,'Terv szerinti alaprajz; helyszíni felmérésre vár. A 05.2 munkahely még ütközik az erkélyajtóval.',8,color=red)
text(30,321,'Egyedi TV-fal / 3,30 m',12,True);ss=.04;sy=205;sx=30
c.setFillColor(taupe);c.rect(sx,sy,3300*ss,400*ss,fill=1,stroke=0);c.setFillColor(pale);c.rect(sx,sy+400*ss,2600*ss,2330*ss,fill=1,stroke=1);c.setFillColor(taupe);c.rect(sx+2600*ss,sy+400*ss,700*ss,2330*ss,fill=1,stroke=1);c.setFillColor(ink);c.rect(sx+580*ss,sy+800*ss,1452.9*ss,834*ss,fill=1,stroke=0)
for k in range(1,4):c.line(sx+k*650*ss,sy+400*ss,sx+k*650*ss,sy+2730*ss)
text(30,190,'TV-01/02/03 – a részletes tervből',8)
text(230,321,'Mikor és mennyire képhű?',12,True)
y=wrap(230,302,'Feltételesen 17 hét a felmérés indításától. A fő kockázat az egyedi gyártás és a kanapé nem visszaigazolt szállítása.',335,10,13)
y=wrap(230,y-4,'A fő szín- és anyagkompozíció követhető. Nyitott eltérés: lapos Enrave a dobforma helyett, nagyobb FADO gömb, újrarajzolt tusgrafika. A takarékos teraszon akác váltja a grafit vázat.',335,10,13)
text(30,166,'Három tulajdonosi döntés',12,True)
y=wrap(30,148,'1. Költség: melyik változatot finomítsuk? A takarékos javaslat is 1,900 M Ft-tal keret felett van; a tartalékot nem vontuk be.',535,9,12)
y=wrap(30,y-2,'2. Látvány: a lámpaformák, tusnyomat és terasz anyagcseréi csak minták és konkrét alternatívák alapján fogadhatók el.',535,9,12)
y=wrap(30,y-2,'3. Funkció:05.2 integrált munkahely, kisebb gardróbbal (+80eFt becslés), vagy további áttervezés? Jakuzzi: szakági feltételek nyitottak.',535,9,12)
wrap(30,56,'Mi van nyitva? Felmérés, több pontos termék, 05.2 ajtóütközés, konyhai használati tér, gépészeti/statikai és gyártói jóváhagyás. Nincs rendelés, gyártási engedély vagy végleges render-PASS.',535,8,10)
c.showPage();c.save();assert len(PdfReader(P/'outputs/A902_R02_tulajdonosi_egyoldalas.pdf').pages)==1
print('Owner PDF1page,159-row catalog,18-deviation report')
