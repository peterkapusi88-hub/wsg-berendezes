import pymupdf, json, sys
from PIL import Image, ImageDraw, ImageFont
PDF='/mnt/user-data/attachments/9b8b9da8-4b7d-59ea-8424-77210777ae42/ab86005a-WGR1_meretezett_alaprajzok.pdf'
L=json.load(open('/home/claude/wsg-berendezes/03_blender/geometry_lock_A902.json'))
d=pymupdf.open(PDF); pg=d[17]; M=72/25.4*1000/50
X0=157.3; Y0=626.4
def tb(x,y): return ((x-X0)/M,(Y0-y)/M)
segs=[]
for dr in pg.get_drawings():
    if dr['type']!='s' or dr.get('color')!=(0.0,0.0,0.0): continue
    w=round(dr.get('width') or 0,2)
    if w not in (0.71,0.99): continue
    for it in dr['items']:
        if it[0]=='l': segs.append((tb(it[1].x,it[1].y),tb(it[2].x,it[2].y),w))
        elif it[0]=='re':
            r=it[1];c=[(r.x0,r.y0),(r.x1,r.y0),(r.x1,r.y1),(r.x0,r.y1)]
            for i in range(4): segs.append((tb(*c[i]),tb(*c[(i+1)%4]),w))
        elif it[0]=='c': segs.append((tb(it[1].x,it[1].y),tb(it[4].x,it[4].y),w))
json.dump([[list(a),list(b),w] for a,b,w in segs],open('pdf_segs_blendercoords.json','w'))
S=110; ox,oy=3.5,10.8  # px per m, offsets
W,H=int(21*S),int(12.5*S)
im=Image.new('RGB',(W,H),'white'); dr=ImageDraw.Draw(im)
P=lambda x,y:((x+ox)*S,(oy-y)*S)
for i in range(-3,18):
    dr.line([P(i,-1.5),P(i,10.8)],fill=(225,235,250)); dr.text(P(i+0.02,10.7),str(i),fill=(90,120,200))
for j in range(-1,11):
    dr.line([P(-3.5,j),P(17.5,j)],fill=(225,235,250)); dr.text(P(-3.45,j+0.1),str(j),fill=(90,120,200))
for k,(x0,y0,z0,x1,y1,z1) in L['walls'].items():
    x0,x1=sorted((x0,x1));y0,y1=sorted((y0,y1))
    dr.rectangle([P(x0,y1),P(x1,y0)],fill=(150,190,255))
for k,(x0,y0,z0,x1,y1,z1) in L['openings'].items():
    x0,x1=sorted((x0,x1));y0,y1=sorted((y0,y1))
    dr.rectangle([P(x0,y1),P(x1,y0)],outline=(0,150,0))
for k,(x0,y0,x1,y1) in L['rooms'].items():
    dr.rectangle([P(x0,y1),P(x1,y0)],outline=(0,90,255)); dr.text(P(x0+0.05,y1-0.1),k,fill=(0,60,200))
for a,b,w in segs:
    dr.line([P(*a),P(*b)],fill=(0,0,0) if w==0.71 else (200,0,0),width=1)
im.save('overlay_pdf_vs_lock.png'); print(len(segs))
