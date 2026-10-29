import bpy,json,math
from pathlib import Path
from mathutils import Vector,Matrix
W=Path('/Users/peterkapusi/Documents/ChatGPT/WSG – Stíluslabor');S=W/'execution/a902-s16-mediafal-20261029';O=W/'execution/a902-s01-kyoto-ink-20261026/CLAUDE_ATADAS/S16_MEDIAFAL_R14';r=S/'R14_kulso_feny_helyreallitasa';parts=json.loads((r/'data/parts.json').read_text());drawers=json.loads((r/'data/drawers.json').read_text());geos=[]
for rev in ['R13_folytonos_kulso_feluletek','R14_kulso_feny_helyreallitasa']:
 f=next((S/rev/'rajzok').glob('*.blend'));bpy.ops.wm.open_mainfile(filepath=str(f))
 for id,hx,angle in [('T-DOOR-L',21,-90),('T-DOOR-R',849,90)]:
  pv=Vector((hx/1000,.4,.573));rot=Matrix.Translation(pv)@Matrix.Rotation(math.radians(angle),4,'Z')@Matrix.Translation(-pv)
  for n in [id]+(['TEXTILE','T-DOOR-L-BACK','TEXTILE-RECESSED-HOUSING','TEXTILE-RECESSED-EMITTER']if id.endswith('L')else[]):bpy.data.objects[n].matrix_basis=rot@bpy.data.objects[n].matrix_basis
 for d in drawers:
  if d['id']=='D3':
   for id in d['moving']:bpy.data.objects[id].location.y-=.3
 bpy.context.view_layer.update()
 geos.append({p['id']:[tuple(c*1000 for c in bpy.data.objects[p['id']].matrix_basis@v.co)for v in bpy.data.objects[p['id']].data.vertices]for p in parts})
diffs=[]
for id in geos[0]:
 a,b=geos[0][id],geos[1][id];assert len(a)==len(b);diffs.append({'id':id,'max_vertex_coordinate_difference_mm':max(abs(x-y)for p,q in zip(a,b)for x,y in zip(p,q))})
maxdiff=max(d['max_vertex_coordinate_difference_mm']for d in diffs);assert maxdiff<.001,maxdiff
report={'scope':'A két eredeti mentett Blender főalkatrészeinek azonos névleges zárt állapotú, csúcsonkénti összevetése. Nem vasalat- vagy gyártási ellenőrzés. Eredeti forrásfájlok nem módosultak.','primary_parts':len(parts),'tolerance_mm':.001,'max_vertex_coordinate_difference_mm':maxdiff,'pass':True,'parts':diffs}
(O/'06_CAD_SEGITSEG/R13_R14_FRISS_GEOMETRIA_OSSZEVETES.json').write_text(json.dumps(report,ensure_ascii=False,indent=2));print('FRESH_COMPARE_OK',maxdiff)
