from pathlib import Path
import sys,json,math,csv
sys.path.insert(0,'/private/tmp/s16-python')
import ezdxf,pymupdf,openpyxl
from ezdxf import bbox
O=Path(__file__).resolve().parents[1];ps=json.loads((O/'data/parts.json').read_text());errors=[]
ids=[p['id']for p in ps];assert len(ids)==len(set(ids))==120
assert {p.stem for p in (O/'alkatreszek').glob('*.dxf')}==set(ids)
w=openpyxl.load_workbook(O/'S16_R05_koltseg_es_alkatreszek.xlsx',data_only=True)
rows={r[0]:r for r in w['Alkatrészek'].iter_rows(min_row=6,max_row=125,values_only=True)}
cs=list(csv.reader((O/'data/alkatreszek.csv').open()));cs={r[0]:r for r in cs[1:]}
pdf=pymupdf.open(O/'rajzok/S16_R05_tervcsomag.pdf')
for p in ps:
 id=p['id'];dims=[p[k]for k in ['L','W','T']];b=p['box'];dx,dy,dz=b[3:];expected={'x':[dy,dz,dx],'y':[dx,dz,dy],'z':[dx,dy,dz]}[p['axis']]
 if any(not math.isfinite(v)or v<=0 for v in dims+b[3:]):errors.append([id,'non-positive or nonfinite'])
 if dims!=expected:errors.append([id,'axis mismatch',dims,expected])
 if list(rows[id][2:5])!=dims:errors.append([id,'xlsx mismatch'])
 if [float(v)for v in cs[id][3:6]]!=dims:errors.append([id,'csv mismatch'])
 doc=ezdxf.readfile(O/'alkatreszek'/f'{id}.dxf');bb=bbox.extents([list(doc.modelspace().query('LWPOLYLINE'))[0]]);actual=[bb.size.x,bb.size.y]
 if any(abs(a-v)>.005 for a,v in zip(actual,dims[:2])):errors.append([id,'DXF extent mismatch',actual,dims])
 expected_text=f'{dims[0]:g} × {dims[1]:g} × {dims[2]:g} mm'
 found=False
 for page in pdf:
  if 'Alkatrészlapok' not in page.get_text():continue
  for block in page.get_text('blocks'):
   if id+' ' in block[4]:
    near=pymupdf.Rect(block[:4]);near.y1+=35;txt=page.get_textbox(near)
    if expected_text in txt:found=True
 if not found:errors.append([id,'PDF part dimension could not be matched',expected_text])
assert not errors,errors
S=O.parent.parent/'a902-s01-kyoto-ink-20261026/R16_feluletek_fiokok';sp=json.loads((S/'data/parts.json').read_text());bad=[];negative=[]
for p in sp:
 dims=[p['x'],p['y'],p['t']];b=p['assembly_box_mm'][3:];f=p['frame'];expected=[sum(abs(v)*d for v,d in zip(f[k],b))for k in ['U','V','outward_A']]
 if any(v<=0 for v in dims):negative.append(p['id'])
 if any(abs(a-b)>.01 for a,b in zip(dims,expected)):bad.append({'id':p['id'],'listed':dims,'geometry':expected})
report={'S16_parts':120,'S16_errors':errors,'checks':['Positive finite L/W/T and physical extents','Unique IDs and exact DXF inventory','L/W/T against assembly-axis mapping','Excel exact columns C/D/E','CSV exact dimensions','Exact arc DXF contour bounding dimensions','PDF dimensions next to corresponding part ID'],'S16_MPR':'None generated; no CNC release.','S01_read_only_crosscheck':{'parts':len(sp),'mismatches':bad,'nonpositive':negative,'additional_dimension_mismatches_beyond_reported_12':len(bad)-12,'scope':'Local part dimensions vs assembly_box_mm and frame U/V/A only; not a new complete S01 manufacturing review. S01 source untouched.'}}
(O/'audit/export_checks.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print(json.dumps(report,ensure_ascii=False))
