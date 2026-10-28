from pathlib import Path
import json,shutil,hashlib,openpyxl,collections
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
parts=json.loads((O/'data/parts.json').read_text());holes=json.loads((O/'data/holes.json').read_text())
# Snapshot the actual current workbook, including formulas and manual values.
src=P/'R13_muhely/TV_R13_alkatreszek_furatok_cimkek.xlsx'
w=openpyxl.load_workbook(src,data_only=False)
snapshot={'source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'sheets':{s.title:[list(r) for r in s.iter_rows(values_only=True)] for s in w}}
(O/'audit/R13_excel_snapshot.json').write_text(json.dumps(snapshot,ensure_ascii=False,indent=2,default=str))
shutil.copy2(src,O/'sources/TV_R13_eredeti_munkafuzet.xlsx')
shutil.copy2(P/'R13_muhely/sources/Salice_S10_gyartoi_szereles.pdf',O/'sources/Salice_S10_gyartoi_szereles.pdf')
for name in ['programs','views','preview']:
 s=(P/f'scripts/r13_{name}.py').read_text().replace('R13','R14').replace('ki13','ki14')
 if name=='views':s=s.replace('54 LAP / 293 FURAT','75 LAP / 579 FURAT').replace('54 native','75 native')
 if name=='preview':
  s=s.replace("render('zart.png')", "render('zart.png')\ncam.location=(5,8,5);aim(cam,(1.65,.3,1.42));render('hatul.png')\ncam.location=(6,-10,6);aim(cam,(1.65,0,1.42))")
  s=s.replace("print('CAD_NATIVE_STL_RENDER_COMPLETE'", "for ob in objs:\n ob.hide_render=ob.name not in ['KI12-TV02S-01','KI14-BAT-03','KI12-TV02H1-01','KI14-RAIL-01'];ob.matrix_world=Matrix.Identity(4)\ncam.location=(.7,1.0,.8);aim(cam,(.10,.36,.44));cam.data.ortho_scale=.6\nrender('hatlap_reszlet.png')\nprint('CAD_NATIVE_STL_RENDER_COMPLETE'")
 if name=='preview':
  fix=""" bb=p['assembly_box_mm'];shift=[(-bb[k]+.000001)/1000 if bb[k]<0 else 0 for k in range(3)]
 vs=[tuple(v[k]-shift[k] for k in range(3)) for v in vs]
 assert all(abs(min(v[k] for v in vs)*1000-bb[k])<.001 and abs(max(v[k] for v in vs)*1000-bb[k]-bb[k+3])<.001 for k in range(3)),p['id']
"""
  s=s.replace(" me=bpy.data.meshes.new(p['id'])",fix+" me=bpy.data.meshes.new(p['id'])")
 (P/f'scripts/r14_{name}.py').write_text(s)
shutil.copy2('/tmp/TV_R14_zart.dwg',O/'rajzok/TV_R14_zart.dwg')
shutil.copy2('/tmp/ki14_build.log',O/'audit/autocad_build.log')
# Cost engineering allowance: explicit quantities, gross HUF, not web prices or a new project total.
bat_length=sum(p['x']/1000 for p in parts if p['type']=='BAT')
rail_area=sum(p['x']*p['y']/1e6 for p in parts if p['type']=='RAIL')
costs=[
 ['C14-01','Bükk 18x18 léc, nettó '+str(round(bat_length,3))+' m; +20% darabolás',round(bat_length*1.2,3),'m',700,1000,1400,'21 új alkatrészből 14 léc; tervezői bruttó egységár-becslés'],
 ['C14-02','18 mm rétegelt lemez merevítők; nettó '+str(round(rail_area,4))+' m²; +35% veszteség',round(rail_area*1.35,4),'m²',18000,24000,32000,'7 darab; kis tétel és beszerzési minimum miatt sávos becslés'],
 ['C14-03','4x30 csavar, 52 beépített +10% tartalék',58,'db',20,35,60,'Nincs konkrét gyártói SKU vagy árajánlat'],
 ['C14-04','3.5x20 csavar, 44 beépített +10% tartalék',49,'db',15,25,45,'Hátlap rögzítés, nem teherhordó falrögzítés'],
 ['C14-05','8x30 bükk csap, 42 beépített +10% tartalék',47,'db',15,25,40,'Merevítők; a korábbi 78 csap nincs újra árazva'],
 ['C14-06','Ragasztó, csiszoló és apróanyag növekmény',1,'csomag',3000,5000,8000,'Az új kötésekhez; indokolt szakági előirányzat'],
 ['C14-07','286 új furat gépi megmunkálása',286,'furat',60,100,160,'Gépidő-becslés, beállítás külön sor; csomagajánlat esetén kiváltandó'],
 ['C14-08','Programellenőrzés és egyszeri befogás-előkészítés',2,'óra',8000,11000,15000,'Műhelyi gép-adatbázis/elsődarab; óradíj bruttó tervezői becslés'],
 ['C14-09','Új lécek/merevítők gyártása és összeszerelése',4,'óra',8000,11000,15000,'Furatkészítés és CNC-beállítás nem ebben a 4 órában'],
 ]
(O/'data/cost_allowance.json').write_text(json.dumps(costs,ensure_ascii=False,indent=2))
print('R13 actual workbook preserved; R14 programs/views/previews prepared')
