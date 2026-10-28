"""R13: real CAD machining design. Preserve R12, no machine execution."""
from pathlib import Path
import json,math,csv,hashlib,itertools,copy
import ezdxf
from ezdxf.render import forms
from ezdxf.acis import api as acis
P=Path(__file__).resolve().parents[1]; O=P/'R13_muhely'
parts=json.loads((P/'R12_muhely/data/parts.json').read_text())
base=json.loads((P/'R12_muhely/data/joints.json').read_text())
by={p['id']:p for p in parts}
def typed(t): return [p for p in parts if p['type']==t]
fronts=typed('TV01-F')+typed('TV02-F1')+typed('TV02-F2')
for p in fronts:
 p['assembly_box_mm'][1]=-21
 p['note']+=' R13: 3 mm tervezett nyomási hézag; teljes névleges mélység 403 mm.'
# Visible lower recess, absent from R12. A single infill, not a new storage module.
p=copy.deepcopy(parts[-1]);p.update(id='KI13-GAP-LOW-01',type='GAP-LOW',name='Alsó visszahúzott grafit betét',x=380,y=117,t=18,material='M01',assembly_box_mm=[721.5,350,151.5,117,18,380],edge=[1,1,1,1],note='Új R13 betét; oldalsó 1,5 mm hézag. Rögzítőkonzol külön egyeztetendő.',mpr='KI13-GAP-LOW-01.mpr');parts.append(p);by[p['id']]=p
holes=[]
def hole(part,xyz,axis,diameter,depth,kind,source):
 holes.append(dict(id=f'H{len(holes)+1:04}',part=part['id'],xyz=xyz,axis=axis,diameter=diameter,depth=depth,kind=kind,source=source,status='DESIGN_NOT_NC'))
for h in base['holes']:
 hole(by[h['part']],h['xyz'],h['axis'],h['diameter'],h['depth'],'CSAP '+h['joint'],'R12 J01-J26 / 8x30, 12+22')
# Cup and plate patterns: manufacturer data. Pilot diameter is a design assumption,
# not a claimed Blum instruction; explicitly retained in source/status fields.
hinges=[]
def hinges_for(front,side,hand,levels):
 x,y,z,w,d,h=front['assembly_box_mm']; sx,sy,sz,sw,sd,sh=side['assembly_box_mm']
 for dz in levels:
  cx=x+23 if hand=='L' else x+w-23; cz=z+dz
  hole(front,[cx,-3,cz],[0,-1,0],35,13,'PANT_CSÉSZE','Blum 70T3550.TL datasheet:35/13; TB5.5, MD0 -> FA16.5')
  screw_x=cx-9.5 if hand=='L' else cx+9.5
  for zz in [cz-22.5,cz+22.5]:hole(front,[screw_x,-3,zz],[0,-1,0],2.5,10,'PANT_CSAVAR_ELOFURAT','45/9.5 gyári kiosztás; Ø2.5x10 próbadarabon igazolandó 3.5x15 csavarhoz')
  px=sx+sw if hand=='L' else sx; ax=[-1,0,0] if hand=='L' else [1,0,0]
  for zz in [cz-16,cz+16]:hole(side,[px,37,zz],ax,2.5,10,'TALP_CSAVAR_ELOFURAT','Blum173H7100 37/32; Ø2.5x10 tervezői próbaérték')
  hinges.append(dict(front=front['id'],side=side['id'],xyz=[cx,-3,cz],hand=hand,sku='70T3550.TL',plate='173H7100'))
for i,p in enumerate(typed('TV01-F')): hinges_for(p,typed('TV01-S')[i],'L' if i==0 else 'R',[100,631.75,1163.5,1695.25,2227])
low=typed('TV02-F1')+typed('TV02-F2')
for i in [0,1,4]:hinges_for(low[i],typed('TV02-S')[2*i],'L',[80,317])
# No hinge drilling on lower doors 3/4 while coplanar variant is evaluated.
pins=[]
for p in typed('TV01-P')+typed('TV02-P1')+typed('TV02-P2'):
 x,y,z,w,d,h=p['assembly_box_mm']
 for side_x,ax in [(x-1,[-1,0,0]),(x+w+1,[1,0,0])]:
  candidates=[s for s in parts if s['type'] in ['TV01-S','TV01-C','TV02-S'] and abs((s['assembly_box_mm'][0]+(s['assembly_box_mm'][3] if ax[0]<0 else 0))-side_x)<.01 and s['assembly_box_mm'][2]<z<s['assembly_box_mm'][2]+s['assembly_box_mm'][5]]
  assert len(candidates)==1,(p['id'],side_x,candidates)
  side=candidates[0]
  for yy in [y+30,y+d-30]:
   hole(side,[side_x,yy,z-2.5],ax,5,8,'POLCTARTO','Ø5 csapos, lapos felfekvésű polctartó; 8mm beülés, tervezési specifikáció')
   pins.append(dict(part=side['id'],shelf=p['id'],xyz=[side_x,yy,z-2.5],axis=ax))
# Pass-through for AV cables in the second lower back: radius, not sharp corner.
av=typed('TV02-H2')[0]
hole(av,[1185,382,300],[0,-1,0],60,8,'AV_KABEL','Tervezési Ø60 átvezetés; cserélhető kefe, villamos kábelek elkülönítése')
# Assign a canonical right-handed frame for every blank. Front A always inner.
for p in parts:
 x,y,z,w,d,h=p['assembly_box_mm'];t=p['type']
 if t in ['TV01-F','GAP','GAP-LOW','TV03-P']:
  org=[x,y+d,z];u=[0,0,1];v=[1,0,0];n=[0,1,0]
 elif t.startswith('TV02-F'):
  org=[x+w,y+d,z];u=[-1,0,0];v=[0,0,1];n=[0,1,0]
 elif w==p['t']:
  org=[x,y,z];u=[0,0,1];v=[0,1,0];n=[-1,0,0]
 elif h==p['t']:
  org=[x,y,z+h];u=[1,0,0];v=[0,1,0];n=[0,0,1]
 elif p['x']==h:
  org=[x,y+d,z];u=[0,0,1];v=[1,0,0];n=[0,1,0]
 else:
  org=[x+w,y+d,z];u=[-1,0,0];v=[0,0,1];n=[0,1,0]
 p['frame']={'origin':org,'U':u,'V':v,'outward_A':n,'meaning':'rajzi jobbkezes rendszer; nem gépi ütköző'}
 p['revision']='R13';p['hole_count']=sum(hh['part']==p['id'] for hh in holes)
 p['raw_size_status']='Élzárási ráhagyás és műhelyélkód még nem kiadott'
for h in holes:
 f=by[h['part']]['frame'];q=[h['xyz'][k]-f['origin'][k] for k in range(3)]
 h['local_UVW']=[sum(a*b for a,b in zip(q,vec)) for vec in [f['U'],f['V'],f['outward_A']]]
 h['local_axis']=[sum(a*b for a,b in zip(h['axis'],vec)) for vec in [f['U'],f['V'],f['outward_A']]]
# Validate full cylinder containment (not just its axis), analytical overlaps.
invalid=[];intersections=[]
for h in holes:
 bb=by[h['part']]['assembly_box_mm'];axis=next(k for k,a in enumerate(h['axis']) if a)
 for k in range(3):
  if k==axis:
   end=h['xyz'][k]+h['axis'][k]*h['depth'];ok=bb[k]-.001<=end<=bb[k]+bb[k+3]+.001
  else:ok=bb[k]-.001<=h['xyz'][k]-h['diameter']/2 and h['xyz'][k]+h['diameter']/2<=bb[k]+bb[k+3]+.001
  if not ok:invalid.append([h['id'],k])
for a,b in itertools.combinations(parts,2):
 A=a['assembly_box_mm'];B=b['assembly_box_mm'];v=[min(A[k]+A[k+3],B[k]+B[k+3])-max(A[k],B[k]) for k in range(3)]
 if min(v)>.01:intersections.append([a['id'],b['id'],v])
assert not invalid,invalid
assert not intersections,intersections
expected=sum(math.prod(p['assembly_box_mm'][3:]) for p in parts)-sum(math.pi*(h['diameter']/2)**2*h['depth'] for h in holes)
# All cuts are nonintersecting by construction; verify parallel drilling pairs.
hole_collisions=[]
for a,b in itertools.combinations(holes,2):
 if a['part']!=b['part']:continue
 ka=next(i for i,v in enumerate(a['axis']) if v);kb=next(i for i,v in enumerate(b['axis']) if v)
 if ka==kb:
  r=(a['diameter']+b['diameter'])/2;dist=math.sqrt(sum((a['xyz'][i]-b['xyz'][i])**2 for i in range(3) if i!=ka))
  aa=sorted([a['xyz'][ka],a['xyz'][ka]+a['axis'][ka]*a['depth']]);bb=sorted([b['xyz'][ka],b['xyz'][ka]+b['axis'][ka]*b['depth']])
  if dist<r-.001 and min(aa[1],bb[1])-max(aa[0],bb[0])>.001:hole_collisions.append([a['id'],b['id']])
assert not hole_collisions,hole_collisions
for name,data in [('parts',parts),('holes',holes),('hinges',hinges),('shelf_pins',pins)]: (O/f'data/{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
(O/'audit/design_checks.json').write_text(json.dumps(dict(parts=len(parts),holes=len(holes),hinges=len(hinges),shelf_pins=len(pins),blank_overlaps=intersections,cylinder_outside_blank=invalid,parallel_hole_intersections=hole_collisions,expected_net_volume_mm3=expected,volume_assumption='No intersecting bores. Native AutoCAD volume must match.',NOT_APPROVED=['actual survey','wall anchoring','lower doors3/4','tool library','woodWOP parser','material samples']),ensure_ascii=False,indent=2))
with (O/'data/furatjegyzek.csv').open('w',encoding='utf-8-sig',newline='') as f:
 wri=csv.writer(f,delimiter=';');wri.writerow(['ID','Darab','Funkcio','X','Y','Z','AX','AY','AZ','D','Melyseg','U','V','W','UA','VA','WA','Forras'])
 for h in holes:wri.writerow([h['id'],h['part'],h['kind'],*h['xyz'],*h['axis'],h['diameter'],h['depth'],*h['local_UVW'],*h['local_axis'],h['source']])
doc=ezdxf.new('R2010');doc.units=4;doc.appids.new('KYOTO_INK');m=doc.modelspace()
palette={'M01':(70,68,64),'M02':(178,160,132),'M03':(205,198,183)}
for p in parts:
 layer=p['id'];color=palette.get(p['material'][:3],(195,185,164));doc.layers.new(layer,dxfattribs={'color':8,'true_color':ezdxf.colors.rgb2int(color)})
 x,y,z,w,d,h=p['assembly_box_mm'];mesh=forms.cube(center=False);mesh.scale(w,d,h);mesh.translate(x,y,z)
 e=m.add_3dsolid(dxfattribs={'layer':layer});acis.export_dxf(e,[acis.body_from_mesh(mesh)])
 e.set_xdata('KYOTO_INK',[(1000,p['id']),(1000,p['material']),(1000,'R13 DESIGN - NOT RELEASED')])
doc.saveas(O/'rajzok/TV_R13_blanks.dxf')
def pt(v):return "'("+' '.join(f'{n:.6f}' for n in v)+')'
pre=['(setvar "CMDECHO" 0)','(setvar "FILEDIA" 0)','(setvar "OSMODE" 0)','(setvar "DELOBJ" 1)','(setq ki_ok 0)']
ops=[]
for h in holes:
 b=h['xyz'];ax=h['axis'];p=pt(b)
 ops += [f'(setq ki_e (ssname (ssget "_X" \'((0 . "3DSOLID") (8 . "{h["part"]}"))) 0))',f'(command "_.CYLINDER" {p} {h["diameter"]/2} {h["depth"]})','(setq ki_c (entlast))']
 if ax[0]:ops.append(f'(command "_.ROTATE3D" ki_c "" "_Y" {p} {90*ax[0]})')
 elif ax[1]:ops.append(f'(command "_.ROTATE3D" ki_c "" "_X" {p} {-90*ax[1]})')
 elif ax[2]<0:ops.append(f'(command "_.ROTATE3D" ki_c "" "_X" {p} 180)')
 ops += ['(command "_.SUBTRACT" ki_e "" ki_c "")','(if (and (entget ki_e) (not (entget ki_c))) (setq ki_ok (1+ ki_ok)))']
tail=['(princ (list "KI_R13_CUTS" ki_ok))','_.AUDIT','_N','_.MASSPROP','_ALL','','_N','(command "_.VPOINT" \'(1 -2 1.1))','(command "_.ZOOM" "_E")','(setvar "FACETRES" 5)','(command "_.SHADEMODE" "_G")','(command "_.-VIEW" "_S" "KI_R13_ZART")','(command "_.SAVEAS" "2018" "/tmp/TV_R13_zart.dwg")','_.QUIT','_Y']
Path('/tmp/ki13_build.scr').write_text('\n'.join(pre+ops+tail)+'\n')
(O/'integration/ki13_build.scr').write_text('\n'.join(pre+ops+tail)+'\n')
print(json.dumps({'parts':len(parts),'holes':len(holes),'expected_net_volume':expected,'hinges':len(hinges),'pins':len(pins)}))
