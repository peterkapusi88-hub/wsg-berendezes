from pathlib import Path
import json
O=Path(__file__).resolve().parents[1]
parts=json.loads((O/'data/parts.json').read_text())
cmd=['(setvar "FILEDIA" 0)','(setvar "CMDECHO" 0)','(setvar "OSMODE" 0)','(setvar "INSUNITS" 4)','(setvar "DELOBJ" 1)','(command "_.UCS" "_W")']
def pt(v):return "'("+' '.join(f'{q:.7f}' for q in v)+')'
for p in parts:
 x,y,z,dx,dy,dz=p['box'];id=p['id'];cmd.append(f'(command "_.-LAYER" "_M" "{id}" "")')
 if p['axis']=='y' and p['outline']:
  pts=[]
  for q in p['outline']:
   if not pts or abs(q[0]-pts[-1][0])+abs(q[1]-pts[-1][1])>.00001:pts.append(q)
  if abs(pts[0][0]-pts[-1][0])+abs(pts[0][1]-pts[-1][1])<.00001:pts.pop()
  cv=p['curve_vertices']
  entries=' '.join(f'(cons 10 (list {a:.7f} {b:.7f})) (cons 42 {bulge:.12f})' for a,b,bulge in cv)
  cmd.append(f'(entmakex (list \'(0 . "LWPOLYLINE") \'(100 . "AcDbEntity") (cons 8 "{id}") \'(100 . "AcDbPolyline") (cons 90 {len(cv)}) \'(70 . 1) {entries}))')
  cmd.append(f'(command "_.EXTRUDE" (entlast) "" {dy} 0)')
  cmd.append('(setq s16_e (entlast))')
  cmd.append('(command "_.ROTATE3D" s16_e "" "_X" \'(0 0 0) 90)')
  cmd.append(f'(command "_.MOVE" s16_e "" \'(0 0 0) {pt([x,y+dy,z])})')
 else:cmd.append(f'(command "_.BOX" {pt([x,y,z])} "_L" {dx} {dy} {dz})')
 if p.get('light_groove'):
  cmd.append('(setq s16_door (entlast))')
  for side,handle in [('outer','s16_go'),('inner','s16_gi')]:
   cv=p['light_groove'][side+'_vertices'];entries=' '.join(f'(cons 10 (list {a:.7f} {b:.7f})) (cons 42 {bulge:.12f})' for a,b,bulge in cv)
   cmd.append(f"(entmakex (list '(0 . \"LWPOLYLINE\") '(100 . \"AcDbEntity\") '(100 . \"AcDbPolyline\") (cons 90 {len(cv)}) '(70 . 1) {entries}))")
   cmd.append('(command "_.EXTRUDE" (entlast) "" 6.1 0)')
   cmd.append(f'(setq {handle} (entlast))')
   cmd.append(f"(command \"_.ROTATE3D\" {handle} \"\" \"_X\" '(0 0 0) 90)")
   cmd.append(f"(command \"_.MOVE\" {handle} \"\" '(0 0 0) {pt([x,400.1,z])})")
  cmd.append('(command "_.SUBTRACT" s16_go "" s16_gi "")')
  cmd.append('(command "_.SUBTRACT" s16_door "" s16_go "")')
# TV body as wireframe, not a furniture part.
lay=json.loads((O/'data/layout.json').read_text());x,y,z,dx,dy,dz=lay['screen_box']
a=[(x,y,z),(x+dx,y,z),(x+dx,y+dy,z),(x,y+dy,z),(x,y,z+dz),(x+dx,y,z+dz),(x+dx,y+dy,z+dz),(x,y+dy,z+dz)]
cmd.append('(command "_.-LAYER" "_M" "TV75_REFERENCE" "")')
for u,v in [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)]:cmd.append(f'(command "_.LINE" {pt(a[u])} {pt(a[v])} "")')
cmd+=['(princ (list "S16_SOLIDS" (sslength (ssget "_X" \'((0 . "3DSOLID"))))))','(command "_.AUDIT" "_N")','(command "_.ZOOM" "_E")','(command "_.SAVEAS" "2018" "/private/tmp/S16_R05_szerkezet.dwg")','(princ "S16_SAVE_DONE")','_.QUIT','_Y']
(O/'rebuild/build.scr').write_text('\n'.join(cmd)+'\n')
verify=['(setvar "FILEDIA" 0)','(princ (list "S16_SOLIDS_READBACK" (sslength (ssget "_X" \'((0 . "3DSOLID"))))))','(princ (list "S16_INSUNITS" (getvar "INSUNITS")))','(command "_.AUDIT" "_N")','(command "_.ZOOM" "_E")','(princ (list "S16_EXTMIN" (getvar "EXTMIN") "S16_EXTMAX" (getvar "EXTMAX")))','_.QUIT','_Y']
(O/'rebuild/verify.scr').write_text('\n'.join(verify)+'\n')
