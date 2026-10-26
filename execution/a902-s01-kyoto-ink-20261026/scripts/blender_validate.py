import bpy,json,math,hashlib,itertools
from pathlib import Path
from mathutils import Vector
P=Path('/Users/peterkapusi/Documents/ChatGPT/WSG – Stíluslabor/execution/a902-s01-kyoto-ink-20261026');D=json.loads((P/'data/design_R02.json').read_text());G=json.loads((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_text());REV=D['revision']
# Hide archived source furniture/styles; source objects are retained in this independent workcopy.
for c in bpy.data.collections:
 if c.name in ['A902_Butor','A902_Falak','A902_Nyilaszarok','A902_Terasz'] or c.name.startswith(('Stil_','VK_')):c.hide_render=True;c.hide_viewport=True
C=bpy.data.collections.new('KI_R02_IMPLEMENTATION');bpy.context.scene.collection.children.link(C)
A=bpy.data.collections.new('KI_R02_LOCKED_SHELL');bpy.context.scene.collection.children.link(A)
def mat(name,col):
 m=bpy.data.materials.new(name);m.diffuse_color=(*col,1);return m
mats={'cab':mat('KI_graphite_matt',(.13,.14,.14)),'pale':mat('KI_chalk_matt',(.67,.62,.54)),'taupe':mat('KI_taupe',(.42,.36,.29)),'shell':mat('KI_existing_shell',(.8,.8,.79)),'wood':mat('KI_light_oak',(.6,.44,.28)),'test':mat('KI_test_zone',(.8,.2,.1))}
objects=[]
def box(name,b,material,coll=C,code=None):
 x,y,z,X,Y,Z=b;verts=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)];faces=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
 mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);mesh.update();o=bpy.data.objects.new(name,mesh);coll.objects.link(o);o.data.materials.append(material);o['revision']=REV
 if code:o['element_id']=code;o['geometry_status']='dimensioned proposal; manufacturer mesh / field survey pending'
 return o
for typ in ['walls','openings']:
 for n,b in G[typ].items():
  o=box('LOCK_'+n,b,mats['shell'],A)
  if 'uveg' in n.lower():o.hide_render=True
  if 'Plafon' in n:o['ceiling']=True
# exact proposal bounds; shell panels, not a solid opaque box representing cabinet interiors.
def bbox(u):
 w=u['w']/1000;d=u['d']/1000
 if u['rot']==90:w,d=d,w
 return [u['x'],u['y'],u['z'],u['x']+w,u['y']+d,u['z']+u['h']/1000]
def addunit(u):
 b=bbox(u);x,y,z,X,Y,Z=b;code=';'.join(u['cost']);m=mats['cab'] if 'grafit' in u['front'] else mats['pale'];name='KI_'+u['id'];parts=[]
 w=u['w']/1000;dd=u['d']/1000;h=u['h']/1000;t=.018;front=u.get('opening_dir','-y')
 def local(suf,bb,mm=m):
  aa,vv,zz,AA,VV,ZZ=bb
  if front=='+x':gb=[X-VV,y+aa,z+zz,X-vv,y+AA,z+ZZ]
  elif front=='-x':gb=[x+vv,y+aa,z+zz,x+VV,y+AA,z+ZZ]
  elif front=='+y':gb=[x+aa,Y-VV,z+zz,x+AA,Y-vv,z+ZZ]
  else:gb=[x+aa,y+vv,z+zz,x+AA,y+VV,z+ZZ]
  o=box(name+'_'+suf,gb,mm,code=code);parts.append(o);return o
 if u['kind'] in ['panel','upholstery','table','bench','shelf']:
  if u['kind']=='panel' and len(u['modules'])>1:
   pos=0
   for j,mod in enumerate(u['modules']):local('panel'+str(j),[pos+.0015,0,0,pos+mod/1000-.0015,dd,h]);pos+=mod/1000
  else:parts=[box(name,b,m,code=code)]
 elif u['id']=='K-04':
  # Dishwasher is a 600 mm clear opening: no enclosing side panels stealing36mm.
  local('SMV4EVX00E',[.001,.019,0,.599,.569,.815],mats['shell']);local('front',[.0015,0,.08,w-.0015,.019,.815])
 else:
  for suf,bb in [('bottom',[0,.019,0,w,dd,t]),('top',[0,.019,h-t,w,dd,h]),('sideL',[0,.019,0,t,dd,h]),('sideR',[w-t,.019,0,w,dd,h]),('back',[t,dd-.008,t,w-t,dd,h-t])]:local(suf,bb)
  if u['id']=='K-01':
   for j,zz in enumerate([.582,1.262,1.8]):local('shelf'+str(j),[t,.019,zz,w-t,dd,zz+t])
   for label,zz,hh,depth in [('HBA534EB3',.6,.595,.548),('BFL524MB0',1.28,.382,.317)]:local(label,[.003,0,zz,.597,depth,zz+hh],mats['cab'])
   for j,(lo,hi) in enumerate([(.08,.58),(1.198,1.259),(1.665,h)]):local('front'+str(j),[.0015,0,lo,w-.0015,.019,hi-.0015])
  elif u['id']=='K-02':
   local('shelf',[t,.019,1.87,w-t,dd,1.888])
   for j,(lo,hi) in enumerate([(.08,.7),(.7,1.852),(1.852,h)]):local('front'+str(j),[.0015,0,lo+.0015,w-.0015,.019,hi-.0015])
  else:
   pos=0
   wardrobe=u['id'].startswith(('WN-','WS-','W52','W53'))
   for j,mod in enumerate(u['modules']):
    mw=mod/1000
    if j:local('partition'+str(j),[pos-t/2,.019,t,pos+t/2,dd,h-t])
    if wardrobe:
     for lo,hi in [(0,2.36),(2.36,h)]:local('front'+str(j)+'_'+str(lo),[pos+.0015,0,lo+.0015,pos+mw-.0015,.019,hi-.0015])
    else:
     n=max(1,round(u['drawers']/len(u['modules'])))
     for k in range(n):local('front'+str(j)+'_'+str(k),[pos+.0015,0,k*h/n+.0015,pos+mw-.0015,.019,(k+1)*h/n-.0015])
    pos+=mw
   if u.get('interior'):
    local('fixed_loft',[t,.019,2.342,w-t,dd-.008,2.36])
    for v in u['interior']:
     bi=v['bay']-1;start=sum(u['modules'][:bi])/1000;mw=u['modules'][bi]/1000
     for j,zzmm in enumerate(v['shelves_mm']):local('bay'+str(bi)+'_shelf'+str(j),[start+t,.019,zzmm/1000,start+mw-t,dd-.008,zzmm/1000+t])
     for j,zzmm in enumerate(v['rails_mm']):
      if dd<.55:bb=[start+mw/2-.012,.08,zzmm/1000,start+mw/2+.012,dd-.04,zzmm/1000+.024]
      else:bb=[start+t,dd/2-.012,zzmm/1000,start+mw-t,dd/2+.012,zzmm/1000+.024]
      local('bay'+str(bi)+'_rail'+str(j),bb,mats['cab'])
     for j in range(v['drawers']):local('bay'+str(bi)+'_drawer'+str(j),[start+.035,.04,.1+j*.18,start+mw-.035,dd-.05,.26+j*.18],mats['wood'])
   else:
    for j in range(u['shelves']):
     zz=(j+1)*h/(u['shelves']+1);local('shelf'+str(j),[t,.019,zz,w-t,dd-.008,zz+t])
 objects.append(dict(id=u['id'],element=code,bounds=b,blender_objects=[o.name for o in parts],kind=u['kind'],status=u['status']))
for u in D['units']:addunit(u)
for it in D['items']:
 b=bbox(it);m=mats['taupe'] if it['id'].startswith(('KI-036','KI-043','KI-058','KI-070')) else mats['wood'];name='KI_'+it['id'];parts=[]
 if it['kind']=='sofa':
  # dimension-faithful L envelope; detailed upholstery/module hand is still a manufacturer gate.
  x,y,z,X,Y,Z=b
  parts=[box(name+'_backrun',[X-1.23,y,z,X,Y,Z],m,code=it['id']),box(name+'_chaise',[x,y,z,X-1.23,y+1.23,Z],m,code=it['id'])]
 elif it['kind']=='oval':
  x,y,z,X,Y,Z=b;verts=[];faces=[]
  for zz in [Z-.025,Z]:
   for k in range(64):a=2*math.pi*k/64;verts.append(((x+X)/2+(X-x)/2*math.cos(a),(y+Y)/2+(Y-y)/2*math.sin(a),zz))
  faces.extend([tuple(range(63,-1,-1)),tuple(range(64,128))]);faces.extend([(k,(k+1)%64,(k+1)%64+64,k+64) for k in range(64)]);mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);o=bpy.data.objects.new(name,mesh);C.objects.link(o);o.data.materials.append(m);parts=[o,box(name+'_base',[x+.15,y+.3,z,X-.15,Y-.3,Z-.025],m,code=it['id'])]
 else:parts=[box(name,b,m,code=it['id'])]
 objects.append(dict(id=it['id'],element=it['id'].split('-')[0]+'-'+it['id'].split('-')[1],bounds=b,blender_objects=[o.name for o in parts],kind=it['kind'],status=it['proof']))
# Existing sanitary items are explicitly included, with source-model limitations retained.
for it in D.get('fixed_existing',[]):
 o=box('KI_'+it['id'],it['bounds'],mats['shell'],code=it['cost'])
 objects.append(dict(id=it['id'],element=it['cost'],bounds=it['bounds'],blender_objects=[o.name],kind='existing',status=it['status']))
# Visible threshold is explicitly uncertain; not silently erased or labelled measured.
box('KI_THRESHOLD_PENDING',[4.44,7.95,0,8.94,8.18,.12],mats['test'],code='SURVEY-THRESHOLD')['measurement_status']='120mm illustrative survey marker; actual height and extent unknown'
# Camera numbers retain exact lock transforms. New QA cameras get new names.
for n,c in G['cameras'].items():
 o=bpy.data.objects.get(n)
 if not o:o=bpy.data.objects.new(n,bpy.data.cameras.new(n));C.objects.link(o)
 o.location=c['loc'];o.rotation_euler=c['rot'];o.data.type=c['tipus'];o.data.lens=c['lens_mm'];o.data.shift_y=c['shift_y'];o.data.ortho_scale=c['ortho_scale'];o['source']='geometry_lock_A902_v2b';o['status']=c['statusz']
for c in D.get('new_cameras',[]):
 o=bpy.data.objects.new(c['id'],bpy.data.cameras.new(c['id']));C.objects.link(o);o.location=c['location'];o.rotation_euler=(Vector(c['target'])-o.location).to_track_quat('-Z','Y').to_euler();o.data.lens=c['lens_mm'];o['status']=c['status'];o['revision']=REV
# FADO is a dimension study, not a downloaded manufacturer mesh.
for suffix,yy in [('L',5.27),('R',7.5)]:
 bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=.125,location=(3.28,yy,.57));o=bpy.context.object;o.name='KI_KI-117_FADO_'+suffix;o.scale.z=.96
 for old in list(o.users_collection):old.objects.unlink(o)
 C.objects.link(o);o.data.materials.append(mats['pale']);o['element_id']='KI-117';o['geometry_status']='FADO diameter250 H240 envelope, base simplification; Hue lamp fit pending'
# Inspection mesh list is saved with actual object IDs.
def overlap(a,b,tol=.005):return all(min(a[i+3],b[i+3])-max(a[i],b[i])>tol for i in range(3))
wallhits=[];pairhits=[]
for o in objects:
 for n,b in G['walls'].items():
  if not n.startswith('Plafon') and overlap(o['bounds'],b):wallhits.append({'item':o['id'],'wall':n,'status':'REVIEW_REQUIRED'})
for a,b in itertools.combinations(objects,2):
 if a['id']==b['id'] or (a['id'].startswith('TV') and b['id'].startswith('TV')):continue
 if {a['id'],b['id']}=={'KI-091','EX-SHOWER62'}:continue
 if overlap(a['bounds'],b['bounds']):pairhits.append({'a':a['id'],'b':b['id'],'status':'AABB_REVIEW; actual solids/working positions need interpretation'})
from mathutils import Vector
def ob_bounds(name):
 o=bpy.data.objects[name];v=[o.matrix_world@Vector(c) for c in o.bound_box];return [min(vv[i] for vv in v) for i in range(3)]+[max(vv[i] for vv in v) for i in range(3)]
bpy.context.view_layer.update()
for hit in pairhits:
 aa=next(o for o in objects if o['id']==hit['a']);bb=next(o for o in objects if o['id']==hit['b'])
 hit['component_overlap']=any(overlap(ob_bounds(a),ob_bounds(b)) for a in aa['blender_objects'] for b in bb['blender_objects'])
 if not hit['component_overlap']:hit['status']='BROAD_PHASE_ONLY: no component-box overlap in current simplified model'
# Swept room-door leaf in 5-degree increments, using actual half-plane from lock.
doorhits=[]
for n,m in G['openings_meta'].items():
 if m.get('tipus') not in ['nyilo','nyilo+fix'] or not m.get('zsaner'):continue
 hx,hy=m['zsaner'];r=m['r'];axis=m['fal'];lo,hi=m['nyilas'];closed=(lo-hx,0) if axis=='x' and abs(hx-hi)<.05 else ((hi-hx,0) if axis=='x' else (0,lo-hy if abs(hy-hi)<.05 else hi-hy))
 base=math.atan2(closed[1],closed[0]);direction=m['irany'];normal={'+x':(1,0),'-x':(-1,0),'+y':(0,1),'-y':(0,-1)}[direction];sign=1 if math.cos(base+math.pi/2)*normal[0]+math.sin(base+math.pi/2)*normal[1]>0 else -1
 for o in objects:
  b=o['bounds']
  if b[2]>=2.1:continue
  hit=False
  for deg in range(0,91,5):
   a=base+sign*math.radians(deg)
   for step in range(1,31):
    xx=hx+r*step/30*math.cos(a);yy=hy+r*step/30*math.sin(a)
    if b[0]-.02<xx<b[3]+.02 and b[1]-.02<yy<b[4]+.02:hit=True;break
   if hit:break
  if hit:doorhits.append({'door':n,'item':o['id'],'angle_deg':deg,'status':'FAIL_CLEARANCE'})
checks=[dict(id='KITCHEN_AISLE',measured_mm=round((9.93-9.09)*1000),target_mm=900,status='FAIL_TARGET',note='R02 west origin8.47 +620 =9.09; 840mm. Nominal wall-to-wall2100 minus2×620=860 before20mmsetback.'),dict(id='NORTH_WARDROBE',available_mm=3020,cabinet_mm=2920,margin_mm=100,status='CONDITIONAL',note='plan clear100mm; finished walls and installation sequence not measured'),dict(id='TERRACE_OPEN_SASH',status='UNRESOLVED',note='lock says sliding; exact operable bay and threshold field survey absent'),dict(id='NORDLI_DRAWERS',status='UNRESOLVED',note='factory drawer travel not imported; full opening cannot be certified'),dict(id='DINING_PULL_OUT',status='UNRESOLVED',note='six Eamy closed envelopes imported; chair pullout and continuous route need reviewed swept test'),dict(id='PRODUCT_IDENTITY',status='NOT_VALIDATED',note='dimension models are not certified manufacturer meshes'),dict(id='TERRACE_LOAD',status='NOT_TESTED',note='geometry cannot validate structure, crane, waterproofing or electrical supply')]
movement=[]
for it in D['items']:
 if not it['id'].startswith('KI-029-'):continue
 b=bbox(it);n=int(it['id'].split('-')[-1]);dx,dy=(-.37,0) if n<=2 else ((.37,0) if n<=4 else ((0,-.37) if n==5 else (0,.37)))
 sweep=[min(b[0],b[0]+dx),min(b[1],b[1]+dy),b[2],max(b[3],b[3]+dx),max(b[4],b[4]+dy),b[5]]
 hits=[o['id'] for o in objects if o['id']!=it['id'] and overlap(sweep,o['bounds'])]
 walls=[n for n,wb in G['walls'].items() if not n.startswith('Plafon') and overlap(sweep,wb)]
 movement.append(dict(id=it['id'],type='370mm chair translation; 900mm use zone from table edge, not a separate route',swept_bounds=sweep,hits=hits,walls=walls,status='REVIEW' if hits or walls else 'CLEAR_AT_ASSUMED_370MM'))
checks=[c for c in checks if c['id']!='DINING_PULL_OUT']
checks.append(dict(id='DINING_PULL_OUT',status='SAMPLED_TRANSLATION_ONLY',note='six chairs translated370mm away from table; results in movement_checks. No separate route claimed between sofa and west chairs. Knee space and manufacturer shape pending.'))
checks.append(dict(id='DISHWASHER_OPEN',status='CONDITIONAL_RESTRICTED_AISLE',note='Factory open depth1150 minus550 closed =600mm additional projection. 840mm aisle leaves240mm: no through passage with dishwasher open.'))
checks.append(dict(id='BATH_LAUNDRY',status='UNRESOLVED_USE_CONFLICT',note='Existing bathtub now included; tower moved to3.80/.95. Open machine vs open bathroom door and basin use needs manufacturer sweep and site survey.'))
report=dict(revision=REV,blender_version=bpy.app.version_string,source_file=bpy.data.filepath,source_sha256=hashlib.sha256(Path(bpy.data.filepath).read_bytes()).hexdigest(),geometry_lock_sha256=hashlib.sha256((P/'sources/original/03_blender/geometry_lock_A902_v2b.json').read_bytes()).hexdigest(),method='AABB wall/pair screen + room door sampled5degrees/30 radialpoints. Not complete collision/egress certification.',status='OPEN_ISSUES_NOT_FINAL_RENDER_READY',wall_collisions=wallhits,pair_overlaps=pairhits,door_sweeps=doorhits,movement_checks=movement,checks=checks,objects=objects)
(P/'blender/validation_R02.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('VALIDATION',len(wallhits),'walls',len(pairhits),'pairs',len(doorhits),'doorhits')
scene=bpy.context.scene;scene.render.engine='BLENDER_WORKBENCH';scene.display.shading.light='FLAT';scene.display.shading.color_type='MATERIAL';scene.display.shading.show_shadows=False;scene.view_settings.view_transform='Standard';scene.view_settings.exposure=0;scene.view_settings.gamma=1;scene.display.shading.show_cavity=True;scene.render.resolution_x=1440;scene.render.resolution_y=900;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='PNG';scene.world.color=(.7,.7,.7)
scene['KI_status']='R02 proposal with open collision/identity gates; not approved construction';scene['KI_revision']=REV
scene.camera=bpy.data.objects['Cam_12_Nappali_Hero']
bpy.ops.wm.save_as_mainfile(filepath=str(P/'blender/A902_Kyoto_Ink_R02.blend'),compress=True)
for cam,out,top in [('Cam_06_Alaprajz_lakas','QA_lakas_top',True),('Cam_09_Terasz_v2_felulnezet','QA_terasz_top',True),('Cam_02_Nappali_terasz','QA_Cam02',False),('Cam_12_Nappali_Hero','QA_Cam12',False)]:
 for o in A.objects:
  if o.get('ceiling'):o.hide_render=top
 scene.camera=bpy.data.objects[cam];scene.render.filepath=str(P/'blender'/f'{out}.png');bpy.ops.render.render(write_still=True)
scene.render.resolution_x=960;scene.render.resolution_y=600
camera_records=[]
for cam in ['Cam_03_Etkezo_konyha','Cam_04_Master','Cam_10_Furdo_06_2','Cam_07_Terasz_v2_greslaprol']+[c['id'] for c in D.get('new_cameras',[])]:
 scene.camera=bpy.data.objects[cam];scene.render.filepath=str(P/'blender'/f'QA_{cam}.png');bpy.ops.render.render(write_still=True)
 o=scene.camera;camera_records.append(dict(camera_id=cam,location=list(o.location),rotation_euler=list(o.rotation_euler),lens_mm=o.data.lens,shift_y=o.data.shift_y,image='blender/QA_'+cam+'.png',status='rendered neutral dimensional study, identity/detail not final'))
(P/'blender/camera_runs_R02.json').write_text(json.dumps(camera_records,ensure_ascii=False,indent=2))
print('COMPLETE_R02')
