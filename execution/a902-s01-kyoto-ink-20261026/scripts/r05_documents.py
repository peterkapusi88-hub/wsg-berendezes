from pathlib import Path
import json,copy,hashlib,csv,math,html,re
import r04_drawing_book as d
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor,white
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader,PdfWriter
P=d.P;O=P/'R05';D=json.loads((O/'data/design_R05.json').read_text());U={u['id']:u for u in D['units']};M=json.loads((O/'data/materials.json').read_text());C=json.loads((O/'data/cost_R05.json').read_text());E=json.loads((O/'data/economy_options.json').read_text());R=json.loads((O/'data/register_proposal.json').read_text());RM={r[2]:r for r in R[1:]}
REF=P/'CP3/reviews/20261027_csomag_es_mediafal/A902_KyotoInk_V01_KI-CP3-R03_VISUAL_RESCUE_v3_CONDITIONAL.png'
REF2=P/'targets/A902_S01_KyotoInk_Cam_12__V33_C_v1.png'
d.O=O;d.SHEETS=[]
def readable(t):
 t=str(t)
 for a,b in [('WNgardrób','WN gardrób'),('WNterv','WN terv'),('WNfront','WN front'),('TVtorony','TV torony'),('LED2074','LED 2074'),('Loox5LED','Loox5 LED'),('WNminta','WN minta'),('PS-A60','PS-A 60'),('PS-B60','PS-B 60')]:t=t.replace(a,b)
 t=re.sub(r'(?<=\d)(?=[a-záéíóöőúüűA-ZÁÉÍÓÖŐÚÜŰ])',' ',t)
 t=re.sub(r'(?<=[a-záéíóöőúüű])(?=\d)',' ',t)
 t=re.sub(r'(?<=[.;:!?])(?=[A-ZÁÉÍÓÖŐÚÜŰ])',' ',t)
 t=re.sub(r'(?<=[a-záéíóöőúüű]),(?=\S)',', ',t)
 t=re.sub(r'(?<=[²³])(?=[a-záéíóöőúüű])',' ',t)
 t=re.sub(r':(?=[0-9A-Za-zÁÉÍÓÖŐÚÜŰ])',': ',t)
 return t
oldtxt=d.txt;oldwrap=d.wrap
def clean_txt(g,x,y,t,*a,**kw):return oldtxt(g,x,y,readable(t),*a,**kw)
def clean_wrap(g,x,y,t,*a,**kw):return oldwrap(g,x,y,readable(t),*a,**kw)
d.txt=clean_txt;d.wrap=clean_wrap
def title(g,name,sub,scale,page):
 d.rect(g,5,5,410,287,None,d.INK,.2);d.txt(g,12,283,'A-902 / KYOTO INK / R05',3.4,True);d.txt(g,12,276,name,4.3,True);d.txt(g,12,270,sub,2.5);d.line(g,12,265,408,265,d.GREY,.12)
 d.rect(g,270,7,138,19,None,d.INK,.15);d.txt(g,274,21,'KI-R05 / 2026-10-27',2.7,True);d.txt(g,404,21,page,2.7,True,anchor='end');d.txt(g,274,16,'A3 / mm / '+scale,2.5);d.txt(g,274,11,'AJÁNLATI / FELMÉRÉSI TERV; NEM GYÁRTÁSI KIADÁS',2.2,c=d.RED)
 d.txt(g,12,17,'[D] tervadat  [J] új javaslat  [H] felmérés / gyártói méretezés szükséges',2.3);d.txt(g,12,12,'Az R05 eltérési lap elsőbbséget élvez az érintett R04 részlettel szemben.',2.3)
d.title=title
# Do not put a fresh invented brushstroke in place of the accepted image.
def no_fake_art(g,x,y,w,h,*args):
 d.txt(g,x+w/2,y+h*.50,'TUSMOTÍVUM:',2.8,True,anchor='middle');d.txt(g,x+w/2,y+h*.50-5,'az eredeti célkép szerint',2.4,anchor='middle');d.txt(g,x+w/2,y+h*.50-10,'nyomdai master még nyitott',2.1,anchor='middle')
d.ink_diagram=no_fake_art
for uid in ['TV-01','TV-02','WN-01','B62-01']:
 u=copy.deepcopy(U[uid]);u['visual_status']='R05 anyagkódok: '+', '.join(u['material_ids'])+'. A részletes technológia a R05 anyagcsomagban.'
 d.cabinet_sheet(u);d.detail_sheet(u)
# Complete W02 panel and edge geometry, quantity and printer layout.
u=U['ART-02'];u['modules']=[1050,1050];u['front_modules']=[1050,1050];u['visual_status']='MAT-05 Bely+Print1040.01 jelölt; két mező, keret nélkül. Nyomdai varrat helye és felső csatlakozás felmérendő.'
d.cabinet_sheet(u);d.detail_sheet(u)
doc,g=d.sheet('W01 / médiafal összehangolt homlokzat','A torony és az alatta lévő700mm-es front közös tengelyű; a világkoordináta nem fordítható meg véletlenül.','1:20 + részlet', 'W01-R05')
s=.05;x=22;y=77
d.rect(g,x,y+27.5,35,116.5,d.GRAPHITE);d.rect(g,x+35,y+27.5,130,116.5,HexColor('#a99b87'))
for j in range(4):d.rect(g,x+35+j*32.5,y+27.5,32.5,116.5,None)
off=0
for w in [700,650,650,650,650]:d.rect(g,x+off*s,y+7.5,w*s,20,d.GRAPHITE);off+=w
d.rect(g,x+65,y+63,72.645,41.7,HexColor('#151515'))
d.txt(g,x+101,y+83,'65 col TV',3,c=white,anchor='middle')
d.line(g,x+35,y+28,x+35,y+143,d.RED,.6);d.line(g,x+35,y+144,x+165,y+144,d.RED,.6);d.line(g,x,y+7,x+165,y+7,d.RED,.6)
d.hd(g,x,x+35,y-4,y,'700');d.hd(g,x+35,x+165,y-4,y,'4×650');d.hd(g,x,x+165,y-12,y,'3300 [D]');d.vd(g,y,y+144,x-8,x,'2880');d.vd(g,y+7.5,y+27.5,x+174,x+165,'400')
d.txt(g,22,245,'ELÖLNÉZET A TORONY FELŐL',3.1,True);d.txt(g,22,233,'A tusgrafikát a jobb oldali eredeti kép határozza meg.',2.8)
im=d.Image(220,133,182,121.333,str(d.reference_preview(REF)));g.add(im)
d.wrap(g,220,123,'Megőrzendő: sötét torony, folytonos tusgesztus, meleg függőleges/felső résfény, lebegő alsó tároló. A tervi panelosztás és méret felmérésre vár. A raszterkép nem méretezési vagy nyomdai bizonyíték.',180,3,4.5)
d.wrap(g,220,91,'R04 modellhiba javítva: a torony a célkép szerint a kamerához közelebbi végre kerül, Y=4,70–5,40m. Panel Y=5,40–8,00m. Az alsó sorrend700+4×650. A TV a panelmezővel együtt700mm-rel eltolódik; új konzolpozíció felmérendő.',180,3,4.5)
d.wrap(g,22,44,'TV konzol: teherbíró falba; a18mm dekorlap nem tartószerkezet. Tápegység és kötés az oldható AV-rekeszből elérhető. A frontot a LED-szervizhez nem kell megsemmisíteni.',380,2.8,4.2)
d.save(doc,'W01_R05_kompozicio','TV-01/02/03','méretezett összehangolt homlokzat')
doc,g=d.sheet('W02 / nyomtatási mezők és szerelési részlet','A keretezett150×220kép tétel helyébe teljes2100×2880falmező kerül.','1:20; rétegrend1:2','W02-R05')
x=25;y=79;s=.05
for j in range(2):
 d.rect(g,x+j*52.5,y,52.5,144,HexColor('#b4a793'));d.txt(g,x+j*52.5+26.25,y+70,f'P{j+1}',4,True,anchor='middle');d.hd(g,x+j*52.5,x+(j+1)*52.5,y-6,y,'1050')
d.hd(g,x,x+105,y-14,y,'2100');d.vd(g,y,y+144,x-9,x,'2880')
d.txt(g,25,246,'NETTÓ MEZŐ / A NYOMAT NINCS MÉG RÁHELYEZVE',3,True)
d.wrap(g,155,245,'Nettó:2,10×2,88=6,048m². Nyomdai előirányzat: két1340mm széles,2980mm hosszú sáv. Teljes7,9864m², árazva8,0m². Ebből a túlnyúlás/szélvágás1,9384m²; ez nem rejtett második fal.',244,3,4.5)
d.wrap(g,155,214,'A két1050mm mező100mm összes oldalsó ráhagyással1150mm, belefér a1330mm nyomtatható szélességbe. A végleges varratot a motívum kevésbé hangsúlyos részére kell tenni. A PDF-ben szereplő50mm ráhagyás technológiai javaslat, a nyomda felülírhatja.',244,3,4.5)
for xx,ww,col,lab in [(175,9,d.CORE,'18mm hordozó'),(184,9,d.EDGE,'18mm szerelőlégrés')]:d.rect(g,xx,107,ww,62,col);d.txt(g,xx-12,98,lab,2.6)
d.line(g,174.6,107,174.6,169,d.RED,.5);d.leader(g,174.5,140,155,183,'nyomat + gyártói ragasztó');d.hd(g,175,193,88,107,'36mm [J]')
d.wrap(g,230,168,'Sarkon nincs vastag képkeret. Élvédelem és visszafordulás próbadarabbal. Dugalj, kapcsoló és felső dobozolás helyét felmérés után kell a vektoros sablonba berajzolni.',165,3,4.5)
d.wrap(g,230,126,'KI-131:60000 grafika. KI-132:224000 nyomat. KI-133:177000 hordozó/él/rögzítés/szerelés. Összes461000Ft becslés; logisztika KI-151 közös keretben.',165,3,4.5)
d.wrap(g,25,44,'Nem alkalmazunk kitalált nyomdai profilt.1:1fekete/greige/szövés próba; nappali és2700K esti jóváhagyás. A célkép felső lépcsőzése és falreturnje felmérésre vár: ez a lap csak a2100×2880tervi mezőt számszerűsíti.',375,2.8,4.2)
d.save(doc,'W02_R05_nyomat_es_reteg','ART-02','nyomatmezők, mennyiség, szerelés')

# Lighting proposal: actual strip identity, explicit compatibility gate.
light={'revision':'KI-R05','element':'KI-114','strip':{'manufacturer':'Häfele','sku':'833.74.308','model':'Loox5 LED2074','voltage':12,'w_per_m':9.6,'kelvin':2700,'cri':'>90','max_recommended_segment_m':4,'source':'https://files.hafele.co.uk/catalogfiles/www/25-1010.pdf'},'segments':[{'id':'W01-TOP','m':2.6,'supply':'PS-A','watts':24.96},{'id':'W01-VERT','m':2.33,'supply':'PS-A','watts':22.368},{'id':'W01-LOW','m':3.3,'supply':'PS-B','watts':31.68}],'supplies':[{'id':'PS-A','voltage':12,'rating_w':60,'load_w':47.328,'load_percent':78.88,'sku':'supplier selection pending'},{'id':'PS-B','voltage':12,'rating_w':60,'load_w':31.68,'load_percent':52.8,'sku':'supplier selection pending'}],'controller':{'candidate':'Gledopto GL-C-009P (full size, not Mini)','each_channel_a_max':5,'source':'https://gledopto.com/h-pd-134.html','gate':'Native Hue bridge pairing, dimming and power recovery test required. No automatic Hue certification claim.'},'budget_breakdown':[['10m LED purchased',10,4500,45000],['10m profile+diffuser purchased',10,2500,25000],['60W12V power supplies',2,12000,24000],['controllers',2,12000,24000],['connectors/cable allowance',1,12000,12000],['local installation',1,20000,20000]],'expected':150000,'cost_status':'Every rate is an allowance, not a supplier quotation; retained KI-114 total','service':'Two ventilated accessible AV compartments; low-voltage cable routes behind removable panels; mains separation and protective design by electrician','open':'Cutting pitch/profile depth/hotspot test; actual230Vpoint; cable sizing/drop; connectors/power supply approval; Hue bridge compatibility'}
(O/'data/W01_light_circuit.json').write_text(json.dumps(light,ensure_ascii=False,indent=2))
doc,g=d.sheet('W01 / három fényvonal, két szervizelhető kör','A fényforrás és a vezérlés külön ellenőrzött. A Zigbee felirat önmagában nem Hue-próba.','kapcsolási elv; mm','EL-W01-R05')
for yy,label,watt,branch in [(225,'Felső2,60m',24.96,'PS-A'),(180,'Függőleges2,33m',22.368,'PS-A'),(135,'Alsó3,30m',31.68,'PS-B')]:
 d.rect(g,260,yy-10,125,22,d.CORE);d.txt(g,265,yy+3,label+' / '+str(round(watt,2))+'W',3.2,True);d.txt(g,265,yy-4,'Loox5 LED2074 / 833.74.308 /12V',2.8)
 d.line(g,210,yy,260,yy,d.RED,.4);d.txt(g,215,yy+3,branch,2.8)
for yy,lab in [(202,'PS-A60W / terhelés47,33W'),(135,'PS-B60W / terhelés31,68W')]:
 d.rect(g,100,yy-14,110,27,HexColor('#d8d3ca'));d.txt(g,105,yy+5,lab,3,True);d.txt(g,105,yy-4,'12V táp + GL-C-009P jelölt',2.8)
 d.line(g,60,yy,100,yy,d.INK,.3)
d.line(g,60,135,60,202,d.INK,.3);d.txt(g,18,213,'230V [H]',3.2,True);d.wrap(g,18,196,'Tényleges kiállás és védelmek villanyszerelői ellenőrzéssel.',65,2.8,4.2)
d.line(g,210,202,225,202,d.RED,.4);d.line(g,225,180,225,225,d.RED,.4)
d.wrap(g,20,94,'PS-A két külön párhuzamos LED-ágat táplál. Nem kötjük egyetlen4,93m szalaggá: a gyártó4m ajánlott ághosszt ad meg. A12V és24V rendszerek nem keverhetők. A konkrét tápegység, csatlakozó, profil és kábelméret még szakági kiválasztás.',380,3,4.7)
d.wrap(g,20,65,'Tervi összterhelés78,?W helyett pontosan78,? nem használható: a számított összeg78,? ellenőrzése a mellékelt JSON alapján.',380,3,4.5) if False else None
d.wrap(g,20,65,'Összes terhelés78,?'.replace('78,?',f"{sum(a['watts'] for a in light['segments']):.3f}" )+'W. Két5m tekercs a rendelési alap; a maradék1,77m szerelési tartalék, nem új fényvonal. Árkeret150000Ft, tételes becslés; fotometriai és hőpróba nincs.',380,3,4.7)
d.save(doc,'EL_W01_R05','KI-114','fényvonalak, terhelések, szerviz')

# Editable production-layout templates. They intentionally contain no substitute ink design.
templates=[]
for code,w,h,mods in [('W01',3300,2880,[700,650,650,650,650]),('W02',2100,2880,[1050,1050]),('WN01',2920,2840,[486.5,486.5,487,487,486.5,486.5])]:
 lines=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}">','<title>KI-R05 production layout; not final print artwork</title>','<g id="CUT_GUIDES" fill="none" stroke="#c00000" stroke-width="1">',f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}"/>'];off=0
 for m in mods[:-1]:off+=m;lines.append(f'<path d="M{off},0 V{h}"/>')
 lines+=['</g>','<g id="APPROVED_INK_MASTER_PENDING"/>',f'<text x="50" y="100" font-size="32">{code} / original ink master required / KI-R05</text>','</svg>'];f=O/'artwork'/f'{code}_R05_nyomdai_kiosztasi_sablon.svg';f.write_text('\n'.join(lines));templates.append({'code':code,'file':str(f.relative_to(P)),'width_mm':w,'height_mm':h,'status':'Szerkeszthető kiosztási sablon. NEM kész grafika, NEM nyomtatandó piros segédvonal.'})
(O/'artwork/manifest.json').write_text(json.dumps(templates,ensure_ascii=False,indent=2))

# Concise portrait material and RFQ book, fully readable at A4.
W,H=A4;style=ParagraphStyle('body',fontName='KI',fontSize=10.2,leading=14,textColor=HexColor('#252522'));small=ParagraphStyle('small',parent=style,fontSize=8.5,leading=11)
def para(c,text,x,y,width=499,sty=style):
 p=Paragraph(html.escape(readable(text)),sty);ww,hh=p.wrap(width,900);p.drawOn(c,x,y-hh);return y-hh
def head(c,title,n,sub='KI-R05 / 2026-10-27 / ajánlatkérés és egyeztetés'):
 c.setFillColor(HexColor('#303C3B'));c.rect(0,H-100,W,100,fill=1,stroke=0);c.setFillColor(white);c.setFont('KIB',19);c.drawString(43,H-50,title);c.setFont('KI',9);c.drawString(43,H-74,sub);c.setFillColor(HexColor('#252522'));c.setFont('KI',8);c.drawString(43,24,'A902 / Kyoto Ink / gyártási és rendelési jóváhagyás nincs');c.drawRightString(W-43,24,str(n))
def sect(c,title,body,y):
 c.setFont('KIB',12);c.drawString(43,y,readable(title));return para(c,body,43,y-10)-20
matpdf=O/'materials/A902_R05_anyag_es_ajanlatkeresi_csomag.pdf';c=canvas.Canvas(str(matpdf),pagesize=A4)
for i,m in enumerate(M):
 head(c,m['id']+' / '+m['name'],i+1);c.setFillColor(HexColor(m['hex']));c.rect(43,H-196,92,65,fill=1,stroke=0);c.setFillColor(HexColor('#252522'));para(c,m['candidate'],153,H-134,390);para(c,'Tájékoztató rajzi szín. A négyzet nem valódi anyagminta.',153,H-171,390,small)
 y=H-230;y=sect(c,'Hol jelenik meg?',m['use'],y);y=sect(c,'Hogyan készül?',m['method'],y);y=sect(c,'Mi szükséges az elfogadáshoz?',m['gate'],y);y=sect(c,'Hogyan szerepel az árban?',m['price'],y);y=sect(c,'Forrás és ellenőrzés',m['source']+' / műszaki forrás olvasva2026-10-27; a helyi tervfájl nem beszállítói bizonyíték.',y);c.showPage()
head(c,'Árak és összehasonlítható tartalom',11);y=H-131
for label,val in [('Fő előrejelzés',C['main']),('Takarékos összehasonlítás',C['economy']),('18 milliós célhoz fennmaradó különbség',C['economy_gap']),('Érintetlen külön tartalék',C['reserve'])]:
 c.setFont('KI',11);c.drawString(43,y,label);c.setFont('KIB',12);c.drawRightString(W-43,y,f'{val:,.0f} Ft'.replace(',',' '));y-=31
y-=10
for e in E:y=sect(c,e['id']+' / '+f"{e['saving']:,.0f} Ft becsült megtakarítás".replace(',',' '),e['basis']+' '+e['compromise']+'.',y)
para(c,'A megtakarítások még nem beszállítói vállalások. A 23,913M főösszeghez képest0,253M csökkenés látszik; az18M eléréséhez ezen túl5,660M hiányzik. Nem töröltük a jakuzzit, a második fagyasztót vagy a kért fiókokat. A 20,415–32,032M sáv becslési tartomány, nem statisztikai garancia.',43,y);c.showPage()
rfqs=[('Asztalos és kárpitos','R05 aktuális rajzcsomag:33szerkezet, a R05index szerint. WN8fiók/2lift; WS,W52,W53 megőrzött rekeszek. Árazza külön a korpuszt, frontot, vasalatot, felületet, nyomatot, szerelést, logisztikát és mintát. A6magasWNfront nem készülhet engedély nélkül vízszintes toldással. A TVtorony 697×2327×19mm frontjának számított csupasz tömege23,1kg; pánt és merevítő méretezendő. A széles fiókokhoz 30/40/60kg vasalatot tényleges használati tömeg alapján válasszon.','KI-006..015;030..032;037..038;046..052;060..061;072..073;083;086;092..095;098;R05 anyagkódok.'),('Nyomda és felületkivitelező','Az eredeti célképek szerint készítsen1:1grafikai mintát. W01panel6,058m²+torony1,622m²; W02nettó6,048m², rendelési előirányzat8,0m². WNminta folytonos a6fronton, a3mmréseket kihagyva. Külön ár:sík nyomat; kézzel finoman texturált nyomat; valódi relief. A főváltozatban relief nincs. A nyomda adja meg azICCprofilt, felbontást, végleges ráhagyást és illesztést.','KI-030;051;131..133. A különbözeti árakat a meglévő csomaghoz kell egyeztetni, nem dupla összegként.'),('Villanyszerelő és világításintegrátor','W01:3külön12Vág, két60Wtáp, két dimmerjelölt, összes78,?W'.replace('78,?',f"{sum(a['watts'] for a in light['segments']):.3f}")+'. Loox5LED2074/2700K/9,6Wm. Felső2,6m és függőleges2,33m külön párhuzamos ág; alsó3,3m. WN7×3,5W=24,5W egy30Wdriver jelölttel, eredeti többi kör változatlan. Kérünk vezetékhossz-, feszültségesés-, hő- és hozzáférési ellenőrzést, Hue-párosítási és áram-visszatérési próbát. Thermosztát és hűtő-fűtő mennyezet külön szakág.','KI-104..108;114;119;CP3-L01/L02/L03/L04;R05-L01. A helyi150000Ft W01keret nem fix vállalás.')]
for i,(name,scope,codes) in enumerate(rfqs):
 head(c,'Ajánlatkérés / '+name,12+i);y=sect(c,'Egységes műszaki tartalom',scope,H-135);y=sect(c,'Kapcsolódó költségsorok',codes,y);y=sect(c,'Kérjük külön visszaigazolni','Bruttó egységár és mennyiség, ajánlat érvényessége, szállítás/felhordás, szerelés, garancia, kizárások, szükséges felmérés, legkorábbi gyártás és vállalt átfutás. Ugyanaz a rajzrevízió szerepeljen az ajánlaton. Helyettesítő terméket pontos SKU-val, mintával és külön árkülönbözettel nevezzen meg.',y);y=sect(c,'Átadási feltétel','Felmérés utáni gyártói rajzjóváhagyás; helyszíni anyagminta; beüzemelési vagy terhelési próba; dokumentált szervizhozzáférés. A csomag előkészített, nem kiküldött ajánlatkérés.',y);c.showPage()
c.save()

# Assemble current furniture sheets without regenerating valid unaffected R04 pages.
writer=PdfWriter();index=[]
for u in D['units']:
 for page in ['01','02']:
  f=O/'drawings'/f"{u['id']}_{page}.pdf"
  if not f.exists():f=P/'R04/drawings'/f"{u['id']}_{page}.pdf"
  if not f.exists():raise FileNotFoundError(f)
  index.append({'unit':u['id'],'page':page,'path':str(f.relative_to(P)),'revision':'KI-R05' if 'R05' in f.parts else 'KI-R04 retained','sha256':hashlib.sha256(f.read_bytes()).hexdigest()});writer.append(str(f))
for name in ['W01_R05_kompozicio','W02_R05_nyomat_es_reteg','EL_W01_R05']:
 f=O/'drawings'/(name+'.pdf');writer.append(str(f));index.append({'unit':name,'path':str(f.relative_to(P)),'revision':'KI-R05'})
for name in ['AT8-01_01','AT8-01_02','T-0-26_01','T-0-26_02']:
 f=P/'R04/drawings'/(name+'.pdf')
 if f.exists():writer.append(str(f));index.append({'unit':name,'path':str(f.relative_to(P)),'revision':'KI-R04 retained; R05 bike candidate in cost/material appendix'})
writer.write(str(O/'drawings/A902_R05_aktualis_butorrajzok.pdf'))
(O/'data/drawing_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2))

# Exactly five owner pages, using the actual project drawings and budget.
c=canvas.Canvas(str(O/'owner/A902_R05_tulajdonosi_utmutato_5oldal.pdf'),pagesize=A4)
head(c,'Kyoto Ink: a látványból otthon',1)
c.drawImage(ImageReader(str(REF)),43,H-440,width=509,height=339.33,preserveAspectRatio=True,anchor='c')
y=H-466;y=sect(c,'Mi lesz benne a legjobb?','A sötét médiafal és az egybefutó tusgrafika adja a nappali karakterét. A meleg fényvonalak kiemelik a felületet, a tároló pedig elrejti a napi tárgyakat. A hálóban a nyugodt külső mögött sok akasztós hely és fiók lesz. A két külön tároló tehermentesít, de nem helyettesíti a lakáson belüli napi tárolást.',y)
para(c,'Ez a kép a cél. A mostani műszaki modell még egyszerűsített bútorformákat tartalmaz, ezért a kész látvány egyezése nincs igazolva. A rajz, az anyagminta, az ajánlat és a végleges3Dtermék ugyanahhoz az elemkódhoz kapcsolódik.',43,y);c.showPage()
head(c,'Miért kerül ennyibe?',2);y=H-139
for lab,val in [('Jelenlegi teljes előrejelzés',C['main']),('Takarékos összehasonlítás',C['economy']),('Tervi bizonytalansági sáv alsó széle',C['low']),('Tervi bizonytalansági sáv felső széle',C['high'])]:
 c.setFont('KI',11);c.drawString(43,y,lab);c.setFont('KIB',14);c.drawRightString(W-43,y,f'{val/1e6:.3f} M Ft'.replace('.',','));y-=33
y=sect(c,'Nem csak a képen látható bútorokat fizetjük','A teljes lakás és kültér, az egyedi tárolóbelsők, világítás, gépek, textilek, falak, jakuzzi és szerelési háttér is szerepel. A nagy szekrények ára a fiókokkal, liftekkel, pántokkal és beépítéssel nő meg; ezek adják a használati érték jelentős részét.',y-18)
y=sect(c,'Mennyire biztos ez az összeg?',f"{C['verified']/1e6:.3f}M Ft ellenőrzött webshopárú rész; írásos beszállítói ajánlat jelenleg0Ft; {C['estimated']/1e6:.3f}M Ft becsült rész. A webshopár sem visszaigazolt magyar címre szállítás. A2M tartalék érintetlen; a18M célhoz a főváltozatból5,913M hiányzik.",y)
y=sect(c,'Mitől lehet olcsóbb?','Három konkrét csere253ezer Ft becsült megtakarítást ad: síkabb médiafalfelület, egyszerűbb W02hordozó és fix fürdődugalj. Fiókot, gardróbot és jakuzzit nem hagytunk el. A további nagy különbségre összehasonlítható ajánlatok kellenek; nem ígérhető, hogy puszta alkuból eltűnik.',y);c.showPage()
head(c,'Miért ennyi idő? Mi jöhet közbe?',3);y=H-135
timeline=[('0–2.hét','Közös felmérés, minták, gép- és vasalatválasztás. Egy tulajdonosi döntési kör.'),('2–4.hét','Összehasonlítható ajánlatok, gyártói rajzok, anyag és költség lezárása.'),('4–10.hét','Jóváhagyás és megrendelés után gyártás/beszerzés; közben helyszíni előkészítés.'),('10–14.hét','Beépítés, textilek, lámpák, gépek, terasz és vezérlés összehangolása.'),('14–16.hét','Próbaüzem, hibajavítás, takarítás és dokumentált átadás.')]
for a,b in timeline:y=sect(c,a,b,y)
y=sect(c,'Ami valóban késleltethet','Eltérő kész méret, meg nem oldott ajtó/fiókütközés, hosszú gyártási idejű kanapé vagy szövet, nem megfelelő anyagminta, gyártói kapacitás, emelési és jakuzzibekötési feltételek. A3–4hónap feltételes időtáv a döntések és rendelések indulásától, nem mai naptól vállalt határidő.',y);c.showPage()
head(c,'Mire lesz használható? Megéri?',4);y=H-135
for title,body in [('Master','WNterv:3,350m akasztórúd,8fiók,436,9liter geometriai fióktér,2,036m²polc és2lift. A régi változathoz képest több fióktér, de1,356m²-rel kevesebb polc; ezt külön mérlegelni kell.'),('05.2 és05.3','05.2 elsődlegesen nagy gardrób, később alakítható gyerekszoba.05.3 vendég és teljes értékű munka. A szék–ágy ütközése még nyitott; ezt nem fedi el egy szép render.'),('AT8-01','Második fagyasztó,12próbadoboznyi tartalékkészlet és ritkán használt kisgépek. A nagy gép ugyanazt a polchelyet foglalja, nem plusz kapacitás.'),('T-0-26','Két polcrendszer,3próbabőrönd,9próbadoboz és egy függőleges kerékpárhely. A valós bicikli, a tartó és az ajtó/kiemelési út még ellenőrizendő.')]:y=sect(c,title,body,y)
para(c,'A ráfordítás akkor éri meg, ha a napi használatot szolgáló belsők és a sokáig szerethető, egységes külső fontosak. Eladásiérték-növekedést ebből nem lehet bizonyítani. Érdemes a mintákra és a pontos illeszkedésre költeni, mielőtt drága felületeket gyártatunk újra.',43,y)
u=U['WN-01'];sc=.05;xx=43;yy=55;c.setStrokeColor(HexColor('#45423e'));c.setLineWidth(.5)
for b in u['cp3_bays']:
 bx=xx+b['offset']*sc;ww=b['module_w']*sc;c.setFillColor(HexColor('#ede9e1'));c.rect(bx,yy,ww,u['h']*sc,fill=1,stroke=1)
 for z in b['shelves_mm']:c.line(bx,yy+z*sc,bx+ww,yy+z*sc)
 for z in b['rails_mm']:c.setLineWidth(1.5);c.line(bx+4,yy+z*sc,bx+ww-4,yy+z*sc);c.setLineWidth(.5)
 for z in b['drawer_z']:c.rect(bx+4,yy+z*sc,ww-8,b['drawer_inner_mm'][2]*sc,fill=0,stroke=1)
c.setFillColor(HexColor('#252522'));para(c,'A tényleges WN belső kiosztás kicsinyített vázlata. Balra hosszú ruha, középen két akasztási szint, jobbra fiókok és felső lift. A részletes rajzon minden rekesz külön méretezett.',215,190,335);c.showPage()
head(c,'Hogyan lehet hamarabb kész?',5);y=H-135
for title,body in [('1. Egy közös felmérés','Asztalos és villanyszerelő ugyanazokat a kész falsíkokat, kiállásokat, küszöböt és szervizhelyeket ellenőrizze. A két külön tároló is kerüljön bele. A közös adatok csökkentik az újratervezést.'),('2. Egy kis, teljes mintasarok','Médiafal600×600mm, valódi fekete motívum, frontfuga és fényprofil együtt. Mellé gardróbfront, kárpit és W02nyomat. Egy alkalommal nappali és esti ellenőrzés.'),('3. Egy azonos tartalmú ajánlati kör','Ugyanaz a rajzrevízió és tételsor menjen minden szakembernek. Legyen külön anyag, munka, logisztika és érvényesség. Az elkészített csomagot még nem küldtük el.'),('4. Előbb a hosszú átfutású döntések','A fő kanapé, fronttechnológia, kárpit, vasalat és nagy fényforrás legyen az első döntés. Rendelés csak jóváhagyott méret és ár után; a rövid út nem a felmérés kihagyása.')]:y=sect(c,title,body,y)
y=sect(c,'A következő három tulajdonosi döntés','A médiafal fizikai felületi mintája; a WNgardrób nagyobb fiókterének és kisebb polcfelületének elfogadása; az ajánlatok után a látványtartás és18M cél közötti konkrét választás. Most nem kell minden helyiségre külön jóváhagyást adni.',y)
xx=43;yy=53;sc=29
c.setStrokeColor(HexColor('#b5b7b2'));c.setLineWidth(.7)
for rs in D['rooms'].values():
 for x0,y0,x1,y1 in rs:c.setFillColor(HexColor('#f2f1ec'));c.rect(xx+x0*sc,yy+y0*sc,(x1-x0)*sc,(y1-y0)*sc,fill=1,stroke=1)
for u in D['units']:
 a,b=(u['d'],u['w']) if u.get('opening_dir') in ['+x','-x'] else (u['w'],u['d']);c.setFillColor(HexColor('#9f998c'));c.rect(xx+u['x']*sc,yy+u['y']*sc,a/1000*sc,b/1000*sc,fill=1,stroke=0)
for it in D['items']:
 if it['room'] in ['04','03','05.1','05.2','05.3']:
  a,b=(it['d'],it['w']) if it.get('rot',0)%180==90 else (it['w'],it['d'])
  c.setStrokeColor(HexColor('#537272'));c.rect(xx+it['x']*sc,yy+it['y']*sc,a/1000*sc,b/1000*sc,fill=0,stroke=1)
c.setFillColor(HexColor('#252522'));c.setFont('KI',8)
for lab,x0,y0 in [('05.1 Master',.3,6.7),('05.2',.6,1.7),('Nappali / étkező',5.9,7.6),('Konyha',8.6,2.8),('Előtér',5.7,.8),('Közlekedő',2.6,3.2),('WC',5.7,3.2),('06.1',4.1,1.2),('05.3 Vendég / munka',11,7.6),('06.2',14.6,6.7)]:c.drawString(xx+x0*sc,yy+y0*sc,lab)
c.setFont('KI',8);c.drawString(43,yy+9.2*sc,'A tényleges tervből: berendezési áttekintés. A nyitott ütközések még ellenőrizendők.')
c.showPage();c.save()
print('R05 drawings',len(index),'owner pages',len(PdfReader(O/'owner/A902_R05_tulajdonosi_utmutato_5oldal.pdf').pages),'materials pages',len(PdfReader(matpdf).pages))
