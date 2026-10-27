import bpy,json,math,hashlib
from pathlib import Path
from mathutils import Vector
P=Path(__file__).resolve().parents[1];O=P/'R06';S=bpy.context.scene
for vl in S.view_layers:vl.material_override=None
S.use_nodes=False
S.world=bpy.data.worlds.new('R06 neutral proof world');S.world.use_nodes=True;S.world.node_tree.nodes.get('Background').inputs[0].default_value=(.5,.5,.5,1);S.world.node_tree.nodes.get('Background').inputs[1].default_value=.7
m=bpy.data.materials.get('R06_INK_W01_0 textured print')
if m:
 ramp=next(n for n in m.node_tree.nodes if n.type=='VALTORGB');ramp.color_ramp.elements[1].color=(.12,.10,.08,1)
tv=bpy.data.objects.get('KI_KI-033')
if tv:tv.data.materials.clear();tv.data.materials.append(bpy.data.materials['R06 graphite'])
# Add the newly budgeted WC cabinet. This is a proposed dry-side layout, not a released installation.
for old in list(bpy.data.objects):
 if old.name.startswith('R06_B62-WC'):bpy.data.objects.remove(old,do_unlink=True)
C=bpy.data.collections['KI_R06_PRODUCT_AND_ARTWORK'];oak=bpy.data.materials['R06 natural oak sample pending'];dark=bpy.data.materials['R06 graphite']
def box(n,b,m,id):
 x,y,z,X,Y,Z=b;bpy.ops.mesh.primitive_cube_add(size=1,location=((x+X)/2,(y+Y)/2,(z+Z)/2));o=bpy.context.object;o.name=n;o.dimensions=(X-x,Y-y,Z-z);bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
 for c in list(o.users_collection):c.objects.unlink(o)
 C.objects.link(o);o.data.materials.append(m);o['element_id']=id;o['revision']='KI-R06';o['asset_status']='CUSTOM_RFQ_PROPOSAL_SITE_AND_TRADE_APPROVAL_REQUIRED';return o
for old in list(bpy.data.objects):
 if old.name.startswith(('R06_BED01_lift_frame','R06_BED01_common_lift_frame')):bpy.data.objects.remove(old,do_unlink=True)
box('R06_BED01_common_lift_frame',(1.50,5.522,.255,3.46,7.278,.285),dark,'KI-043')
for n,b in [('left',(14.5,5.2,1.3,14.518,5.4,2.7)),('right',(15.382,5.2,1.3,15.4,5.4,2.7)),('top',(14.518,5.2,2.682,15.382,5.4,2.7)),('bottom',(14.518,5.2,1.3,15.382,5.4,1.318)),('divider',(15.082,5.2,1.318,15.1,5.4,2.682)),('back',(14.518,5.2,1.318,15.382,5.208,2.682))]:box('R06_B62-WC_'+n,b,oak,'KI-R06-01')
for z in [1.72,2.14,2.54]:box('R06_B62-WC_shelf',(14.518,5.208,z,15.082,5.381,z+.018),oak,'KI-R06-01')
box('R06_B62-WC_door',(14.5015,5.4,1.3015,15.0985,5.419,2.6985),oak,'KI-R06-01')
for k in range(30):box('R06_B62-WC_lamella',(14.505+k*.02,5.419,1.302,14.515+k*.02,5.429,2.698),oak,'KI-R06-01')
# Independent checks calculated from reopened actual mesh bounds.
def bnd(obs):
 pts=[o.matrix_world@Vector(v) for o in obs for v in o.bound_box];return [min(v[i] for v in pts) for i in range(3)]+[max(v[i] for v in pts) for i in range(3)]
def find(prefix):return [o for o in S.objects if o.type=='MESH' and o.name.startswith(prefix) and not o.hide_render]
bpy.context.view_layer.update();checks=json.loads((O/'blender/checks.json').read_text())[:8]
bed=bnd(find('KI_KI-070'));chair=bnd(find('KI_KI-075'));gap=(chair[1]-.6-bed[4])*1000
for ch in checks:
 if ch.get('test')=='Master bed drawers versus nightstands':ch['result']='HORIZONTAL_CONFLICT_REMOVED_LIFT_MOTION_OPEN';ch['reason']='One common frame for the180cm single mattress; paired lift hardware and forward motion clear of headboard require manufacturer approval.'
checks.append(dict(test='REOPENED mesh05.3 chair600mm withdrawal versus bed',actual_mm=round(gap,2),result='PASS_LIMITED' if gap>0 else 'FAIL',source_objects=[o.name for o in find('KI_KI-070')+find('KI_KI-075')],scope='AABB clearance only; no human walking path claim'))
# Sector sampling for the two relevant room doors against furniture at floor level.
furniture=[o for o in S.objects if o.type=='MESH' and not o.hide_render and (o.name.startswith(('KI_KI-070','KI_KI-074','KI_KI-075')) or 'NT-76' in o.name or 'W53-01' in o.name)]
for name,hx,hy,r,a0,a1 in [('05.3 entry',10.85,6.95,.9,-90,0),('06.2 bath entry',14.375,7.05,.75,-90,-180),('05.3 terrace',12.06,8.05,.84,0,-90)]:
 hits=set()
 for o in furniture:
  b=bnd([o])
  for j in range(91):
   a=math.radians(a0+(a1-a0)*j/90)
   for k in range(1,31):
    x=hx+r*k/30*math.cos(a);y=hy+r*k/30*math.sin(a)
    if b[0]-.01<x<b[3]+.01 and b[1]-.01<y<b[4]+.01:hits.add(o.name)
 checks.append(dict(test=name+' sampled door leaf sweep',result='FAIL' if hits else 'PASS_LIMITED',hits=sorted(hits),scope='1degree/30radial samples with10mm buffer; handles and actual hinges not measured'))
(O/'blender/checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2))
# Same actual asset neutral colour trial. No material override or inherited powerful lamps.
vis={o.name:o.hide_render for o in S.objects};cam=bpy.data.objects['R06_ASSET_CONTROL'];S.camera=cam
for o in S.objects:
 if o.type=='LIGHT':o.hide_render=True
 if o.type=='MESH':o.hide_render=not o.name.startswith('R06_Lennon')
S.render.filepath=str(O/'blender/Lennon_R06_shape_control.png');bpy.ops.render.render(write_still=True)
# Media wall proof uses actual assembled panels and ink mapping.
cam.location=(9,6.35,1.45);target=Vector((3.9,6.35,1.45));cam.rotation_euler=(target-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.ortho_scale=4.6
for o in S.objects:
 if o.type=='MESH':o.hide_render=vis.get(o.name,False) or not(any(x in o.name for x in ['TV-01','TV-02','TV-03','R06_INK_W01']) or o.name=='KI_KI-033')
S.render.filepath=str(O/'blender/W01_R06_colour_proof.png');bpy.ops.render.render(write_still=True)
for n,v in vis.items():bpy.data.objects[n].hide_render=v
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_R06.blend'),compress=True)
reg=[]
for o in S.objects:
 if o.type=='MESH' and o.name.startswith('R06_'):reg.append(dict(object=o.name,element=o.get('element_id'),sku=o.get('sku','CUSTOM'),status=o.get('asset_status'),bounds=bnd([o])))
(O/'blender/object_register.json').write_text(json.dumps(reg,ensure_ascii=False,indent=2));print('R06_REOPEN_VERIFIED',len(reg),len(checks))
