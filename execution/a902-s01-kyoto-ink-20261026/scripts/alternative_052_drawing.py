from pathlib import Path
import json,math
from reportlab.graphics.shapes import Drawing,Rect,Line,String,PolyLine
from reportlab.graphics import renderPDF,renderSVG
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pypdf import PdfReader,PdfWriter
P=Path(__file__).resolve().parents[1];D=json.loads((P/'data/design_R02.json').read_text());A=json.loads((P/'blender/alternative_052_check.json').read_text());pdfmetrics.registerFont(TTFont('Arial','/System/Library/Fonts/Supplemental/Arial.ttf'));d=Drawing(1190.55,841.89);ink=colors.HexColor('#263b39');red=colors.HexColor('#a44a35');pale=colors.HexColor('#efece5')
def tx(x,y,s,z=11,col=ink):d.add(String(x,y,s,fontName='Arial',fontSize=z,fillColor=col))
def rc(x,y,w,h,c=pale):d.add(Rect(x,y,w,h,strokeColor=ink,fillColor=c,strokeWidth=.7))
def ln(x,y,X,Y,col=ink):d.add(Line(x,y,X,Y,strokeColor=col,strokeWidth=.7))
rc(25,25,1140,792,colors.white);tx(45,785,'ALT-052 | Gardróbba integrált munkahely',22);tx(45,760,'R02 | mm | NEM ELFOGADOTT ALTERNATÍVA | a fő változat és főösszeg nem módosult',11,red)
sc=130;ox=65;oy=220;rc(ox,oy,3.65*sc,2.65*sc);rc(ox,oy+2.65*sc,2.42*sc,.7*sc)
for a in A['objects']:
 b=a['bounds']
 if b[2]>1:continue
 rc(ox+b[0]*sc,oy+b[1]*sc,(b[3]-b[0])*sc,(b[4]-b[1])*sc,colors.HexColor('#bbae9e'));tx(ox+b[0]*sc+3,oy+b[1]*sc+9,a['id'],9)
for i in D['items']:
 if i['id']!='KI-058':continue
 rc(ox+i['x']*sc,oy+i['y']*sc,i['d']/1000*sc,i['w']/1000*sc);tx(ox+i['x']*sc+15,oy+i['y']*sc+90,'SLATTUM160 változatlan',11)
for hx,hy,r,base,sign in [(0,1.03,.91,math.pi/2,-1),(3.574,2.65,.9,math.pi,1)]:
 pts=[]
 for deg in range(0,91,5):a=base+sign*math.radians(deg);pts += [ox+(hx+r*math.cos(a))*sc,oy+(hy+r*math.sin(a))*sc]
 d.add(PolyLine(pts,strokeColor=red,strokeWidth=1,fillColor=None));ln(ox+hx*sc,oy+hy*sc,pts[-2],pts[-1],red)
tx(65,185,'Alaprajz: a160-as ágy és1000mm munkahely megmarad.',12)
tx(65,162,'A05.2 belső és erkélyajtó mintavett nyitása:0jelzés.',11)
tx(65,141,'Korlát: tárolónyitás, szék használati tér és rögzítés még ellenőrizendő.',10,red)
x=675;y=220;s=.16;rc(x,y,2380*s,2840*s);ln(x+1380*s,y,x+1380*s,y+2840*s);ln(x+690*s,y,x+690*s,y+2840*s);rc(x+1380*s,y+750*s,1000*s,1090*s,colors.white);ln(x+1380*s,y+750*s,x+2380*s,y+750*s);tx(x+10,y+200,'1380mm teljes magas tároló',11);tx(x+1380*s+8,y+130,'1000mm asztal',11);tx(x+1380*s+8,y+350,'Felső tároló',11);tx(x,y-25,'Elölnézet:2380×2840; mélység600; asztal750mm magas.',11)
tx(65,100,'Kompromisszum:2380→1380mm teljes magas gardrób; felső tároló részben visszapótolja a térfogatot.',12,red)
tx(65,77,'Költség: régi KI-060/061/062 csomag315000Ft → alternatíva395000Ft; +80000Ft (±40000) becslés.',11)
tx(65,55,'Bontás: kisebb gardrób165000 + asztal80000 + felső tároló90000 + szerelés/rögzítés60000Ft. Ajánlat és döntés kell.',10)
renderPDF.drawToFile(d,str(P/'drawings/ALT-052.pdf'));renderSVG.drawToFile(d,str(P/'drawings/ALT-052.svg'))
w=PdfWriter();w.append(str(P/'outputs/A902_R02_rajzcsomag.pdf'));w.append(str(P/'drawings/ALT-052.pdf'));w.write(str(P/'outputs/A902_R02_rajzcsomag.pdf'))
A['cost_breakdown_huf']={'replaced_KI060_061_062':315000,'wardrobe':165000,'desk':80000,'upper':90000,'installation':60000,'new_total':395000,'delta':80000,'uncertainty_plus_minus':40000,'included_in_main':False};(P/'data/alternative_052.json').write_text(json.dumps(A,ensure_ascii=False,indent=2));print('Drawing78pages incl conditional alternative')
