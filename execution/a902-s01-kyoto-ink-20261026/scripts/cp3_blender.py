"""Run only against the independent R02 .blend. Writes CP3 outputs."""
import bpy,json,math,hashlib,itertools
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'CP3';D=json.loads((O/'data/design_CP3.json').read_text());REV=D['revision']
C=bpy.data.collections.new('KI_CP3_INTERIORS');bpy.context.scene.collection.children.link(C)
def mat(n,c,emit=0):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*c,1);p.inputs['Roughness'].default_value=.7
 if emit:p.inputs['Emission Color'].default_value=(*c,1);p.inputs['Emission Strength'].default_value=emit
 return m
M={'wood':mat('CP3_warm_white',(.71,.67,.58)),'front':mat('CP3_chalk',(.59,.54,.46)),'dark':mat('CP3_graphite',(.1,.11,.105)),'led':mat('CP3_LED_proxy_not_photometry',(1,.7,.35),4),'cloth':mat('CP3_dark_cloth',(.16,.18,.2)),'storage':mat('CP3_storage_white',(.86,.87,.84))}
records=[];fronts=[];drawers=[];lifts=[];unitparts={}
def box(n,b,m,code,kind='part'):
 x,y,z,X,Y,Z=b
 if min(X-x,Y-y,Z-z)<=0:raise ValueError((n,b))
 verts=[(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)];faces=[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]
 mesh=bpy.data.meshes.new(n);mesh.from_pydata(verts,[],faces);mesh.update();o=bpy.data.objects.new(n,mesh);C.objects.link(o);o.data.materials.append(m);o['element_id']=code;o['revision']=REV;o['part_kind']=kind;return o
def bounds(u):
 w,d=u['w']/1000,u['d']/1000
 if u['rot']==90:w,d=d,w
 return [u['x'],u['y'],u['z'],u['x']+w,u['y']+d,u['z']+u['h']/1000]
def transform(u,v):
 a,dep,z=v;x,y,zz,X,Y,Z=bounds(u);dr=u.get('opening_dir','-y')
 return (X-dep,y+a,zz+z) if dr=='+x' else (x+dep,y+a,zz+z) if dr=='-x' else (x+a,Y-dep,zz+z) if dr=='+y' else (x+a,y+dep,zz+z)
def outward(u):return Vector({'+x':(1,0,0),'-x':(-1,0,0),'+y':(0,1,0),'-y':(0,-1,0)}[u.get('opening_dir','-y')])
def local(u,n,b,m,kind='part'):
 a=transform(u,b[:3]);z=transform(u,b[3:]);bb=[min(a[i],z[i]) for i in range(3)]+[max(a[i],z[i]) for i in range(3)]
 o=box('CP3_'+u['id']+'_'+n,bb,m,';'.join(u['cost']),kind);unitparts.setdefault(u['id'],[]).append(o.name);return o
for u in D['units']:
 if not u['cp3_bays']:continue
 for o in bpy.data.objects:
  if o.name.startswith('KI_'+u['id']+'_') or o.name=='KI_'+u['id']:o.hide_render=True;o.hide_viewport=True
 w,dep,h=u['w']/1000,u['d']/1000,u['h']/1000
 for b in u['cp3_bays']:
  x=b['offset']/1000;mw=b['module_w']/1000;cw=b['clear_w']/1000;cd=b['clear_d']/1000;bid='B'+str(b['bay'])
  for label,bb in [('left',[x,.019,0,x+.018,dep,h]),('right',[x+mw-.018,.019,0,x+mw,dep,h]),('base',[x+.018,.019,0,x+mw-.018,dep,.018]),('top',[x+.018,.019,h-.018,x+mw-.018,dep,h]),('back',[x+.018,dep-.008,.018,x+mw-.018,dep,h-.018])]:local(u,bid+'_'+label,bb,M['wood'])
  for i,z in enumerate(b['shelves_mm']):local(u,bid+'_shelf'+str(i),[x+.018,.019,z/1000,x+mw-.018,.019+cd,(z+18)/1000],M['wood'])
  for i,z in enumerate(b['rails_mm']):
   islift=z in b['lift_rails_mm'];rl=b['rod_lengths_mm'][i]/1000
   bb=[x+mw/2-.012,.08,z/1000,x+mw/2+.012,.43,(z+24)/1000] if dep<.55 else [x+(mw-rl)/2,dep/2-.012,z/1000,x+(mw+rl)/2,dep/2+.012,(z+24)/1000]
   ro=local(u,bid+'_rod'+str(i),bb,M['dark'],'lift' if islift else 'rod')
   if islift:lifts.append((ro,outward(u),ro.location.copy()))
   # 80% illustrative clothing occupancy, never a counted owner inventory.
   for k in range(max(1,int(rl/.08*.8))):
    xx=x+(mw-rl)/2+.04+k*.08;hh=.78 if z<1500 else .95 if islift else 1.5
    if dep>=.55:local(u,bid+'_load'+str(i)+'_'+str(k),[xx,.09,z/1000-hh,xx+.028,dep-.09,z/1000-.03],M['cloth'],'test_load')
  for j,z in enumerate(b['drawer_z']):
   dw,dd,dh=[v/1000 for v in b['drawer_inner_mm']];dx=x+(mw-dw)/2;zz=z/1000;dl=[]
   # Upper vanity drawer U cut: leave central notch empty, two side trays.
   notch=u['id'].startswith('B') and j==0
   spans=[(dx,dx+(dw-.25)/2),(dx+(dw+.25)/2,dx+dw)] if notch and dw>.25 else [(dx,dx+dw)]
   for k,(a,aa) in enumerate(spans):
    for label,bb in [('bottom',[a,.04,zz,aa,.04+dd,zz+.012]),('left',[a-.012,.04,zz,a,.04+dd,zz+dh]),('right',[aa,.04,zz,aa+.012,.04+dd,zz+dh]),('back',[a,.04+dd,zz,aa,.052+dd,zz+dh])]:dl.append(local(u,bid+f'_drawer{j}_{k}_{label}',bb,M['wood'],'drawer'))
   dl.append(local(u,bid+f'_drawer{j}_face',[x+.03,.019,zz-.008,x+mw-.03,.038,zz+dh+.02],M['front'],'drawer'))
   for obj in dl:drawers.append((obj,outward(u)*b['runner_mm']/1000,obj.location.copy(),u['id']))
  # Hinged fronts only for genuinely hinged units; low drawer cabinets get drawer fronts.
  if u['id'] not in ['K-05','K-06','B62-01','B61-01','NT-L','NT-R','NT-64','NT-76']:
   spans=[(0,2.36),(2.36,h)] if h>2.4 else [(0,h)]
   if u['id']=='K-01':spans=[(.08,.58),(1.8,h)]
   if u['id']=='K-02':spans=[(.08,.7),(.7,1.852),(1.852,h)]
   for j,(lo,hi) in enumerate(spans):
    fo=local(u,bid+f'_front{j}',[x+.0015,0,lo+.0015,x+mw-.0015,.019,hi-.0015],M['dark'] if 'grafit' in u['front'] else M['front'],'front')
    pivot=bpy.data.objects.new(fo.name+'_hinge',None);C.objects.link(pivot);pivot.location=transform(u,(x,0,lo));bpy.context.view_layer.update();fo.parent=pivot;fo.matrix_parent_inverse=pivot.matrix_world.inverted();sgn=-1 if u.get('opening_dir') in ['-y','+x'] else 1
    fronts.append((pivot,sgn*(155 if b['drawers'] else 110),u['id']))
  for j,z in enumerate(b['lights_mm']):
   length=.46 if cw>=.5 else .25;local(u,bid+'_LED'+str(j),[x+(mw-length)/2,.04,z/1000,x+(mw+length)/2,.055,(z+8)/1000],M['led'],'light')
  # Top-cubby service enclosure, accessible behind a removable front strip.
 if u['id']=='K-01':
  for n,z,hh,dd in [('HBA534EB3',.6,.595,.548),('BFL524MB0',1.28,.382,.317)]:local(u,n,[.003,0,z,.597,dd,z+hh],M['dark'],'appliance_envelope')
 records.append(dict(unit=u['id'],cost=u['cost'],objects=unitparts[u['id']],capacity=u['capacity'],status='dimensioned functional proposal; exact hardware geometry pending'))
# Two independent external storage scenes. Graphic-read envelopes, not measured rooms.
stores=[dict(id='AT8-01',origin=[22,0,0],w=2580,d=1870,h=2400,area=4.57,door='north-right, 750 mm proposal from earlier drawing; hinge field check',pillar=[240,650,600,410],
 items=[dict(id='AT-R1',kind='rack',x=50,y=50,w=800,d=380,h=1600,sku='IKEA JONAXEL 504.199.72'),dict(id='AT-R2',kind='rack',x=1720,y=50,w=800,d=380,h=1600,sku='IKEA JONAXEL 504.199.72'),dict(id='AT-FR',kind='freezer',x=1000,y=50,w=597,d=675,h=1455,sku='Liebherr FNd 4625 / GN46Vd25 page-name conflict: exact EAN required')]),
 dict(id='T-0-26',origin=[27,0,0],w=2500,d=1600,h=2400,area=4.,door='actual opening is not identifiable on cadastral page; south access is a conditional arrangement',pillar=None,
 items=[dict(id='T-R1',kind='rack',x=50,y=1000,w=850,d=550,h=1900,sku='IKEA BROR s59619405'),dict(id='T-R2',kind='rack',x=950,y=1000,w=850,d=550,h=1900,sku='IKEA BROR s59619405'),dict(id='T-LUG',kind='luggage',x=1900,y=1050,w=500,d=500,h=1000,sku='owner luggage placeholder, not surveyed')])]
for st in stores:
 ox,oy,oz=st['origin'];sw,sd=st['w']/1000,st['d']/1000
 box('CP3_'+st['id']+'_floor',[ox,oy,-.04,ox+sw,oy+sd,0],M['storage'],st['id'],'room_proposal')
 for lab,b in [('back',[ox,oy+sd,0,ox+sw,oy+sd+.08,2.4]),('left',[ox-.08,oy,0,ox,oy+sd,2.4])]:box('CP3_'+st['id']+'_'+lab,b,M['storage'],st['id'],'room_proposal')
 if st['pillar']:
  x,y,w,d=[i/1000 for i in st['pillar']];box('CP3_AT_pillar',[ox+x,oy+y,0,ox+x+w,oy+y+d,2.4],M['storage'],st['id'],'column_graphic_read')
 for it in st['items']:
  x,y,w,d,h=[it[k]/1000 for k in ['x','y','w','d','h']];x+=ox;y+=oy
  if it['kind']=='rack':
   for i,(xx,yy) in enumerate([(x,y),(x+w-.025,y),(x,y+d-.025),(x+w-.025,y+d-.025)]):box('CP3_'+it['id']+'_leg'+str(i),[xx,yy,0,xx+.025,yy+.025,h],M['storage'] if st['id']=='AT8-01' else M['dark'],it['id'])
   for j,z in enumerate([.1,h*.33,h*.65,h-.02]):
    box('CP3_'+it['id']+'_shelf'+str(j),[x,y,z,x+w,y+d,z+.018],M['storage'] if st['id']=='AT8-01' else M['dark'],it['id'])
    for k in range(2):box('CP3_'+it['id']+f'_box{j}_{k}',[x+.04+k*.36,y+.04,z+.02,x+.32+k*.36,y+d-.03,z+.25],M['wood'],it['id'],'illustrative_load')
  else:box('CP3_'+it['id'],[x,y,0,x+w,y+d,h],M['storage'] if it['kind']=='freezer' else M['dark'],it['id'],'product_envelope')
 st['dimension_status']='[J] graphic-read / planning envelope; all finished dimensions, height and door hinge await survey. Area alone did not establish dimensions.'
(O/'data/storage_CP3.json').write_text(json.dumps(stores,ensure_ascii=False,indent=2))
# Capacity-preserving modular 05.2 alternative. Original bed/wardrobe retained.
ALT=bpy.data.collections.new('CP3_ALT052_CAPACITY_PRESERVED');bpy.context.scene.collection.children.link(ALT)
ao=box('CP3_ALT052_fold_desk',[.1,.05,.72,.85,.4,.75],M['wood'],'ALT052-B','alternative')
for c in list(ao.users_collection):c.objects.unlink(ao)
ALT.objects.link(ao)
stool=box('CP3_ALT052_stool',[.22,.43,0,.67,.88,.46],M['dark'],'ALT052-B','alternative')
for c in list(stool.users_collection):c.objects.unlink(stool)
ALT.objects.link(stool);ALT.hide_render=True;ALT.hide_viewport=True
def cam(n,loc,target,lens=35):
 o=bpy.data.objects.get(n)
 if not o:o=bpy.data.objects.new(n,bpy.data.cameras.new(n));C.objects.link(o)
 o.location=loc;o.rotation_euler=(Vector(target)-o.location).to_track_quat('-Z','Y').to_euler();o.data.lens=lens;return o
cam('CP3_Cam_AT8',(24.9,3.3,2.4),(23.3,.65,.85),32);cam('CP3_Cam_T026',(29.8,-2.2,2.3),(28.2,1.1,.9),32)
functions=[('F01','WN-01'),('F02','WS-01'),('F03','W52-01'),('F04','W53-01'),('F05','K-06'),('F06','B62-01'),('F07','ENT-01')]
for fid,uid in functions:
 u=next(u for u in D['units'] if u['id']==uid);center=Vector(transform(u,(u['w']/2000,0,u['h']/2000)));cam('CP3_'+fid,center+outward(u)*max(2.8,u['w']/700)+Vector((0,0,.25)),center,40)
def setstate(opened=False):
 for p,a,uid in fronts:p.rotation_euler.z=math.radians(a if opened else 0)
 for o,delta,start,uid in drawers:o.location=start+delta if opened else start
 for o,vec,start in lifts:o.location=start+vec*.6+Vector((0,0,-.6)) if opened else start
 bpy.context.view_layer.update()
scene=bpy.context.scene;scene.render.engine='BLENDER_WORKBENCH';scene.display.shading.light='STUDIO';scene.display.shading.color_type='MATERIAL';scene.display.shading.show_shadows=True;scene.display.shading.show_cavity=True;scene.view_settings.view_transform='Standard';scene.render.resolution_x=1100;scene.render.resolution_y=760;scene.render.resolution_percentage=100;scene.render.image_settings.file_format='JPEG';scene.render.image_settings.quality=92;scene.world.color=(.65,.65,.65)
renderlog=[]
def render(cid,name,state='closed'):
 scene.camera=bpy.data.objects[cid];scene.render.filepath=str(O/'blender'/f'{name}.jpg');bpy.ops.render.render(write_still=True);o=scene.camera
 renderlog.append(dict(id=name,camera_id=cid,location=list(o.location),rotation_euler=list(o.rotation_euler),lens_mm=o.data.lens,camera_type=o.data.type,ortho_scale=o.data.ortho_scale,image=f'CP3/blender/{name}.jpg',state=state,revision=REV,engine=scene.render.engine,status='native dimensional control; simplified products; not photometric proof'))
setstate(False)
# Hide plan-study ceiling and walls only for external isolated storage cameras.
for fid,uid in functions:
 saved={o.name:o.hide_render for o in bpy.data.objects if o.type=='MESH'}
 for o in bpy.data.objects:
  if o.type=='MESH':o.hide_render=not o.name.startswith('CP3_'+uid+'_')
 u=next(u for u in D['units'] if u['id']==uid);cc=bpy.data.objects['CP3_'+fid];cc.data.type='ORTHO';cc.data.ortho_scale=max(u['w']/1000*1.5,u['h']/1000*1.9,1.7)
 setstate(False);render('CP3_'+fid,fid+'_closed','isolated cabinet; context removed for technical inspection')
 setstate(True);render('CP3_'+fid,fid+'_open','isolated cabinet; actual hinged fronts open; lift end position only, no certified motion sweep')
 for o in bpy.data.objects:
  if o.name.startswith('CP3_'+uid+'_') and o.get('part_kind')=='front':o.hide_render=True
 render('CP3_'+fid,fid+'_cutaway','technical cutaway: fronts removed explicitly, drawers extended; not a real room photograph')
 for n,v in saved.items():bpy.data.objects[n].hide_render=v
setstate(False)
bpy.data.objects['CP3_AT8-01_back'].hide_render=True
render('CP3_Cam_AT8','V27_AT8','room cutaway: north wall omitted to show furniture; exact door unknown')
bpy.data.objects['CP3_AT8-01_back'].hide_render=False
render('CP3_Cam_T026','V28_T026','conditional room arrangement, south access assumed; final door unknown')
# Updated identical-camera control images for every existing 26 view ID.
manifest=json.loads((P/'render_handoff/manifest_R02.json').read_text())
scene.render.resolution_x=960;scene.render.resolution_y=640
for v in manifest:render(v['camera_id'],v['view_id']+'_CP3')
# Actually executed geometric tests, explicit limitations.
checks=[]
def test(n,result,detail):checks.append(dict(check=n,result=result,detail=detail))
for u in D['units']:
 for b in u['cp3_bays']:
  test(b['id']+' clear width', 'PASS' if b['clear_w']>0 else 'FAIL',str(b['clear_w'])+' mm after 2×18 mm sides')
  for zz in b['drawer_z']:test(b['id']+' drawer height','PASS' if zz+b['drawer_inner_mm'][2]+20<u['h'] else 'FAIL',f'{zz}+{b["drawer_inner_mm"][2]}+20 < {u["h"]}')
test('Kitchen working aisle','FAIL','840 mm between current 620 mm counters; design target 900 mm. No geometry narrowing silently applied.')
test('Dishwasher open route','FAIL','840 - 600 door projection = 240 mm. Open dishwasher blocks through passage.')
# Exact sampled quarter disk intersection vs desk/stool alternative AABBs.
hinge=(0,1.03);rad=.91
for name,bb in [('ALT052 desk',(.1,.05,.85,.4)),('ALT052 stool',(.22,.43,.67,.88))]:
 hit=False
 for deg in range(0,91,2):
  for k in range(1,101):
   x=hinge[0]+rad*k/100*math.sin(math.radians(deg));y=hinge[1]+rad*k/100*math.cos(math.radians(deg))
   if bb[0]<=x<=bb[2] and bb[1]<=y<=bb[3]:hit=True
 test(name+' balcony sweep','FAIL' if hit else 'PASS','91 cm source hinge; sampled 2°/100 radial points; desk 750×350 and stool450×450. Not a full ergonomic chair approval.')
test('05.2 wardrobe capacity','PASS','2380 mm retained; ALT-B does not remove the former 1000 mm wardrobe segment.')
test('05.2 ergonomic work','OPEN','Compact 750×350 desk and stool is not a full office workstation; child age and ergonomic selection pending. No automatic purchase substitution.')
test('05.3 simultaneous use','OPEN','Existing workchair and bed clearances require full occupancy/withdrawal check; shallow wardrobe itself is modelled with front-hanging rail.')
test('CONERO motion','OPEN','625–808 mm normal12 kg selected for694 mm clear bay; conservative600 mm forward/down end position shown. Exact manufacturer linkage and collision sweep pending.')
test('AT8 geometry','CONDITIONAL','2580×1870 graphical reading, column600×410; freezer relocated between racks to keep planned entrance side clear. Final door, vent and appliance EAN unresolved.')
test('T026 geometry','OPEN','2500×1600 arrangement envelope only; cadastral PDF lacks a reliable door/finished interior. No fit PASS.')
test('Lighting loaded shelves','OPEN','Loaded dark-cloth native workbench views rendered; workbench does not simulate light. No lux / shadow or CRI approval asserted.')
test('Threshold','OPEN','R02 120 mm is an illustrative object; source sheet mentions150 mm. Field step, width and route survey required.')
setstate(False);scene.camera=bpy.data.objects['Cam_12_Nappali_Hero'];bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_CP3.blend'),compress=True)
(O/'blender/object_register.json').write_text(json.dumps(records,ensure_ascii=False,indent=2));(O/'blender/render_runs.json').write_text(json.dumps(renderlog,ensure_ascii=False,indent=2));(O/'blender/checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
print('CP3_DONE',len(records),'units',len(renderlog),'renders',len(checks),'executed checks / open gates')
