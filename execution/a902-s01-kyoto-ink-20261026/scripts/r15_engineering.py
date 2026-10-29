"""R15 manufacturing proposal. No CNC execution or physical approval is implied."""
from pathlib import Path
import json,copy,math,shutil,hashlib,itertools,openpyxl,csv
import ezdxf
from ezdxf.render import forms
from ezdxf.acis import api as acis
P=Path(__file__).resolve().parents[1]; O=P/'R15_muhely'; B=P/'R14_muhely'
for d in ['data','audit','rajzok','integration','sources','cimkek','pilot']:(O/d).mkdir(parents=True,exist_ok=True)
def put(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2))
parts=json.loads((B/'data/parts.json').read_text());holes=json.loads((B/'data/holes.json').read_text())
hinges=json.loads((B/'data/hinges.json').read_text());pins=json.loads((B/'data/shelf_pins.json').read_text())
by={p['id']:p for p in parts};changes=[];notches=[];hardware=[]
oldparts=copy.deepcopy(parts)
def addhole(p,xyz,axis,d,depth,kind,source):
 h=dict(id=f'H{len(holes)+1:04}',part=p['id'],xyz=xyz,axis=axis,diameter=d,depth=depth,kind=kind,source=source,status='DESIGN_NOT_NC');holes.append(h);return h
def hw(id,sku,name,box,kind='ENVELOPE',source='R15 design'):
 hardware.append(dict(id=id,sku=sku,name=name,box=box,geometry=kind,source=source,status='DESIGN_NOT_RELEASED'))
# Actual workbook is preserved byte-for-byte before any regenerated sheets.
src=B/'TV_R14_alkatreszek_furatok_cimkek.xlsx'; dest=O/'sources/TV_R14_eredeti_munkafuzet.xlsx'
if not dest.exists():shutil.copy2(src,dest)
w=openpyxl.load_workbook(src,data_only=False)
put('audit/R14_excel_snapshot.json',{'source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'sheets':{s.title:[list(r) for r in s.iter_rows(values_only=True)] for s in w}})
# Camar IN hangers need a recessed back. Move only hidden construction; keep facade.
for p in parts:
 b=p['assembly_box_mm'];t=p['type']
 if t in ['TV01-H','TV02-H1','TV02-H2']:b[1]-=20
 if t=='BAT' and p['id'].startswith('KI14-BAT-'):
  b[1]-=20;b[5]=2142 if b[2]>500 else 212;p['x']=b[5]
 if t=='RAIL':b[1]-=20;b[2]-=130 if b[2]>500 else 132
 if t in ['TV01-P','TV02-P1','TV02-P2']:b[4]=290;p['y']=290
 if t=='TV01-C':b[4]=354;p['y']=354
for h in holes:
 k=h['kind'];p=by[h['part']]
 if k.startswith(('LEC_OLDAL','HATLAP_LEC')):
  h['xyz'][1]-=20
  if p['assembly_box_mm'][2]<550:
   h['xyz'][2]={350:290,490:370,365:305,505:385}.get(h['xyz'][2],h['xyz'][2])
  else:h['xyz'][2]={2780:2700,2795:2715}.get(h['xyz'][2],h['xyz'][2])
 if k.startswith('MEREVITO_CSAP'):
  h['xyz'][1]-=20;h['xyz'][2]-=130 if h['xyz'][2]>550 else 132
 if k=='AV_KABEL':h['xyz'][1]-=20
 if k=='POLCTARTO' and h['xyz'][1]==310:h['xyz'][1]=280
for h in pins:
 if h['xyz'][1]==310:h['xyz'][1]=280
for p in parts:
 if p['assembly_box_mm']!=next(q for q in oldparts if q['id']==p['id'])['assembly_box_mm']:
  changes.append({'part':p['id'],'old':next(q for q in oldparts if q['id']==p['id'])['assembly_box_mm'],'new':p['assembly_box_mm'],'reason':'Camar IN helyigény: 20mm hátlapvisszahúzás, szabad függesztőtér; polcmélység 320→290mm.'})
  p['note']='R15 rejtett szerkezeti átrendezés. Látható front változatlan; hátlap Y354..362, polc 290mm mély.'
# Hanger pattern from Camar 80702Z1IN F1, 2016-05-01: Ø10,12 deep,32x64 centres.
# Top row 30 below underside of top (minimum20), rear row20 from rear. Conservative envelope.
starts=[0,840,1530,2220,2910];widths=[720,690,690,690,690]
groups=[('T',0,720,2862,[p for p in parts if p['type']=='TV01-S'],next(p for p in parts if p['type']=='TV01-H'))]
for i,(off,ww) in enumerate(zip(starts,widths)):
 groups.append((str(i+1),off,ww,532,[p for p in parts if p['type']=='TV02-S'][2*i:2*i+2], [p for p in parts if p['type'] in ['TV02-H1','TV02-H2']][i]))
mounts=[]
for module,off,ww,top,sides,back in groups:
 for hand in range(2):
  x=off+18 if hand==0 else off+ww-18;axis=[-1,0,0] if hand==0 else [1,0,0]
  hs=[addhole(sides[hand],[x,y,z],axis,10,12,'CAMAR807_DUBEL','Camar807_IN.pdf F1: Ø10/12,32x64;30mm felső visszaállás; új vasalat/oldallap próba és alkalmazás jóváhagyandó')['id'] for y in [330,362] for z in [top-30,top-94]]
  ident=f'HG-{module}-{hand+1}';sku='80702Z1INSX' if hand==0 else '80702Z1INDX'
  hw(ident,sku,'Camar 807 IN függesztő / konzervatív helyfoglalás',[x if hand==0 else x-10,314,top-122,10,68,102],source='Camar807_IN.pdf; befoglaló tervezői helyfoglalás, nem gyártói 3D')
  # Full-height open corner avoids a router corner-radius dependency in the back.
  bx=back['assembly_box_mm'];xx=bx[0] if hand==0 else bx[0]+bx[3]-22
  nc={'id':f'NC-{module}-{hand+1}','part':back['id'],'box':[xx,354,top-127,22,8,bx[2]+bx[5]-(top-127)],'method':'Nyitott sarokkivágás; két egyenes vágás, sarokig. CNC-szerszámút nincs kiadva.'};notches.append(nc)
  hw('WP-'+ident,'897ASZ11212','Camar anti-drop falilemez /120x120 helyfoglalás',[off+30 if hand==0 else off+ww-150,384,top-115,120,3,120],source='Camar897ASZ11212; furathely a valós lemez sablonjával, falrögzítés külön')
  mounts.append({'id':ident,'module':module,'side':sides[hand]['id'],'holes':hs,'plate':'WP-'+ident,'load_path':'oldallap → 807IN → 897 lemez → méretezett távtartó/falhorgony → teherhordó fal','wall_plane_nominal_Y':418,'plate_back_Y':387,'packer_nominal_mm':31,'condition':'31mm távtartás + hook beállítás 1:1 próbaszereléssel ellenőrizendő; horgony és szilárd távtartó a falhoz méretezendő. Nem átvezetett teher a vékony hátlapon.'})
# Removable decor panels: 12 MF375 clips/panel; 2 pilot screws/clip. Wall rails independent.
panels=[p for p in parts if p['type']=='TV03-P'];clips=[]
for j,p in enumerate(panels):
 x,y,z,ww,d,hh=p['assembly_box_mm']
 for row,zz in enumerate([650,1350,2050,2750]):
  for col,dx in enumerate([60,ww/2,ww-60]):
   xx=x+dx;ids=[addhole(p,[xx+a,400,zz],[0,-1,0],2.5,12,'MF375_PANEL_CSAVAR','MF375.pdf 32.004mm furatköz; Ø2.5x12 próbaérték 3.5x16 pan-head csavarhoz')['id'] for a in [-16.002,16.002]]
   id=f'PC-{j+1}-{row+1}{col+1}';hw(id,'MF375 50.8mm','Monarch panelklipsz / profil helyfoglalás',[xx-25.4,400,zz-9.525,50.8,6.353,34.93],source='MF375.pdf; nem részletes gyári profilmodell')
   clips.append({'id':id,'part':p['id'],'holes':ids,'centre':[xx,400,zz]})
for r,zz in enumerate([650,1350,2050,2750]):
 hw(f'PR-{r+1}','MF375 rail / vágva 2760','Fali klipszsín két toldott szálból',[840,400,zz-9.525,2760,6.353,34.93],source='MF375; páros profilok helyfoglalása szándékosan közös, nem tömör testek ütközése')
 hw(f'PK-{r+1}','Egyedi szilárd kiegyenlítés','Fali síkbeállítás, névleges 11.647mm',[840,406.353,zz-9.525,2760,11.647,34.93],source='18mm panelhát-fal hézag mínusz6.353mm; helyszínen méretezendő')
# TV bracket: independent rigid spacers; precise anchor pattern is not fabricated.
hw('TV-BRACKET','3836050 / TVM3605','Vogel TV konzol gyári befoglaló',[1882.5,360,1236,675,22,428],source='Vogel3605.pdf')
hw('TV-SCREEN','QE65Q7FAAUXXH','Samsung 65 TV névleges készüléktest',[1493.55,299.4,1033,1452.9,60.6,834],source='R05 kiválasztott termék; VESA magassági offset ellenőrzendő')
# AV service ventilation: actual bores, not decorative hatch marks. 37.7 cm² per bank.
av=next(p for p in parts if p['type']=='TV02-H2')
for zs in [[195,210,225,240],[460,475,490,505]]:
 for z in zs:
  for x in range(1035,1201,15):addhole(av,[x,362,z],[0,-1,0],10,8,'AV_SZELLOZO','R15 12x4 Ø10/bank;37.70cm² szabad felület. Légút és hőpróba szükséges.')
for x,d,k in [(920,20,'230V elkülönített'),(950,12,'24V ágak')]:addhole(av,[x,362,250],[0,-1,0],d,8,'KABEL_'+k,'R15 terv; szigetelő perem/átvezető, kábel és erősáram elkülönítése')
bottom=[p for p in parts if p['type'] in ['TV02-T1','TV02-T2']][1]
addhole(bottom,[920,80,168],[0,0,-1],12,18,'LED_ALSO_ATVEZETES','R15 24V vezeték; szigetelő perem, Ø12 átmérő tervérték')
hw('EL-TRAY','Egyedi acél 430x240x2','Kivehető szerelőtálca',[890,60,185,430,240,2],kind='DESIGN_SOLID')
hw('PSU','LPV-150-24','MEAN WELL /151.2W',[910,80,200,191,63,37.5],source='MeanWell.pdf')
for i,yy in enumerate([80,150,220]):hw('DIM-'+str(i+1),'SR-ZG9101FA-DIM','Sunricher CV PWM / külön fényág',[1120,yy,200,170,53.4,28],source='Sunricher_DIM.pdf V1;170x53.4x28 nagyobb gyári ház alapján')
hw('EL-PARTITION','Egyedi szigetelő válaszfal','230V és24V szerelési zóna elválasztás',[1107,60,187,3,240,75],kind='DESIGN_SOLID')
# The tray's attachment to wood is deliberately mechanical, removable and accessible.
for x in [905,1305]:
 for yy in [75,285]:
  addhole(bottom,[x,yy,168],[0,0,-1],2.5,10,'TALCA_TAVTARTO','17mm szigetelő távtartó,3.5x30 csavar; tálca2+17=19mm,lapba11mm; próbafúrás')
  hw(f'TRAY-SP-{x}-{yy}','17mm szigetelő távtartó','Tálca alátámasztás',[x-5,yy-5,168,10,10,17],kind='DESIGN_SOLID')
for i,h in enumerate(hinges):
 x,y,z=h['xyz'];hw(f'HINGE-{i+1:02}',h['sku']+' + '+h['plate'],'Blum pánt / kar helyfoglalás',[x-17.5,-16,z-25,35,72,50],source='R13 gyári furatkép; nem valódi mozgó mechanizmus')
for i,t in enumerate(json.loads((B/'data/tipon.json').read_text())):
 x,y,z=t['position'];long=t['unit']=='956A1004';hw(f'TIP-{i+1}',t['unit']+' + '+t['adapter'],'TIP-ON befoglaló',[x-6,0,z-6,12,79 if long else 53,12],source='Blum R14 adapterfuratok; test egyszerűsített')
# Reuse proven right-handed frames and cylinder validation, then append explicit notches.
tail=(P/'scripts/r13_cad.py').read_text().split('# Assign a canonical right-handed frame')[1]
tail=('# Assign a canonical right-handed frame'+tail).replace('R13','R15').replace('ki13','ki15')
exec(compile(tail,__file__+':canonical_pipeline','exec'))
script=Path('/tmp/ki15_build.scr').read_text();cutops=[]
for n in notches:
 x,y,z,ww,d,hh=n['box'];pid=n['part']
 cutops += [f'(setq ki_e (ssname (ssget "_X" \'((0 . "3DSOLID") (8 . "{pid}"))) 0))',f'(command "_.BOX" \'({x} {y} {z}) \'({x+ww} {y+d} {z}) {hh})','(setq ki_c (entlast))','(command "_.SUBTRACT" ki_e "" ki_c "")']
script=script.replace('(princ (list "KI_R15_CUTS" ki_ok))','\n'.join(cutops)+'\n(princ (list "KI_R15_CUTS" ki_ok))').replace('/tmp/TV_R15_zart.dwg','/tmp/TV_R15_zart_v1.dwg')
Path('/tmp/ki15_build.scr').write_text(script);(O/'integration/ki15_build.scr').write_text(script)
checks=json.loads((O/'audit/design_checks.json').read_text());checks['expected_net_volume_mm3']-=sum(math.prod(n['box'][3:]) for n in notches);checks['notches']=len(notches);checks['NOT_APPROVED']=['site dimensions','Camar application and shim/anchor design','3-4 front owner choice','woodWOP5 machine/tool/fixture','material samples','thermal/electrical commissioning'];put('audit/design_checks.json',checks)
# Whole cylinder AABB screen, including orthogonal bores.
collisions=[]
def bb(h):
 k=next(i for i,v in enumerate(h['axis']) if v);ends=[h['xyz'][i]+h['axis'][i]*h['depth'] for i in range(3)]
 return [[min(h['xyz'][i],ends[i]) if i==k else h['xyz'][i]-h['diameter']/2 for i in range(3)],[max(h['xyz'][i],ends[i]) if i==k else h['xyz'][i]+h['diameter']/2 for i in range(3)]]
for a,b in itertools.combinations(holes,2):
 if a['part']!=b['part']:continue
 aa,ab=bb(a);ba,bc=bb(b)
 if all(min(ab[i],bc[i])-max(aa[i],ba[i])>.001 for i in range(3)):collisions.append([a['id'],b['id']])
assert not collisions,collisions
for n in notches:
 for h in holes:
  if h['part']!=n['part']:continue
  a,b=bb(h);c=n['box'];assert not all(min(b[i],c[i]+c[i+3])-max(a[i],c[i])>.001 for i in range(3)),(n['id'],h['id'])
put('audit/all_axis_bore_check.json',{'bores':len(holes),'intersecting_bore_AABBs':collisions,'notch_bore_intersections':0,'scope':'part geometry, not tool/fixture simulation'})
for name,data in [('changes',changes),('hardware_geometry',hardware),('mounts',mounts),('panel_clips',clips),('notches',notches)]:put('data/'+name+'.json',data)
for name in ['tipon.json','connections.json']:shutil.copy2(P/'R14_muhely/data'/name,O/'data'/name)
print('R15',len(parts),'parts',len(holes),'bores',len(notches),'notches',len(hardware),'hardware envelopes',checks['expected_net_volume_mm3'])
