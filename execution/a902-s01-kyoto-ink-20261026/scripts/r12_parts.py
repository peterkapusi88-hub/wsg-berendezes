from pathlib import Path
import csv,json,hashlib,shutil
P=Path(__file__).resolve().parents[1];O=P/'R12_muhely';rows=list(csv.DictReader((P/'R11_butorterv/data/elozetes_alkatreszek.csv').open(encoding='utf-8-sig'),delimiter=';'));parts=[]
for r in rows:
 if r['ID'].startswith(('CF','ST')):continue
 key=r['ID'];n=int(r['Db']);X,Y,T=[int(r[k]) for k in ['Hossz_mm','Szel_mm','Vast_mm']]
 for i in range(n):
  id='KI12-'+key.replace('-','')+'-'+str(i+1).zfill(2)
  edge=[1,0,0,0];front='E1';face='A = belső/felső használati felület';role='E1 látszó első él; E2/E4 szerkezeti vég; E3 hátoldal'
  if '-H' in key:edge=[0,0,0,0];front='nincs homlokél';face='A = bútor belseje felé';role='E1 alsó helyi él; mind4 él hátfalcsatlakozás'
  if key in ['TV01-F','TV02-F1','TV02-F2','GAP']:edge=[1,1,1,1];face='A = látszó homlokfelület';front='mind4 él';role='E1..E4 látszó kerület; ajtó esetén pántoldal még kijelölendő'
  if key=='TV03-P':edge=[None]*4;face='A = nyomtatott felület';front='mind4 él';role='Panelcsatlakozások, nyomat/élzárás módja mintára vár'
  if key=='TV02-CAP':edge=[1,1,0,1];face='A = látszó felső felület';role='E1 első; E2/E4 vég látszó; E3 fal felőli'
  if key in ['TV01-S','TV02-S']:hand='bal oldallap' if i%2==0 else 'jobb oldallap'
  elif key=='TV01-T':hand='alsó' if i==0 else 'felső'
  elif key=='TV01-F':hand='bal ajtó' if i==0 else 'jobb ajtó'
  else:hand='példány '+str(i+1)
  ops=['Befoglaló és anyag ellenőrzése','Élzárás / élanyag igazolása']
  if key in ['TV01-S','TV01-C','TV02-S']:ops+=['Korpusz-kötés furatai: kötőrendszer még nincs kijelölve','Polctartó/pántfurat: oldal és vasalat szerint kiosztandó']
  elif key in ['TV01-F','TV02-F1','TV02-F2']:ops+=['Pántcsésze és fogás: gyártói fúráskép hiányzik']
  elif key=='TV03-P':ops+=['Panel rögzítés/TV/LED kivágás: hely és rögzítő választandó']
  else:ops+=['Kötés / támasz / rögzítés műhelyi jóváhagyásra']
  parts.append(dict(id=id,type=key,name=r['Elem']+' / '+hand,x=X,y=Y,t=T,material=r['Anyag'],face=face,grain='X irány: magasság' if key in ['TV01-F','TV03-P','GAP'] else 'egyszínű / mintázat egyeztetendő',primary='E1 / Y=0 (tervezési javaslat)',secondary='E4 / X=0 (tervezési javaslat)',front=front,edge=edge,roles=role,ops=ops,note=r['Megjegyzes'],status='TERV - NEM GYARTAS',mpr=id+'.mpr'))
(O/'data/parts.json').write_text(json.dumps(parts,ensure_ascii=False,indent=2))
for p in parts:
 # MPR candidate: no drilling, no toolpaths, no tool IDs. Finished envelope only.
 lines=['[H','VERSION="4.0"','HP="1"','IN="0"','','[001',f'L="{p["x"]}"',f'B="{p["y"]}"',f'D="{p["t"]}"','','<100 \\WerkStck\\','LA="L"','BR="B"','DI="D"','','<101 \\Kommentar\\',f'KM="{p["id"]} R12 DESIGN ENVELOPE ONLY - NO MACHINING - NOT RELEASED"','','<101 \\Kommentar\\','KM="E1 Y0 / E4 X0 ARE PROPOSED DESIGN DATUMS, NOT APPROVED MACHINE STOPS"','!']
 (O/'mpr_alap'/p['mpr']).write_bytes(('\r\n'.join(lines)+'\r\n').encode('ascii'))
 # Minimal standard DXF ASCII R12, finished perimeter in mm, reference-only layers.
 out=['0','SECTION','2','HEADER','9','$ACADVER','1','AC1009','0','ENDSEC','0','SECTION','2','ENTITIES']
 pts=[(0,0),(p['x'],0),(p['x'],p['y']),(0,p['y'])]
 for i in range(4):
  a,b=pts[i],pts[(i+1)%4];out+=['0','LINE','8','REF_E'+str(i+1),'10',str(a[0]),'20',str(a[1]),'30','0','11',str(b[0]),'21',str(b[1]),'31','0']
 out+=['0','TEXT','8','REF_NOT_CAM','10','0','20',str(p['y']+30),'30','0','40','15','1',p['id']+' FINISHED ENVELOPE MM - NO TOOLPATH','0','ENDSEC','0','EOF']
 (O/'dxf'/(p['id']+'.dxf')).write_text('\n'.join(out)+'\n')
with (O/'data/program_index.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f,delimiter=';');w.writerow(['piece_id','mpr_file','dxf_file','stage','machine','woodwop'])
 for p in parts:w.writerow([p['id'],'mpr_alap/'+p['mpr'],'dxf/'+p['id']+'.dxf','NO_MACHINING_UNTESTED','WOF211 (user supplied)','5.0 (user supplied)'])
shutil.copy('/tmp/km_preview.png',O/'sources/km_embedded_preview.png')
(O/'data/forrasok.json').write_text(json.dumps({'dwg':{'path':'/Users/peterkapusi/Downloads/km.dwg','sha256':hashlib.sha256(Path('/Users/peterkapusi/Downloads/km.dwg').read_bytes()).hexdigest(),'format':'AC1027 DWG2013','read_status':'embedded preview only; no DWG entity converter available; geometry not interpreted'},'machine':'Homag WOF211 as supplied; model designation unverified','woodwop':'5.0','C_code':'edge banding/material-thickness shop code; exact mapping not supplied','label_photo':'user clipboard image; C meaning confirmed by user','basis':'R11 preliminary parts, fixed design dimensions, NOT surveyed','mpr':'ASCII candidate workpiece/comment blocks, VERSION4.0 format header not software version; no woodWOP opening test','reference':'https://stilesmachinery.com/assigning-woodwop-layer-names-to-dxf-geometry/'},ensure_ascii=False,indent=2))
print('instances',len(parts),'types',len(set(p['type'] for p in parts)))
