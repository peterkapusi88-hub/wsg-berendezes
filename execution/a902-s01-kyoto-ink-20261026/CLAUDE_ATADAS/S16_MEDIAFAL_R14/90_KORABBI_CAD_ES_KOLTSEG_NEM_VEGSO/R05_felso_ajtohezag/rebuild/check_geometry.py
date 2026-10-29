from pathlib import Path
import sys,json,itertools,math
sys.path.insert(0,'/private/tmp/s16-python')
import numpy as np
from shapely.geometry import Polygon,box,LineString
from shapely.affinity import rotate
from shapely.ops import unary_union
from shapely import distance,points
import ezdxf
from ezdxf.math import bulge_to_arc
O=Path(__file__).resolve().parents[1]
r=lambda n:json.loads((O/'data'/n).read_text())
ps=r('parts.json');lookup={p['id']:p for p in ps};layout=r('layout.json');lights=r('lighting.json')
def xz(p):
 x,y,z,w,d,h=p['box'];return Polygon([(x+a,z+b)for a,b in p['outline']]).buffer(0) if p['axis']=='y' and p['outline'] else box(x,z,x+w,z+h)
sh={p['id']:xz(p)for p in ps};hits=[]
for p,q in itertools.combinations(ps,2):
 b=p['box'];c=q['box'];ov=min(b[1]+b[4],c[1]+c[4])-max(b[1],c[1]);a=sh[p['id']].intersection(sh[q['id']]).area
 if ov>.001 and a>.01:hits.append([p['id'],q['id'],round(ov*a,3)])
assert not hits,hits
fronts=[p for p in ps if p['id'].startswith('T-DOOR') or p['id'].endswith('-FRONT')]
frames=[p for p in ps if p['id'].startswith('FRAME')]
gaps=[]
for p in fronts:
 other=unary_union([sh[q['id']] for q in fronts+frames if q['id']!=p['id']])
 boundary=sh[p['id']].boundary
 samples=[boundary.interpolate(d) for d in np.linspace(0,boundary.length,math.ceil(boundary.length/.5)+1)]
 ds=distance(points([(p.x,p.y) for p in samples]),other)
 rec={'part':p['id'],'boundary_samples':len(samples),'min_mm':float(min(ds)),'max_mm':float(max(ds))}
 gaps.append(rec)
 # At a T seam, distance to the nearest corner can exceed the orthogonal3mm reveal.
 assert rec['min_mm']>2.99 and rec['max_mm']<4.25,rec
# Every adjacent front joint is exactly3mm at the shared straight edge.
seams=[]
for a,b in [('T-DOOR-L','T-DOOR-R'),('T-DOOR-L','D1-FRONT')]+[(f'D{i}-FRONT',f'D{i+1}-FRONT')for i in range(1,6)]:
 gap=lookup[b]['box'][0]-(lookup[a]['box'][0]+lookup[a]['box'][3]);assert abs(gap-3)<1e-8;seams.append([a,b,gap])
bg=[lookup[f'BG-{i}']['box'] for i in range(1,5)];bgg=[bg[0][0]-870]+[bg[i][0]-sum([bg[i-1][0],bg[i-1][3]]) for i in range(1,4)]+[3600-bg[-1][0]-bg[-1][3]]
assert bgg==[3]*5,bgg
# Exact CAD circular arcs agree with the intended concentric inset geometry.
arc_proof={}
for id,expected in [('T-DOOR-L',[79,79]),('T-DOOR-R',[79]),('D6-FRONT',[59,59]),('FRAME-T-TOP',[100,100,82,82]),('FRAME-T-BOT',[100,82]),('FRAME-B-TOP',[80,62]),('FRAME-B-BOT',[80,62])]:
 doc=ezdxf.readfile(O/'alkatreszek'/f'{id}.dxf');v=list(doc.modelspace().query('LWPOLYLINE'))[0].get_points('xyb');radii=[]
 for i,(x,y,b) in enumerate(v):
  if abs(b)>1e-8:radii.append(round(bulge_to_arc((x,y),v[(i+1)%len(v)][:2],b)[3],6))
 assert sorted(radii)==sorted(expected),(id,radii,expected)
 arc_proof[id]=radii
# Slice true XZ contours to check nominal door rotation against ALL curved caps as well.
# 2mm height grid plus all contour vertex heights;1-degree angular grid. This is sampled, not a hinge manufacturer certification.
def intervals(shape,z):
 q=shape.intersection(LineString([(-10,z),(3610,z)]));geoms=list(q.geoms) if hasattr(q,'geoms') else [q]
 return [(a.bounds[0],a.bounds[2])for a in geoms if a.geom_type=='LineString' and a.length>.00001]
curved=[p for p in ps if p['id'].startswith(('CURVE-T','FRAME-T')) and p['outline']]
curved_hits=[];pose_count=0
for did,hx,sgn in [('T-DOOR-L',21,1),('T-DOOR-R',849,-1)]:
 door=lookup[did];b=door['box']
 for fixed in curved:
  c=fixed['box'];lo=max(b[2],c[2]);hi=min(b[2]+b[5],c[2]+c[5])
  if hi<=lo:continue
  heights=sorted(set([lo+.0001,hi-.0001]+list(np.arange(lo+1,hi,2))+[z for x,z in sh[did].exterior.coords if lo<z<hi]+[z for x,z in sh[fixed['id']].exterior.coords if lo<z<hi]))
  for z in heights:
   fi=intervals(sh[fixed['id']],z)
   if not fi:continue
   fs=unary_union([box(x,c[1],xx,c[1]+c[4])for x,xx in fi])
   for x,xx in intervals(sh[did],z):
    dfoot=box(x,b[1],xx,b[1]+b[4])
    for angle in range(91):
     pose_count+=1
     if rotate(dfoot,sgn*angle,origin=(hx,400)).intersection(fs).area>.001:curved_hits.append([did,fixed['id'],float(z),angle])
assert not curved_hits,curved_hits[:5]
t=lookup['TEXTILE']['box'];assert layout['height']-t[2]-t[5]==t[2]-150==105
loop=next(c for c in lights['circuits'] if c['id']=='A4-TEXTILE-LOOP')['path'];assert layout['height']-max(p[2]for p in loop)==min(p[2]for p in loop)-150==100
# Pocket remains aligned after the left door's lower edge moved.
d=lookup['T-DOOR-L'];g=d['light_groove'];outer=Polygon([(d['box'][0]+x,d['box'][2]+z)for x,z in g['outer']]);inner=Polygon([(d['box'][0]+x,d['box'][2]+z)for x,z in g['inner']]);pocket=outer.difference(inner)
assert pocket.buffer(.001).covers(LineString([(x,z)for x,y,z in loop]))
assert sh['T-DOOR-L'].covers(outer)
assert lookup['TV-LINK']['box'][0]==870 and all(lookup[id]['box'][2]==570 for id in ['TV-LINK','TV-MID','TV-END'])
assert layout['screen_box']==[1436.25,151,968.8,1677.5,61.1,962.4]
assert layout['ceiling_nominal']-layout['height']==25
report={'revision':layout['revision'],'part_count':len(ps),'static_pairs_tested':len(ps)*(len(ps)-1)//2,'static_intersections':hits,'full_front_boundary_gaps':gaps,'straight_front_seams_mm':seams,'background_edge_and_internal_seams_mm':bgg,'exact_DXF_arc_radii_mm':arc_proof,'curved_cap_door_sweep':{'sampled_cross_section_poses':pose_count,'hits':curved_hits,'limits':'Nominal pivot only;1degree/2mm plus contour vertices. Real hinges/cables and workshop tolerances not certified.'},'textile_top_bottom_margins_mm':[105,105],'textile_light_margins_mm':[100,100],'light_loop_inside_real_pocket':True,'TV_size_unchanged':True,'ceiling_LED_gap_mm':25,'further_scope':'Static part envelopes/contours and sampled nominal motions. No assertion of installed building dimensions, real hinges, fasteners, electrical/thermal verification or manufacturing approval.'}
(O/'audit/geometry_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
