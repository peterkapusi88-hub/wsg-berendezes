import bpy,math,json,hashlib
from pathlib import Path
from mathutils import Vector
from mathutils.bvhtree import BVHTree
P=Path(__file__).resolve().parents[1];O=P/'R10';S=bpy.context.scene;src=Path(bpy.data.filepath);sh=hashlib.sha256(src.read_bytes()).hexdigest()
# Reuse tested mesh primitives only, not prior design mutations.
code=Path(__file__).with_name('r09_living.py').read_text().split('# Correct materials')[0]
exec(code.replace("O=P/'R09_living'","O=P/'R10'").replace("'R09_COMPLETE_LIVING'","'R10_MEDIA_WALL'"))
for ob in list(S.objects):
 if ob.type=='MESH' and (any(n in ob.name for n in ['TV-01','TV-02','TV-03','R06_INK_W01']) or ob.name.startswith('R09_art_book') or ob.name=='R09_broad_ceramic_bowl'):ob.hide_render=True
# 4000mm source wall4.05..8.05;3600mm proposal4.35..7.95.
# Tower720 / physical shadow reveal120 / four690mm print fields.
char=mat('R10 EGGER U961 ST7 proposed sample',(.045,.048,.05),220);ground=mat('R10 matte printed fibre cool greige',(.40,.38,.34),350)
parts=[]
def B(n,x,y,z,w,d,h,m,id):
 ob=box(n,(x+w/2,y+d/2,z+h/2),(w,d,h),m,id,.001);ob.name=ob.name.replace('R09_','R10_');parts.append(ob);return ob
for k,(y,d) in enumerate([(4.35,.72),(5.19,.69),(5.88,.69),(6.57,.69),(7.26,.69)]):
 B('TV02_carcass_'+str(k),3.71,y,.15,.382,d,.4,char,'KI-031');B('TV02_front_'+str(k),4.092,y+.0015,.1515,.018,d-.003,.397,char,'KI-031')
B('TV02_recess_infill',3.71,5.07,.15,.22,.12,.4,char,'KI-031')
B('TV02_continuous_top',3.71,4.35,.532,.4,3.6,.018,char,'KI-031')
# Visible tower, not a generic white cuboid. Upper front starts above lower cabinet.
B('TV01_tower_body',3.71,4.35,.55,.382,.72,2.33,char,'KI-030')
for k in range(2):B('TV01_upper_front_'+str(k),4.092,4.3515+k*.36,.5515,.018,.357,2.327,char,'KI-030')
B('TV_gap_120_recess',3.674,5.07,.55,.018,.12,2.33,char,'KI-030')
for k in range(4):B('TV03_panel_'+str(k),3.674,5.1915+k*.69,.55,.036,.687,2.33,ground,'KI-030')
# Remap same artwork continuously over the wider physical design; no relief.
mask=bpy.data.images.get('INK-W01_mask.png')
if mask is None:mask=bpy.data.images.load(str(P/'R06/artwork/INK-W01_mask.png'));mask.pack()
for i,(a,b,x) in enumerate([(0,.36,4.111),(.36,.72,4.111),(.84,1.53,3.711),(1.53,2.22,3.711),(2.22,2.91,3.711),(2.91,3.6,3.711)]):
 vs=[(x,4.35+a+.0015,.55),(x,4.35+b-.0015,.55),(x,4.35+b-.0015,2.88),(x,4.35+a+.0015,2.88)];ob=mesh('INK_R10_'+str(i),vs,[(0,1,2,3)],ground,'KI-030');ob.name=ob.name.replace('R09_','R10_');me=ob.data;uv=me.uv_layers.new(name='Print');coords=[(a/3.6,0),(b/3.6,0),(b/3.6,1),(a/3.6,1)]
 for lp in me.loops:uv.data[lp.index].uv=coords[lp.vertex_index]
 m=mat('R10 print '+str(i),(.4,.38,.34),300);nt=m.node_tree;t=nt.nodes.new('ShaderNodeTexImage');t.image=mask;r=nt.nodes.new('ShaderNodeValToRGB');r.color_ramp.elements[0].color=(.012,.011,.009,1);r.color_ramp.elements[1].color=(*((.065,.06,.05) if i<2 else (.42,.40,.36)),1);nt.links.new(t.outputs['Color'],r.inputs[0]);nt.links.new(r.outputs[0],nt.nodes.get('Principled BSDF').inputs['Base Color']);ob.data.materials.clear();ob.data.materials.append(m)
# Explicit concealed profiles for top, reveal and underside, no front-edge glowing seam.
for n,x,y,z,w,d,h in [('TOP',3.71,5.19,2.865,.018,2.76,.015),('VERT',3.94,5.075,.55,.015,.015,2.33),('LOW',4.07,4.35,.15,.018,3.6,.015)]:B('LED_PROFILE_'+n,x,y,z,w,d,h,char,'KI-114')
# Raised wall-mounted rail beneath ceiling, removable brackets; no ceiling penetration.
for ob in S.objects:
 if ob.name.startswith('R09_curtain_track'):ob.location.z=2.84
 if ob.name.startswith('R09_gathered_sheer'):
  for v in ob.data.vertices:v.co.z=.015+(v.co.z-.13)*(2.81-.015)/(2.57-.13)
# Reposition cabinet styling safely onto updated400mm top.
for ob in S.objects:
 if ob.name=='R09_vase':continue
for i in range(3):B('artbook_'+str(i),3.78,5.23,.55+i*.027,.23,.30,.023,pages,'KI-135')
# Reuse the prior bowl object at its supported coordinates.
ob=bpy.data.objects.get('R09_broad_ceramic_bowl')
if ob:ob.hide_render=False
# Numerical chair insertion test against evaluated Toni support/top meshes.
deps=bpy.context.evaluated_depsgraph_get()
def tree(o):
 e=o.evaluated_get(deps);m=e.to_mesh();verts=[o.matrix_world@v.co for v in m.vertices];polys=[tuple(p.vertices) for p in m.polygons];t=BVHTree.FromPolygons(verts,polys);e.to_mesh_clear();return t
supports=[o for o in S.objects if o.name.startswith('R06_Toni') and not o.hide_render];tests=[]
for idx in range(1,7):
 id='KI-029-'+str(idx);obs=[o for o in S.objects if o.get('instance_id')==id and not o.hide_render]
 # R09 replacement backs are authored in world coordinates.
 backs=[o for o in S.objects if o.name.startswith('R09_Eamy_continuous_'+id)]
 obs+=backs;v=Vector((1,0,0) if idx<3 else (-1,0,0) if idx<5 else (0,1,0) if idx==5 else (0,-1,0));origin={o.name:o.location.copy() for o in obs};accepted=0
 for step in range(1,31):
  delta=step*.005
  for o in obs:o.location=origin[o.name]+v*delta
  bpy.context.view_layer.update();deps=bpy.context.evaluated_depsgraph_get();hit=any(tree(a).overlap(tree(b)) for a in obs for b in supports)
  if hit:break
  accepted=delta
 for o in obs:o.location=origin[o.name]+v*max(0,accepted-.01)
 tests.append({'chair':id,'additional_insertion_mm':round(max(0,accepted-.01)*1000),'test':'5mm mesh-surface insertion steps against Toni top/supports with10mm setback','limit':'surface intersection only; initial overlap/containment, humans and tolerances not fully certified'})
S.camera=bpy.data.objects['Cam_02_Nappali_terasz'];S.render.resolution_x=1600;S.render.resolution_y=1000;S.cycles.samples=24
bpy.context.view_layer.update();a={'source_sha256':sh,'source_unchanged':hashlib.sha256(src.read_bytes()).hexdigest()==sh,'wall_source':[4.05,8.05],'composition':[4.35,7.95],'wall_end_clearances_mm':[300,100],'tower_reveal_screen_mm':[720,120,2760],'fronts_mm':[720,690,690,690,690],'recess_infill_mm':120,'upper_height_mm':2330,'top_mm':2880,'curtain_rail_z_mm':2840,'curtain_status':'wall mounted proposal; verify lintel/service cover/fixing, no ceiling anchors approved','chair_tests':tests,'status':'DIMENSIONED_PROPOSAL_NOT_MANUFACTURING_RELEASE'};(O/'audit/model_checks.json').write_text(json.dumps(a,ensure_ascii=False,indent=2));bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_R10.blend'),compress=True);S.render.filepath=str(O/'images/V01_R10_NATIVE.png');bpy.ops.render.render(write_still=True);print('R10_COMPLETE')
