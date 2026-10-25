# A-902 Cam_02 – V3_TEST szürke bútortömbös referencia (1b kép) az Astra Creative Upgrade V3 r1 méreteivel
# (draft PR #16, commit be6b1f333cf2923790e4577c9b716f5fcb3bb417). Péter, 2026-10-25 01:55: „Külön figyelj arra, hogy az Astra V3
# új TV-szekrényei és magas tárolói eltérnek a korábbi Blender-tömbök méreteitől. Először ellenőrizd és szükség esetén frissítsd.”
# Alap: a main v2b-1-k11b modell (sha256 9875cd57…), lock 7aa85d70…, validátor v2 – a .blend-et NEM menti, a lockhoz nem nyúl.
# Előzmény: a 01:44–01:50-es, nem commitolt V3-tömbpróba (KEP-004/_munka/blender_cam12_v1/03_ellenorzes_tomegek.py, k12 JAVASLAT-fájl).
# Eltérés tőle (dokumentálva: 05_promptok/KEP004_ChatGPT_Images_V3_TEST/INTEGRACIO_V3_TEST.md):
#  (1) a main modellből renderel, nem a Cam_12-es JAVASLAT-fájlból; üres ellenőrző render az 1. alapképpel való egyezéshez;
#  (2) KI3-P / BN3-P egyetlen 260×190, ill. 240×190-es befoglaló – a korábbi próba a TV tengelyében (y 6,35) kettévágta a mezőt;
#  (3) BN3-V két mezőre bontva: 45 cm-es nyíló oszlop (y 4,25–4,70) + 45 cm-es fix tükör/szervizmező (y 4,70–5,15); a tükör
#      z 0,40–2,20, alatta levehető szervizlap a D18 dugaljhoz (y 4,749);
#  (4) a W02-re javasolt mű/grafika x-helye a kapcsolóoszloptól (x 7,149) távolabb, a BN3-A valódi 120 cm-es szélességgel.
# Futtatás: Blender -b <v2b-1-k11b.blend> --python 01_tomeg_cam02_v3test.py -- <kimenet>
import bpy, sys, os, json, time, hashlib, runpy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
W = os.path.dirname(os.path.abspath(__file__)) + '/'
LOCK = os.environ['WSG_LOCK']; VILL = os.environ['WSG_VILLAMOS']; VALID = os.environ['WSG_VALIDATOR']
sc = bpy.context.scene
sha = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest()
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=sha,
           lock_sha256=hashlib.sha256(open(LOCK, 'rb').read()).hexdigest(), validator={}, kepek=[], stilus={})
if not sha.startswith('9875cd57'):
    raise SystemExit('HIBA: nem a main v2b-1-k11b modell: ' + sha)
T.SZIN['tukor'] = 0.45   # a tükörmező a tömbképen középszürke (a 0,62-es tónus a fallal összemosódott – r1 render, 02:11)
MARAD = T.MARAD
cam02 = bpy.data.objects['Cam_02_Nappali_terasz']
log['kamera'] = dict(loc=[round(v, 4) for v in cam02.location], rot=[round(v, 4) for v in cam02.rotation_euler], lens=cam02.data.lens,
                     sensor=[cam02.data.sensor_width, cam02.data.sensor_height, cam02.data.sensor_fit])

def stilus_tomeg(kod):
    col = bpy.data.collections.new('Stil_TOMEG_' + kod + '_V3TEST'); sc.collection.children.link(col); rec = {}
    d = lambda nev, a, b, f: T.doboz(col, nev, a, b, f, rec)
    if kod == 'S01':
        d('S01_KI3L_also_tarolo', (3.67, 5.15, 0), (4.07, 7.55, 0.48), 'tarolo')       # 240×48×40 teljes külső
        d('S01_KI3V_torony', (3.67, 4.35, 0), (3.97, 4.95, 2.20), 'tarolo')            # 60×220×30 teljes külső
        d('S01_KI3P_panelmezo', (3.67, 5.05, 0.55), (3.71, 7.65, 2.45), 'panel')       # 260×190, max. 4 cm (két sík együtt)
        d('S01_TV_kepernyo', (3.72, 6.35 - 0.725, 0.85), (3.77, 6.35 + 0.725, 1.68), 'kepernyo')  # 65", D16/D17-zóna
        d('S01_KI3A_mu_W02', (5.65, 4.05, 0.80), (6.65, 4.08, 2.60), 'mu')             # 100×180, W02 – a Cam_02-n kívül
        XB, YS, YN, D, CH, CW = 7.17, 5.21, 7.59, 0.95, 1.80, 0.95                       # Lennon jobbos L 238×180×68
        d('S01_kanape_L_fo', (XB - D, YS + CW, 0), (XB, YN, 0.42), 'kanape')
        d('S01_kanape_L_chaise', (XB - CH, YS, 0), (XB, YS + CW, 0.42), 'kanape')
        d('S01_kanape_L_hattamla', (XB - 0.22, YS, 0.42), (XB, YN, 0.68), 'kanape')
        d('S01_kanape_L_kar', (XB - D, YN - 0.20, 0.42), (XB - 0.22, YN, 0.60), 'kanape')
        AX0, AY0, AX1, AY1, SZ, MEL, YK = 7.90, 5.27, 8.80, 7.27, 0.55, 0.53, (5.60, 6.27, 6.94)   # Toni 200×90, 6 Eamy 55×53
    else:
        d('S02_BN3L_also_tarolo', (3.67, 5.25, 0), (4.07, 7.65, 0.50), 'tarolo')       # 240×50×40 teljes külső
        d('S02_BN3V_nyilo_oszlop', (3.67, 4.25, 0), (3.99, 4.70, 2.20), 'tarolo')      # 45 cm nyíló oszlop (a 90×220×32-ből)
        d('S02_BN3V_szerviz_lap', (3.67, 4.70, 0), (3.99, 5.15, 0.40), 'tarolo')       # fix mező alja: levehető szervizlap (D18)
        d('S02_BN3R_tukor_mezo', (3.67, 4.70, 0.40), (3.99, 5.15, 2.20), 'tukor')      # 45×180 fix ezüsttükör, z 0,40–2,20
        d('S02_BN3P_panelmezo', (3.67, 5.25, 0.55), (3.71, 7.65, 2.45), 'panel')       # 240×190, max. 4 cm
        d('S02_TV_kepernyo', (3.72, 6.35 - 0.725, 0.85), (3.77, 6.35 + 0.725, 1.68), 'kepernyo')
        d('S02_BN3A_grafika_W02', (5.55, 4.05, 0.85), (6.75, 4.07, 2.45), 'mu')        # 120×160, W02 – a Cam_02-n kívül
        X1, Y0, Y1, D, AR = 7.17, 4.975, 7.825, 0.95, 1.60                              # JÄTTEBO valódi U 285×160×71
        d('S02_kanape_U_hat', (X1 - D, Y0, 0), (X1, Y1, 0.42), 'kanape')
        d('S02_kanape_U_del', (X1 - AR, Y0, 0), (X1 - D, Y0 + D, 0.42), 'kanape')
        d('S02_kanape_U_eszak', (X1 - AR, Y1 - D, 0), (X1 - D, Y1, 0.42), 'kanape')
        d('S02_kanape_U_hattamla', (X1 - 0.22, Y0, 0.42), (X1, Y1, 0.71), 'kanape')
        d('S02_kanape_U_hattamla_d', (X1 - AR, Y0, 0.42), (X1 - 0.22, Y0 + 0.22, 0.71), 'kanape')
        d('S02_kanape_U_hattamla_e', (X1 - AR, Y1 - 0.22, 0.42), (X1 - 0.22, Y1, 0.71), 'kanape')
        AX0, AY0, AX1, AY1, SZ, MEL, YK = 7.90, 5.37, 8.80, 7.17, 0.525, 0.55, (5.67, 6.27, 6.87)  # Anouk 180×90, 6 Ciselia 52,5×55
    d(f'{kod}_etkezo_asztal_lap', (AX0, AY0, 0.72), (AX1, AY1, 0.75), 'etkezo')
    d(f'{kod}_etkezo_asztal_labd', (AX0 + 0.20, AY0 + 0.25, 0), (AX1 - 0.20, AY0 + 0.33, 0.72), 'etkezo')
    d(f'{kod}_etkezo_asztal_labe', (AX0 + 0.20, AY1 - 0.33, 0), (AX1 - 0.20, AY1 - 0.25, 0.72), 'etkezo')
    for i, yc in enumerate(YK):
        x1 = AX0 + 0.18; x0 = x1 - MEL
        d(f'{kod}_etkezo_szekny{i}_ules', (x0, yc - SZ / 2, 0), (x1, yc + SZ / 2, 0.46), 'etkezo')
        d(f'{kod}_etkezo_szekny{i}_hat', (x0, yc - SZ / 2, 0.46), (x0 + 0.06, yc + SZ / 2, 0.78), 'etkezo')
        x0 = AX1 - 0.18; x1 = x0 + MEL
        d(f'{kod}_etkezo_szekk{i}_ules', (x0, yc - SZ / 2, 0), (x1, yc + SZ / 2, 0.46), 'etkezo')
        d(f'{kod}_etkezo_szekk{i}_hat', (x1 - 0.06, yc - SZ / 2, 0.46), (x1, yc + SZ / 2, 0.78), 'etkezo')
    col.hide_render = True
    return col, rec

TOMEG = {k: stilus_tomeg(k) for k in ('S01', 'S02')}

# ---- validátor (bútorréteg nélkül + a két V3-tömbréteggel) ----
def lathatosag(mod):
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        o.hide_render = True
    if mod.startswith('tomeg_'): TOMEG[mod[6:]][0].hide_render = False
os.environ['WSG_LOCK'] = LOCK; os.environ['WSG_VILLAMOS'] = VILL
for mod in ('ures', 'tomeg_S01', 'tomeg_S02'):
    lathatosag(mod); os.environ['WSG_REPORT_JSON'] = OUT + f'/validator_v2b1k11b_V3TEST_{mod}.json'
    runpy.run_path(VALID)
    log['validator'][mod] = json.load(open(OUT + f'/validator_v2b1k11b_V3TEST_{mod}.json', encoding='utf-8'))['summary']

# ---- renderek (az alapkép-beállítással azonos: a szaniterek láthatók, minden más bútor rejtve) ----
lathatosag('ures')
for o in bpy.data.collections['A902_Butor'].objects:
    o.hide_render = not o.name.startswith(MARAD)
T.alap_beallitas(sc)
for k in TOMEG: TOMEG[k][0].hide_render = True
def renderel(cam, fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cam.name, fajl=fajl, mp=round(time.time() - t, 1)))
renderel(cam02, 'A902_Cam02_alap_ellenorzes_V3TEST.png')
PONTOK = {'sarok_padlo': (3.67, 8.05, 0.0), 'sarok_plafon': (3.67, 8.05, 2.90), 'uveg_bal_also': (4.44, 8.05, 0.0),
          'uveg_bal_felso_2_53': (4.38, 8.05, 2.53), 'ML05': (5.619, 6.274, 2.90), 'ML04': (8.549, 6.274, 2.90),
          'D16': (3.67, 6.33, 0.30), 'D17': (3.67, 6.249, 0.30), 'G08': (3.67, 6.169, 0.30), 'D18': (3.67, 4.749, 0.30),
          'FL02': (3.67, 7.849, 2.85), 'D15_pillér': (4.24, 8.05, 0.30), 'W02_kapcsolooszlop': (7.149, 4.05, 1.10),
          'W01_del_vege_padlo': (3.67, 4.05, 0.0)}
for k, (col, rec) in TOMEG.items():
    col.hide_render = False; bpy.context.view_layer.update()
    renderel(cam02, f'A902_Cam02_tomeg_{k}_V3TEST_v1.png')
    log['stilus'][k] = dict(tomegek=rec, kepteri_Cam02={o.name: T.kepteri(sc, cam02, o) for o in col.objects})
    col.hide_render = True
log['pontok_Cam02'] = {p: T.vetit(sc, cam02, P) for p, P in PONTOK.items()}

# ---- felülnézeti ellenőrző képek (dokumentáció, mennyezet nélkül) ----
cd = bpy.data.cameras.new('JEL_felul_cam'); cd.type = 'ORTHO'; cd.ortho_scale = 8.4
fc = bpy.data.objects.new('JEL_felul_cam', cd); sc.collection.objects.link(fc); fc.location = (6.6, 6.2, 9.0); fc.rotation_euler = (0, 0, 0)
felso = [o for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render and min((o.matrix_world @ T.Vector(c)).z for c in o.bound_box) >= 2.80]
for o in felso: o.hide_render = True
sc.render.resolution_x, sc.render.resolution_y = 1400, 1000
for k, (col, rec) in TOMEG.items():
    col.hide_render = False; renderel(fc, f'A902_Cam02_tomeg_{k}_V3TEST_felulnezet_v1.png'); col.hide_render = True
log['felulnezet_rejtett_mennyezeti_elem'] = len(felso)

# ---- ellenőrzött távolságok (m), a tömbadatokból ----
log['tavolsagok'] = {
 'S01': {'KI3L_front_es_L_chaise_ny_vege': round(5.37 - 4.07, 2), 'KI3V_ajto_60_lendulet_x': round(3.97 + 0.60, 2),
         'KI3L_ajto_60_lendulet_x': round(4.07 + 0.60, 2), 'KI3V_es_KI3L_kozti_res': round(5.15 - 4.95, 2),
         'KI3V_es_DNy_atjaro_sik': round(4.35 - 4.05, 2), 'FL02_es_KI3P_vizszintes': round(7.849 - 7.65, 3),
         'FL02_es_KI3P_fuggoleges': round(2.85 - 2.45, 2), 'TV_tengely_y': 6.35, 'kanape_tengely_y': round((5.21 + 7.59) / 2, 3),
         'L_eszaki_vege_es_uveg': round(8.05 - 7.59, 2), 'kanape_hat_es_szek_ny_tamla': round(7.90 + 0.18 - 0.53 - 7.17, 2),
         'nezotav_TV_es_ules_kozep': round((7.17 - 0.95 / 2) - 3.77, 2)},
 'S02': {'BN3L_front_es_U_kar_vege': round(5.57 - 4.07, 2), 'BN3V_ajto_45_lendulet_x': round(3.99 + 0.45, 2),
         'BN3L_ajto_60_lendulet_x': round(4.07 + 0.60, 2), 'BN3V_es_BN3L_kozti_res': round(5.25 - 5.15, 2),
         'BN3V_es_DNy_atjaro_sik': round(4.25 - 4.05, 2), 'FL02_es_BN3P_vizszintes': round(7.849 - 7.65, 3),
         'FL02_es_BN3P_fuggoleges': round(2.85 - 2.45, 2), 'D18_a_szervizlap_mogott': '4,70 ≤ 4,749 ≤ 5,15 és z 0,30 < 0,40',
         'TV_tengely_y': 6.35, 'kanape_tengely_y': round((4.975 + 7.825) / 2, 3), 'U_eszaki_vege_es_uveg': round(8.05 - 7.825, 3),
         'U_hat_es_szek_ny_tamla': round(7.90 + 0.18 - 0.55 - 7.17, 2), 'nezotav_TV_es_ules_kozep': round((7.17 - 0.95 / 2) - 3.77, 2)}}
json.dump(log, open(os.path.join(OUT, 'tomeg_cam02_V3TEST_log_v1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', log['validator'])
