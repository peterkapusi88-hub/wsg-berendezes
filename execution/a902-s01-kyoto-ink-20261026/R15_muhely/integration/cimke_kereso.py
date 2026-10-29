"""Offline lookup only; no CNC execution, no automatic stale-revision replacement."""
import sqlite3,json,sys,hashlib
from pathlib import Path
root=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('Használat: python cimke_kereso.py R15:KI12-TV01S-01')
db=sqlite3.connect('file:'+str(root/'integration/alkatreszek_R15.sqlite')+'?mode=ro',uri=True)
row=db.execute('SELECT * FROM parts WHERE barcode=?',(sys.argv[1],)).fetchone()
if not row:raise SystemExit('Ismeretlen vagy más revíziójú címke; nincs helyettesítés.')
files=[row[3]]+json.loads(row[4])
for name in files:
 target=(root/name).resolve()
 if not target.is_relative_to(root) or not target.is_file():raise SystemExit('Hiányzó/hibás fájl: '+name)
 expected=db.execute('SELECT sha256 FROM file_hashes WHERE path=?',(name,)).fetchone()
 if not expected or hashlib.sha256(target.read_bytes()).hexdigest()!=expected[0]:raise SystemExit('Hash eltérés: '+name+'; programot nem adunk át.')
print(json.dumps({'barcode':row[0],'part':row[1],'revision':row[2],'drawing':str(root/row[3]),'active_program_drafts':[str(root/f) for f in json.loads(row[4])],'hashes_verified':True,'release_state':row[5],'machine_send':False},ensure_ascii=False,indent=2))
