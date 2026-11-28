from pathlib import Path
import json
from collections import Counter
root=Path(__file__).resolve().parents[2]
p=root/'02_referenciak/GDESIGN3D_20261127/catalog/build_families.py';ns={'__file__':str(p)}
exec(p.read_text().split('covered={i')[0],ns)
rows=ns['rows'];bases=[x for x in rows if x['category']=='base'];modules=[x for x in rows if x['category']=='module'];cat=ns['albums']
out=Path(__file__).parent
role={
 'master':{'A811':['MASTER_HERO','MASTER_MEDIA'],'A812':['MASTER_HERO','MASTER_MEDIA'],'A902':['Cam_04','Cam_11c']},
 'wardrobe':{'A811':['MASTER_GARD_HERO'],'A812':['GARD3_HERO'],'A902':['Cam_04','Cam_11c']},
 'bath':{'A811':['BATH1_HERO','BATH2_HERO','BATH2_SHOWER','WC_HERO'],'A812':['BATH2_HERO','BATH2_SHOWER','BATH08_HERO'],'A902':['Cam_10']},
 'kitchen_dining':{'A811':['KITCHEN_HERO'],'A812':['KITCHEN_HERO'],'A902':['Cam_12','Cam_03']},
 'entry_hall':{'A811':['ENTRY_HERO','HALL_HERO'],'A812':['ENTRY_HERO','HALL_HERO'],'A902':[]},
 'study':{'A811':['BED1_HERO','BED1_MEDIA'],'A812':['BED2_HERO','BED2_MEDIA'],'A902':[]},
 'child':{'A811':[],'A812':['BED1_HERO','BED1_MEDIA'],'A902':[]},
 'guest_child':{'A811':['BED1_HERO','BED1_MEDIA'],'A812':['BED1_HERO','BED1_MEDIA'],'A902':[]},
 'utility':{'A811':['UTILITY_HERO'],'A812':['UTILITY_HERO'],'A902':[]},
 'no_direct_camera':{'A811':[],'A812':[],'A902':[]}}
# Camera applicability, not a room/function change instruction.
rules={
'M23_ROCK_MASTER':['master','bath'],'M23_GREEN_BATH':['bath'],'M23_WALNUT_MASTER':['master'],
'M25_BURGUNDY_BATH':['bath'],'M25_BLUE_MASTER':['master'],'M25_BROWN_BATH':['bath'],
'M25_INDUSTRIAL_KITCHEN':['kitchen_dining','entry_hall'],'M25_STUDY':['study'],
'M25_ENTRY_ROCK':['entry_hall'],'M25_ENTRY_BRONZE':['entry_hall'],'M25_CHILD_SAND':['child'],
'M25_BRONZE_BATH':['bath'],'M25_GRAPHITE_BATH':['bath'],'M25_SAND_MASTER':['master'],
'M25_BRONZE_WARDROBE':['wardrobe'],'M25_LIGHT_STONE_KITCHEN':['kitchen_dining'],'M25_LIGHT_SPA':['bath'],
'M25_CHILD_GRAPHITE':['child'],'M25_CHILD_POWDER':['child'],'M25_INDUSTRIAL_MASTER':['master','wardrobe','entry_hall'],
'GD24_F08':['master','wardrobe'],'GD24_F10':['entry_hall'],'GD24_F11':['bath'],
'GD24_F13':['no_direct_camera'],'GD24_F14':['entry_hall'],'GD24_F15':['master'],'GD24_F17':['child'],
'GD24_F18':['master','wardrobe'],'GD24_F19':['bath'],'GD24_F21':['entry_hall'],
'GD24_F22':['study'],'GD24_F23':['kitchen_dining'],'GD24_F25':['bath'],'GD24_F26':['study'],'GD24_F27':['study'],
'G26-05':['kitchen_dining','entry_hall'],'G26-12':['kitchen_dining'],'G26-13':['entry_hall'],'G26-14':['study'],
'M26_GD007':['bath'],'M26_GD003':['bath'],'M26_GD023':['bath'],'M26_GD004':['master','wardrobe','bath'],
'M26_GD010':['bath'],'M26_GD011':['kitchen_dining'],'M26_GD016':['kitchen_dining'],
'M26_GD012':['bath','utility'],'M26_GD013':['master','wardrobe'],'M26_GD018':['kitchen_dining'],
'M26_GD020':['guest_child'],'M26_GD021':['no_direct_camera'],'M26_GD022':['master','wardrobe'],
'M26_GD2026_02':['study'],'M26_GD2026_03':['bath'],'M26_GD026':['kitchen_dining'],
'M26_GD028':['bath'],'M26_GD2026_04':['entry_hall']}
assert set(rules)=={x['id'] for x in modules}
# Optional function variants are separate; never included in the main count.
optional={
 'M25_BLUE_MASTER':('Vendég/dolgozó változat külön két száraz szobában',{'A811':['BED1_HERO','BED1_MEDIA'],'A812':['BED2_HERO','BED2_MEDIA'],'A902':[]}),
 'M25_CHILD_SAND':('A811 vendégszoba alternatív gyerekszoba-funkciója',{'A811':['BED1_HERO','BED1_MEDIA'],'A812':[],'A902':[]}),
 'M25_CHILD_GRAPHITE':('A811 vendégszoba alternatív gyerekszoba-funkciója',{'A811':['BED1_HERO','BED1_MEDIA'],'A812':[],'A902':[]}),
 'M25_CHILD_POWDER':('A811 vendégszoba alternatív gyerekszoba-funkciója',{'A811':['BED1_HERO','BED1_MEDIA'],'A812':[],'A902':[]}),
 'GD24_F17':('A811 vendégszoba alternatív babaszoba-funkciója',{'A811':['BED1_HERO','BED1_MEDIA'],'A812':[],'A902':[]}),
 'GD24_F13':('Lépcső nélkül csak falburkolat/fényrészlet az előtérben; kreatív átdolgozás, nem ugyanaz a helyiségterv',role['entry_hall']),
 'M26_GD021':('Külön pihenőszoba-változat a vendég/dolgozó száraz szoba helyén; master és vizes helyiségek maradnak',role['study']),
 'M26_GD020':('A812 dolgozó alternatív vendégszoba-funkciója',{'A811':[],'A812':['BED2_HERO','BED2_MEDIA'],'A902':[]})}
views=json.loads((root/'05_promptok/GDESIGN3D_20261127/CAMERA_RESUME_MANIFEST.json').read_text())
cams={a:{v['camera'] for v in views['views'] if v['apartment']==a} for a in ['A811','A812','A902']}
baseids={i for b in bases for i in b['ids']}
modids={i for m in modules for i in m['ids']}
records=[];gross=Counter();optcount=Counter()
for m in modules:
 r=rules[m['id']];cv={a:sorted({c for k in r for c in role[k][a]}) for a in cams}
 for a,c in cv.items():assert set(c)<=cams[a];gross[a]+=len(c)
 hosts=[b['id'] for b in bases if set(m['ids'])&set(b['companions'])]
 op=optional.get(m['id']);oc=op[1] if op else {a:[] for a in cams}
 for a,c in oc.items():assert set(c)<=cams[a];optcount[a]+=len(c)
 rec={'id':m['id'],'title_hu':m['title'],'source_album_ids':m['ids'],'source_image_indices':m.get('image_indices'),'roles':r,'compatible_existing_cameras':cv,'image_counts':{a:len(c) for a,c in cv.items()},'total':sum(map(len,cv.values())),'already_in_base_primary_source':bool(set(m['ids'])&baseids),'proposed_base_hosts_not_yet_selected':hosts,'optional_function_variant':{'reason_hu':op[0],'cameras':oc,'count':sum(map(len,oc.values()))} if op else None}
 if m['id']=='GD24_F21':rec['limitation_hu']='Csak a folyosó fal-/tárolórészlete kerül át, lépcső és emeleti nyílás nem.'
 if m['id']=='M25_INDUSTRIAL_MASTER':rec['limitation_hu']='A forrás gardrób-folyosója itt előtér/folyosó anyagváltozatként számít; ha csak master suite készül, 4 képpel csökkenthető.'
 if 'bath' in r:rec['wet_room_rule']='Anyag- és mosdóbútor-nyelv a meglévő vizes helyiségben; kád, bidé, WC vagy második medence csak meglévő helyen. A811 külön WC is csak WC marad.'
 records.append(rec)
base_counts={a:len(bases)*len(c) for a,c in cams.items()}
result={'date':'2026-11-28','status':'COUNTING_PROPOSAL_NOT_GENERATION_QUEUE','camera_manifest':'05_promptok/GDESIGN3D_20261127/CAMERA_RESUME_MANIFEST.json','fixed_views':{a:len(c) for a,c in cams.items()},'catalog_audit':{'base_cards':len(bases),'module_cards':len(modules),'distinct_module_source_albums':len(modids),'base_source_albums':len(baseids),'module_source_albums_already_in_base_primary':sorted(modids&baseids),'split_source_albums':{'GD037':['M25_ENTRY_ROCK','M25_ENTRY_BRONZE'],'GD051':['M25_CHILD_GRAPHITE','M25_CHILD_POWDER']},'39_are_creative_seeds_not_39_verified_original_projects':True},'base_full_apartment_count':len(bases)*3,'base_image_counts':base_counts,'base_images':sum(base_counts.values()),'module_records':records,'module_gross_counts':dict(gross),'module_gross_total':sum(gross.values()),'optional_function_counts':dict(optcount),'optional_function_images':sum(optcount.values()),'base_plus_separate_modules_gross_by_apartment':{a:base_counts[a]+gross[a] for a in cams},'base_plus_separate_modules_gross':sum(base_counts.values())+sum(gross.values()),'optional_inclusive_gross':sum(base_counts.values())+sum(gross.values())+sum(optcount.values()),'net_count_rule':'1482 + unique additional module jobs - module jobs already rendered identically within a selected baseline. No baseline room assignment exists, so exact net total is not yet fixed. Same source album alone does not prove identical output: host scheme, apartment, camera, function and lighting must match.','unique_job_key':['host_base_or_variant','module_or_base_design','apartment','physical_room','camera','function_variant','lighting_variant'],'count_boundaries':['One final accepted image per listed camera; corrections/retries excluded.','Cam_02_DAY is already one of the 38 views; do not add a second day-pass globally.','No Cartesian product of all bedrooms × all bathrooms × all bases.','Commercial/hospitality 11 cards, outdoor 2 cards and archive 15 cards are outside this 39+57 estimate; they require explicit separate adaptation scope.','A902 has no standalone study, child, hall, wardrobe-room or terrace camera in this 7-view manifest. Wardrobe design is counted in existing master views only.','Open-plan consistency: a separate kitchen/dining study is a module comparison, not a new complete 38-view home. If a chosen module changes visible furniture in other views, regenerate only affected cameras as a later selected variant.','Stair-only GD24_F13 and meditation GD021 have zero direct default room slots; optional dry-room/detail adaptations are separately counted.','Nominal master/wardrobe cameras may overlap; set union removes duplicate cameras.'],'default_role_map':{'A811':{'master':'master','BED1':'guest/study'},'A812':{'master':'master','BED1':'child','BED2':'study'},'A902':{'master':'master'}},'source_role_camera_map':role,'base_records':[{'id':b['id'],'title_hu':b['title'],'source_album_ids':b['ids'],'candidate_module_source_ids':b['companions'],'source_relationship':b['status']} for b in bases]}
(out/'MODULE_CAMERA_COUNT_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
lines=['# G.Design – duplikációmentes képszám audit','',f'**39 teljes lakóalap × (15 + 16 + 7) nézet = {result["base_images"]} kép, 117 lakásváltozat.**','',f'A külön 57 modulkártya 55 forrásalbumot jelent. A GD037 két előteret, a GD051 két eltérő gyerekszobát ad. A modulok saját albumai és a 39 alap saját/igazolt tagalbumjai között nincs forrásazonosító-átfedés. A galériában látható javasolt társítás nem jelenti, hogy azt már beválasztottuk az alapváltozatba.','',f'Az alábbi explicit szerep- és kameratérkép szerint a külön modulkör **{sum(gross.values())} kép**. A teljes alapokkal együtt bruttó **{result["base_plus_separate_modules_gross"]} kép**. További, külön jelölt funkció-/részletváltozat: **{sum(optcount.values())} kép**; ezekkel bruttó **{result["optional_inclusive_gross"]} kép**. Ez nem végleges nettó generálási sor: a tényleges alaphoz rendelt és már az alapban elkészített modulokat le kell vonni.','', '## Mire elég a 39 és az 57?','', 'A 39 lakóalap kreatív kiindulás, nem 39 bizonyítottan külön eredeti projekt. Részleges konyha/étkező vagy galériatér is van közöttük; a hiányzó szobák új tervezést igényelnek. A Ződ, Dunakanyar, Balaton-parti kislakás, a 2024-es igazolt sorozatok már összevont csoportok; tagalbumjaikból nem kell új teljes lakást számolni. A külön forrású modulok hozzáadása csak javaslat.','', 'A számítás az alábbi 39+57 lakó-/helyiségkörre szól. A 11 kereskedelmi/szálláshelyi, 2 kültéri és 15 archív kártya külön feladatkör; nem rejtett 38 képes lakásváltozat.','', '## Helyiség és kamera','', '| Modul | A811 | A812 | A902 | Összesen | Külön opció |','|---|---:|---:|---:|---:|---:|']
for r in records:lines.append(f'| {r["id"]} – {r["title_hu"]} | {r["image_counts"]["A811"]} | {r["image_counts"]["A812"]} | {r["image_counts"]["A902"]} | {r["total"]} | {r["optional_function_variant"]["count"] if r["optional_function_variant"] else 0} |')
lines+=['', '## Nettó sor felépítése','', '1. Minden teljes alapnál rögzíteni kell a kiválasztott háló-, fürdő-, konyha- és előtérforrást.','2. Modulonként egy elsődleges gazdakoncepciót kell kijelölni. A többi javasolt gazda nem automatikusan új képsor.','3. A már elkészült, azonos lakás + helyiség + kamera + funkció + fény + teljes környezet kombinációt újra kell használni. Ugyanaz a referencia más környezettel önmagában nem duplikátum.','4. A modulcsere teljes lakásváltozattá csak kiválasztás után bővül. Az egymásra látó helyiségek összes érintett nézete ekkor frissítendő.','', 'A 38 nézet tartalmazza a 902 világosabb nappali változatát. Új teraszkamera vagy új fürdőnézet nincs ebben a darabszámban. Gyerekszoba, dolgozó, pihenő kizárólag meglévő száraz szoba funkcióváltozata lehet; rögzített vizes helyiséget nem alakítunk át. A 902 master megmarad; külön gyerek- vagy dolgozószoba oda nem számolható.','', 'A géppel olvasható JSON minden modult és konkrét kameraazonosítót tartalmaz. A meglévő archívum változatlan.']
(out/'MODULE_CAMERA_COUNT_ANALYSIS.md').write_text('\n'.join(lines)+'\n')
print(json.dumps({k:v for k,v in result.items() if k in ['catalog_audit','base_images','module_gross_counts','module_gross_total','optional_function_counts','optional_function_images','base_plus_separate_modules_gross','optional_inclusive_gross']},ensure_ascii=False,indent=2))
