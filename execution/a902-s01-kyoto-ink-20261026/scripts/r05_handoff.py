from pathlib import Path
import json,hashlib,csv
P=Path(__file__).resolve().parents[1];O=P/'R05';H=O/'render_handoff';(H/'prompts').mkdir(exist_ok=True)
def read(f):return json.loads((P/f).read_text())
def sha(f):return hashlib.sha256(f.read_bytes()).hexdigest()
D=read('R05/data/design_R05.json');U={u['id']:u for u in D['units']};R=read('R05/data/register_proposal.json');RM={r[2]:r for r in R[1:]};old=read('CP3/render_handoff/manifest_CP3.json');idx=read('R05/data/drawing_index.json');photos=read('CP3/evidence/product_photo_manifest.json');C=read('R05/data/cost_R05.json');B=P/'R05/blender/A902_Kyoto_Ink_R05.blend';bhash=sha(B)
MF={
'MAT-01':'Light fronts: EGGER U702 PM Cashmere Grey candidate,19mm lacquered MDF only where sheet size permits. Edge and physical colour sample pending.',
'MAT-02':'Graphite fronts/tables: EGGER U961 PM Graphite Grey candidate,19mm matt MDF; real matching edges. Do not portray polished stone.',
'MAT-03':'Full-height wardrobe fronts: bespoke19mm painted MDF matched to a physical U702 sample. Nominal2837mm front requires a raw board longer than2800mm; no invented horizontal joint. Original ink artwork pending.',
'MAT-04':'W01: light greige mineral-effect TV panels and a DARK graphite tower, with the exact accepted rescue brushstroke composition. Sample-made thin texture, not deep relief. Original printable ink master is absent; do not substitute a fresh graphic.',
'MAT-05':'W02: Vescom Bely+Print1040.01 printable woven-look vinyl candidate;1340mm roll/1330mm printable. Two1050mm fields over2100×2880mm nominal area. No decorative picture frame. It is not linen or sculpted relief.',
'MAT-06':'Quiet adjacent wall: fine-textured greige paint matched physically to W02. Preserve corners and service access.',
'MAT-07':'Countertop: EGGER F274 ST9 Light Concrete decor candidate,38mm laminate worktop appearance. No thin marble upgrade. Exact local board SKU and cutouts pending.',
'MAT-08':'Headboard/pad: separate taupe and graphite upholstered fields,18mm carrier+about30mm foam within60mm overall. Actual fabric SKU and sample pending; do not erase the asymmetry.',
'MAT-09':'Bathroom:19mm moisture-resistant MDF with sealed edges/holes and matt graphite coating; removable trap drawer. Coating/basin/trap exact selections pending.',
'MAT-10':'Dry cabinet interior:18mm light melamine board,8mm back, matching sealed edges. Preserve the compartment schedule and all drawers/lifts.'}
titles=['Living room toward terrace','Living dining kitchen continuity','Dining toward kitchen','Master bedroom','Bathroom06.2','Terrace toward apartment','Entrance storage','Kitchen appliance towers','Kitchen parallel counters','Media wall detail','W02 full-height artwork','North master wardrobe','South master wardrobe','Room05.2 sleeping and study','Room05.2 wardrobe and desk','Room05.3 guest bed and wardrobe','Room05.3 workspace and terrace door','Bathroom06.1 bath and laundry','Bathroom06.2 shower and storage','Hallway','WC storage and mirror','West terrace and jacuzzi','East terrace lounge','Outdoor levels and green roof','Balcony and storage','Master panorama view','AT8-01 reserve pantry and freezer','T-0-26 bicycle luggage and seasonal storage']
globalgaps=[
 {'id':'G01','item':'Ready-made product meshes','owner':'render/model operator','next':'Build/import exact selected product geometry using manufacturer dimensions and verified variant photos. Simplified proxies are not final identity proof.','blocks':'final product render'},
 {'id':'G02','item':'Original ink masters','owner':'graphic artist / printer','next':'Reconstruct/obtain accepted artwork and approve a1:1physical sample. The three SVGs are panel layouts only.','blocks':'final artwork and manufacturing'},
 {'id':'G03','item':'Survey / services','owner':'surveyor + joiner + electrician','next':'Measure finished walls, doors, thresholds, both stores and service points. Confirm TV move on wall.','blocks':'manufacturing'},
 {'id':'G04','item':'Functional clearances','owner':'designer + joiner','next':'Resolve kitchen840mm aisle/open dishwasher,05.3chair-bed overlap, master bedside versus bed drawers, cupboard lift motion and bike removal.','blocks':'functional signoff'},
 {'id':'G05','item':'Material and lighting samples','owner':'joiner / printer / electrician + owner','next':'Approve physical finish family,6tall wardrobe fronts, TV heavy front, three12Vlight branches and Hue test.','blocks':'appearance and installation signoff'},
 {'id':'G06','item':'Supplier quotations','owner':'owner / procurement','next':'Use identical R05scope for RFQs after permission to send.18M target remains; current estimate is not an agreed contract price.','blocks':'ordering and budget closure'}]
views=[];links=[]
def attachment(path,role,order):
 f=P/path;return {'order':order,'path':path,'role':role,'exists':f.exists(),'sha256':sha(f) if f.exists() else None}
for i,v in enumerate(old['views']):
 vid=v['view_id'];units=[U[x] for x in v['custom_structures'] if x in U];products=[]
 if vid in ['V27','V28']:
  codes=['KI-CP3-S01','KI-CP3-F01','KI-CP3-F02','KI-CP3-S03','KI-CP3-S04'] if vid=='V27' else ['KI-CP3-S02','KI-R05-B01','KI-CP3-S03','KI-CP3-S04']
  v['products']=[{'element':code} for code in codes]
 for pr in v['products']:
  id=pr['element'];r=RM.get(id)
  if not r:continue
  custom=[u['id'] for u in units if id in u['cost']]
  products.append({'element':id,'name':r[7],'sku':r[9] or None,'url':r[10] or None,'size':r[11],'finish':r[12],'cost_main_huf':r[14]*r[16]+sum((r[k] or 0) for k in [17,18,19]),'quantity':r[14],'price_status':r[21],'price_checked':r[23],'custom_structures':custom,'asset_status':'custom drawing/model conditional' if custom else 'exact mesh NOT verified'})
 at=[]
 control='R05/blender/V01_R05_native_technical.png' if vid=='V01' else v['primary_control']
 at.append(attachment(control,'R05 native technical trial; simplified products' if vid=='V01' else 'OLDER CP3 pose/context reference only; generate new R05 native control before editing',1))
 target='CP3/reviews/20261027_csomag_es_mediafal/A902_KyotoInk_V01_KI-CP3-R03_VISUAL_RESCUE_v3_CONDITIONAL.png' if vid in ['V01','V10'] else None
 if not target:
  target=next((a['path'] for a in v['attachments'] if 'Aesthetic' in a.get('role','')),None)
 if target:at.append(attachment(target,'Accepted aesthetic reference; not dimension evidence',len(at)+1))
 for u in units:
  f=next(a['path'] for a in idx if a['unit']==u['id'] and a.get('page')=='01');at.append(attachment(f,'Current selected custom drawing; R05 material addendum governs finish',len(at)+1))
 for ph in photos:
  if any(p['element']==ph['element'] for p in products) and 'ARCHIVED' not in ph['status']:at.append(attachment(ph['file'],'Exact product-page photo; verify selected variant, never an exact3Dmesh substitute',len(at)+1))
 mids=sorted(set(m for u in units for m in u['material_ids']));opens=['All current geometry and product-identity checks are conditional. Do not label this a construction-approved final image.']
 if vid in ['V01','V02','V03','V08','V09','V10','V11']:
  opens+=['W01 tower must be at worldY4.70–5.40m, away from the terrace end. PanelsY5.40–8.00m; TVshifted+700mm with panel. Local render is not photometric proof.','Kitchen aisle840mm and open dishwasher passage remain unresolved. Exact Lennon/Eamy/Somar meshes and ink master pending.']
 if vid in ['V04','V12','V13','V26']:opens+=['WN03-module/6front proposal has8drawers/2lifts;3.350m rods,436.914L drawer boxes,2.036m²shelves. Shelf reduction1.356m²vs prior proposal needs owner review. Master bed-side-drawer/nightstand collision remains unresolved.']
 if vid in ['V14','V15','V16','V17']:opens+=['05.2 remains wardrobe/child room;05.3guest/work. Do not shrink the bed or delete wardrobe capacity silently.05.3chair/bed clash still open.']
 if vid in ['V05','V19']:opens+=['B62-01 uses600+300side-by-side fronts; exact basin/trap cutout and mirror-wall assembly remain open.']
 if vid in ['V06','V22','V23','V24','V25']:opens+=['Retain jacuzzi and existing outdoor levels/drainage/green roof. Actual thresholds, load, lifting and hookup are unapproved. Outdoor exact product models are incomplete.']
 if vid=='V27':opens+=['AT8area4.57m²is known;2580×1870planning rectangle is not surveyed. TwoJONAXEL racks, freezer and12exampleboxcapacity. Exact freezer variant/ventilation and door remain open.']
 if vid=='V28':opens+=['T026area4m²is known;2500×1600planning rectangle not surveyed. TwoBROR racks,3examplecases,9exampleboxes,1verticalbike. Bike envelope700×1150×2000mm is unmeasured; rack contact/no spare margin and door/extraction open. SteadyrackClassicRoad candidate does not accept all bikes.']
 out={'view_id':vid,'title':titles[i],'room':v['room'],'camera_id':v['camera_id'],'camera':v['camera'],'revision':'KI-R05','blender_file':'R05/blender/A902_Kyoto_Ink_R05.blend','blender_sha256':bhash,'primary_control':control,'control_revision':'KI-R05' if vid=='V01' else 'KI-CP3-R03 ARCHIVED; R05 control required','attachments':at,'products':products,'custom_structures':[{'id':u['id'],'size_mm':[u['w'],u['d'],u['h']],'cost':u['cost'],'materials':u['material_ids'],'position_m':[u['x'],u['y'],u['z']]} for u in units],'materials':{m:MF[m] for m in mids},'light_scene':v['light_scene'],'open_conditions':opens,'geometry_status':'CONDITIONAL; see R05/blender/checks.json. No whole-apartment PASS.','output_file':f'A902_KyotoInk_{vid}_KI-R05_CONDITIONAL.png','release':'CONDITIONAL_TECHNICAL_ONLY'}
 if vid=='V28':out['storage_placement_mm']='R1(50,1000)850×550;R2(900,1000)850×550;bike(1750,50)700×1150×2000. No separate T-LUG floor block; cases inside lower rack bays. No surveyed door.'
 if vid=='V27':out['storage_placement_mm']='R1(50,50)800×380;R2(1720,50)800×380;freezer(1000,50)597×675×1455. Room2580×1870planning only; known pillar retained.'
 if vid in ['V01','V02','V10']:out['lighting_detail']='KI-114 Loox5LED2074/833.74.308;12V2700K9.6W/m;TOP2.6m,VERT2.33m,LOW3.3m;PS-A47.328W/60W,PS-B31.68W/60W;GL-C-009P candidate,Hue test pending. No invented glow strips.'
 camera=v['camera'];parts=[f'KYOTO INK A902 — {vid}: {titles[i]}', 'Design/model revision KI-R05. CONDITIONAL TECHNICAL RENDER; not a final construction image.',f'Use model R05/blender/A902_Kyoto_Ink_R05.blend SHA256 {bhash}.',f"Camera {v['camera_id']}; position {camera.get('location')}; rotation Euler radians {camera.get('rotation_euler')}; lens {camera.get('lens_mm')}mm; type {camera.get('camera_type')}; ortho scale {camera.get('ortho_scale')}. Do not rename another perspective to this camera.", 'ATTACH FILES IN THIS EXACT ORDER:']
 parts += [f"{a['order']}. {a['path']} — {a['role']}; SHA256 {a['sha256']}" for a in at]
 parts+=['CUSTOM STRUCTURES — preserve dimensions, division, material and placement:']
 parts += [f"{u['id']}: {u['w']}×{u['d']}×{u['h']}mm; worldposition {[u['x'],u['y'],u['z']]}; modules {u['modules']}; front modules {u.get('front_modules',u['modules'])}; cost lines {','.join(u['cost'])}; finishes {','.join(u['material_ids'])}." for u in units]
 parts+=['PRODUCT IDENTITY — no substitution with a prettier unpriced product:']
 parts += [f"{p['element']}: SKU {p['sku'] or 'UNRESOLVED'}, size {p['size']}; exact product source {p['url'] or 'custom structure / unresolved supplier'}. Quantity {p['quantity']}; current row amount {p['cost_main_huf']}HUF; {p['price_status']}. Custom structure IDs {p['custom_structures']}. Mesh status: {p['asset_status']}." for p in products]
 parts+=['FINISH SPECIFICATIONS:']+[f'{m}: {MF[m]}' for m in mids]
 if 'storage_placement_mm' in out:parts+=['STORAGE PLAN: '+out['storage_placement_mm']]
 parts += [f"LIGHT SCENE: {v['light_scene']}. {out.get('lighting_detail','Use the actual light schedule. No added strips, fittings, hidden light sources or changed colour temperature without updating the bill and drawings.')}" ,'OPEN CONDITIONS:']+opens
 parts += ['WORKFLOW: First render a native Blender technical trial at this exact camera. Check furniture silhouette, SKU variants, dimensions, door seams, graphics, thresholds, services and routes. A legacy CP3 camera image is only pose evidence. If the R05 control is absent, generate it before image editing. Simplified proxies must be replaced and checked before a product-faithful image can be released.','Image editing may refine photographic finish only after a faithful native base exists. It may not relocate furniture, erase a threshold, change the wardrobe internals, enlarge the room, invent a product or hide a collision. Preserve real building photography for floor/windows/terrace/panorama; align the camera rather than relabelling a photograph.','If a required reference, exact asset, artwork master or check is missing, report it and stop the final-image release. A clearly labelled conditional technical study may be saved. Do not silently create plausible substitutes.',f"Save as {out['output_file']} and a same-name audit text listing input hashes, camera/model revision, product/material matches, discrepancies and unresolved gates. Only continue to the next view after reviewing the first trial. No bulk image generation is authorized by this handoff alone."]
 fn=H/'prompts'/f'{vid}_KI_R05_EN.txt';fn.write_text('\n\n'.join(parts));out['prompt_path']=str(fn.relative_to(P));out['prompt_sha256']=sha(fn);views.append(out)
 for u in units:
  for cost in u['cost']:links.append({'element':cost,'unit':u['id'],'view':vid,'materials':';'.join(u['material_ids']),'drawing':next(a['path'] for a in idx if a['unit']==u['id'] and a.get('page')=='01'),'object_binding':'R05/blender/object_register.json','revision':'KI-R05'})
functional=[]
for f in old['functional_views']:
 uid=f['unit'];u=U.get(uid);state=f['id'].split('_')[-1];fn=H/'prompts'/(f['id']+'_KI_R05_EN.txt')
 if not u:continue
 text=f"""A902 KYOTO INK / {f['id']} / KI-R05 / {uid}
Use R05/blender/A902_Kyoto_Ink_R05.blend (SHA256 {bhash}).
Camera {f['camera_id']}, location {f['location']}, rotation {f['rotation_euler']}, orthographic scale {f['ortho_scale']}.
Requested state: {state}. First create a native R05 control. The old CP3 state image is archival, not current evidence.
Structure size {u['w']}×{u['d']}×{u['h']}mm. Front modules {u.get('front_modules',u['modules'])}; internal modules {u['modules']}. Material IDs {u['material_ids']}. Cost lines {u['cost']}.
Attach in order: current R05 native control once generated; current 01 and02 drawings from R05/data/drawing_index.json; R05/data/design_R05.json compartment entry; R05/data/materials.json; accepted room image from data/render_manifest.json. For W01 use the selected VISUAL_RESCUE override.
Do not invent contents or hidden capacity. Keep actual shelf, rod and drawer coordinates in the compartment JSON. Illustrative clothing/bins must fit their declared planning dimensions and must not be counted twice.
Closed means actual doors present. Cutaway means removed fronts, clearly labelled; it is not an opening test. Open means real hinge/runner/lift motion based on supplier geometry. If motion data is missing, stop the open-state release and report the missing specification. Never replace a lift sweep with a simple rotating rectangle and call it validated.
Manufacturer hinge/fixing loads, exact drawer clearances, garment clearance, bath trap exclusion and surveyed wall dimensions remain open. No manufacturing approval.
Save A902_KyotoInk_{f['id']}_KI-R05_CONDITIONAL.png plus audit with model/camera/input hashes. No batch generation without review of the first trial.
"""
 fn.write_text(text);functional.append({'id':f['id'],'unit':uid,'state':state,'camera_id':f['camera_id'],'prompt_path':str(fn.relative_to(P)),'prompt_sha256':sha(fn),'release':'CONDITIONAL; supplier motion unavailable for opening proof'})
manifest={'revision':'KI-R05','base_commit':'0c0d3c7727936949b282f3374519ea3b9f182641','blender_sha256':bhash,'workbook_sha256':sha(P/'outputs/A902_Kyoto_Ink_elo_regiszter.xlsx'),'cost':C,'views':views,'functional_views':functional,'release':'CONDITIONAL_TECHNICAL_ONLY','global_gaps':globalgaps}
(H/'manifest_R05.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
with (O/'data/element_drawing_model_view.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=links[0].keys());w.writeheader();w.writerows(links)
(O/'data/open_gates.json').write_text(json.dumps(globalgaps,ensure_ascii=False,indent=2))
start=f"""A902 KYOTO INK — R05 RENDER OPERATOR START

Continue the existing execution project. Do not redesign the style. Source branch: execution/a902-s01-kyoto-ink-design-to-budget-20261026. Use the R05 files, not older CP3/R04 proposals where superseded.

Read R05/render_handoff/manifest_R05.json, R05/data/design_R05.json, R05/data/materials.json, R05/data/drawing_index.json and R05/blender/checks.json. Open R05/blender/A902_Kyoto_Ink_R05.blend, SHA256 {bhash}. The live workbook is outputs/A902_Kyoto_Ink_elo_regiszter.xlsx. Current main estimate23912890HUF; comparative economy23659890HUF;18Mtarget, separate2Mreserve untouched. These are not quotations or spending authorization.

The selected media-wall appearance is CP3/reviews/20261027_csomag_es_mediafal/A902_KyotoInk_V01_KI-CP3-R03_VISUAL_RESCUE_v3_CONDITIONAL.png. The tower was on the wrong end in the previous model: R05 moves it to Y4.70–5.40m, panel toY5.40–8.00m, TV+700mm. Do not restore the old window-side tower. Keep the external ink composition, narrow seams, warm light lines and floating base. The true ink master is still missing; the red SVG layout guides are NOT printable artwork.

First run V01 only using its complete standalone English prompt. The native technical trial supplied is a geometry study, not a final product render. Replace simplified purchased-product proxies with verified selected assets, make the ink/material sample approval explicit and resolve the per-view gates. A SKU tag alone does not establish identical product geometry. The operator must report what is still absent before requesting a final image.

Each view has its own prompt, camera, ordered attachment list and output filename. Attach the actual images/drawings, not just their filenames in text. Use original room photographs for existing finishes/thresholds/panorama with actual camera matching. Do not substitute another view and retain an old camera ID.

Render the faithful Blender base, check it against the drawing, register and references, then optionally use image editing only to refine photographic appearance. Do not move objects, improve proportions beyond the real products, erase collisions or add unpriced elements. Before/after overlays and product silhouette checks are required. If geometry, product identity or graphics fail, stop and correct; do not continue a batch of attractive but misleading images.

After each approved trial save PNG and audit TXT, including file hashes, exact model/camera, product/SKU/material list, actual checks, discrepancies and open conditions. All current views remain conditional technical studies until their gates close. This handoff does not authorize ordering, supplier messages or bulk generative rendering. There are28room/terrace/store views plus21functional-state prompts.
"""
(H/'START_RENDER_OPERATOR_EN.txt').write_text(start)
missing=[a for v in views for a in v['attachments'] if not a['exists']]
(O/'qa/render_handoff_checks.json').write_text(json.dumps({'views':len(views),'functional':len(functional),'missing_listed_attachments':missing,'current_native_room_controls':1,'older_camera_controls':27,'final_release':False,'reason':'Product shapes/artwork/samples/functional constraints unresolved'},ensure_ascii=False,indent=2))
print('Handoff',len(views),len(functional),'missing files',len(missing),'all conditional')
