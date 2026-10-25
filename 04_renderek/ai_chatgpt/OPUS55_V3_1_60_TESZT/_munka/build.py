import subprocess, csv, io, json, hashlib, os, sys
sys.path.insert(0, '/home/claude/build')
from headers import LOCK
R='/home/claude/wsg-berendezes'
OC='7d3c67f823c646d9daef06b294826e89c1c61467'
AC='94f80688dff460dd1c726e3bca2338d603f047c6'
OB='competition/opus55-v3-1-20261025'; AB='integrator/opus55-v3-1-audit-20261025'
PD='05_promptok/KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_2_7d3c67f'
def gs(c,p): return subprocess.run(['git','-C',R,'show',f'{c}:{p}'],capture_output=True,check=True).stdout
man=gs(OC,'05_promptok/KEP004_OPUS55_V3_1_r1/01_MANIFEST_66.csv').decode()
rows=list(csv.DictReader(io.StringIO(man),delimiter=';'))[:60]
assert len(rows)==60 and rows[-1]['nr']=='60'
PATCH={'A902_S01_KyotoInk_1_nappali-hero_Cam_12_A','A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A','A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A','A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A'}
REF={ # camera -> (image1 file, role-source)
 'Cam_02':('Cam_02_image1_A902_Alap-v2b1_blender_02_nappali-terasz.png','04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png @7d3c67f'),
 'Cam_12':('Cam_12_image1_A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png','04_renderek/A902_cam12_v3_korrekcio/A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png @09c2762 (same Cam_12 v3 camera as A902_kameracsomag_C/..._JAVASLAT_v3.png, readable lighting)'),
 'Cam_03':('Cam_03_image1_A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png','04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png @7d3c67f'),
 'Cam_04':('Cam_04_image1_A902_Alap-v2b1_blender_04_master.png','04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png @7d3c67f'),
 'Cam_11':('Cam_11_image1_A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png','04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png @7d3c67f'),
 'Cam_10':('Cam_10_image1_A902_Alap-v2b1_blender_10_furdo-06-2.png','04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png @7d3c67f'),
}
FLOOR='image2_A902_04_ME-BAL-080_parketta_szegely_kozel.jpg'
BATH='image2_A902_06-2_ME-BAL-064_zuhany_mosdo.jpg'
CAMTXT={'Cam_02':'Cam_02 (living room – terrace)','Cam_12':'Cam_12 v3 (living room hero)','Cam_03':'Cam_03 K1 (kitchen – dining)','Cam_04':'Cam_04 (master bedroom)','Cam_11':'Cam_11 (master bedroom panorama)','Cam_10':'Cam_10 (bathroom 06.2)'}
out='/home/claude/build/uzenetek'; os.makedirs(out,exist_ok=True)
plan=[]
for r in rows:
    kid=r['kep_id']; cam=r['kamera']
    if kid in PATCH:
        src=f'{PD}/{kid}_v1_2.prompt.md'; body=gs(AC,src).decode(); srcline=f'integrator v1.2 corrected copy (K-02/K-03), {AB} @ {AC}, {src}'; patched=True
    else:
        src=r['fajl']; body=gs(OC,src).decode(); srcline=f'{OB} @ {OC}, {src}'; patched=False
    body=body.strip('\n')
    assert body.startswith(f'=== BEGIN PROMPT {kid} ===') and body.endswith(f'=== END PROMPT {kid} ==='), kid
    img1=REF[cam][0]
    if cam=='Cam_10':
        img2=BATH; img2role="real site photo of this bathroom as built (Geostone tiles, decor wall, black fittings, basin) – material and fitting reference only, taken from a different position. Not a camera or layout reference."
    else:
        img2=FLOOR; img2role="real site photo of the existing floor and skirting – material and colour reference only: a medium grey-brown oak-look laminate with visible grain and knots and matching skirting. Keep exactly this tone – not lighter, not warmer, not more orange. Not a camera or layout reference."
    EXTRA={'Cam_02':[('photo_A902_04_ME-BAL-045_nappali_terasz_fele.jpg','living room towards the terrace'),('photo_A902_11_ME-BAL-004_terasz_dobogo_ajto.jpg','the terrace, the raised WPC deck and the terrace door'),('photo_A902_12_ME-BAL-003_zoldteto_fu_korlat_kilatas.jpg','the green roof, the railing and the real view')],
     'Cam_12':[('photo_A902_04_ME-BAL-046_nappali_eloter_fele.jpg','living room towards the entrance hall')],
     'Cam_03':[('photo_A902_02_ME-BAL-056_konyhafal_kiallasok.jpg','the kitchen wall with its existing outlets')],
     'Cam_11':[('photo_A902_00_ME-BAL-077_szoba_uvegfal_kilatas.jpg','the master-bedroom glass wall and the real view')],
     'Cam_10':[('photo_A902_06-2_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg','the WC niche, towel radiator and door of this bathroom')],
     'Cam_04':[]}[cam]
    extra_txt=''.join(f"\n- Image {i+3} ({fn}): real site photo of {what}, taken from a DIFFERENT position – reference ONLY for the real existing materials, surfaces, railing, terrace and outside view. Do NOT copy its camera, framing or layout; image 1 decides the geometry." for i,(fn,what) in enumerate(EXTRA))
    hdr=f"""WSG A-902 · OPUS55-V3.1 · {kid} · camera {CAMTXT[cam]}
STATUS: CONCEPT TEST – NOT VALIDATED (KONCEPCIÓ – NEM VALIDÁLT)

Please generate exactly ONE image. Read the GEOMETRY LOCK first; it overrides anything in the creative brief that conflicts with image 1.

ATTACHED IMAGES AND THEIR ROLES
- Image 1 ({img1}): the MANDATORY geometry and camera reference – a neutral Blender render of the real apartment shell from the exact camera {cam}. Nothing in image 1 may be moved, added or removed: walls, corners, openings, doors, parapets, glazing, ceiling and floor lines stay exactly where they are. Its flat colours are neutral placeholders, not the materials.
- Image 2 ({img2}): {img2role}{extra_txt}

GEOMETRY LOCK (mandatory)
{LOCK[cam]}
4. Output: exactly one photorealistic image, same framing and 16:10 landscape aspect as image 1, no text, no labels, no collage, no split view.
5. If anything in the creative brief below conflicts with image 1, image 1 wins.

CREATIVE BRIEF – Claude Opus 5.5 V3.1 prompt, verbatim and unchanged (source: {srcline}):

"""
    msg=hdr+body+'\n'
    fn=f"{r['nr']}_{kid}.txt"
    open(f'{out}/{fn}','w').write(msg)
    plan.append(dict(nr=r['nr'],kep_id=kid,stilus=r['stilus'],kamera=cam,prompt_forras=srcline,v1_2=patched,image1=img1,image2=img2,extra=[e[0] for e in EXTRA],uzenet=fn,uzenet_chars=len(msg),uzenet_sha256=hashlib.sha256(msg.encode()).hexdigest(),prompt_sha256=hashlib.sha256(body.encode()).hexdigest(),cel_fajl=f'{kid}__OPUS55_V3_1__v1.png'))
json.dump(plan,open('/home/claude/build/plan.json','w'),ensure_ascii=False,indent=1)
print(len(plan), max(p['uzenet_chars'] for p in plan), min(p['uzenet_chars'] for p in plan), sum(p['v1_2'] for p in plan))
