from pathlib import Path
import json,csv,itertools,hashlib,shutil,math
import ezdxf
from ezdxf.render import forms
from ezdxf.acis import api as acis
P=Path(__file__).resolve().parents[1]; O=P/'R12_muhely'
parts=json.loads((O/'data/parts.json').read_text()); by={p['id']:p for p in parts}
def ids(t): return [p for p in parts if p['type']==t]
def place(p,x,y,z,w,d,h):
 p['assembly_box_mm']=[x,y,z,w,d,h]
 assert sorted([w,d,h])==sorted([p['x'],p['y'],p['t']]),p['id']
# Correct R11 arithmetic. These remain nominal design envelopes, not cut approval.
for p in parts:
 if p['type'] in ['TV02-H1','TV02-H2']:
  p['y']=364;p['note']='R12 javítás: 382-18=364 mm; R11 346 mm téves. Illesztési játék még nincs levonva.'
 if p['type']=='TV02-CAP':
  p['y']=382;p['note']='R12 javítás: fedő 382 mm mély; a 400 mm-es korábbi fedő áthatolt a 397 mm magas frontokon. Kész mélység továbbra is 382+18=400.'
place(ids('TV01-S')[0],0,0,550,18,382,2330);place(ids('TV01-S')[1],702,0,550,18,382,2330)
place(ids('TV01-T')[0],18,0,550,684,382,18);place(ids('TV01-T')[1],18,0,2862,684,382,18)
place(ids('TV01-C')[0],351,0,568,18,374,2294)
for i,p in enumerate(ids('TV01-P')):place(p,19 if i<5 else 370,20,935+(i%5)*385,331,320,18)
for i,p in enumerate(ids('TV01-F')):place(p,1.5+i*360,-18,551.5,357,18,2327)
place(ids('TV01-H')[0],18,374,568,684,8,2294)
offsets=[0,840,1530,2220,2910];widths=[720,690,690,690,690]
for i,(x,w) in enumerate(zip(offsets,widths)):
 place(ids('TV02-S')[i*2],x,0,150,18,382,382);place(ids('TV02-S')[i*2+1],x+w-18,0,150,18,382,382)
 place(ids('TV02-T1')[0] if i==0 else ids('TV02-T2')[i-1],x+18,0,150,w-36,382,18)
 place(ids('TV02-H1')[0] if i==0 else ids('TV02-H2')[i-1],x+18,374,168,w-36,8,364)
 place(ids('TV02-F1')[0] if i==0 else ids('TV02-F2')[i-1],x+1.5,-18,151.5,w-3,18,397)
 if i!=1:place(ids('TV02-P1')[0] if i==0 else ids('TV02-P2')[i-2],x+19,20,341,w-38,320,18)
place(ids('TV02-CAP')[0],0,0,532,3600,382,18)
for i,p in enumerate(ids('TV03-P')):place(p,841.5+i*690,382,550,687,18,2330)
place(ids('GAP')[0],720,400,550,120,18,2330)
# Paired design dowel centres in a SINGLE assembly frame: X along wall, Y back, Z up.
# No machine transform or machining approval is implied.
joints=[];holes=[]
def joint(a,b,centres,axis,sign_a):
 j='J'+str(len(joints)+1).zfill(2);joints.append(dict(id=j,a=a['id'],b=b['id'],method='8x30 bükk köldökcsap + ragasztás, szerkezeti jóváhagyásra',n=3))
 for k,c in enumerate(centres):
  for part,sg,depth in [(a,sign_a,12),(b,-sign_a,22)]:
   v=[0,0,0];v[axis]=sg
   holes.append(dict(joint=j,pair=k+1,part=part['id'],xyz=c,axis=v,diameter=8,depth=depth,frame='ASSEMBLY_XYZ_NOT_MACHINE',status='DESIGN_NOT_NC'))
for i,s in enumerate(ids('TV01-S')):
 for e in ids('TV01-T'):
  z=e['assembly_box_mm'][2]+9;x=18 if i==0 else 702
  joint(s,e,[[x,y,z] for y in [50,191,332]],0,-1 if i==0 else 1)
for i,e in enumerate(ids('TV01-T')):
 z=568 if i==0 else 2862
 joint(e,ids('TV01-C')[0],[[360,y,z] for y in [50,191,332]],2,-1 if i==0 else 1)
for i,(x,w) in enumerate(zip(offsets,widths)):
 bottom=ids('TV02-T1')[0] if i==0 else ids('TV02-T2')[i-1]
 for n in range(2):
  side=ids('TV02-S')[2*i+n];xx=x+18 if n==0 else x+w-18
  joint(side,bottom,[[xx,y,159] for y in [50,191,332]],0,-1 if n==0 else 1)
  # top has 12 mm blind depth; side end 22 mm
  joint(ids('TV02-CAP')[0],side,[[x+9 if n==0 else x+w-9,y,532] for y in [50,191,332]],2,1)
# Geometry checks: all hole axes point into their own blank; design pairs coincide.
bad=[]
for h in holes:
 p=by[h['part']];bb=p['assembly_box_mm'];end=[h['xyz'][k]+h['axis'][k]*h['depth'] for k in range(3)]
 if not all(bb[k]-1e-6<=end[k]<=bb[k]+bb[k+3]+1e-6 for k in range(3)):bad.append(h)
overlaps=[]
for a,b in itertools.combinations(parts,2):
 A=a['assembly_box_mm'];B=b['assembly_box_mm'];v=[min(A[k]+A[k+3],B[k]+B[k+3])-max(A[k],B[k]) for k in range(3)]
 if min(v)>0.01:overlaps.append([a['id'],b['id'],v])
assert not bad,bad
assert not overlaps,overlaps
(O/'data/parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2))
(O/'data/joints.json').write_text(json.dumps({'joints':joints,'holes':holes},ensure_ascii=False,indent=2))
with (O/'data/kotopontok_furatkozepek.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['Kotes','Par','Darab','X','Y','Z','IranyX','IranyY','IranyZ','Atmero','Melyseg','Statusz'])
 for h in holes:w.writerow([h['joint'],h['pair'],h['part'],*h['xyz'],*h['axis'],h['diameter'],h['depth'],h['status']])
# Valid ACIS 3D solids, one per named board, no pretended Livewood plug-in metadata.
doc=ezdxf.new('R2010');doc.units=4;doc.appids.new('KYOTO_INK');m=doc.modelspace()
for p in parts:
 layer='KI_'+p['type'];
 if layer not in doc.layers:doc.layers.new(layer,dxfattribs={'color':8 if p['material'].startswith('M01') else 30 if p['type']=='TV03-P' else 7})
 x,y,z,w,d,h=p['assembly_box_mm'];mesh=forms.cube(center=False);mesh.scale(w,d,h);mesh.translate(x,y,z)
 e=m.add_3dsolid(dxfattribs={'layer':layer});acis.export_dxf(e,[acis.body_from_mesh(mesh)])
 e.set_xdata('KYOTO_INK',[(1000,p['id']),(1000,p['material']),(1000,'R12 DESIGN - NO MACHINING')])
doc.saveas(O/'rajzok/TV_modul_R12_alkatreszmodell.dxf')
check=ezdxf.readfile(O/'rajzok/TV_modul_R12_alkatreszmodell.dxf');count=0
for e in check.modelspace().query('3DSOLID'):
 pid=e.get_xdata('KYOTO_INK')[0].value;vs=acis.vertices_from_body(acis.load_dxf(e)[0]);bb=by[pid]['assembly_box_mm']
 for k in range(3):assert abs(min(v[k] for v in vs)-bb[k])<.001 and abs(max(v[k] for v in vs)-bb[k]-bb[k+3])<.001,pid
 count+=1
# Update finished contours and MPR envelopes for corrected back panels only.
for p in parts:
 if p['type'] in ['TV02-H1','TV02-H2']:
  f=O/'mpr_alap'/p['mpr'];s=f.read_text();f.write_bytes(s.replace('B="346"','B="364"').replace('\r\n','\n').replace('\n','\r\n').encode('ascii'))
  f=O/'dxf'/(p['id']+'.dxf');s=f.read_text();f.write_text(s.replace('\n346\n','\n364\n').replace('\n376\n','\n394\n'))
 if p['type']=='TV02-CAP':
  f=O/'mpr_alap'/p['mpr'];s=f.read_text();f.write_bytes(s.replace('B="400"','B="382"').replace('\r\n','\n').replace('\n','\r\n').encode('ascii'))
  f=O/'dxf'/(p['id']+'.dxf');s=f.read_text();f.write_text(s.replace('\n400\n','\n382\n').replace('\n430\n','\n412\n'))
proof={'revision':'R12','parts':len(parts),'solid_readback':count,'dxf_audit_errors':len(check.audit().errors),'nominal_board_overlaps':overlaps,'paired_dowel_joints':len(joints),'design_holes':len(holes),'hole_axis_outside_blank':bad,'correction':'lower clear height 382-18=364 not346; 5 backs updated','NOT_TESTED':['loads/fasteners','actual site geometry','whole apartment opening clearance','woodWOP parsing/machine simulation','toolholder/clamp collisions','Livewood import/database integration'],'limitations':'Solid blank assembly with separate joint-centre schedule; holes are NOT subtracted from solids. No machining operations in MPR.'}
(O/'audit/engineering_checks.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2))
# Evidence from user DWG: types/layers decoded; ACIS solids did NOT survive this converter.
ref=ezdxf.readfile('/tmp/coo1.dxf');solids=list(ref.modelspace().query('3DSOLID'))
(O/'sources/coo1_kiolvasas.json').write_text(json.dumps({'source':'/Users/peterkapusi/Downloads/coo1.dwg','sha256':hashlib.sha256(Path('/Users/peterkapusi/Downloads/coo1.dwg').read_bytes()).hexdigest(),'modelspace_solid_entities':len(solids),'solids_with_acis_payload':sum(bool(e.sat or e.sab) for e in solids),'layers':[l.dxf.name for l in ref.layers],'status':'rétegek és objektumtípusok kiolvashatók; térfogattest-geometria a konverterrel nem igazolt. A konvertált referencia nem gyártási adat.'},ensure_ascii=False,indent=2))
shutil.copy('/tmp/coo1_preview.png',O/'sources/coo1_preview.png')
print(json.dumps(proof,ensure_ascii=False))
