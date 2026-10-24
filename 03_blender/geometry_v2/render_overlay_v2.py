"""v1 (Blender lock) vs v2 (PDF) összevető kép. Bemenet: ../../_local/pdf_segs_*.json (helyi, PDF-ből kinyert vonalak)."""
import json, sys
from PIL import Image, ImageDraw, ImageFont
G='/tmp/claude-0/-home-claude/9b8b9da8-4b7d-59ea-8424-77210777ae42/scratchpad/geo/'
v2=json.load(open('A902_geometria_v2_ELOZETES.json')); v1=json.load(open('../geometry_lock_A902.json'))
S18=json.load(open(G+'pdf_segs_blendercoords.json')); A=json.load(open(G+'p3_align.json')); P3=json.load(open(G+'p3_segs_pt.json'))
try: F=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',22); Fs=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17)
except: F=Fs=None
S=90; ox,oy=3.2,21.4; W,H=int(21.8*S),int(23.2*S)
im=Image.new('RGB',(W,H),'white'); dr=ImageDraw.Draw(im,'RGBA'); P=lambda x,y:((x+ox)*S,(oy-y)*S)
col={-0.15:(205,205,200,150),0.47:(120,95,80,120),0.77:(110,170,90,120)}
for k,t in v2['terrace'].items():
    if 'poly' in t:
        dr.polygon([P(x,y) for x,y in t['poly']],fill=(205,205,200,150),outline=(60,60,60,200)); dr.text(P(t['poly'][1][0]+0.08,1.2),'Erkély 13',fill=(20,20,20),font=Fs)
    if 'box' in t:
        x0,y0,x1,y1=t['box']; z=t.get('z',t.get('z_to'))
        c=(240,120,0,90) if 'Jakuzzi' in k else col.get(z,(150,150,250,90))
        dr.rectangle([P(x0,y1),P(x1,y0)],fill=c,outline=(60,60,60,200))
        dr.text(P(x0+0.08,(y0-0.05) if k.startswith('Lepcso') else (y1-0.12)),k.replace('_',' ')+(f"  z={z:+.2f}" if z is not None else ''),fill=(20,20,20),font=Fs)
for i in range(-3,19): dr.line([P(i,-1.6),P(i,21.2)],fill=(225,232,248,255)); dr.text(P(i+0.04,21.3),str(i),fill=(90,110,170),font=Fs)
for j in range(-1,22): dr.line([P(-3.1,j),P(18.4,j)],fill=(225,232,248,255)); dr.text(P(-3.15,j+0.25),str(j),fill=(90,110,170),font=Fs)
M3=A['M3']
for x1,y1,x2,y2,w,c in P3:
    a=(x1/M3+A['dx'],-y1/M3+A['dy']); b=(x2/M3+A['dx'],-y2/M3+A['dy'])
    if -3.2<a[0]<18.4 and -1.6<a[1]<21.2 and (a[1]>8.3 or a[0]<0.05): dr.line([P(*a),P(*b)],fill=(90,90,90),width=1)
for a,b,w in S18:
    if w==0.71: dr.line([P(*a),P(*b)],fill=(0,0,0),width=2)
for k,(x0,y0,x1,y1) in v1['rooms'].items(): dr.rectangle([P(x0,y1),P(x1,y0)],outline=(30,110,255),width=3)
for k,(x0,y0,x1,y1) in v2['rooms'].items():
    dr.rectangle([P(x0,y1),P(x1,y0)],outline=(0,170,60),width=3); dr.text(P(x0+0.08,y0+0.35),k,fill=(0,120,40),font=Fs)
for k,(x0,y0,z0,x1,y1,z1) in v1['floors'].items():
    if y1>8.3 or y0>8.3 or x0<-0.2:
        x0,x1=sorted((x0,x1)); y0,y1=sorted((y0,y1)); dr.rectangle([P(x0,y1),P(x1,y0)],outline=(30,110,255),width=2)
dr.rectangle([P(-3.1,-0.9),P(11.0,-1.55)],fill='white')
dr.text(P(-3.05,-0.95),"A-902 geometria  KÉK = Blender lock v1   ZÖLD = v2 (PDF)   FEKETE = méretezett alaprajz   SZÜRKE = megvalósulási terv",fill=(0,0,0),font=Fs)
dr.text(P(-3.05,-1.2),"terasz z: greslap −0.15 · WPC +0.47 · zöldtető +0.77 (becslés)  — ELŐZETES, nem helyszíni mérés",fill=(0,0,0),font=Fs)
im.save('A902_v1_vs_v2_overlay.png'); print(im.size)
