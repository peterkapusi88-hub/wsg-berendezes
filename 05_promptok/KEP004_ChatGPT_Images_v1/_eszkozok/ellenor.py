# Összefűzött promptok szó szerinti ellenőrzése a forrásokkal + csomagteljesség (csak olvas). Claude, 2026-10-24.
import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import forrasok as F, epito as E
hibak, sorok = [], []
for nr, kod, cam, lepes, statusz in E.CSOMAGOK:
    L = E.bemenetek(kod, cam); id_ = E.kepid(kod, cam)
    p = open(E.REPO_P + id_ + '.prompt.txt', encoding='utf-8').read()
    m = E.KOR + f'{nr:02d}_{id_}/'; pm = open(m + f'PROMPT_{id_}.prompt.txt', encoding='utf-8').read()
    r = E.ROOM[cam]; s = E.STY[kod]; ok = {}
    ok['mac=repo'] = (p == pm)
    ok['kozos_fixed'] = F.kozos_fixed().replace('{ROOM}', r[1]).replace('{STYLE_NAME}', s[1]) in p
    if cam == 'Cam_10': ok['helyiseg_fixed'] = F.cam10_csere() in p and 'Camera Cam_10_Furdo_06_2 (PROVISIONAL' not in p
    elif cam == 'Cam_11': ok['helyiseg_fixed'] = F.cam11_csere() in p and F.helyiseg_fixed('Cam_04 · master háló 05.1') not in p
    else: ok['helyiseg_fixed'] = F.helyiseg_fixed(r[2]) in p
    ok['hue'] = F.hue_blokk() in p
    if cam in ('Cam_04', 'Cam_11'): ok['gardrob'] = F.gardrob_blokk() in p and ((E.KAL_FRONT[kod] if kod in E.KAL_FRONT else F.gardrob_front(kod)) in p)
    if kod in ('S01', 'S02'):
        blokk = F.astra(f"{s[0]} · {r[0]} ({'Cam_04' if cam == 'Cam_11' else cam})"); ok['astra_szo_szerint'] = blokk in p
        out = re.search(r'Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/(\S+)\.png', blokk).group(1)
        ok['kep_id=Astra_Output'] = (out == id_) if cam != 'Cam_11' else (out.replace('_Cam_04_', '_Cam_11_') == id_ and id_ in p.split('=== RUN NOTES')[1])
    else:
        ok['kalibracio'] = F.kalibracio(kod) in p and F.koncepcio_cella('Zenit' if kod == 'C1' else 'Lake Forest', 'Nappali' if cam == 'Cam_02' else 'Master háló') in p
    ok['nincs_helyorzo'] = '{ROOM}' not in p and '{STYLE_NAME}' not in p
    jegyz = p.split('=== RUN NOTES')[1]
    lampak = {'SOMAR': 'Somar', 'BRISIA': 'Brisia', 'BRISIA50': 'Brisia pendant', 'RAZE': 'Raze', 'ALEYLA': 'Aleyla'}
    for k in E.TERMEKEK.get((kod, cam), []):
        if k in lampak: ok[f'hue_jegyzet_{lampak[k]}'] = any(l.startswith('- Hue check') and lampak[k] in l for l in jegyz.split('\n'))
    if 'BRISIA50' in E.TERMEKEK.get((kod, cam), []): ok['brisia_fuggeszto_csere'] = 'one frosted glass globe Ø50 cm' in jegyz and 'L00152CR05' in jegyz
    if kod in ('S01', 'S02') and cam == 'Cam_04': ok['olvasolampa'] = ('Raze' if kod == 'S01' else 'Aleyla') in jegyz and 'D20/21 and D22/23' in jegyz
    if cam == 'Cam_04': ok['ket_kamera'] = 'shown from two cameras' in jegyz and 'BLOCKED' not in p
    if cam == 'Cam_11': ok['ket_kamera'] = 'same chat directly after the Cam_04 image' in jegyz
    if 'CISELIA' in E.TERMEKEK.get((kod, cam), []): ok['ciselia_meret'] = 'width 52.5 × depth 55 × height 75 cm, seat height 47 cm' in jegyz
    if 'EAMY' in E.TERMEKEK.get((kod, cam), []): ok['eamy_meret'] = 'width 55 × depth 53 × height 75 cm, seat height 46 cm' in jegyz
    ok['nincs_hianyzo_kave'] = not any(f.startswith('_HIANYZIK_') for f in os.listdir(m))
    megvan = sum(1 for f, src, en, hu in L if src and os.path.exists(m + f)); hianyzik = [f for f, src, en, hu in L if not src]
    ok['csatolmany_fajlok'] = megvan == sum(1 for x in L if x[1])
    ok['fejlec_listaszam'] = p.split('OUTPUT:')[0].count('\n- ') == len(L)
    for k, v in ok.items():
        if not v: hibak.append(f'{id_}: {k}')
    sorok.append(dict(nr=nr, id=id_, lepes=lepes, karakter=len(p), csatolmany=len(L), megvan=megvan, kave_hianyzik=len(hianyzik), ellenorzesek=ok))
for x in sorok: print(f"{x['nr']:02d} {x['id']:<48} {x['lepes']} kar={x['karakter']:>5} csat={x['csatolmany']} megvan={x['megvan']} KH-hiány={x['kave_hianyzik']}  " + ' '.join(k + ('✓' if v else '✗') for k, v in x['ellenorzesek'].items()))
print('HIBÁK:', hibak or 'nincs')
json.dump(dict(datum='2026-10-24', hibak=hibak, csomagok=sorok), open(os.path.dirname(os.path.abspath(__file__)) + '/ellenorzes_promptok_v1.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
