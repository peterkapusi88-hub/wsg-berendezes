"""R14 hidden joinery; all dimensions remain design dimensions, not field measurements."""
from pathlib import Path
import json,copy,math,csv,itertools
import ezdxf
from ezdxf.render import forms
from ezdxf.acis import api as acis
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
for d in ['data','audit','rajzok','integration','sources','cimkek']:(O/d).mkdir(parents=True,exist_ok=True)
parts=json.loads((P/'R13_muhely/data/parts.json').read_text())
holes=json.loads((P/'R13_muhely/data/holes.json').read_text())
hinges=json.loads((P/'R13_muhely/data/hinges.json').read_text())
pins=json.loads((P/'R13_muhely/data/shelf_pins.json').read_text())
by={p['id']:p for p in parts};connections=[];changes=[]
def typed(t):return [p for p in parts if p['type']==t]
def hole(part,xyz,axis,diameter,depth,kind,source):
 h=dict(id=f'H{len(holes)+1:04}',part=part['id'],xyz=xyz,axis=axis,diameter=diameter,depth=depth,kind=kind,source=source,status='DESIGN_NOT_NC');holes.append(h);return h['id']
def add(pid,typ,name,box,x,y,t,material):
 p=copy.deepcopy(parts[0]);p.update(id=pid,type=typ,name=name,assembly_box_mm=box,x=x,y=y,t=t,material=material,edge=[0,0,0,0],note='R14 rejtett szerkezeti terv; műhelypróba és anyagjóváhagyás szükséges.',mpr=pid+'.mpr');parts.append(p);by[pid]=p;return p
def join(a,b,pa,pb,axis,da,db,deptha,depthb,kind,hardware):
 cid=f'R14-J{len(connections)+1:03}'
 ha=hole(a,pa,axis,da,deptha,kind+' / '+cid,'R14 tervezői kiosztás; tényleges laphoz és csavarhoz próbafúrás')
 hb=hole(b,pb,axis,db,depthb,kind+' / '+cid,'R14 tervezői kiosztás; tényleges laphoz és csavarhoz próbafúrás')
 connections.append(dict(id=cid,parts=[a['id'],b['id']],holes=[ha,hb],hardware=hardware,quantity=1,status='WORKSHOP_TRIAL_REQUIRED'))
# 1 mm clearance around backs, preserving visible design and existing bore locations.
backs=typed('TV01-H')+typed('TV02-H1')+typed('TV02-H2')
for p in backs:
 old=copy.deepcopy(p['assembly_box_mm']);p['assembly_box_mm'][0]+=1;p['assembly_box_mm'][2]+=1;p['assembly_box_mm'][3]-=2;p['assembly_box_mm'][5]-=2;p['x']-=2;p['y']-=2
 p['note']='R14 hátlap: körben 1 mm tervezett illesztési hézag; hátulról csavarozott, nem függesztő elem.'
 changes.append(dict(part=p['id'],before=old,after=p['assembly_box_mm'],reason='Hátlap szerelhetősége: 1 mm kerületi hézag'))
starts=[0,840,1530,2220,2910];widths=[720,690,690,690,690]
# 12 retaining battens. Screws enter from cabinet interior; backs assembled from rear before installation.
groups=[(0,720,588,2254,typed('TV01-S'),typed('TV01-H')[0],[660,1040,1420,1800,2180,2560,2780])]
for i,(off,w) in enumerate(zip(starts,widths)):groups.append((off,w,188,324,typed('TV02-S')[2*i:2*i+2],backs[i+1],[210,350,490]))
for gi,(off,w,z,h,sides,back,zs) in enumerate(groups):
 for hand in range(2):
  x=off+18 if hand==0 else off+w-36
  cleat=add(f'KI14-BAT-{gi*2+hand+1:02}','BAT','Hátlaprögzítő bükk léc',[x,356,z,18,18,h],h,18,18,'BEECH18')
  for zz in zs:
   axis=[-1,0,0] if hand==0 else [1,0,0];cx=x+18 if hand==0 else x;sx=off+18 if hand==0 else off+w-18
   join(cleat,sides[hand],[cx,365,zz],[sx,365,zz],axis,4,2.5,18,12,'LEC_OLDAL','4x30 domború fejű facsavar / tervezési specifikáció')
   join(back,cleat,[x+9,382,zz+15],[x+9,374,zz+15],[0,-1,0],3.5,2.5,8,12,'HATLAP_LEC','3.5x20 domború fejű facsavar / tervezési specifikáció')
# Lower visible infill retained by two hidden blocks, no face screws.
infill=by['KI13-GAP-LOW-01'];infill['note']='R14: két hátsó bükk rögzítőléc; elöl nincs látható csavar. Szerelés hátulról, falhoz állítás előtt.'
for hand,x in enumerate([720,822]):
 block=add(f'KI14-GAPBAT-{hand+1:02}','BAT','Alsó betét rejtett rögzítőléce',[x,368,190,18,18,320],320,18,18,'BEECH18')
 side=typed('TV02-S')[1 if hand==0 else 2];axis=[-1,0,0] if hand==0 else [1,0,0];cx=x+18 if hand==0 else x;sx=720 if hand==0 else 840
 for zz in [210,490]:join(block,side,[cx,377,zz],[sx,377,zz],axis,4,2.5,18,12,'BETET_OLDAL','4x30 domború fejű facsavar / tervezési specifikáció')
 for zz in [270,430]:join(block,infill,[x+9,386,zz],[x+9,368,zz],[0,-1,0],4,2.5,18,12,'BETET_HATUL','4x30 domború fejű facsavar / tervezési specifikáció')
# Seven rear crossrails, dowelled to sides. These are NOT certified wall hangers.
railgroups=[]
for i,(off,w) in enumerate(zip(starts,widths)):railgroups.append((off+18,w-36,432,typed('TV02-S')[2*i],typed('TV02-S')[2*i+1],[452,482,512]))
railgroups += [(18,333,2762,typed('TV01-S')[0],typed('TV01-C')[0],[2782,2812,2842]),(369,333,2762,typed('TV01-C')[0],typed('TV01-S')[1],[2792,2822,2852])]
for i,(x,w,z,left,right,zs) in enumerate(railgroups):
 rail=add(f'KI14-RAIL-{i+1:02}','RAIL','Hátsó merevítő keresztléc',[x,338,z,w,18,100],w,100,18,'PLY18')
 for hand,side in enumerate([left,right]):
  xx=x if hand==0 else x+w;sign=1 if hand==0 else -1
  for zz in zs:
   cid=f'R14-J{len(connections)+1:03}'
   ha=hole(rail,[xx,347,zz],[sign,0,0],8,22,'MEREVITO_CSAP / '+cid,'R14 Ø8x30 bükk csap, 22+12 mélység; ragasztott próbakötés')
   hb=hole(side,[xx,347,zz],[-sign,0,0],8,12,'MEREVITO_CSAP / '+cid,'R14 Ø8x30 bükk csap, 22+12 mélység; középosztón 10 mm eltolt tengely')
   connections.append(dict(id=cid,parts=[rail['id'],side['id']],holes=[ha,hb],hardware='8x30 bükk köldökcsap + anyaghoz választott ragasztó',quantity=1,status='WORKSHOP_TRIAL_REQUIRED'))
# Verified Blum adapter patterns; the two centre-divider patterns are staggered vertically.
tipons=[]
for hand,zz in enumerate([1200,1250]):
 side=typed('TV01-C')[0];xx=351 if hand==0 else 369;axis=[1,0,0] if hand==0 else [-1,0,0]
 ids=[hole(side,[xx,yy,zz],axis,2.5,10,'TIPON_ADAPTER','Blum LIT.HNG4700.06.17 p2: setback20/spacing32; Ø2.5x10 designer pilot, trial required') for yy in [20,52]]
 tipons.append(dict(front=typed('TV01-F')[hand]['id'],support=side['id'],unit='956A1004',adapter='956A1201',holes=ids,position=[xx,20,zz],catch='Gyári öntapadó ellenlemez; helyét a felszerelt nyitóval átjelölni, tapadáspróba szükséges'))
for i in [0,1,4]:
 side=typed('TV02-S')[2*i+1];xx=starts[i]+widths[i]-18
 ids=[hole(side,[xx,yy,450],[1,0,0],2.5,10,'TIPON_ADAPTER','Blum LIT.HNG4700.06.17 p2: setback20/spacing17; Ø2.5x10 designer pilot, trial required') for yy in [20,37]]
 tipons.append(dict(front=(typed('TV02-F1')+typed('TV02-F2'))[i]['id'],support=side['id'],unit='956.1004',adapter='956.1201',holes=ids,position=[xx,20,450],catch='Gyári öntapadó ellenlemez; helyét a felszerelt nyitóval átjelölni, tapadáspróba szükséges'))
(O/'data/tipon.json').write_text(json.dumps(tipons,ensure_ascii=False,indent=2))
(O/'data/connections.json').write_text(json.dumps(connections,ensure_ascii=False,indent=2))
(O/'data/changes.json').write_text(json.dumps(changes,ensure_ascii=False,indent=2))
# Reuse the proven R13 canonical-frame and native-Boolean pipeline, with current data.
tail=(P/'scripts/r13_cad.py').read_text().split('# Assign a canonical right-handed frame')[1]
tail='# Assign a canonical right-handed frame'+tail
tail=tail.replace("['TV01-F','GAP','GAP-LOW','TV03-P']","['TV01-F','GAP','GAP-LOW','TV03-P']")
tail=tail.replace('R13','R14').replace('ki13','ki14')
exec(compile(tail,str(__file__)+':pipeline','exec'))
# Frame descriptions override the old generic labels. No implied machine stop.
for p in parts:
 p['face']='A = U×V szerinti külső normál; a rajzon és frame adatokban meghatározva, nem gépi felfekvő oldal.'
 p['edge_definition']='E1: V=0; E2: U=Umax; E3: V=Vmax; E4: U=0. Forgatásnál az ID és tengelynyilak az irányadók.'
(O/'data/parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2))
# Check every pair of bores conservatively with cylinder bounding boxes (all axes).
possible=[]
for a,b in itertools.combinations(holes,2):
 if a['part']!=b['part']:continue
 def box(h):
  k=next(i for i,v in enumerate(h['axis']) if v);lo=[];hi=[]
  for i in range(3):
   ends=[h['xyz'][i],h['xyz'][i]+h['axis'][i]*h['depth']]
   lo.append(min(ends) if i==k else h['xyz'][i]-h['diameter']/2);hi.append(max(ends) if i==k else h['xyz'][i]+h['diameter']/2)
  return lo,hi
 aa,ab=box(a);ba,bb=box(b)
 if all(min(ab[i],bb[i])-max(aa[i],ba[i])>.001 for i in range(3)):possible.append([a['id'],b['id']])
assert not possible,possible
(O/'audit/all_axis_bore_check.json').write_text(json.dumps({'cylinders':len(holes),'overlapping_cylinder_bounding_boxes':possible,'scope':'Nominal isolated lap parts; no machine/tool/fixture simulation.'},indent=2))
print('R14 connections',len(connections),'parts',len(parts),'holes',len(holes))
