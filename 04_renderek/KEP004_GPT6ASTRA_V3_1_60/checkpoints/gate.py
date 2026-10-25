"""gate.py <cam> <base.png> <render> <out.jpg> : base | render | blend | edges, with projected guide marks on render+base."""
import sys, json
from PIL import Image, ImageDraw, ImageFilter, ImageOps
sys.path.insert(0,'/home/claude/work/py')
G=json.load(open('/home/claude/work/py/guides.json'))
cam,bp,rp,op=sys.argv[1:5]
base=Image.open(bp).convert('RGB'); ren=Image.open(rp).convert('RGB')
W,H=800,500
b=base.resize((W,H)); r=ren.resize((W,H))
def marks(im):
    d=ImageDraw.Draw(im)
    for lab,x,y in G.get(cam,[]):
        X,Y=x/100*W,y/100*H
        d.line([(X,0),(X,H)],fill=(255,0,255),width=1)
        d.ellipse([X-5,Y-5,X+5,Y+5],outline=(255,0,255),width=2); d.text((X+4,Y+4),lab,fill=(255,0,255))
    return im
blend=Image.blend(b,r,0.5)
eb=ImageOps.autocontrast(b.convert('L').filter(ImageFilter.FIND_EDGES)).point(lambda v:255 if v>40 else 0)
er=ImageOps.autocontrast(r.convert('L').filter(ImageFilter.FIND_EDGES)).point(lambda v:255 if v>60 else 0)
ov=Image.merge('RGB',(eb,er,Image.new('L',(W,H),0)))
S=Image.new('RGB',(2*W,2*H+40),'white')
for im,(x,y) in [(marks(b.copy()),(0,0)),(marks(r.copy()),(W,0)),(blend,(0,H+20)),(ov,(W,H+20))]: S.paste(im,(x,y))
d=ImageDraw.Draw(S); d.text((5,H+4),f'BASE {cam} (magenta = projected lock points)',fill='black'); d.text((W+5,H+4),f'RENDER {ren.size} stretched to 16:10',fill='black')
d.text((5,2*H+24),'blend 50%',fill='black'); d.text((W+5,2*H+24),'edges: red=base green=render',fill='black')
S.save(op,quality=85); print(op, ren.size, round(ren.size[0]/ren.size[1],3))
