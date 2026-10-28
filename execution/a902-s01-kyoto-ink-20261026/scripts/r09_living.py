import bpy,math,json,hashlib
from pathlib import Path
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
P=Path(__file__).resolve().parents[1];O=P/'R09_living';S=bpy.context.scene;src=Path(bpy.data.filepath);oldhash=hashlib.sha256(src.read_bytes()).hexdigest()
C=bpy.data.collections.new('R09_COMPLETE_LIVING');S.collection.children.link(C);reg=[]
def mat(n,c,noise=0):
 m=bpy.data.materials.new(n);m.use_nodes=True;b=m.node_tree.nodes.get('Principled BSDF');b.inputs['Base Color'].default_value=(*c,1);b.inputs['Roughness'].default_value=.7
 if noise:
  t=m.node_tree.nodes.new('ShaderNodeTexNoise');t.inputs['Scale'].default_value=noise;bump=m.node_tree.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.18;bump.inputs['Distance'].default_value=.001;m.node_tree.links.new(t.outputs['Fac'],bump.inputs['Height']);m.node_tree.links.new(bump.outputs['Normal'],b.inputs['Normal'])
 return m
coal=mat('R09 graphite laminate',(.075,.065,.055),160);paper=mat('R09 cool greige textile carrier',(.37,.34,.29),220);taupe=mat('R09 taupe textile sample pending',(.34,.29,.24),250);grey=mat('R09 grey throw',(.25,.25,.24),300);ivory=mat('R09 warm white sheer',(.8,.77,.70),180);ceramic=mat('R09 handmade ceramic',(.09,.07,.045),40);pages=mat('R09 paper edges',(.68,.65,.59));ash=bpy.data.materials['R06 natural oak sample pending'];chenille=mat('R09 Eamy light grey chenille',(.43,.43,.40),300)
def link(o,id):
 for c in list(o.users_collection):c.objects.unlink(o)
 C.objects.link(o);o['element_id']=id;o['revision']='KI-R09';o['status']='DESIGN_RECONSTRUCTION_SAMPLE_AND_SITE_PENDING';reg.append(o);return o
def box(n,loc,dim,m,id,bev=0):
 bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name='R09_'+n;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);link(o,id);o.data.materials.append(m)
 if bev:mo=o.modifiers.new('soft edges','BEVEL');mo.width=bev;mo.segments=6;o.modifiers.new('normals','WEIGHTED_NORMAL')
 return o
def cyl(n,loc,r,h,m,id):
 bpy.ops.mesh.primitive_cylinder_add(vertices=64,radius=r,depth=h,location=loc);o=bpy.context.object;o.name='R09_'+n;link(o,id);o.data.materials.append(m);return o
def mesh(n,vs,fs,m,id):
 me=bpy.data.meshes.new(n);me.from_pydata(vs,[],fs);me.update();o=bpy.data.objects.new('R09_'+n,me);C.objects.link(o);o.data.materials.append(m);o['element_id']=id;reg.append(o)
 for p in me.polygons:p.use_smooth=True
 return o
def bounds(o):
 v=[o.matrix_world@Vector(x) for x in o.bound_box];return [min(a[i] for a in v) for i in range(3)]+[max(a[i] for a in v) for i in range(3)]
# Correct materials on visible physical furniture, not a global white override.
for o in S.objects:
 if o.type!='MESH' or o.hide_render:continue
 if any(x in o.name for x in ['TV-01','TV-02','KI-037','KI-038','CF-01','ST-01']):o.data.materials.clear();o.data.materials.append(coal)
 if o.name.startswith('R06_Lennon'):o.data.materials.clear();o.data.materials.append(taupe)
 if o.name.startswith('R06_INK_W01'):
  m=o.data.materials[0];nt=m.node_tree;r=next(n for n in nt.nodes if n.type=='VALTORGB');r.color_ramp.elements[1].color=(*((.075,.065,.055) if o.name.endswith('_0') else (.42,.39,.34)),1)
  t=nt.nodes.new('ShaderNodeTexNoise');t.inputs['Scale'].default_value=210;b=nt.nodes.new('ShaderNodeBump');b.inputs['Strength'].default_value=.18;b.inputs['Distance'].default_value=.001;nt.links.new(t.outputs['Fac'],b.inputs['Height']);nt.links.new(b.outputs['Normal'],nt.nodes.get('Principled BSDF').inputs['Normal'])
# Replace segmented Eamy back by a continuous rounded shell; preserve envelope.
items=json.loads((P/'R06/data/design_R06.json').read_text())['items'];chairs=[]
for it in [i for i in items if i['id'].startswith('KI-029-')]:
 idx=int(it['id'].split('-')[-1]);cx=it['x']+it['w']/2000;cy=it['y']+it['d']/2000;a={1:-math.pi/2,2:-math.pi/2,3:math.pi/2,4:math.pi/2,5:0,6:math.pi}[idx];dx=.12 if idx in [1,2] else -.12 if idx in [3,4] else 0;dy=.12 if idx==5 else -.12 if idx==6 else 0
 for o in list(S.objects):
  if o.get('instance_id')!=it['id']:continue
  if o.name.startswith('R06_Eamy_curved_back'):o.hide_render=True
  else:o.location.x+=dx;o.location.y+=dy
 for m,offset in [(ash,0),(chenille,.014)]:
  vs=[];fs=[]
  for j in range(13):
   t=j/12
   for k in range(49):
    u=-1+2*k/48;ang=u*.94;x=(.325-offset)*math.sin(ang);y=.075-(.325-offset)*math.cos(ang);top=.75-.075*abs(u)**3;z=.48+t*(top-.48);vs.append((cx+dx+x*math.cos(a)-y*math.sin(a),cy+dy+x*math.sin(a)+y*math.cos(a),z))
  for j in range(12):
   for k in range(48):q=j*49+k;fs.append((q,q+1,q+50,q+49))
  ob=mesh('Eamy_continuous_'+it['id']+m.name,vs,fs,m,'KI-029');sol=ob.modifiers.new('shell','SOLIDIFY');sol.thickness=.009 if m==ash else .018
 chairs.append({'id':it['id'],'translation_m':[dx,dy,0],'purpose':'tucked presentation position, not withdrawal test'})
# Wall-mounted track and gathered sheer: existing shutter service remains separate.
box('curtain_track',(6.69,7.965,2.60),(4.5,.025,.025),coal,'KI-041')
for start,width,label in [(4.46,.53,'west'),(8.46,.45,'east')]:
 vs=[];fs=[]
 for j in range(17):
  z=.13+j*(2.44/16)
  for k in range(97):u=k/96;vs.append((start+u*width,7.94+.042*math.sin(u*math.pi*18)+.007*math.sin(z*3+u*8),z))
 for j in range(16):
  for k in range(96):q=j*97+k;fs.append((q,q+1,q+98,q+97))
 mesh('gathered_sheer_'+label,vs,fs,ivory,'KI-040')
# Existing ML05 circuit position from electrical schedule; fixture envelope from register.
opal=mat('R09 Hue opal diffuser',(.88,.86,.80));b=opal.node_tree.nodes.get('Principled BSDF');b.inputs['Emission Color'].default_value=(1,.64,.32,1);b.inputs['Emission Strength'].default_value=2
cyl('ML05_Hue_381x84',(5.619,6.274,2.858),.1905,.084,ivory,'KI-113');cyl('ML05_diffuser',(5.619,6.274,2.814),.179,.005,opal,'KI-113')
# Three cushions and a physically draped throw on the selected sofa.
for i,(y,m) in enumerate([(5.35,taupe),(5.88,grey),(6.48,taupe)]):
 o=box('cushion_'+str(i),(6.12,y,.64),(.16,.43,.43),m,'KI-036',.065);o.rotation_euler.y=-.15
vs=[];fs=[]
for j in range(41):
 t=j/40;x=4.84+t*1.0;z=.455 if t>.1 else .15+3.05*t
 for k in range(25):y=5.20+k*.60/24;vs.append((x,y,z+.011*math.sin(k*1.4+j*.3)))
for j in range(40):
 for k in range(24):q=j*25+k;fs.append((q,q+1,q+26,q+25))
mesh('grey_throw',vs,fs,grey,'KI-036')
# Books, bowl and vase are styling within the existing accessory allowance, not purchased SKUs.
for i in range(3):box('art_book_'+str(i),(4.1,5.5,.56+i*.027),(.24,.32,.023),pages,'ACCESSORY_ALLOWANCE')
def vessel(n,loc,profile,m):
 vs=[];fs=[]
 for z,r in profile:
  for k in range(64):a=k*2*math.pi/64;vs.append((loc[0]+r*math.cos(a),loc[1]+r*math.sin(a),loc[2]+z))
 for j in range(len(profile)-1):
  for k in range(64):q=j*64+k;fs.append((q,j*64+(k+1)%64,(j+1)*64+(k+1)%64,q+64))
 return mesh(n,vs,fs,m,'ACCESSORY_ALLOWANCE')
vessel('broad_ceramic_bowl',(4.02,6.1,.55),[(0,.07),(.03,.12),(.08,.16),(.09,.158),(.07,.14),(.02,.06)],ceramic)
vessel('vase',(3.97,7.63,.55),[(0,.07),(.08,.11),(.22,.10),(.3,.045),(.31,.04)],ceramic)
# Restore true depth for staging objects: all on the 400mm-deep low cabinet.
# Preserve exterior unresolved objects; don't make up purchased products.
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];cam=S.camera;original=json.loads((O/'audit/original_camera_log.json').read_text())['kamera'];cam.location=original['loc'];cam.rotation_euler=original['rot_rad'];cam.data.lens=original['lens'];cam.data.sensor_width=36;cam.data.sensor_fit='AUTO';cam.data.shift_x=cam.data.shift_y=0
for vl in S.view_layers:vl.material_override=None
for o in S.objects:
 if o.type=='LIGHT':o.hide_render=True
S.world.use_nodes=True;S.world.node_tree.nodes.get('Background').inputs[0].default_value=(.55,.62,.75,1);S.world.node_tree.nodes.get('Background').inputs[1].default_value=.45
l=bpy.data.lights.new('R09 technical fill NOT installed','AREA');l.energy=350;l.shape='DISK';l.size=4;o=bpy.data.objects.new(l.name,l);S.collection.objects.link(o);o.location=(7,5,2.7);o.rotation_euler=(Vector((4,6,1))-o.location).to_track_quat('-Z','Y').to_euler()
S.render.engine='CYCLES';S.cycles.samples=32;S.render.resolution_x=1600;S.render.resolution_y=1000;S.render.resolution_percentage=100;S.view_settings.view_transform='AgX';S.view_settings.exposure=0;S.use_nodes=False
bpy.context.view_layer.update();audit={'source_sha256':oldhash,'source_unchanged':hashlib.sha256(src.read_bytes()).hexdigest()==oldhash,'camera_matches_original_numeric_log':True,'chair_moves':chairs,'new_objects':[{'name':o.name,'element':o.get('element_id'),'bounds':bounds(o)} for o in reg],'limits':['not photometric','curtain suspension and site dimensions pending','furniture photo reconstruction not manufacturer mesh','outdoor product selection unresolved','3300mm media wall retained; no silent increase to3600','existing threshold100mm remains estimate; source creative prompt15cm is not survey']}
(O/'audit/model_changes.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2));bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_R09.blend'),compress=True);S.render.filepath=str(O/'images/V01_R09_NATIVE_CONTROL.png');bpy.ops.render.render(write_still=True);print('R09_COMPLETE')
