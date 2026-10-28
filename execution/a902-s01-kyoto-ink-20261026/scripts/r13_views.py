from pathlib import Path
import json,math
P=Path(__file__).resolve().parents[1];O=P/'R13_muhely';parts=json.loads((O/'data/parts.json').read_text())
Path('/tmp/ki13_stls').mkdir(exist_ok=True)
def pt(v):return "'("+' '.join(str(round(n,5)) for n in v)+')'
def select(p):return f'(setq ki_s (ssget "_X" \'((0 . "3DSOLID") (8 . "{p["id"]}"))))'
cmd=['(setvar "CMDECHO" 0)','(setvar "FILEDIA" 0)','(setvar "OSMODE" 0)','(setvar "FACETRES" 5)']
for p in parts:
 cmd += [select(p),f'(command "_.STLOUT" ki_s "" "_Y" "/tmp/ki13_stls/{p["id"]}.stl")']
# Rotation is an inspection pose only, not manufacturer kinematics.
poses={}
lower=0;tower=0
for p in parts:
 x,y,z,w,d,h=p['assembly_box_mm'];pose={'rotation_deg':0,'pivot':[0,0,0],'translation':[0,0,0]}
 if p['type']=='TV01-F':
  right=tower==1;pose.update(rotation_deg=100 if right else -100,pivot=[x+w if right else x,-12,z]);tower+=1
 elif p['type'] in ['TV02-F1','TV02-F2']:
  if lower in [2,3]:pose['translation']=[0,-680,0];pose['note']='KIEMELT FRONT: nem működő nyitási póz'
  else:pose.update(rotation_deg=-100,pivot=[x,-12,z])
  lower+=1
 poses[p['id']]=pose
 if pose['rotation_deg']:
  cmd += [select(p),f'(command "_.ROTATE3D" ki_s "" "_Z" {pt(pose["pivot"])} {pose["rotation_deg"]})']
 if any(pose['translation']):cmd += [select(p),f'(command "_.MOVE" ki_s "" \'(0 0 0) {pt(pose["translation"])})']
cmd+=['(entmake \'((0 . "LAYER") (2 . "KI_ANNO") (70 . 0) (62 . 7)))']
def label(x,z,s,size=28):
 cmd.append(f'(entmake \'((0 . "TEXT") (8 . "KI_ANNO") (10 {x} {z} 900.0) (40 . {size}) (1 . "{s}") (210 0.0 -1.0 0.0)))')
label(0,3220,'KYOTO INK / TV R13 / SZERELESI NEZET',55)
label(0,3130,'54 LAP / 293 FURAT | 3-4 FRONT KIEMELVE, NEM UZEMI NYITAS',27)
label(0,3070,'TERV - NEM GYARTASI KIADAS | Minden lap sajat ID-retegen',24)
for i,p in enumerate([p for p in parts if p['type']=='TV03-P']):label(850+i*690,2920,p['id'],21)
for i,p in enumerate([p for p in parts if p['type'] in ['TV02-F1','TV02-F2']]):label(p['assembly_box_mm'][0],45,p['id'],21)
label(-430,1960,'TV01 / 10 POLC',25);label(-430,1880,'2 x 5 PANT',25)
label(1520,-80,'3-4: TOLÓAJTÓ-VALTOZAT KULON TERVEN'.encode('ascii','replace').decode(),24)
cmd += ['(command "_.VPOINT" \'(1 -2 1.1))','(command "_.ZOOM" "_E")','(command "_.SHADEMODE" "_G")','(command "_.-VIEW" "_S" "KI_R13_BELSO")','(command "_.SAVEAS" "2018" "/tmp/TV_R13_belso.dwg")']
# Second inspection file: reverse pose, then explode in front/back/side directions.
for p in parts:
 pose=poses[p['id']];cmd += [select(p)]
 if any(pose['translation']):cmd += [f'(command "_.MOVE" ki_s "" \'(0 0 0) {pt([-v for v in pose["translation"]])})']
 if pose['rotation_deg']:cmd += [f'(command "_.ROTATE3D" ki_s "" "_Z" {pt(pose["pivot"])} {-pose["rotation_deg"]})']
 t=p['type'];x,y,z,w,d,h=p['assembly_box_mm'];delta=[0,0,0]
 if t in ['TV01-F','TV02-F1','TV02-F2']:delta[1]=-850
 elif t in ['TV01-H','TV02-H1','TV02-H2','TV03-P','GAP']:delta[1]=450
 elif t in ['TV01-T','TV02-CAP']:delta[2]=180 if z>500 else -100
 elif t in ['TV02-T1','TV02-T2']:delta[2]=-120
 elif t in ['TV01-S','TV02-S']:delta[0]=-100 if x<351 else 100
 elif t=='TV01-C':delta[1]=-180
 elif t in ['TV01-P','TV02-P1','TV02-P2']:delta[1]=-250
 if any(delta):cmd += [f'(command "_.MOVE" ki_s "" \'(0 0 0) {pt(delta)})']
 poses[p['id']]['exploded_translation']=delta
cmd += ['(command "_.ERASE" (ssget "_X" \'((8 . "KI_ANNO"))) "")']
label(0,3300,'KYOTO INK / TV R13 / ROBBANTOTT SZERELESI NEZET',48)
label(0,3210,'Alkatreszek kiemelve. Ez a helyzet nem beépítési méret.'.encode('ascii','replace').decode(),27)
cmd += ['(command "_.ZOOM" "_E")','(command "_.-VIEW" "_S" "KI_R13_ROBBANTOTT")','_.AUDIT','_N','(command "_.SAVEAS" "2018" "/tmp/TV_R13_robbantott.dwg")','_.QUIT','_Y']
Path('/tmp/ki13_views.scr').write_text('\n'.join(cmd)+'\n')
(O/'integration/ki13_views.scr').write_text('\n'.join(cmd)+'\n')
(O/'data/view_poses.json').write_text(json.dumps(poses,ensure_ascii=False,indent=2))
print('54 native STL exports; assembly and exploded scripts ready')
