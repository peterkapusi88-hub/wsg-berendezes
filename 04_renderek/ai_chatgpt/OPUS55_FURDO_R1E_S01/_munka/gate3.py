import sys
from PIL import Image, ImageFilter, ImageDraw
src,out,basef=sys.argv[1:4]
base=Image.open(basef).convert('RGB'); W=800; H=round(W*base.size[1]/base.size[0])
base=base.resize((W,H)); r=Image.open(src).convert('RGB').resize((W,H))
def edges(im): return im.convert('L').filter(ImageFilter.FIND_EDGES).point(lambda v:255 if v>18 else 0)
ed=Image.merge('RGB',(edges(base),edges(r),Image.new('L',(W,H))))
o=Image.new('RGB',(2*W,2*H)); o.paste(base,(0,0)); o.paste(r,(W,0)); o.paste(Image.blend(base,r,0.5),(0,H)); o.paste(ed,(W,H))
d=ImageDraw.Draw(o)
for x0 in (0,W):
  for i in range(1,10): d.line([(x0+i*W//10,0),(x0+i*W//10,8)],fill=(255,255,0),width=2)
o.save(out,quality=80)
