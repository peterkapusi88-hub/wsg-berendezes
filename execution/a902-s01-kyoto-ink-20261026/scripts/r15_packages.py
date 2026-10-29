from pathlib import Path
import json,math,copy,csv,shutil,hashlib
import ezdxf
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
def read(n):return json.loads((O/n).read_text())
def put(n,v):(O/n).write_text(json.dumps(v,ensure_ascii=False,indent=2))
parts=read('data/parts.json');holes=read('data/holes.json');by={p['id']:p for p in parts}
# Exact selected lighting; profile length and active LED length are distinct.
circuits=[]
for id,name,profile,led,cable,path in [
 ('L01','Alsó fény',3600,3550,3,[[0,35,138],[3600,35,138]]),
 ('L02','Felső fény',2760,2750,5,[[840,406,2860],[3600,406,2860]]),
 ('L03','Függőleges fény',2330,2300,4,[[736,394,550],[736,394,2880]])]:
 power=led/1000*8;current=power/24;drop=2*.0225*cable*current/.75
 circuits.append(dict(id=id,name=name,profile_mm=profile,LED_mm=led,unlit_end_total_mm=profile-led,cut_pitch_mm=50,W=power,A=current,cable_m_oneway=cable,cable_mm2=.75,voltage_drop_V=drop,voltage_drop_pct=drop/24*100,fuse_design_A=2,path=path,controller='DIM-'+str(len(circuits)+1),cable_condition='2x0.75mm² Cu tervezési választás; vezetési mód, hő és védelem villanyszerelővel ellenőrzendő. 0.0225Ωmm²/m meleg réz számítási feltételezés.'))
lighting={'status':'SPECIFIED_DESIGN_NOT_ELECTRICAL_APPROVAL','strip':{'brand':'LED line PRIME','sku':'476821','description':'320COB24V2700K8WIP20,8x2mm,Ra90,5cmvágás','purchase_m':10,'reels':2,'cutting':'A tekercs:3600mm+1400mm maradék. B tekercs:2750mm+2250mm;L03=2250+50mm az A maradékból,forrasztott vezetékes híd. 1350mm maradék/minta. Egy szalagág sem hosszabb5m-nél.','source':'https://ledline.pl/produkty/tasmy-led/tasmy-led-cob/tasma-led-320-cob-24v-2700k-8w-ip20-8mm-5m-800lmm-prime/'},'profile':{'sku':'KLUS B1718K7_3','description':'PDS-4-ALU fekete eloxált,3000mm;4szál','cross_section_mm':[16,12],'clear_width_mm':11.2,'cut_list_mm':[3000,600,2760,2330],'stock_assignment':'1.szál3000;2.szál2760;3.szál2330;4.szál600. Nettó8690mm,maradék3310mm mínusz fűrészrés. A3000+600toldás csakL01-ben.','cover':'LIGER17037 szatén kompatibilis fedél,12m;legacy cikkszám, rendeléskor az aktuális egyenérték megerősítendő','endcap':'24066 zárt és24081 kivezetett fekete PDS-4-ALU végzáró,4+4db','bracket':'PDS24189,22db;tervezett legfeljebb450mm kiosztás, tényleges végpontok rajzon','source':'https://www.kitokogroup.com/wp-content/uploads/catalogs/KLUS%20CATALOG.pdf'},'driver':{'sku':'MEAN WELL LPV-150-24','W':151.2,'source':'https://www.meanwell.com/Upload/PDF/LPV-150/LPV%2CLPVL-150-SPEC.pdf'},'dimmers':{'sku':'SR-ZG9101FA-DIM','quantity':3,'mode':'12–36V DC constant voltage,5A/channel;mindegyik egység csakCH1-et használja,egy önálló fényág. Nem0–10V változat!','source':'https://www.lemona.lt/Files/Instrukcijos/Pdf/SR-ZG9101FA-DIM%20instruction%20V1.pdf','Hue':'Gyártói útmutató Hue Bridge párosítást említ; helyi firmware/párosítás/jelenet még nincs kipróbálva. A meglevő Bridge-et használni, újat csak hiány esetén számolni.'},'circuits':circuits,'total_W':sum(x['W'] for x in circuits),'total_A':sum(x['A'] for x in circuits),'driver_load_pct':sum(x['W'] for x in circuits)/151.2*100,'service':'AV2,430x240mm elölről kivehető tálca. Baloldali230V kivezetés/érintésvédelem elkülönítve; jobb oldalt3vezérlő. Nem zárt hőszigetelt doboz. Hátlapon alul/felül48dbØ10=37.70cm²/bank; a fali üreg szabad levegőkapcsolata külön helyszíni ellenőrzés. AV-gépet nem tenni közvetlenül a tápegységre.','commissioning':['Villanyszerelő ellenőrzi a meglévő kiállást, kapcsolást, védelmet és érintésvédelmet.','24V áganként2A DC biztosító tervezve; 230V ésSELV vezetékek fizikailag elkülönítve, kötés csak hozzáférhető dobozban.','Maxfényen2órás hőmérés a lezárt végleges fronttal; határérték az összes tényleges komponens adatlapjának legszigorúbb értéke.','Huesötétítés1/10/50/100%, villogás, visszakapcsolás,Bridgekiesés és kézi kapcsolás próbája.','1:1fényminta2700K; panel relief/nyomat árnyéka és felső fénykilépés ellenőrzése.'],'scenes':[{'name':'Este','L01':25,'L02':35,'L03':20},{'name':'Film','L01':8,'L02':10,'L03':5},{'name':'Takarítás','L01':100,'L02':100,'L03':100}]}
put('data/lighting.json',lighting)
# Manufacturability fields and exact locator semantics. No invented shop stop/tool IDs.
profile={'revision':'R15','machine_reported':'WOF211 homag','woodWOP_reported':'5.0','machine_verified':False,'C_edge_code_mapping':None,'primary_stop':None,'secondary_stop':None,'face_A_orientation':None,'tool_map':{},'min_clampable_width_mm':None,'feed_spindle_table':None,'shop_approved_by':None,'convention':'E1 V=0; E2 U=Umax; E3 V=Vmax; E4 U=0. A outward=U×V; B flip aboutU. A/B drawing orientation is not machine placement.'}
put('integration/shop_profile.json',profile)
put('data/tool_requirements.json',[{'operation':op,'nominal_diameter_mm':dia,'depths_mm':sorted({h['depth'] for h in holes if h['diameter']==dia and (abs(h['local_axis'][2])>.5)==(op=='V_FURO') }),'tool_id':None,'direction':'vertical' if op=='V_FURO' else 'edge','status':'Tényleges szerszámtárra és anyagra leképezendő; nincs kitalált fordulat/előtolás'} for op in ['V_FURO','H_FURO'] for dia in sorted({h['diameter'] for h in holes if (abs(h['local_axis'][2])>.5)==(op=='V_FURO')})])
# Complete comparison of real room obstacles and two developed alternatives.
obs=json.loads((P/'R12_muhely/audit/room_obstacle_bounds.json').read_text());obstacles=[]
for ob in obs:
 mn,mx=ob['min'],ob['max'];obstacles.append({'id':ob['name'],'box':[(mn[1]-4.35)*1000,(4.092-mx[0])*1000,mn[2]*1000,(mx[1]-mn[1])*1000,(mx[0]-mn[0])*1000,(mx[2]-mn[2])*1000]})
def intersects(poly,b):
 corners=[(b[0],b[1]),(b[0]+b[3],b[1]),(b[0]+b[3],b[1]+b[4]),(b[0],b[1]+b[4])]
 for ax in [(1,0),(0,1)]+[(poly[(i+1)%4][1]-poly[i][1],poly[i][0]-poly[(i+1)%4][0]) for i in range(4)]:
  aa=[x*ax[0]+y*ax[1] for x,y in poly];bb=[x*ax[0]+y*ax[1] for x,y in corners]
  if max(aa)<min(bb) or max(bb)<min(aa):return False
 return True
fronts=[p for p in parts if p['type'] in ['TV02-F1','TV02-F2']]
coffee=next(o for o in obstacles if 'CF-01' in o['id']);newcoffee=[1900,-1088,0,700,350,350]
results=[]
for alt in ['ORIGINAL','A_ASZTAL_700x350']:
 objects=copy.deepcopy(obstacles)
 for ob in objects:
  if ob['id']==coffee['id'] and alt!='ORIGINAL':ob['box']=newcoffee
 for i in [2,3]:
  x,y,z,ww,dd,hh=fronts[i]['assembly_box_mm'];pivot=[x,-12];contacts=[]
  for ob in objects:
   b=ob['box']
   if min(z+hh,b[2]+b[5])<=max(z,b[2]):continue
   for step in range(1101):
    rad=math.radians(step/10);u=(math.cos(rad),-math.sin(rad));n=(math.sin(rad),math.cos(rad));poly=[(pivot[0]+a*ww*u[0]+bb*9*n[0],pivot[1]+a*ww*u[1]+bb*9*n[1]) for a,bb in [(0,-1),(1,-1),(1,1),(0,1)]]
    if intersects(poly,b):contacts.append({'obstacle':ob['id'],'first_deg':step/10});break
  results.append({'alternative':alt,'front':i+1,'contacts':contacts})
def boxhit(a,b):return all(min(a[i]+a[i+3],b[i]+b[i+3])-max(a[i],b[i])>0.001 for i in range(3))
tablehits=[o['id'] for o in obstacles if o['id']!=coffee['id'] and boxhit(newcoffee,o['box'])]
removable=[]
for i in [2,3]:
 b=fronts[i]['assembly_box_mm'];contacts=[]
 for dy,dz in [(k,0) for k in range(31)]+[(30,k) for k in range(221)]:
  a=[b[0],b[1]-dy,b[2]+dz,*b[3:]]
  for o in obstacles:
   if boxhit(a,o['box']):contacts.append({'obstacle':o['id'],'pull':dy,'lift':dz})
 removable.append({'front':i+1,'pull_mm':30,'lift_mm':220,'contacts':contacts,'clearance_above_coffee_mm':b[2]+220-350})
alts={'source':'R10 extracted obstacle AABBs, same asR12; not a fresh room survey','method':'0.1degree rigid18mm panel0..110deg; approximate hinge pivot. Clearance envelope includes no operator/hardware exact motion. Removable trajectory1mm sampled.','main_selection':None,'coffee_original':coffee,'coffee_A':newcoffee,'results':results,'table_A_other_object_contacts':tablehits,'A_nominal_min_sweep_to_table_mm':738-12-math.sqrt(687**2+9**2),'A_nominal_coffee_to_chaise_mm':300,'removable_B':removable,'alternatives':[{'id':'A','description':'Két eredeti687x397front,2-2baloldali110fokosBlumpánt +1-1rövidTIPON;dohányzóasztal700x350x350, hosszában a TV-fallal párhuzamosan.','cost_delta_low_HUF':15000,'cost_delta_HUF':35000,'cost_delta_high_HUF':75000,'compromise':'Az asztallap700x450helyett700x350:22.2%kisebbfelület,elforgatott/eltoltelhelyezés;300mmnévlegeskanapérés.','release':'Tulajdonosi döntés és pontos pántpróba szükséges.'},{'id':'B','description':'Eredeti asztal marad;3-4front leemelhető szervizpanel,4párHäfeleKEKUAS/front (262.50.359panel+262.50.368keret),belső rögzítőlécekhez.30mmkihúzás,220mmemelés.','cost_delta_low_HUF':22000,'cost_delta_HUF':45000,'cost_delta_high_HUF':80000,'compromise':'Nem kényelmes napi tároló.3.44kgfront kézzel kiemelendő;alsó megfogás/cliperő próbája szükséges. Használatkor dísztárgyak helyét szabaddá kell tenni.','release':'Tulajdonosi funkciójóváhagyás és1:1klipsz/működéspróba szükséges.'},{'id':'C','description':'SaliceS10coplanar:korábbiR14méretezettalternatíva továbbra is összehasonlításra.','cost_delta_low_HUF':120000,'cost_delta_HUF':180000,'cost_delta_high_HUF':260000,'compromise':'Közös korpusz,raisedfloor,két686.5mmfront,4mmközéprés,középfogantyúk;gyári mozgásburkolat még nem digitálisan igazolt.','release':'Nem választott; nincs igazolt teljes mozgásmodell.'}]}
assert not tablehits
assert all(not r['contacts'] for r in results if r['alternative']!='ORIGINAL')
assert all(not r['contacts'] for r in removable)
put('data/door_alternatives.json',alts);put('data/room_obstacles.json',obstacles)
# DXF plan with actual dimensions and sampled opening paths, separate variants.
for name,table in [('ORIGINAL',coffee['box']),('A_700x350',newcoffee),('B_leemelheto',coffee['box'])]:
 d=ezdxf.new('R2010');d.units=4;m=d.modelspace()
 for l,col in [('FURNITURE',7),('TABLE',3),('SWEEP',1),('SOFA',8),('DIM',2)]:d.layers.new(l,dxfattribs={'color':col})
 def rect(b,layer):m.add_lwpolyline([(b[0],b[1]),(b[0]+b[3],b[1]),(b[0]+b[3],b[1]+b[4]),(b[0],b[1]+b[4])],close=True,dxfattribs={'layer':layer})
 rect([0,0,0,3600,382,550],'FURNITURE');rect(table,'TABLE')
 for ob in obstacles:
  if 'SO' in ob['id']:rect(ob['box'],'SOFA')
 for i in [2,3]:
  b=fronts[i]['assembly_box_mm'];rect(b,'FURNITURE')
  if not name.startswith('B'):
   m.add_lwpolyline([(b[0]+b[3]*math.cos(math.radians(a)),-12-b[3]*math.sin(math.radians(a))) for a in range(111)],dxfattribs={'layer':'SWEEP'})
  else:rect([b[0],b[1]-30,b[2]+220,*b[3:]],'SWEEP')
 for a,b,base,angle in [((table[0],table[1]),(table[0]+table[3],table[1]),(table[0],table[1]-100),0),((table[0]+table[3],table[1]),(table[0]+table[3],table[1]+table[4]),(table[0]+table[3]+150,table[1]),90)]:m.add_linear_dim(base=base,p1=a,p2=b,angle=angle,dimstyle='EZDXF',override={'dimtxt':25,'dimasz':20}).render()
 m.add_text('R15 / '+name+' / mm / OWNER SELECTION PENDING',dxfattribs={'height':40,'insert':(0,650)})
 d.saveas(O/'rajzok'/('NYITAS_'+name+'.dxf'))
# Door A hinge and opener hole schedule, held separately until choice.
variant_holes=[]
for i in [2,3]:
 f=fronts[i];x,y,z,ww,dd,hh=f['assembly_box_mm'];side=[p for p in parts if p['type']=='TV02-S'][2*i];right=[p for p in parts if p['type']=='TV02-S'][2*i+1]
 for dz in [80,317]:
  zz=z+dz
  variant_holes.append({'part':f['id'],'xyz':[x+23,-3,zz],'axis':[0,-1,0],'diameter':35,'depth':13,'function':'70T3550.TL cup'})
  for off in [-22.5,22.5]:variant_holes.append({'part':f['id'],'xyz':[x+13.5,-3,zz+off],'axis':[0,-1,0],'diameter':2.5,'depth':10,'function':'hinge screw pilot'})
  for off in [-16,16]:variant_holes.append({'part':side['id'],'xyz':[starts if False else side['assembly_box_mm'][0]+18,37,zz+off],'axis':[-1,0,0],'diameter':2.5,'depth':10,'function':'173H7100 plate pilot'})
 for yy in [20,37]:variant_holes.append({'part':right['id'],'xyz':[right['assembly_box_mm'][0],yy,450],'axis':[1,0,0],'diameter':2.5,'depth':10,'function':'956.1201 adapter pilot'})
put('data/alternative_A_holes_NOT_MAIN.json',variant_holes)
# Fabricated bracket/anchor requirements are separated from purchasable hardware.
loads=[]
for module,x0,x1,z0,z1,payload in [('T',0,720,550,2880,60),('1',0,720,150,550,20),('2',840,1530,150,550,15),('3',1530,2220,150,550,20),('4',2220,2910,150,550,20),('5',2910,3600,150,550,20)]:
 mass=0;ids=[]
 for p in parts:
  x,y,z,ww,dd,hh=p['assembly_box_mm']
  if x>=x0-.01 and x+ww<=x1+.01 and z>=z0-.01 and z+hh<=z1+.01 and p['type'] not in ['TV03-P','GAP','GAP-LOW']:
   mass+=ww*dd*hh/1e9*700;ids.append(p['id'])
 if module!='T':mass+=(x1-x0)*382*18/1e9*700 # share of common cap
 gross=mass+payload+5;loads.append({'module':module,'parts':ids,'blank_mass_kg_at700':mass,'planned_contents_kg':payload,'hardware_allowance_kg':5,'service_mass_kg':gross,'pair_vertical_service_N':gross*9.81,'single_hanger_vertical_equal_share_N':gross*9.81/2,'overturning_moment_Nm_e0_20':gross*9.81*.20,'condition':'Tervezési teher, nem engedélyezett terhelhetőség. A falhorgony húzás/nyírás, csoporthatás, távtartás és lapoldali vasalat ellenőrzése szükséges. Camar alkalmazási jóváhagyás magas toronyra külön.'})
put('data/load_demands.json',loads)
# Complete itemised allowances. Estimate status is explicit, no fake current web prices.
cost=[
 ['H01','Camar807IN bal+jobb+2x897lemez+fedelek',6,'készlet',9000,15000,24000,'Új függesztési rendszer;gyártóiSKU,árbecslés'],
 ['H02','MonarchMF37550.8mmklipsz',48,'db',700,1100,1700,'Paneloldali48klipsz;faloldali sínkülön'],
 ['H03','MonarchMF375 sín,4x2760 nettó,5x2500 rendelési',12.5,'m',3000,4800,7000,'Vágásveszteséggel;konkrét szállítói ajánlat kell'],
 ['H04','Síkbeállító tartók,távtartók és méretezett falhorgonyok',1,'csomag',30000,50000,85000,'12függesztőlemez+4panelrails+TV;faltípusfüggő,összevonhatómeglévősorral'],
 ['H05','VogelTVM3605SKU3836050',1,'db',24000,32000,45000,'A meglévő TVkonzol előirányzatot kiváltja,nem duplán'],
 ['H06','Blum609.1500 pántcsavar + szerkezeti csavarok/csapok/polctartók',1,'csomag',13000,20000,30000,'MeglévőR14kötőelemeket is lefedi;nem növekményként összegezni'],
 ['L01','LEDline476821COB2700K8W24V',10,'m',1600,2300,3200,'2x5m;8.65mbeépül,1.35mmaradék'],
 ['L02','KLUSB1718K7_3profil+LIGERfedél',12,'m',3500,5000,7500,'4x3m;nettó8.69m'],
 ['L03','KLUSvégzáró8db+rögzítő22db',1,'készlet',5000,9000,14000,'24066/24081+24189;aktuális cikkszámhelyettesítésellenőrzendő'],
 ['L04','MEANWELLLPV-150-24',1,'db',12000,17000,23000,'151.2W,24V'],
 ['L05','SunricherSR-ZG9101FA-DIM CV',3,'db',16000,23000,31000,'3különfényzóna;nemAC0–10Vváltozat'],
 ['L06','Tálca,válaszfal,kábel,biztosító,kötődoboz,átvezető',1,'csomag',18000,28000,42000,'12mnyomvonal+30%rendelés,3DCágvédelem,230Vkülön'],
 ['L07','Villamos szerelés,konfigurálás,hő/párosításpróba',6,'óra',9000,12500,16000,'Helyszíniárbecslés,nemvisszaigazoltajánlat'],
 ['M01','Új megmunkálás és kötésellenőrzés',1,'csomag',35000,55000,90000,'247újfurat+12nyitottsarok,megváltozottkötések;R14gépidővelegyeztetni'],
 ['M02','Felszerelés/síkbeállítás/elsődarab',12,'óra',9000,12000,16000,'Asztalosmunkadíj;meglévőszereléscsomaggalösszevezetendő'],
 ['M03','Szállítás és kis mennyiségi felár',1,'csomag',10000,18000,30000,'Magyarszállításnemvisszaigazolt'],
]
put('data/cost_allowance.json',cost)
with (O/'data/kivalasztott_rendszer.csv').open('w',encoding='utf-8-sig',newline='') as f:
 wr=csv.writer(f,delimiter=';');wr.writerow(['ID','Tartalom','Mennyiség','Egység','AlsóFt','VárhatóFt','FelsőFt','Bázis']);wr.writerows(cost)
put('data/six_workpackages.json',[
 {'id':1,'output':'75lapos új megmunkált összeállítás;12Camarfüggesztő,48panelklipsz,TVkonzol+teherút és terhelési számítás.','open':'Fal,távtartó és toronyra alkalmazás gyártói/szakági jóváhagyása.'},
 {'id':2,'output':'A:700x350asztallal nyílófront;B:eredeti asztallal leemelhetőfront. Számított nyitási képek és különDXF.','open':'Tulajdonosi változatválasztás;valódi vasalatkinematika/használópróba.'},
 {'id':3,'output':'Számozott szerelési rajzok,metszetek,hardwaremodell,egyedi alkatrészlapok és szerelési sorrend.','open':'Felmérés,anyagvastagság és minták.'},
 {'id':4,'output':'Pontos szalag/táp/3vezérlő,profilvágás,nyomvonal,37.7cm²szellőzőbankok,kivehető tálca és költség.','open':'230Vkiállás,érintésvédelem,hőmérés,Huepárosítás.'},
 {'id':5,'output':'Revíziós Excel/címke,nyers/kész méretképlet,A/B/E1-E4tájoló,CSV/SQLite/hashkereső és kitölthetőműhelyprofil.','open':'Ckód,ütköző,befogó,szerszámtár és tényleges műhelyadatbázis adaptere.'},
 {'id':6,'output':'5.alsó modul10darabos próbacsomag,egyedi próbafedlappal,programok/címkék/mérőlap és elfogadási jegyzőkönyv.','open':'woodWOP5megnyitás,gépi szimuláció és fizikai elsődarab;nem futtatva.'}])
print('Lighting',lighting['total_W'],'W; alternatives A/B geometry screening clear; selected-package estimate',sum(r[2]*r[5] for r in cost))
