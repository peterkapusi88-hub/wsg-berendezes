import sys,json
from PIL import Image, ImageFilter, ImageChops, ImageDraw
plan={p['kep_id']:p for p in json.load(open('/home/claude/build/plan.json'))}
src=sys.argv[1]; kid=src.split('/')[-1].split('__')[0]; p=plan[kid]
base=Image.open('/home/claude/opus_ref/'+p['image1']).convert('RGB').resize((800,500))
r=Image.open(src).convert('RGB').resize((800,500))
def edges(im): return im.convert('L').filter(ImageFilter.FIND_EDGES).point(lambda v:255 if v>18 else 0)
eb,er=edges(base),edges(r)
ed=Image.merge('RGB',(eb,er,Image.new('L',(800,500))))
bl=Image.blend(base,r,0.5)
out=Image.new('RGB',(1600,1000)); out.paste(base,(0,0)); out.paste(r,(800,0)); out.paste(bl,(0,500)); out.paste(ed,(800,500))
d=ImageDraw.Draw(out)
for x0 in (0,800):
  for i in range(1,10): d.line([(x0+i*80,0),(x0+i*80,8)],fill=(255,255,0),width=2)
out.save(sys.argv[2],quality=80)
