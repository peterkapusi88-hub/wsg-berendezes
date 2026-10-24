# =====================================================================================
# A-902 v2b lock-javítás „v2b-1” (2026-10-24, Claude)
# Jóváhagyás: Péter, 2026-10-24 17:06 – draft PR; a main-be csak az ő „mehet”-je után.
#
# Mit javít (a burok_zartsag_ellenorzes.py leletei, PR #8):
#  1) Kulso_E_05_1_0 x1: 2,95 -> 3,02 – a 05.1 fülke északi fala a v2b-ben x 3,02-re tolt pillérig ér
#     (7 cm-es homlokzati rés y 8,95–9,25-nél).
#  2) Kulso_D_05_2_furdo_0 x1: 6,60 -> 6,70 – a déli homlokzati fal a v2b-ben x 6,70-re tolt előtér-sarokelemig ér
#     (10 cm-es homlokzati rés y −0,30–0,00-nál).
#  3) v2_Mellved_Ny y0: 8,50 -> 9,25 – a tetőkert nyugati mellvédje a szerkezeti fal külső síkjánál kezdődik
#     (eddig 47 cm magasan belelógott a 05.1 fülkébe, a pillérbe és a fülke északi falába).
#  4) Anyag (csak a .blend-ben): Fal_05_1_nappali_0 és Kulso_E_05_1_0 – a falon maradt Zenit-tapéta
#     (Z_tapeta_greige) helyett Fal_feher. A Z_tapeta_greige anyag a fájlban marad (fake user) egy későbbi,
#     árazott tapétafelülethez.
# Más nem változik. A Pillér_05_1_EK 1 cm-es síkeltérése (y 8,04 vs. a fal 8,05) a hétfői mérésig marad.
#
# Futtatás (bpy 5.2 modul vagy Blender 5.2 háttérben), kézzel:
#   WSG_REPO=<repo> [WSG_LOCK=...] [WSG_BLEND_IN=...] [WSG_BLEND_OUT=...] python3 lockjavitas_v2b_burok.py
#   Alapértelmezés: a repóbeli lock és v2b .blend, helyben. Az élő ~/Downloads/WSG_A902_stilusok.blend-hez nem nyúl.
# Idempotens: ha egy érték már az új, kihagyja; ha sem a régi, sem az új, megáll, és semmit nem ír.
# Utána: geometry_validator_v2.py + geometry_v2/burok_zartsag_ellenorzes.py.
# =====================================================================================
import os
import json
import bpy

REPO = os.environ.get('WSG_REPO') or os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
LOCK = os.environ.get('WSG_LOCK') or os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json')
BLEND_IN = os.environ.get('WSG_BLEND_IN') or os.path.join(REPO, '03_blender', 'WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend')
BLEND_OUT = os.environ.get('WSG_BLEND_OUT') or BLEND_IN
TENGELY = ['x0', 'y0', 'z0', 'x1', 'y1', 'z1']
GEOM = [
    ('walls', 'Kulso_E_05_1_0', 3, 2.95, 3.02,
     '05.1 fülke északi fala a v2b-ben áthelyezett pillérig (7 cm-es homlokzati rés)'),
    ('walls', 'Kulso_D_05_2_furdo_0', 3, 6.60, 6.70,
     'déli homlokzati fal a v2b-ben áthelyezett előtér-sarokelemig (10 cm-es homlokzati rés)'),
    ('terrace_v2', 'v2_Mellved_Ny', 1, 8.50, 9.25,
     'tetőkert nyugati mellvédje a szerkezeti fal külső síkjától (eddig belelógott a 05.1 fülkébe)'),
]
ANYAG = [('Fal_05_1_nappali_0', 'Z_tapeta_greige', 'Fal_feher'), ('Kulso_E_05_1_0', 'Z_tapeta_greige', 'Fal_feher')]
EPS = 1e-6

# ---------------------------------------------------------------- 1) lock
L = json.load(open(LOCK, encoding='utf-8'))
valt = []
for grp, n, ax, old, new, ok in GEOM:
    v = L[grp][n][ax]
    if abs(v - new) < EPS:
        print('lock: már javítva –', n)
        continue
    if abs(v - old) > EPS:
        raise SystemExit(f'lock: {n} {TENGELY[ax]} = {v}, várt {old} – nem javítok semmit')
for grp, n, ax, old, new, ok in GEOM:
    if abs(L[grp][n][ax] - old) < EPS:
        L[grp][n][ax] = new
        valt.append(f'{grp}.{n} {TENGELY[ax]}: {old} → {new} – {ok}')
if valt:
    L['statusz']['terasz_v2'] = 'v2, ELŐZETES; a nyugati mellvéd déli vége y 9,25 (javítva 2026-10-24, v2b-1)'
    L.setdefault('javitasok', []).append(dict(
        azonosito='v2b-1', datum='2026-10-24', keszitette='Claude',
        jovahagyas='Péter, 2026-10-24 17:06 – draft PR; a main-be csak „mehet” után',
        ok='burokzártság- és terasz–belső tér átfedés-ellenőrzés (03_blender/geometry_v2/burok_zartsag_ellenorzes.py)',
        geometria=valt,
        anyag=[f'{o}: {a} → {b} (csak a .blend-ben)' for o, a, b in ANYAG],
        nem_valtozott='minden más fal, nyílászáró, padló, teraszelem és kamera; '
                      'a Pillér_05_1_EK 1 cm-es síkeltérése a hétfői mérésig marad'))
    tmp = LOCK + '.tmp'
    open(tmp, 'w', encoding='utf-8').write(json.dumps(L, ensure_ascii=False, indent=1))
    os.replace(tmp, LOCK)
    print('lock: írva,', len(valt), 'változás')

# ---------------------------------------------------------------- 2) .blend
bpy.ops.wm.open_mainfile(filepath=BLEND_IN)
bpy.context.preferences.filepaths.save_version = 0      # ne keletkezzen .blend1 a repóban
for grp, n, ax, old, new, ok in GEOM:
    o = bpy.data.objects[n]
    M = o.matrix_world
    Mi = M.inverted()
    a = ax % 3
    moved = 0
    for vtx in o.data.vertices:
        p = M @ vtx.co
        if abs(p[a] - old) < 1e-4:
            p[a] = new
            vtx.co = Mi @ p
            moved += 1
    o.data.update()
    pts = [M @ vtx.co for vtx in o.data.vertices]
    bb = [min(p[i] for p in pts) for i in range(3)] + [max(p[i] for p in pts) for i in range(3)]
    want = L[grp][n]
    if max(abs(bb[i] - want[i]) for i in range(6)) > 1e-4:
        raise SystemExit(f'blend: {n} befoglaló doboza {bb} nem egyezik a lockkal {want} – nem mentek')
    print('blend:', n, '– mozgatott csúcs:', moved)
for n, a, b in ANYAG:
    o = bpy.data.objects[n]
    for s in o.material_slots:
        if s.material and s.material.name == a:
            s.material = bpy.data.materials[b]
            print('anyag:', n, a, '→', b)
if 'Z_tapeta_greige' in bpy.data.materials:
    bpy.data.materials['Z_tapeta_greige'].use_fake_user = True
bpy.ops.wm.save_as_mainfile(filepath=BLEND_OUT, compress=True)
print('mentve:', BLEND_OUT)
