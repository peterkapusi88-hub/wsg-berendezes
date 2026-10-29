from pathlib import Path
import json,sqlite3,hashlib,shutil
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok'
s=(P/'scripts/r14_programs.py').read_text().replace("O=P/'R14_muhely'","O=P/'R16_feluletek_fiokok'").replace('R14','R16').replace("r'H\\d{4}'","r'(?:R16)?H\\d{4}'")
exec(compile(s,__file__,'exec'))
parts=json.loads((O/'data/parts.json').read_text());programs=json.loads((O/'data/programs.json').read_text())
import ezdxf
notches=json.loads((O/'data/notches.json').read_text())
for p in parts:
 ns=[n for n in notches if n['part']==p['id']]
 if not ns:continue
 path=O/'dxf_alkatreszek'/(p['id']+'_R16.dxf');doc=ezdxf.readfile(path);doc.layers.new('SAW_NOTCH',dxfattribs={'color':6});m=doc.modelspace()
 for n in ns:
  b=n['box'];f=p['frame'];pts=[]
  for X,Z in [(b[0],b[2]),(b[0]+b[3],b[2]),(b[0]+b[3],b[2]+b[5]),(b[0],b[2]+b[5])]:
   q=[X-f['origin'][0],354-f['origin'][1],Z-f['origin'][2]];pts.append(tuple(sum(q[k]*f[v][k] for k in range(3)) for v in ['U','V']))
  m.add_lwpolyline(pts,close=True,dxfattribs={'layer':'SAW_NOTCH'})
 m.add_text('22x126 OPEN NOTCH / SAW / NOT IN MPR',dxfattribs={'height':8,'insert':(10,-140),'layer':'SAW_NOTCH'});doc.saveas(path)
db=sqlite3.connect(O/'integration/alkatreszek_R16.sqlite');db.execute('CREATE TABLE IF NOT EXISTS file_hashes(path TEXT PRIMARY KEY,sha256 TEXT)')
for dxf,progs in db.execute('SELECT dxf,programs FROM parts').fetchall():
 for name in [dxf]+json.loads(progs):db.execute('INSERT OR REPLACE INTO file_hashes VALUES(?,?)',(name,hashlib.sha256((O/name).read_bytes()).hexdigest()))
db.commit();db.close()
(O/'integration/cimke_kereso.py').write_text((P/'R15_muhely/integration/cimke_kereso.py').read_text().replace('R15','R16'))
(O/'integration/MPR_KORLATOK.txt').write_text('R16: csak a megadott szerkezeti furatok aktív tervezete. A MOVENTO gyári sablonfuratok, kapcsolók és stabilizátor megmunkálásai nincsenek kitalálva; a pending_hardware_operations.json listázza őket. A fiókok ezért e fájlokból önmagukban nem készre gyárthatók. RégiR15 ajtós program/címke nem használható az új alsó sorhoz. woodWOP5 megnyitás, gép/szerszám/befogás és elsődarab jóváhagyás szükséges. Nincs marópálya vagy CNC-végrehajtás.')
