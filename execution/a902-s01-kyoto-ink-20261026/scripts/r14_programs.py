"""Active MPR engineering drafts plus local ID resolver data; never machine-send."""
from pathlib import Path
import json,math,re,csv,sqlite3,unicodedata,hashlib
import ezdxf
P=Path(__file__).resolve().parents[1];O=P/'R14_muhely'
parts=json.loads((O/'data/parts.json').read_text());holes=json.loads((O/'data/holes.json').read_text())
for d in ['mpr_aktiv_tervezet','dxf_alkatreszek']: (O/d).mkdir(exist_ok=True)
programs=[];mapped=[]
def ascii(s):return unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode()
for p in parts:
 hs=[h for h in holes if h['part']==p['id']];faces=['A']+(['B'] if any(h['local_axis'][2]>.5 for h in hs) else [])
 for face in faces:
  assigned=[h for h in hs if (h['local_axis'][2]>.5)==(face=='B')]
  if not assigned:continue
  name=f'{p["id"]}_R14_{face}.mpr';s=['[H','VERSION="4.0"','HP="1"','IN="0"','[001',f'L="{p["x"]}"',f'B="{p["y"]}"',f'D="{p["t"]}"','<100 \\WerkStck\\','LA="L"','BR="B"','DI="D"','<101 \\Kommentar\\',f'KM="R14 {p["id"]} FACE {face} DESIGN ONLY ACTIVE OPERATIONS - NOT SHOP VALIDATED"']
  for h in assigned:
   u,v,w=h['local_UVW'];a=h['local_axis'];diam=h['diameter'];depth=h['depth']
   if face=='B':v=p['y']-v;w=-p['t']-w;a=[a[0],-a[1],-a[2]]
   if abs(a[2])>.5:
    macro=102;mode='SS';extra=[]
   else:
    macro=103;mode=('XP' if a[0]>0 else 'XM') if a[0] else ('YP' if a[1]>0 else 'YM');extra=[f'ZA="{p["t"]+w:g}"']
   values=dict(id=h['id'],part=p['id'],program=name,face=face,macro=macro,X=u,Y=v,Z=p['t']+w,D=diam,depth=depth,mode=mode,enabled=True)
   mapped.append(values)
   s += [f'<{macro} \\'+('BohrVert' if macro==102 else 'BohrHoriz')+'\\',f'XA="{u:g}"',f'YA="{v:g}"',*extra,f'BM="{mode}"',f'TI="{depth:g}"',f'DU="{diam:g}"','AN="1"','MI="0"','AB="0"','F_="STANDARD"','EN="1"','??="1"',f'KM="{h["id"]} {ascii(h["kind"])} ACTIVE DRAFT"']
  s+=['!'];f=O/'mpr_aktiv_tervezet'/name;f.write_bytes(('\r\n'.join(s)+'\r\n').encode('ascii'))
  programs.append(dict(part=p['id'],revision='R14',face=face,path='mpr_aktiv_tervezet/'+name,holes=len(assigned),enabled=True,sha256=hashlib.sha256(f.read_bytes()).hexdigest()))
 # Real editable 1:1 CAD drawing: A-face bores, edge-axis projections, dimensions.
 doc=ezdxf.new('R2010');doc.units=4;m=doc.modelspace()
 for name,color in [('CONTOUR',7),('BORE_A',1),('BORE_B',5),('EDGE_BORE',3),('TEXT',7),('DIM',2)]:doc.layers.new(name,dxfattribs={'color':color})
 x,y,t=p['x'],p['y'],p['t'];sc=max(x,y)/60
 m.add_lwpolyline([(0,0),(x,0),(x,y),(0,y)],close=True,dxfattribs={'layer':'CONTOUR'})
 for h in hs:
  u,v,w=h['local_UVW'];a=h['local_axis'];layer='BORE_A' if a[2]<0 else 'BORE_B' if a[2]>0 else 'EDGE_BORE'
  if a[2]:m.add_circle((u,v),h['diameter']/2,dxfattribs={'layer':layer})
  else:m.add_line((u,v),(u+a[0]*h['depth'],v+a[1]*h['depth']),dxfattribs={'layer':layer})
  m.add_text(h['id'],dxfattribs={'height':max(4,sc*.22),'insert':(u+5,v+5),'layer':'TEXT'})
 for a,b,base,angle in [((0,0),(x,0),(0,-sc*3),0),((0,0),(0,y),(-sc*3,0),90)]:
  dim=m.add_linear_dim(base=base,p1=a,p2=b,angle=angle,dimstyle='EZDXF',override={'dimtxt':sc*.7,'dimasz':sc*.4,'dimclrd':2,'dimclre':2,'dimclrt':7,'dimdec':2});dim.render()
 m.add_text(p['id']+' / R14 / A-FACE / mm',dxfattribs={'height':sc,'insert':(0,y+sc*4),'layer':'TEXT'})
 m.add_text('RED=A BORE | BLUE=B PROJECTION | GREEN=EDGE AXIS',dxfattribs={'height':sc*.6,'insert':(0,y+sc*2),'layer':'TEXT'})
 m.add_text('DESIGN ONLY - DATUM NOT A MACHINE STOP - t='+str(t),dxfattribs={'height':sc*.6,'insert':(0,-sc*6),'layer':'TEXT'})
 doc.saveas(O/'dxf_alkatreszek'/(p['id']+'_R14.dxf'))
# Independent text readback of the MPR macro numbers, coordinates and disabled state.
errors=[];count=0
for pr in programs:
 text=(O/pr['path']).read_text();blocks=re.split(r'(?m)^<',text)[1:]
 for block in blocks:
  mm=re.match(r'(102|103) ',block)
  if not mm:continue
  vals=dict(re.findall(r'(?m)^([A-Z_?]+)="([^"]*)"',block));hid=re.search(r'H\d{4}',vals['KM']).group();src=next(h for h in mapped if h['id']==hid)
  assert vals['EN']=='1' and vals['??']=='1'
  for key,skey in [('XA','X'),('YA','Y'),('DU','D'),('TI','depth')]:
   if abs(float(vals[key])-src[skey])>1e-5:errors.append([hid,key])
  if vals['BM']!=src['mode']:errors.append([hid,'BM'])
  count+=1
assert count==len(holes) and not errors,(count,errors)
(O/'data/programs.json').write_text(json.dumps(programs,ensure_ascii=False,indent=2));(O/'data/mpr_mapping.json').write_text(json.dumps(mapped,ensure_ascii=False,indent=2))
(O/'audit/mpr_readback.json').write_text(json.dumps({'files':len(programs),'mapped_holes':count,'all_operations_enabled':True,'readback_errors':errors,'woodWOP_5_opened':False,'machine_simulation':False,'basis':'HOMAG woodWOP file description4.2.7 / 9-080-42-7190-D00 2006-07-26, macros102/103; secondary-hosted manufacturer excerpt','source':'https://www.scribd.com/document/615867902/HOMAG-Mpr4x-Format-Us','limitations':'No routing, no hardware bodies, no shop tool library, raw-size and stop convention not confirmed. Own parser readback is not woodWOP acceptance.'},indent=2))
dbfile=O/'integration/alkatreszek_R14.sqlite'
if dbfile.exists():dbfile.unlink()
db=sqlite3.connect(dbfile);db.execute('CREATE TABLE parts(barcode TEXT PRIMARY KEY,part TEXT,revision TEXT,dxf TEXT,programs TEXT,release_state TEXT)')
for p in parts:db.execute('INSERT INTO parts VALUES(?,?,?,?,?,?)',('R14:'+p['id'],p['id'],'R14','dxf_alkatreszek/'+p['id']+'_R14.dxf',json.dumps([pr['path'] for pr in programs if pr['part']==p['id']]),'ACTIVE_DRAFT_NOT_SHOP_VALIDATED'))
db.commit();assert db.execute('SELECT COUNT(*) FROM parts').fetchone()[0]==len(parts);db.close()
print(json.dumps({'MPR_files':len(programs),'drilling_macros':count,'parts':len(parts),'status':'ACTIVE_DRAFT_NO_MACHINE_TEST'}))
