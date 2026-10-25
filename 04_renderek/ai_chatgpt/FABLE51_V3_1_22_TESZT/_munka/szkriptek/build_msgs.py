import re, json, os, shutil
os.chdir('/home/claude/wsg-berendezes')
O = '/mnt/user-data/outputs/WSG_FABLE51_V3_1_REF'
os.makedirs(O + '/uzenetek', exist_ok=True)
shutil.copy('08_allapotfelmeres/fotok/A902/12_zoldtető/A902_12_20261021_ME-BAL-003_zoldtető_fu_korlat_kilatas.jpg',
            O + '/REF_ME-BAL-003_zoldteto_korlat_kilatas.jpg')
P = '05_promptok/KEP004_FABLE51_V3_1_r1/20_PROMPTOK/'
order = """A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A
A902_S01_KyotoInk_1_nappali-hero_Cam_12_A
A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A
A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A
A902_S03_AleliCasa_1_nappali-terasz_Cam_02_A
A902_S03_AleliCasa_1_nappali-hero_Cam_12_A
A902_S06_ZenitAtelier_1_nappali-terasz_Cam_02_A
A902_S06_ZenitAtelier_1_nappali-hero_Cam_12_A
A902_S04_LAHorizon_1_nappali-terasz_Cam_02_A
A902_S04_LAHorizon_1_nappali-hero_Cam_12_A
A902_S05_MiamiStreamline_1_nappali-terasz_Cam_02_A
A902_S05_MiamiStreamline_1_nappali-hero_Cam_12_A
A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A
A902_S01_KyotoInk_3_master_Cam_04_A
A902_S01_KyotoInk_3_master_Cam_11_A
A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A
A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A
A902_S02_BiBoNocturne_3_master_Cam_04_A
A902_S02_BiBoNocturne_3_master_Cam_11_A
A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A
A902_S07_LakeForestCouture_1_nappali-terasz_Cam_02_A
A902_S07_LakeForestCouture_1_nappali-hero_Cam_12_A""".split()
FLOOR = ('REF_padlo_ME-BAL-080_parketta_szegely_kozel.jpg',
         'real site photo of the existing laminate floor and skirting (colour, grain, plank direction) - match it; the exact decor code is not verified')
refs = {
    'Cam_02': [('Cam_02_ref1_ALAPKEP_A902_Alap-v2b1_blender_02_nappali-terasz.png', 'neutral Blender base image of camera Cam_02 - AUTHORITATIVE for room shell, camera, framing, openings and floor-wall lines'), FLOOR,
               ('REF_ME-BAL-045_nappali_terasz_fele.jpg', 'real site photo of this living room towards the glass wall and terrace - real window frames and terrace'),
               ('REF_ME-BAL-004_terasz_WPC_dobogo_ajto.jpg', 'real site photo of the terrace: light-grey tiles, raised brown WPC deck, steps, anthracite frames'),
               ('REF_ME-BAL-074_sotet_tegla_teraszajto.jpg', 'real site photo of the dark brick reveal around the terrace glazing'),
               ('REF_ME-BAL-003_zoldteto_korlat_kilatas.jpg', 'real site photo of the green roof, railing and the real city / Buda hills panorama')],
    'Cam_12': [('Cam_12_ref1_ALAPKEP_A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png', 'neutral Blender base image of camera Cam_12 (hero v3) - AUTHORITATIVE for room shell, camera, framing, openings and floor-wall lines'), FLOOR,
               ('REF_ME-BAL-046_nappali_eloter_fele.jpg', 'real site photo of this living/kitchen zone towards the entrance - real white walls, light-grey doors, existing surfaces')],
    'Cam_03': [('Cam_03_ref1_ALAPKEP_A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png', 'neutral Blender base image of camera Cam_03 K1 - AUTHORITATIVE for room shell, camera, framing, openings and floor-wall lines'), FLOOR,
               ('REF_ME-BAL-056_konyhafal.jpg', 'real site photo of the kitchen wall (the laminate floor continues in the kitchen, white walls)')],
    'Cam_04': [('Cam_04_ref1_ALAPKEP_A902_Alap-v2b1_blender_04_master.png', 'neutral Blender base image of camera Cam_04 - AUTHORITATIVE for room shell, camera, framing, openings and floor-wall lines'), FLOOR,
               ('REF_ME-BAL-077_master_uvegfal_kilatas.jpg', 'real site photo of the master bedroom glass wall, balcony railing and real view')],
    'Cam_11': [('Cam_11_ref1_ALAPKEP_A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png', 'neutral Blender base image of camera Cam_11 - AUTHORITATIVE for room shell, camera, framing, openings and floor-wall lines'), FLOOR,
               ('REF_ME-BAL-077_master_uvegfal_kilatas.jpg', 'real site photo of the master bedroom glass wall, balcony, light brick return and the real panorama')],
    'Cam_10': [('Cam_10_ref1_ALAPKEP_A902_Alap-v2b1_blender_10_furdo-06-2.png', 'neutral Blender base image of camera Cam_10 - AUTHORITATIVE for room shell, camera, framing and the built bathroom'),
               ('REF_ME-BAL-064_furdo06-2_zuhany_mosdo.jpg', 'real site photo of bathroom 06.2: shower, basin, real tiles and black fittings'),
               ('REF_ME-BAL-066_furdo06-2_wc_fulke.jpg', 'real site photo of bathroom 06.2: WC niche, towel radiator, door')],
}
manifest = []
for n, k in enumerate(order, 1):
    t = open(P + k + '.prompt.md', encoding='utf-8').read()
    m = re.search(r'=== BEGIN PROMPT (\S+) ===\n(.*?)\n=== END PROMPT \1 ===', t, re.S)
    assert m and m.group(1) == k, k
    cam = re.search(r'(Cam_\d+)', k).group(1)
    rs = refs[cam]
    for f, _ in rs:
        assert os.path.exists(O + '/' + f), f
    head = (f"IMAGE ID: {k}\nSOURCE VERSION: FABLE51-V3.1 (branch competition/fable51-v3-1-20261025, commit b44541205cdd79e3d1f33ee8074c2bc280beb7a7)\n"
            "STATUS: KONCEPCIÓ – NEM VALIDÁLT\n\n"
            "Please generate exactly ONE image (landscape, same aspect ratio as image 1). Attached reference images, in order:\n")
    head += "\n".join(f"- image {i}: {d}" for i, (f, d) in enumerate(rs, 1))
    head += ("\n\nKeep the original walls, ceiling, windows and doors, the existing laminate floor and real surfaces, the camera view and perspective, "
             "the real terrace and view; add only the furniture, materials and lighting named in the prompt; no new walls, pillars, rooms or invented ceiling elements.\n\n"
             "The creative prompt follows verbatim:\n\n")
    msg = head + m.group(2)
    open(f'{O}/uzenetek/{n:02d}_{k}.txt', 'w', encoding='utf-8').write(msg)
    manifest.append(dict(nr=n, kep_id=k, kamera=cam, prompt_chars=len(m.group(2)), msg_chars=len(msg), refs=[f for f, _ in rs]))
json.dump(manifest, open(f'{O}/uzenetek/_terv.json', 'w'), ensure_ascii=False, indent=1)
print(len(manifest), max(x['msg_chars'] for x in manifest))
