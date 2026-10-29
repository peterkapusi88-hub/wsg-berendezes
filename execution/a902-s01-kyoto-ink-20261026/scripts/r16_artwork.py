"""Technical vector tracing from supplied raster; no generative repainting."""
from pathlib import Path
import json,hashlib,cv2,numpy as np
from shapely.geometry import Polygon,box
from shapely.ops import unary_union
import ezdxf
P=Path(__file__).resolve().parents[1];O=P/'R16_feluletek_fiokok';src=O/'sources/T16_mediafal_tulajdonosi_celkep.png'
im=cv2.imread(str(src));assert im.shape[:2]==(992,1586),im.shape
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# Measured image control points, not surveyed architectural geometry.
zones=[dict(id='TOWER',quad=[[35,23],[202,60],[202,580],[35,603]],target=[[1.5,2878.5],[718.5,2878.5],[718.5,551.5],[1.5,551.5]],threshold=72,roi=[[[35,475],[202,367],[202,433],[35,578]]]),dict(id='FIELD',quad=[[257,93],[704,202],[704,514],[257,568]],target=[[920,2880],[3600,2880],[3600,550],[920,550]],threshold=90,roi=[[[299,102],[366,118],[367,188],[355,275],[345,331],[329,419],[315,483],[310,546],[291,547],[292,468],[296,416],[291,374],[300,316],[302,253],[294,193],[296,132]],[[257,394],[387,356],[387,397],[257,455]]])]
allpolys=[];meta=[];d=ezdxf.new('R2013');d.units=4;m=d.modelspace();d.layers.new('INK_TRACE',dxfattribs={'color':7});d.layers.new('PANEL_CUT',dxfattribs={'color':3});d.layers.new('REVEAL_NO_PRINT',dxfattribs={'color':1})
for zn in zones:
 mask=np.zeros(gray.shape,np.uint8)
 for roi in zn['roi']:cv2.fillPoly(mask,[np.array(roi,np.int32)],255)
 mask=((gray<zn['threshold'])&(mask>0)).astype(np.uint8)*255
 H=cv2.getPerspectiveTransform(np.float32(zn['quad']),np.float32(zn['target']))
 contours,hier=cv2.findContours(mask,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE);polys=[]
 for i,c in enumerate(contours):
  if hier[0,i,3]!=-1 or cv2.contourArea(c)<.8:continue
  outer=cv2.perspectiveTransform(c.astype(np.float32),H).reshape(-1,2);holes=[];child=hier[0,i,2]
  while child!=-1:
   if len(contours[child])>=3:holes.append(cv2.perspectiveTransform(contours[child].astype(np.float32),H).reshape(-1,2))
   child=hier[0,child,0]
  if len(outer)<3:continue
  g=Polygon(outer,holes).buffer(0).simplify(.45,preserve_topology=True)
  for p in list(g.geoms) if hasattr(g,'geoms') else [g]:
   if p.area>2:polys.append(p)
 geom=unary_union(polys).intersection(Polygon(zn['target']));geoms=list(geom.geoms) if hasattr(geom,'geoms') else [geom];allpolys+=geoms
 meta.append({**zn,'H_pixel_to_XZ':H.tolist(),'polygons':len(geoms),'image_alignment_error_pixels':'manually selected plane corners, not camera calibration; source-only 1pixel tracing tolerance','hidden_regions':'TV/objects/reveal: no invented original brushwork'})
geom=unary_union(allpolys)
parts=json.loads((O/'data/parts.json').read_text());panels=[p for p in parts if p['type'] in ['TV01-F','TV03-P']]
def paths(g,ox=0,oy=0,flip=False):
 out=[]
 for p in list(g.geoms) if hasattr(g,'geoms') else [g]:
  if p.is_empty or p.geom_type!='Polygon':continue
  rings=[list(p.exterior.coords)]+[list(h.coords) for h in p.interiors]
  s=' '.join('M '+' L '.join(f'{x-ox:.3f},{oy-y if flip else y-oy:.3f}' for x,y in ring)+' Z' for ring in rings)
  out.append(s)
 return out
def svgfile(f,g,vb,width,height,ox=0,oy=0,flip=False):
 ps=''.join('<path d="'+s+'" fill="#24211e" fill-rule="evenodd"/>' for s in paths(g,ox,oy,flip))
 f.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}mm" height="{height}mm" viewBox="{vb}"><title>KI-R16 derived trace, dimensional artwork; proof required</title>{ps}</svg>')
svgfile(O/'artwork/INK_W01_R16_MASTER_3600.svg',geom,'0 0 3600 2330',3600,2330,0,2880,True)
register=[]
for p in panels:
 x,y,z,w,dep,h=p['assembly_box_mm'];g=geom.intersection(box(x,z,x+w,z+h))
 svgfile(O/'artwork'/(p['id']+'_INK_TRIM.svg'),g,f'0 0 {w} {h}',w,h,x,z+h,True)
 # 10mm non-distorting bleed crop from same master; exterior master area remains unprinted.
 gb=geom.intersection(box(x-10,z-10,x+w+10,z+h+10));svgfile(O/'artwork'/(p['id']+'_INK_BLEED10.svg'),gb,f'0 0 {w+20} {h+20}',w+20,h+20,x-10,z+h+10,True)
 m.add_lwpolyline([(x,z),(x+w,z),(x+w,z+h),(x,z+h)],close=True,dxfattribs={'layer':'PANEL_CUT'})
 for shape in list(g.geoms) if hasattr(g,'geoms') else [g]:
  if shape.geom_type!='Polygon' or shape.is_empty:continue
  hatch=m.add_hatch(color=7,dxfattribs={'layer':'INK_TRACE'});hatch.paths.add_polyline_path(list(shape.exterior.coords),is_closed=True,flags=1)
  for hole in shape.interiors:hatch.paths.add_polyline_path(list(hole.coords),is_closed=True,flags=0)
 register.append({'part':p['id'],'X':x,'Z':z,'W':w,'H':h,'ink_area_m2':g.area/1e6,'net_surface_m2':w*h/1e6,'print_with_bleed_m2':(w+20)*(h+20)/1e6,'TRIM':p['id']+'_INK_TRIM.svg','BLEED':p['id']+'_INK_BLEED10.svg','surface':'M02 Bely+Print 1040.01 candidate' if p['type']=='TV03-P' else 'M01 dark graphite + printed compatible face layer; sample required'})
m.add_lwpolyline([(720,550),(920,550),(920,2880),(720,2880)],close=True,dxfattribs={'layer':'REVEAL_NO_PRINT'})
d.saveas(O/'artwork/INK_W01_R16_3600.dxf')
(O/'data/artwork.json').write_text(json.dumps({'source':str(src),'sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'revision':'R16','zones':meta,'panels':register,'ink_polygons':[{'outer':list(p.exterior.coords),'holes':[list(q.coords) for q in p.interiors]} for p in allpolys],'status':'source-derived visible brushwork; manual plane calibration; no guarantee of original hidden art; printer ICC and material proof pending'},ensure_ascii=False,indent=2))
print(json.dumps({'polygons':len(allpolys),'panels':len(register),'net_m2':sum(r['net_surface_m2'] for r in register),'print_m2':sum(r['print_with_bleed_m2'] for r in register)}))
