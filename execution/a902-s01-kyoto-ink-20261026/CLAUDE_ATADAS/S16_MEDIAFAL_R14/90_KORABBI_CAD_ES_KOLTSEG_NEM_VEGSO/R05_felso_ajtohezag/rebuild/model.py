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
black=mat('TV készüléktest, külön meglévő tétel',(.009,.012,.016),.18);wall=mat('Semleges műszaki háttér',(.68,.68,.65));metal=mat('Vasalati helyfoglaló',(.12,.32,.36));lightmat=mat('2700K névleges fény jelölése',(.98,.70,.32));pr=lightmat.node_tree.nodes.get('Principled BSDF');pr.inputs['Emission Color'].default_value=(1,.55,.19,1);pr.inputs['Emission Strength'].default_value=3
def box(n,b,ma):
 bpy.ops.mesh.primitive_cube_add(size=1,location=[(b[k]+b[k+3]/2)/1000 for k in range(3)]);o=bpy.context.object;o.name=n;o.dimensions=[v/1000 for v in b[3:]];bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);o.data.materials.clear();o.data.materials.append(ma);return o
objs={};proof=[]
for p in parts:
 b=p['box']
 if p['axis']=='y' and p['outline']:
  pts=p['outline'];n=len(pts);verts=[((b[0]+x)/1000,y/1000,(b[2]+z)/1000) for y in [b[1],b[1]+b[4]] for x,z in pts];faces=[tuple(range(n-1,-1,-1)),tuple(range(n,n*2))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)];me=bpy.data.meshes.new(p['id']);me.from_pydata(verts,[],faces);me.update();o=bpy.data.objects.new(p['id'],me);bpy.context.collection.objects.link(o);o.data.materials.append(mats[p['material']])
 else:o=box(p['id'],b,mats[p['material']])
 o['part_id']=p['id'];o['revision']='S16-R05';o['cost_id']=p['cost'];o['release']='DESIGN_NOT_RELEASED';objs[p['id']]=o
 coords=[o.matrix_world@Vector(v) for v in o.bound_box];bpy.context.view_layer.update();coords=[o.matrix_world@Vector(v) for v in o.bound_box]
 err=max(abs(min(v[k] for v in coords)*1000-b[k]) for k in range(3));err=max(err,max(abs(max(v[k] for v in coords)*1000-b[k]-b[k+3]) for k in range(3)))
 # Contour approximation can differ at a rounded extent by tiny sampling error only.
 proof.append({'id':p['id'],'bbox_error_mm':err})
# A real pocket in the moving left door supports the complete light loop.
p=next(p for p in parts if p.get('light_groove'));g=p['light_groove'];b=p['box'];out=g['outer'];inn=g['inner'];n=len(out)
verts=[((b[0]+x)/1000,y/1000,(b[2]+z)/1000) for y in [394,400.1] for loop in [out,inn] for x,z in loop]
faces=[]
for i in range(n):
 j=(i+1)%n
 faces.extend([(i,j,2*n+j,2*n+i),(n+j,n+i,3*n+i,3*n+j),(i,n+i,n+j,j),(2*n+j,3*n+j,3*n+i,2*n+i)])
me=bpy.data.meshes.new('LIGHT-GROOVE-CUT');me.from_pydata(verts,[],faces);me.update();cut=bpy.data.objects.new('LIGHT-GROOVE-CUT',me);bpy.context.collection.objects.link(cut)
mod=objs[p['id']].modifiers.new('10x6mm perimeter pocket','BOOLEAN');mod.operation='DIFFERENCE';mod.object=cut;mod.solver='EXACT';bpy.context.view_layer.objects.active=objs[p['id']];bpy.ops.object.modifier_apply(modifier=mod.name);bpy.data.objects.remove(cut,do_unlink=True)
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
 if '--reuse-previews' in sys.argv and (O/'nezetek'/name).exists():return
 s.render.filepath=str(O/'nezetek'/name);bpy.ops.render.render(write_still=True)
render('S16_R05_zart.png')
# Open each drawer by its actual planned stroke; door movement about an explicit nominal hinge axis.
for d in drawers:
 if d['id']=='D3':
  for id in d['moving']:objs[id].location.y+=.3
original={}
for id,hingex,angle in [('T-DOOR-L',21,90),('T-DOOR-R',849,-90)]:
 extra=[objs['TEXTILE']]+[o for o in leds if o.name.startswith('A4-')] if id.endswith('L') else[]
 pivot=Vector((hingex/1000,.4,.573));rot=Matrix.Translation(pivot)@Matrix.Rotation(math.radians(angle),4,'Z')@Matrix.Translation(-pivot)
 for obj in [objs[id]]+extra:original[obj.name]=obj.matrix_basis.copy();obj.matrix_basis=rot@obj.matrix_basis
render('S16_R05_nyitott.png')
for d in drawers:
 if d['id']=='D3':
  for id in d['moving']:objs[id].location.y-=.3
for id,matrix in original.items():bpy.data.objects[id].matrix_basis=matrix
bpy.context.view_layer.update()
# Closed lighting study with low ambient illumination; geometry and light paths unchanged.
for ob in bpy.context.scene.objects:
 if ob.type=='LIGHT':ob.data.energy*=.08
s.world.color=(.025,.025,.025);s.view_settings.exposure=0
render('S16_R05_fenyek.png')
bpy.ops.wm.save_as_mainfile(filepath=str(O/'rajzok/S16_R05_koordinacio.blend'))
(O/'audit/blender_readback.json').write_text(json.dumps({'parts':proof,'max_bbox_error_mm':max(p['bbox_error_mm'] for p in proof),'render_status':'TECHNICAL_CONTROL, műszaki anyagszín és stúdiófény; nem Cam_02 végső lakásrender','parts_count':len(parts),'door_sweep':'Névleges90° pivot, nem gyári pántkinematika','hardware':'Helyfoglaló, nem gyártói test','external_dependencies':'Procedurális textúrák; külső textúra nincs'},ensure_ascii=False,indent=2))
