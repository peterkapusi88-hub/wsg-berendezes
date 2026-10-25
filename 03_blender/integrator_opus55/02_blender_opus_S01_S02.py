# Integrátori Blender-méretpróba – Opus 5.5 V3.1 (PR #22) S01 Kyoto Ink / S02 BiBo Nocturne, Cam_02 + Cam_12 v3.
# Claude integrátor, 2026-10-25. Egy MÁSOLATON fut (v2b-1-k13, sha e01170d3…), a betöltött .blend-et NEM menti.
# Tömbök: az Opus-ág b24bee7 S01/S02 specifikációja, 30_TV_FAL_KONCEPCIOK (KI-A, BN-A) és a négy kiemelt prompt; ahol Opus nem
# adott méretet/koordinátát, az integrátori feltételezés a tömb nevében „FELT” jelöléssel szerepel.
# Kimenet: validátor (üres / referencia = Cam_10 régi szaniterhibák / OPUS_S01 / OPUS_S02), képterület- és falláthatóság Cam_02 és
# Cam_12 v3 nézetben, tömbképek (EEVEE, 50 %).
import bpy, sys, os, json, time, hashlib, runpy, math
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, os.path.join(REPO, '03_blender', 'geometry_v2', 'cam12_C'))
import tomeg_lib as T, c_tomeg_lib as L
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
RENDER = '--nincs-render' not in sys.argv
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('e01170d3'), SHA
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=SHA, validator={}, kepterulet={}, lathatosag={}, vetites={}, kepek=[], tomeg={})
T.SZIN.update(dict(lampa=0.80, noveny=0.15, szonyeg=0.55, tukor=0.05, asztal=0.20))

def gyujt(nev):
    c = bpy.data.collections.new(nev); sc.collection.children.link(c); return c
def henger(col, nev, cx, cy, r, z0, z1, fajta, rec, seg=24):
    bpy.ops.mesh.primitive_cylinder_add(vertices=seg, radius=r, depth=z1 - z0, location=(cx, cy, (z0 + z1) / 2))
    o = bpy.context.active_object; o.name = nev
    for c in o.users_collection: c.objects.unlink(o)
    col.objects.link(o); o.data.materials.append(T.anyag('JEL_t_' + fajta, T.SZIN[fajta])); rec[nev] = [round(v, 3) for v in (cx - r, cy - r, z0, cx + r, cy + r, z1)]
    return o
def gomb(col, nev, cx, cy, r, zc, fajta, rec):
    bpy.ops.mesh.primitive_uv_sphere_add(radius=r, location=(cx, cy, zc)); o = bpy.context.active_object; o.name = nev
    for c in o.users_collection: c.objects.unlink(o)
    col.objects.link(o); o.data.materials.append(T.anyag('JEL_t_' + fajta, T.SZIN[fajta])); rec[nev] = [round(v, 3) for v in (cx - r, cy - r, zc - r, cx + r, cy + r, zc + r)]
ML04, ML05 = L.ML04, (5.62, 6.27)
SZEKEK = [(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]

def opus_S01():
    col = gyujt('Stil_OPUS_S01'); r = {}
    T.l_kanape_del_sarok(col, 6.67, 5.21, 7.59, 0.95, 1.80, 0.95, H=0.68, log=r, elotag='OPUS_kanape_Lennon')
    T.doboz(col, 'OPUS_etkezo_Toni160_lap', (8.00, 5.40, 0.72), (8.90, 7.00, 0.75), 'etkezo', r)
    T.doboz(col, 'OPUS_etkezo_Toni160_lab', (8.25, 5.95, 0), (8.65, 6.45, 0.72), 'etkezo', r)
    for i, (cx, cy, nx, ny) in enumerate(SZEKEK): L.szek(col, f'OPUS_etkezo_szek_Eamy_{i}', cx, cy, nx, ny, 0.55, 0.53, r)
    T.doboz(col, 'OPUS_tv_KI-A3_washi_panel', (3.67, 4.05, 0), (3.71, 8.05, 2.885), 'panel', r)
    T.doboz(col, 'OPUS_tv_KI-A2_torony', (3.71, 4.45, 0), (4.11, 5.05, 2.53), 'tarolo', r)
    T.doboz(col, 'OPUS_tv_KI-A1_uszo_pad', (3.71, 5.05, 0.18), (4.13, 7.65, 0.56), 'tv', r)
    T.doboz(col, 'OPUS_tv_kepernyo_65', (3.71, 6.25 - 0.725, 0.735), (3.76, 6.25 + 0.725, 1.565), 'kepernyo', r)
    henger(col, 'OPUS_dohanyzoasztal_FELT_O80', 4.85, 6.85, 0.40, 0.0, 0.35, 'asztal', r)
    T.doboz(col, 'OPUS_szonyeg_Nifelia_200x300_FELT_hely', (4.30, 5.05, 0), (6.30, 8.00 - 0.05, 0.012), 'szonyeg', r)
    henger(col, 'OPUS_ML05_lampa_Misaki_O40x70', ML05[0], ML05[1], 0.20, 2.15, 2.85, 'lampa', r)
    henger(col, 'OPUS_ML04_lampa_Somar_O76_FELT_magassag', ML04[0], ML04[1], 0.38, 1.55, 1.90, 'lampa', r)
    T.doboz(col, 'OPUS_ML04_kabel', (ML04[0] - .005, ML04[1] - .005, 1.90), (ML04[0] + .005, ML04[1] + .005, 2.90), 'tv', r)
    T.doboz(col, 'OPUS_W02_mu_tusvonas_120x200', (5.40, 4.05, 0.45), (6.60, 4.09, 2.45), 'mu', r)
    T.doboz(col, 'OPUS_W02_tintavonal_sin_z210', (5.18, 4.05, 2.10), (7.00, 4.13, 2.14), 'tv', r)
    henger(col, 'OPUS_noveny_W02_DNy_sarok_FELT_O45', 5.45, 4.285, 0.225, 0.0, 1.80, 'noveny', r)
    return col, r

def opus_S02():
    col = gyujt('Stil_OPUS_S02'); r = {}
    T.u_kanape(col, 5.00, 4.975, 6.60, 7.825, D=0.95, log=r, elotag='OPUS_kanape_JATTEBO_U')
    T.doboz(col, 'OPUS_etkezo_Toni160_fekete_lap', (8.00, 5.40, 0.72), (8.90, 7.00, 0.75), 'etkezo', r)
    T.doboz(col, 'OPUS_etkezo_Toni160_fekete_lab', (8.25, 5.95, 0), (8.65, 6.45, 0.72), 'etkezo', r)
    for i, (cx, cy, nx, ny) in enumerate(SZEKEK): L.szek(col, f'OPUS_etkezo_szek_Ciselia_{i}', cx, cy, nx, ny, 0.525, 0.55, r)
    T.doboz(col, 'OPUS_tv_BN-A1_deli_kabinet', (3.67, 4.05, 0), (4.12, 4.85, 2.53), 'tarolo', r)
    T.doboz(col, 'OPUS_tv_BN-A2_eszaki_kabinet', (3.67, 7.35, 0), (4.07, 8.05, 2.53), 'tarolo', r)
    T.doboz(col, 'OPUS_tv_BN-A3_ezust_mezo', (3.67, 4.85, 0), (3.71, 7.35, 2.885), 'panel', r)
    T.doboz(col, 'OPUS_tv_BN-A3_ezust_kabinetek_felett', (3.67, 4.05, 2.53), (3.71, 8.05, 2.885), 'panel', r)
    T.doboz(col, 'OPUS_tv_BN-A4_uszo_pad', (3.71, 5.00, 0.22), (4.11, 7.20, 0.54), 'tv', r)
    T.doboz(col, 'OPUS_tv_BN-A5_tukorres_del', (3.71, 4.85, 0.54), (3.714, 5.00, 2.53), 'tukor', r)
    T.doboz(col, 'OPUS_tv_BN-A5_tukorres_eszak', (3.71, 7.20, 0.54), (3.714, 7.35, 2.53), 'tukor', r)
    T.doboz(col, 'OPUS_tv_kepernyo_65', (3.71, 6.25 - 0.725, 0.735), (3.76, 6.25 + 0.725, 1.565), 'kepernyo', r)
    T.doboz(col, 'OPUS_dohanyzoasztal_FELT_60x60', (4.60, 6.10, 0), (5.20, 6.70, 0.40), 'asztal', r)
    T.doboz(col, 'OPUS_szonyeg_Marely_200x300_FELT_hely', (4.30, 4.95, 0), (6.30, 7.95, 0.012), 'szonyeg', r)
    henger(col, 'OPUS_ML05_lampa_sargarez_opal_FELT_O60', ML05[0], ML05[1], 0.30, 2.15, 2.70, 'lampa', r)
    gomb(col, 'OPUS_ML04_lampa_Brisia_O50_FELT_magassag', ML04[0], ML04[1], 0.25, 1.70, 'lampa', r)
    T.doboz(col, 'OPUS_ML04_kabel', (ML04[0] - .005, ML04[1] - .005, 1.95), (ML04[0] + .005, ML04[1] + .005, 2.90), 'tv', r)
    T.doboz(col, 'OPUS_W02_navy_labazat_18mm', (5.18, 4.05, 0), (7.00, 4.068, 1.10), 'tarolo', r)
    T.doboz(col, 'OPUS_W02_mu_140x180', (5.35, 4.068, 0.65), (6.75, 4.098, 2.45), 'mu', r)
    henger(col, 'OPUS_noveny_olajfa_W02_sarok_FELT_O45', 5.45, 4.285, 0.225, 0.0, 2.00, 'noveny', r)
    return col, r

K = L.konyha(sc); EL = {'S01': opus_S01(), 'S02': opus_S02()}
log['tomeg'] = {st: EL[st][1] for st in EL}; log['konyha'] = K[1]
MARAD = T.MARAD
def lathatosag(mod):
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        o.hide_render = not (mod == 'referencia' and o.name.startswith(MARAD))
    if mod.startswith('OPUS_'): EL[mod[5:]][0].hide_render = False
os.environ['WSG_LOCK'] = os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json')
os.environ['WSG_VILLAMOS'] = os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.json')
for mod in ('ures', 'referencia', 'OPUS_S01', 'OPUS_S02'):
    lathatosag(mod); os.environ['WSG_REPORT_JSON'] = os.path.join(OUT, f'validator_integrator_k13_{mod}.json')
    runpy.run_path(os.path.join(REPO, '03_blender', 'geometry_validator_v2.py'))
    log['validator'][mod] = json.load(open(os.environ['WSG_REPORT_JSON'], encoding='utf-8'))['summary']
lathatosag('ures')

# ---- képterület és falláthatóság (sugárvetés), csak építészet + az adott stílus tömbjei + generikus konyha
c02 = bpy.data.objects['Cam_02_Nappali_terasz']; c12 = bpy.data.objects['Cam_12_Nappali_Hero']
def lc_keres(lc, nev):
    if lc.collection.name == nev: return lc
    for ch in lc.children:
        r = lc_keres(ch, nev)
        if r: return r
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
                   ('OPUS_tv', 'TV_fal_butor_panel'), ('OPUS_noveny', 'noveny'), ('OPUS_W02_mu', 'W02_mu'), ('OPUS_W02', 'W02_sav'), ('OPUS_dohanyzo', 'dohanyzoasztal'),
                   ('OPUS_szonyeg', 'szonyeg'), ('KONYHA_', 'konyha_butor')):
        if n.startswith(pre): return k
    x, y, z = p
    if z < 0.02: return 'padlo'
    if z > 2.87: return 'mennyezet'
    if y > 8.12: return 'uveg_terasz_kilatas'
    if abs(y - 4.05) < 0.04 and 5.18 <= x <= 7.32: return 'W02'
    if (abs(x - 5.20) < 0.04 and 2.70 <= y <= 3.97) or (abs(y - 2.75) < 0.04 and 3.70 <= x <= 5.22): return 'W07'
    if abs(x - 10.75) < 0.04 and 5.0 <= y <= 7.05: return 'W03_05_3'
    if abs(x - 3.67) < 0.04: return 'W01_TV_fal'
    return 'egyeb_epitett'
NU, NV = 160, 100
def kepterulet(cam, deps):
    fr = [cam.matrix_world @ v for v in cam.data.view_frame(scene=sc)]; tr, br, bl, tl = fr; O = cam.matrix_world.translation.copy(); cnt = {}
    for j in range(NV):
        vv = (j + 0.5) / NV; left = tl.lerp(bl, vv); right = tr.lerp(br, vv)
        for i in range(NU):
            P = left.lerp(right, (i + 0.5) / NU); d = (P - O).normalized()
            hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, d, distance=60.0)
            k = osztaly(ob, loc) if hit else 'kint'; cnt[k] = cnt.get(k, 0) + 1
    return {k: round(v / (NU * NV), 4) for k, v in sorted(cnt.items(), key=lambda t: -t[1])}
FAL_MINTA = {
 'W01_TV_fal': [('x', 3.765, a, z) for a in [4.15 + 0.1 * i for i in range(38)] for z in (0.3, 0.7, 1.1, 1.5, 1.9, 2.3, 2.7)],
 'W02': [('y', 4.10, a, z) for a in [5.25 + 0.1 * i for i in range(21)] for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)],
 'W07': [('x', 5.198, a, z) for a in [3.47 + 0.05 * i for i in range(10)] for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)] +
        [('y', 2.752, a, z) for a in [4.55 + 0.05 * i for i in range(10)] for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)],
 'W03_05_3_ajto': [('x', 10.778, a, z) for a in [6.12 + 0.08 * i for i in range(10)] for z in (0.3, 0.8, 1.3, 1.8)],
 'etkezo_asztallap': [('z', 0.752, (x, y)) for x in (8.1, 8.3, 8.5, 8.7, 8.85) for y in (5.5, 5.8, 6.1, 6.4, 6.7, 6.95)],
 'konyha_magas_elemek_eleje': [('y', 1.952, a, z) for a in [9.10 + 0.08 * i for i in range(11)] for z in (0.3, 0.8, 1.3, 1.8)] +
        [('x', 9.948, a, z) for a in [4.70 + 0.05 * i for i in range(11)] for z in (0.3, 0.8, 1.3, 1.8, 2.1)],
 'terasz_uveg_kilatas': [('y', 8.06, a, z) for a in [4.6 + 0.2 * i for i in range(22)] for z in (0.4, 0.9, 1.4, 1.9, 2.4)],
}
def pont(m):
    if m[0] == 'z': return Vector((m[2][0], m[2][1], m[1]))
    ax, s, a, z = m; return Vector((s, a, z)) if ax == 'x' else Vector((a, s, z))
def lathato(cam, deps, P, tol=0.05):
    p = world_to_camera_view(sc, cam, P)
    if p.z <= 0 or not (0 <= p.x <= 1 and 0 <= p.y <= 1): return None
    O = cam.matrix_world.translation.copy(); d = P - O; Ln = d.length; d.normalize()
    hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, d, distance=Ln + 0.05)
    return (not hit) or (loc - P).length <= tol
def bbox_kep(cam, rec):
    pts = []
    for b in rec:
        for x in (b[0], b[3]):
            for y in (b[1], b[4]):
                for z in (b[2], b[5]):
                    p = world_to_camera_view(sc, cam, Vector((x, y, z)))
                    if p.z > 0: pts.append(p)
    if not pts: return None
    return dict(x0=round(min(p.x for p in pts), 3), x1=round(max(p.x for p in pts), 3), y_alul=round(min(p.y for p in pts), 3), y_felul=round(max(p.y for p in pts), 3))
for st in ('S01', 'S02'):
    kizar(NEM_EPIT, True); kizar(lambda n: n in ('Stil_OPUS_' + st, 'KONYHA_TOMEG'), False)
    deps = bpy.context.evaluated_depsgraph_get(); rec = EL[st][1]
    for nev, c in (('Cam_02', c02), ('Cam_12_v3', c12)):
        log['kepterulet'][f'{nev}|{st}'] = kepterulet(c, deps)
        lt = {}
        for fn, ms in FAL_MINTA.items():
            res = [lathato(c, deps, pont(m)) for m in ms]; bent = [x for x in res if x is not None]
            lt[fn] = dict(minta=len(ms), kepben=len(bent), takaratlan=sum(1 for x in bent if x), arany_kepben=round(len(bent) / len(ms), 3),
                          takaratlan_a_kepbenibol=round(sum(1 for x in bent if x) / len(bent), 3) if bent else None)
        log['lathatosag'][f'{nev}|{st}'] = lt
        grp = {}
        for k, b in rec.items():
            for pre in ('OPUS_etkezo', 'OPUS_kanape', 'OPUS_ML04_lampa', 'OPUS_ML05', 'OPUS_tv', 'OPUS_noveny', 'OPUS_W02_mu', 'OPUS_dohanyzo'):
                if k.startswith(pre): grp.setdefault(pre, []).append(b)
        log['vetites'][f'{nev}|{st}'] = {k: bbox_kep(c, v) for k, v in grp.items()}
    # Cam_12 állóhely (x 4,30–4,50; y 7,75–8,05) szabad-e
    allo = (4.30, 7.75, 4.50, 8.05)
    log.setdefault('cam12_allohely_utkozes', {})[st] = [k for k, b in rec.items() if b[0] < allo[2] and b[3] > allo[0] and b[1] < allo[3] and b[4] > allo[1] and b[2] < 1.9]
kizar(lambda n: True, False)

# ---- tömbképek
if RENDER:
    T.alap_beallitas(sc); sc.render.resolution_percentage = 50
    for st in ('S01', 'S02'):
        for c, _ in EL.values(): c.hide_render = True
        EL[st][0].hide_render = False; K[0].hide_render = False; vl.update()
        for nev, c in (('Cam02', c02), ('Cam12v3', c12)):
            f = f'A902_OPUS55_{st}_{nev}_tomeg_integrator.png'; sc.camera = c; sc.render.filepath = os.path.join(OUT, f)
            t = time.time(); bpy.ops.render.render(write_still=True); log['kepek'].append(dict(kamera=c.name, stilus=st, fajl=f, mp=round(time.time() - t, 1)))
json.dump(log, open(os.path.join(OUT, '02_blender_opus_S01_S02_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', json.dumps(log['validator'], ensure_ascii=False))
