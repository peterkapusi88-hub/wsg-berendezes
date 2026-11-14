# v2b-1-k12 JAVASLAT v2: validátor (üres / referencia / master bútor / S01 V3 tömb / S02 V3 tömb), Cam_12 üres alapkép és tömbrenderek
# (generikus P902_24A, S01 V3, S02 V3), képtéri befoglalók, célpontok és falszakasz-láthatóság (ray cast) a V3.1 briefhez. Claude, 2026-10-25. NEM MENT.
import bpy, sys, os, json, time, hashlib, math, runpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T, stilus_tomeg_v3 as SV
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
W = os.path.dirname(os.path.abspath(__file__)) + '/'; L = '/Users/peterkapusi/Downloads/WSG/KEP-004/_munka/blender_cam11_v1/'
sc = bpy.context.scene; vl = bpy.context.view_layer
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(), validator={}, kepek=[])
MARAD = T.MARAD; MASTER = ('Agy_05_1_', 'Ejjeli_05_1_', 'Szonyeg_05_1_')
TOMEG = {k: SV.stilus_tomeg(k, sc, T) for k in ('S01', 'S02')}
gcol = bpy.data.collections.new('Stil_TOMEG_GEN'); sc.collection.children.link(gcol); grec = {}; T.generikus_P902_24A(gcol, grec); gcol.hide_render = True
def lathatosag(mod):
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        o.hide_render = not ((mod == 'referencia' and o.name.startswith(MARAD)) or (mod == 'master_butor' and o.name.startswith(MASTER)))
    if mod.startswith('tomeg_'): TOMEG[mod[6:]][0].hide_render = False
os.environ['WSG_LOCK'] = W + 'lock_k12v2/geometry_lock_A902_v2b.json'; os.environ['WSG_VILLAMOS'] = L + 'A902_villamos.json'
for mod in ('ures', 'referencia', 'master_butor', 'tomeg_S01', 'tomeg_S02'):
    lathatosag(mod); os.environ['WSG_REPORT_JSON'] = OUT + f'/validator_v2b1k12v2_{mod}.json'
    runpy.run_path(L + 'geometry_validator_v2.py')
    log['validator'][mod] = json.load(open(OUT + f'/validator_v2b1k12v2_{mod}.json', encoding='utf-8'))['summary']
lathatosag('ures'); T.alap_beallitas(sc)
for col, r in list(TOMEG.values()) + [(gcol, grec)]: col.hide_render = True
cam = bpy.data.objects['Cam_12_Nappali_Hero']; vl.update()
def renderel(fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cam.name, fajl=fajl, mp=round(time.time() - t, 1)))
renderel('A902_Alap-v2b1k12_blender_12_nappali-hero_JAVASLAT.png')
for nev, col in (('P902_24A_generikus', gcol), ('S01_V3', TOMEG['S01'][0]), ('S02_V3', TOMEG['S02'][0])):
    col.hide_render = False; vl.update(); renderel(f'A902_Cam12_tomeg_{nev}_v2.png'); col.hide_render = True
log['kepteri'] = {k: {o.name: T.kepteri(sc, cam, o) for o in col.objects} for k, col in (('S01', TOMEG['S01'][0]), ('S02', TOMEG['S02'][0]), ('GEN', gcol))}
# célpontok + falszakaszok (ray cast) – a 01_sarok_jeloltek.py-val azonos definíciók
exec(open(W + '01_sarok_jeloltek.py', encoding='utf-8').read().split('# ---- 2) célpontok vetítése + takarás (ray cast) ----')[1].split('MINDEN = dict(cams)')[0])
CEL['kozlekedo_kapcsolok_K25_27_D46'] = (5.182, 3.90, 1.10)
log['celpontok'] = {}; log['falak'] = {}
for mod in ('epiteszet', 'S01', 'S02'):
    kizar(NEM_EPIT, True)
    if mod != 'epiteszet': kizar(lambda n: n == 'Stil_TOMEG_' + mod, False)
    deps = bpy.context.evaluated_depsgraph_get()
    log['celpontok'][mod] = {n: lat(cam, P, deps) for n, P in CEL.items()}
    fl = {}
    for nev, ax, sik, (a0, a1), zmax in FALAK:
        n = 0; bent = 0; vis = []
        steps = max(2, int(round((a1 - a0) / 0.05)) + 1)
        for i in range(steps):
            a = a0 + (a1 - a0) * i / (steps - 1)
            for z in ZK:
                if z > zmax - 0.03: continue
                P = (sik, a, z) if ax == 'x' else (a, sik, z); n += 1
                r = lat(cam, P, deps)
                if r is None: continue
                bent += 1
                if r[2]: vis.append((a, z, r[0], r[1]))
        fl[nev] = dict(minta=n, kepben=bent, lathato=len(vis), arany=round(len(vis) / n, 3)) if not vis else dict(minta=n, kepben=bent, lathato=len(vis), arany=round(len(vis) / n, 3),
            fal_tartomany=[round(min(v[0] for v in vis), 2), round(max(v[0] for v in vis), 2)], z_tartomany=[min(v[1] for v in vis), max(v[1] for v in vis)],
            u=[round(min(v[2] for v in vis), 3), round(max(v[2] for v in vis), 3)], v=[round(min(v[3] for v in vis), 3), round(max(v[3] for v in vis), 3)])
    log['falak'][mod] = fl
    kizar(lambda n: True, False)
json.dump(log, open(os.path.join(OUT, 'cam12v2_ellenorzes_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', log['validator'])
