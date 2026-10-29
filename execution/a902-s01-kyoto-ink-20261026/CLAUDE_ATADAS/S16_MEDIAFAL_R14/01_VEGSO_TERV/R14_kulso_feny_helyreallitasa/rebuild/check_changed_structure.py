from pathlib import Path
import bpy,bmesh,json,itertools
O=Path(__file__).resolve().parents[1]
# Reuse the same source geometry constructor, without running its mutation/export loop.
code=(O/'rebuild/prepare_geometry.py').read_text();exec(code.split('reports=[]')[0])
objects={p['id']:solid(p)for p in parts};pairs=[];collisions=[]
for a,b in itertools.combinations(parts,2):
 if a['id']not in changed and b['id']not in changed:continue
 aa,bb=a['box'],b['box'];overlap=[min(aa[k]+aa[k+3],bb[k]+bb[k+3])-max(aa[k],bb[k])for k in range(3)]
 if min(overlap)<.001:continue
 ob=objects[a['id']].copy();ob.data=objects[a['id']].data.copy();bpy.context.collection.objects.link(ob);m=ob.modifiers.new('volume_intersection','BOOLEAN');m.operation='INTERSECT';m.solver='EXACT';m.object=objects[b['id']];bpy.context.view_layer.objects.active=ob;bpy.ops.object.modifier_apply(modifier=m.name)
 bm=bmesh.new();bm.from_mesh(ob.data);vol=abs(bm.calc_volume())*1e9;bm.free();bpy.data.objects.remove(ob,do_unlink=True)
 entry={'a':a['id'],'b':b['id'],'intersection_mm3':vol};pairs.append(entry)
 if vol>1:collisions.append(entry)
report={'revision':'R14','affected_main_parts':changed,'broadphase_pairs_checked':len(pairs),'intersections_over_1mm3':collisions,'pairs':pairs,'scope':'Exact Boolean volume intersections of changed primary parts in closed pose. Excludes hidden lighting extras, hardware, actual hinge motion and shop tolerances.'}
(O/'audit/changed_structure_intersections.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('R14_INTERSECTION_RESULT',len(pairs),collisions,flush=True);assert not collisions,collisions
