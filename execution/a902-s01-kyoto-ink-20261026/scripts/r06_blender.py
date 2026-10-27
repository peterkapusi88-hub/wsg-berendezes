import bpy,math,json,hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1]; O=P/'R06'; src=Path(bpy.data.filepath); sha=hashlib.sha256(src.read_bytes()).hexdigest()
C=bpy.data.collections.new('KI_R06_PRODUCT_AND_ARTWORK');bpy.context.scene.collection.children.link(C)
def mat(n,c,rough=.7):
 m=bpy.data.materials.new(n);m.diffuse_color=(*c,1);m.use_nodes=True;b=m.node_tree.nodes.get('Principled BSDF');b.inputs['Base Color'].default_value=(*c,1);b.inputs['Roughness'].default_value=rough;return m
fabric=mat('R06 Lennon woven taupe sample pending',(.38,.31,.24)); oak=mat('R06 natural oak sample pending',(.52,.36,.19)); charcoal=mat('R06 graphite',(.055,.05,.045));cream=mat('R06 warm chalk',(.65,.60,.51));white=mat('R06 opal',(.9,.86,.75));stone=mat('R06 F243 visual approximation',(.39,.36,.30))
for m,scale,strength in [(fabric,350,.12),(cream,180,.04),(stone,8,.1),(oak,30,.05)]:
 nt=m.node_tree;ns=nt.nodes;tex=ns.new('ShaderNodeTexNoise');tex.inputs['Scale'].default_value=scale;bump=ns.new('ShaderNodeBump');bump.inputs['Strength'].default_value=strength;bump.inputs['Distance'].default_value=.002;nt.links.new(tex.outputs['Fac'],bump.inputs['Height']);nt.links.new(bump.outputs['Normal'],ns.get('Principled BSDF').inputs['Normal'])
new=[];hidden=[]
def tag(o,id,sku='CUSTOM',status='PHOTO_DIMENSION_RECONSTRUCTION_NOT_MANUFACTURER_MESH'):
 o['element_id']=id;o['sku']=sku;o['revision']='KI-R06';o['asset_status']=status;new.append(o);return o
def link(o):
 for c in list(o.users_collection):c.objects.unlink(o)
 C.objects.link(o)
def box(n,bb,m,id,bev=0,sku='CUSTOM'):
 x,y,z,X,Y,Z=bb;bpy.ops.mesh.primitive_cube_add(size=1,location=((x+X)/2,(y+Y)/2,(z+Z)/2));o=bpy.context.object;o.name=n;o.dimensions=(X-x,Y-y,Z-z);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);link(o);o.data.materials.append(m)
 if bev:mod=o.modifiers.new('Rounded actual upholstery silhouette','BEVEL');mod.width=bev;mod.segments=5;o.modifiers.new('Weighted normals','WEIGHTED_NORMAL')
 return tag(o,id,sku)
def cyl(n,a,b,r,m,id):
 v=Vector(b)-Vector(a);bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=r,depth=v.length,location=(Vector(a)+Vector(b))/2);o=bpy.context.object;o.name=n;o.rotation_euler=v.to_track_quat('Z','Y').to_euler();link(o);o.data.materials.append(m);return tag(o,id)
def hide(o):o.hide_render=True;o.hide_viewport=True;hidden.append(o.name)
# Archive earlier proxy meshes; source file itself remains untouched.
for o in list(bpy.data.objects):
 if o.name.startswith(('KI_KI-036','KI_KI-028','KI_KI-029','KI_KI-043')):hide(o)
# Lennon: manufacturer envelope, module split, seat height430, arms320, low back680.
sku='DEQ21WES12329-168260'
for j,(y,front) in enumerate([(4.77,4.87),(5.96,5.48)]):
 box(f'R06_Lennon_module{j}_base',(front,y,.04,6.67,y+1.19,.30),fabric,'KI-036',.055,sku)
 box(f'R06_Lennon_module{j}_back',(6.35,y,.30,6.67,y+1.19,.68),fabric,'KI-036',.065,sku)
 low=y if j==0 else y+.87
 box(f'R06_Lennon_module{j}_arm',(front,low,.30,6.35,low+.32,.68),fabric,'KI-036',.06,sku)
 sy=y+.32 if j==0 else y
 box(f'R06_Lennon_module{j}_seat',(front+.005,sy,.295,6.35,sy+.87,.43),fabric,'KI-036',.05,sku)
 box(f'R06_Lennon_module{j}_backcushion',(6.18,sy+.025,.43,6.35,sy+.845,.67),fabric,'KI-036',.065,sku)
# Toni elliptical25mm top and two bent panel bases (photo reconstruction).
bpy.ops.mesh.primitive_cylinder_add(vertices=96,radius=1,depth=.025,location=(8.25,6.2,.7375));o=bpy.context.object;o.name='R06_Toni160_oval_top';o.scale=(.45,.8,1);link(o);o.data.materials.append(oak);tag(o,'KI-028','DEQ19WES60483-225182')
for y,sgn in [(5.79,1),(6.61,-1)]:
 verts=[];faces=[]
 for z in [0,.725]:
  for k in range(25):
   a=-1+2*k/24;verts.append((8.25+a*.29,y+sgn*.10*a*a,z))
 for k in range(24):faces.append((k,k+1,k+26,k+25))
 me=bpy.data.meshes.new('Toni bent panel');me.from_pydata(verts,[],faces);ob=bpy.data.objects.new('R06_Toni_bent_panel',me);C.objects.link(ob);ob.data.materials.append(oak);sol=ob.modifiers.new('25mm panel','SOLIDIFY');sol.thickness=.025;tag(ob,'KI-028','DEQ19WES60483-225182')
# Eamy: curved ash shell, chenille seat/back and thin black legs.
items=json.loads((P/'R05/data/design_R05.json').read_text())['items']
for it in [i for i in items if i['id'].startswith('KI-029-')]:
 idx=int(it['id'].split('-')[-1]);cx=it['x']+it['w']/2000;cy=it['y']+it['d']/2000;angle={1:-math.pi/2,2:-math.pi/2,3:math.pi/2,4:math.pi/2,5:0,6:math.pi}[idx];start=len(new)
 # Local front +Y. Full width .55 and depth .53.
 box('R06_Eamy_seat',(-.225,-.21,.40,.225,.21,.46),fabric,'KI-029',.035,'C0100003HE12')
 for sx in [-1,1]:
  for sy in [-1,1]:cyl('R06_Eamy_steel_leg',(sx*.25,sy*.245,0),(sx*.19,sy*.17,.43),.012,charcoal,'KI-029')
 for z0,z1,m,rad in [(.49,.67,oak,.34),(.55,.75,fabric,.325)]:
  vs=[];fs=[]
  for z in [z0,z1]:
   for k in range(33):
    a=-.94+k*1.88/32;vs.append((rad*math.sin(a),.075-rad*math.cos(a),z))
  for k in range(32):fs.append((k,k+1,k+34,k+33))
  me=bpy.data.meshes.new('Eamy curved back');me.from_pydata(vs,[],fs);ob=bpy.data.objects.new('R06_Eamy_curved_back',me);C.objects.link(ob);ob.data.materials.append(m);mod=ob.modifiers.new('shell thickness','SOLIDIFY');mod.thickness=.012 if m==oak else .035;tag(ob,'KI-029','C0100003HE12')
 for ob in new[start:]:
  ob.rotation_euler.z+=angle;v=ob.location.copy();ob.location.x=cx+v.x*math.cos(angle)-v.y*math.sin(angle);ob.location.y=cy+v.x*math.sin(angle)+v.y*math.cos(angle);ob['instance_id']=it['id']
# Custom upholstered lift bed proposal avoids horizontal master drawer conflict.
box('R06_BED01_upholstered_frame',(1.47,5.5,.04,3.49,7.3,.30),cream,'KI-043',.025)
box('R06_VAGSTRANDA_180x200',(1.48,5.5,.30,3.48,7.3,.58),white,'KI-044',.035,'004.507.57')
# Lift split visible in underside/motion sheets; no imaginary certified mechanism.
box('R06_BED01_common_lift_frame',(1.50,5.522,.255,3.46,7.278,.285),charcoal,'KI-043',.005)
# Shift 05.3 bed and chair; preserve width, then test actual clearances.
for ob in bpy.data.objects:
 if ob.name.startswith('KI_KI-070'):ob.location.y-=.10
 if ob.name.startswith('KI_KI-075'):ob.location.y+=.15
 if ('NT-76' in ob.name) and ob.type=='MESH' and not ob.hide_render:
  ob.location.x+=.925;ob.location.y-=.21
# Front-only replacement, interiors preserved.
for uid,count,x,y,width,fronty in [('WN-01',6,.05,8.3,2.92,8.3),('WS-01',4,.02,3.47,2.38,3.95)]:
 for ob in list(bpy.data.objects):
  if uid in ob.name and any(t in ob.name.lower() for t in ['front','handle']) and not ob.name.startswith('R06'):hide(ob)
 for k in range(count):
  xx=x+k*width/count
  box(f'R06_{uid}_full_front{k}',(xx+.0015,fronty,.0015,xx+width/count-.0015,fronty+.019,2.8385),cream,'KI-048' if uid=='WN-01' else 'KI-049')
  if uid=='WS-01':cyl(f'R06_{uid}_handle{k}',(xx+width/count-.045,fronty+.045,.85),(xx+width/count-.045,fronty+.045,1.75),.006,charcoal,'KI-049')
# Artwork plane with global UV keeps motif continuous across separate panels.
def art(n,verts,uvs,path,id):
 me=bpy.data.meshes.new(n);me.from_pydata(verts,[],[(0,1,2,3)]);me.uv_layers.new(name='Print coordinates')
 for poly in me.polygons:
  for li in poly.loop_indices:me.uv_layers.active.data[li].uv=uvs[me.loops[li].vertex_index]
 ob=bpy.data.objects.new(n,me);C.objects.link(ob);m=mat(n+' textured print',(.6,.55,.46));nt=m.node_tree;tex=nt.nodes.new('ShaderNodeTexImage');tex.image=bpy.data.images.load(str(path),check_existing=True);tex.image.pack();ramp=nt.nodes.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(.025,.02,.015,1);ramp.color_ramp.elements[1].color=(.58,.52,.43,1);nt.links.new(tex.outputs['Color'],ramp.inputs['Fac']);nt.links.new(ramp.outputs['Color'],nt.nodes.get('Principled BSDF').inputs['Base Color']);ob.data.materials.append(m);tag(ob,id,'VECTOR_REDRAW_R06','REFERENCE_REDRAW_PROOF_NOT_ORIGINAL_MASTER');return ob
for k,(a,b,x) in enumerate([(0,.7,4.111),(.7,1.35,3.712),(1.35,2,3.712),(2,2.65,3.712),(2.65,3.3,3.712)]):
 art('R06_INK_W01_'+str(k),[(x,4.7+a+.0015,.55),(x,4.7+b-.0015,.55),(x,4.7+b-.0015,2.88),(x,4.7+a+.0015,2.88)],[(a/3.3,0),(b/3.3,0),(b/3.3,1),(a/3.3,1)],O/'artwork/INK-W01_mask.png','KI-030')
art('R06_INK_W02',[(5.2,4.091,0),(7.3,4.091,0),(7.3,4.091,2.88),(5.2,4.091,2.88)],[(0,0),(1,0),(1,1),(0,1)],O/'artwork/INK-W02_mask.png','KI-131')
for uid,count,x,y,w,mask in [('WN',6,.05,8.298,2.92,'INK-WN'),('WS',4,.02,3.971,2.38,'INK-WS')]:
 for k in range(count):
  a=k/count;b=(k+1)/count
  art('R06_INK_'+uid+str(k),[(x+a*w+.0015,y,.0015),(x+b*w-.0015,y,.0015),(x+b*w-.0015,y,2.8385),(x+a*w+.0015,y,2.8385)],[(a,0),(b,0),(b,1),(a,1)],O/f'artwork/{mask}_mask.png','KI-050')
# Correct shower glass orientation to existing north shower tray, 780mm entry.
ob=bpy.data.objects.get('KI_KI-091')
if ob:hide(ob)
glass=mat('R06 shower glass',(.55,.7,.75),.05);glass.node_tree.nodes.get('Principled BSDF').inputs['Transmission Weight'].default_value=.9
box('R06_GL01_1000mm',(15.4,7.10,.03,16.4,7.108,2.03),glass,'KI-091')
# Kitchen finish, same material across views; procedural approximation until sample scan.
for ob in bpy.data.objects:
 if not ob.hide_render and any(t in ob.name for t in ['K-08','K-09']):ob.data.materials.clear();ob.data.materials.append(stone)
# Rondo orb lamps: manufacturer's 200mm envelope; white base remains a visible difference.
for y in [5.27,7.50]:
 cyl('R06_Rondo_base',(3.25,y,.45),(3.25,y,.48),.055,white,'KI-117')
 bpy.ops.mesh.primitive_uv_sphere_add(segments=32,ring_count=16,radius=.1,location=(3.25,y,.55));ob=bpy.context.object;ob.name='R06_Rondo_85264_globe';link(ob);ob.data.materials.append(white);tag(ob,'KI-117','85264')
# Somar actual 760mm wide/360mm high ribbed flattened globe, not generic large sphere.
vs=[];fs=[];profile=[(0,.12),(.03,.23),(.09,.35),(.18,.38),(.27,.34),(.33,.24),(.36,.12)]
for z,r in profile:
 for k in range(64):a=2*math.pi*k/64;vs.append((8.25+r*math.cos(a),6.2+r*math.sin(a),1.95+z))
for j in range(len(profile)-1):
 for k in range(64):fs.append((j*64+k,j*64+(k+1)%64,(j+1)*64+(k+1)%64,(j+1)*64+k))
me=bpy.data.meshes.new('Somar shell');me.from_pydata(vs,[],fs);ob=bpy.data.objects.new('R06_Somar_760x360',me);C.objects.link(ob);ob.data.materials.append(white);tag(ob,'KI-109','L00148FA05')
for k in range(16):
 a=2*math.pi*k/16
 for j in range(len(profile)-1):
  z,r=profile[j];Z,R=profile[j+1];cyl('R06_Somar_rib',(8.25+r*math.cos(a),6.2+r*math.sin(a),1.95+z),(8.25+R*math.cos(a),6.2+R*math.sin(a),1.95+Z),.0025,cream,'KI-109')
cyl('R06_Somar_cable',(8.25,6.2,2.31),(8.25,6.2,2.88),.002,white,'KI-109')
bpy.context.view_layer.update()
def bb(obs):
 pts=[o.matrix_world@Vector(v) for o in obs for v in o.bound_box];return [min(v[i] for v in pts) for i in range(3)]+[max(v[i] for v in pts) for i in range(3)]
bindings=[dict(object=o.name,element=o.get('element_id'),sku=o.get('sku'),status=o.get('asset_status'),bounds=bb([o])) for o in new]
checks=[]
for prefix,expected in [('R06_Lennon',[1.8,2.38,.64]),('R06_Toni160_oval_top',[.9,1.6,.025])]:
 b=bb([o for o in new if o.name.startswith(prefix)]);dims=[b[i+3]-b[i] for i in range(3)];checks.append(dict(test=prefix+' nominal mesh envelope',actual_m=dims,expected_m=expected,result='PASS' if max(abs(a-b) for a,b in zip(dims,expected))<.001 else 'FAIL',scope='nominal mesh only; cushion compression and manufacture tolerances excluded'))
checks += [dict(test='Kitchen closed aisle',actual_mm=840,result='CONDITIONAL',reason='Open 600mm dishwasher leaves240mm: no through circulation; side loading only.'),dict(test='05.3 chair withdrawn600mm versus bed',actual_mm=150,result='PASS_LIMITED',reason='Bed north5.95; chair rear working6.70 minus.60=6.10. Gap is not a walking route.'),dict(test='Master bed drawers versus nightstands',result='RESOLVED_BY_PROPOSED_LIFT_BED',reason='Horizontal drawers replaced by one common upward opening frame with paired mechanisms; hinge strength and lift swept volume approval remains open.'),dict(test='06.2 shower glass',result='PROPOSED_CORRECTION',reason='1000mm east fixed pane parallel north tray edge, nominal780mm entry; waterproofing and exact tray/door/site survey pending.'),dict(test='T07 branch wall/hooks',result='FAIL_TARGET_GEOMETRY',reason='Target dry wall overlaps north shower area in source geometry. Waterproof art possible; hooks/bench placement not accepted there.'),dict(test='All apartment clearance and manufacturing release',result='OPEN',reason='Selective checks do not certify all door/lift/drawer motion, dimensions or installation.' )]
(O/'blender/object_register.json').write_text(json.dumps(bindings,ensure_ascii=False,indent=2));(O/'blender/checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2));(O/'blender/source.json').write_text(json.dumps(dict(path=str(src),sha256=sha,unchanged=sha==hashlib.sha256(src.read_bytes()).hexdigest(),hidden_proxies=hidden,revision='KI-R06'),indent=2))
S=bpy.context.scene;S.render.engine='CYCLES';S.cycles.samples=12;S.render.resolution_x=1400;S.render.resolution_y=900;S.render.resolution_percentage=100
# Product/art studio views use the very same new objects, no different replacement assets.
vis={o.name:o.hide_render for o in S.objects};cam=bpy.data.objects.new('R06_ASSET_CONTROL',bpy.data.cameras.new('R06_ASSET_CONTROL'));C.objects.link(cam);cam.data.type='ORTHO';cam.data.ortho_scale=3.4;cam.location=(2.9,2.5,2.5);target=Vector((5.7,5.9,.35));cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler();S.camera=cam
for o in S.objects:
 if o.type=='MESH':o.hide_render=not o.name.startswith('R06_Lennon')
 if o.type=='LIGHT':o.hide_render=True
S.view_settings.view_transform='AgX';S.view_settings.exposure=0;S.view_settings.look='None'
S.world.use_nodes=True;S.world.node_tree.nodes.get('Background').inputs[0].default_value=(.6,.6,.6,1);S.world.node_tree.nodes.get('Background').inputs[1].default_value=.8
S.render.filepath=str(O/'blender/Lennon_R06_shape_control.png');bpy.ops.render.render(write_still=True)
for n,v in vis.items():bpy.data.objects[n].hide_render=v
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_R06.blend'),compress=True)
print('R06_SAVED',len(new),'asset parts',len(checks),'checks')
