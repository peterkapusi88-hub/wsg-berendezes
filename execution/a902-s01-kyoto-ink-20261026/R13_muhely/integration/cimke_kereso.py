"""Offline label lookup. Never launches a CNC program or writes to a machine."""
import sqlite3,json,sys
from pathlib import Path
root=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('Használat: python cimke_kereso.py R13:KI12-TV01S-01')
db=sqlite3.connect('file:'+str(root/'integration/alkatreszek_R13.sqlite')+'?mode=ro',uri=True)
row=db.execute('SELECT * FROM parts WHERE barcode=?',(sys.argv[1],)).fetchone()
if not row:raise SystemExit('Ismeretlen vagy más revíziójú címke; nincs automatikus helyettesítés.')
files=[row[3]]+json.loads(row[4]);missing=[f for f in files if not (root/f).is_file()]
if missing:raise SystemExit('Hiányzó fájlok: '+str(missing))
print(json.dumps({'barcode':row[0],'part':row[1],'revision':row[2],'drawing':str(root/row[3]),'active_program_drafts':[str(root/f) for f in json.loads(row[4])],'release_state':row[5],'machine_send':False},ensure_ascii=False,indent=2))
