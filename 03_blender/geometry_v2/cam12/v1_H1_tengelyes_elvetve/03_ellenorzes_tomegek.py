# v2b-1-k12: validátor (üres / referencia / master bútor / S01 V3 tömb / S02 V3 tömb), Cam_12 üres alapkép, stílustömb-renderek
# Cam_02 és Cam_12 nézetből, képtéri befoglalók és távolságok a FRAME LAYOUT-hoz. Claude, 2026-10-25. NEM MENT.
import bpy, sys, os, json, time, hashlib, math, runpy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
W = os.path.dirname(os.path.abspath(__file__)) + '/'; L = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/'
sc = bpy.context.scene
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(), validator={}, kepek=[], stilus={})
MARAD = T.MARAD; MASTER = ('Agy_05_1_', 'Ejjeli_05_1_', 'Szonyeg_05_1_')
# ---- stílustömbök (külön Stil_TOMEG_* gyűjteményben, hogy a validátor bútorként lássa) ----
def blokk(col, nev, a, b, fajta, rec):
    return T.doboz(col, nev, a, b, fajta, rec)
def stilus_tomeg(kod):
    col = bpy.data.collections.new('Stil_TOMEG_' + kod); sc.collection.children.link(col); rec = {}
    if kod == 'S01':
        blokk(col, 'S01_KI3L_also_tarolo', (3.67, 5.15, 0), (4.07, 7.55, 0.48), 'tarolo', rec)          # 240×48×40
        blokk(col, 'S01_KI3V_torony', (3.67, 4.35, 0), (3.97, 4.95, 2.20), 'tarolo', rec)               # 60×220×30
        blokk(col, 'S01_KI3P_panel_a', (3.67, 5.05, 0.55), (3.69, 6.35, 2.45), 'panel', rec)            # 260×190, két sík, 15 mm eltolás
        blokk(col, 'S01_KI3P_panel_b', (3.67, 6.35, 0.55), (3.705, 7.65, 2.45), 'panel', rec)
        blokk(col, 'S01_TV_kepernyo', (3.71, 6.35 - 0.725, 0.85), (3.76, 6.35 + 0.725, 1.68), 'kepernyo', rec)
        blokk(col, 'S01_KI3A_mu_W02', (5.95, 4.05, 0.80), (6.95, 4.08, 2.60), 'mu', rec)                 # 100×180, javasolt hely
        # Lennon jobbos L 238×180×68: fő rész háttal kelet felé, y 5,21–7,59; chaise a déli végén nyugat felé (1,80)
        XB, YS, YN, D, CH, CW = 7.17, 5.21, 7.59, 0.95, 1.80, 0.95
        blokk(col, 'S01_kanape_L_fo', (XB - D, YS + CW, 0), (XB, YN, 0.42), 'kanape', rec)
        blokk(col, 'S01_kanape_L_chaise', (XB - CH, YS, 0), (XB, YS + CW, 0.42), 'kanape', rec)
        blokk(col, 'S01_kanape_L_hattamla', (XB - 0.22, YS, 0.42), (XB, YN, 0.68), 'kanape', rec)
        blokk(col, 'S01_kanape_L_kar', (XB - D, YN - 0.20, 0.42), (XB - 0.22, YN, 0.60), 'kanape', rec)
        AX0, AY0, AX1, AY1, SZ, MEL, YK = 7.90, 5.27, 8.80, 7.27, 0.55, 0.53, (5.60, 6.27, 6.94)    # Toni 200×90, 6 Eamy 55×53
    else:
        blokk(col, 'S02_BN3L_also_tarolo', (3.67, 5.25, 0), (4.07, 7.65, 0.50), 'tarolo', rec)          # 240×50×40
        blokk(col, 'S02_BN3V_kabinet', (3.67, 4.25, 0), (3.99, 5.15, 2.20), 'tarolo', rec)              # 90×220×32 (benne a tükörmező)
        blokk(col, 'S02_BN3P_panel', (3.67, 5.25, 0.55), (3.71, 7.65, 2.45), 'panel', rec)              # 240×190
        blokk(col, 'S02_TV_kepernyo', (3.71, 6.35 - 0.725, 0.85), (3.76, 6.35 + 0.725, 1.68), 'kepernyo', rec)
        blokk(col, 'S02_BN3A_grafika_W02', (5.85, 4.05, 0.85), (7.05 - 0.05, 4.07, 2.45), 'mu', rec)     # 120×160 → x 5,85–7,00 (a kapcsolóoszloptól 15 cm)
        # JÄTTEBO valódi U 285×160×71, nyitott oldal nyugat felé, y 4,975–7,825
        X1, Y0, Y1, D, AR = 7.17, 4.975, 7.825, 0.95, 1.60
        blokk(col, 'S02_kanape_U_hat', (X1 - D, Y0, 0), (X1, Y1, 0.42), 'kanape', rec)
        blokk(col, 'S02_kanape_U_del', (X1 - AR, Y0, 0), (X1 - D, Y0 + D, 0.42), 'kanape', rec)
        blokk(col, 'S02_kanape_U_eszak', (X1 - AR, Y1 - D, 0), (X1 - D, Y1, 0.42), 'kanape', rec)
        blokk(col, 'S02_kanape_U_hattamla', (X1 - 0.22, Y0, 0.42), (X1, Y1, 0.71), 'kanape', rec)
        blokk(col, 'S02_kanape_U_hattamla_d', (X1 - AR, Y0, 0.42), (X1 - 0.22, Y0 + 0.22, 0.71), 'kanape', rec)
        blokk(col, 'S02_kanape_U_hattamla_e', (X1 - AR, Y1 - 0.22, 0.42), (X1 - 0.22, Y1, 0.71), 'kanape', rec)
        AX0, AY0, AX1, AY1, SZ, MEL, YK = 7.90, 5.37, 8.80, 7.17, 0.525, 0.55, (5.67, 6.27, 6.87)   # Anouk 180×90, 6 Ciselia 52,5×55
    blokk(col, f'{kod}_etkezo_asztal_lap', (AX0, AY0, 0.72), (AX1, AY1, 0.75), 'etkezo', rec)
    blokk(col, f'{kod}_etkezo_asztal_labd', (AX0 + 0.20, AY0 + 0.25, 0), (AX1 - 0.20, AY0 + 0.33, 0.72), 'etkezo', rec)
    blokk(col, f'{kod}_etkezo_asztal_labe', (AX0 + 0.20, AY1 - 0.33, 0), (AX1 - 0.20, AY1 - 0.25, 0.72), 'etkezo', rec)
    for i, yc in enumerate(YK):
        x1 = AX0 + 0.18; x0 = x1 - MEL
        blokk(col, f'{kod}_etkezo_szekny{i}_ules', (x0, yc - SZ / 2, 0), (x1, yc + SZ / 2, 0.46), 'etkezo', rec)
        blokk(col, f'{kod}_etkezo_szekny{i}_hat', (x0, yc - SZ / 2, 0.46), (x0 + 0.06, yc + SZ / 2, 0.78), 'etkezo', rec)
        x0 = AX1 - 0.18; x1 = x0 + MEL
        blokk(col, f'{kod}_etkezo_szekk{i}_ules', (x0, yc - SZ / 2, 0), (x1, yc + SZ / 2, 0.46), 'etkezo', rec)
        blokk(col, f'{kod}_etkezo_szekk{i}_hat', (x1 - 0.06, yc - SZ / 2, 0.46), (x1, yc + SZ / 2, 0.78), 'etkezo', rec)
    col.hide_render = True
    return col, rec
TOMEG = {k: stilus_tomeg(k) for k in ('S01', 'S02')}
# ---- validátor ----
def lathatosag(mod):
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        o.hide_render = not ((mod == 'referencia' and o.name.startswith(MARAD)) or (mod == 'master_butor' and o.name.startswith(MASTER)))
    if mod.startswith('tomeg_'): TOMEG[mod[6:]][0].hide_render = False
os.environ['WSG_LOCK'] = W + 'lock_k12/geometry_lock_A902_v2b.json'; os.environ['WSG_VILLAMOS'] = L + 'A902_villamos.json'
for mod in ('ures', 'referencia', 'master_butor', 'tomeg_S01', 'tomeg_S02'):
    lathatosag(mod); os.environ['WSG_REPORT_JSON'] = OUT + f'/validator_v2b1k12_{mod}.json'
    runpy.run_path(L + 'geometry_validator_v2.py')
    log['validator'][mod] = json.load(open(OUT + f'/validator_v2b1k12_{mod}.json', encoding='utf-8'))['summary']
# ---- renderek ----
lathatosag('ures'); T.alap_beallitas(sc)
for k in TOMEG: TOMEG[k][0].hide_render = True
cam02 = bpy.data.objects['Cam_02_Nappali_terasz']; cam12 = bpy.data.objects['Cam_12_Nappali_Hero']
def renderel(cam, fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cam.name, fajl=fajl, mp=round(time.time() - t, 1)))
renderel(cam12, 'A902_Alap-v2b1k12_blender_12_nappali-hero_JAVASLAT.png')
CEL = {'ML05': (5.619, 6.274, 2.90), 'ML04': (8.549, 6.274, 2.90), 'Ajto_05_3_kozep': (10.75, 6.50, 1.05), 'W03_kapcsolok_K07_09': (10.734, 5.65, 1.10),
       'W02_kapcsolooszlop': (7.149, 4.05, 1.10), 'D18': (3.693, 4.749, 0.30), 'FL02': (3.684, 7.849, 2.85)}
for k, (col, rec) in TOMEG.items():
    col.hide_render = False; bpy.context.view_layer.update()
    for cam, nev in ((cam02, 'Cam02'), (cam12, 'Cam12')):
        renderel(cam, f'A902_{nev}_tomeg_{k}_V3_v1.png')
    log['stilus'][k] = dict(tomegek=rec,
        kepteri={nev: {o.name: T.kepteri(sc, cam, o) for o in col.objects} for cam, nev in ((cam02, 'Cam02'), (cam12, 'Cam12'))},
        pontok={nev: {p: T.vetit(sc, cam, P) for p, P in CEL.items()} for cam, nev in ((cam02, 'Cam02'), (cam12, 'Cam12'))})
    col.hide_render = True
# generikus P902_24A Cam_12-ből (dokumentáció)
gcol = bpy.data.collections.new('JEL_generikus'); sc.collection.children.link(gcol); T.generikus_P902_24A(gcol); bpy.context.view_layer.update()
renderel(cam12, 'A902_Cam12_tomeg_P902_24A_generikus_v1.png')
# ---- távolságok (m) ----
log['tavolsagok'] = {
 'S01': {'torony_KI3V_es_chaise_kozt': round(5.37 - 3.97, 2), 'also_tarolo_front_es_kanape_fo': round(6.22 - 4.07, 2), 'tarolo_ajto_60_lendulete_x': 4.07 + 0.60,
         'D18_a_torony_mogott': 'igen (y 4,749 ∈ 4,35–4,95)', 'FL02_szabad': 'igen (y 7,85 > 7,65; z 2,85 > 2,45)', 'TV_tengely_y': 6.35, 'kanape_tengely_y': 6.40,
         'kanape_eszaki_vege_es_uveg': round(8.05 - 7.59, 2), 'kanape_hat_es_szek_ny_tamla': round(7.90 + 0.18 - 0.53 - 7.17, 2)},
 'S02': {'kabinet_BN3V_es_U_del_kar': round(5.57 - 3.99, 2), 'also_tarolo_front_es_U_kar_vege': round(5.57 - 4.07, 2), 'tarolo_ajto_60_lendulete_x': 4.07 + 0.60,
         'D18_a_kabinet_mogott': 'igen (y 4,749 ∈ 4,25–5,15)', 'FL02_szabad': 'igen', 'TV_tengely_y': 6.35, 'kanape_tengely_y': 6.40,
         'U_eszaki_vege_es_uveg': round(8.05 - 7.825, 2), 'U_hat_es_szek_ny_tamla': round(7.90 + 0.18 - 0.55 - 7.17, 2)}}
json.dump(log, open(os.path.join(OUT, 'cam12_ellenorzes_log_v1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', log['validator'])
