from pathlib import Path
import json,shutil
import ezdxf
from ezdxf.render import forms
from ezdxf.acis import api as acis
from shapely.geometry import Polygon,box
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok'
parts=json.loads((O/'data/parts.json').read_text());hw=json.loads((O/'data/hardware_geometry.json').read_text());art=json.loads((O/'data/artwork.json').read_text())
shutil.copy2('/tmp/TV_R16_zart_v2.dwg',O/'rajzok/TV_R16_megmunkalt.dwg');shutil.copy2('/tmp/ki16build02.log',O/'audit/autocad_build.log')
d=ezdxf.new('R2013');d.units=4;m=d.modelspace()
for h in hw:
 layer='HW_'+h['id'];d.layers.new(layer,dxfattribs={'color':4 if not h['id'].startswith('LED') else 30});x,y,z,w,dep,hh=h['box'];mesh=forms.cube(center=False);mesh.scale(w,dep,hh);mesh.translate(x,y,z);e=m.add_3dsolid(dxfattribs={'layer':layer});acis.export_dxf(e,[acis.body_from_mesh(mesh)])
d.layers.new('INK_W01_R16',dxfattribs={'true_color':ezdxf.colors.rgb2int((34,30,25))})
for panel in art['panels']:
 p=next(p for p in parts if p['id']==panel['part']);x,y,z,w,dep,h=p['assembly_box_mm'];clip=box(x,z,x+w,z+h)
 for raw in art['ink_polygons']:
  g=Polygon(raw['outer'],raw['holes']).intersection(clip)
  for shape in list(g.geoms) if hasattr(g,'geoms') else [g]:
   if shape.is_empty or shape.geom_type!='Polygon':continue
   hatch=m.add_hatch(dxfattribs={'layer':'INK_W01_R16','extrusion':(0,-1,0),'elevation':(0,0,-y+.02),'true_color':ezdxf.colors.rgb2int((34,30,25))});hatch.paths.add_polyline_path(list(shape.exterior.coords),is_closed=True,flags=1)
   for q in shape.interiors:hatch.paths.add_polyline_path(list(q.coords),is_closed=True,flags=0)
# Editable dimensioned front elevation in the same DWG, deliberately separate from3D.
for layer,c in [('R16_FRONT_VIEW',7),('R16_DIMS',2),('R16_NOTES',3)]:d.layers.new(layer,dxfattribs={'color':c})
ox=5000
for p in parts:
 if p['type'] in ['TV01-F','TV02-F1','TV02-F2','TV03-P','GAP']:
  x,y,z,w,dep,h=p['assembly_box_mm'];m.add_lwpolyline([(ox+x,z),(ox+x+w,z),(ox+x+w,z+h),(ox+x,z+h)],close=True,dxfattribs={'layer':'R16_FRONT_VIEW'})
for a,b in [(0,720),(720,1170),(1170,1620),(1620,2700),(2700,3150),(3150,3600)]:
 dm=m.add_linear_dim(base=(ox,-100),p1=(ox+a,150),p2=(ox+b,150),dimstyle='EZDXF',override={'dimtxt':35,'dimasz':15,'dimdec':0});dm.render()
dm=m.add_linear_dim(base=(ox,3100),p1=(ox+720,2880),p2=(ox+920,2880),dimstyle='EZDXF',override={'dimtxt':35,'dimasz':15,'dimdec':0});dm.render()
for i,s in enumerate(['R16 /3600 x2880mm / 6 HIGH DRAWERS / NO HORIZONTAL SPLIT','BRONZE BAND200mm / MDF18 + MATCHING MATT FINISH','RECESSED LED ON TOWER SIDE:45deg18x18 PROFILE /2300mm','ALL DIMENSIONS DESIGN ONLY / SURVEY + HARDWARE TRIAL PENDING','BLUE=HARDWARE ENVELOPE / NOT FACTORY MESH','INK=TRACE OF VISIBLE SOURCE / PROOF PRINT REQUIRED']):m.add_text(s,dxfattribs={'height':38,'insert':(ox,3300+i*65),'layer':'R16_NOTES'})
d.saveas('/tmp/ki16_overlay.dxf');d.saveas(O/'rajzok/TV_R16_feluletek_vasalat_rajz.dxf')
Path('/tmp/ki16_overlay.scr').write_text('(setvar "FILEDIA" 0)\n(command "_.SAVEAS" "2018" "/tmp/ki16_overlay_v3.dwg")\n_.QUIT\n_Y\n')
Path('/tmp/ki16v2_stls').mkdir(exist_ok=True)
def pt(v):return "'("+' '.join(str(vv) for vv in v)+')'
def ss(pid):return f'(ssget "_X" \'((0 . "3DSOLID") (8 . "{pid}")))'
cmd=['(setvar "CMDECHO" 0)','(setvar "FILEDIA" 0)','(setvar "OSMODE" 0)','(setvar "FACETRES" 5)']
for p in parts:
 if not (Path('/tmp/ki16v2_stls')/(p['id']+'.stl')).exists():cmd.append(f'(command "_.STLOUT" {ss(p["id"])} "" "_Y" "/tmp/ki16v2_stls/{p["id"]}.stl")')
cmd+=['(command "_.-INSERT" "/tmp/ki16_overlay_v3.dwg" \'(0 0 0) 1 1 0)','(command "_.EXPLODE" (entlast))','(command "_.VPOINT" \'(1 -2 1.1))','(command "_.ZOOM" "_W" \'(-250 -600 -50) \'(4000 900 3200))','(command "_.SAVEAS" "2018" "/tmp/TV_R16_teljes_zart_v3.dwg")']
drawers=json.loads((O/'data/drawers.json').read_text())
for q in drawers:
 for pid in [q['front']]+q['parts']:cmd.append(f'(command "_.MOVE" {ss(pid)} "" \'(0 0 0) \'(0 -300 0))')
cmd+=['_.AUDIT','_N','(command "_.SAVEAS" "2018" "/tmp/TV_R16_fiokok_nyitva_v3.dwg")','_.QUIT','_Y'];Path('/tmp/ki16_views.scr').write_text('\n'.join(cmd)+'\n');(O/'integration/ki16_views.scr').write_text('\n'.join(cmd)+'\n')
print('overlay and views prepared',len(hw))
