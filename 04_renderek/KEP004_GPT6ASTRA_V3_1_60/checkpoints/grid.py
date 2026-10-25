import sys
from PIL import Image, ImageDraw
src,out=sys.argv[1:3]
im=Image.open(src).convert('RGB').resize((1200,750)); d=ImageDraw.Draw(im)
for p in range(0,101,5):
    x=p*12; y=p*7.5; c=(255,0,0) if p%10==0 else (255,160,160)
    d.line([(x,0),(x,750)],fill=c,width=1); d.line([(0,y),(1200,y)],fill=c,width=1)
    if p%10==0: d.text((x+2,2),str(p),fill=(255,255,0)); d.text((2,y+2),str(p),fill=(255,255,0))
im.save(out,quality=85)
