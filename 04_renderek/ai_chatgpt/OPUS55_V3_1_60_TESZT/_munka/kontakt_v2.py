import csv
from PIL import Image,ImageDraw,ImageFont
D='/home/claude/wsg-berendezes/04_renderek/ai_chatgpt/OPUS55_V3_1_60_TESZT/'
m=list(csv.reader(open(D+'GENERALASI_NAPLO.csv'),delimiter=';')); ix={c:i for i,c in enumerate(m[0])}
L=list(csv.reader(open(D+'GENERALASI_NAPLO_v2.csv'),delimiter=';'))[1:]
v2={x[0]:x for x in L if x[3]=='v2'}; v2g={x[0]:x[14] for x in L}
cams=['Cam_12','Cam_02','Cam_03','Cam_04','Cam_11','Cam_10']
W,H=320,200; LW=150; TOP=40
img=Image.new('RGB',(LW+6*W,TOP+10*(H+22)),(245,243,238)); d=ImageDraw.Draw(img)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',13); fb=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',15)
d.text((10,10),'A902 OPUS55 V3.1 – ChatGPT Images, 60 sor, legfrissebb változat (v2 = javított; kék felirat = javítókörben készült)  ·  KONCEPCIÓ – NEM VALIDÁLT',font=fb,fill=(30,30,30))
for i,c in enumerate(cams): d.text((LW+i*W+8,TOP-8),c,font=fb,fill=(30,30,30))
rows=m[1:]; styles=sorted({x[ix['stilus']] for x in rows})
for si,s in enumerate(styles):
    y=TOP+si*(H+22)+10; d.text((8,y+H//2-8),s,font=fb,fill=(30,30,30))
    for x in rows:
        if x[ix['stilus']]!=s: continue
        ci=cams.index(x[ix['kamera']]); fn=v2[x[0]][11] if x[0] in v2 else x[ix['eredmeny_fajl']]
        img.paste(Image.open(D+fn).convert('RGB').resize((W-6,H-6)),(LW+ci*W+3,y))
        g=v2g.get(x[0]) or x[ix['geometria']]
        lab=f"{x[0]} {'v2' if x[0] in v2 else 'v1'} · {g.replace('GEOMETRY ','')[:34]}"
        col=(170,30,30) if g.startswith('GEOMETRY_FAIL') else ((20,60,160) if x[0] in v2g else (30,30,30))
        d.text((LW+ci*W+4,y+H-4),lab,font=f,fill=col)
img.save(D+'A902_OPUS55_V3_1_kontaktlap_v2.jpg',quality=82); print('ok')
