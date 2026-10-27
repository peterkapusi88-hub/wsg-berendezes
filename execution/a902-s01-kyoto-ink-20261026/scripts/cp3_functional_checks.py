import bpy,json,math,hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'CP3';S=bpy.context.scene;D=json.loads((O/'data/design_CP3.json').read_text());G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text())
checks=json.loads((O/'blender/checks.json').read_text());runs=json.loads((O/'blender/render_runs.json').read_text())
alt=bpy.data.collections.new('CP3_ALT053_MALM_UNAPPROVED');S.collection.children.link(alt)
def box(n,b):
 x,y,z,X,Y,Z=b;v=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)];f=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)];me=bpy.data.meshes.new(n);me.from_pydata(v,[],f);ob=bpy.data.objects.new(n,me);alt.objects.link(ob);ob.data.materials.append(bpy.data.materials['CP3_warm_white']);ob['proposal']='not owner approved';return ob
box('ALT053_MALM_20404806',[12.225,4.15,0,14.325,5.9,.38]);box('ALT053_MALM_HEAD',[14.275,4.15,.38,14.325,5.9,1]);box('ALT053_mattress160',[12.275,4.225,.38,14.275,5.825,.6]);box('ALT053_CHAIR_WORK',[12.88,6.7,0,13.59,7.41,.9]);box('ALT053_CHAIR_WITHDRAWN',[12.88,6.1,0,13.59,6.81,.9]).hide_render=True
testboxes={'bed':[12.225,4.15,14.325,5.9],'chair_work':[12.88,6.7,13.59,7.41],'chair_withdrawn':[12.88,6.1,13.59,6.81],'desk':[12.95,7.3,14.15,8.0]}
def hitdoor(meta,b):
 hx,hy=meta['zsaner'];rad=meta['r']
 if meta['fal']=='y':vx=0;vy=meta['nyilas'][0]-hy if abs(meta['nyilas'][0]-hy)>.001 else meta['nyilas'][1]-hy;ex=1 if meta['irany']=='+x' else -1;ey=0
 else:vy=0;vx=meta['nyilas'][0]-hx if abs(meta['nyilas'][0]-hx)>.001 else meta['nyilas'][1]-hx;ey=1 if meta['irany']=='+y' else -1;ex=0
 ll=math.hypot(vx,vy);vx/=ll;vy/=ll
 for deg in range(0,91,2):
  a=math.radians(deg)
  for k in range(1,101):
   x=hx+rad*k/100*(vx*math.cos(a)+ex*math.sin(a));y=hy+rad*k/100*(vy*math.cos(a)+ey*math.sin(a))
   if b[0]<x<b[2] and b[1]<y<b[3]:return True
 return False
for dn in ['Ajto_05_3','Ajto_06_2','Uvegfal_05_3_terasz']:
 for name,b in testboxes.items():checks.append(dict(check='ALT053 '+dn+' / '+name,result='FAIL' if hitdoor(G['openings_meta'][dn],b) else 'PASS',detail='2° angular / 100 radial sample points; source door geometry; no field clearance guarantee'))
checks.append(dict(check='ALT053 chair withdrawn / bed',result='PASS',detail='Chair y_min6.10 - bed y_max5.90 =200 mm; this is separation, not a walking route. Main passage west of the work area.'))
checks.append(dict(check='ALT053 effect',result='OWNER_DECISION',detail='NORDLI180 → MALM160 lifting storage: 20 cm narrower mattress; 219900 vs189900 Ft frame, +30000 Ft; mattress160 replacing180 needs exact quote. Wardrobe unchanged. Lifted-bed headroom / mattress mass still manufacturer gate.'))
checks.append(dict(check='Master NORDLI drawers / nightstands',result='FAIL',detail='NT-L/NT-R footprint crosses the head-end side-drawer zones. Full six-drawer usability is not proved. Alternative floating 300×420×180 bedside box bottom320 mm needs design acceptance; no automatic loss of two-drawer bedside capacity.'))
altdata=dict(id='ALT053',accepted=False,bed_sku='204.048.06',bed_mm=[2100,1750,1000],mattress_mm=[2000,1600],bed_price=219900,frame_delta=30000,mattress_price_status='existing mattress allowance retained only as estimate; exact160 SKU needed',source='https://www.ikea.com/hu/hu/p/malm-agynemutartos-agy-feher-20404806/',date='2026-10-27',placements=testboxes,wardrobe_loss_mm=0)
(O/'data/alternative_053.json').write_text(json.dumps(altdata,ensure_ascii=False,indent=2))
saved={o.name:o.hide_render for o in bpy.data.objects if o.type=='MESH'}
for o in bpy.data.objects:
 if o.name.startswith(('KI_KI-070','KI_KI-075')):o.hide_render=True
cc=bpy.data.objects.new('CP3_ALT053_TOP',bpy.data.cameras.new('CP3_ALT053_TOP'));alt.objects.link(cc);cc.location=(12.6,6.05,12);cc.rotation_euler=(0,0,0);cc.data.type='ORTHO';cc.data.ortho_scale=5.5
for ob in bpy.data.objects:
 if ob.get('ceiling'):ob.hide_render=True
S.camera=cc;S.render.engine='BLENDER_WORKBENCH';S.render.filepath=str(O/'blender/ALT053_top.jpg');bpy.ops.render.render(write_still=True)
for n,v in saved.items():bpy.data.objects[n].hide_render=v
alt.hide_render=True;alt.hide_viewport=True
# Actual light transport test. No manufacturer IES exists here: intentionally no lux claim.
saved={o.name:o.hide_render for o in bpy.data.objects if o.type=='MESH'}
for ob in bpy.data.objects:
 if ob.type=='MESH':ob.hide_render=not ob.name.startswith('CP3_WN-01_') or ob.get('part_kind')=='front'
S.camera=bpy.data.objects['CP3_F01'];S.render.engine='CYCLES';S.cycles.device='CPU';S.cycles.samples=24;S.cycles.use_denoising=True;S.render.resolution_x=900;S.render.resolution_y=760
S.world.use_nodes=True;bg=S.world.node_tree.nodes.get('Background');oldbg=bg.inputs['Strength'].default_value;bg.inputs['Strength'].default_value=.03
S.render.filepath=str(O/'blender/WN_loaded_light_cycles.jpg');bpy.ops.render.render(write_still=True)
checks.append(dict(check='WN loaded light transport test',result='CONDITIONAL',detail='Cycles CPU24 samples; dark clothes80% illustrative occupancy; actual emission surfaces at planned shelf fronts. No IES, calibrated luminous flux or confirmed CRI: only shadow/layout diagnostic, not illuminance acceptance.'))
for n,v in saved.items():bpy.data.objects[n].hide_render=v
bg.inputs['Strength'].default_value=oldbg;S.render.engine='BLENDER_WORKBENCH';S.camera=bpy.data.objects['Cam_12_Nappali_Hero'];S.render.resolution_x=960;S.render.resolution_y=640
bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_CP3.blend'),compress=True)
(O/'blender/checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));(O/'blender/reopen_check.json').write_text(json.dumps(dict(opened_from=str(bpy.data.filepath),objects=len(bpy.data.objects),cp3_objects=sum(o.name.startswith('CP3_') for o in bpy.data.objects),alternative053=True,native_cycles_test=True,status='opened and saved successfully; geometric limitations in checks.json'),ensure_ascii=False,indent=2))
print('CP3_REOPEN_AND_FUNCTION_TESTS_DONE')
