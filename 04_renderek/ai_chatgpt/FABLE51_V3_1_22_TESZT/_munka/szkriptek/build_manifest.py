import csv, json, hashlib, os
D = '/home/claude/wsg-renders/04_renderek/ai_chatgpt/FABLE51_V3_1_22_TESZT/'
terv = {x['kep_id']: x for x in json.load(open('/home/claude/fable_msgs/_terv.json'))}
log = {r[0]: r for r in csv.reader(open('/home/claude/fable_out/log.csv', encoding='utf-8'), delimiter=';') if r and r[0] != 'nr'}
gate = {r[0]: r for r in csv.reader(open('/home/claude/fable_out/gate.csv', encoding='utf-8'), delimiter=';') if r and r[0] != 'nr'}
REFPATH = {
 'Cam_02_ref1_ALAPKEP_A902_Alap-v2b1_blender_02_nappali-terasz.png': '04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_02_nappali-terasz.png',
 'Cam_12_ref1_ALAPKEP_A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png': '04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png',
 'Cam_03_ref1_ALAPKEP_A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png': '04_renderek/A902_kameracsomag_C/A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png',
 'Cam_04_ref1_ALAPKEP_A902_Alap-v2b1_blender_04_master.png': '04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_04_master.png',
 'Cam_11_ref1_ALAPKEP_A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png': '04_renderek/A902_cam11_javaslat_v1/A902_Alap-v2b1k11_blender_11_master-panorama_JAVASLAT.png',
 'Cam_10_ref1_ALAPKEP_A902_Alap-v2b1_blender_10_furdo-06-2.png': '04_renderek/A902_alap_v2b1/A902_Alap-v2b1_blender_10_furdo-06-2.png',
 'REF_padlo_ME-BAL-080_parketta_szegely_kozel.jpg': '08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg',
 'REF_ME-BAL-045_nappali_terasz_fele.jpg': '08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg',
 'REF_ME-BAL-046_nappali_eloter_fele.jpg': '08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-046_nappali_eloter_fele.jpg',
 'REF_ME-BAL-004_terasz_WPC_dobogo_ajto.jpg': '08_allapotfelmeres/fotok/A902/11_terasz-WPC/A902_11_20261021_ME-BAL-004_terasz_dobogo_ajto.jpg',
 'REF_ME-BAL-074_sotet_tegla_teraszajto.jpg': '08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-074_homlokzat_sotet_tegla_teraszajto.jpg',
 'REF_ME-BAL-003_zoldteto_korlat_kilatas.jpg': '08_allapotfelmeres/fotok/A902/12_zoldtető/A902_12_20261021_ME-BAL-003_zoldtető_fu_korlat_kilatas.jpg',
 'REF_ME-BAL-077_master_uvegfal_kilatas.jpg': '08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-077_szoba_uvegfal_kilatas.jpg',
 'REF_ME-BAL-056_konyhafal.jpg': '08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg',
 'REF_ME-BAL-064_furdo06-2_zuhany_mosdo.jpg': '08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-064_zuhany_mosdo.jpg',
 'REF_ME-BAL-066_furdo06-2_wc_fulke.jpg': '08_allapotfelmeres/fotok/A902/06-2_furdo/A902_06-2_20261021_ME-BAL-066_wc_fulke_torolkozoszarito_ajto.jpg',
}
KORR = {'06','08','10','12','22'}
KORR_REFS = ['integrator/cam12-v3-korrekcio-20261025: 05_promptok/KEP004_FABLE51_V3_1_CAM12_KORREKCIO/csomag_S01/01_image1_A902_Cam12v3_KORR_semleges.png (sha 8ffd40c0…)', REFPATH['REF_padlo_ME-BAL-080_parketta_szegely_kozel.jpg'], REFPATH['REF_ME-BAL-046_nappali_eloter_fele.jpg']]
items = sorted(terv.items(), key=lambda kv: kv[1]['nr'])
items.insert([i for i,(k,_) in enumerate(items) if _['nr']==13][0]+1, ('A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A', dict(terv['A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A'], nr='13v2')))
rows = []
for kid, t in items:
    nrs = t['nr'] if isinstance(t['nr'], str) else f"{t['nr']:02d}"
    lg = log.get(nrs, ['', '', '', 'NINCS', '', '']); g = gate.get(nrs)
    refs = t['refs'][:]
    if kid == 'A902_S02_BiBoNocturne_3_master_Cam_04_A':
        refs = [r for r in refs if 'ME-BAL-077' not in r]
    fn = kid + ('__FABLE51_V3_1__v2.png' if nrs=='13v2' else '__FABLE51_V3_1__v1.png')
    p = D + fn
    st = lg[3]
    gen = 'DONE' if os.path.exists(p) else ('BLOCKED' if st.startswith('DEFERRED') else 'FAILED')
    rows.append({
        'nr': nrs, 'kep_id': kid, 'kamera': t['kamera'],
        'forras_branch': 'competition/fable51-v3-1-20261025', 'forras_commit': 'b44541205cdd79e3d1f33ee8074c2bc280beb7a7',
        'promptfajl': f'05_promptok/KEP004_FABLE51_V3_1_r1/20_PROMPTOK/{kid}.prompt.md', 'prompt_verzio': 'FABLE51-V3.1 r1 (szó szerint, BEGIN/END között)',
        'kuldott_uzenet': (f'04_renderek/ai_chatgpt/FABLE51_V3_1_22_TESZT/uzenetek/cam12_v3/{nrs}_{kid}__CAM12V3KORR.txt' if nrs in KORR else f"04_renderek/ai_chatgpt/FABLE51_V3_1_22_TESZT/uzenetek/{nrs[:2]}_{kid}.txt"),
        'referenciak_sorrendben': ' | '.join(KORR_REFS) if nrs in KORR else ' | '.join(REFPATH[r] for r in refs),
        'chatgpt_link': lg[2], 'generalas': gen,
        'blokk_ok': ('Cam_12 v3 KORR módszer: Péter 07:46 visszatartás után 08:26-os mehet; integrátori geometriai fejléc + Fable-prompt szó szerint' if nrs in KORR else ('13 v2: újragenerálás Péter kérésére, azonos bemenet' if nrs=='13v2' else '')),
        'fajl': ('04_renderek/ai_chatgpt/FABLE51_V3_1_22_TESZT/' + fn) if gen == 'DONE' else '',
        'mac_utvonal': ('~/Downloads/WSG_FABLE51_V3_1_RENDEREK/' + fn) if gen == 'DONE' else '',
        'meret': g[2] if g else '', 'sha256': hashlib.sha256(open(p, 'rb').read()).hexdigest() if gen == 'DONE' else '',
        'kreativ': g[3] if g else '', 'geometria': g[4] if g else '', 'geometriai_elteresek': g[5] if g else '',
        'padlo': g[6] if g else '', 'termek_elteresek': g[7] if g else '', 'statusz': 'KONCEPCIÓ – NEM VALIDÁLT',
        'gate_kep': f'04_renderek/ai_chatgpt/FABLE51_V3_1_22_TESZT/_gate/' + (fn.replace('.png','') + '__gate.jpg' if (nrs in KORR or nrs=='13v2') else kid + '__gate.jpg') if gen == 'DONE' else '',
    })
with open(D + 'MANIFEST_FABLE51_V3_1_22.csv', 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=';'); w.writeheader(); w.writerows(rows)
from collections import Counter
print(Counter(r['generalas'] for r in rows)); print(Counter(' '.join(r['geometria'].split(' ')[:2]) for r in rows)); print(len(rows))
