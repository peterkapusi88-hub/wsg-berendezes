# Cam_12 nappali hero – kamerajelöltek a TV-fal felől (Péter 2026-10-25 01:39). Tömbök: P902_24A generikus. NEM MENT.
import bpy, sys, os, json, time, hashlib, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tomeg_lib as T
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; T.alap_beallitas(sc)
col = bpy.data.collections.new('JEL_cam12_vizsgalat'); sc.collection.children.link(col)
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(), jeloltek={}, tomegek={})
JEL = {
 'H1_kozep_kelet_20': ((4.25, 6.35, 1.52), (1.4791, 0.0, -math.pi / 2), 20.0),
 'H1_kozep_kelet_18': ((4.25, 6.35, 1.52), (1.4791, 0.0, -math.pi / 2), 18.0),
 'H2_delnyugat_ENy_20': ((4.30, 5.10, 1.52), (1.4791, 0.0, -1.25), 20.0),
 'H3_eszaknyugat_KDK_20': ((4.30, 7.55, 1.52), (1.4791, 0.0, -1.95), 20.0),
}
cams = {k: T.kamera('JEL_' + k, *v, col=col) for k, v in JEL.items()}
cams['Cam_03_referencia'] = bpy.data.objects['Cam_03_Etkezo_konyha']
CEL = {'05.3 ajtó közepe': (10.75, 6.50, 1.05), 'keleti fal (konyha-csonk/05.3 fal) 1,5 m': (10.75, 5.55, 1.50), 'akna ÉK sarok': (9.80, 7.50, 1.50),
       'étkezőasztal közepe': (8.35, 6.27, 0.75), 'konyhanyílás közepe': (9.50, 4.05, 0.90), 'konyha hátsó fala': (9.50, 2.40, 1.20),
       'előtér-átjáró közepe': (7.82, 4.05, 1.00), 'üvegfal közepe': (6.70, 8.25, 1.25), 'U belseje (ülés)': (5.50, 6.45, 0.42),
       'U hát közepe': (7.07, 6.45, 0.80), 'D19 déli dugalj': (7.10, 4.05, 0.30)}
for n, P in CEL.items(): pass
log['celpontok'] = {}
def renderel(nev, fajl):
    sc.camera = cams[nev]; sc.render.filepath = os.path.join(OUT, fajl); t = time.time(); bpy.ops.render.render(write_still=True); return round(time.time() - t, 1)
# 1) üres alapnézetek (a későbbi „1. kép”)
for k in cams:
    mp = renderel(k, f'cam12_{k}_ures.png'); log['jeloltek'].setdefault(k, {})['ures_mp'] = mp
# 2) tömbökkel
T.generikus_P902_24A(col, log['tomegek'])
bpy.context.view_layer.update()
for k, c in cams.items():
    mp = renderel(k, f'cam12_{k}_tomeg.png')
    j = log['jeloltek'][k]; j.update(tomeg_mp=mp, loc=[round(v, 3) for v in c.location], rot=[round(v, 4) for v in c.rotation_euler], lens=c.data.lens,
        celpontok={n: T.vetit(sc, c, P) for n, P in CEL.items()},
        tomeg_kepteri={o.name: T.kepteri(sc, c, o) for o in col.objects if o.type == 'MESH'})
# 3) felülnézet a kamerákkal (dokumentáció)
fc = T.kamera('JEL_felul', (7.0, 5.0, 12.0), (0, 0, 0), col=col); fc.data.type = 'ORTHO'; fc.data.ortho_scale = 12.0
felso = [o for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render and o.name not in col.objects and min((o.matrix_world @ T.Vector(c)).z for c in o.bound_box) >= 2.80]
for o in felso: o.hide_render = True
sc.camera = fc; sc.render.resolution_x, sc.render.resolution_y = 1400, 1000; sc.render.filepath = os.path.join(OUT, 'cam12_felulnezet.png'); bpy.ops.render.render(write_still=True)
log['felulnezet'] = dict(kozep=[7.0, 5.0], ortho_scale=12.0, px=[1400, 1000])
json.dump(log, open(os.path.join(OUT, 'cam12_jeloltek_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ')
