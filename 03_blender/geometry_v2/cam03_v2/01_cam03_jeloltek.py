# Új, konyhaorientált Cam_03 – jelöltek (Péter 2026-10-25 02:33 és 02:52 CET: „érdemben különbözzön a Cam_12-től”). Alap: v2b-1-k12 v2 (PR #17, sha 66172d43).
# Üres tér + generikus konyhatömb, valamint az A/C elrendezés tömbjével; láthatósági átfedés a Cam_12-vel (sugárvetés), a konyha képaránya. Claude, 2026-10-25. NEM MENT.
import bpy, sys, os, json, time, hashlib, math
from mathutils import Vector
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T, elrendezes_tomeg_lib as L
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
SHA = hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(); assert SHA.startswith('66172d43'), SHA
T.alap_beallitas(sc); sc.render.resolution_percentage = 50
KCOL, KREC = L.konyha_tomeg(sc)
ALT = {k: L.alternativa_tomeg(sc, k) for k in ('S01_A', 'S02_A', 'S01_C', 'S02_C')}
jcol = L.gyujtemeny(sc, 'JEL_cam03v2')
JEL = {
 'K1_EK_konyhatengely_20': dict(loc=(9.45, 7.55, 1.50), theta=-90.0, lens=20.0, shift_y=-0.08),
 'K1_EK_konyhatengely_18': dict(loc=(9.45, 7.55, 1.50), theta=-90.0, lens=18.0, shift_y=-0.08),
 'K2_EK_atlos_20':         dict(loc=(8.95, 7.70, 1.50), theta=-78.0, lens=20.0, shift_y=-0.08),
 'K3_nappali_kozep_22':    dict(loc=(7.20, 7.20, 1.50), theta=-55.0, lens=22.0, shift_y=-0.06),
 'K4_konyhabol_ki_18':     dict(loc=(9.50, 2.20, 1.50), theta=90.0, lens=18.0, shift_y=-0.05),
}
cams = {}
for k, p in JEL.items():
    c = T.kamera('JEL_' + k, p['loc'], L.rot(p['theta']), lens=p['lens'], col=jcol); c.data.shift_y = p['shift_y']; cams[k] = c
REF = {'Cam_12_hero': bpy.data.objects['Cam_12_Nappali_Hero'], 'Cam_03_regi': bpy.data.objects['Cam_03_Etkezo_konyha'], 'Cam_02_kontroll': bpy.data.objects['Cam_02_Nappali_terasz']}
vl.update()
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=SHA, jeloltek={}, konyha_tomeg=KREC, alt_tomeg={k: v[1] for k, v in ALT.items()})
def renderel(cam, fajl):
    sc.camera = cam; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True); return round(time.time() - t, 1)
# ---- 1) renderek: üres + konyhatömb; S02_A és S01_C tömbbel ----
MIND = dict(cams); MIND.update(REF)
for k, c in MIND.items():
    j = log['jeloltek'].setdefault(k, {})
    j.update(loc=[round(v, 3) for v in c.location], rot=[round(v, 4) for v in c.rotation_euler], lens=c.data.lens, shift_y=c.data.shift_y)
    j['ures_konyha_mp'] = renderel(c, f'cam03v2_{k}_ures_konyha.png')
    for kk in ('S02_A', 'S01_C'):
        ALT[kk][0].hide_render = False; vl.update(); j[f'{kk}_mp'] = renderel(c, f'cam03v2_{k}_tomeg_{kk}.png'); ALT[kk][0].hide_render = True
# ---- 2) sugárvetés: látható felületek (fal, konyha, bútor), átfedés a Cam_12-vel; a konyha képaránya ----
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
def minta(cam, deps, nx=120, ny=75):
    fr = cam.data.view_frame(scene=sc); M = cam.matrix_world; O = M.translation.copy(); R = M.to_3x3()
    tr, br, bl, tl = fr[0], fr[1], fr[2], fr[3]
    vox = set(); kony = 0; ossz = 0; obj = {}
    for iy in range(ny):
        for ix in range(nx):
            u = (ix + 0.5) / nx; v = (iy + 0.5) / ny
            top = tl.lerp(tr, u); bot = bl.lerp(br, u); P = top.lerp(bot, v)
            d = (R @ P).normalized(); hit, loc, nor, idx, ob, mw = sc.ray_cast(deps, O, d, distance=40.0); ossz += 1
            if not hit: continue
            if ob.name.startswith('KONYHA_'): kony += 1
            if 0.03 < loc.z < 2.86:
                vox.add((round(loc.x / 0.2), round(loc.y / 0.2), round(loc.z / 0.2)))
            obj[ob.name] = obj.get(ob.name, 0) + 1
    return vox, round(kony / ossz, 3), obj
kizar(lambda n: n.startswith(('Stil_', 'VK_', 'A902_Butor', 'A902_Villamos', 'ALT_')), True)
deps = bpy.context.evaluated_depsgraph_get()
V = {}
for k, c in MIND.items():
    vox, kony, obj = minta(c, deps); V[k] = vox
    log['jeloltek'][k]['konyha_kepterulet'] = kony
    log['jeloltek'][k]['legtobb_talalat'] = sorted(obj.items(), key=lambda kv: -kv[1])[:12]
for k in MIND:
    a = V[k]; b = V['Cam_12_hero']
    log['jeloltek'][k]['atfedes_cam12'] = round(len(a & b) / max(1, len(a)), 3)
    log['jeloltek'][k]['atfedes_cam03_regi'] = round(len(a & V['Cam_03_regi']) / max(1, len(a)), 3)
kizar(lambda n: True, False)
json.dump(log, open(os.path.join(OUT, 'cam03v2_jeloltek_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', json.dumps({k: (v.get('konyha_kepterulet'), v.get('atfedes_cam12')) for k, v in log['jeloltek'].items()}))
