# Cam_12 hero – újrakivágás a C elrendezéssel (Péter 2026-10-25 04:08: „a kanapé ne foglaljon túl nagy képterületet, ne takarja a
# nappali–étkező–konyha és a W02/W07 fontos elemeit; a hero kreatív értékét ne áldozzuk fel a régi beállítás mechanikus megtartásáért”).
# Alap: v2b-1-k12 v2 (PR #17), sha 66172d43. Jelölt kamerák × (S01, S02) × (TV40, TV60M): képterület-osztályozás sugárvetéssel
# (160×100), falfelület-láthatóság, 50 %-os EEVEE-renderek. Claude, 2026-10-25. A .blend-et NEM menti.
import bpy, sys, os, json, time, hashlib, math
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T, c_tomeg_lib as L
ARGS = sys.argv[sys.argv.index('--') + 1:]; OUT = ARGS[0]; os.makedirs(OUT, exist_ok=True)
JFAJL = ARGS[1] if len(ARGS) > 1 else None; RENDER = (ARGS[2] if len(ARGS) > 2 else 'mind')  # 'mind' | 'nincs' | vesszős jelöltlista
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('66172d43'), SHA
T.alap_beallitas(sc); sc.render.resolution_percentage = 50
K = L.konyha(sc); EL = {st: L.elrendezes(sc, st) for st in ('S01', 'S02')}; TV = {m: L.tv_fal(sc, m) for m in ('TV40', 'TV60M')}
jcol = L.gyujt(sc, 'JEL_cam12C')
J = {  # név: (loc, theta, lens, shift_y)
 'R0_mostani':          ((3.95, 7.90, 1.45), -45.0, 22.0, -0.08),
 'R1_magasabb_160':     ((3.95, 7.90, 1.60), -45.0, 22.0, -0.10),
 'R2_24mm':             ((3.95, 7.90, 1.45), -45.0, 24.0, -0.08),
 'R3_fordit_40':        ((3.95, 7.90, 1.45), -40.0, 22.0, -0.08),
 'R4_fordit_40_155_24': ((3.95, 7.90, 1.55), -40.0, 24.0, -0.10),
 'R5_fordit_42_155':    ((3.95, 7.90, 1.55), -42.0, 22.0, -0.10),
 'R6_kelet_440':        ((4.40, 7.88, 1.50), -45.0, 22.0, -0.08),
 'R7_kelet_440_50_24':  ((4.40, 7.88, 1.55), -50.0, 24.0, -0.10),
 'R8_420_43_155':       ((4.20, 7.92, 1.55), -43.0, 22.0, -0.10),
 'R9_magas_170_20':     ((3.95, 7.90, 1.70), -44.0, 20.0, -0.14),
}
if JFAJL: J = {k: (tuple(v[0]), v[1], v[2], v[3]) for k, v in json.load(open(JFAJL, encoding='utf-8')).items()}
CAMS = {}
for k, (loc, th, lens, sy) in J.items():
    c = T.kamera('JEL_' + k, loc, L.rot(th), lens=lens, col=jcol); c.data.shift_y = sy; CAMS[k] = c
vl.update()
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
NEM_EPIT = lambda n: n.startswith(('Stil_', 'VK_', 'A902_Butor', 'A902_Villamos', 'C_', 'TV_', 'KONYHA_', 'JEL_'))
def osztaly(ob, p):
    n = ob.name
    if n.startswith('C_kanape'): return 'kanape'
    if n.startswith('C_etkezo'): return 'etkezo'
    if n.startswith('C_ML04'): return 'ML04'
    if n.startswith('KONYHA_'): return 'konyha_butor'
    if n.startswith('TV_szekreny'): return 'tv_szekreny60'
    if n.startswith('TV_'): return 'tv_egyeb'
    x, y, z = p
    if z < 0.02: return 'padlo'
    if z > 2.87: return 'mennyezet'
    if y > 8.12: return 'uveg_terasz'
    if abs(y - 4.05) < 0.04 and 5.18 <= x <= 7.32: return 'W02'
    if (abs(x - 5.20) < 0.04 and 2.70 <= y <= 3.97) or (abs(x - 5.00) < 0.04 and 2.90 <= y <= 3.50) or (abs(y - 2.75) < 0.04 and 3.70 <= x <= 5.22) or (4.98 <= x <= 5.22 and abs(y - 3.45) < 0.04) or (4.98 <= x <= 5.22 and abs(y - 2.95) < 0.04): return 'W07'
    if abs(x - 10.75) < 0.04 and 5.0 <= y <= 7.05: return 'W03_05_3'
    if x > 8.40 and y < 5.10: return 'konyha_fal'
    if abs(x - 3.67) < 0.04: return 'W01_TV_fal'
    if 9.75 <= x <= 10.8 and y > 7.0: return 'akna'
    return 'egyeb_fal'
NU, NV = 160, 100
def kepterulet(cam, deps):
    fr = [cam.matrix_world @ v for v in cam.data.view_frame(scene=sc)]  # jobb-felső, jobb-alsó, bal-alsó, bal-felső
    tr, br, bl, tl = fr; O = cam.matrix_world.translation.copy(); cnt = {}
    rac = {}  # durva rács a kanapé takarásához: oszloponként
    for j in range(NV):
        vv = (j + 0.5) / NV
        left = tl.lerp(bl, vv); right = tr.lerp(br, vv)
        for i in range(NU):
            P = left.lerp(right, (i + 0.5) / NU); d = (P - O).normalized()
            hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, d, distance=60.0)
            k = osztaly(ob, loc) if hit else 'kint'
            cnt[k] = cnt.get(k, 0) + 1
    tot = NU * NV
    return {k: round(v / tot, 4) for k, v in sorted(cnt.items(), key=lambda t: -t[1])}
FAL_MINTA = {  # sík, tengely, tartomány, z – a takaratlan láthatóság mérésére (csak építészet vs. tömbökkel)
 'W02': [('y', 4.052, a, z) for a in [5.25 + 0.1 * i for i in range(21)] for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)],
 'W07': [('x', 5.198, a, z) for a in [3.47 + 0.05 * i for i in range(10)] for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)] +
        [('y', 2.752, a, z) for a in [4.55 + 0.05 * i for i in range(10)] for z in (0.2, 0.6, 1.0, 1.4, 1.8, 2.2, 2.6)],
 'konyha_magas_elemek_eleje': [('y', 1.952, a, z) for a in [9.10 + 0.08 * i for i in range(11)] for z in (0.3, 0.8, 1.3, 1.8)] +
        [('x', 9.948, a, z) for a in [4.70 + 0.05 * i for i in range(11)] for z in (0.3, 0.8, 1.3, 1.8, 2.1)],
 'konyha_pultfal_x10_55': [('x', 10.548, a, z) for a in [2.0 + 0.1 * i for i in range(26)] for z in (1.0, 1.3, 1.6, 1.9, 2.2)],
 'etkezo_asztallap': [('z', 0.752, (x, y)) for x in (8.1, 8.3, 8.5, 8.7, 8.85) for y in (5.5, 5.8, 6.1, 6.4, 6.7, 6.95)],
 'W03_05_3_ajto': [('x', 10.778, a, z) for a in [6.12 + 0.08 * i for i in range(10)] for z in (0.3, 0.8, 1.3, 1.8)],
}
def pont(m):
    if m[0] == 'z': return Vector((m[2][0], m[2][1], m[1]))
    ax, s, a, z = m
    return Vector((s, a, z)) if ax == 'x' else Vector((a, s, z))
def lathato(cam, deps, P, tol=0.05):
    p = world_to_camera_view(sc, cam, P)
    if p.z <= 0 or not (0 <= p.x <= 1 and 0 <= p.y <= 1): return None
    O = cam.matrix_world.translation.copy(); d = P - O; Ln = d.length; d.normalize()
    hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, d, distance=Ln + 0.05)
    return (not hit) or (loc - P).length <= tol
log = dict(blender=bpy.app.version_string, sha256=SHA, jeloltek={k: dict(loc=list(v[0]), theta=v[1], lens=v[2], shift_y=v[3]) for k, v in J.items()},
           tomeg={st: EL[st][1] for st in EL}, tv={m: TV[m][1] for m in TV}, konyha=K[1], meres={})
KONF = [('S01', 'TV40'), ('S02', 'TV40'), ('S01', 'TV60M'), ('S02', 'TV60M')]
for st, tvm in KONF:
    kizar(NEM_EPIT, True); kizar(lambda n: n in ('C_' + st, 'TV_' + tvm, 'KONYHA_TOMEG'), False)
    deps = bpy.context.evaluated_depsgraph_get()
    for k, c in CAMS.items():
        r = dict(kepterulet=kepterulet(c, deps), lathatosag={})
        for fn, ms in FAL_MINTA.items():
            res = [lathato(c, deps, pont(m)) for m in ms]
            bent = [x for x in res if x is not None]
            r['lathatosag'][fn] = dict(minta=len(ms), kepben=len(bent), takaratlan=sum(1 for x in bent if x), arany=round(sum(1 for x in bent if x) / len(ms), 3))
        r['ML04_jel_kepben'] = [round(v, 3) for v in world_to_camera_view(sc, c, Vector((L.ML04[0], L.ML04[1], 1.78)))]
        log['meres'][f'{k}|{st}|{tvm}'] = r
kizar(lambda n: True, False)
# renderek: minden jelölt S01/S02 × TV40, a TV60M-ből S01
for c in list(EL.values()) + list(TV.values()): c[0].hide_render = True
K[0].hide_render = False
def renderel(cam, f):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, f); bpy.ops.render.render(write_still=True)
for st, tvm in [('S01', 'TV40'), ('S02', 'TV40'), ('S01', 'TV60M'), ('S02', 'TV60M')]:
    EL[st][0].hide_render = False; TV[tvm][0].hide_render = False; vl.update()
    for k, c in CAMS.items():
        if RENDER == 'mind' or (RENDER != 'nincs' and k in RENDER.split(',')): renderel(c, f'c12_{k}_{st}_{tvm}.png')
    EL[st][0].hide_render = True; TV[tvm][0].hide_render = True
json.dump(log, open(os.path.join(OUT, ('cam12C_jeloltek_log.json' if not JFAJL else 'cam12C_' + os.path.splitext(os.path.basename(JFAJL))[0] + '_log.json')), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ')
