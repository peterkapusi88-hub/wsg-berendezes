# A-902 Cam_02 – szürke bútortömbös elrendezés-referencia a KEP-004 v2 geometriai javításához (Péter, 2026-10-25 01:23: mehet).
# Elrendezés: P902_24A elfogadott MÉRETPRÓBA (U 3,00 × 2,40 nyitott oldal a nyugati TV-blokk felé; TV-konzol 1,80 × 0,45 a gyári blokk
# előtt; étkező a terv 80 × 180-as asztalával, 0,30 m-rel nyugatra, 3 + 3 betolt szék). Forrás: 03_blender/geometry_A811_A812/meretproba/
# terv_elrendezes_A902.json + terv_elrendezes_a902.py. Az alapkép-beállítás azonos a render_alapkepek_v2b1.py-val (Cam_02 rész).
# Csak a betöltött példányon módosít, NEM MENT. Futtatás: Blender -b <v2b-1-k11b.blend> --python 01_tomeg_cam02.py -- <kimenet>
import bpy, sys, os, json, time, hashlib, math
from bpy_extras.object_utils import world_to_camera_view
from mathutils import Vector
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; r = sc.render; vs = sc.view_settings
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
for c in bpy.data.collections:
    if c.name.startswith('Stil_') or c.name.startswith('VK_') or c.name == 'A902_Villamos_TERV': c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    if not o.name.startswith(MARAD): o.hide_render = True
FAL_FEHER = bpy.data.materials['Fal_feher']
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher': s.material = FAL_FEHER
r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
sc.eevee.taa_render_samples = 128
vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.gamma = 1.0; r.image_settings.file_format = 'PNG'
nt = sc.world.node_tree; bg = nt.nodes['Background']
for l in list(nt.links):
    if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0
for o in bpy.data.objects:
    if o.type == 'LIGHT': o.hide_render = True
vs.exposure = 0.75
cam = bpy.data.objects['Cam_02_Nappali_terasz']; sc.camera = cam
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(),
           kamera=dict(loc=[round(v, 4) for v in cam.location], rot=[round(v, 4) for v in cam.rotation_euler], lens=cam.data.lens), kepek=[], tomegek={})
# 1) ellenőrző: tömbök nélkül (meg kell egyeznie a v1 csomag 01-es alapképével)
r.filepath = os.path.join(OUT, 'A902_Cam02_alap_ellenorzes_k11b.png'); t = time.time(); bpy.ops.render.render(write_still=True)
log['kepek'].append(dict(fajl='A902_Cam02_alap_ellenorzes_k11b.png', mp=round(time.time() - t, 1)))
# 2) tömbök
col = bpy.data.collections.new('JEL_tomeg_Cam02'); sc.collection.children.link(col)
def anyag(nev, v):
    m = bpy.data.materials.new(nev); m.use_nodes = True; b = m.node_tree.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (v, v, v, 1); b.inputs['Roughness'].default_value = 0.85; return m
M = dict(kanape=anyag('JEL_t_kanape', 0.30), etkezo=anyag('JEL_t_etkezo', 0.42), tv=anyag('JEL_t_tvkonzol', 0.22), kepernyo=anyag('JEL_t_kepernyo', 0.02))
def doboz(nev, a, b, m):
    me = bpy.data.meshes.new(nev); x0, y0, z0 = a; x1, y1, z1 = b
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    me.from_pydata(v, [], [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]); me.update()
    o = bpy.data.objects.new(nev, me); col.objects.link(o); me.materials.append(M[m]); log['tomegek'][nev] = [round(t, 3) for t in a + b]; return o
# U-kanapé zóna P902_24A: [4,77; 4,95; 7,17; 7,95], hát az étkező (kelet) felé, nyitott a TV (nyugat) felé
X0, Y0, X1, Y1 = 4.77, 4.95, 7.17, 7.95; D = 0.90; ULES, HAT, HV = 0.42, 0.80, 0.20
doboz('T_kanape_hat_ules', (X1 - D, Y0, 0), (X1, Y1, ULES), 'kanape')
doboz('T_kanape_del_kar_ules', (X0, Y0, 0), (X1 - D, Y0 + D, ULES), 'kanape')
doboz('T_kanape_eszak_kar_ules', (X0, Y1 - D, 0), (X1 - D, Y1, ULES), 'kanape')
doboz('T_kanape_hattamla_kelet', (X1 - HV, Y0, ULES), (X1, Y1, HAT), 'kanape')
doboz('T_kanape_hattamla_del', (X0, Y0, ULES), (X1 - HV, Y0 + HV, HAT), 'kanape')
doboz('T_kanape_hattamla_eszak', (X0, Y1 - HV, ULES), (X1 - HV, Y1, HAT), 'kanape')
# TV-konzol a gyári blokk előtt [3,67; 5,15; 4,12; 6,95], h 0,50 + 65"-os képernyő (1,45 × 0,83) a konzol közepén
doboz('T_tv_konzol', (3.67, 5.15, 0), (4.12, 6.95, 0.50), 'tv')
doboz('T_tv_kepernyo', (3.70, 6.05 - 0.725, 0.85), (3.75, 6.05 + 0.725, 1.68), 'kepernyo')
# étkező: a terv 80 × 180-as asztala 0,30 m-rel nyugatra [7,95; 5,37; 8,75; 7,17], lap 0,72–0,75 + két lapláb; 3 + 3 betolt szék
AX0, AY0, AX1, AY1 = 7.95, 5.37, 8.75, 7.17
doboz('T_asztal_lap', (AX0, AY0, 0.72), (AX1, AY1, 0.75), 'etkezo')
doboz('T_asztal_lab_d', (AX0 + 0.25, AY0 + 0.25, 0), (AX1 - 0.25, AY0 + 0.33, 0.72), 'etkezo')
doboz('T_asztal_lab_e', (AX0 + 0.25, AY1 - 0.33, 0), (AX1 - 0.25, AY1 - 0.25, 0.72), 'etkezo')
for i, yc in enumerate((5.67, 6.27, 6.87)):
    doboz(f'T_szek_ny_{i}_ules', (7.68, yc - 0.225, 0), (8.13, yc + 0.225, 0.46), 'etkezo')
    doboz(f'T_szek_ny_{i}_hat', (7.68, yc - 0.225, 0.46), (7.74, yc + 0.225, 0.82), 'etkezo')
    doboz(f'T_szek_k_{i}_ules', (8.57, yc - 0.225, 0), (9.02, yc + 0.225, 0.46), 'etkezo')
    doboz(f'T_szek_k_{i}_hat', (8.96, yc - 0.225, 0.46), (9.02, yc + 0.225, 0.82), 'etkezo')
bpy.context.view_layer.update()
# képtéri befoglalók (0–1, bal felső sarok = 0,0) – a FRAME LAYOUT szöveghez
def kep(o):
    pts = [world_to_camera_view(sc, cam, o.matrix_world @ Vector(c)) for c in o.bound_box]
    pts = [p for p in pts if p.z > 0]
    if not pts: return None
    xs = [p.x for p in pts]; ys = [1 - p.y for p in pts]
    return [round(min(xs), 3), round(min(ys), 3), round(max(xs), 3), round(max(ys), 3)]
log['kepteri_befoglalo'] = {o.name: kep(o) for o in col.objects}
pont = lambda P: (lambda p: [round(p.x, 3), round(1 - p.y, 3), round(p.z, 2)])(world_to_camera_view(sc, cam, Vector(P)))
log['kepteri_pontok'] = {'ML05_mennyezet': pont((5.619, 6.274, 2.90)), 'ML04_mennyezet': pont((8.549, 6.274, 2.90)), 'D16_D17_doboz': pont((3.693, 6.29, 0.35)),
                         'G08': pont((3.693, 6.169, 0.35)), 'asztal_ny_el_kozep_074': pont((7.95, 6.27, 0.75)), 'kanape_zona_kozep_042': pont((5.97, 6.45, 0.42))}
r.filepath = os.path.join(OUT, 'A902_Cam02_tomeg_P902_24A_v1.png'); t = time.time(); bpy.ops.render.render(write_still=True)
log['kepek'].append(dict(fajl='A902_Cam02_tomeg_P902_24A_v1.png', mp=round(time.time() - t, 1)))
# 3) felülnézeti ellenőrző (ortho), a tömbökkel – dokumentáció
cd = bpy.data.cameras.new('JEL_felul_cam'); cd.type = 'ORTHO'; cd.ortho_scale = 8.4
fc = bpy.data.objects.new('JEL_felul_cam', cd); col.objects.link(fc); fc.location = (6.6, 6.2, 9.0); fc.rotation_euler = (0, 0, 0)
felso = [o for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render and o.name not in col.objects and
         min((o.matrix_world @ Vector(c)).z for c in o.bound_box) >= 2.80]
for o in felso: o.hide_render = True
sc.camera = fc; r.resolution_x, r.resolution_y = 1400, 1000; r.filepath = os.path.join(OUT, 'A902_Cam02_tomeg_P902_24A_felulnezet_v1.png'); bpy.ops.render.render(write_still=True)
log['kepek'].append(dict(fajl='A902_Cam02_tomeg_P902_24A_felulnezet_v1.png', megjegyzes=f'{len(felso)} mennyezeti elem rejtve'))
json.dump(log, open(os.path.join(OUT, 'tomeg_cam02_log_v1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ')
