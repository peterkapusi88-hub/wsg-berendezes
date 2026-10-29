from pathlib import Path
import io
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
O=Path(__file__).resolve().parents[1]
pdfmetrics.registerFont(TTFont('A','/System/Library/Fonts/Supplemental/Arial.ttf'));pdfmetrics.registerFont(TTFont('AB','/System/Library/Fonts/Supplemental/Arial Bold.ttf'))
c=canvas.Canvas(str(O/'rajzok/S16_R14_ketiranyu_felso_vilagitas.pdf'),pagesize=(297*mm,210*mm));c.setTitle('S16 R14 - Kétirányú felső világítás és külső fényudvar')
def txt(x,y,t,size=10,bold=False):
 c.setFillColorRGB(.13,.14,.14);c.setFont('AB'if bold else'A',size);c.drawString(x*mm,y*mm,t)
def pic(name,x,y,w,h,crop=None):
 im=Image.open(O/'nezetek'/name).convert('RGB');im=im.crop(crop) if crop else im
 b=io.BytesIO();im.save(b,format='JPEG',quality=96,subsampling=0);b.seek(0);c.drawImage(ImageReader(b),x*mm,y*mm,w*mm,h*mm)
def foot(n):
 txt(12,7,'Tervezési és fényhatás-tanulmány. Az R05 műhelycsomagot még nem helyettesíti.',7);txt(275,7,str(n),7)
for i,(scene,title,sub)in enumerate([('este','S16 R14 | Faerezetes változat - este','Erősebb lefelé súrolófény, külön felfelé résfény, helyreállított jobb oldali külső fényudvar.'),('nappal','S16 R14 | Faerezetes változat - nappal','Azonos forma és anyagok, szórt fény az ÉK-i üvegfal helyéről. LED-ek nélkül.')],1):
 txt(12,198,title,14,True);txt(12,190,sub,8);pic(f'S16_R14_faerezet_{scene}_csukott.png',35.5,18,226,169.5);foot(i);c.showPage()
txt(12,198,'Újraépített csatlakozások - nappali nagyítás',14,True)
for name,x,y,label in [('felso_csatlakozas',12,105,'Folytonos külső ív; a háttér és a fénytakaró mögötte fut.'),('felso_jobb_iv',155,105,'Visszaállítva: szögletes felső jobb sarok, oldalkeret nélkül.'),('also_jobb_csatlakozas',12,14,'Egységes alsó külső felület; a háttér az ív mögé fut.')]:
 txt(x,y+84,label,7.4,True);pic('S16_R14_reszlet_'+name+'.png',x,y,110,82.5)
for j,t in enumerate(['TV-panel jobb széle: ismét 3500 mm.','Eredeti TV-panel-szélesség: 2630 mm.','A TV helye és 75 colos mérete változatlan.','A teljes bútor szélessége továbbra is 3600 mm.','','A háttér kész síkja 52 mm-rel hátrébb került.','A felső profil a szekrény hátsó síkja mögött marad.','A süllyesztett ajtótextil és a fióknyitások megmaradtak.','','A 8 mm-es hátsó hézag, a konkrét Hue-profil','és a távtartók rétegrendje műhelyi ellenőrzést igényel.']):txt(155,88-j*6,t,8)
foot(3);c.showPage()
txt(12,198,'Nyitott nézet - külön nyíló ajtók és fiók',14,True);txt(12,190,'A belső fény is meleg; a bal oldali süllyesztett textilbetét a saját ajtajával együtt mozog.',8);pic('S16_R14_faerezet_este_nyitott.png',35.5,18,226,169.5);foot(4);c.showPage()
txt(12,198,'Felső világítás - két külön irány',14,True)
txt(12,190,'Felfelé: a plafonrés megvilágítása. Lefelé: erősebb súrolófény a textilhatású panelen.',8)
pic('S16_R14_felso_ketiranyu_feny.png',12,40,273,136.5,crop=(0,320,1280,960))
txt(12,29,'A fő bútor teteje 2875 mm, a plafon 2900 mm: a névleges rés 25 mm.',9)
txt(12,22,'A bemutatott felső profil 4 mm-t foglal a résből; felette 21 mm marad. A gyári profil még kiválasztandó.',8)
foot(5);c.showPage();c.save();print('R14 PDF ready:5 pages')
