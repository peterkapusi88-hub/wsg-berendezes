from pathlib import Path
from PIL import Image as PILImage
import io
import json,math,sys
sys.path.insert(0,'/private/tmp/s16-python')
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor,Color,white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit,ImageReader
from reportlab.platypus import Table,TableStyle,Paragraph
from reportlab.lib.styles import ParagraphStyle
from xml.sax.saxutils import escape
O=Path(__file__).resolve().parents[1];P=O.parent
read=lambda n:json.loads((O/'data'/n).read_text())
parts=read('parts.json');cost=read('cost.json');layout=read('layout.json');lighting=read('lighting.json');drawers=read('drawers.json');materials=read('materials.json');gates=read('gates.json')
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('ArialB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
C=canvas.Canvas(str(O/'rajzok/S16_R05_tervcsomag.pdf'),pagesize=(420*mm,297*mm));C.setTitle('S16 Monza Magno médiafal - R05 ívkorrekció - 3600 mm')
page=0;INK='#283236';ACC='#9D7C4C';COL={m[0]:m[4] for m in materials}
def text(t,x,y,size=10,bold=False,color=INK):C.setFillColor(HexColor(color));C.setFont('ArialB' if bold else 'Arial',size);C.drawString(x*mm,y*mm,str(t))
def para(t,x,y,w,size=10,leading=4.8):
 for ln in simpleSplit(t,'Arial',size,w*mm):text(ln,x,y,size);y-=leading
 return y
def rect(x,y,w,h,fill=None,stroke=INK,lw=.25):
 C.setLineWidth(lw*mm);C.setStrokeColor(HexColor(stroke));C.setFillColor(HexColor(fill or '#FFFFFF'));C.rect(x*mm,y*mm,w*mm,h*mm,stroke=1,fill=bool(fill))
def line(x1,y1,x2,y2,color=INK,lw=.25):C.setLineWidth(lw*mm);C.setStrokeColor(HexColor(color));C.line(x1*mm,y1*mm,x2*mm,y2*mm)
def poly(pts,fill=None,color=INK,lw=.15):
 p=C.beginPath();p.moveTo(pts[0][0]*mm,pts[0][1]*mm)
 for x,y in pts[1:]:p.lineTo(x*mm,y*mm)
 p.close();C.setLineWidth(lw*mm);C.setStrokeColor(HexColor(color));C.setFillColor(HexColor(fill or '#FFFFFF'));C.drawPath(p,stroke=1,fill=bool(fill))
def _pdfimage(p):
 b=io.BytesIO();PILImage.open(p).convert('RGB').save(b,format='JPEG',quality=94,subsampling=0);b.seek(0);return b
def image(p,x,y,w,h):
 if Path(p).exists():C.drawImage(ImageReader(_pdfimage(p)),x*mm,y*mm,w*mm,h*mm,preserveAspectRatio=True,anchor='c',mask='auto')
def new(title,scale='jelölt / A3'):
 global page
 if page:C.showPage()
 page+=1;text('S16  /  MONZA MAGNO',15,282,10,True);text(title,15,269,19,True);line(15,262,405,262,'#A3ADAD')
 text(f'R05 · 2026.10.29. · {page:02d}  |  mm  |  {scale}',15,12,8)
 text('TERVEZÉSI JAVASLAT - NEM GYÁRTÁSI JÓVÁHAGYÁS',247,12,8,True,'#9B591F')
def hdim(x1,x2,y,label):
 line(x1,y,x2,y,ACC,.2)
 for x in [x1,x2]:line(x-1.3,y-1.3,x+1.3,y+1.3,ACC,.3)
 text(label,(x1+x2)/2-pdfmetrics.stringWidth(label,'Arial',8)/mm/2,y+2,8,color=ACC)
def vdim(x,y1,y2,label):
 line(x,y1,x,y2,ACC,.2)
 for y in [y1,y2]:line(x-1.3,y-1.3,x+1.3,y+1.3,ACC,.3)
 C.saveState();C.translate((x-2)*mm,((y1+y2)/2)*mm);C.rotate(90);text(label,0,0,8,color=ACC);C.restoreState()
def elevation(x,y,s=1/15,interior=False,lights=False):
 for p in sorted(parts,key=lambda p:p['box'][1]):
  if interior and (p['id'].startswith(('TV-','BG-','FRAME-','SILVER-','CURVE-')) or 'FRONT' in p['id'] or 'DOOR' in p['id'] or p['id']=='TEXTILE'):continue
  a,b,z,dx,dy,dz=p['box'];pts=p['outline'] if p['axis']=='y' and p['outline'] else [[0,0],[dx,0],[dx,dz],[0,dz]]
  poly([(x+(a+u)*s,y+(z+v)*s) for u,v in pts],COL[p['material']] if not interior else '#E8EAE6','#555C5E',.12)
 if not interior:
  a,b,z,dx,dy,dz=layout['screen_box'];rect(x+a*s,y+z*s,dx*s,dz*s,'#171E24',lw=.12)
 if lights:
  for c in lighting['circuits']:
   for a,b in zip(c['path'],c['path'][1:]):line(x+a[0]*s,y+a[2]*s,x+b[0]*s,y+b[2]*s,'#F4B85C',.5)
def table(headers,rows,x,y,widths,size=9):
 ps=ParagraphStyle('cell',fontName='Arial',fontSize=size,leading=size*1.3,textColor=HexColor(INK));ph=ParagraphStyle('head',parent=ps,fontName='ArialB',textColor=white)
 cells=[[Paragraph(escape(str(v)),ph) for v in headers]]+[[Paragraph(escape(str(v)),ps) for v in row] for row in rows]
 t=Table(cells,colWidths=[w*mm for w in widths],repeatRows=1,hAlign='LEFT');t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#343D41')),('VALIGN',(0,0),(-1,-1),'TOP'),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEBELOW',(0,1),(-1,-1),.3,HexColor('#D5DAD8')),('ROWBACKGROUNDS',(0,1),(-1,-1),[white,HexColor('#F3F4F0')])]))
 tw,th=t.wrap(390*mm,240*mm)
 if y*mm-th<23*mm:raise ValueError(f'Table overflows page {page}: {th/mm} at{y}')
 t.drawOn(C,x*mm,y*mm-th);return y-th/mm
money=lambda v:f'{v:,.0f}'.replace(',',' ')

new('3600 mm médiafal, a képhez javított íves forma')
image(P/'sources/S16_Cam02_C_celkep.png',15,126,190,119);image(O/'nezetek/S16_R05_zart.png',215,112,190,142)
text('Kiválasztott C célkép - S16 Cam_02 V3.3 C v1',15,121,9,True)
text('R05: tényleges 3D modell, műszaki stúdiónézet',215,107,9,True)
y=99
for t in ['A tulajdonos korrekciója alapján a TV-réteg a bal toronytól indul, ívesen felkanyarodik a képernyő mellé, és alul az alsó bútor fedlapjáig fut. R05:870mm torony,75col TV,25mm felső fényrés; bal fél alatt nincs fiók; teljes peremfény,105/105mm betétmargó; ezüstcsík nélkül.',
 'Az új rádiuszok képre illesztett tervezési javaslatok: torony R100, alsó jobb sarok R80, textilbetét R60, TV átmenet R160/R140/R100. Ezeket nem állítjuk felmért képméretnek.',
 f'Becsült bruttó bútorár: {money(cost["totals"]["base"])} Ft; soronkénti sáv {money(cost["totals"]["low"])}–{money(cost["totals"]["high"])} Ft. S01 R16-hoz képest {money(cost["delta"])} Ft többlet. A két becslés sávja átfed.',
 'Tartalom: hat magas nyomásra nyíló, csillapított fiók; két magas ajtó; tíz állítható polc; nyolc külön belső fényérzékelő. A frontosztás az összehasonlításhoz kidolgozott javaslat.',
 'Állapot: rajzi és költség-előkészítés. Felmérés, anyag/ív/fény-minta, végleges vasalatfuratok, falrögzítés és műhelyi elsődarab még szükséges.']:
 y=para(t,15,y,390,10,4.8)-4

new('R05 – a teljes front hézagellenőrzése')
y=245
for title,body in [
 ('Mi volt hibás?', 'A torony felső ajtóhézaga20mm volt. Az alsó bal front alatt5mm, a jobb szélső fiók ívénél helyenként1,07mm, a bal ajtó melletti osztólécnél1,5mm maradt. Ezek nem szerepelhettek volna ellenőrzött, egységes3mm-es részletként.'),
 ('Mi változott?', 'A felső ajtóél17mm-rel feljebb, a bal ajtó alsó éle2mm-rel lejjebb került. Az alsó frontok Z171–549mm között futnak. Az alsó frontkeret18mm vastag; a jobb szélső fiókR59 a keretR62 belső ívében. Az osztóléc bal végeX436,5. A háttérpanel szélső illesztései is3mm-esek.'),
 ('Mit ellenőriztünk?', 'Mind a8 nyíló front teljes kerületét0,5mm-es mintavétellel; az egyenes illesztéseket és az egyközpontú köríveket külön méretszámítással. Névleges hézag3mm. A poligon közelítés legkisebb eltérése0,001mm; a T-csatlakozásnál a legközelebbi sarok ferde távolsága3,34mm, a merőleges hézag ott is3mm.'),
 ('Ütközés és mozgás', 'A120 bútoralkatrész7140 páros összevetésében nincs térfogati átfedés. Mind a6 fiók külön0–300mm mozgásánál nincs vizsgált ütközés. A névleges ajtóforgást az íves sapkák ellen is ellenőriztük1°-os és2mm-es mintavétellel, a kontúrcsúcsoknál is; találat nincs.'),
 ('Megőrzött arányok', 'A TV mérete változatlan. A világos betét felső/alsó margója105/105mm, fényperemé100/100mm. A fényút a valódi ajtóhoronyban marad. A teljes panel feletti25mm mennyezeti LED-rés szándékos.'),
 ('Az ellenőrzés határa', 'Ez a saját modell geometriai ellenőrzése. A felmért helyiség, tényleges pánt és kábelátvezetés, rögzítés, gyártási tűrések és villamos hőpróba még nem igazolt. A rajz továbbra sem gyártási kiadás. Részletes bizonyíték: audit/geometry_checks.json és motion_checks.json.')]:
 text(title,18,y,12,True);y=para(body,18,y-7,380,10,5)-9
assert y>23

new('Homlokzat és fő méretláncok','1:15; nyomtatás 100%, A3')
elevation(18,42);line(18,42+2900/15,258,42+2900/15,'#A97B38',.3);hdim(18,258,31,'3600 - tulajdonosi tervezési cél');vdim(270,42,42+2875/15,'2875');line(18,42,258,42)
x=18+435/15
hdim(18,x,39,'435 ajtó')
for w in layout['module_widths']:hdim(x,x+w/15,39,str(w));x+=w/15
text('870-es torony',18,246,10,True);text('Folytonos, háromrészes TV-réteg',95,246,10,True)
notes=[('Befoglaló','3600 × 2875 mm. Korpusz/front 400 mm, textilbetéttel max.408 mm. Kész padló felett150 mm alsó él.'),('Alsó felső él','Minden alsó modul felső éle570mm. A torony jobb alsó sarka szögletes, folytonosan csatlakozik a fióksorhoz.'),('TV-réteg','X870–3500; Z570–2150. Y95–113; háttérfrontY78. Kiemelés35 mm. Nincs nyitott függőleges sáv a torony és a réteg között.'),('Szerelési hézag','3mm felső ajtóhézag is: keretR82/ajtóR79; a korábbi20mm rés javítva.3 mm front/panel közök,5 mm tervezett benyomási tér. Felső25 mm névleges rés nem helyszíni igazolás.'),('Rétegillesztések','TV-réteg3rész: LINK/MID/END. VarratX1500 és2550; cél a TV által részben takart hely. Valódi hézagot nem tüntetünk el.'),('Magassági forrás','Tulajdonosi25mm felső fényrés; v2b névleges2,90m; a legkisebb helyszíni érték és felállítás ellenőrizendő.')]
y=245
for title,t in notes:text(title,287,y,10,True);y=para(t,287,y-6,113,9,4.3)-8

new('Az ívek és a folytonos réteg','homlokzati kontúr 1:10; részlet 1:2')
tv=[p for p in parts if p['id'] in ['TV-LINK','TV-MID','TV-END']]
for p in tv:
 x,y,z,dx,dy,dz=p['box'];poly([(20+(x+u-870)/10,70+(z+v-570)/10) for u,v in p['outline']],COL['M03'])
line(20,70,20,228,'#925B35',.6);text('TORONY OLDALA',20,237,10,True)
text('Csatlakozó nyelv',23,114,9);text('R160 homorú',35,143,9);text('R140 domború',57,234,9);text('R100',276,232,9)
hdim(20,283,59,'2630 mm teljes rétegszélesség');text('Alsó kontúr a bútor fedlapjáig: Z570. Nincs lebegő rés.',20,48,10,True)
text('Rajzi kontúr nem darabolt ív',315,244,11,True)
y=para('Az alkatrész-DXF-ekben és a DWG-ben az ívek körívként szerepelnek. A Blender megjelenítése sűrű háló; ez nem a gyártási kontúr felbontása.',315,236,87,9,4.2)
y=para('A toronyR100 és az alsó sarokR80 saját belső ívvel rendelkező,18mm rétegvastagságú íves héj. Befoglaló mélysége337mm; nem337mm vastag MDF lap.',315,y-8,87,9,4.2)
y=para('Kötelező1:1 sarokminta: külső ív, érintőleges átmenet, látszó hézag, élburkolat/festés, LED és az ajtó nyitása együtt.',315,y-8,87,9,4.2)
text('R100 / R82 héj',315,113,10,True)
poly([(325+x/2,55+z/2) for x,z in next(p for p in parts if p['id']=='CURVE-T-TOP')['outline'] if x<=100],COL['M02'])
para('Általános élletörés: csak finom R1–R2 tapintási él, mintával. Ez nem helyettesíti a nagy homlokzati rádiuszokat.',315,38,87,8.5,4)

new('Belső kiosztás és nyitott állapot','bal: 1:15 / jobb: műszaki nézet')
elevation(17,39,interior=True);image(O/'nezetek/S16_R05_nyitott.png',255,82,150,145)
text('Tíz polc: 406 × 290 mm',25,244,10,True);text('Két alsó szervizrekesz mögött bontható elektronika',25,25,9)
para('Hat fiók teljes kihúzása300mm. Nettó össztérfogat155,7liter; a S01 R16 értéke180,8liter. A bal fél alatt fiók helyett az aljáig nyíló szekrényajtó van. Doboz:15mm nyír, hasznos belmagasság222mm és mélység260mm.',270,74,128,10,4.8)
para('A polcszám azonos, de a torony polcai406×290mm-esek,22,7%-kal szélesebbek a S01-nél. A nagyobb felső ív a legfelső rekesz külső sarkaiból helyet vesz el; a sarok környezetét nem számoljuk téglatestként szabad tárolótérnek.',270,43,128,9,4.2)

new('Alaprajz, kihúzás és használati sáv','1:12; névleges helyfoglalások')
sx,sy,sc=20,235,1/12
for p in parts:
 x,y,z,dx,dy,dz=p['box']
 if z<350<z+dz:rect(sx+x*sc,sy-(y+dy)*sc,dx*sc,dy*sc,'#DCE0DB',lw=.12)
for d in drawers:
 x=d['x'];ww=d['width'];rect(sx+x*sc,sy-700*sc,ww*sc,300*sc,None,'#B87937',.4);text(d['id'],sx+(x+ww/2)*sc-3,sy-750*sc,9,True)
hdim(20,320,242,'3600');vdim(335,sy-400*sc,sy,'400');vdim(345,sy-700*sc,sy-400*sc,'300 kihúzás')
rect(20,sy-1300*sc,300,600*sc,'#F0F1E9','#A4AD9A',.2);text('600 mm használati sáv cél a NYITOTT fiókok előtt',45,sy-1030*sc,11,True)
y=105
for t in ['A szükséges szabad mélység a faltól:400mm bútor +300mm kihúzás +600mm használat =1300mm. Ez tervezési ellenőrzési sáv, nem igazolt helyszíni közlekedő.',
 'A toronyajtók névleges90° nyitásánál kb.413mm előrenyúlással számolunk. A valós pántkinematika, textilbetét és szomszéd tárgyak mozgása külön sablonpróba.',
 'S01-nél ismert asztal/fiók konfliktus volt. Az S16 dohányzóasztal pontos helye és a tényleges JÄTTEBO modulösszeállítás még nincs helyszínen rögzítve: nincs teljes szobai ütközésmentességi állítás.',
 'W01 v2b falhossz4000mm. A3600mm bútorhoz kétoldalt200mm névleges hely marad; a javasolt kezdőpont világY4,25m. A függöny, nyíló teraszszárny, szegőléc és kiállások ezt még módosíthatják.']:
 y=para(t,20,y,380,10,4.8)-7

new('Metszetek, rétegrend és szerviz','teljes metszetek 1:15; részlet 1:2')
for title,cut,bx in [('A-A / TV-mező',2200,30),('B-B / torony',350,130)]:
 text(title,bx,245,11,True)
 for p in parts:
  x,y,z,dx,dy,dz=p['box']
  if x<=cut<=x+dx:rect(bx+y/15,40+z/15,dy/15,dz/15,COL[p['material']],lw=.12)
 line(bx,40,bx,232,'#111111',.5)
 text('fal',bx-7,36,8);hdim(bx,bx+400/15,30,'400')
text('TV-mező vízszintes rétegrend',230,245,12,True)
layers=[(0,40,'Falsín40'),(40,20,'Oldható kapocs20'),(60,18,'Háttér18'),(78,17,'Távtartó17'),(95,18,'TV-réteg18')]
for start,w,label in layers:rect(230+start/2,195,w/2,30,COL['M04'] if start==60 else '#C9CECB');text(label,230+start/2,230-(start%3)*4,7)
hdim(230+78/2,230+113/2,186,'35 mm relief')
y=171
for t in ['TV teherút: készülék -> saját VESA-konzol -> méretezett távtartó/teherhordó alátét -> igazolt fal. A18mm dekorpanel nem a TV teherhordó alapja. Konzolkivágás és távtartóhossz TV- és faladat után.',
 'Torony alsó hátsó szerviz: Y40–135. Elölről kivehető406×345mm fedél; mögötte külön230V doboz és három DC-táp. A tárolásra maradó alsó rekeszmélység240mm.',
 'Háttérpanel: elölről oldható kapocs kell. A25mm felső hézag miatt a hagyományos felfelé emelős akasztást nem tekintjük automatikusan szerelhetőnek.',
 'Szellőzés: alsó és felső200×15mm rés/rekesz előirányzat, eltakarhatatlan kivitelben. A méretet a kiválasztott tápegységek vesztesége és teljes terhelésű hőpróba zárja le.']:
 y=para(t,230,y,170,9.5,4.5)-8

new('Világítás, betáp és hozzáférés','fényutak 1:20; villamos elvi terv')
elevation(15,92,1/20,lights=True)
text(f'Külső {lighting["ambient_mm"]/1000:.2f} m + belső {lighting["internal_mm"]/1000:.2f} m',15,244,11,True)
text(f'LED névleges összteljesítmény: {lighting["total_W"]:.1f} W',15,83,10,True)
rows=[[c['id'],f'{c["length_mm"]/1000:.3f}',f'{c["watts"]:.2f}',c['group']] for c in lighting['circuits']]
table(['Ág','m','W','Táp / vezérlés'],rows,215,246,[60,27,27,70],8.5)
y=66
for t in ['D16 meglévő betáp -> elkülönített230V csatlakozó -> PS1/PS2/PS3 -> ágankénti védelem -> CCT vezérlő / belső szenzor -> fix korpuszprofil. Tápkimenetek nem párhuzamosíthatók.',
 '5 külső CCT vezérlő; PS1:200W, PS2:200W, PS3:60W jelölt. A gyártói csatlakozók, Hue párosítás,2200–2700K jelenet és hőpróba még nyitott.',
 'Az íves TV-fényhez hajlítható megfelelő profil/hűtés vagy műhelyben igazolt szegmentált rendszer kell, folyamatos opál fedéllel. Ez új technológiai tétel, nem az eredeti3m Hue szalag ingyenes meghosszabbítása.']:
 y=para(t,15,y,390,9,4.2)-5

new('Nyitás és a világos betét teljes peremfénye')
table(['Rész','R05 kialakítás','Ellenőrzés'],[
 ['Világos betét','360×2515mm,R60;105mm felső és105mm alsó távolság a teljes külső szekrényhez. Bal ajtóval mozog.','A peremfény teljes zárt lekerekített kör, nem csak egy függőleges csík.'],
 ['Peremprofil','370×2525mm középvonal, R65;10mm széles,6mm mély fészek az18mm ajtóban.','CAD-ben és a modellben külön mart fészek. A profil pontos mérete, hűtése és hajlíthatósága próbaminta után végleges.'],
 ['Ajtó táplálása','24V CCT, rejtett pántoldali hajlításálló3eres átvezetés. Oldható csatlakozó, mindkét oldalon húzásmentesítés.','Nyitási íven túlvezetett laza hurok a pántok között; gyári kábel minimális hajlítási sugara, becsípődés és ismételt nyitáspróba. Méretezés nélkül nincs gyártási kiadás.'],
 ['Ajtók','2×412,5mm széles, eltérő magasságú, rugó nélküli pánt +mágneses nyomásnyitó;bal6/jobb5pánt keret.','Nincs klasszikus fogantyú. Textilnél a merev ajtóperem a nyomási pont. Nyomóút és nyitási erő mintán ellenőrizendő.'],
 ['Fiókok','6 magas front, MOVENTO300 +TIP-ON BLUMOTION. Nyomásra nyitás és csillapított záródás.','3mm frontköz,5mm tervezett benyomási tér; széles D1/D4 front szinkronnal és stabilizátorpróbával.'],
 ['Külső keret','Fix fényudvar a teljes kompozíció körül,25mm mennyezeti rés.','A torony jobb alsó sarkán nincs önálló visszakerekítés; alul a fény a fióksorral együtt fut tovább.']
 ],15,248,[48,172,170],10)
para('Az ajtó és a fiók eltérő működésű: a fiók csillapított, az ajtónál a rugó nélküli nyomásnyitást terveztük. A nyitott modellen csak D3 fiók van kihúzva, a többi csukva; az ajtók névleges90°-ot szemléltetnek; a gyári pánt tényleges mozgását és a vezetéket műhelyi próbával kell igazolni.',15,49,390,10,4.8)

new('75 colos TV: a tulajdonos méretkorrekciója')
tv=read('tv75.json')
table(['Adat','75col méretreferencia','Ellenőrzés / határ'],[
 ['Készülék','Samsung QE75Q7FAAUXXH','A65colos előző helyfoglalót váltja ki. A család méretsorában65 után75col következik.'],
 ['Talp nélküli méret','1677,5 ×962,4 ×61,1mm','Gyári HU specifikáció,2026.10.29. Nem arányosan felszorzott65colos test.'],
 ['Tömeg / VESA','25,3kg /400×400mm','VESA magassági eltolás, csavarhossz és távtartó a valós szerelési rajz szerint.'],
 ['TVM3605 konzol','40–100col; max75kg; max600×400 VESA','A75colos referencia névleg belefér. Ez nem a falhorgony vagy a dekorpanel teherbírásának igazolása.'],
 ['Hely a képernyő körül','Fent218,8mm; fedlapig398,8mm','Jobbra386,25mm; a bal egyenes kontúrszakaszig256,25mm. A folytonos íves forma változatlan.'],
 ['Képernyő középpontja','X2275 /Z1450mm','Szemmagasság és nézési komfort a tényleges kanapén próbálandó.'],
 ['TV árkeret','350000Ft becslés;300000–450000Ft sáv','Régi KI-033 keret250000Ft; különbözet100000Ft. Nem írjuk hozzá a bútor3,68M keretéhez duplán.'],
 ['Lakás75col TV-vel',money(cost['project_S16_if_replaced']+tv['delta_estimate'])+'Ft','Csak W01 ésTV-csere utáni feltételes előirányzat;2M tartalék külön.']
 ],15,248,[60,130,200],10)
para('Forrás: '+tv['source'],15,66,390,8.5,4)
para('Konzol: '+tv['mount_source'],15,52,390,8.5,4)
para('Beszerzési státusz: a gyári oldalon a referencia nem eladó. A75col méret a terv része, a végleges készülék és ára külön beszerzési döntés. Nincs rendelés.',15,36,390,9,4.2)

new('Anyagok és felületképzés')
table(['Kód','Anyag / felület','Konkrét megoldás és feltétel'],[[m[0],m[1],m[2]+' '+m[3]] for m in materials],15,248,[18,112,260],9)
para('R05 változás: a M02 íves sarokhéjak18mm kész rétegvastagságú, rétegelt/lamellázott szerelvények. A118-as R01 laplista nem érvényes. A sarkok nem sűrű sokszögként gyártandók. Mintázat: visszafogott szürke fa, grafika nélkül; a meleg esti fény nem barna festékkód.',15,52,390,10,4.7)

for idx,chunk in enumerate([cost['rows'][:15],cost['rows'][15:]]):
 new('Tételes költségbecslés '+str(idx+1)+'/2')
 rows=[[r['id'],r['name'],f'{r["qty"]:g} {r["unit"]}',money(r['base']),money(r['low']),money(r['high'])] for r in chunk]
 y=table(['Kód','Tartalom','Mennyiség','Alap Ft','Alsó Ft','Felső Ft'],rows,15,248,[18,162,45,55,55,55],8.7)
 if idx==1:
  y-=10;table(['Összesen','Alap Ft','Alsó Ft','Felső Ft'],[['S16 R05',money(cost['totals']['base']),money(cost['totals']['low']),money(cost['totals']['high'])]],15,y,[190,65,65,70],11)
 para('Árállapot: minden új S16 tétel bruttó tervezői becslés,2026.10.29.; nincs írásos ajánlat vagy igazolt magyar webshopár. Az Excelben a mennyiség és egységár külön szerkeszthető; a csomagok tartalmi lehatárolása és forrása mellettük olvasható.',15,40,390,9,4.2)

new('S01 / S16 összevetés és feltételes lakáskeret')
rows=[['Szélesség','3600mm','3600mm'],['Fiókok / nyitás','6 magas, MOVENTO300 +TIP-ON BLUMOTION','6 magas, külön nyitású;155,7liter, eltérő szélességek'],['Fióktérfogat','180,8liter','155,7liter;−13,9%;bal alsó rész helyette szekrényrekesz'],['Torony','2ajtó,10polc331×290mm','2ajtó,10polc406×290mm;22,7%-kal szélesebb polcok'],['Belső fény','8 külön érzékelő,7,25m LED','8 külön érzékelő,6,83m LED'],['Külső fény','8,50m,3fényút',f'{lighting["ambient_mm"]/1000:.2f}m,5fényút'],['Alapbecslés',money(2969300)+'Ft',money(cost['totals']['base'])+'Ft'],['Becslési sáv','2 438 726–4 030 447Ft',money(cost['totals']['low'])+'–'+money(cost['totals']['high'])+'Ft']]
table(['Feltétel','S01 Kyoto Ink R16','S16 Monza Magno R05'],rows,15,248,[80,150,160],10)
y=119
for t in [f'A feltételes lakáselőirányzat:26 212 190 -2 969 300 +{money(cost["totals"]["base"])} = {money(cost["project_S16_if_replaced"])} Ft. Ez kizárólag a W01 médiafal cseréje, nem a teljes S16 lakás költsége.',
 f'A18 000 000Ft cél feletti összeg {money(cost["project_S16_if_replaced"]-18000000)}Ft. A2 000 000Ft tartalék külön marad; a keretet nem emeltük meg.',
 'Az S16 alsó fiókos rész950 000Ft, a közös rögzítési alap504 800Ft, a TV-konzol32 000Ft a S01-ből induló összehasonlító feltevés; a fiókos rész az eltérő szélesség miatt korrigált. Az S16 íves héjak, rétegelt háttér és több fényút külön többlet.',
 'TV-készülék, közös szállítás/felhordás/daruzás és más szobai tárgyak nem részei ennek az öt csomagsornak. A meglévő lakáskeret KI-151/KI-137 soraiban maradnak; nem nullaköltségűek.',
 'Szerelési/műhelyi átfedés: KI-014 és KI-106 a végső ajánlatban egyeztetendő. Az eredeti négyajtós kisebb promptbútor nem közvetlen árversenytárs. Második stílus nincs megadva.']:
 y=para(t,15,y,390,10,4.7)-6

new('Vasalatok, kötés és szerelési sorrend')
table(['Rész','Kidolgozott javaslat','Még szükséges igazolás'],[
 ['Fiókok','760H3000S 300mm sínpár;T51.7601 kapocspár;T60L7040 S0 vagyT60L7140 S1;T60.1125W szinkron LW-267.','S0≤10kg/S1>10–20kg teljes fióktömeg. A40kg sínterhelés nem helyettesíti a TIP-ON működési tartományt. Széles/rövid D4 stabilizátorpróba.'],
 ['Doboz','SKW=LW-42; SKL=300-10=290. 15mm oldalak,260mm nettó mélység,222mm nettó magasság.','Blum T65.1000.02 sablon, pontos kapocs/kampó/alákivágás. Saját CNC-koordináta nincs kitalálva.'],
 ['Toronyajtó','bal6/jobb5pánt költségkeret; rugó nélküli inset CLIP top +mágneses TIP-ON; a textil és teljes peremfénye a bal ajtóval mozog, rejtett24V átvezetéssel.','Pontos cikkszám/talp, ráütés, csészetávolság és ajtótömeg műhelyi lezárásra. Az ajtócsillapítás nincs állítva.'],
 ['Rögzítés','7 korpuszra S01 minőségű Camar-rendszer költségelőirányzat; panelre elöl oldható rejtett kapocs.','Falanyag, vezetékkeresés, üres/teli tömeg és kihúzási nyomaték után pontos rögzítési terv. Nem univerzális tiplikiosztás.'],
 ['Íves héj','R100/R82 torony ésR80/R62 alsó sarok;18mm rétegvastagság,337mm mély egyedi szerelvény.','Ragasztott lamellák/hajlítható rétegelt lemez technológiája; rugóvisszaalakulás, sablon és felületminta.'],
 ],15,248,[42,170,178],9)
y=98
for i,t in enumerate(['Felmérés és D16–18/G kiállások közös koordinátájú rögzítése; fal és szerelőút igazolása.','Falsínek és korpuszok szintezése; a torony helyszíni összeépítése. Az íves héjakat a korpusz után, oldható kötéssel rögzítsék.','Tápkörök, hozzáférhető szerviz és hőpróba; bontható hátak, majd háttérpanelek.','TV teherhordó konzol és átvezetések; kontúrozott háromrészes réteg; fiókok/ajtók, világítás és hézagok beállítása.','Teljes elsődarab- és használati próba, terhelés, nyitás, fény, szerviz. Csak ezután gyártásra kiadás.'],1):y=para(f'{i}. {t}',15,y,390,10,4.5)-5

for j,chunk in enumerate([gates[:6],gates[6:]]):
 new('Felmérési és jóváhagyási nyilvántartás '+str(j+1)+'/2')
 table(['Kód / nyitott adat','Felelős','Elfogadási feltétel','Határ'],[[g['id']+' '+g['open'],g['owner'],g['acceptance'],g['deadline']] for g in chunk],15,248,[76,61,187,66],9)
 para('Minden felsorolt pont állapota NYITOTT. Bizonyíték, jóváhagyó és dátum az Excel Lezárás lapján és a data/gates.json-ban rögzíthető. Nincs automatikus gyártási jóváhagyás. Nincs rendelés, ajánlatkérő levél vagy gépi futtatás.',15,48,390,10,4.7)

new('Források, állományok és ellenőrzési határ')
src=read('sources.json')['sources'];y=248
for id,title,url,note in src:
 text(id+'  '+title,15,y,10,True);y=para(url,15,y-5,390,8.4,4)-2;y=para(note,15,y,390,9,4.2)-6
para('Aktív változat:R05_felso_ajtohezag. R01/R02/R03 elavult; R05 tartalmazza a tulajdonos szélesség-,75col TV- és világításkorrekcióját. A fő nézetek, DXF-alkatrészek, költségmodell és Blender ugyanebből az R05 adatmodellből készültek. A részletes ellenőrzések az audit mappában találhatók. A műhelyi sablonműveletek és CNC-programok nincsenek kiadva.',15,42,390,9,4.2)

# Four traceable part cards per A3 page; curved assemblies explicitly labelled as bounding sizes.
for start in range(0,len(parts),4):
 new('Alkatrészlapok '+str(start+1)+'–'+str(min(start+4,len(parts))),'1:25 névleges kontúr; készméret / íves héjnál befoglaló')
 for k,p in enumerate(parts[start:start+4]):
  col=k%2;row=k//2;cx=15+col*197;cy=140-row*117
  rect(cx,cy,192,111,None,'#B8C0BF',.18);text(p['id']+'  '+p['name'],cx+4,cy+103,9,True)
  dims=f'{p["L"]:g} × {p["W"]:g} × {p["T"]:g} mm'
  if p['kind']=='curved_assembly':dims+=' BEFOGLALÓ; héj18mm'
  text(dims,cx+4,cy+97,8.5)
  pts=p['outline'] if p['outline'] else [[0,0],[p['L'],0],[p['L'],p['W']],[0,p['W']]]
  # Upper-left card area uses a fixed scale; wider horizontal parts rotate for fit when needed.
  scale=1/25;maxh=max(z for x,z in pts)*scale;maxw=max(x for x,z in pts)*scale
  if maxh>85:
   pts=[[z,x] for x,z in pts];maxh=max(z for x,z in pts)*scale;maxw=max(x for x,z in pts)*scale
  px=cx+6;py=cy+6
  poly([(px+x*scale,py+z*scale) for x,z in pts],COL[p['material']],lw=.13)
  nx=cx+112;ny=cy+86
  for t in [f'Anyag:{p["material"]}; költség:{p["cost"]}',f'Szál:{p["grain"]}','Nyers méret/művelet: műhelyi lezárásra.',p['note'] or 'Kontúr kész névleges méret. Vasalatfuratok gyári sablonnal.']:
   ny=para(t,nx,ny,75,8,3.8)-4
  text('U → ; V ↑ ; helyi (0,0) / mm',cx+4,cy+2,7)
C.save()
print(json.dumps({'pages':page,'parts':len(parts),'file':'rajzok/S16_R05_tervcsomag.pdf'}))
