# A-902 05.1 master – GARDRÓBFAL-JAVASLAT (Péter 22:37: hosszú gardrób az északi fülkében) a Cam_04/Cam_11 nézetben.
# A 02_cam11_ellenorzo_render.py beállításaival; a gardróbfal csak befoglaló-jelölés, nem termék és nem lock.
# Munkamásolaton fut (v2b-1-k10, sha256 028695…c6a1), NEM MENT. Az ágyat, falakat, nyílásokat nem mozdítja:
# a jelölők külön, ideiglenes objektumok. Claude, 2026-10-24.
# Futtatás: Blender -b <munkamasolat.blend> --python 02_cam11_ellenorzo_render.py -- <kimeneti mappa>
import bpy, bmesh, sys, os, json, time, math, hashlib
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; r = sc.render; vs = sc.view_settings
# --- 1. az alapképekkel azonos rejtés (render_alapkepek_v2b1.py) ---
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
for c in bpy.data.collections:
    if c.name.startswith('Stil_') or c.name.startswith('VK_') or c.name == 'A902_Villamos_TERV': c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    if not o.name.startswith(MARAD): o.hide_render = True
FAL_FEHER = bpy.data.materials['Fal_feher']; falanyag_csere = []
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher': falanyag_csere.append([o.name, s.material.name]); s.material = FAL_FEHER
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
# --- 2. Cam_11 JAVASLAT ---
def kamera(nev, loc, rot, lens=20.0):
    if nev in bpy.data.objects: co = bpy.data.objects[nev]
    else:
        cd = bpy.data.cameras.new(nev); co = bpy.data.objects.new(nev, cd); bpy.data.collections['Kamerak_Fenyek'].objects.link(co)
    cd = co.data; cd.type = 'PERSP'; cd.lens = lens; cd.sensor_width = 36.0; cd.sensor_height = 24.0; cd.sensor_fit = 'AUTO'
    cd.shift_x = 0.0; cd.shift_y = 0.0; cd.clip_start = 0.1; cd.clip_end = 200.0; cd.dof.use_dof = False
    co.location = loc; co.rotation_mode = 'XYZ'; co.rotation_euler = rot; return co
CAM11 = dict(loc=(3.20, 6.10, 1.20), rot=(math.pi / 2, 0.0, math.pi / 2), lens=20.0)
c11 = kamera('Cam_11_Master_Panorama', CAM11['loc'], CAM11['rot'], CAM11['lens'])
c11f = kamera('Cam_11_proba_fekve_z090', (3.25, 6.10, 0.90), (math.pi / 2, 0.0, math.pi / 2), 20.0)
# --- 3. jelölők (ideiglenes, csak ebben a futásban) ---
jc = bpy.data.collections.new('JELOLO_Cam11_ellenorzes'); sc.collection.children.link(jc)
def anyag(nev, rgb, alfa, emis):
    m = bpy.data.materials.new(nev)
    try: m.use_nodes = True
    except Exception: pass
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Alpha'].default_value = alfa
    b.inputs['Emission Color'].default_value = (*rgb, 1); b.inputs['Emission Strength'].default_value = emis
    try: m.surface_render_method = 'BLENDED' if alfa < 1 else 'DITHERED'
    except Exception: pass
    m.use_backface_culling = False; return m
MAT = {k: (anyag('JEL_' + k, rgb, 0.30, 0.35), anyag('JEL_' + k + '_el', rgb, 1.0, 2.5)) for k, rgb in
       dict(narancs=(1.0, 0.42, 0.05), sarga=(1.0, 0.85, 0.10), magenta=(0.85, 0.10, 0.75), zold=(0.10, 0.75, 0.25), kek=(0.10, 0.35, 1.0), szurke=(0.45, 0.45, 0.45)).items()}
def doboz(nev, a, b, szin, el=True, felulet=True):
    me = bpy.data.meshes.new(nev); bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0); bm.to_mesh(me); bm.free()
    cx = [(a[i] + b[i]) / 2 for i in range(3)]; sx = [b[i] - a[i] for i in range(3)]
    for v in me.vertices: v.co = [cx[i] + v.co[i] * sx[i] for i in range(3)]
    if felulet:
        o = bpy.data.objects.new(nev, me); jc.objects.link(o); me.materials.append(MAT[szin][0])
    if el:
        e = bpy.data.objects.new(nev + '_el', me.copy() if felulet else me); jc.objects.link(e)
        e.data.materials.clear(); e.data.materials.append(MAT[szin][1])
        w = e.modifiers.new('el', 'WIREFRAME'); w.thickness = 0.012; w.use_even_offset = True; w.use_replace = True
JEL = dict(
    NORDLI_keret_180x202x30=((1.47, 5.10, 0.00), (3.49, 6.90, 0.30), 'narancs'),
    matrac_BECSLES_22cm=((1.48, 5.11, 0.30), (3.48, 6.89, 0.52), 'sarga'),
    fejveg_befoglalo_W260_H100_D8=((3.49, 4.70, 0.00), (3.57, 7.30, 1.00), 'magenta'),
    szabad_sav_60_D=((1.47, 4.50, 0.000), (3.49, 5.10, 0.006), 'zold'),
    szabad_sav_60_E=((1.47, 6.90, 0.000), (3.49, 7.50, 0.006), 'zold'),
    gardrobfal_eszaki_fulke_JAVASLAT_300x290=((0.01, 8.05, 0.00), (3.01, 8.95, 2.90), 'kek'),
    modell_PAX_242_deli_sav=((0.00, 3.45, 0.00), (2.42, 4.02, 2.36), 'szurke'))
for nev, (a, b, s) in JEL.items(): doboz('JEL_' + nev, a, b, s)
# a tervrajz (brosúra + 1:50) szerinti ágyhely kontúrja a padlón – csak jelölés, nem ágyáthelyezés
#doboz('JEL_tervrajz_agyhely_kontur', (1.59, 5.505, 0.0), (3.57, 7.295, 0.012), 'kek', el=True, felulet=False)
# villamos kiállások 05.1 (a VK-réteg rejtett elemei közül csak a 05.1-ben lévők)
VK05 = ('A902-D20', 'A902-D21', 'A902-D22', 'A902-D23', 'A902-D24', 'A902-D25', 'A902-D26', 'A902-K13', 'A902-K14', 'A902-K15', 'A902-K16', 'A902-T02', 'A902-G05', 'A902-ML06')
vk_lathato = []
def vk_mutat(be):
    for c in bpy.data.collections:
        if c.name.startswith('VK_') and c.name != 'VK_HF_hutes_futes_mezo_NEM_FURUNK' or c.name == 'A902_Villamos_TERV': c.hide_render = not be
    for c in bpy.data.collections:
        if c.name.startswith('VK_'):
            for o in c.objects:
                l = be and any(k in o.name for k in VK05); o.hide_render = not l
                if l and o.name not in vk_lathato: vk_lathato.append(o.name)
def jel(be):
    jc.hide_render = not be; vk_mutat(be)
def cam(o): c = o.data; return dict(loc=[round(x, 4) for x in o.location], rot=[round(x, 4) for x in o.rotation_euler], lens=c.lens, sensor=[c.sensor_width, c.sensor_height], fit=c.sensor_fit, clip=[c.clip_start, c.clip_end], shift=[c.shift_x, c.shift_y])
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(),
           cel='KEP-004 – Cam_04 vs Cam_11 összevetés, 05.1 master; JAVASLAT, nem lock', kepek=[], jelolok={k: dict(min=a, max=b) for k, (a, b, s) in JEL.items()},
           falanyag_csere=falanyag_csere, beallitas=dict(motor=r.engine, felbontas=[1600, 1000], minta=128, view='AgX', look=vs.look, expozicio=0.75,
           egbolt='egyszínű (0,86/0,88/0,92), erősség 1,0; nap és belső lámpák nélkül – az alapképekkel azonos'))
for cn, fn, j in [('Cam_04_Master', 'ellenorzes_Cam04_gardrobfal_javaslat_v1.png', True),
                  ('Cam_11_Master_Panorama', 'ellenorzes_Cam11_gardrobfal_javaslat_v1.png', True)]:
    jel(j); sc.camera = bpy.data.objects[cn]; r.filepath = os.path.join(OUT, fn); t = time.time()
    bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cn, fajl=fn, jelolok=j, kamera_parameterek=cam(sc.camera), mp=round(time.time() - t, 1)))
log['vk_jelolok'] = vk_lathato
json.dump(log, open(os.path.join(OUT, 'render_log_gardrobfal_v1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('RENDER KÉSZ')
