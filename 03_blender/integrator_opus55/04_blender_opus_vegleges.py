# Integrátori Blender-ellenőrzés – Opus 5.5 V3.1 VÉGLEGES forrás (PR #22 @ 7d3c67f): S01F/S02F (a v1.2 javított promptok szerint, növény nélkül,
# az S02 végleges lámpáival) + S04, S05, S07, S08 (60 és 45 cm-es torony), S09, S10. Claude integrátor, 2026-10-25.
# MÁSOLATON fut (v2b-1-k13, sha e01170d3…), a betöltött .blend-et NEM menti. Koordinátát Opus nem adott: integrátori hozzárendelés;
# a gyártó által nem közölt belső méret „FELT” jelölésű. Kimenet: validátor stílusonként, Cam_02/Cam_12 képterület és falláthatóság, tömbképek.
import bpy, sys, os, json, time, hashlib, runpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, '03_blender', 'geometry_v2', 'cam12_C'))
import tomeg_lib as T, c_tomeg_lib as L
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('e01170d3'), SHA
T.SZIN.update(dict(lampa=0.80, noveny=0.15, asztal=0.20, tukor=0.05))
ML04, ML05 = L.ML04, (5.62, 6.27)
SZEKEK = [(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]
TV65 = ('OPUS_tv_kepernyo_65', (3.715, 6.25 - 0.725, 0.735), (3.765, 6.25 + 0.725, 1.565), 'kepernyo')

def henger(col, nev, cx, cy, r, z0, z1, fajta, rec):
    bpy.ops.mesh.primitive_cylinder_add(vertices=24, radius=r, depth=z1 - z0, location=(cx, cy, (z0 + z1) / 2)); o = bpy.context.active_object; o.name = nev
    for c in o.users_collection: c.objects.unlink(o)
    col.objects.link(o); o.data.materials.append(T.anyag('JEL_t_' + fajta, T.SZIN[fajta])); rec[nev] = [round(v, 3) for v in (cx - r, cy - r, z0, cx + r, cy + r, z1)]
def L_kanape(col, rec, XB, YS, YN, D, CH, CW, H, nev):
    U, HV = 0.42, 0.20
    T.doboz(col, nev + '_fo_ules', (XB - D, YS + CW, 0), (XB, YN, U), 'kanape', rec); T.doboz(col, nev + '_chaise', (XB - CH, YS, 0), (XB, YS + CW, U), 'kanape', rec)
    T.doboz(col, nev + '_hattamla_k', (XB - HV, YS, U), (XB, YN, H), 'kanape', rec); T.doboz(col, nev + '_kartamla_e', (XB - D, YN - 0.18, U), (XB - HV, YN, 0.60), 'kanape', rec)
def etkezo(col, rec, sz, mely, nev, veg=None):
    T.doboz(col, 'OPUS_etkezo_' + nev + '_lap', (8.00, 5.40, 0.72), (8.90, 7.00, 0.75), 'etkezo', rec)
    T.doboz(col, 'OPUS_etkezo_' + nev + '_lab', (8.25, 5.95, 0), (8.65, 6.45, 0.72), 'etkezo', rec)
    for i, p in enumerate(SZEKEK):
        s, m = (veg if (veg and i >= 4) else (sz, mely))
        L.szek(col, f'OPUS_etkezo_szek_{i}', *p, s, m, rec)
def ml(col, rec, ml04, ml05):
    (n4, r4, z40, z41), (n5, r5, z50, z51) = ml04, ml05
    henger(col, 'OPUS_ML04_' + n4, ML04[0], ML04[1], r4, z40, z41, 'lampa', rec); henger(col, 'OPUS_ML05_' + n5, ML05[0], ML05[1], r5, z50, z51, 'lampa', rec)

def epit(st):
    col = bpy.data.collections.new('Stil_OPUS_' + st); sc.collection.children.link(col); r = {}; d = lambda n, a, b, f: T.doboz(col, n, a, b, f, r)
    if st in ('S01F', 'S02F'):
        if st == 'S01F':
            T.l_kanape_del_sarok(col, 6.67, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=r, elotag='OPUS_kanape_Lennon')
            etkezo(col, r, 0.55, 0.53, 'Toni160')
            d('OPUS_tv_KI-A3_panel', (3.67, 4.05, 0), (3.71, 8.05, 2.885), 'panel'); d('OPUS_tv_KI-A2_torony', (3.71, 4.45, 0), (4.11, 5.05, 2.53), 'tarolo')
            d('OPUS_tv_KI-A1_pad', (3.71, 5.05, 0.18), (4.13, 7.65, 0.56), 'tv'); henger(col, 'OPUS_dohanyzo_FELT_O80', 4.85, 6.85, 0.40, 0, 0.35, 'asztal', r)
            ml(col, r, ('Somar_O76_FELT_z', 0.38, 1.55, 1.90), ('Misaki_O40x70', 0.20, 2.15, 2.85))
            d('OPUS_W02_mu_120x200', (5.40, 4.05, 0.45), (6.60, 4.09, 2.05), 'mu'); d('OPUS_W02_tintavonal_z210', (5.18, 4.05, 2.10), (7.00, 4.13, 2.14), 'tv')
        else:
            T.u_kanape(col, 5.00, 4.975, 6.60, 7.825, D=0.95, log=r, elotag='OPUS_kanape_JATTEBO_U'); etkezo(col, r, 0.525, 0.55, 'Toni160_fekete')
            d('OPUS_tv_BN-A1_del', (3.67, 4.05, 0), (4.12, 4.85, 2.53), 'tarolo'); d('OPUS_tv_BN-A2_eszak', (3.67, 7.35, 0), (4.07, 8.05, 2.53), 'tarolo')
            d('OPUS_tv_BN-A3_mezo', (3.67, 4.85, 0), (3.71, 7.35, 2.885), 'panel'); d('OPUS_tv_BN-A4_pad', (3.71, 5.00, 0.22), (4.11, 7.20, 0.54), 'tv')
            T.doboz(col, 'OPUS_dohanyzo_FELT_60x60', (4.60, 6.10, 0), (5.20, 6.70, 0.40), 'asztal', r)
            ml(col, r, ('Idela_O26_FELT_z', 0.13, 1.55, 1.85), ('Dancing_O65x38', 0.325, 2.15, 2.53))
            d('OPUS_W02_navy_labazat', (5.18, 4.05, 0), (7.00, 4.068, 1.10), 'tarolo'); d('OPUS_W02_mu_140x180', (5.35, 4.068, 0.65), (6.75, 4.098, 2.45), 'mu')
    elif st == 'S04':
        L_kanape(col, r, 6.67, 4.99, 7.59, 1.00, 1.76, 1.00, 0.79, 'OPUS_kanape_Lilo_FELT_belso'); etkezo(col, r, 0.55, 0.52, 'Calla160')
        d('OPUS_tv_HZ-2_panel', (3.67, 4.05, 0), (3.71, 8.05, 2.885), 'panel'); d('OPUS_tv_HZ-1_konzol', (3.71, 4.10, 0.26), (4.11, 7.90, 0.58), 'tv')
        henger(col, 'OPUS_dohanyzo_Lesley_FELT_O80', 6.67 - 1.00 - 0.47 - 0.40, 6.95, 0.40, 0, 0.40, 'asztal', r)
        ml(col, r, ('Ardali_O50_FELT_z', 0.25, 1.55, 1.85), ('korong_FELT_O60', 0.30, 2.15, 2.40))
    elif st == 'S05':
        L_kanape(col, r, 6.67, 5.21, 7.59, 0.90, 1.43, 0.90, 0.75, 'OPUS_kanape_Melva_FELT_belso'); etkezo(col, r, 0.55, 0.55, 'Archie160')
        d('OPUS_tv_MS-3_oszlopok_panel', (3.67, 4.05, 0), (3.71, 8.05, 2.885), 'panel'); d('OPUS_tv_MS-1_konzol', (3.71, 4.75, 0), (4.12, 7.75, 0.45), 'tv')
        d('OPUS_tv_MS-2_portal', (3.71, 6.25 - 1.15, 0.45), (3.764, 6.25 + 1.15, 2.45), 'panel'); henger(col, 'OPUS_dohanyzo_Antigua_O78', 6.67 - 0.90 - 0.47 - 0.39, 6.85, 0.39, 0, 0.45, 'asztal', r)
        ml(col, r, ('Novae_O40_FELT_z', 0.20, 1.55, 1.85), ('Brisia_O50', 0.25, 2.15, 2.65))
        d('OPUS_W02_tukor_O90_FELT_hely', (6.30, 4.05, 1.00), (7.20, 4.08, 1.90), 'tukor')
    elif st == 'S07':
        L_kanape(col, r, 6.67, 5.03, 7.59, 0.95, 1.18, 0.95, 0.65, 'OPUS_kanape_Wolke_FELT_belso'); etkezo(col, r, 0.56, 0.51, 'Toni160')
        d('OPUS_tv_LF-1_karpitpanel', (3.67, 4.05, 0), (3.71, 8.05, 2.885), 'panel'); d('OPUS_tv_LF-2_konzol', (3.71, 4.85, 0.15), (4.16, 7.65, 0.60), 'tv')
        henger(col, 'OPUS_dohanyzo_Sheffield_O80', 6.67 - 0.95 - 0.47 - 0.40, 6.85, 0.40, 0, 0.40, 'asztal', r)
        ml(col, r, ('Brisia_O50', 0.25, 1.45, 1.95), ('FELT_O60', 0.30, 2.15, 2.45))
    elif st in ('S08', 'S08_45'):
        T.l_kanape_del_sarok(col, 6.67, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=r, elotag='OPUS_kanape_Lennon'); etkezo(col, r, 0.56, 0.51, 'Luca160')
        m = 0.60 if st == 'S08' else 0.45
        d('OPUS_tv_MR-5_panel', (3.67, 4.05, 0), (3.71, 8.05, 2.885), 'panel'); d('OPUS_tv_MR-1_torony', (3.71, 4.45, 0), (3.71 + m, 5.05, 2.53), 'tarolo')
        d('OPUS_tv_MR-3_also_testek', (3.71, 5.05, 0), (4.11, 7.45, 0.45), 'tv')
        d('OPUS_tv_MR-2_sarga_doboz_TV_tol_delre', (3.71, 5.525 - 0.05 - 1.20, 1.30), (4.11, 5.525 - 0.05, 1.70), 'tarolo')
        d('OPUS_tv_MR-4_dio_kocka', (3.71, 7.30, 0.90), (4.01, 7.90, 1.50), 'tarolo')
        T.doboz(col, 'OPUS_dohanyzo_Naruto_140x80', (6.67 - 0.95 - 0.47 - 0.80, 6.30, 0), (6.67 - 0.95 - 0.47, 7.70, 0.38), 'asztal', r)
        ml(col, r, ('Idela_O26_FELT_z', 0.13, 1.55, 1.85), ('Misaki_O40x70', 0.20, 2.15, 2.85))
    elif st == 'S09':
        T.l_kanape_del_sarok(col, 6.67, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=r, elotag='OPUS_kanape_Lennon'); etkezo(col, r, 0.55, 0.52, 'Luca160', veg=(0.66, 0.60))
        d('OPUS_tv_PC-1_konyvtar_del', (3.67, 4.05, 0), (4.02, 4.85, 2.53), 'tarolo'); d('OPUS_tv_PC-2_konyvtar_eszak', (3.67, 7.25, 0), (4.02, 8.05, 2.53), 'tarolo')
        d('OPUS_tv_PC-4_also_szekreny', (3.67, 4.85, 0), (4.07, 7.25, 0.50), 'tv'); d('OPUS_tv_felso_panel', (3.67, 4.05, 2.53), (3.71, 8.05, 2.885), 'panel')
        henger(col, 'OPUS_dohanyzo_Orlia_FELT_O55', 6.67 - 0.95 - 0.47 - 0.28, 6.90, 0.28, 0, 0.45, 'asztal', r)
        ml(col, r, ('Ardali_O50_FELT_z', 0.25, 1.55, 1.85), ('FELT_O60', 0.30, 2.15, 2.45))
    elif st == 'S10':
        T.u_kanape(col, 5.00, 4.975, 6.60, 7.825, D=0.95, log=r, elotag='OPUS_kanape_JATTEBO_U'); etkezo(col, r, 0.46, 0.56, 'Kesia160')
        d('OPUS_tv_DM-1_also_lepcso', (3.67, 4.05, 0), (4.12, 8.05, 0.30), 'tv'); d('OPUS_tv_DM-2_okker_lepcso', (3.67, 4.05, 0.30), (4.07, 5.35, 0.90), 'tarolo')
        d('OPUS_tv_DM-3_kakao_lepcso', (3.67, 4.05, 0.90), (4.07, 4.75, 2.50), 'tarolo'); d('OPUS_tv_DM-4_napkorong_O100', (3.67, 7.00, 1.05), (3.71, 8.00, 2.05), 'panel')
        T.doboz(col, 'OPUS_dohanyzo_Adularia_85x85', (4.35, 5.975, 0), (5.20, 6.825, 0.40), 'asztal', r)
        ml(col, r, ('Drava_FELT_O25', 0.125, 1.55, 1.85), ('Styrka_O75x75', 0.375, 2.15, 2.90))
    T.doboz(col, *TV65, r)
    return col, r

STILUSOK = ('S01F', 'S02F', 'S04', 'S05', 'S07', 'S08', 'S08_45', 'S09', 'S10')
EL = {st: epit(st) for st in STILUSOK}
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=SHA, forras='Opus PR #22 @ 7d3c67f + integrátori v1.2', tomeg={st: EL[st][1] for st in EL},
           validator={}, kepterulet={}, lathatosag={}, vetites={}, kepek=[])
os.environ['WSG_LOCK'] = os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json')
os.environ['WSG_VILLAMOS'] = os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.json')
for o in bpy.data.collections['A902_Butor'].objects: o.hide_render = True
for c in bpy.data.collections:
    if c.name.startswith('Stil_') and not c.name.startswith('Stil_OPUS_'): c.hide_render = True
for st in STILUSOK:
    for s2 in STILUSOK: EL[s2][0].hide_render = (s2 != st)
    os.environ['WSG_REPORT_JSON'] = os.path.join(OUT, f'validator_integrator_k13_vegleges_{st}.json'); runpy.run_path(os.path.join(REPO, '03_blender', 'geometry_validator_v2.py'))
    d = json.load(open(os.environ['WSG_REPORT_JSON'], encoding='utf-8')); log['validator'][st] = dict(summary=d['summary'], errors=d['errors'],
        warnings_nem_villamos_pont=[w for w in d['warnings'] if not w.startswith('VILLAMOS')], villamos_figyelmeztetes_db=sum(1 for w in d['warnings'] if w.startswith('VILLAMOS')))

c02 = bpy.data.objects['Cam_02_Nappali_terasz']; c12 = bpy.data.objects['Cam_12_Nappali_Hero']
K = L.konyha(sc)
def lc_keres(lc, nev):
    if lc.collection.name == nev: return lc
    for ch in lc.children:
        x = lc_keres(ch, nev)
        if x: return x
def kizar(f, e):
    for c in bpy.data.collections:
        if f(c.name):
            lc = lc_keres(vl.layer_collection, c.name)
            if lc: lc.exclude = e
    vl.update()
NEM_EPIT = lambda n: n.startswith(('Stil_', 'VK_', 'A902_Butor', 'A902_Villamos', 'KONYHA_'))
def osztaly(ob, p):
    n = ob.name
    for pre, k in (('OPUS_kanape', 'kanape'), ('OPUS_etkezo', 'etkezo'), ('OPUS_ML04', 'ML04_lampa'), ('OPUS_ML05', 'ML05_lampa'), ('OPUS_tv_kepernyo', 'TV_kepernyo'),
                   ('OPUS_tv', 'TV_fal'), ('OPUS_W02', 'W02_elem'), ('OPUS_dohanyzo', 'dohanyzoasztal'), ('KONYHA_', 'konyha_butor')):
        if n.startswith(pre): return k
    x, y, z = p
    if z < 0.02: return 'padlo'
    if z > 2.87: return 'mennyezet'
    if y > 8.12: return 'uveg_terasz_kilatas'
    if abs(y - 4.05) < 0.04 and 5.18 <= x <= 7.32: return 'W02'
    if (abs(x - 5.20) < 0.04 and 2.70 <= y <= 3.97) or (abs(y - 2.75) < 0.04 and 3.70 <= x <= 5.22): return 'W07'
    if abs(x - 10.75) < 0.04 and 5.0 <= y <= 7.05: return 'W03_05_3'
    if abs(x - 3.67) < 0.04: return 'W01'
    return 'egyeb_epitett'
def kepterulet(cam, deps, NU=160, NV=100):
    tr, br, bl, tl = [cam.matrix_world @ v for v in cam.data.view_frame(scene=sc)]; O = cam.matrix_world.translation.copy(); cnt = {}
    for j in range(NV):
        vv = (j + 0.5) / NV; a = tl.lerp(bl, vv); b = tr.lerp(br, vv)
        for i in range(NU):
            P = a.lerp(b, (i + 0.5) / NU); hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, (P - O).normalized(), distance=60.0)
            k = osztaly(ob, loc) if hit else 'kint'; cnt[k] = cnt.get(k, 0) + 1
    return {k: round(v / (NU * NV), 4) for k, v in sorted(cnt.items(), key=lambda t: -t[1]) if v / (NU * NV) >= 0.004}
FAL = {'W01': [Vector((3.80, 4.15 + 0.1 * i, z)) for i in range(38) for z in (0.3, 0.7, 1.1, 1.5, 1.9, 2.3, 2.7)],
       'W02': [Vector((5.25 + 0.1 * i, 4.11, z)) for i in range(21) for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)]}
def lathato(cam, deps, P, tol=0.12):
    p = world_to_camera_view(sc, cam, P)
    if p.z <= 0 or not (0 <= p.x <= 1 and 0 <= p.y <= 1): return None
    O = cam.matrix_world.translation.copy(); dv = P - O; Ln = dv.length; dv.normalize()
    hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, dv, distance=Ln + 0.05)
    return (not hit) or (loc - P).length <= tol or ob.name.startswith(('OPUS_tv', 'OPUS_W02'))
def vetit(cam, rec, pre):
    pts = [world_to_camera_view(sc, cam, Vector((x, y, z))) for k, b in rec.items() if k.startswith(pre) for x in (b[0], b[3]) for y in (b[1], b[4]) for z in (b[2], b[5])]
    pts = [p for p in pts if p.z > 0]
    return None if not pts else [round(min(p.x for p in pts), 3), round(max(p.x for p in pts), 3)]
for st in STILUSOK:
    kizar(NEM_EPIT, True); kizar(lambda n: n in ('Stil_OPUS_' + st, 'KONYHA_TOMEG'), False); deps = bpy.context.evaluated_depsgraph_get()
    for nev, c in (('Cam_02', c02), ('Cam_12_v3', c12)):
        log['kepterulet'][f'{nev}|{st}'] = kepterulet(c, deps)
        lt = {}
        for fn, P in FAL.items():
            res = [lathato(c, deps, q) for q in P]; bent = [x for x in res if x is not None]
            lt[fn] = None if not bent else dict(kepben=round(len(bent) / len(P), 3), takaratlan=round(sum(1 for x in bent if x) / len(bent), 3))
        log['lathatosag'][f'{nev}|{st}'] = lt
        log['vetites'][f'{nev}|{st}'] = {'ML04_x': vetit(c, EL[st][1], 'OPUS_ML04'), 'ML05_x': vetit(c, EL[st][1], 'OPUS_ML05')}
    allo = (4.30, 7.75, 4.50, 8.05)
    log.setdefault('cam12_allohely', {})[st] = [k for k, b in EL[st][1].items() if b[0] < allo[2] and b[3] > allo[0] and b[1] < allo[3] and b[4] > allo[1] and b[2] < 1.9]
kizar(lambda n: True, False)
T.alap_beallitas(sc); sc.render.resolution_percentage = 50
for st in STILUSOK:
    for s2 in STILUSOK: EL[s2][0].hide_render = (s2 != st)
    K[0].hide_render = False; vl.update()
    for nev, c in (('Cam02', c02), ('Cam12v3', c12)):
        f = f'A902_OPUS55_7d3c67f_{st}_{nev}_tomeg.png'; sc.camera = c; sc.render.filepath = os.path.join(OUT, f); t = time.time()
        bpy.ops.render.render(write_still=True); log['kepek'].append(dict(stilus=st, kamera=c.name, fajl=f, mp=round(time.time() - t, 1)))
json.dump(log, open(os.path.join(OUT, '04_blender_opus_vegleges_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', json.dumps({k: v['summary'] for k, v in log['validator'].items()}, ensure_ascii=False))
