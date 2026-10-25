import subprocess, csv, io, json, hashlib, os, sys
sys.path.insert(0, '/home/claude/build')
from headers import LOCK
R='/home/claude/wsg-berendezes'; OC='7d3c67f823c646d9daef06b294826e89c1c61467'; AC='94f80688dff460dd1c726e3bca2338d603f047c6'
OB='competition/opus55-v3-1-20261025'; AB='integrator/opus55-v3-1-audit-20261025'
PD12='05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_2_7d3c67f'; PD13='05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_3_7d3c67f'
def gs(c,p): return subprocess.run(['git','-C',R,'show',f'{c}:{p}'],capture_output=True,check=True).stdout.decode()
plan={p['nr']:p for p in json.load(open('/home/claude/build/plan.json'))}
LOCK2=dict(LOCK)
LOCK2['Cam_02']=LOCK['Cam_02'].replace("3. Forbidden:", "   f) Image 1b shows the SAME camera with one dark-grey block on W01: it marks the whole TV-wall composition zone (4.00 m wide, floor to ceiling, at most 0.40 m deep). The TV-wall design of the brief must occupy exactly this block's place and shape – a long, strongly foreshortened band receding from the left edge to the corner at about 48 %. Its near (left) end is cut by the left image edge; its far end touches the corner.\n3. Forbidden:")
EXTRA_LOCK={
 '27':"   h) The west row ends at the end of the parapet: its rounded champagne end panel stays within the parapet's length – nothing projects beyond the parapet end into the dining zone.\n",
 '50':"   k) Through the opening above the parapet only the entrance hall with white walls and the apartment entrance door may appear – do not invent any window there.\n",
 '52':"   e) Furniture only as listed in the brief: nothing in the left foreground (no chest of drawers, commode, pouf or bench).\n",
}
CAMTXT={'Cam_02':'Cam_02 (living room – terrace)','Cam_12':'Cam_12 v3 (living room hero)','Cam_03':'Cam_03 K1 (kitchen – dining)','Cam_04':'Cam_04 (master bedroom)','Cam_11':'Cam_11 (master bedroom panorama)','Cam_10':'Cam_10 (bathroom 06.2)'}
REGEN={'01':'v2','07':'v2','13':'v1','19':'v1','25':'v1','31':'v1','37':'v1','43':'v1','49':'v1','55':'v1','14':'v2','17':'v2','20':'v2','27':'v2','50':'v2','52':'v2'}
V13={'13','19','25','31','37','43','49','55','14','20'}
out='/home/claude/build/uzenetek_v2'; os.makedirs(out,exist_ok=True); plan2=[]
for nr,ver in REGEN.items():
    p=plan[nr]; kid=p['kep_id']; cam=p['kamera']
    if nr in V13:
        src=f'{PD13}/{kid}_v1_3.prompt.md'; body=open(f'/home/claude/patch13/{kid}_v1_3.prompt.md').read(); srcline=f'integrator v1.3 corrected copy (K-02/K-03, Claude 2026-10-25, from {OB} @ {OC}), {src}'
    elif p['v1_2']:
        src=f'{PD12}/{kid}_v1_2.prompt.md'; body=gs(AC,src); srcline=f'integrator v1.2 corrected copy (K-02/K-03), {AB} @ {AC}, {src}'
    else:
        src=f"05_promptok/KEP004_OPUS55_V3_1_r1/20_PROMPTOK/{kid}.prompt.md"; body=gs(OC,src); srcline=f'{OB} @ {OC}, {src}'
    body=body.strip('\n'); assert body.startswith(f'=== BEGIN PROMPT {kid} ===') and body.endswith(f'=== END PROMPT {kid} ===')
    imgs=[]
    if cam=='Cam_02':
        imgs=[('Cam_02_image1_A902_Alap-v2b1k13_blender_02_nappali-terasz_KORR_semleges.png',"the MANDATORY geometry and camera reference – a neutral, daylit Blender render of the real apartment shell from the exact camera Cam_02 (same camera as before, only better lit so wall planes read). Nothing in image 1 may be moved, added or removed: walls, corners, openings, parapets, glazing, ceiling and floor lines stay exactly where they are. Its flat colours are neutral placeholders, not the materials."),
              ('Cam_02_image1b_A902_Cam02_KORR_1b_TVfal_zona.png',"the same camera with one dark-grey block marking the W01 TV-wall zone – placement and perspective guide only; the block colour is not a material.")]
    else:
        imgs=[(p['image1'],f"the MANDATORY geometry and camera reference – a neutral Blender render of the real apartment shell from the exact camera {cam}. Nothing in image 1 may be moved, added or removed: walls, corners, openings, doors, parapets, glazing, ceiling and floor lines stay exactly where they are. Its flat colours are neutral placeholders, not the materials.")]
    if cam=='Cam_10':
        imgs.append((p['image2'],"real site photo of this bathroom as built (Geostone tiles, decor wall, black fittings, basin) – material and fitting reference only, taken from a different position. Not a camera or layout reference."))
    else:
        imgs.append((p['image2'],"real site photo of the existing floor and skirting – material and colour reference only: a medium grey-brown oak-look laminate with visible grain and knots and matching skirting. Keep exactly this tone – not lighter, not warmer, not more orange. Not a camera or layout reference."))
    WHAT={'photo_A902_04_ME-BAL-045_nappali_terasz_fele.jpg':'living room towards the terrace','photo_A902_11_ME-BAL-004_terasz_dobogo_ajto.jpg':'the terrace, the raised WPC deck and the terrace door','photo_A902_12_ME-BAL-003_zoldteto_fu_korlat_kilatas.jpg':'the green roof, the railing and the real view','photo_A902_04_ME-BAL-046_nappali_eloter_fele.jpg':'living room towards the entrance hall','photo_A902_02_ME-BAL-056_konyhafal_kiallasok.jpg':'the kitchen wall with its existing outlets','photo_A902_00_ME-BAL-077_szoba_uvegfal_kilatas.jpg':'the master-bedroom glass wall and the real view','photo_A902_06-2_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg':'the WC niche, towel radiator and door of this bathroom'}
    extra=p['extra'] or {'Cam_02':['photo_A902_04_ME-BAL-045_nappali_terasz_fele.jpg','photo_A902_11_ME-BAL-004_terasz_dobogo_ajto.jpg','photo_A902_12_ME-BAL-003_zoldteto_fu_korlat_kilatas.jpg']}.get(cam,[])
    for e in extra: imgs.append((e,f"real site photo of {WHAT[e]}, taken from a DIFFERENT position – reference ONLY for the real existing materials, surfaces, railing, terrace and outside view. Do NOT copy its camera, framing or layout; image 1 decides the geometry."))
    labels=['1','1b','2','3','4','5'] if cam=='Cam_02' else ['1','2','3','4','5']
    roles='\n'.join(f"- Image {labels[i]} ({fn}): {txt}" for i,(fn,txt) in enumerate(imgs))
    lock=LOCK2[cam]
    if nr in EXTRA_LOCK: lock=lock.replace("3. Forbidden:", EXTRA_LOCK[nr]+"3. Forbidden:")
    hdr=f"""WSG A-902 · OPUS55-V3.1 · {kid} · camera {CAMTXT[cam]} · {'re-run '+ver if ver=='v2' else 'run v1'} (corrected package)
STATUS: CONCEPT TEST – NOT VALIDATED (KONCEPCIÓ – NEM VALIDÁLT)

Please generate exactly ONE image. Read the GEOMETRY LOCK first; it overrides anything in the creative brief that conflicts with image 1.

ATTACHED IMAGES AND THEIR ROLES (in this order)
{roles}

GEOMETRY LOCK (mandatory)
{lock}
4. Output: exactly one photorealistic image, same framing and 16:10 landscape aspect as image 1, no text, no labels, no collage, no split view.
5. If anything in the creative brief below conflicts with image 1, image 1 wins.

CREATIVE BRIEF – Claude Opus 5.5 V3.1 prompt, verbatim (source: {srcline}):

"""
    msg=hdr+body+'\n'; fn=f"{nr}_{kid}__{ver}.txt"; open(f'{out}/{fn}','w').write(msg)
    plan2.append(dict(nr=nr,kep_id=kid,kamera=cam,verzio=ver,prompt_forras=srcline,csatolmanyok=[i[0] for i in imgs],uzenet=fn,uzenet_sha256=hashlib.sha256(msg.encode()).hexdigest(),cel_fajl=f'{kid}__OPUS55_V3_1__{ver}.png'))
json.dump(plan2,open('/home/claude/build/plan_v2.json','w'),ensure_ascii=False,indent=1)
print(len(plan2))
