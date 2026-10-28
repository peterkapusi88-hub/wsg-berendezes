from pathlib import Path
exec(Path(__file__).with_name('r09_living.py').read_text().split('# Correct materials')[0])
# Complete outside forms within the existing procurement envelopes: proposal, not selected SKU.
items=json.loads((P/'R06/data/design_R06.json').read_text())['items']
for it in items:
 id=it['id']
 if not any(id.startswith('KI-'+str(i)) for i in [136,138,139,140,141,142]):continue
 for ob in list(S.objects):
  if ob.name.startswith('KI_'+id):ob.hide_render=True
 x,y,z=it['x'],it['y'],it['z'];w,d,h=[it[k]/1000 for k in ['w','d','h']]
 if id=='KI-136':
  box('SPA_body',(x+w/2,y+d/2,z+h/2),(w-.02,d-.02,h-.04),coal,id,.025)
  box('SPA_closed_cover',(x+w/2,y+d/2,z+h-.025),(w,d,.05),grey,id,.02)
 elif id.startswith(('KI-140','KI-141')):
  box('OUT_table_top_'+id,(x+w/2,y+d/2,z+h-.015),(w,d,.03),coal,id,.007)
  for X in [x+.04,x+w-.04]:
   for Y in [y+.04,y+d-.04]:box('OUT_leg_'+id,(X,Y,z+(h-.03)/2),(.035,.035,h-.03),coal,id,.003)
 else:
  seat=.43 if id.startswith('KI-142') else .40
  for X in [x+.035,x+w-.035]:
   for Y in [y+.035,y+d-.035]:box('OUT_leg_'+id,(X,Y,z+seat/2),(.035,.035,seat),coal,id,.003)
  box('OUT_seat_'+id,(x+w/2,y+d/2,z+seat),(w-.04,d-.06,.10),grey,id,.025)
  box('OUT_back_'+id,(x+w/2,y+d-.05,z+(seat+h)/2),(w,.08,h-seat),grey,id,.025)
  for X in [x+.02,x+w-.02]:box('OUT_arm_'+id,(X,y+d/2,z+seat+.15),(.04,d,.045),coal,id,.005)
# Correct book/bowl support and restore physical lighting position ML04.
for ob in S.objects:
 if ob.name.startswith('R09_art_book'):ob.location.x-=.19
 if ob.name=='R09_broad_ceramic_bowl':
  for v in ob.data.vertices:v.co.x-=.11
 if ob.name.startswith('R06_Somar'):ob.location.x+=.299;ob.location.y+=.074
# Additional table styling, bounded to actual table surfaces.
for ob in list(S.objects):
 if ob.type=='MESH' and not ob.hide_render and ob.name.startswith('KI_KI-037'):
  b=bounds(ob);x=(b[0]+b[3])/2;y=(b[1]+b[4])/2;z=b[5]
  for i in range(2):box('coffee_artbook'+str(i),(x,y,z+.015+i*.03),(.22,.27,.025),pages,'ACCESSORY_ALLOWANCE')
# Store exact proposed replacement bounds for the audit.
bpy.context.view_layer.update();a=json.loads((O/'audit/model_changes.json').read_text());a['ML04_correction_m']=[.299,.074,0];a['ML04_source']={'x':8.549,'y':6.274,'source':'A902_villamos.csv'};a['outdoor_status']='DETAILED_DESIGN_PROPOSALS_SAME_ENVELOPES_NOT_PURCHASED_SKUS';a['additional_objects']=[{'name':o.name,'element':o.get('element_id'),'bounds':bounds(o)} for o in reg];(O/'audit/model_changes.json').write_text(json.dumps(a,ensure_ascii=False,indent=2))
bpy.ops.file.pack_all();bpy.ops.wm.save_as_mainfile(filepath=str(O/'blender/A902_Kyoto_Ink_R09.blend'),compress=True);S.render.filepath=str(O/'images/V01_R09_NATIVE_CONTROL.png');bpy.ops.render.render(write_still=True);print('R09_FINISHED')
