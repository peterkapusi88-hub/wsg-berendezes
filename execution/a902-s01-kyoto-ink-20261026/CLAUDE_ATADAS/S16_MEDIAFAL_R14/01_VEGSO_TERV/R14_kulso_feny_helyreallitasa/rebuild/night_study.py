from pathlib import Path
import bpy,json,math,sys
from mathutils import Vector,Matrix
O=Path(__file__).resolve().parents[1]
parts=json.loads((O/'data/parts.json').read_text());drawers=json.loads((O/'data/drawers.json').read_text());lighting=json.loads((O/'data/lighting.json').read_text());layout=json.loads((O/'data/layout.json').read_text())
bpy.ops.object.select_all(action='SELECT');bpy.ops.object.delete(use_global=False)
def mat(n,rgb,rough=.7):
 m=bpy.data.materials.new(n);m.diffuse_color=(*rgb,1);m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(*rgb,1);p.inputs['Roughness'].default_value=rough;return m
mats={}
for id,name,desc,status,h in json.loads((O/'data/materials.json').read_text()):
 c=tuple((int(h[i:i+2],16)/255)**2.2 for i in [1,3,5]);mats[id]=mat(id+' '+name,c)
 if id in ['M03','M04','M05']:
  nt=mats[id].node_tree;p=nt.nodes.get('Principled BSDF');tex=nt.nodes.new('ShaderNodeTexNoise');tex.inputs['Scale'].default_value=150 if id=='M03' else 350;tex.inputs['Detail'].default_value=2
  bump=nt.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.12;bump.inputs['Distance'].default_value=.0004;nt.links.new(tex.outputs['Fac'],bump.inputs['Height']);nt.links.new(bump.outputs['Normal'],p.inputs['Normal'])
black=mat('TV készüléktest, külön meglévő tétel',(.009,.012,.016),.18);wall=mat('Meleg törtfehér környezet',(.65,.61,.55));metal=mat('Vasalati helyfoglaló',(.12,.32,.36));lightmat=mat('2700K névleges fény jelölése',(.98,.70,.32));pr=lightmat.node_tree.nodes.get('Principled BSDF');pr.inputs['Emission Color'].default_value=(1,.52,.20,1);pr.inputs['Emission Strength'].default_value=3
def box(n,b,ma):
 bpy.ops.mesh.primitive_cube_add(size=1,location=[(b[k]+b[k+3]/2)/1000 for k in range(3)]);o=bpy.context.object;o.name=n;o.dimensions=[v/1000 for v in b[3:]];bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.clear();o.data.materials.append(ma);return o
objs={};proof=[]
for p in parts:
 b=p['box']
 if p.get('mesh_mm'):
  mm=p['mesh_mm'];me=bpy.data.meshes.new(p['id']);me.from_pydata([[v/1000 for v in q]for q in mm['vertices']],[],mm['faces']);me.update();o=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(o);o.data.materials.append(mats[p['material']])
 elif p['axis']=='y' and p['outline']:
  pts=p['outline'];n=len(pts);verts=[((b[0]+x)/1000,y/1000,(b[2]+z)/1000) for y in [b[1],b[1]+b[4]] for x,z in pts];faces=[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)];me=bpy.data.meshes.new(p['id']);me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(o);o.data.materials.append(mats[p['material']])
 else:o=box(p['id'],b,mats[p['material']])
 o['part_id']=p['id'];o['revision']='S16-R14-LIGHT-STUDY';o['cost_id']=p['cost'];o['release']='DESIGN_NOT_RELEASED';objs[p['id']]=o
 coords=[o.matrix_world@Vector(v) for v in o.bound_box];bpy.context.view_layer.update();coords=[o.matrix_world@Vector(v) for v in o.bound_box]
 err=max(abs(min(v[k] for v in coords)*1000-b[k]) for k in range(3));err=max(err,max(abs(max(v[k] for v in coords)*1000-b[k]-b[k+3]) for k in range(3)))
 # Contour approximation can differ at a rounded extent by tiny sampling error only.
 proof.append({'id':p['id'],'bbox_error_mm':err})
# Curved extruded outer surfaces share tangent normals; retain sharp front/back boundaries.
for id in ['CURVE-T-TOP','CURVE-B-TOP','CURVE-B-BOT','CURVE-T-BOT']:
 ob=objs[id]
 for face in ob.data.polygons:face.use_smooth=abs(face.normal.y)<.1
 ob.data.set_sharp_from_angle(angle=math.radians(30))
for part in parts:
 if part.get('exposed_top_finish'):
  ob=objs[part['id']];idx=len(ob.data.materials);ob.data.materials.append(mats[part['exposed_top_finish']])
  for face in ob.data.polygons:
   if face.normal.z>.99:face.material_index=idx
print('Primary meshes built',flush=True)
tv=box('TV-SCREEN',layout['screen_box'],black)
# Actual structural bracket is a placeholder. It is anchored independently into wall, through panels.
br=box('TV-CONSOLE-ENVELOPE',[1937.5,113,1200,675,22,428],metal);br.hide_render=True;br['status']='VESA/anchor/load not released'
hardware=[]
for i,(x,z) in enumerate([(35,650),(35,730),(35,810),(460,650),(460,730)],1):hardware.append(box('CCT-CONTROLLER-'+str(i),[x,60,z,170,53.4,28],metal))
for i,x in enumerate([35,460],1):hardware.append(box('PSU-AMBIENT-'+str(i),[x,55,600,250,72,45],metal))
hardware.append(box('PSU-INTERNAL',[460,55,810,128,60,32],metal))
for o in hardware:o.hide_render=True;o['status']='Gyári/előirányzati helyfoglaló, szerelési távolság és hőpróba nyitott'
leds=[]
for c in lighting['circuits']:
 if c.get('profile_section_xy'):
  pts=c['profile_section_xy'];zs=[c['path'][0][2],c['path'][-1][2]]
  verts=[(x/1000,y/1000,z/1000) for z in zs for x,y in pts]
  faces=[(2,1,0),(3,4,5),(0,1,4,3),(1,2,5,4),(2,0,3,5)]
  mesh=bpy.data.meshes.new(c['id']+'-HOUSING');mesh.from_pydata(verts,[],faces);mesh.update();housing=bpy.data.objects.new(c['id']+'-HOUSING',mesh);bpy.context.collection.objects.link(housing);housing.data.materials.append(mats['M02'])
  x,y,_=c['path'][0];nx,ny,_=c['beam_direction_xyz'];tx,ty=-ny,nx;half=c['diffuser_width_mm']/2
  verts=[((x+sgn*half*tx+.2*nx)/1000,(y+sgn*half*ty+.2*ny)/1000,z/1000) for z in zs for sgn in [-1,1]]
  mesh=bpy.data.meshes.new(c['id']+'-DIFFUSER');mesh.from_pydata(verts,[],[(0,1,3,2)]);mesh.update();o=bpy.data.objects.new(c['id']+'-DIFFUSER',mesh);bpy.context.collection.objects.link(o);o.data.materials.append(lightmat);leds.append(o)
  continue
 for k,(a,b) in enumerate(zip(c['path'],c['path'][1:])):
  d=[max(abs(a[i]-b[i]),4) for i in range(3)];bb=[min(a[i],b[i])- (2 if a[i]==b[i] else 0) for i in range(3)]+d;o=box(c['id']+'-'+str(k),bb,lightmat);leds.append(o)
floor=box('TECHNICAL-FLOOR',[-300,-120,-45,4200,1500,40],wall);back=box('TECHNICAL-WALL',[-300,-60,0,4200,55,2900],wall)
ceiling=box('CEILING-DATUM',[-300,-60,2900,4200,100,40],wall)
def aim(o,p):o.rotation_euler=(Vector(p)-o.location).to_track_quat('-Z','Y').to_euler()
for loc,power,size in [((1,4,5),1100,5),((-3,2,4),900,4),((5,1,4),1300,5)]:
 bpy.ops.object.light_add(type='AREA',location=loc);o=bpy.context.object;o.data.energy=power;o.data.size=size;aim(o,(1.8,0,1.5))
# Local drawing coordinates X=front-view right, Y=towards viewer are mapped by a mirror for Blender's right-handed world.
root=bpy.data.objects.new('LOCAL_TO_BLENDER_X_MIRROR',None);bpy.context.collection.objects.link(root)
for ob in list(bpy.context.scene.objects):
 if ob.type=='MESH':ob.parent=root
root.scale.x=-1
for ob in bpy.context.scene.objects:
 if ob.type=='LIGHT':ob.location.x=-ob.location.x;aim(ob,(-1.8,0,1.5))
bpy.ops.object.camera_add(location=(-5.4,8.5,4.7));cam=bpy.context.object;cam.name='S16_technical_axon';cam.data.type='ORTHO';cam.data.ortho_scale=5.2;aim(cam,(-1.8,.1,1.45));s=bpy.context.scene;s.camera=cam;s.render.engine='CYCLES';s.cycles.samples=16;s.cycles.use_denoising=True;s.render.resolution_x=1600;s.render.resolution_y=1200;s.render.resolution_percentage=100;s.world.color=(.35,.35,.35);s.view_settings.view_transform='AgX';s.view_settings.exposure=-1.2
def render(name):
 return
 if '--reuse-previews' in sys.argv and (O/'nezetek'/name).exists():return
 s.render.filepath=str(O/'nezetek'/name);bpy.ops.render.render(write_still=True)
# Door-controlled shelf lighting: illustrative light levels, not a calibrated photometric calculation.
shelf_lights=[]
for c in lighting['circuits']:
 if not c.get('beam_direction_xyz'):continue
 x,y,z=c['path'][0];z=(z+c['path'][-1][2])/2;nx,ny,_=c['beam_direction_xyz']
 bpy.ops.object.light_add(type='AREA',location=(-(x+.4*nx)/1000,(y+.4*ny)/1000,z/1000));o=bpy.context.object;o.name=c['id']+'-INWARD-LIGHT';o.data.shape='RECTANGLE';o.data.size=.008;o.data.size_y=c['length_mm']/1000;o.data.energy=4
 aim(o,(o.location.x-nx,o.location.y+ny,o.location.z));o.hide_render=True;shelf_lights.append(o)
for o in leds:
 if o.name.startswith('I-'):o.hide_render=True
render('S16_R05_zart.png')
# Open each drawer by its actual planned stroke; door movement about an explicit nominal hinge axis.
for d in drawers:
 if d['id']=='D3':
  for id in d['moving']:objs[id].location.y+=.3
original={}
for id,hingex,angle in [('T-DOOR-L',21,90),('T-DOOR-R',849,-90)]:
 extra=[objs['TEXTILE'],objs['T-DOOR-L-BACK']]+[o for o in leds if o.name.startswith('A4-')] if id.endswith('L') else[]
 pivot=Vector((hingex/1000,.4,.573));rot=Matrix.Translation(pivot)@Matrix.Rotation(math.radians(angle),4,'Z')@Matrix.Translation(-pivot)
 for obj in [objs[id]]+extra:original[obj.name]=obj.matrix_basis.copy();obj.matrix_basis=rot@obj.matrix_basis
for o in shelf_lights:o.hide_render=False
for o in leds:
 if o.name.startswith(('I-TL','I-TR','I-D3-')):o.hide_render=False
render('S16_R05_nyitott.png')
for d in drawers:
 if d['id']=='D3':
  for id in d['moving']:objs[id].location.y-=.3
for id,matrix in original.items():bpy.data.objects[id].matrix_basis=matrix
bpy.context.view_layer.update()
for o in shelf_lights:o.hide_render=True
for o in leds:
 if o.name.startswith('I-'):o.hide_render=True
# Closed lighting study with low ambient illumination; geometry and light paths unchanged.
for ob in bpy.context.scene.objects:
 if ob.type=='LIGHT':ob.data.energy*=.08
s.world.color=(.025,.025,.025);s.view_settings.exposure=0
render('S16_R05_fenyek.png')

# Remove exposed proxy strips from all external circuits.
for o in list(leds):
 if o.name.startswith('A'):bpy.data.objects.remove(o,do_unlink=True)
for ob in list(bpy.data.objects):
 if ob.name.startswith(('CCT-CONTROLLER','PSU-AMBIENT')):bpy.data.objects.remove(ob,do_unlink=True)
# Recessed diffuse emitters; no bloom postprocessing and no painted halo.
em=mat('Rejtett meleg2700K emisszió',(.8,.5,.2));shader=em.node_tree.nodes.get('Principled BSDF');shader.inputs['Emission Color'].default_value=(1,.52,.20,1);shader.inputs['Emission Strength'].default_value=22
print('Lighting build',flush=True)
# Original model uses X mirror, so newly added objects join its parent too.
def emitter(n,verts,faces):
 mesh=bpy.data.meshes.new(n);mesh.from_pydata([(x/1000,y/1000,z/1000)for x,y,z in verts],[],faces);mesh.update();ob=bpy.data.objects.new(n,mesh);bpy.context.collection.objects.link(ob);ob.data.materials.append(em);ob.parent=root;return ob
for c in lighting['circuits']:
 if c['id'] not in ['A1-OUTER-UP','A2-OUTER-LOW','A3-TV-CONTOUR']:continue
 path=c['path'];verts=[];faces=[]
 if c['id']=='A2-OUTER-LOW':
  path=[[(p[0]-1800)*3540/3580+1800,p[1],250+(p[2]-250)*2595/2615 if c['id']=='A1-OUTER-UP' else p[2]] for p in path]
 for a,b in zip(path,path[1:]):
  dx=b[0]-a[0];dz=b[2]-a[2];ll=math.hypot(dx,dz)
  if ll<.00001:continue
  nx,nz=dz/ll,-dx/ll
  if c['id']=='A3-TV-CONTOUR':
   # Offset inside the opaque TV panel, so only reflected light emerges.
   for pt,sign in [(a,-1),(b,-1),(b,1),(a,1)]:verts.append((pt[0]+(22+sign*5)*nx,88,pt[2]+(22+sign*5)*nz))
  elif c['id']=='A4-TEXTILE-LOOP':
   # Strip mounted on edge below the overhanging textile plaque; emitter is15mm deep.
   verts.extend([(a[0],394,a[2]),(b[0],394,b[2]),(b[0],408.5,b[2]),(a[0],408.5,a[2])])
  else:
   for pt,sign in [(a,-1),(b,-1),(b,1),(a,1)]:verts.append((pt[0]+sign*5*nx,pt[1],pt[2]+sign*5*nz))
  j=len(verts)-4;faces.append((j,j+1,j+2,j+3))
 emitter(c['id']+'-CONCEALED',verts,faces)
# Continuous curved lower light shield: no stub end at tower or right radius.
bottompath=[(870,570),(3498,570)]
def offset_path(path,t):
 normals=[]
 for a,b in zip(path,path[1:]):
  dx,dz=b[0]-a[0],b[1]-a[1];ll=math.hypot(dx,dz);normals.append((-dz/ll,dx/ll))
 out=[]
 for i,p in enumerate(path):
  if i==0:n=normals[0]
  elif i==len(path)-1:n=normals[-1]
  else:
   a,b=normals[i-1],normals[i];v=(a[0]+b[0],a[1]+b[1]);den=v[0]*a[0]+v[1]*a[1];n=(v[0]/den,v[1]/den)
  out.append((p[0]+t*n[0],p[1]+t*n[1]))
 return out
def ribbon(name,t0,t1,y0,y1,material,path=None):
 path=path or bottompath;a=offset_path(path,t0);b=offset_path(path,t1);vv=[];ff=[]
 for u,v in zip(a,b):vv.extend([(u[0],y0,u[1]),(v[0],y0,v[1]),(u[0],y1,u[1]),(v[0],y1,v[1])])
 for i in range(len(path)-1):
  j=i*4;ff.extend([tuple(j+k for k in f)for f in [(0,4,6,2),(1,3,7,5),(0,1,5,4),(2,6,7,3)]])
 ff.append((0,2,3,1));j=(len(path)-1)*4;ff.append((j,j+1,j+3,j+2))
 ob=emitter(name,vv,ff);ob.data.materials.clear();ob.data.materials.append(material)
 import bmesh
 bm=bmesh.new();bm.from_mesh(ob.data);bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bm.to_mesh(ob.data);bm.free()
 return ob

lowercover=ribbon('DECK-CONTINUOUS-COVER',22,26,101,109,mats['M03'])
endcap=objs['TV-FIELD'] # Existing panel already closes the channel terminal.
lowerbaffle=ribbon('DECK-CONTINUOUS-BAFFLE',9,26,109,113,mats['M03'])
vv=[];ff=[]
for a,b in zip(bottompath,bottompath[1:]):
 dx,dz=b[0]-a[0],b[1]-a[1];ll=math.hypot(dx,dz);nx,nz=-dz/ll,dx/ll;j=len(vv)
 vv.extend([(p[0]+t*nx,y,p[1]+t*nz)for p,t,y in [(a,25.5,107),(b,25.5,107),(b,11,107),(a,11,107)]]);ff.append((j,j+1,j+2,j+3))
emitter('A5-CONTINUOUS-CONCEALED',vv,ff)
# Concealed underside light supplements the reflected lower halo, within the same A2 scene.
emitter('A2-UNDERSIDE',[(100,280,148),(3500,280,148),(3500,294.5,148),(100,294.5,148)],[(0,1,2,3)])
# A concealed upper return lights the textured panel face downward.
top_path=[(3597,2875),(740,2875)]
topcover=ribbon('TOP-WASH-COVER',0,3,26,34,mats['M04'],top_path)
topbaffle=ribbon('TOP-WASH-BAFFLE',0,18,34,38,mats['M04'],top_path)
# Conceal the profile junction behind the full opaque cabinet silhouette.
# Using the hollow shell as a cutter leaves exposed islands inside its contour.
maskpts=[(0,570),(870,570)]+[(770+100*math.cos(math.radians(i*90/64)),2775+100*math.sin(math.radians(i*90/64)))for i in range(65)]+[(0,2875)]
n=len(maskpts);vv=[(x,y,z)for y in [40,400]for x,z in maskpts];ff=[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n)for i in range(n)]
mask=emitter('TEMP-OPAQUE-TOWER-ENVELOPE',vv,ff)
import bmesh
bm=bmesh.new();bm.from_mesh(mask.data);bmesh.ops.recalc_face_normals(bm,faces=list(bm.faces));bmesh.ops.triangulate(bm,faces=list(bm.faces));bm.to_mesh(mask.data);bm.free();bpy.context.view_layer.update()
for ob in [topcover,topbaffle]:
 m=ob.modifiers.new('concealed_full_outline_join','BOOLEAN');m.operation='DIFFERENCE';m.solver='EXACT';m.object=mask;bpy.context.view_layer.objects.active=ob;bpy.ops.object.modifier_apply(modifier=m.name)
bpy.data.objects.remove(mask,do_unlink=True)
cap=box('TOP-WASH-HIDDEN-END',[3595,26,2857,2,8,15],mats['M04']);cap.parent=root

vv=[];ff=[]
top_light_path=[(3585,2875),(880,2875)]
for a,b in zip(top_light_path,top_light_path[1:]):
 dx,dz=b[0]-a[0],b[1]-a[1];ll=math.hypot(dx,dz);nx,nz=-dz/ll,dx/ll;j=len(vv)
 vv.extend([(p[0]+t*nx,y,p[1]+t*nz)for p,t,y in [(a,3.25,31),(b,3.25,31),(b,17.75,31),(a,17.75,31)]]);ff.append((j,j+1,j+2,j+3))
downlight=emitter('TOP-WASH-EMITTER',vv,ff)
downmat=em.copy();downmat.name='Felső lefelé súrolófény';downmat.node_tree.nodes.get('Principled BSDF').inputs['Emission Strength'].default_value=35;downlight.data.materials.clear();downlight.data.materials.append(downmat)
bpy.ops.object.light_add(type='AREA',location=(-2.235,.031,2.860));topwash=bpy.context.object;topwash.name='TOP-PANEL-GRAZING-LIGHT';topwash.data.shape='RECTANGLE';topwash.data.size=2.7;topwash.data.size_y=.0145;topwash.data.energy=4;topwash.data.color=(1,.52,.20);aim(topwash,(-2.235,.026,2.55))
# Independent upward light in the nominal25mm ceiling gap; all parts behind cabinet rear Y40.
for n,b in [('UPLIGHT-TRAY',[740,5,2875,2845,24,1]),('UPLIGHT-FRONT-VISOR',[740,25,2876,2845,4,3]),('UPLIGHT-REAR-VISOR',[740,5,2876,2845,3,3])]:
 ob=box(n,b,mats['M04']);ob.parent=root
uplight=emitter('A8-UPWARD-CEILING-GAP',[(745,8,2876.2),(3580,8,2876.2),(3580,22.5,2876.2),(745,22.5,2876.2)],[(0,1,2,3)])
upmat=em.copy();upmat.name='Felfelé plafonrés';upmat.node_tree.nodes.get('Principled BSDF').inputs['Emission Strength'].default_value=16;uplight.data.materials.clear();uplight.data.materials.append(upmat)
# The front lip conceals the inward-facing light around the textile inset.
# This is a profile study, not a claimed fit for a selected Hue SKU.
def ring(name,outer,inner,y0,y1):
 n=len(outer);vv=[(x,y,z) for y in [y0,y1] for loop in [outer,inner] for x,z in loop];ff=[]
 for i in range(n):
  j=(i+1)%n;ff.extend([(i,j,2*n+j,2*n+i),(n+j,n+i,3*n+i,3*n+j),(i,n+i,n+j,j),(2*n+j,3*n+j,3*n+i,2*n+i)])
 ob=emitter(name,vv,ff);ob.data.materials.clear();ob.data.materials.append(mats['M02']);return ob
from math import sin,cos,pi
def roundrect(x,z,w,h,r):
 out=[]
 for cx,cz,start in [(x+w-r,z+r,-90),(x+w-r,z+h-r,0),(x+r,z+h-r,90),(x+r,z+r,180)]:
  for i in range(33):
   a=math.radians(start+i*90/32);out.append((cx+r*cos(a),cz+r*sin(a)))
 return out
# Recessed cassette; door face Y400, textile face Y374. No raised front rim.
backrim=ring('TEXTILE-RECESSED-HOUSING',roundrect(42,250,370,2525,65),roundrect(46,254,362,2517,61),366,382)
loop=roundrect(47,255,360,2515,60);loop.append(loop[0]);vv=[];ff=[]
for a,b in zip(loop,loop[1:]):
 j=len(vv);vv.extend([(a[0],377.5,a[1]),(b[0],377.5,b[1]),(b[0],392,a[1] if False else b[1]),(a[0],392,a[1])]);ff.append((j,j+1,j+2,j+3))
inward=emitter('TEXTILE-RECESSED-EMITTER',vv,ff)
lowshield=box('LOW-INTERNAL-LIGHT-VISOR',[57,359,554,306,5,16],mats['M02']);lowshield.parent=root
# Additional very soft floor bounce remains physically generated by the existing underside emitter.
# Very low room ambient; retained only to make dark furniture edges readable.
for ob in bpy.context.scene.objects:
 if ob.type=='LIGHT' and ob not in shelf_lights and ob.name!='TOP-PANEL-GRAZING-LIGHT':ob.data.energy*=.055
s.world.color=(.001,.001,.001);s.view_settings.exposure=1.1;s.cycles.samples=32;s.cycles.use_denoising=True
s.render.resolution_x=1280;s.render.resolution_y=960
# Warm neutral instead of decorative RGB for an honest first view.
def out(name):
 if '--open-only' in sys.argv and name.endswith('csukott.png'):return
 s.render.filepath=str(O/'nezetek'/name);bpy.ops.render.render(write_still=True)
style='femes' if '--metal' in sys.argv else 'faerezet';day='--day' in sys.argv
paint=mat('Szatén fémes szürkésbarna mintajavaslat',(.065,.061,.048),.38)
paint.node_tree.nodes.get('Principled BSDF').inputs['Metallic'].default_value=.38
# Reference palette. Shared object coordinates keep grain continuous across fronts.
def wood_shader(name,direction,dark,light):
 ma=mat(name,dark,.58);nt=ma.node_tree;bs=nt.nodes.get('Principled BSDF');co=nt.nodes.new('ShaderNodeTexCoord');co.object=root
 scale=nt.nodes.new('ShaderNodeVectorMath');scale.operation='MULTIPLY';scale.inputs[1].default_value={'horizontal':(2,45,180),'vertical':(180,45,2),'floor':(120,2,35)}[direction];nt.links.new(co.outputs['Object'],scale.inputs[0])
 noise=nt.nodes.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=2;noise.inputs['Detail'].default_value=2.5;noise.inputs['Roughness'].default_value=.65;nt.links.new(scale.outputs[0],noise.inputs['Vector'])
 ramp=nt.nodes.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(*dark,1);ramp.color_ramp.elements[1].color=(*light,1);nt.links.new(noise.outputs['Fac'],ramp.inputs[0]);nt.links.new(ramp.outputs[0],bs.inputs['Base Color'])
 bump=nt.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=.12;bump.inputs['Distance'].default_value=.00015;nt.links.new(noise.outputs['Fac'],bump.inputs['Height']);nt.links.new(bump.outputs[0],bs.inputs['Normal']);return ma
wood_h=wood_shader('M03 referencia – vízszintes füstös fa','horizontal',(.018,.014,.011),(.043,.034,.027))
wood_v=wood_shader('M03 referencia – függőleges füstös fa','vertical',(.018,.014,.011),(.043,.034,.027))
for part in parts:
 if part['material']=='M03':
  ob=objs[part['id']];ob.data.materials.clear();ob.data.materials.append(wood_h if part['grain'].startswith('U') else wood_v)
for ob in [lowercover,lowerbaffle]:ob.data.materials.clear();ob.data.materials.append(wood_v)
floormat=wood_shader('Referencia – meleg szürkés tölgy padlótónus','floor',(.16,.125,.087),(.29,.235,.17));floor.data.materials.clear();floor.data.materials.append(floormat)
# Textile background: restrained colour variation and fine physical surface relief.
for mid,base,strength in [('M04',(.12,.095,.073),.16),('M05',(.57,.50,.38),.20)]:
 ma=mats[mid];nt=ma.node_tree;bs=nt.nodes.get('Principled BSDF');bs.inputs['Roughness'].default_value=.88
 co=nt.nodes.new('ShaderNodeTexCoord');co.object=root;noise=nt.nodes.new('ShaderNodeTexNoise');noise.inputs['Scale'].default_value=260;noise.inputs['Detail'].default_value=2;nt.links.new(co.outputs['Object'],noise.inputs['Vector'])
 ramp=nt.nodes.new('ShaderNodeValToRGB');ramp.color_ramp.elements[0].color=(*(v*.88 for v in base),1);ramp.color_ramp.elements[1].color=(*(v*1.12 for v in base),1);nt.links.new(noise.outputs['Fac'],ramp.inputs[0]);nt.links.new(ramp.outputs[0],bs.inputs['Base Color'])
 bump=nt.nodes.new('ShaderNodeBump');bump.inputs['Strength'].default_value=strength;bump.inputs['Distance'].default_value=.00035;nt.links.new(noise.outputs['Fac'],bump.inputs['Height']);nt.links.new(bump.outputs[0],bs.inputs['Normal'])
# Keep textile readable under its edge light, rather than making it look self-lit.
insert_em=em.copy();insert_em.name='Rejtett betétperem – visszafogott meleg fény';insert_em.node_tree.nodes.get('Principled BSDF').inputs['Emission Strength'].default_value=10;inward.data.materials.clear();inward.data.materials.append(insert_em)
for ob in bpy.data.objects:
 if ob.type=='LIGHT' and ob.name.startswith('Area'):
  ob.data.color=(1,.85,.69);ob.data.energy*=8 if not day else 2
if style=='femes':
 for ob in [objs['TV-FIELD'],lowercover,lowerbaffle,endcap]:ob.data.materials.clear();ob.data.materials.append(paint)
if day:
 # Window position/orientation is loaded from independently documented room evidence.
 cfg=json.loads((O/'data/daylight_context.json').read_text());bpy.ops.object.light_add(type='AREA',location=cfg['window_light_location_blender_m']);win=bpy.context.object;win.name='ROOM-WINDOW-DIFFUSE';win.data.shape='RECTANGLE';win.data.size=cfg['window_size_m'][0];win.data.size_y=cfg['window_size_m'][1];win.data.energy=cfg['illustrative_energy_W'];win.data.color=(.88,.94,1);win.rotation_euler=(math.pi/2,0,-math.pi/2);s.world.color=(.12,.12,.12);s.view_settings.exposure=.2
 for ob in bpy.data.objects:
  if ob.type=='MESH':
   for ma in ob.data.materials:
    if ma and ma.use_nodes:
     for node in ma.node_tree.nodes:
      if node.type=='BSDF_PRINCIPLED':node.inputs['Emission Strength'].default_value=0
 for ob in bpy.data.objects:
  if ob.type=='LIGHT'and ob.name in ['TOP-PANEL-GRAZING-LIGHT']:ob.data.energy=0
bpy.context.view_layer.update()
if '--check-only' in sys.argv:
 hits=[]
 for x,z in [(100,400),(200,1500),(300,2600)]:
  hit,loc,normal,idx,obj,matrix=s.ray_cast(bpy.context.evaluated_depsgraph_get(),Vector((-x/1000,1,z/1000)),Vector((0,-1,0)))
  hits.append({'x_mm':x,'z_mm':z,'object':obj.name if obj else None,'y_mm':loc.y*1000 if hit else None})
 assert all(q['object']=='TEXTILE' for q in hits),hits
 (O/'audit/insert_visibility.json').write_text(json.dumps(hits,indent=2))
 print('RECESSED_TEXTILE_VISIBLE',hits,flush=True)
 bpy.ops.wm.quit_blender();raise SystemExit(0)
if '--preview' in sys.argv:
 s.render.resolution_percentage=50;s.cycles.samples=8;out('S16_R14_edge_preview.png');bpy.ops.wm.quit_blender();raise SystemExit(0)
out(f'S16_R14_{style}_{"nappal" if day else "este"}_csukott.png')
if '--details' in sys.argv:
 for name,x,z in [('felso_csatlakozas',.84,2.80),('felso_jobb_iv',3.51,2.78),('also_jobb_csatlakozas',3.51,.57)]:
  cam.location=(-(x+1.1),3.5,z+1.25);aim(cam,(-x,.13,z));cam.data.ortho_scale=.64
  out('S16_R14_reszlet_'+name+'.png')
 bpy.ops.wm.quit_blender();raise SystemExit(0)


if not day:
 oldloc=cam.location.copy();oldrot=cam.rotation_euler.copy();oldscale=cam.data.ortho_scale
 cam.location=(-3.0,4.5,2.65);aim(cam,(-2.2,.02,2.78));cam.data.ortho_scale=1.7
 out('S16_R14_felso_ketiranyu_feny.png')
 cam.location=oldloc;cam.rotation_euler=oldrot;cam.data.ortho_scale=oldscale
# Open doors and one drawer; the internal lighting follows their sensors.
for d in drawers:
 if d['id']=='D3':
  for id in d['moving']:objs[id].location.y+=.3
for id,hingex,angle in [('T-DOOR-L',21,90),('T-DOOR-R',849,-90)]:
 extra=[objs['TEXTILE'],objs['T-DOOR-L-BACK'],backrim,inward] if id.endswith('L') else []
 pivot=Vector((hingex/1000,.4,.573));rot=Matrix.Translation(pivot)@Matrix.Rotation(math.radians(angle),4,'Z')@Matrix.Translation(-pivot)
 for ob in [objs[id]]+extra:ob.matrix_basis=rot@ob.matrix_basis
for ob in shelf_lights:ob.hide_render=False;ob.data.energy=2.5;ob.data.color=(1,.52,.20)
for ob in bpy.data.objects:
 if ob.name.startswith(('I-TL-DIFFUSER','I-TR-DIFFUSER','I-D3-','I-TL-LOW-')):ob.hide_render=False
bpy.ops.object.light_add(type='AREA',location=(-1.485,.356,.547));dl=bpy.context.object;dl.name='D3-CONCEALED-INWARD-LIGHT';dl.data.shape='RECTANGLE';dl.data.size=.28;dl.data.size_y=.008;dl.data.energy=.6;dl.data.color=(1,.52,.20);aim(dl,(-1.485,.54,.3))
bpy.ops.object.light_add(type='AREA',location=(-.21,.355,.566));low=bpy.context.object;low.name='LEFT-LOW-CONCEALED-LIGHT';low.data.shape='RECTANGLE';low.data.size=.30;low.data.size_y=.008;low.data.energy=.6;low.data.color=(1,.52,.20);aim(low,(-.21,.20,.30))

if not day:out(f'S16_R14_{style}_este_nyitott.png')

if not day:bpy.ops.wm.save_as_mainfile(filepath=str(O/'rajzok'/f'S16_R14_{style}.blend'))
