# Cam_12 nappali HERO v2 – sarokközeli kamerajelöltek (Péter 2026-10-25 01:58 és 02:06): ÉNy-i sarok (TV-fal + teraszüveg) fő jelölt,
# DNy-i sarok összevetés. Alap: v2b-1-k11b (main, sha 9875cd57). Üres + S01/S02 V3 tömb renderek, célpont-vetítés, falszakasz-láthatóság
# (ray cast, csak építészet / + stílustömb). Függőlegesek egyenesek (vízszintes kamera, shift_y). Claude, 2026-10-25. NEM MENT.
import bpy, sys, os, json, time, hashlib, math
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T, stilus_tomeg_v3 as SV
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('9875cd57')
T.alap_beallitas(sc)
TOMEG = {k: SV.stilus_tomeg(k, sc, T) for k in ('S01', 'S02')}
jcol = bpy.data.collections.new('JEL_cam12v2'); sc.collection.children.link(jcol)
def rot(theta, tilt=0.0):  # theta: nézési irány az +x tengelytől, fok (kelet 0, észak +90); tilt: lefelé dőlés, fok
    return (math.radians(90.0 - tilt), 0.0, math.radians(theta - 90.0))
JEL = {
 'K1_ENy_sarok_20':   dict(loc=(3.95, 7.90, 1.45), theta=-47.0, lens=20.0, shift_y=-0.05),
 'K2_ENy_bentebb_20': dict(loc=(4.50, 7.65, 1.45), theta=-52.0, lens=20.0, shift_y=-0.05),
 'K3_DNy_sarok_20':   dict(loc=(4.25, 4.35, 1.45), theta=30.0, lens=20.0, shift_y=-0.05),
 'K1_ENy_sarok_22':   dict(loc=(3.95, 7.90, 1.45), theta=-47.0, lens=22.0, shift_y=-0.05),
 'K1_ENy_sarok_24':   dict(loc=(3.95, 7.90, 1.45), theta=-45.0, lens=24.0, shift_y=-0.05),
}
cams = {}
for k, p in JEL.items():
    c = T.kamera('JEL_' + k, p['loc'], rot(p['theta']), lens=p['lens'], col=jcol); c.data.shift_y = p['shift_y']; cams[k] = c
REF = {'Cam_03_referencia': bpy.data.objects['Cam_03_Etkezo_konyha'], 'Cam_02_kontroll': bpy.data.objects['Cam_02_Nappali_terasz']}
vl.update()
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=SHA, jeloltek={}, tomegek={k: v[1] for k, v in TOMEG.items()})
def renderel(cam, fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True); return round(time.time() - t, 1)
# ---- 1) renderek: üres, S01, S02 ----
for k, c in cams.items():
    j = log['jeloltek'].setdefault(k, {}); j.update(JEL[k]); j['loc'] = list(JEL[k]['loc']); j['rot'] = [round(v, 4) for v in c.rotation_euler]
    j['ures_mp'] = renderel(c, f'cam12v2_{k}_ures.png')
    for kod, (col, rec) in TOMEG.items():
        col.hide_render = False; vl.update(); j[f'{kod}_mp'] = renderel(c, f'cam12v2_{k}_tomeg_{kod}.png'); col.hide_render = True
# ---- 2) célpontok vetítése + takarás (ray cast) ----
CEL = {
 'kanape_S01_ules_eleje': (6.22, 6.90, 0.42), 'kanape_S02_U_belseje': (6.40, 6.40, 0.42), 'etkezo_asztal_kozep': (8.35, 6.27, 0.75),
 'ajto_05_3_kozep': (10.778, 6.50, 1.05), 'W03_kapcsolok_K07_09_D12': (10.748, 5.65, 1.10), 'W03_huto_dugalj_D13': (10.748, 5.199, 0.30),
 'akna_nyugati_lap_kozep': (9.798, 7.54, 1.45), 'konyha_csonk_kozep': (10.548, 4.58, 1.45), 'konyha_keleti_fal_kozep': (10.548, 2.70, 1.45),
 'konyha_deli_fal_kozep': (9.80, 1.352, 1.45), 'atjaro_kozep': (7.83, 4.05, 1.05), 'bejarati_ajto': (7.83, 0.86, 1.05),
 'W02_kozep': (6.25, 4.052, 1.45), 'W02_kapcsolooszlop_K10_12_T01_D19': (7.149, 4.052, 1.10), 'kozlekedo_torok_kozep': (4.43, 4.00, 1.05),
 'kozlekedo_keleti_fal': (5.198, 3.70, 1.45), 'kozlekedo_kapcsolok_K25_27_D46': (5.182, 3.90, 1.10), 'furdo_06_1_ajto': (4.20, 2.722, 1.05),
 'ajto_05_2': (3.12, 2.722, 1.05), 'uvegfal_kozep': (6.70, 8.248, 1.25), 'TV_kozep': (3.712, 6.35, 1.26), 'FL02': (3.672, 7.849, 2.85),
 'ML04': (8.549, 6.274, 2.898), 'ML05': (5.619, 6.274, 2.898)}
FALAK = [  # név, tengely, sík (mintapont a szoba felőli oldalon), tartomány a falon, z_max
 ('W03 keleti fal x10,75 y5,05–6,05 (K07–K09+D12, D13)', 'x', 10.748, (5.05, 6.05), 2.90),
 ('W03 05.3 ajtó y6,08–6,92', 'x', 10.778, (6.08, 6.92), 2.08),
 ('W03 ajtó fölötti szemöldök y6,05–6,95', 'x', 10.748, (6.05, 6.95), 2.90),
 ('W03 csík y6,95–7,025', 'x', 10.748, (6.95, 7.025), 2.90),
 ('Akna nyugati lap x9,80 y7,025–8,05', 'x', 9.798, (7.025, 8.05), 2.90),
 ('Akna déli lap y7,025 x9,80–10,75', 'y', 7.023, (9.80, 10.75), 2.90),
 ('Konyhacsonk x10,55 y4,10–5,05', 'x', 10.548, (4.10, 5.05), 2.90),
 ('Konyha keleti fal x10,55 y1,35–4,10', 'x', 10.548, (1.35, 4.10), 2.90),
 ('Konyha déli fal y1,35 x9,10–10,55', 'y', 1.352, (9.10, 10.55), 2.90),
 ('W02 déli tömör fal y4,05 x5,20–7,30 (kapcsolóoszlop x7,149)', 'y', 4.052, (5.20, 7.30), 2.90),
 ('Átjáró nyugati fala x7,30 y2,00–3,95', 'x', 7.302, (2.00, 3.95), 2.90),
 ('Közlekedő keleti fala x5,20 y2,75–3,95 (K25–K27+D46 y3,90)', 'x', 5.198, (2.75, 3.95), 2.90),
 ('Közlekedő pillér x5,00 y2,95–3,45', 'x', 4.998, (2.95, 3.45), 2.90),
 ('Közlekedő déli fala y2,75 x3,75–5,20 (06.1 ajtó)', 'y', 2.752, (3.75, 5.20), 2.90),
 ('W01 TV-fal x3,67 y4,05–8,05', 'x', 3.672, (4.05, 8.05), 2.90),
 ('Északi pillér Ny y8,05 x3,67–4,38', 'y', 8.048, (3.67, 4.38), 2.90),
 ('Üvegfal y8,25 x4,44–8,94', 'y', 8.248, (4.44, 8.94), 2.48),
 ('Északi pillér K y8,05 x9,00–9,80', 'y', 8.048, (9.00, 9.80), 2.90),
]
ZK = (0.15, 0.60, 1.05, 1.50, 1.95, 2.40, 2.80)
def lc_keres(lc, nev):
    if lc.collection.name == nev: return lc
    for ch in lc.children:
        r = lc_keres(ch, nev)
        if r: return r
def kizar(feltetel, ertek):
    for c in bpy.data.collections:
        if feltetel(c.name):
            lc = lc_keres(vl.layer_collection, c.name)
            if lc: lc.exclude = ertek
    vl.update()
NEM_EPIT = lambda n: n.startswith(('Stil_', 'VK_', 'A902_Butor', 'A902_Villamos'))
def lat(cam, P, deps, tol=0.04):
    p = world_to_camera_view(sc, cam, Vector(P))
    if p.z <= 0 or not (0 <= p.x <= 1 and 0 <= p.y <= 1): return None
    O = cam.matrix_world.translation.copy(); d = Vector(P) - O; L = d.length; d.normalize()
    hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, d, distance=L + 0.05)
    ok = (not hit) or (loc - Vector(P)).length <= tol
    return [round(p.x, 3), round(1 - p.y, 3), bool(ok), (ob.name if (hit and not ok) else None)]
MINDEN = dict(cams); MINDEN.update(REF)
CAMM = {k: (c.matrix_world.copy()) for k, c in MINDEN.items()}
for mod in ('epiteszet', 'S01', 'S02'):
    kizar(NEM_EPIT, True)
    if mod != 'epiteszet': kizar(lambda n: n == 'Stil_TOMEG_' + mod, False)
    deps = bpy.context.evaluated_depsgraph_get()
    for k, c in MINDEN.items():
        j = log['jeloltek'].setdefault(k, {})
        if 'loc' not in j: j.update(loc=[round(v, 3) for v in c.location], rot=[round(v, 4) for v in c.rotation_euler], lens=c.data.lens, shift_y=c.data.shift_y)
        j.setdefault('celpontok', {})[mod] = {n: lat(c, P, deps) for n, P in CEL.items()}
        fl = {}
        for nev, ax, sik, (a0, a1), zmax in FALAK:
            n = 0; bent = 0; vis = []; 
            steps = max(2, int(round((a1 - a0) / 0.05)) + 1)
            for i in range(steps):
                a = a0 + (a1 - a0) * i / (steps - 1)
                for z in ZK:
                    if z > zmax - 0.03: continue
                    P = (sik, a, z) if ax == 'x' else (a, sik, z); n += 1
                    r = lat(c, P, deps)
                    if r is None: continue
                    bent += 1
                    if r[2]: vis.append((a, z, r[0], r[1]))
            if vis:
                fl[nev] = dict(minta=n, kepben=bent, lathato=len(vis), arany=round(len(vis) / n, 3),
                    fal_tartomany=[round(min(v[0] for v in vis), 2), round(max(v[0] for v in vis), 2)],
                    z_tartomany=[min(v[1] for v in vis), max(v[1] for v in vis)],
                    u=[round(min(v[2] for v in vis), 3), round(max(v[2] for v in vis), 3)], v=[round(min(v[3] for v in vis), 3), round(max(v[3] for v in vis), 3)])
            else:
                fl[nev] = dict(minta=n, kepben=bent, lathato=0, arany=0.0)
        j.setdefault('falak', {})[mod] = fl
    kizar(lambda n: True, False)
# ---- 3) bútor-ütközés a kamerahelyen (tömegekkel) ----
for k, p in JEL.items():
    x, y, z = p['loc']; utk = []
    for kod, (col, rec) in TOMEG.items():
        for nev, bb in rec.items():
            if bb[0] - 0.15 <= x <= bb[3] + 0.15 and bb[1] - 0.15 <= y <= bb[4] + 0.15: utk.append(nev)
    log['jeloltek'][k]['kozeli_tomeg_15cm'] = utk
    log['jeloltek'][k]['fal_tav'] = dict(TV_fal_x367=round(x - 3.67, 2), eszaki_sik_y805=round(8.05 - y, 2), deli_sik_y405=round(y - 4.05, 2))
# ---- 4) felülnézet S01/S02 tömbbel (a jelölt-ékeket utólag rajzolom rá) ----
fc = T.kamera('JEL_felul2', (7.0, 5.0, 12.0), (0, 0, 0), col=jcol); fc.data.type = 'ORTHO'; fc.data.ortho_scale = 12.0
felso = [o for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render and o.name not in jcol.objects
         and not any(o.name in col.objects for col, r in TOMEG.values()) and min((o.matrix_world @ Vector(cc)).z for cc in o.bound_box) >= 2.80]
for o in felso: o.hide_render = True
sc.render.resolution_x, sc.render.resolution_y = 1400, 1000
for kod, (col, rec) in TOMEG.items():
    col.hide_render = False; vl.update(); sc.camera = fc; sc.render.filepath = os.path.join(OUT, f'cam12v2_felulnezet_{kod}.png'); bpy.ops.render.render(write_still=True); col.hide_render = True
log['felulnezet'] = dict(kozep=[7.0, 5.0], ortho_scale=12.0, px=[1400, 1000])
json.dump(log, open(os.path.join(OUT, 'cam12v2_jeloltek_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ')
