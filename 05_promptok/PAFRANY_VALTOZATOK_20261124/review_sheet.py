from PIL import Image,ImageDraw
import pathlib,json,sys,math
p=pathlib.Path(__file__).resolve().parent;f=[p/'renders'/(i+'.png') for i in sys.argv[1:]];o=Image.new('RGB',(1600,math.ceil(len(f)/2)*530),'#eee');d=ImageDraw.Draw(o)
for k,x in enumerate(f):
 a=Image.open(x);a.thumbnail((790,495));xx=k%2*800;yy=k//2*530;o.paste(a,(xx,yy+28));d.text((xx+5,yy+3),x.stem,fill='black')
o.save('/private/tmp/pafrany_review.jpg')
