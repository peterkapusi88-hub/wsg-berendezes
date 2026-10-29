from pathlib import Path
import json,shutil
P=Path(__file__).resolve().parents[1];O=P/'R15_muhely'
parts=json.loads((O/'data/parts.json').read_text());hardware=json.loads((O/'data/hardware_geometry.json').read_text());lighting=json.loads((O/'data/lighting.json').read_text())
Path('/tmp/ki15_stls').mkdir(exist_ok=True)
shutil.copy2('/tmp/TV_R15_zart_v1.dwg',O/'rajzok/TV_R15_megmunkalt.dwg');shutil.copy2('/tmp/ki15build01.log',O/'audit/autocad_build.log')
def pt(v):return "'("+' '.join(f'{x:.6f}' for x in v)+')'
def select(pid):return f'(ssget "_X" \'((0 . "3DSOLID") (8 . "{pid}")))'
cmd=['(setvar "CMDECHO" 0)','(setvar "FILEDIA" 0)','(setvar "OSMODE" 0)','(setvar "FACETRES" 5)']
for p in parts:
 if not Path('/tmp/ki15_stls/'+p['id']+'.stl').exists():cmd.append(f'(command "_.STLOUT" {select(p["id"])} "" "_Y" "/tmp/ki15_stls/{p["id"]}.stl")')
for h in hardware:
 x,y,z,w,d,hh=h['box'];layer='HW_'+h['id'];col=4 if h['id'].startswith(('HG','WP','PC','PR','PK')) else 2
 cmd.extend([f'(command "_.-LAYER" "_M" "{layer}" "_C" "{col}" "{layer}" "")',f'(command "_.BOX" {pt([x,y,z])} {pt([x+w,y+d,z])} {hh})',f'(progn (entmod (append (entget (entlast)) \'((-3 ("KYOTO_INK" (1000 . "{h["id"]}") (1000 . "R15 HARDWARE ENVELOPE - NOT MANUFACTURER SOLID")))))) (princ))'])
for light in lighting['circuits']:
 a,b=light['path'];layer=light['id'];cmd += [f'(command "_.-LAYER" "_M" "{layer}" "_C" "30" "{layer}" "")',f'(command "_.3DPOLY" {pt(a)} {pt(b)} "")']
cmd+=['(command "_.VPOINT" \'(1 -2 1.1))','(command "_.ZOOM" "_E")','(command "_.-VIEW" "_S" "R15_KOORDINACIO")','(command "_.SAVEAS" "2018" "/tmp/TV_R15_koordinacio_v2.dwg")']
poses={}
for p in parts:
 x,y,z,w,d,h=p['assembly_box_mm'];delta=[0,0,0]
 if p['type'] in ['TV01-F','TV02-F1','TV02-F2']:delta=[0,-650,0]
 elif p['type'] in ['TV01-H','TV02-H1','TV02-H2']:delta=[0,500,0]
 elif p['type']=='TV03-P':delta=[0,700,0]
 elif p['type']=='TV02-CAP':delta=[0,0,180]
 elif p['type'] in ['TV01-P','TV02-P1','TV02-P2']:delta=[0,-180,0]
 poses[p['id']]=delta
 if any(delta):cmd.append(f'(command "_.MOVE" {select(p["id"])} "" \'(0 0 0) {pt(delta)})')
cmd+=['(command "_.ZOOM" "_E")','(command "_.-VIEW" "_S" "R15_ROBBANTOTT")','_.AUDIT','_N','(command "_.SAVEAS" "2018" "/tmp/TV_R15_robbantott_v2.dwg")','_.QUIT','_Y']
Path('/tmp/ki15_views.scr').write_text('\n'.join(cmd)+'\n');(O/'integration/ki15_views.scr').write_text('\n'.join(cmd)+'\n');(O/'data/exploded_poses.json').write_text(json.dumps(poses,indent=2))
# Independent readback of the machined-only saved DWG.
verify=['(setvar "CMDECHO" 0)','(princ (list "KI_R15_SOLIDS" (sslength (ssget "_X" \'((0 . "3DSOLID"))))))','_.AUDIT','_N','_.MASSPROP','_ALL','','_N']
for p in parts:verify.append(f'(princ (list "PART" "{p["id"]}" (sslength {select(p["id"])})))')
verify+=['_.QUIT','_Y'];Path('/tmp/ki15_verify.scr').write_text('\n'.join(verify)+'\n')
print('Native export and coordination scripts ready')
