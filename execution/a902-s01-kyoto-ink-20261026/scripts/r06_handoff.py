import json,hashlib,copy
from pathlib import Path
P=Path(__file__).resolve().parents[1];O=P/'R06';H=O/'render_handoff';(H/'prompts').mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
d=json.loads((P/'R05/render_handoff/manifest_R05.json').read_text());r=json.loads((O/'data/register_R06.json').read_text());rm={x[2]:x for x in r[1:]};targets=json.loads((O/'data/target_manifest.json').read_text());checks=json.loads((O/'blender/checks.json').read_text());blend='R06/blender/A902_Kyoto_Ink_R06.blend'
maptarget={'V01':'T01_W01_nappali.png','V02':'T02_W02_etkezo.png','V03':'T03_Konyha.png','V04':'T04_Master_eszak.png','V05':'T06_Furdo_mosdo.png','V08':'T03_Konyha.png','V09':'T03_Konyha.png','V10':'T01_W01_nappali.png','V11':'T02_W02_etkezo.png','V12':'T04_Master_eszak.png','V13':'T05_Master_del.png','V19':'T07_Furdo_WC.png','V26':'T05_Master_del.png'}
assetids={'KI-036','KI-028','KI-029','KI-043','KI-044','KI-109','KI-117'}
d['revision']='KI-R06';d['base_commit']='e1d557ded0e49069e46a922b3f4dcfee6b68b55a';d['blender_sha256']=sha(P/blend);d['workbook_sha256']=sha(P/'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx');d['cost']=json.loads((O/'data/budget_R06.json').read_text());d['release']='CONDITIONAL DESIGN ONLY — NOT BUDGET-CLOSED OR MANUFACTURING APPROVED';d['geometry_checks']=checks
d['global_gaps']=[{'item':'Original artwork versus redraw','status':'Five editable dimensioned R06 proposals exist; original masters unavailable, physical proof approval pending.'},{'item':'Product geometry','status':'Lennon/Toni/Eamy/Somar/Rondo are dimension-and-photo reconstructions, not manufacturer meshes; other products retain inherited proxies.'},{'item':'Site and samples','status':'No site measurements or physical sample approval fabricated.'},{'item':'T07 bathroom','status':'Exact hooks/branch-wall/bench arrangement conflicts with shower-zone geometry; waterproof alternative remains conditional.'},{'item':'Budget','status':'18M not achieved; reserve untouched; no supplier quotes.'}]
for v in d['views']:
 vid=v['view_id'];v['revision']='KI-R06';v['blender_file']=blend;v['blender_sha256']=d['blender_sha256'];v['release']='CONDITIONAL';v['primary_control']=None;v['control_revision']='R06 CAMERA CONTROL MUST BE RENDERED BEFORE EDITING';v['geometry_result']='Selective actual tests only; see R06/blender/checks.json; no apartment-wide PASS'
 at=[]
 def add(path,role):at.append({'order':len(at)+1,'path':path,'role':role,'exists':(P/path).exists(),'sha256':sha(P/path) if(P/path).exists()else None})
 if vid in maptarget:add('R06/targets/'+maptarget[vid],'User-selected appearance target; camera/geometric authority NOT granted')
 add('R06/drawings/R06_valtozott_szerkezetek.pdf','R06 changes override affected R05 exterior/front/bed/shower decisions')
 for a in v.get('attachments',[]):
  if 'drawing' in a.get('role','').lower() and (P/a['path']).exists():add(a['path'],'Unchanged underlying interior/assembly drawing; R06 amendments take precedence')
 for pr in v.get('products',[]):
  row=rm.get(pr['element'])
  if row:pr.update(name=row[7],sku=row[9],size=row[11],url=row[10],cost_main_huf=row[14]*row[16]+sum(row[k] or 0 for k in [17,18,19]),asset_status='R06 photo/dimension reconstruction, NOT exact certified mesh' if row[2] in assetids else 'Inherited conditional asset; inspect actual model before final claim')
 v['attachments']=at;v['output_filename']=f'A902_{vid}_KI-R06_CONDITIONAL.png'
 specs='\n'.join(f"{p['element']}: {p['name']}; SKU {p.get('sku')}; dimensions {p.get('size')}; {p.get('asset_status')}" for p in v.get('products',[]))
 prompt=f"""KYOTO INK — {vid} / {v['title']} — KI-R06 CONDITIONAL DESIGN
Room: {v.get('room')}. Exact camera ID: {v.get('camera_id')}. Do not rename another perspective to this camera.
Open {blend}; expected SHA256 {d['blender_sha256']}. Use the camera transform from the manifest, verify it against actual photographs when photo matching is claimed. Render a new native R06 control first; an old CP3/R05 image is context only.
The seven new target images govern appearance, never wall dimensions. Keep architecture, window divisions, thresholds, terrace levels, greenery and service access from the locked geometry. Never enlarge a room to fit a target image.
VISIBLE PRODUCT SCHEDULE:
{specs}
CUSTOM STRUCTURES: {json.dumps(v.get('custom_structures',[]),ensure_ascii=False)}. Follow the existing interiors plus R06 seven-sheet revision. Preserve all drawer, rail and lift capacity. Full-height master fronts: north6, south4; no invented horizontal seam. Dark media tower remains on the dining end,700mm, followed by4×650mm panels. Lower cabinet3300mm. Keep the three actual proposed light-profile locations; no painted glow.
MATERIALS: graphite matt fronts; warm chalk wardrobe fronts; F243 ST76 laminated38mm stone-effect kitchen top, not thin natural stone. Exact selected taupe Lennon fabric and Eamy ash/grey chenille/black steel photo references govern; do not beautify to a different product. Somar is760×360mm. Rondo85264 is200mm with a white base. No alternate premium product may appear unless its full project cost is updated.
ART: use R06/artwork/INK-W01,INK-W02,INK-WN,INK-WS masks and corresponding SVG masters on the specified panels. They are new reference-based redraw proofs, not recovered originals or approved print files. Keep panel gaps, switches and service openings. Branch art INK-B62 is a conditional waterproof alternative; never place towels/bench inside the shower to mimic T07.
FUNCTION: kitchen840mm closed aisle, no passage with dishwasher open.05.3bed retains180cm width and moves100mm south; desk chair moves150mm north,600mm withdrawal gives150mm nominal separation, not a route. Master BED-01 lift-bed is a proposal pending hardware and swept-volume approval. Shower glass is1000mm along the north tray's south edge, with780mm nominal entry; no false site validation.
ATTACHMENTS IN ORDER:
"""+'\n'.join(f"{a['order']}. {a['path']} — {a['role']}" for a in at)+f"\nOUTPUT: {v['output_filename']}. Label CONDITIONAL DESIGN. Check silhouette, SKU, dimensions, finish, graphic placement and repeated furniture across views. Stop on geometry/product mismatch; do not silently fix with generative editing. No bulk generation is authorized."
 (H/'prompts'/f'{vid}_R06.txt').write_text(prompt)
for v in d.get('functional_views',[]):
 vid=v.get('view_id',v.get('id','functional'));v['revision']='KI-R06';v['blender_file']=blend;v['status']='R06 closed/open state must be run; older picture is not a fresh PASS';(H/'prompts'/f'{vid}_R06_functional.txt').write_text('KI-R06 FUNCTIONAL CONTROL\n'+json.dumps(v,ensure_ascii=False,indent=2)+'\nUse actual R06 geometry. Show dimensions and motion envelopes. No generative image editing; report FAIL/OPEN honestly. Use R06/blender/checks.json for the already executed selective tests.')
(H/'manifest_R06.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
(H/'START_RENDER_OPERATOR_EN.txt').write_text('''Open the Kyoto Ink KI-R06 package in this same project. Read manifest_R06.json and the requested view-specific prompt in full. This is a CONDITIONAL design package, not a final construction-approved release. Load the actual R06 .blend and verify its SHA256. Do not execute the old R05 prompts.
First make ONE native camera test. Inspect geometry, actual product silhouette, artwork/panel continuity, materials and service access against the seven target images, R06 drawings and live Excel. The current studio proof is not a camera-matched apartment render. Do not replace unresolved product meshes with attractive invented products.
If using ChatGPT image editing, attach the NEW native camera control first, then the view target, actual selected-product photographs and relevant drawings in the manifest order. An image editor may refine surface/lighting only; it must not change shape, wall location, camera, door/window geometry or product identity. Text-only tools may audit the prompt but cannot certify the image or geometry.
On mismatch stop that view and record the failure. Save each accepted conditional image with its exact filename and a product/geometry audit. Never batch-generate all views automatically. No purchasing, RFQ sending or bookings. Physical measurements, material/print samples, lift-bed hardware and the bathroom alternative remain explicit gates.18M is not currently achieved; use the actual24.483M full estimate and do not conceal the separate2M reserve.
''')
print(len(d['views']),len(d.get('functional_views',[])),'render handoff records')
