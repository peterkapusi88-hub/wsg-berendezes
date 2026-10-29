from pathlib import Path
import sys,json,math,hashlib
sys.path.insert(0,'/private/tmp/s16-python')
from shapely.geometry import Polygon,box
from shapely.affinity import rotate
O=Path(__file__).resolve().parents[1]
read=lambda n:json.loads((O/'data'/n).read_text())
parts=read('parts.json');drawers=read('drawers.json');layout=read('layout.json');lookup={p['id']:p for p in parts}
def xz(p):
 x,y,z,dx,dy,dz=p['box']
 return Polygon([(x+a,z+b) for a,b in p['outline']]).buffer(0) if p['axis']=='y' and p['outline'] else box(x,z,x+dx,z+dz)
shapes={p['id']:xz(p) for p in parts};collisions=[]
for d in drawers:
 moving=set(d['moving']);assert len(moving)==6
 for id in moving:
  p=lookup[id];b=p['box'];shape=shapes[id]
  for q in parts:
   if q['id'] in moving:continue
   qb=q['box'];area=shape.intersection(shapes[q['id']]).area
   if area<.01:continue
   for stroke in range(0,301,25):
    overlap=min(b[1]+b[4]+stroke,qb[1]+qb[4])-max(b[1]+stroke,qb[1])
    if overlap>.01:collisions.append({'drawer':d['id'],'moving':id,'fixed':q['id'],'stroke':stroke,'intersection_mm3':round(area*overlap,3)});break
# Check nominal door sweep against fixed rectangular body envelopes at intersecting heights.
door_hits=[]
excluded={p['id'] for p in parts if p['id'].startswith('T-DOOR') or p['id']=='TEXTILE'}
for did,hx,sgn in [('T-DOOR-L',21,1),('T-DOOR-R',849,-1)]:
 d=lookup[did];x,y,z,dx,dy,dz=d['box'];foot=box(x,y,x+dx,y+dy)
 for angle in range(0,91,5):
  swept=rotate(foot,sgn*angle,origin=(hx,400),use_radians=False)
  for p in parts:
   if p['id'] in excluded:continue
   xx,yy,zz,wx,wy,wz=p['box']
   # Curved caps are conservative envelopes, separately verified in model; do not mislabel them as solid boxes.
   if p['outline']:continue
   if min(z+dz,zz+wz)-max(z,zz)>.01 and swept.intersection(box(xx,yy,xx+wx,yy+wy)).area>.01:door_hits.append([did,angle,p['id']])
baseline=json.loads((O/'audit/baseline.json').read_text());protected={p:hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in baseline['protected_files'].items()}
assert all(protected.values())
report={'drawer_test':'One drawer at a time,0..300mm in25mm steps, actual XZ contours extruded along Y; includes other closed drawers. Hardware and room furniture excluded.','drawer_collisions':collisions,'door_test':'Nominal hinge pivot0..90° in5° steps against fixed rectangular elements. Curved caps/real hinge kinematics/cable loop require workshop test.','door_hits':door_hits,'independent_drawers':len(drawers),'moving_parts_per_drawer':[len(d['moving']) for d in drawers],'drawer_litres':sum(d['litres'] for d in drawers),'ceiling_gap':layout['ceiling_nominal']-layout['height'],'textile_margins':layout['textile_margins'],'S01_unchanged':all(protected.values())}
(O/'audit/motion_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
