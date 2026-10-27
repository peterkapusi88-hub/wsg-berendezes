"""Run with CP3 blend as read-only input; save independent R04 proposals."""
import bpy,json,math,hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'R04';B=O/'blender';B.mkdir(exist_ok=True)
source=Path(bpy.data.filepath);source_hash=hashlib.sha256(source.read_bytes()).hexdigest()
C=bpy.data.collections.new('KI_R04_PROPOSALS_NOT_APPROVED');bpy.context.scene.collection.children.link(C)
def material(n,color):
 m=bpy.data.materials.new(n);m.diffuse_color=(*color,1);return m
cream=material('R04_matt_greige_SAMPLE_REQUIRED',(.63,.58,.50));core=material('R04_interior',(.78,.75,.68));dark=material('R04_graphite_SAMPLE_REQUIRED',(.12,.115,.105));light=material('R04_LED_position_NOT_photometry',(1,.45,.1));bike=material('R04_bike_ENVELOPE',(.55,.18,.12))
allparts=[];checks=[];unitparts={};faceparts=[]
def box(n,bb,mat,uid,kind):
 x,y,z,X,Y,Z=bb
 if min(X-x,Y-y,Z-z)<=0:raise ValueError((n,bb))
 vs=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)];fs=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
 mesh=bpy.data.meshes.new(n);mesh.from_pydata(vs,[],fs);ob=bpy.data.objects.new(n,mesh);C.objects.link(ob);ob.data.materials.append(mat);ob['element_id']=uid;ob['revision']='KI-R04';ob['status']='PROPOSAL';ob['part_kind']=kind
 allparts.append(ob);unitparts.setdefault(uid,[]).append(ob.name);return ob

def tr(u,a,d,z):
 x,y,zz=u['x'],u['y'],u['z'];w=u['w']/1000;dep=u['d']/1000;di=u.get('opening_dir','-y')
 return (x+dep-d,y+a,zz+z) if di=='+x' else (x+d,y+a,zz+z) if di=='-x' else (x+a,y+dep-d,zz+z) if di=='+y' else (x+a,y+d,zz+z)
def part(u,name,bb,m,kind='structure'):
 aa=tr(u,*bb[:3]);ab=tr(u,*bb[3:]);b=[min(aa[i],ab[i]) for i in range(3)]+[max(aa[i],ab[i]) for i in range(3)]
 ob=box('R04_'+u['id']+'_'+name,b,m,u['id'],kind);ob['cost_ids']=';'.join(u['cost']);return ob
units=[json.loads((O/'data/WN-01_R04A_alternative.json').read_text()),json.loads((O/'data/B62-01_R04A_alternative.json').read_text())]+json.loads((O/'data/TV_R04A_frontjavaslat.json').read_text())
for u in units:
 old=u['id'].split('-R04')[0]
 for ob in bpy.data.objects:
  if ob.name.startswith(('CP3_'+old+'_','KI_'+old+'_')):ob.hide_render=True;ob.hide_viewport=True
 w,dep,h=[u[k]/1000 for k in ['w','d','h']]
 for b in u['cp3_bays']:
  x=b['offset']/1000;mw=b['module_w']/1000;cw=b['clear_w']/1000;cd=b['clear_d']/1000;bid='B'+str(b['bay'])
  for name,bb in [('L',[x,.019,0,x+.018,dep,h]),('R',[x+mw-.018,.019,0,x+mw,dep,h]),('bottom',[x+.018,.019,0,x+mw-.018,dep,.018]),('top',[x+.018,.019,h-.018,x+mw-.018,dep,h]),('back',[x+.018,dep-.038,.018,x+mw-.018,dep-.03,h-.018])]:part(u,bid+name,bb,core)
  for j,z in enumerate(b['shelves_mm']):part(u,bid+'shelf'+str(j),[x+.018,.019,z/1000,x+mw-.018,.019+cd,(z+18)/1000],core)
  for j,z in enumerate(b['rails_mm']):
   length=b['rod_lengths_mm'][j]/1000
   part(u,bid+'rod'+str(j),[x+(mw-length)/2,dep/2-.012,z/1000,x+(mw+length)/2,dep/2+.012,(z+24)/1000],dark,'rod')
  for j,z in enumerate(b['lights_mm']):
   ln=u.get('fixture_length',min(460,b['clear_w']-50))/1000
   part(u,bid+'light'+str(j),[x+(mw-ln)/2,.04,z/1000,x+(mw+ln)/2,.055,(z+8)/1000],light,'light_position')
  for j,z in enumerate(b['drawer_z']):
   dw,dd,dh=[v/1000 for v in b['drawer_inner_mm']];dx=x+(mw-dw)/2;zz=z/1000
   # Not a made-up siphon cutout: keep explicit exclusion volume separate.
   for lab,bb in [('floor',[dx,.04,zz,dx+dw,.04+dd,zz+.012]),('left',[dx-.012,.04,zz,dx,.04+dd,zz+dh]),('right',[dx+dw,.04,zz,dx+dw+.012,.04+dd,zz+dh]),('rear',[dx,.04+dd,zz,dx+dw,.052+dd,zz+dh])]:part(u,bid+f'drawer{j}'+lab,bb,core,'drawer')
   if old=='WN-01':part(u,bid+f'drawer{j}front',[x+.03,.019,zz-.008,x+mw-.03,.038,zz+dh+.02],cream,'inner_drawer_front')
   checks.append({'check':b['id']+f'/drawer{j}/vertical_envelope','result':'PASS' if z+b['drawer_inner_mm'][2]+20<u['h'] else 'FAIL','scope':'algebraic height only, not certified runner geometry'})
  checks.append({'check':b['id']+'/positive_clearance','result':'PASS' if cw>0 and cd>0 else 'FAIL','scope':'nominal compartment only'})
 off=0
 for j,mwmm in enumerate(u['front_modules']):
  mw=mwmm/1000
  ob=part(u,'visible_front_'+str(j),[off+.0015,0,.0015,off+mw-.0015,.019,h-.0015],dark if old.startswith(('TV','B62')) else cream,'visible_front');faceparts.append(ob);off+=mw
 checks.append({'check':u['id']+'/front_sum','result':'PASS' if abs(off-w)<1e-6 else 'FAIL','scope':'front module widths sum to overall design width'})
 if old=='B62-01':checks.append({'check':u['id']+'/siphon','result':'OPEN','scope':'current drawer box is an envelope; exact cutout pending basin and trap. Not usable capacity proof.'})
 if old=='WN-01':checks.append({'check':u['id']+'/lift_and_hinge_motion','result':'OPEN','scope':'no supplier motion mesh; closed/open-front cutaway only. No operating-sweep PASS.'})
# Storage move: retain both racks, move second 50 mm, delete only old luggage placeholder.
for ob in bpy.data.objects:
 if ob.name.startswith('CP3_T-R2_'):ob.location.x-=.05;ob['revision']='R04 storage proposal'
 if ob.name=='CP3_T-LUG':ob.hide_render=True;ob.hide_viewport=True
box('R04_T026_bicycle_PLANNING_ENVELOPE',[28.75,.05,0,29.45,1.2,2],bike,'T-0-26','unmeasured_bicycle_envelope')
# Unambiguous numerical test, touching boundaries are reported separately.
checks += [
 {'check':'T026/rack2_bike','result':'CONTACT_NO_MARGIN','scope':'rack2 xmax=28.750; bike xmin=28.750. No solid overlap in design boxes, zero spare clearance. Actual hardware and movement unresolved.'},
 {'check':'T026/access','result':'OPEN','scope':'door not surveyed; bicycle extraction/turning path not validated'},
 {'check':'AT8/freezer','result':'OPEN','scope':'exact appliance EAN, vent clearance and usable opening unknown'},
 {'check':'CP3/inherited_issues','result':'OPEN','scope':'Kitchen aisle 840mm, open dishwasher route, 05.3 bed/chair and master bedside/bed drawer conflict remain from CP3. This script does not resolve them.'},
 {'check':'Surface_identity','result':'OPEN','scope':'plain material placeholders; no approved ink art or calibrated swatches. Not final appearance render.'}]
S=bpy.context.scene;S.render.engine='BLENDER_WORKBENCH';S.display.shading.light='STUDIO';S.display.shading.color_type='MATERIAL';S.display.shading.show_cavity=True;S.view_settings.view_transform='Standard';S.render.resolution_x=1400;S.render.resolution_y=1100;S.render.resolution_percentage=100;S.render.image_settings.file_format='PNG'
visibility={o.name:o.hide_render for o in bpy.data.objects if o.type=='MESH'};renders=[]
for u in units:
 uid=u['id'];w,dep,h=[u[k]/1000 for k in ['w','d','h']];center=Vector(tr(u,w/2,dep/2,h/2));out=Vector({'+x':(1,0,0),'-x':(-1,0,0),'+y':(0,1,0),'-y':(0,-1,0)}[u.get('opening_dir','-y')]);side=Vector((-out.y,out.x,0))
 cam=bpy.data.objects.new('R04_camera_'+uid,bpy.data.cameras.new('R04_camera_'+uid));C.objects.link(cam);cam.location=center+out*5+side*1.5+Vector((0,0,1.5));cam.rotation_euler=(center-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=max(w*1.6,h*1.6,1.3);S.camera=cam
 for state in ['closed','cutaway']:
  for ob in bpy.data.objects:
   if ob.type=='MESH':ob.hide_render=ob.name not in unitparts[uid] or (state=='cutaway' and ob.get('part_kind')=='visible_front')
  dest=B/(uid+'_'+state+'.png');S.render.filepath=str(dest);bpy.ops.render.render(write_still=True)
  renders.append({'unit':uid,'state':state,'file':dest.name,'status':'native dimensional study; cutaway removes fronts, does not simulate opening'})
for n,hide in visibility.items():bpy.data.objects[n].hide_render=hide
S.camera=bpy.data.objects.get('Cam_12_Nappali_Hero',S.camera)
bpy.ops.wm.save_as_mainfile(filepath=str(B/'A902_Kyoto_Ink_R04_javaslat.blend'),compress=True)
(B/'checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));(B/'render_manifest.json').write_text(json.dumps(renders,ensure_ascii=False,indent=2));(B/'object_register.json').write_text(json.dumps(unitparts,ensure_ascii=False,indent=2));(B/'source.json').write_text(json.dumps({'input':str(source),'sha256':source_hash,'revision':'KI-R04_PROPOSAL','source_unchanged':hashlib.sha256(source.read_bytes()).hexdigest()==source_hash},indent=2))
print('R04_SAVED',len(allparts),'objects',len(renders),'native studies',len(checks),'checks and open conditions')
