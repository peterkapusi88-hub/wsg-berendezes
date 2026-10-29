from pathlib import Path
import json,csv,sqlite3,hashlib,shutil
import ezdxf
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
def read(n):return json.loads((O/n).read_text())
parts=read('data/parts.json');hw=read('data/hardware_geometry.json');progs=read('data/programs.json')
def csvwrite(name,headers,rows):
 with (O/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f,delimiter=';');w.writerow(headers);w.writerows(rows)
for root in [O,O/'pilot']:
 ps=json.loads((root/'data/parts.json').read_text());pr=json.loads((root/'data/programs.json').read_text())
 rows=[]
 for p in ps:
  rows.append(['R15:'+p['id'],p['id'],'R15',p['name'],p['x'],p['y'],p['t'],p['material'],p['primary'],p['secondary'],p['face'],p['front'],*p['edge'],'NYITOTT',p['grain'],'dxf_alkatreszek/'+p['id']+'_R15.dxf',json.dumps([q['path'] for q in pr if q['part']==p['id']]),'TERV_NEM_GYARTAS'])
 with (root/'integration/alkatresz_import_UTF8.csv').open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.writer(f,delimiter=';');w.writerow(['barcode','part_id','revision','name','finished_U_mm','finished_V_mm','thickness_mm','material','reference_1','reference_2','face_definition','visible_edge','E1_mm','E2_mm','E3_mm','E4_mm','C_shop_code','grain','drawing','mpr_paths_json','release']);w.writerows(rows)
csvwrite('integration/szerszam_lekepzes.csv',['muvelet','atmero_mm','melysegek_mm','irany','gep_szerszam_ID','fordulat_rpm','elotolas','befogas','ellenorzo'],[[t['operation'],t['nominal_diameter_mm'],','.join(map(str,t['depths_mm'])),t['direction'],'','','','',''] for t in read('data/tool_requirements.json')])
csvwrite('integration/elanyag_kodtabla.csv',['C_kod','anyag','vastagsag_mm','ragaszto','elmarasi_rahagyas','szinminta','jovahagyas'],[['','','','','','','']])
# Editable 1:1 engineering sections, derived from current boxes, not generative images.
for axis,cut,title in [(2,470,'D15_05_vizszintes_Z470'),(0,2919,'D15_06_fuggoleges_X2919'),(0,1000,'D15_07_AV_X1000')]:
 d=ezdxf.new('R2013');d.units=4;m=d.modelspace();a,b=[i for i in range(3) if i!=axis]
 for name,col in [('WOOD',7),('HARDWARE_ENVELOPE',4),('WALL_ASSUMED',8),('NOTES',2)]:d.layers.new(name,dxfattribs={'color':col})
 for obj in parts+hw:
  box=obj.get('assembly_box_mm',obj.get('box'));x,y=box[a],box[b];w,h=box[a+3],box[b+3]
  if box[axis]<=cut<=box[axis]+box[axis+3]:
   lay='WOOD' if 'assembly_box_mm' in obj else 'HARDWARE_ENVELOPE'
   m.add_lwpolyline([(x,y),(x+w,y),(x+w,y+h),(x,y+h)],close=True,dxfattribs={'layer':lay})
   m.add_text(obj['id'],dxfattribs={'height':5,'layer':'NOTES','insert':(x,y+h+4)})
 if axis==2:m.add_line((0,418),(3600,418),dxfattribs={'layer':'WALL_ASSUMED'});m.add_linear_dim(base=(0,-90),p1=(0,0),p2=(3600,0),dimstyle='EZDXF').render()
 else:
  m.add_line((418,0),(418,2880),dxfattribs={'layer':'WALL_ASSUMED'});m.add_linear_dim(base=(-100,0),p1=(-21,0),p2=(418,0),dimstyle='EZDXF').render()
 m.add_text(title+' / R15 / mm / nominal dimensions; not surveyed',dxfattribs={'height':12,'insert':(0,-150)})
 m.add_text('Cyan = hardware ENVELOPE. Wall Y418 assumed. Bore details: part drawings.',dxfattribs={'height':10,'insert':(0,-180)})
 assert not d.audit().has_errors;d.saveas(O/'rajzok'/f'{title}.dxf')
# Preserve exact scripts that were run for reproducibility.
for name in ['ki15_verify.scr','ki15_coord_verify.scr']:
 shutil.copy2('/tmp/'+name,O/'integration'/name)
print('75 +10 CSV records;13 tool mappings;3 editable sections')
