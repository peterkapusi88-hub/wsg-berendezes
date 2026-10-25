import csv
from PIL import Image,ImageDraw,ImageFont
D='/home/claude/wsg-berendezes/04_renderek/ai_chatgpt/OPUS55_FURDO_R1B/'
rows=list(csv.reader(open(D+'GENERALASI_NAPLO.csv'),delimiter=';'))[1:]
W,H=560,350; C=2; TOP=46; GAP=28
img=Image.new('RGB',(C*W+30,TOP+5*(H+GAP)),(245,243,238)); d=ImageDraw.Draw(img)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',15); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',17)
d.text((10,12),'A902 fürdő 06.2 · r1b · Cam_10 · ChatGPT Images, 10 kép  ·  KONCEPCIÓ – NEM VALIDÁLT',font=fb,fill=(30,30,30))
for i,x in enumerate(rows):
    c,r=i%2,i//2; X=10+c*(W+10); Y=TOP+r*(H+GAP)
    img.paste(Image.open(D+x[12]).convert('RGB').resize((W,H)),(X,Y))
    st=x[1].split('_')[1]+' '+x[1].split('_')[2]
    d.text((X+4,Y+H+4),f"{x[0]} {st} · {x[15].replace('GEOMETRY ','')}",font=f,fill=(30,30,30))
img.save(D+'A902_FURDO_R1B_kontaktlap.jpg',quality=84); print(img.size)
