"""Generate active drilling drafts plus a complete, separately identified M5 pilot."""
from pathlib import Path
import json,copy,shutil,hashlib,sqlite3
import ezdxf
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
parts=json.loads((O/'data/parts.json').read_text());holes=json.loads((O/'data/holes.json').read_text());notches=json.loads((O/'data/notches.json').read_text())
for p in parts:
 p['face']='A=U×V külső normál a rajzi rendszerben; a gépi felső/felfekvő oldal külön jóváhagyandó.'
 p['primary']='E1 V=0 / javasolt első referencia, nem igazolt gépi ütköző';p['secondary']='E4 U=0 / javasolt második referencia';p['edge_definition']='E1 V0; E2 Umax; E3 Vmax; E4 U0'
 p['ops']=['Névleges készméret és anyag',f'{p["hole_count"]} furat a külön furatjegyzék szerint','Élzárás és nyersméret műhelyszabály szerint']
 if any(n['part']==p['id'] for n in notches):p['ops']+=['Két nyitott sarokkivágás: 22x126mm, két egyenes fűrészvágással. Az MPR csak fúrás.']
(O/'data/parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2))
r15_main_code=(P/'scripts/r14_programs.py').read_text().replace('R14','R15')
exec(compile(r15_main_code,__file__+':main','exec'))
# Add actual back outline notches and mark the drilling-only MPR scope prominently.
by={p['id']:p for p in parts}
for pid in {n['part'] for n in notches}:
 p=by[pid];doc=ezdxf.readfile(O/'dxf_alkatreszek'/(pid+'_R15.dxf'));m=doc.modelspace();doc.layers.new('SAW_CUT',dxfattribs={'color':6})
 for n in [n for n in notches if n['part']==pid]:
  b=n['box'];f=p['frame'];points=[]
  for X,Z in [(b[0],b[2]),(b[0]+b[3],b[2]),(b[0]+b[3],b[2]+b[5]),(b[0],b[2]+b[5])]:
   q=[X-f['origin'][0],362-f['origin'][1],Z-f['origin'][2]];points.append(tuple(sum(q[k]*f[uv][k] for k in range(3)) for uv in ['U','V']))
  m.add_lwpolyline(points,close=True,dxfattribs={'layer':'SAW_CUT'})
  m.add_text('22x126 OPEN NOTCH / SAW CUT / NOT IN MPR',dxfattribs={'height':8,'insert':(20,-150),'layer':'SAW_CUT'})
 doc.saveas(O/'dxf_alkatreszek'/(pid+'_R15.dxf'))
pil=O/'pilot';(pil/'data').mkdir(exist_ok=True);(pil/'integration').mkdir(exist_ok=True);(pil/'audit').mkdir(exist_ok=True)
ps=[copy.deepcopy(p) for p in parts if p['assembly_box_mm'][0]>=2910 and p['assembly_box_mm'][2]<550 and p['type']!='TV03-P']
# Pilot-only top is a crop of the final full-width top; main part remains 3600mm.
cap=copy.deepcopy(next(p for p in parts if p['type']=='TV02-CAP'));original_cap=cap['id'];cap.update(id='KI15-PILOT-CAP-M5',name='M5 próbafedlap / csak próbához, nem beépülő darab',x=690,assembly_box_mm=[2910,0,532,690,382,18],frame={'origin':[2910,0,550],'U':[1,0,0],'V':[0,1,0],'outward_A':[0,0,1],'meaning':'próbafedlap rajzi rendszer'},note='A3600mm végleges fedlap2910..3600szakaszának külön próbája. Nem számítandó még egyszer a beépülő alkatrészekhez.');ps.append(cap)
ph=[copy.deepcopy(h) for h in holes if h['part'] in {p['id'] for p in ps}]
for h in holes:
 if h['part']==original_cap and h['xyz'][0]>=2910:
  hh=copy.deepcopy(h);hh['part']=cap['id'];hh['local_UVW'][0]-=2910;ph.append(hh)
cap['hole_count']=sum(h['part']==cap['id'] for h in ph)
(pil/'data/parts.json').write_text(json.dumps(ps,ensure_ascii=False,indent=2));(pil/'data/holes.json').write_text(json.dumps(ph,ensure_ascii=False,indent=2))
pilot_src=r15_main_code.replace("O=P/'R15_muhely'","O=P/'R15_muhely/pilot'")
exec(compile(pilot_src,__file__+':pilot','exec'))
# Copy improved notch drawing over generic pilot back view.
for p in ps:
 if any(n['part']==p['id'] for n in notches):shutil.copy2(P/'R15_muhely/dxf_alkatreszek'/(p['id']+'_R15.dxf'),pil/'dxf_alkatreszek'/(p['id']+'_R15.dxf'))
O=P/'R15_muhely'
manifest={'id':'M5-PILOT-R15','parts':[p['id'] for p in ps],'part_count':len(ps),'bore_count':len(ph),'notch_manual_operations':2,'extra_top':cap['id'],'main_cap_retained':original_cap,'method':'Fúrások aktív MPR-tervezetben; hátlap két nyitott sarok kivágása külön fűrészes művelet. Nem teljesen gépesített kontúrprogram.','hardware':[{'sku':'70T3550.TL','qty':2},{'sku':'173H7100','qty':2},{'sku':'956.1004','qty':1},{'sku':'956.1201','qty':1},{'sku':'80702Z1INSX','qty':1},{'sku':'80702Z1INDX','qty':1},{'sku':'897ASZ11212','qty':2},{'sku':'8x30 bükk csap','qty':21},{'sku':'Ø5 polctartó 8mm beülés','qty':4},{'sku':'4x30 léc-csavar','qty':6},{'sku':'3.5x20 hátlapcsavar','qty':6},{'sku':'609.1500 pánt/pánttalp csavar','qty':8},{'sku':'606N/606P adaptercsavar','qty':2}], 'test_sequence':['Műhelyprofil,szerszám/befogás és anyag ellenőrzés.','MPR megnyitása woodWOP5-ben:méret,oldal,makró,mélység;szimuláció.','Elsőoldal,front és hátlap próbadarab:furatok külön lemérése.','Korpusz szárazpróba,átlók,hézag,polc,pánt,TIPON.','Camarfüggesztő próbaszerelés külön tesztfalon;jóváhagyott terhelési próba.','Mért értékek rögzítése;jóváhagyás után sorozat.'],'release':'NOT_MANUFACTURED_NOT_SHOP_VALIDATED'}
(pil/'pilot_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
# Main and pilot SQLite lookup resolves hashes and explicitly refuses stale revisions.
for base in [O,pil]:
 db=sqlite3.connect(base/'integration/alkatreszek_R15.sqlite');db.execute('CREATE TABLE IF NOT EXISTS file_hashes(path TEXT PRIMARY KEY,sha256 TEXT)');db.execute('DELETE FROM file_hashes')
 for dxf,progs in db.execute('SELECT dxf,programs FROM parts').fetchall():
  for name in [dxf]+json.loads(progs):db.execute('INSERT OR REPLACE INTO file_hashes VALUES(?,?)',(name,hashlib.sha256((base/name).read_bytes()).hexdigest()))
 db.commit();db.close()
 code=(P/'R14_muhely/integration/cimke_kereso.py').read_text().replace('R14','R15')
 (base/'integration/cimke_kereso.py').write_text(code)
print('Main and pilot generated:',len(ps),'pilot parts',len(ph),'pilot bores')
