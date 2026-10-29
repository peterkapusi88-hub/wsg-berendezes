from pathlib import Path
import json,copy,math,itertools,csv,hashlib,shutil
import ezdxf
from ezdxf.render import forms
from ezdxf.acis import api as acis
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok';BASE=P/'R15_muhely'
def read(n):return json.loads((BASE/n).read_text())
def put(n,x):(O/n).write_text(json.dumps(x,ensure_ascii=False,indent=2))
old=read('data/parts.json');oldh=read('data/holes.json');oldby={p['id']:p for p in old}
# Latest owner: six unequal vertical zones inferred from visible seams; NO horizontal split.
starts=[0,720,1170,1620,2700,3150];widths=[720,450,450,1080,450,450]
parts=[copy.deepcopy(p) for p in old if p['assembly_box_mm'][2]>=550 or p['type']=='TV02-CAP'];by={p['id']:p for p in parts}
cap=next(p for p in parts if p['type']=='TV02-CAP')
holes=[copy.deepcopy(h) for h in oldh if h['part'] in by and h['part']!=cap['id']]
# Upper panel width chain:720+200+4*670=3600. Edge margins of mounting clips retained.
for i,p in enumerate([q for q in parts if q['type']=='TV03-P']):
 oldx=p['assembly_box_mm'][0];newx=921.5+i*670
 for h in holes:
  if h['part']==p['id']:
   dx=h['xyz'][0]-oldx
   if dx<150:pass
   elif dx>537:dx-=20
   else:dx-=10
   h['xyz'][0]=newx+dx
 p['assembly_box_mm'][0]=newx;p['assembly_box_mm'][3]=667;p['y']=667 if p['x']==2330 else p['y'];p['x']=667 if p['x']==687 else p['x']
gap=next(p for p in parts if p['type']=='GAP');gap['assembly_box_mm']=[720,382,550,200,18,2330];gap['x']=2330;gap['y']=200;gap['material']='M16-BRONZE';gap['name']='200 mm matt bronzbarna betétsáv / nem üres rés';gap['note']='Front Y382 azonos panelhordozó-sík; tapétaréteg előrébb. Hátsó18mm szerelőtér. Oldalról súrolófény.'
# Reuse the verified M5 carcass drilling pattern, retaining IDs for matching existing roles.
template=[p for p in old if p['assembly_box_mm'][0]>=2910 and p['assembly_box_mm'][2]<550 and p['type'] not in ['TV03-P','TV02-CAP','TV02-P2']]
priorstarts=[0,840,1530,2220,2910];priorwidth=[720,690,690,690,690]
def role(p):
 t=p['type']
 if t.startswith('TV02-H'):return 'BACK'
 if t.startswith('TV02-F'):return 'FRONT'
 if t.startswith('TV02-T'):return 'BOTTOM'
 return t
notches=[];mapping=[];drawers=[];hardware=[];connections=[]
def hole(p,xyz,axis,d,dep,kind):
 ident=f'R16H{len(holes)+1:04}';holes.append(dict(id=ident,part=p['id'],xyz=xyz,axis=axis,diameter=d,depth=dep,kind=kind,source='R16 szerkezeti terv; anyaghoz illesztett próbafúrás kell',status='DESIGN_NOT_NC'));return ident
def newpart(id,name,box,material='M16-DRAWER15',type='DRAWER',t=15):
 x,y,z,w,d,h=box
 if w==t:u,v=h,d
 elif h==t:u,v=w,d
 else:u,v=w,h
 p=copy.deepcopy(old[0]);p.update(id=id,name=name,type=type,x=u,y=v,t=t,material=material,assembly_box_mm=box,grain='hosszanti / mintázat jóváhagyandó',edge=[0,0,0,0],note='R16 készméret; nem felmért gyártási méret',status='TERV - NEM GYARTAS');parts.append(p);by[id]=p;return p
def hw(id,name,box,sku='tervezési specifikáció'):hardware.append(dict(id=id,name=name,box=box,sku=sku,geometry='ENVELOPE',status='DESIGN_NOT_RELEASED'))
for module,(off,W) in enumerate(zip(starts,widths),1):
 group=[];matches={}
 if module<=5:
  a=priorstarts[module-1];b=a+priorwidth[module-1]
  previous=[p for p in old if a<=p['assembly_box_mm'][0]<b and p['assembly_box_mm'][2]<550 and p['type'] not in ['TV02-CAP','GAP-LOW','TV02-P1','TV02-P2']]
 else:previous=[]
 used=set()
 def mx(x):return off+(x-2910)+(W-690 if x>=3255 else 0)
 for t in template:
  p=copy.deepcopy(t);bb=p['assembly_box_mm'];bb[0]=mx(bb[0]);
  if bb[3]>100:bb[3]+=W-690
  candidates=[q for q in previous if role(q)==role(t) and q['id'] not in used]
  candidates.sort(key=lambda q:q['assembly_box_mm'][0]);pid=candidates[0]['id'] if candidates else f'KI16-M{module}-{role(t)}-{len(group)+1:02}'
  used.add(pid);p['id']=pid;p['name']=f'M{module} / '+t['name'].split(' / ')[-1];p['note']='R16 új frontosztás; korábbi R15 program nem használható automatikusan.'
  if p['x']==t['assembly_box_mm'][3]:p['x']+=W-690
  elif p['y']==t['assembly_box_mm'][3]:p['y']+=W-690
  parts.append(p);by[pid]=p;group.append(p);matches[t['id']]=pid
  for h in oldh:
   if h['part']!=t['id'] or h['kind'].startswith(('PANT','TALP','POLCTARTO','TIPON','TALCA')):continue
   hh=copy.deepcopy(h);hh['part']=pid;hh['xyz'][0]=mx(hh['xyz'][0]);hh['id']=f'R16H{len(holes)+1:04}';holes.append(hh)
  mapping.append({'module':module,'part':pid,'pattern_source':t['id'],'old_module_part':pid if pid in oldby else None})
 # Cap dowel mating locations, copied from M5 section only.
 for h in oldh:
  if h['part']==cap['id'] and h['xyz'][0]>=2910:
   hh=copy.deepcopy(h);hh['xyz'][0]=mx(hh['xyz'][0]);hh['id']=f'R16H{len(holes)+1:04}';holes.append(hh)
 back=next(p for p in group if role(p)=='BACK')
 for hand in [0,1]:
  xx=back['assembly_box_mm'][0] if hand==0 else back['assembly_box_mm'][0]+back['assembly_box_mm'][3]-22
  notches.append(dict(id=f'NC-M{module}-{hand+1}',part=back['id'],box=[xx,354,405,22,8,126],method='Nyitott sarok, két egyenes fűrészes vágás; nem MPR'))
 # Drawer: 15mm birch plywood, 290 depth, 13mm bottom recess, 6mm cabinet gap per side.
 SKW=W-78
 l=newpart(f'KI16-D{module}-L','Fiók bal oldal',[off+24,0,197,15,290,250]);r=newpart(f'KI16-D{module}-R','Fiók jobb oldal',[off+W-39,0,197,15,290,250])
 bot=newpart(f'KI16-D{module}-B','Fiók fenék',[off+39,0,210,SKW,290,15]);ff=newpart(f'KI16-D{module}-F','Fiókdoboz belső előlap',[off+39,0,225,SKW,15,222]);bk=newpart(f'KI16-D{module}-H','Fiókdoboz hátlap',[off+39,275,225,SKW,15,222])
 for side,sign in [(l,1),(r,-1)]:
  xx=side['assembly_box_mm'][0]+(15 if sign<0 else 0)
  for yy in [50,145,240]:
   h1=hole(side,[xx,yy,217.5],[sign,0,0],4.5,15,'FIÓK_FENEK_ATMENO');h2=hole(bot,[xx+sign*15,yy,217.5],[sign,0,0],2.5,20,'FIÓK_FENEK_PILOT');connections.append([h1,h2,'4x35 csavar / próba'])
  for target,yy in [(ff,7.5),(bk,282.5)]:
   for zz in [270,400]:
    h1=hole(side,[xx,yy,zz],[sign,0,0],4.5,15,'FIÓK_ELO_HAT_ATMENO');h2=hole(target,[xx+sign*15,yy,zz],[sign,0,0],2.5,20,'FIÓK_ELO_HAT_PILOT');connections.append([h1,h2,'4x35 csavar / próba'])
 decor=next(p for p in group if role(p)=='FRONT')
 for xx in [off+100,off+W-100]:
  for zz in [270,400]:
   h1=hole(ff,[xx,15,zz],[0,-1,0],5,15,'FRONT_ROGZITES_ATMENO');h2=hole(decor,[xx,-3,zz],[0,-1,0],2.5,12,'FRONT_ROGZITES_PILOT');connections.append([h1,h2,'4x30 csavar +3mm távtartó / frontállítás'])
 mass=sum(math.prod(p['assembly_box_mm'][3:])*700/1e9 for p in [l,r,bot,ff,bk,decor])+1.1
 unit='T60L7140 / S1' if mass>=10 else 'T60L7040 / S0';limit=20 if mass>=10 else 10
 drawers.append(dict(id=f'D{module}',module=module,front=decor['id'],parts=[p['id'] for p in [l,r,bot,ff,bk]],offset=off,width=W,LW=W-36,SKW=SKW,NL=300,depth=290,inside=[SKW,260,222],litres=SKW*260*222/1e6,empty_mass_estimate_kg=mass,motion_unit=unit,max_total_kg=limit,contents_limit_estimate_kg=max(0,limit-mass),sync_cut_mm=W-36-267,stabilizer_cut_mm=W-36-315,status='Fa geometria kidolgozva; MOVENTO sablonfuratok + valós tömegpróba még szükséges'))
 for xx in [off+18,off+W-48]:hw(f'SLIDE-D{module}-{xx}','MOVENTO300 sín helyfoglalás',[xx,0,181.5,30,303,28.5],'760H3000S')
 # Hardware template gates are visible, not invented bores in a CNC program.
 hw(f'LED-D{module}','Fix testre szerelt belső LED; nincs mozgó kábel',[off+50,20,519.5,W-100,18,12.5],'Loox5 2194 + LED3040 +833.89.253')
# Bronze band is a real removable panel, supported like the decorative field.
for zz in [650,1350,2050,2750]:
 for xx in [803.998,836.002]:hole(gap,[xx,400,zz],[0,-1,0],2.5,12,'BRONZ_MF375_PILOT')
 hw(f'BRONZE-CLIP-{zz}','Bronzbetét MF375 pár + fali kiegyenlítés',[794.6,400,zz-9.525,50.8,6.353,34.93],'MF375')
# Keep tower hardware, panel mounting changes separately rebuilt.
for h in read('data/hardware_geometry.json'):
 if h['id'].startswith(('HG-T','WP-HG-T')) or h['id'] in ['TV-BRACKET','TV-SCREEN'] or (h['id'].startswith('HINGE-') and int(h['id'].split('-')[1])<=10) or h['id'] in ['TIP-1','TIP-2']:hardware.append(h)
for p in [p for p in parts if p['type']=='TV03-P']:
 x=p['assembly_box_mm'][0]
 for zz in [650,1350,2050,2750]:
  for dx in [60,333.5,607]:hw(f'CLIP-{p["id"]}-{zz}-{dx}','MF375 klipsz',[x+dx-25.4,400,zz-9.525,50.8,6.353,34.93],'MF375')
for module,(off,W) in enumerate(zip(starts,widths),1):
 for hand in [0,1]:hw(f'HG-M{module}-{hand}','Camar807 IN',[off+18 if hand==0 else off+W-28,314,410,10,68,102],'80702Z1IN SX/DX')
# Accessible electronics in tower lower rear bays. No service tray occupies the new drawers.
hw('SERVICE-L','Bal oldali bontható szerelőlemez',[30,278,600,300,2,300],'2mm szerelőlemez;4sarok távtartó')
hw('SERVICE-R','Jobb oldali bontható szerelőlemez',[390,278,600,300,2,300],'2mm szerelőlemez;4sarok távtartó')
hw('PSU','MEAN WELL LPV15024',[400,282,625,191,37.5,63],'LPV-150-24')
for i in range(3):hw(f'DIM-{i+1}','Sunricher CV PWM dimmer',[50,282,620+i*80,170,28,53.4],'SR-ZG9101FA-DIM')
for i,xx in enumerate([333,369]):hw(f'LED-T{i+1}','Torony belső LED / a polcok előtt',[xx,0,600,18,12.5,2250],'Loox5 2194 + LED3040 +833.89.253')
hw('LED-BRONZE','Oldallapi rejtett45fokos alumínium LEDprofil',[720,330,565,18,18,2300],'18x18 sarokprofil,8mm szalag,diffúzor; mintapróba')
# Accessory timber plate mounting and cable ports: designed, no wall anchor guess.
for p in [p for p in parts if p['type']=='TV01-H']:
 for xx in [45,315,405,675]:
  for zz in [615,885]:hole(p,[xx,362,zz],[0,-1,0],5,8,'SERVICE_M4_ATMENO')
 for xx,d in [(630,20),(660,12)]:hole(p,[xx,362,780],[0,-1,0],d,8,'SERVICE_KABEL')
# Upper reveal retained as separate bronze laminate-faced substrate, no art in the band.
hinges=[h for h in read('data/hinges.json') if oldby[h['front']]['type']=='TV01-F'];pins=[h for h in read('data/shelf_pins.json') if oldby[h['shelf']]['type']=='TV01-P']
# Drop stale part operations and IDs from regenerated program metadata.
for p in parts:p['ops']=[];p['mpr']=p['id']+'.mpr'
# Existing stable geometry pipeline computes frames, containment and overlaps and writes native CAD script.
by={p['id']:p for p in parts}
tail=(P/'scripts/r13_cad.py').read_text().split('# Assign a canonical right-handed frame')[1]
exec(compile(('# Assign a canonical right-handed frame'+tail).replace('R13','R16').replace('ki13','ki16'),__file__,'exec'))
# Restore source handle clobbered by geometry-loop local names.
BASE=P/'R15_muhely'
# Tower back notches retained; all six lower backs notched.
notches += [n for n in json.loads((BASE/'data/notches.json').read_text()) if n['box'][2]>550]
s=Path('/tmp/ki16_build.scr').read_text();cut=[]
for n in notches:
 x,y,z,w,d,h=n['box'];cut.extend([f'(setq ki_e (ssname (ssget "_X" \'((0 . "3DSOLID") (8 . "{n["part"]}"))) 0))',f'(command "_.BOX" \'({x} {y} {z}) \'({x+w} {y+d} {z}) {h})','(setq ki_c (entlast))','(command "_.SUBTRACT" ki_e "" ki_c "")'])
s=s.replace('(princ (list "KI_R16_CUTS" ki_ok))','\n'.join(cut)+'\n(princ (list "KI_R16_CUTS" ki_ok))').replace('/tmp/TV_R16_zart.dwg','/tmp/TV_R16_zart_v1.dwg');Path('/tmp/ki16_build.scr').write_text(s);(O/'integration/ki16_build.scr').write_text(s)
checks=json.loads((O/'audit/design_checks.json').read_text());checks['expected_net_volume_mm3']-=sum(math.prod(n['box'][3:]) for n in notches);checks['NOT_APPROVED']=['helyszíni felmérés','MOVENTO gyári fúrósablon és vasalati próba','falrögzítés','woodWOP és gépi próba','szín/nyomat/adhézió/matt bronz minta','asztal200mm eltolás tulajdonosi és helyszíni próba'];put('audit/design_checks.json',checks)
# Analytical drawer-front sweep; actual coffee-table bounds from R15 room model.
coffee=[2050,-858,0,450,700,350];proposed=coffee.copy();proposed[1]-=200
motions=[]
for d in drawers:
 p=by[d['front']];b=p['assembly_box_mm']
 def hit(t,table):return all(min(b[k]+b[k+3]-(t if k==1 else 0),table[k]+table[k+3])-max(b[k]-(t if k==1 else 0),table[k])>0.001 for k in range(3))
 hits=[t for t in range(301) if hit(t,coffee)];pro=[t for t in range(301) if hit(t,proposed)]
 motions.append({'drawer':d['id'],'steps_mm':1,'range_mm':[0,300],'original_first_collision_mm':hits[0] if hits else None,'proposed_collisions':len(pro),'proposed_table_move_Y_mm':-200})
assert not any(m['proposed_collisions'] for m in motions)
put('audit/drawer_sweep.json',{'scope':'Névleges téglatestfrontok,1mm transzláció; nem emberi használat, teljes mechanizmus vagy falfelmérés','original_table':coffee,'proposed_table':proposed,'front_clearance_mm_at_full_extension':37,'table_to_sofa_nominal_mm':330,'status':'Asztalmozgatás javaslat, nem automatikusan elfogadott','results':motions})
put('data/drawers.json',drawers);put('data/hardware_geometry.json',hardware);put('data/notches.json',notches);put('data/revision_mapping.json',mapping);put('data/new_connections.json',connections)
put('data/layout.json',{'width':3600,'height':2880,'tower':720,'bronze_band':200,'upper_panels_nominal':[670]*4,'lower_modules':list(zip(starts,widths)),'lower_fronts':'6 db egyetlen magas fiók, nincs vízszintes osztás','basis':'képi frontosztás értelmezése a korábbi3600/720mm tervkereten belül; méretarányos tervezési adaptáció, nem a raster méretbizonyítéka','owner_decision':'Minden alsó front egyetlen magas fiók; magas szekrény ajtós.'})
put('data/pending_hardware_operations.json',[{'drawer':d['id'],'operations':['760H3000S oldalfúrás a pontos rögzítési rajz szerint','T51.7601 zárókapocs sablonfuratai','hátsó Ø6 kampófurat / TIPON alákivágás','ZS7M400MU széles/rövid fiókstabilizátor szerelése','TIPON egység valódi üres/teli tömegre választása'],'status':'Nem kerül kitalált koordinátával az MPR-be'} for d in drawers])
# Preserve the actual workbook, before adding any new sheets.
shutil.copy2(BASE/'TV_R15_muhelyi_regiszter.xlsx',O/'sources/TV_R15_eredeti_munkafuzet.xlsx')
print(json.dumps({'parts':len(parts),'bores':len(holes),'drawers':len(drawers),'volume':checks['expected_net_volume_mm3'],'capacity_litres':sum(d['litres'] for d in drawers)}))
