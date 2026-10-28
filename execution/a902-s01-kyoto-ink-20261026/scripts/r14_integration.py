from pathlib import Path
import json,sqlite3,hashlib,csv
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
db=sqlite3.connect(O/'integration/alkatreszek_R14.sqlite');db.execute('CREATE TABLE IF NOT EXISTS file_hashes(path TEXT PRIMARY KEY,sha256 TEXT)');db.execute('DELETE FROM file_hashes')
for drawing,progs in db.execute('SELECT dxf,programs FROM parts').fetchall():
 for name in [drawing]+json.loads(progs):db.execute('INSERT OR REPLACE INTO file_hashes VALUES(?,?)',(name,hashlib.sha256((O/name).read_bytes()).hexdigest()))
db.commit();db.close()
code='''"""Offline lookup only; no CNC execution, no automatic stale-revision replacement."""
import sqlite3,json,sys,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('Használat: python cimke_kereso.py R14:KI12-TV01S-01')
db=sqlite3.connect('file:'+str(root/'integration/alkatreszek_R14.sqlite')+'?mode=ro',uri=True)
row=db.execute('SELECT * FROM parts WHERE barcode=?',(sys.argv[1],)).fetchone()
if not row:raise SystemExit('Ismeretlen vagy más revíziójú címke; nincs helyettesítés.')
files=[row[3]]+json.loads(row[4])
for name in files:
 target=(root/name).resolve()
 if not target.is_relative_to(root) or not target.is_file():raise SystemExit('Hiányzó/hibás fájl: '+name)
 expected=db.execute('SELECT sha256 FROM file_hashes WHERE path=?',(name,)).fetchone()
 if not expected or hashlib.sha256(target.read_bytes()).hexdigest()!=expected[0]:raise SystemExit('Hash eltérés: '+name+'; programot nem adunk át.')
print(json.dumps({'barcode':row[0],'part':row[1],'revision':row[2],'drawing':str(root/row[3]),'active_program_drafts':[str(root/f) for f in json.loads(row[4])],'hashes_verified':True,'release_state':row[5],'machine_send':False},ensure_ascii=False,indent=2))
'''
(O/'integration/cimke_kereso.py').write_text(code)
rows=[
 ['HW01','Blum','70T3550.TL','Rugó nélküli ráütődő pánt',16,'Gyári furatkép, tömeg/nyitáspróba nyitott'],
 ['HW02','Blum','173H7100','0mm pánttalp',16,'Gyári37/32 kiosztás; csavar pilot próba'],
 ['HW03','Blum','956A1004','Hosszú mágneses TIP-ON',2,'Frontonként1; működéspróba szükséges'],
 ['HW04','Blum','956A1201','Hosszú egyenes adapter',2,'20/32 furat; benne a CAD-ben'],
 ['HW05','Blum','956.1004','Rövid mágneses TIP-ON',3,'Alsó1,2,5; működéspróba szükséges'],
 ['HW06','Blum','956.1201','Rövid egyenes adapter',3,'20/17 furat; benne a CAD-ben'],
 ['HW07','Blum','A nyitók készletéhez','Öntapadó ellenlemez',5,'Helyszíni átjelölés; tapadáspróba'],
 ['HW08','Kiválasztandó','Spec:Ø5 csap,8mm beülés','Lapos felfekvésű polctartó',56,'Geometria és terhelés jóváhagyandó'],
 ['HW09','Kiválasztandó','8x30 bükk','Köldökcsap',120,'78 meglévő+42 új; ragasztott próbakötés'],
 ['HW10','Kiválasztandó','4x30 domború fej','Rögzítőléc/betét csavar',52,'Nem falhorgony; előfúrás próbálandó'],
 ['HW11','Kiválasztandó','3.5x20 domború fej','Hátlapcsavar',44,'Nem teherhordó falrögzítés'],
 ['HW12','Kiválasztandó','Pánthoz és talphoz illeszkedő','Pánt/pánttalp csavar',64,'A32+32 csavar konkrét fej/szár alakja gyári vasalathoz egyeztetendő'],
 ['HW13','Blum/kompatibilis','606N/606P gyári hivatkozás','TIP-ON adaptercsavar',10,'Konkrét csavar/lap páros szerint2.5x10 pilot próbálandó'],
 ]
with (O/'data/vasalatjegyzek.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['ID','Gyártó','SKU vagy tervezési specifikáció','Megnevezés','Nettó db','Státusz']);w.writerows(rows)
(O/'data/hardware.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
print('Hash-aware local lookup and full provisional hardware schedule created')
