# v2b-1-k13 KAMERACSOMAG C: validátor (üres / referencia / master bútor / C S01–S02 × TV40–TV60M tömb), alapképek (Cam_12 v3, Cam_03 K1),
# tömbképek, képterület- és láthatósági mérés az új és a régi (v2) Cam_12-vel. Claude, 2026-10-25. NEM MENT.
import bpy, sys, os, json, time, hashlib, math, runpy
from mathutils import Vector
from bpy_extras.object_utils import world_to_camera_view
W = os.path.dirname(os.path.abspath(__file__)) + '/'; sys.path.insert(0, W)
import tomeg_lib as T, c_tomeg_lib as L
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest()
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=SHA, validator={}, kepek=[], meres={})
K = L.konyha(sc); EL = {st: L.elrendezes(sc, st) for st in ('S01', 'S02')}; TV = {m: L.tv_fal(sc, m) for m in ('TV40', 'TV60M')}
# a validátor a „Stil_” gyűjteményeket nézi → átnevezés
for st, (c, r) in EL.items(): c.name = 'Stil_TOMEG_C_' + st
for m, (c, r) in TV.items(): c.name = 'Stil_TOMEG_' + m
log['tomeg'] = {st: EL[st][1] for st in EL}; log['tv'] = {m: TV[m][1] for m in TV}; log['konyha'] = K[1]
MARAD = T.MARAD; MASTER = ('Agy_05_1_', 'Ejjeli_05_1_', 'Szonyeg_05_1_')
def lathatosag(mod):
    for c in bpy.data.collections:
        if c.name.startswith('Stil_'): c.hide_render = True
    for o in bpy.data.collections['A902_Butor'].objects:
        o.hide_render = not ((mod == 'referencia' and o.name.startswith(MARAD)) or (mod == 'master_butor' and o.name.startswith(MASTER)))
    if mod.startswith('C_'):
        _, st, tvm = mod.split('_'); EL[st][0].hide_render = False; TV[tvm][0].hide_render = False
os.environ['WSG_LOCK'] = W + 'lock_k13/geometry_lock_A902_v2b.json'; os.environ['WSG_VILLAMOS'] = W + 'A902_villamos.json'
for mod in ('ures', 'referencia', 'master_butor', 'C_S01_TV40', 'C_S02_TV40', 'C_S01_TV60M', 'C_S02_TV60M'):
    lathatosag(mod); os.environ['WSG_REPORT_JSON'] = OUT + f'/validator_v2b1k13_{mod}.json'
    runpy.run_path(W + 'geometry_validator_v2.py')
    log['validator'][mod] = json.load(open(OUT + f'/validator_v2b1k13_{mod}.json', encoding='utf-8'))['summary']
lathatosag('ures'); T.alap_beallitas(sc)
for c, r in list(EL.values()) + list(TV.values()): c.hide_render = True
K[0].hide_render = True
c12 = bpy.data.objects['Cam_12_Nappali_Hero']; c3 = bpy.data.objects['Cam_03_Etkezo_konyha']
jcol = L.gyujt(sc, 'JEL_regi_cam12')
r12 = T.kamera('JEL_Cam12_v2_regi', (3.95, 7.90, 1.45), L.rot(-45.0), lens=22.0, col=jcol); r12.data.shift_y = -0.08
vl.update()
def renderel(cam, fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cam.name, fajl=fajl, mp=round(time.time() - t, 1)))
renderel(c12, 'A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png')
renderel(c3, 'A902_Alap-v2b1k13_blender_03_konyha-etkezo_K1_JAVASLAT.png')
K[0].hide_render = False
for st in ('S01', 'S02'):
    for tvm in ('TV40', 'TV60M'):
        EL[st][0].hide_render = False; TV[tvm][0].hide_render = False; vl.update()
        renderel(c12, f'A902_Cam12v3_tomeg_C_{st}_{tvm}.png'); renderel(r12, f'A902_Cam12v2regi_tomeg_C_{st}_{tvm}.png')
        if tvm == 'TV40': renderel(c3, f'A902_Cam03K1_tomeg_C_{st}.png')
        EL[st][0].hide_render = True; TV[tvm][0].hide_render = True
# mérés (a jelöltkeresés definícióival)
src = open(W + '01_cam12C_jeloltek.py', encoding='utf-8').read()
defs = 'def lc_keres(lc, nev):' + src.split('def lc_keres(lc, nev):')[1].split("log = dict(")[0]
ns = dict(globals()); exec(defs, ns)
NEM_EPIT = lambda n: n.startswith(('Stil_', 'VK_', 'A902_Butor', 'A902_Villamos', 'KONYHA_', 'JEL_'))
for st in ('S01', 'S02'):
    for tvm in ('TV40', 'TV60M'):
        ns['kizar'](NEM_EPIT, True); ns['kizar'](lambda n: n in ('Stil_TOMEG_C_' + st, 'Stil_TOMEG_' + tvm, 'KONYHA_TOMEG'), False)
        deps = bpy.context.evaluated_depsgraph_get()
        for nev, c in (('Cam_12_v3', c12), ('Cam_12_v2_regi', r12), ('Cam_03_K1', c3)):
            r = dict(kepterulet=ns['kepterulet'](c, deps), lathatosag={})
            for fn, ms in ns['FAL_MINTA'].items():
                res = [ns['lathato'](c, deps, ns['pont'](m)) for m in ms]; bent = [x for x in res if x is not None]
                r['lathatosag'][fn] = dict(minta=len(ms), kepben=len(bent), takaratlan=sum(1 for x in bent if x), arany=round(sum(1 for x in bent if x) / len(ms), 3))
            log['meres'][f'{nev}|{st}|{tvm}'] = r
ns['kizar'](lambda n: True, False)
log['kamerak'] = {o.name: dict(loc=[round(v, 4) for v in o.matrix_world.translation], rot=[round(v, 5) for v in o.rotation_euler], lens=o.data.lens, shift_y=o.data.shift_y) for o in (c12, c3, r12)}
json.dump(log, open(os.path.join(OUT, 'kameracsomag_C_ellenorzes_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', json.dumps(log['validator'], ensure_ascii=False))
