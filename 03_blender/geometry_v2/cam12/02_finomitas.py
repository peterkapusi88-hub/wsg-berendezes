# Cam_12 hero v2 – a K1 (ÉNy-i sarok) finomítása: lencse 20/22 mm, kevesebb mennyezet (shift_y), kamera-magasság. Alap: v2b-1-k11b. NEM MENT.
import bpy, sys, os, json, time, hashlib, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T, stilus_tomeg_v3 as SV
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; vl = bpy.context.view_layer
assert hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest().startswith('9875cd57')
T.alap_beallitas(sc)
TOMEG = {k: SV.stilus_tomeg(k, sc, T) for k in ('S01', 'S02')}
jcol = bpy.data.collections.new('JEL_finom'); sc.collection.children.link(jcol)
rot = lambda th, tilt=0.0: (math.radians(90.0 - tilt), 0.0, math.radians(th - 90.0))
JEL = {'R1_20mm_th46_sh08_z145': ((3.95, 7.90, 1.45), -46.0, 20.0, -0.08),
       'R2_22mm_th45_sh08_z145': ((3.95, 7.90, 1.45), -45.0, 22.0, -0.08),
       'R3_22mm_th45_sh06_z135': ((3.95, 7.90, 1.35), -45.0, 22.0, -0.06)}
log = {}
for k, (loc, th, lens, sh) in JEL.items():
    c = T.kamera('JEL_' + k, loc, rot(th), lens=lens, col=jcol); c.data.shift_y = sh; vl.update()
    log[k] = dict(loc=loc, theta=th, lens=lens, shift_y=sh, rot=[round(v, 4) for v in c.rotation_euler])
    for suf, col in (('ures', None), ('S01', TOMEG['S01'][0]), ('S02', TOMEG['S02'][0])):
        if col: col.hide_render = False
        vl.update(); sc.camera = c; sc.render.filepath = os.path.join(OUT, f'{k}_{suf}.png'); bpy.ops.render.render(write_still=True)
        if col: col.hide_render = True
json.dump(log, open(os.path.join(OUT, 'finomitas_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ')
