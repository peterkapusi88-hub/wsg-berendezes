from pathlib import Path
import json,math,textwrap
from reportlab.graphics.shapes import Drawing,Rect,Line,String,PolyLine,Polygon,Circle
from reportlab.graphics import renderPDF,renderSVG
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfWriter
P=Path(__file__).resolve().parents[1];O=P/'CP3';D=json.loads((O/'data/design_CP3.json').read_text());L=json.loads((O/'data/belso_vilagitas.json').read_text())
pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'))
pdfmetrics.registerFont(TTFont('ArialB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
INK=colors.HexColor('#2b3633');PALE=colors.HexColor('#eee9df');GREY=colors.HexColor('#7b817d');RED=colors.HexColor('#a64d37');GOLD=colors.HexColor('#cb8e2e');BLUE=colors.HexColor('#477a89')
W,H=1190.55,841.89
def t(d,x,y,s,size=10,col=INK,bold=False):d.add(String(x,y,str(s),fontName='ArialB' if bold else 'Arial',fontSize=size,fillColor=col))
def ln(d,x,y,X,Y,col=GREY,width=.6,dash=None):d.add(Line(x,y,X,Y,strokeColor=col,strokeWidth=width,strokeDashArray=dash))
def r(d,x,y,w,h,fill=None,col=INK,width=.6):d.add(Rect(x,y,w,h,fillColor=fill,strokeColor=col,strokeWidth=width))
def para(d,x,y,s,width=63,size=10):
 for line in textwrap.wrap(str(s),width):t(d,x,y,line,size);y-=size*1.4
 return y-8
def dim(d,x,y,X,Y,label):
 ln(d,x,y,X,Y,INK)
 for a,b in [(x,y),(X,Y)]:ln(d,a-3,b-3,a+3,b+3,INK)
 if abs(Y-y)<1:t(d,(x+X)/2-12,y+6,label)
 else:t(d,x+5,(y+Y)/2,label)
def frame(title,sub):
 d=Drawing(W,H);r(d,0,0,W,H,colors.white,colors.white);r(d,25,25,W-50,H-50)
 t(d,45,784,title,20,bold=True);t(d,45,759,sub,11,RED);ln(d,45,742,W-45,742)
 t(d,45,44,'KI-CP3-R03 · 2026-10-27 · mm · [D] tervi méret [J] javaslat [H] felmérés / jóváhagyás szükséges',10)
 return d
allpages=[];index=[]
def output(d,name):
 f=O/'drawings'/name;renderPDF.drawToFile(d,str(f.with_suffix('.pdf')));renderSVG.drawToFile(d,str(f.with_suffix('.svg')));allpages.append(f.with_suffix('.pdf'));return f.with_suffix('.pdf')
def drawunit(u):
 pages=[];scale=next(n for n in [5,10,20,25,50] if u['w']*2.83465/n<=485 and u['h']*2.83465/n<=365);s=2.83465/scale;x=70;y=330;ww=u['w']*s;hh=u['h']*s
 d=frame(u['id']+'  '+u['name'],'01 · Belső kiosztás / metszet · 1:'+str(scale)+' A3-on · Ajánlati és felmérési terv')
 t(d,x,716,'NYITOTT ELÖLNÉZET',12,bold=True);r(d,x,y,ww,hh,PALE)
 for b in u['cp3_bays']:
  bx=x+b['offset']*s;cw=b['clear_w'];mw=b['module_w'];r(d,bx,y,18*s,hh,colors.HexColor('#bcb2a4'));r(d,bx+(mw-18)*s,y,18*s,hh,colors.HexColor('#bcb2a4'))
  t(d,bx+3,y+hh+11,'B'+str(b['bay']),10,bold=True)
  for z in b['shelves_mm']:r(d,bx+18*s,y+z*s,cw*s,18*s,colors.HexColor('#bcb2a4'))
  for j,z in enumerate(b['rails_mm']):
   islift=z in b['lift_rails_mm'];ln(d,bx+36*s,y+z*s,bx+(mw-36)*s,y+z*s,BLUE if islift else INK,2)
   if islift:
    ln(d,bx+55*s,y+z*s,bx+55*s,y+(z-480)*s,BLUE,1.4);ln(d,bx+(mw-55)*s,y+z*s,bx+(mw-55)*s,y+(z-480)*s,BLUE,1.4)
   if u['d']<550:t(d,bx+4,y+z*s+5,'előre 350',8,BLUE)
  for z in b['drawer_z']:r(d,bx+30*s,y+z*s,(mw-60)*s,(b['drawer_inner_mm'][2]+20)*s,None,INK);ln(d,bx+42*s,y+(z+20)*s,bx+(mw-42)*s,y+(z+20)*s)
  for z in b['lights_mm']:ln(d,bx+(mw-460 if cw>=500 else mw-250)/2*s,y+z*s,bx+(mw+460 if cw>=500 else mw+250)/2*s,y+z*s,GOLD,2)
  dim(d,bx,y-22,bx+mw*s,y-22,str(mw))
 if not u['cp3_bays']:
  pos=0
  for m in u['modules']:ln(d,x+pos*s,y,x+pos*s,y+hh);pos+=m
  if hh>100:para(d,x+10,y+hh/2,'Felület / szerkezeti mező. Nincs általános szekrénypánt.',max(25,int(ww/6)),10)
 if u['id']=='K-01':
  for z,h,label in [(600,595,'SÜTŐ'),(1280,382,'MIKRO')]:r(d,x+18*s,y+z*s,564*s,h*s,colors.HexColor('#707873'));t(d,x+22*s,y+(z+h/2)*s,label,9,colors.white)
 if u['id']=='K-02':r(d,x+18*s,y+80*s,564*s,1780*s,colors.HexColor('#d2d6d1'));t(d,x+8,y+hh/2,'HŰTŐ',10)
 if u['id'].startswith('B') and u['drawers']:r(d,x+(u['w']/2-125)*s,y+(u['h']-200)*s,250*s,200*s,None,RED,1.4)
 dim(d,x,y-45,x+ww,y-45,str(u['w'])+' [D]');dim(d,x-25,y,x-25,y+hh,str(u['h']))
 sx=570;sd=u['d']*s;t(d,sx,716,'A-A METSZET',12,bold=True);r(d,sx,y,sd,hh,None)
 if u['cp3_bays']:
  b=u['cp3_bays'][0]
  for z in b['shelves_mm']:r(d,sx+19*s,y+z*s,b['clear_d']*s,18*s,PALE)
  for z in b['rails_mm']:d.add(Circle(sx+u['d']/2*s,y+z*s,2,fillColor=INK))
  ln(d,sx+(u['d']-38)*s,y,sx+(u['d']-38)*s,y+hh,BLUE,.8,[3,3])
 dim(d,sx,y-25,sx+sd,y-25,str(u['d']))
 yy=710
 for label,text in [('Elhelyezés',f"x {u['x']:.3f} / y {u['y']:.3f} / z {u['z']:.3f} m; nyitás {u.get('opening_dir','nincs')}"),('Méretforrás',u['dimension_source']),('Szerkezet',u['material']),('Felület / él',u['front']+'; '+u['edge']),('Vasalat',u['hardware']),('Fény',u['internal_light']),('Költségkód',', '.join(u['cost']))]:
  t(d,740,yy,label,11,bold=True);yy=para(d,740,yy-17,text,61,10)-5
 t(d,70,240,'FELÜLNÉZET / SZERVIZSÁV',12,bold=True);pd=u['d']*s;r(d,70,110,ww,pd,PALE);ln(d,70,110+38*s,70+ww,110+38*s,BLUE,1,[4,3]);dim(d,70,90,70+ww,90,str(u['w']))
 t(d,70,66,'Hátsó 30 mm kábel/szerviz előirányzat + 8 mm hát. Fiók nettó méret nem gyártási szabásképlet.',9)
 # True scale bar in millimetres.
 ln(d,570,130,570+500*s,130,INK,2);t(d,570,112,'0');t(d,570+500*s-15,112,'500 mm')
 pages.append(output(d,u['id']+'_01'))
 d=frame(u['id']+'  Működés, rekeszméretek és kapcsolatok','02 · Zárt front / használat / részlet · [J] tervezett kialakítás; gyártásra még nem jóváhagyott')
 ss=min(2.83465/20,240/u['h'],430/u['w']);xx=65;yy=430
 r(d,xx,yy,u['w']*ss,u['h']*ss,PALE);pos=0
 for m in u['modules']:
  r(d,xx+(pos+1.5)*ss,yy+1.5*ss,(m-3)*ss,(u['h']-3)*ss)
  if u['h']>2400:ln(d,xx+pos*ss,yy+2360*ss,xx+(pos+m)*ss,yy+2360*ss)
  pos+=m
 t(d,65,700,'ZÁRT FRONT - V3.3 osztások megtartásával',12,bold=True)
 t(d,570,700,'HASZNÁLATI / SZERVIZRÉSZLET',12,bold=True)
 # Actual drawer travel sketch with dimensions, not generic hinges on panels.
 if any(b['drawers'] for b in u['cp3_bays']):
  b=next(b for b in u['cp3_bays'] if b['drawers']);s2=.23;r(d,590,530,u['d']*s2,120,PALE);r(d,590-b['runner_mm']*s2,550,b['runner_mm']*s2,42,None,BLUE);dim(d,590-b['runner_mm']*s2,520,590,520,str(b['runner_mm'])+' teljes kihúzás')
  para(d,795,642,'Fiók előtt a kihúzás teljes útja szabad. Belső fióknál az ajtó 155°-os nyitása és a szomszéd fogantyú külön ellenőrzendő.',51)
 elif u['kind']=='panel':
  r(d,590,530,7,110,PALE);r(d,620,530,12,110,PALE);dim(d,590,510,632,510,'réteg: '+str(u['d'])+' mm [D]')
  para(d,680,640,'Mechanikus függesztősín és levehető mező; nyomatot a panel- és ajtórésekre bontani. Elektromos szervizfedél nem ragasztható le.',69)
 else:
  r(d,590,530,150,100,PALE);ln(d,590,530,690,460,BLUE,1.5);para(d,785,640,'Ajtós elemnél a teljes nyitási ív, polc előtt a kézhely és a kiemelés helye ellenőrzendő. Nem ajtós elemnél ez nem pántelőírás.',54)
 para(d,570,477,'Fényút: helyiségi betáp [H] → hozzáférhető tápegység → oldalsó kábelcsatorna → polc alatti frontközeli fény. A tápegység nem kerülhet takart ruhakupac mögé.',89,10)
 headers=['Rekesz / funkció','Nettó Sz×Mé mm','Polc felső síkja mm','Rúd / lift mm','Fiók belső mm / db']
 xs=[55,330,480,730,920];y0=390
 for x,h in zip(xs,headers):t(d,x,y0,h,10,bold=True)
 ln(d,50,379,1140,379)
 for bi,b in enumerate(u['cp3_bays']):
  y0=354-bi*43
  para(d,xs[0],y0,b['id']+' '+b['purpose'],42,9)
  t(d,xs[1],y0,f"{b['clear_w']} × {b['clear_d']}",10)
  para(d,xs[2],y0,', '.join(map(str,b['shelves_mm'])) or 'nincs',36,9)
  para(d,xs[3],y0,', '.join(map(str,b['rails_mm']))+(' / lift '+','.join(map(str,b['lift_rails_mm'])) if b['lift_rails_mm'] else '') or 'nincs',27,9)
  t(d,xs[4],y0,'×'.join(map(str,b['drawer_inner_mm']))+' / '+str(b['drawers']),9)
 if not u['cp3_bays']:para(d,55,350,u['notes'],165,11)
 c=u.get('capacity',{});t(d,55,112,f"Kapacitás [J]: {c.get('rail_m',0):.3f} m akasztás · {c.get('shelf_m2',0):.3f} m² polc · {c.get('drawer_l',0):.1f} liter fiók",12,bold=True)
 para(d,55,91,'A nettó értékekből további 25% szabad tartalék javasolt. Terhelés, nyitási ütközés, fali rögzítés és kész belméret jóváhagyása még szükséges. A részletes alkatrész- és vasalatjegyzék az elemkódhoz kapcsolva.',169,9)
 pages.append(output(d,u['id']+'_02'))
 w=PdfWriter()
 for p in pages:w.append(str(p))
 w.write(str(O/'drawings'/f"{u['id']}_CP3.pdf"));index.append(dict(unit=u['id'],pdf=f"drawings/{u['id']}_CP3.pdf",pages=[len(allpages)-1,len(allpages)],scale=scale))
if __name__=='__main__':
 for u in D['units']:drawunit(u)
 w=PdfWriter()
 for p in allpages:w.append(str(p))
 w.compress_identical_objects(remove_identicals=True,remove_orphans=True)
 w.write(str(O/'drawings/A902_CP3_egyedi_butorok.pdf'))
 (O/'data/rajzjegyzek.json').write_text(json.dumps(index,ensure_ascii=False,indent=2))
 print('33 egyedi rajzpár; 66 A3 oldal, PDF + SVG; összefűzött rajzkönyv.')
