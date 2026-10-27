"""Editable vector re-draws from the owner's T01–T07, not recovered originals."""
from pathlib import Path
import random,math,json,subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
P=Path(__file__).resolve().parents[1];O=P/'R06';rng=random.Random(90206)
def stroke(points,widths,rough=0):
 left=[];right=[]
 for i,(x,y) in enumerate(points):
  a=points[max(0,i-1)];b=points[min(len(points)-1,i+1)];dx=b[0]-a[0];dy=b[1]-a[1];ll=math.hypot(dx,dy);nx=-dy/ll;ny=dx/ll
  w=widths[i]/2;left.append([x+nx*(w+rng.uniform(-rough,rough)),y+ny*(w+rng.uniform(-rough,rough))]);right.append([x-nx*(w+rng.uniform(-rough,rough)),y-ny*(w+rng.uniform(-rough,rough))])
 return left+right[::-1]
def line(a,b,w1,w2,n=45,rough=0):
 ps=[[a[0]+(b[0]-a[0])*i/n,a[1]+(b[1]-a[1])*i/n] for i in range(n+1)]
 return stroke(ps,[w1+(w2-w1)*i/n for i in range(n+1)],rough)
specs=[('INK-W01',3300,2330,'T01',[line((-80,1970),(1830,1010),165,22,80,10),line((1160,0),(1020,2330),230,105,95,12)]),
 ('INK-W02',2100,2880,'T02',[line((1450,-20),(1465,1250),430,360,75,20),line((1468,1380),(1450,2900),345,440,80,18)]),
 ('INK-WN',2920,2837,'T04',[stroke([[0,820],[550,930],[1030,1110],[1500,1300],[2050,1480],[2550,1590],[2920,1670]],[5,12,24,18,31,60,18],3),line((2460,100),(2425,2837),18,5,60,2),line((2430,370),(2410,1810),56,22,60,5)]),
 ('INK-WS',2380,2837,'T05',[line((1100,-50),(1600,2900),240,60,80,18),line((300,400),(2110,2270),160,12,90,11)]),
 ('INK-B62',900,2400,'T07',[])]
branches=[[(810,2430),(610,1960),(400,1450),(180,800),(80,0)],[(610,1960),(820,1570),(890,1040)],[(400,1450),(80,1120),(-20,900)],[(180,800),(470,530),(620,50)],[(650,2070),(220,1830),(30,1530)]]
for j,pts in enumerate(branches):
 specs[-1][4].append(stroke(pts,[max(2,22-j*3-i*4) for i in range(len(pts))],1.5))
 for a,b in zip(pts,pts[1:]):
  for t in [.22,.48,.75]:
   x=a[0]+(b[0]-a[0])*t;y=a[1]+(b[1]-a[1])*t
   for side in [-1,1]:
    q=(x+side*rng.uniform(30,65),y-rng.uniform(25,75));specs[-1][4].append(line((x,y),q,2,1,4));specs[-1][4].append([[q[0]+math.cos(k*math.pi/8)*6,q[1]+math.sin(k*math.pi/8)*15] for k in range(16)])
manifest=[]
for ident,w,h,target,polys in specs:
 # All paths are editable. Small negative spaces are deliberately supplied as a separate layer.
 holes=[]
 if ident not in ['INK-WN','INK-B62']:
  for poly in polys:
   xs=[a[0] for a in poly];ys=[a[1] for a in poly]
   # Dry-brush holes only where the polygon actually covers the sample point.
   def inside(x,y):
    c=False
    for a,b in zip(poly,poly[1:]+poly[:1]):
     if (a[1]>y)!=(b[1]>y) and x<(b[0]-a[0])*(y-a[1])/(b[1]-a[1])+a[0]:c=not c
    return c
   for _ in range(1200):
    x=rng.uniform(min(xs),max(xs));y=rng.uniform(min(ys),max(ys))
    if inside(x,y):
     dx=rng.uniform(1,4);dy=rng.uniform(2,16);holes.append([[x-dx,y-dy],[x+dx,y-dy],[x+dx,y+dy],[x-dx,y+dy]])
 def points(p):return ' '.join(f'{x:.2f},{y:.2f}' for x,y in p)
 svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}mm" height="{h}mm" viewBox="0 0 {w} {h}"><title>{ident} R06 - reference-based redraw, approval proof, no ICC profile assigned</title><g id="INK" fill="#26231f">'+''.join(f'<polygon points="{points(p)}"/>' for p in polys)+'</g><g id="PAPER_BREAKS" fill="white">'+''.join(f'<polygon points="{points(p)}"/>' for p in holes)+'</g></svg>'
 (O/'artwork'/f'{ident}_R06.svg').write_text(svg)
 f=O/'artwork'/f'{ident}_R06.pdf';c=canvas.Canvas(str(f),pagesize=(w*mm,h*mm));c.setTitle(ident+' - approval artwork, not press approved')
 def draw(p,color):
  c.setFillColorRGB(*color);path=c.beginPath();path.moveTo(p[0][0]*mm,(h-p[0][1])*mm)
  for x,y in p[1:]:path.lineTo(x*mm,(h-y)*mm)
  path.close();c.drawPath(path,stroke=0,fill=1)
 for p in polys:draw(p,(.149,.137,.122))
 for p in holes:draw(p,(1,1,1))
 c.save();subprocess.run(['pdftoppm','-png','-singlefile','-scale-to','2048',str(f),str(O/'artwork'/f'{ident}_mask')],check=True,stdout=subprocess.DEVNULL,stderr=subprocess.PIPE)
 manifest.append(dict(id=ident,w_mm=w,h_mm=h,target=target,svg=str((O/'artwork'/f'{ident}_R06.svg').relative_to(P)),pdf=str(f.relative_to(P)),polygons=polys,negative_polygons=holes,status='REFERENCE-BASED VECTOR REDRAW; NOT original source master; unseen regions reconstructed; proof approval pending',printing='Single-colour ink mask; white negative spaces must be converted to knockout before output. No embedded final ICC; printer assigns for actual substrate. Panel gaps are imposed from the dimensioned drawing, never stretched independently.'))
(O/'data/artwork_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print('5 full-size SVG/PDF artwork proofs and render masks created')
