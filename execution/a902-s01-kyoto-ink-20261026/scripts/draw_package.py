from pathlib import Path
import json,math,textwrap,csv
from reportlab.graphics.shapes import Drawing,Rect,Line,String,Circle,PolyLine,Path as GPath
from reportlab.graphics import renderPDF,renderSVG
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,landscape,A3
from pypdf import PdfReader,PdfWriter
P=Path(__file__).resolve().parents[1];D=json.loads((P/'data/design_R02.json').read_text());G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text());R=json.loads((P/'data/elemek.json').read_text());C=json.loads((P/'data/cost_snapshot_R02.json').read_text())
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'))
INK=colors.HexColor('#253c3b');GREY=colors.HexColor('#6d7471');PAPER=colors.HexColor('#f3f0e9');RED=colors.HexColor('#a94d36');TAUPE=colors.HexColor('#b9aa96')
def txt(d,x,y,s,size=10,color=INK):d.add(String(x,y,str(s),fontName='Arial',fontSize=size,fillColor=color))
def line(d,x1,y1,x2,y2,color=GREY,width=.6,dash=None):d.add(Line(x1,y1,x2,y2,strokeColor=color,strokeWidth=width,strokeDashArray=dash))
def rect(d,x,y,w,h,fill=None,color=GREY,width=.6):d.add(Rect(x,y,w,h,fillColor=fill,strokeColor=color,strokeWidth=width))
def para(d,x,y,s,width=100,size=10,leading=14):
 for l in textwrap.wrap(str(s),width):txt(d,x,y,l,size);y-=leading
 return y

def dim(d,x1,y1,x2,y2,label):
 line(d,x1,y1,x2,y2,INK,.6)
 if abs(y2-y1)<.1:
  for x in [x1,x2]:line(d,x-3,y1-3,x+3,y1+3,INK)
  txt(d,(x1+x2)/2-15,y1+5,label,10)
 else:
  for y in [y1,y2]:line(d,x1-3,y-3,x1+3,y+3,INK)
  txt(d,x1+5,(y1+y2)/2,label,10)
def frame(title,sub='R02 | 2026-10-26 | mm | Ajánlati terv, nem gyártásra kiadva'):
 d=Drawing(1190.55,841.89);rect(d,0,0,d.width,d.height,colors.white,color=colors.white);rect(d,25,25,1140,792);txt(d,45,787,title,21);txt(d,45,764,sub,11,RED);line(d,45,745,1145,745);return d

def export(d,name):
 renderPDF.drawToFile(d,str(P/'drawings'/f'{name}.pdf'));renderSVG.drawToFile(d,str(P/'drawings'/f'{name}.svg'))

def custom(u):
 d=frame(u['id']+' | '+u['name']);s=min(480/u['w'],340/u['h'],.45);x=80;y=360;w=u['w']*s;h=u['h']*s
 txt(d,x,720,'ELÖLNÉZET / FRONTKIOSZTÁS',12);rect(d,x,y,w,h,PAPER)
 pos=0
 for j,m in enumerate(u['modules']):
  xx=x+pos*s;rect(d,xx+1,y+1,m*s-2,h-2,None);txt(d,xx+4,y+h-16,str(j+1),10);pos+=m
  if u['drawers'] and u['kind']=='cabinet' and not u.get('interior'):
   nd=max(1,round(u['drawers']/len(u['modules'])));dh=min(u['h']/nd,230)
   for n in range(1,nd):line(d,xx,y+n*dh*s,xx+m*s,y+n*dh*s)
  elif u['kind']=='cabinet':line(d,xx+5,y+5,xx+m*s-5,y+h/2, GREY,.4,[3,3]);line(d,xx+m*s-5,y+h/2,xx+5,y+h-5,GREY,.4,[3,3])
 if u['id']=='K-01':
  for zz,hh,label in [(600,595,'HBA534EB3: niche590×564'),(1280,382,'BFL524MB0: niche365×564')]:
   rect(d,x+18*s,y+zz*s,564*s,hh*s,colors.HexColor('#d5d5d5'));line(d,x+w,y+(zz+hh/2)*s,x+w+40,y+(zz+hh/2)*s);txt(d,x+w+45,y+(zz+hh/2)*s,label,11)
 elif u['id']=='K-02':
  for zz in [700,1852]:line(d,x,y+zz*s,x+w,y+zz*s)
  txt(d,x+w+20,y+h/2,'KIN86VSE0 - frontosztás gyári rajzról',10)
 elif u['id'].startswith(('WN-','WS-','W52','W53')):
  line(d,x,y+2360*s,x+w,y+2360*s)
 if u['id'].startswith(('B62-01','B61-01')):
  rect(d,x+w/2-125*s,y+h-200*s,250*s,200*s,None,RED);txt(d,x+w+20,y+h/2,'Szifon250×200 célkivágás',10)
 if u['kind'] in ['panel','upholstery']:txt(d,x+8,y+h/2,'anyagmezők / nyomat külön SVG-ben',10)
 dim(d,x,y-22,x+w,y-22,str(u['w']));dim(d,x-25,y,x-25,y+h,str(u['h']))
 txt(d,x,285,'ALAPRAJZ / FELÜLNÉZET',12);pd=min(u['d']*s,135);rect(d,x,120,w,pd,PAPER);dim(d,x,100,x+w,100,str(u['w']));dim(d,x+w+15,120,x+w+15,120+pd,str(u['d']))
 txt(d,x,75,f"Elhelyezés: x={u['x']:.3f}; y={u['y']:.3f}; z={u['z']:.3f} m. Fordítás {u['rot']}°.",10)
 txt(d,x,58,f"Nyitási előirányzat: {u['opening']} mm / irány {u.get('opening_dir','PENDING')}.",10)
 # Side and a real internal section with shelf elevations.
 sx=680;sy=360;sd=max(25,min(u['d']*s,150));rect(d,sx,sy,sd,h,PAPER);rect(d,sx+3,sy+3,max(1,sd-6),h-6,None)
 txt(d,sx,720,'A-A OLDALMETSZET / BELSŐ',12)
 for i in range(0 if u['id'] in ['K-01','K-02'] else u['shelves']):
  hh=(i+1)*u['h']/(u['shelves']+1);line(d,sx+3,sy+hh*s,sx+sd-3,sy+hh*s);txt(d,sx+sd+12,sy+hh*s-3,str(round(hh))+' mm',9)
 if u['id'] in ['K-01','K-02']:
  txt(d,sx+sd+12,sy+h-30,'Gépnyílások: specifikáció szerint',9)
 dim(d,sx,sy-22,sx+sd,sy-22,str(u['d']))
 # readable notes dedicated right bottom and across lower strip
 yy=310
 for label,k in [('Méretek forrása','dimension_source'),('Anyag','material'),('Felület','front'),('Él / erezet','edge'),('Vasalat','hardware'),('Fogás / lábazat','handle'),('Szerelés','clearance'),('Szerviz','service')]:
  yy=para(d,650,yy,label+': '+u[k],77,9,12)-5
 txt(d,650,yy,'Költség: '+', '.join(u['cost']),10)
 export(d,u['id'])
 # Specification page contains item-specific construction, separate from identical cabinet conventions.
 d2=frame(u['id']+' | műszaki specifikáció és részletek')
 yy=710
 for title,content in [('Egyedi kialakítás',u['notes']),('Méret és gyártási kapu',u['dimension_source']+'. Végleges méretet a gyártó felmérési jegyzőkönyvvel rögzít. A rajz minden számadata ajánlati célérték.'),('Rétegrend és felület',u['material']+'; '+u['front']+'; '+u['edge']+'; erezet: '+u['grain']),('Működés és szerelés',u['hardware']+'. '+u['handle']+'. '+u['plinth']+'. '+u['clearance']),('Szerviz és szakági kapcsolat',u['service']+'. Szerelés előtt cső/kábelkeresés; mennyezeti hűtő-fűtő mezőbe nem rögzítünk. Falrögzítés alapanyaga és terhe nyitott.'),('Költség és jóváhagyás',', '.join(u['cost'])+'. Az Excelben szereplő csomagsorok megosztottak, a rajzlapok alapján nem összeadandók újra. Státusz: '+u['status'])]:
  txt(d2,55,yy,title,13);yy=para(d2,55,yy-22,content,155,11,16)-23
 # 1:2 generic edge/service detail actually labelled as system principle
 txt(d2,55,215,'CS-01 / BÚTORÉL ÉS HÁTSÓ SZERVIZSÁV - rendszerelv, méretek mm',12)
 rect(d2,70,90,250,36,PAPER);rect(d2,70,126,4,36,INK);dim(d2,340,90,340,126,'18');txt(d2,85,145,'18 mm lap + 2 mm élzárás',11)
 rect(d2,600,90,15,100,GREY);rect(d2,675,90,36,100,PAPER);dim(d2,615,80,675,80,'30 cél');txt(d2,735,125,'Levehető hát / kábel és szerviz',11);txt(d2,735,108,'Vizes bútornál szifon helye külön sablon.',10)
 export(d2,u['id']+'_spec')
 return [u['id'],u['id']+'_spec']

def bounds(o):
 w=o['w']/1000;dd=o['d']/1000
 if o['rot']==90:w,dd=dd,w
 return o['x'],o['y'],o['x']+w,o['y']+dd

def plan(title,name,area=(-2.3,-.5,17.1,9.5),electrical=False,terrace=False):
 d=frame(title,'R02 | 2026-10-26 | világkoordináták m; méretvonalak mm | Terv szerinti, nem helyszíni felmérés')
 x0,y0,x1,y1=area;sc=min(1040/(x1-x0),560/(y1-y0));ox=65-x0*sc;oy=135-y0*sc
 def xy(x,y):return ox+x*sc,oy+y*sc
 if terrace:
  for k,z in G['terrace_zones'].items():
   a,b,c,e=z['r'];xx,yy=xy(a,b);rect(d,xx,yy,(c-a)*sc,(e-b)*sc,colors.HexColor('#dde5d5') if not z['butorozhato'] else PAPER);txt(d,xx+3,yy+5,k,8)
 else:
  for k,rs in G['rooms'].items():
   for a,b,c,e in rs:
    xx,yy=xy(a,b);rect(d,xx,yy,(c-a)*sc,(e-b)*sc,PAPER,color=colors.white)
   a,b,c,e=max(rs,key=lambda r:(r[2]-r[0])*(r[3]-r[1]));xx,yy=xy((a+c)/2,(b+e)/2);txt(d,xx-20,yy,k,10) if electrical else None
  for k,v in G['walls'].items():
   if v[2]>1 or k.startswith('Plafon'):continue
   xx,yy=xy(v[0],v[1]);rect(d,xx,yy,(v[3]-v[0])*sc,(v[4]-v[1])*sc,INK)
  for k,m in G['openings_meta'].items():
   if not m.get('zsaner'):continue
   xx,yy=xy(*m['zsaner']);d.add(Circle(xx,yy,m['r']*sc,strokeColor=colors.HexColor('#bbbbbb'),strokeDashArray=[2,3],fillColor=None));txt(d,xx+3,yy+3,k.replace('Ajto_',''),7)
 for o in D['units']+D['items']:
  a,b,c,e=bounds(o)
  if terrace!=(o.get('room') in ['09','10','WPC','13']):continue
  if not terrace and o.get('z',0)>1:continue
  xx,yy=xy(a,b);rect(d,xx,yy,(c-a)*sc,(e-b)*sc,TAUPE if o.get('kind') not in ['panel','glass'] else None,color=GREY);txt(d,xx+2,yy+3,o['id'],7)
  # overall plan uses IDs; detailed dimensions are on individual sheets
 for it in D.get('fixed_existing',[]):
  if terrace:continue
  a,b,z,c,e,Z=it['bounds'];xx,yy=xy(a,b);rect(d,xx,yy,(c-a)*sc,(e-b)*sc,colors.white);txt(d,xx+2,yy+3,it['id'],7)
 if electrical:
  for l in D['lights']:
   if terrace!=(l['y']>8.5 or l['x']<0):continue
   xx,yy=xy(l['x'],l['y']);d.add(Circle(xx,yy,4,fillColor=colors.HexColor('#e0aa36'),strokeColor=RED));txt(d,xx+6,yy+4,l['id'],8,RED)
  txt(d,55,92,'Jel: arany kör = meglévő kiállás; L- jel = tervezett bútorfény meglévő forrásról. Áthelyezés nincs jóváhagyva.',11)
  txt(d,55,74,'Minden kábelút és táp a szakági jegyzékben; a pontos rejtett vezetés és védelmek szakági jóváhagyásra várnak.',11)
 else:
  txt(d,55,92,'Szaggatott kör: ajtó teljes sugárburka, konzervatív ellenőrzés; nem tényleges teljes nyitási kör.',11)
  txt(d,55,74,'A berendezés R02 ajánlati javaslat. Piros nyitott feltételek a Blender-jelentésben. Méretet a renderből nem vettünk.',11)
 dim(d,*xy(0,y0+.1),*xy(5,y0+.1),'5000 mm ellenőrző lépték')
 export(d,name);return name
names=[]
for u in D['units']:names+=custom(u)
names+=[plan('P-01 | Teljes lakás berendezési alaprajz','P-01_alaprajz'),plan('P-02 | Teljes kültér berendezési alaprajz','P-02_terasz',(-2.3,-.5,17.1,20.5),terrace=True),plan('E-01 | Világítási és kiállási egyeztető alaprajz','E-01_villamos',electrical=True),plan('E-02 | Kültéri világítás és szerviz','E-02_kulter',(-2.3,-.5,17.1,20.5),True,True)]
w=PdfWriter()
for n in names:w.append(str(P/'drawings'/f'{n}.pdf'))
w.write(str(P/'outputs/A902_R02_rajzcsomag.pdf'))
# Scaled artwork master. Artwork is a newly drawn proposal, never claimed pixel-identical approved original.
for id,wid,hei in [('ART-02',2100,2880),('TV-03',2600,2330),('WN-01',2920,2840)]:
 art=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{wid}mm" height="{hei}mm" viewBox="0 0 {wid} {hei}"><title>{id} R02 - jóváhagyandó tuskompozíció, nem végleges nyomdai állomány</title><rect width="100%" height="100%" fill="#b7aea0"/><g fill="#242421">'''
 if id=='ART-02':
  art+='<path d="M760 80 L1090 55 L1170 1030 L1030 1350 L1140 1780 L1080 2760 L810 2810 L850 1900 L760 1500 L850 1190 Z"/>'
  for i in range(18):art+=f'<path d="M{700+i*27} 120 Q{900+i*16} 1250 {750+i*29} 2770" fill="none" stroke="#242421" stroke-width="{2+i%5}"/>'
 else:art+=f'<path d="M0 {hei*.24} C{wid*.4} {hei*.15} {wid*.55} {hei*.62} {wid} {hei*.52} L{wid} {hei*.60} C{wid*.55} {hei*.7} {wid*.4} {hei*.23} 0 {hei*.32} Z"/>'
 art+='</g><g id="CUT_GUIDES_NONPRINT" stroke="#ff0000" stroke-width="1" fill="none">'
 divs=3 if id=='ART-02' else 4
 for i in range(1,divs):art+=f'<path d="M{wid*i/divs} 0 V{hei}"/>'
 art+='</g></svg>';(P/'drawings'/f'{id}_artwork_master.svg').write_text(art)
print('PDF drawing pages',len(names))
