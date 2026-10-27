import bpy,json,hashlib,math
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'R05';B=O/'blender';src=Path(bpy.data.filepath);srcsha=hashlib.sha256(src.read_bytes()).hexdigest()
units=json.loads((O/'data/design_R05.json').read_text())['units'];um={u['id']:u for u in units}
materials=json.loads((O/'data/materials.json').read_text());reg=json.loads((O/'data/register_proposal.json').read_text());rm={r[2]:r for r in reg[1:]}
C=bpy.data.collections.new('KI_R05_TECHNICAL_REVISION');bpy.context.scene.collection.children.link(C)
mats={}
for m in materials:
 h=m['hex'].lstrip('#');rgb=tuple(int(h[i:i+2],16)/255 for i in (0,2,4));mat=bpy.data.materials.new(m['id']+' '+m['candidate']);mat.diffuse_color=(*rgb,1);mat['approval']='UNAPPROVED_DISPLAY_COLOUR';mat['material_id']=m['id'];mat.use_nodes=True
 bs=mat.node_tree.nodes.get('Principled BSDF');bs.inputs['Base Color'].default_value=(*rgb,1);bs.inputs['Roughness'].default_value=.75;mats[m['id']]=mat
def box(n,bb,mid,uid,kind):
 x,y,z,X,Y,Z=bb;mesh=bpy.data.meshes.new(n);mesh.from_pydata([(x,y,z),(X,y,z),(X,Y,z),(x,Y,z),(x,y,Z),(X,y,Z),(X,Y,Z),(x,Y,Z)],[],[(0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)]);ob=bpy.data.objects.new(n,mesh);C.objects.link(ob);ob.data.materials.append(mats[mid]);ob['structure_id']=uid;ob['element_id']=';'.join(um[uid]['cost']);ob['revision']='KI-R05';ob['part_kind']=kind;ob['material_id']=mid;ob['status']='TECHNICAL_ENVELOPE_NOT_PRODUCTION';return ob
def part(u,n,a,d,z,A,D,Z,mid,kind):
 # +X-facing media wall: local depth goes toward -X; local width along world +Y.
 x,y,zz=u['x'],u['y'],u['z'];dep=u['d']/1000
 return box(n,[x+dep-D,y+a,zz+z,x+dep-d,y+A,zz+Z],mid,u['id'],kind)
superseded=[]
for ob in bpy.data.objects:
 if ob.name.startswith('R04_TV-01-R04A_'):ob.location.y-=2.6
 if ob.name.startswith('KI_TV-03_panel'):ob.location.y+=.7
 if ob.name=='KI_KI-033':ob.location.y+=.7
 if ob.name.startswith(('R04_TV-02-R04A_','KI_ART-02_panel')):
  ob.hide_render=True;ob.hide_viewport=True;superseded.append(ob.name)
# Rebuild lower module shells and fronts, retaining overall placement.
u=um['TV-02'];dep=u['d']/1000;h=u['h']/1000
for i,b in enumerate(u['cp3_bays']):
 a=b['offset']/1000;w=b['module_w']/1000
 for tag,bb in [('L',(a,.019,0,a+.018,dep,h)),('R',(a+w-.018,.019,0,a+w,dep,h)),('base',(a+.018,.019,0,a+w-.018,dep,.018)),('top',(a+.018,.019,h-.018,a+w-.018,dep,h)),('back',(a+.018,dep-.038,.018,a+w-.018,dep-.03,h-.018))]:part(u,f'R05_TV-02_B{i+1}_{tag}',*bb,'MAT-10','structure')
 for j,sz in enumerate(b['shelves_mm']):part(u,f'R05_TV-02_B{i+1}_shelf{j}',a+.018,.019,sz/1000,a+w-.018,.019+b['clear_d']/1000,(sz+18)/1000,'MAT-10','shelf')
 part(u,f'R05_TV-02_front{i+1}',a+.0015,0,.0015,a+w-.0015,.019,h-.0015,'MAT-02','visible_front')
# W02 panel carrier matches two 1050 mm print fields. No invented ink artwork.
u=um['ART-02']
for i in range(2):
 x=u['x']+i*1.05
 box('R05_ART-02_panel'+str(i+1),[x+.0015,u['y'],0,x+1.0485,u['y']+.036,2.88],'MAT-05','ART-02','print_carrier')
bindings=[];unbound=[]
for ob in bpy.data.objects:
 if ob.type!='MESH':continue
 uid=ob.get('structure_id')
 if not uid:
  for k in sorted(um,key=len,reverse=True):
   if any(ob.name.startswith(pre+k) for pre in ('KI_','CP3_','R04_')):uid=k;break
 if uid:
  u=um[uid];ob['structure_id']=uid;ob['cost_ids']=';'.join(u['cost']);ob['design_revision']='KI-R05';ob['material_ids']=';'.join(u['material_ids'])
  if not ob.hide_render:
   mids=u['material_ids'];mid=mids[-1] if mids else None
   exterior=any(t in ob.name.lower() for t in ('front','panel','cf-','st-','hb-','k-08','k-09','hall'))
   if mid and (exterior or ob.get('part_kind')=='visible_front'):
    shader=mats['MAT-02'] if uid=='TV-01' else mats[mid]
    ob.data.materials.clear();ob.data.materials.append(shader);ob['material_id']=mid
  bindings.append({'object':ob.name,'unit':uid,'cost':u['cost'],'materials':u['material_ids'],'hidden':ob.hide_render,'asset_status':'dimensioned custom mesh; finish samples and ink master pending'})
 else:
  code=str(ob.get('element_id','')).split(';')[0]
  if not code and ob.name=='KI_KI-028':code='KI-028'
  if code not in rm and code.startswith('KI-'):code='-'.join(code.split('-')[:2])
  if code in rm:
   r=rm[code];ob['cost_id']=code;ob['sku']=str(r[9] or 'UNRESOLVED');ob['product_identity']='SIMPLIFIED_PROXY_NOT_EXACT_PRODUCT_MODEL';bindings.append({'object':ob.name,'unit':None,'cost':[code],'sku':r[9],'hidden':ob.hide_render,'asset_status':'simplified proxy; exact shape unverified'})
  elif ob.name.startswith(('KI_','CP3_','R04_')) and not ob.hide_render:unbound.append(ob.name)
# Tests based on actual rebuilt mesh bounds, not just a status label.
def bounds(obs):
 pts=[o.matrix_world@Vector(v) for o in obs for v in o.bound_box];return [min(v[i] for v in pts) for i in range(3)]+[max(v[i] for v in pts) for i in range(3)]
bpy.context.view_layer.update()
lower=[bpy.data.objects[f'R05_TV-02_front{i+1}'] for i in range(5)]
tower=[o for o in bpy.data.objects if o.name.startswith('R04_TV-01-R04A_visible_front')]
lb=bounds([lower[0]]);tb=bounds(tower);err=max(abs(lb[1]-tb[1]),abs(lb[4]-tb[4]))
checks=[{'test':'TV lower end front aligns with tower in world Y','result':'PASS' if err<.0001 else 'FAIL','error_mm':err*1000,'scope':'nominal front edges only'},
 {'test':'TV lower five modules overall width','result':'PASS' if abs(bounds(lower)[4]-bounds(lower)[1]-3.297)<.0001 else 'FAIL','scope':'front gaps excluded; design width3300mm'},
 {'test':'W02 print field count','result':'PASS' if len([o for o in bpy.data.objects if o.name.startswith('R05_ART-02_panel')])==2 else 'FAIL','count':len([o for o in bpy.data.objects if o.name.startswith('R05_ART-02_panel')]),'scope':'two1050mm design modules; gap/bleed final with printer'},
 {'test':'W01 artwork and texture','result':'OPEN','reason':'No original master artwork. Display colors are not measured. No exact-appearance claim.'},
 {'test':'Ready-made product identity','result':'OPEN','reason':'SKU tags do not turn existing simplified boxes into exact manufacturer models.'},
 {'test':'WN high door / lift motion','result':'OPEN','reason':'2837mm fronts require long raw board, approved hinges/straightening and lift motion data.'},
 {'test':'Inherited functional conflicts','result':'OPEN','reason':'840mm kitchen aisle; dishwasher blocks passage;05.3chair/bed; master side drawers/nightstands; store door/bike path; threshold discrepancy. No overall apartment PASS.'}]
S=bpy.context.scene;S.render.engine='BLENDER_WORKBENCH';S.display.shading.light='STUDIO';S.display.shading.color_type='MATERIAL';S.display.shading.show_cavity=True;S.view_settings.view_transform='Standard';S.render.resolution_x=1600;S.render.resolution_y=1000;S.render.resolution_percentage=100;S.render.image_settings.file_format='PNG';S.render.image_settings.color_mode='RGB'
visibility={o.name:o.hide_render for o in bpy.data.objects if o.type=='MESH'}
# Exact inherited camera: one technical trial only, no generative batch.
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];S.render.filepath=str(B/'V01_R05_native_technical.png');bpy.ops.render.render(write_still=True)
cam=bpy.data.objects.new('R05_MEDIAWALL_ORTHO',bpy.data.cameras.new('R05_MEDIAWALL_ORTHO'));C.objects.link(cam);cam.location=(10,6.35,1.45);target=Vector((3.9,6.35,1.45));cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=5.2;S.camera=cam
for ob in bpy.data.objects:
 if ob.type=='MESH':ob.hide_render=visibility[ob.name] or (ob.get('structure_id') not in ('TV-01','TV-02','TV-03') and ob.name!='KI_KI-033')
S.render.filepath=str(B/'W01_R05_front_control.png');bpy.ops.render.render(write_still=True)
for n,v in visibility.items():bpy.data.objects[n].hide_render=v
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];bpy.ops.wm.save_as_mainfile(filepath=str(B/'A902_Kyoto_Ink_R05.blend'),compress=True)
def js(n,d):(B/n).write_text(json.dumps(d,ensure_ascii=False,indent=2))
js('object_register.json',bindings);js('checks.json',checks);js('unbound_objects.json',unbound);js('source.json',{'path':str(src),'sha256':srcsha,'unchanged':hashlib.sha256(src.read_bytes()).hexdigest()==srcsha,'superseded_meshes':superseded,'model_revision':'KI-R05','renders':['V01_R05_native_technical.png','W01_R05_front_control.png']})
print('R05_SAVED',len(bindings),'bindings',len(checks),'checks')
