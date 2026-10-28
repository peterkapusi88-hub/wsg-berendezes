"""Actual coordinate-derived sections; separate service proposal, not fabricated site data."""
from pathlib import Path
import json,math
import ezdxf
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
parts=json.loads((O/'data/parts.json').read_text());holes=json.loads((O/'data/holes.json').read_text())
sections=[]
for name,z in [('D01_OLDALLEC',210),('D02_HATLAP',225),('D03_MEREVITO',452)]:
 xmin,xmax,ymin,ymax=0,90,320,400;rects=[];cuts=[]
 for p in parts:
  x,y,zz,w,d,h=p['assembly_box_mm']
  if not zz<z<zz+h:continue
  a,b,c,e=max(x,xmin),max(y,ymin),min(x+w,xmax),min(y+d,ymax)
  if c>a and e>b:rects.append(dict(part=p['id'],box=[a,b,c-a,e-b],material=p['material']))
 for h in holes:
  if h['axis'][2]:continue
  dz=abs(h['xyz'][2]-z);rad=h['diameter']/2
  if dz>=rad:continue
  chord=2*math.sqrt(rad*rad-dz*dz);x,y,_=h['xyz'];ax=h['axis'];ex=x+ax[0]*h['depth'];ey=y+ax[1]*h['depth']
  box=[min(x,ex),y-chord/2,abs(ex-x),chord] if ax[0] else [x-chord/2,min(y,ey),chord,abs(ey-y)]
  if box[0]>=xmin and box[1]>=ymin and box[0]+box[2]<=xmax and box[1]+box[3]<=ymax:cuts.append(dict(id=h['id'],part=h['part'],box=box,kind=h['kind']))
 sec=dict(id=name,z=z,rectangles=rects,bores=cuts,range=[xmin,xmax,ymin,ymax]);sections.append(sec)
 doc=ezdxf.new('R2010');doc.units=4;m=doc.modelspace();doc.layers.new('PARTS',dxfattribs={'color':7});doc.layers.new('BORES',dxfattribs={'color':1})
 for group,layer in [(rects,'PARTS'),(cuts,'BORES')]:
  for r in group:
   x,y,w,h=r['box'];m.add_lwpolyline([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],close=True,dxfattribs={'layer':layer})
 m.add_text(name+f' / XY Z={z} / mm / R14 DESIGN',dxfattribs={'height':3,'insert':(0,415)})
 for axis,a,b,base,ang in [('X',(0,320),(90,320),(0,310),0),('Y',(0,320),(0,400),(-10,0),90)]:
  di=m.add_linear_dim(base=base,p1=a,p2=b,angle=ang,dimstyle='EZDXF',override={'dimtxt':2.5,'dimasz':1.5});di.render()
 doc.saveas(O/'rajzok'/f'{name}_R14.dxf')
(O/'data/sections.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
service={
 'status':'DIMENSIONED_PROPOSAL_NOT_ELECTRICAL_RELEASE',
 'datum':'Same assembly XYZ as parts. Z0 is design floor level, not newly surveyed.',
 'circuits':[
 {'id':'L01','name':'Alsó lebegő fény','length_mm':3600,'power_W_per_m':9.6,'profile':'KLUS PDS-4-ALU B1718 family,16x12mm; cover/endcap variant pending','polyline_mm':[[0,35,138],[3600,35,138]],'condition':'Felületre szerelt profil a fenék alatt;120mm köztes sáv felett áthidaló tartás és bontható csatlakozás. Nem marás a lapba.'},
 {'id':'L02','name':'Felső TV-panel fény','length_mm':2760,'power_W_per_m':9.6,'profile':'Same family','polyline_mm':[[840,406,2860],[3600,406,2860]],'condition':'Panel mögötti profilcsatorna. Fénykilépési rés, plafon és paneltartás metszeti próbadarabbal igazolandó; helyfoglalás, nem kiadott furat.'},
 {'id':'L03','name':'Függőleges köztes fény','length_mm':2330,'power_W_per_m':9.6,'profile':'Same family','polyline_mm':[[736,394,550],[736,394,2880]],'condition':'A120mm köztes sáv bal oldalán; grafit betét előtt. Végleges fényirány és árnyékolás1:1mintán zárandó.'}],
 'strip_spec':'24V DC,2700K,CRI>=90,egyszínű,legfeljebb10mm széles,9.6W/m tervezési érték. Pontos megvásárolható cikkszám és vágásosztás még nincs kiválasztva.',
 'driver_candidate':{'model':'MEAN WELL LPV-150-24','size_mm':[191,63,37.5],'rated_W':151.2,'source':'https://www.meanwell.com/Upload/PDF/LPV-150/LPV%2CLPVL-150-SPEC.pdf','status':'Manufacturer dimension checked; electrical/thermal approval pending'},
 'access_box_mm':[890,60,185,430,240,150],
 'access_condition':'Második alsó rekesz, polc nélküli AV-tér. Ajtó felől hozzáférhető, kivehető szerelőtálca. Ez helyfoglalás; szellőzőfelület/hőmérséklet ellenőrzése nélkül nem lezárt doboz.',
 'chain':'Meglévő kiállás helyszíni azonosítása -> elkülönített230V betáp -> kivehető tápegység/vezérlőtálca -> külön biztosított24V ágak -> profilok; szerelvényekhez front felől hozzáférés.',
 'control':'3 külön dimmelhető ág tervezett. Hue-integrációhoz konkrét vezérlő és próbakapcsolás hiányzik; a jelölt tápegység önmagában nem Hue-eszköz.',
 'sources':['https://www.led-obchod.sk/fotky13065/produktov_karta_pds-4-alu.pdf','https://www.meanwell.com/Upload/PDF/LPV-150/LPV%2CLPVL-150-SPEC.pdf']}
for x in service['circuits']:x['design_power_W']=x['length_mm']/1000*x['power_W_per_m'];x['design_current_A']=x['design_power_W']/24
service['design_total_W']=sum(x['design_power_W'] for x in service['circuits']);service['driver_load_fraction']=service['design_total_W']/151.2
(O/'data/lighting_service.json').write_text(json.dumps(service,ensure_ascii=False,indent=2))
doc=ezdxf.new('R2010');doc.units=4;m=doc.modelspace()
for name,color in [('CABINET',8),('LED_PROPOSAL',2),('SERVICE',3),('TEXT',7)]:doc.layers.new(name,dxfattribs={'color':color})
for p in parts:
 x,y,z,w,d,h=p['assembly_box_mm']
 m.add_lwpolyline([(x,z),(x+w,z),(x+w,z+h),(x,z+h)],close=True,dxfattribs={'layer':'CABINET'})
for q in service['circuits']:
 m.add_lwpolyline([(p[0],p[2]) for p in q['polyline_mm']],dxfattribs={'layer':'LED_PROPOSAL'});x,y,z=q['polyline_mm'][0];m.add_text(q['id'],dxfattribs={'height':35,'insert':(x+30,z+35),'layer':'TEXT'})
x,y,z,w,d,h=service['access_box_mm'];m.add_lwpolyline([(x,z),(x+w,z),(x+w,z+h),(x,z+h)],close=True,dxfattribs={'layer':'SERVICE'});m.add_text('SERVICE TRAY / DESIGN ONLY',dxfattribs={'height':28,'insert':(850,-150),'layer':'TEXT'})
m.add_text('R14 / 24V LIGHTING AND SERVICE RESERVATION / NOT ELECTRICAL RELEASE',dxfattribs={'height':45,'insert':(0,3050),'layer':'TEXT'})
doc.saveas(O/'rajzok/TV_R14_LED_szerviz_javaslat.dxf')
print('3 true XY sections + lighting/service DXF; total design load',service['design_total_W'])
