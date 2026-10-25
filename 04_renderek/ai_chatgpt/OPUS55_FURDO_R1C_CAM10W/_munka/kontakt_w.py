import csv,sys
from PIL import Image,ImageDraw,ImageFont
X=sys.argv[1]; D=f'/home/claude/wsg-berendezes/04_renderek/ai_chatgpt/OPUS55_FURDO_R1{X}_CAM10W/'
rows=list(csv.reader(open(D+'GENERALASI_NAPLO.csv'),delimiter=';'))[1:]
W,H=520,390; GAP=28; TOP=46; n=len(rows); R=(n+1)//2
img=Image.new('RGB',(2*W+30,TOP+R*(H+GAP)),(245,243,238)); d=ImageDraw.Draw(img)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',14); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',16)
d.text((10,12),f'A902 fürdő 06.2 · r1{X.lower()} · Cam_10W (WC-fülke + ajtó{" + zuhanyvégfal" if X=="D" else ""}) · {n} kép  ·  KONCEPCIÓ – NEM VALIDÁLT',font=fb,fill=(30,30,30))
for i,x in enumerate(rows):
    c,r=i%2,i//2; Xp=10+c*(W+10); Y=TOP+r*(H+GAP)
    img.paste(Image.open(D+x[12]).convert('RGB').resize((W,H)),(Xp,Y))
    st=x[1].split('_')[1]+' '+x[1].split('_')[2]
    g=x[15].replace('GEOMETRY ','')
    d.text((Xp+4,Y+H+4),f"{x[0]} {st} · {g[:46]}",font=f,fill=(170,30,30) if 'HIBÁS' in g else ((150,90,0) if 'FELTÉTELES' in g else (30,30,30)))
img.save(D+f'A902_FURDO_R1{X}_CAM10W_kontaktlap.jpg',quality=84); print(img.size)
