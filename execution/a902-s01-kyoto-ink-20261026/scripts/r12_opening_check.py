from pathlib import Path
import json,math
P=Path(__file__).resolve().parents[1];O=P/'R12_muhely';obs=json.loads((O/'audit/room_obstacle_bounds.json').read_text());result=[]
def hit(poly,box):
 corners=[(box[0],box[1]),(box[2],box[1]),(box[2],box[3]),(box[0],box[3])]
 for ax in [(1,0),(0,1)]+[(poly[(i+1)%4][1]-poly[i][1],poly[i][0]-poly[(i+1)%4][0]) for i in range(4)]:
  A=[x*ax[0]+y*ax[1] for x,y in poly];B=[x*ax[0]+y*ax[1] for x,y in corners]
  if max(A)<min(B) or max(B)<min(A):return False
 return True
for i,(lo,width) in enumerate([(4.3515,.717),(5.1915,.687),(5.8815,.687),(6.5715,.687),(7.2615,.687)]):
 for hand in ['left','right']:
  pivot=(4.101,lo if hand=='left' else lo+width);sg=1 if hand=='left' else -1;first=[]
  for ob in obs:
   if ob['max'][2]<.1515 or ob['min'][2]>.5485:continue
   for deg in range(0,111):
    t=math.radians(deg);v=(math.sin(t),sg*math.cos(t));n=(v[1],-v[0]);poly=[(pivot[0]+a*width*v[0]+b*.009*n[0],pivot[1]+a*width*v[1]+b*.009*n[1]) for a,b in [(0,-1),(1,-1),(1,1),(0,1)]]
    if hit(poly,[ob['min'][0],ob['min'][1],ob['max'][0],ob['max'][1]]):first.append({'object':ob['name'],'first_deg':deg});break
  result.append({'module':i+1,'hinge_side':hand,'potential_contacts':first})
(O/'audit/door_sweep_screening.json').write_text(json.dumps({'method':'1 degree sampled rigid rectangle vs Blender extracted AABBs,0..110deg; fixed approximate hinge axis; not actual Blum hinge motion','source':'R10 scene read only; only sofa, coffee and side-table candidates','results':result,'status':'SCREENING_NOT_FUNCTIONAL_APPROVAL'},ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False))
