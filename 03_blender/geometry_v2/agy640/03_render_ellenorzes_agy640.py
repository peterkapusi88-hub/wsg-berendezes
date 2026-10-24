# A-902 05.1 master – ellenőrzőképek az ágy y 6,40-es tengelyével: Cam_04, Cam_11 és felülnézet; hozzáférési mérések.
# Az új (agy640) fájlon fut, NEM MENT. A jelölők ideiglenes objektumok, csak ebben a futásban léteznek. Claude, 2026-10-25.
# Futtatás: Blender -b <agy640.blend> --python 03_render_ellenorzes_agy640.py -- <kimeneti mappa>
import bpy, bmesh, sys, os, json, time, math, hashlib, mathutils
OUT = sys.argv[sys.argv.index('--') + 1]; os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; r = sc.render; vs = sc.view_settings
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
MASTER = ('Agy_05_1_', 'Ejjeli_05_1_', 'Szonyeg_05_1_')
for c in bpy.data.collections:
    if c.name.startswith('Stil_') or c.name.startswith('VK_') or c.name == 'A902_Villamos_TERV': c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    o.hide_render = not (o.name.startswith(MARAD) or o.name.startswith(MASTER))
FAL_FEHER = bpy.data.materials['Fal_feher']
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher': s.material = FAL_FEHER
r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
sc.eevee.taa_render_samples = 64
vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.gamma = 1.0; r.image_settings.file_format = 'PNG'
nt = sc.world.node_tree; bg = nt.nodes['Background']
for l in list(nt.links):
    if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0
for o in bpy.data.objects:
    if o.type == 'LIGHT': o.hide_render = True
vs.exposure = 0.75
def bb(o):
    pts = [o.matrix_world @ mathutils.Vector(c) for c in o.bound_box]
    return [min(p[i] for p in pts) for i in range(3)] + [max(p[i] for p in pts) for i in range(3)]
# --- jelölők ---
jc = bpy.data.collections.new('JELOLO_agy640'); sc.collection.children.link(jc)
def anyag(nev, rgb, alfa, emis):
    m = bpy.data.materials.new(nev); m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Alpha'].default_value = alfa
    b.inputs['Emission Color'].default_value = (*rgb, 1); b.inputs['Emission Strength'].default_value = emis
    try: m.surface_render_method = 'BLENDED' if alfa < 1 else 'DITHERED'
    except Exception: pass
    m.use_backface_culling = False; return m
SZ = dict(narancs=(1.0, 0.42, 0.05), magenta=(0.85, 0.10, 0.75), zold=(0.10, 0.75, 0.25), kek=(0.10, 0.35, 1.0), piros=(0.95, 0.05, 0.05), sarga=(1.0, 0.80, 0.0), fekete=(0.02, 0.02, 0.02))
MAT = {k: (anyag('JEL_' + k, rgb, 0.28, 0.3), anyag('JEL_' + k + '_el', rgb, 1.0, 2.5)) for k, rgb in SZ.items()}
def doboz(nev, a, b, szin, el=True, felulet=True, tomor=False):
    me = bpy.data.meshes.new(nev); bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0); bm.to_mesh(me); bm.free()
    cx = [(a[i] + b[i]) / 2 for i in range(3)]; sx = [b[i] - a[i] for i in range(3)]
    for v in me.vertices: v.co = [cx[i] + v.co[i] * sx[i] for i in range(3)]
    if felulet:
        o = bpy.data.objects.new(nev, me); jc.objects.link(o); me.materials.append(MAT[szin][1 if tomor else 0])
    if el:
        e = bpy.data.objects.new(nev + '_el', me.copy() if felulet else me); jc.objects.link(e)
        e.data.materials.clear(); e.data.materials.append(MAT[szin][1])
        w = e.modifiers.new('el', 'WIREFRAME'); w.thickness = 0.012; w.use_even_offset = True; w.use_replace = True
JEL = dict(
    NORDLI_keret_180x202x30=((1.47, 5.50, 0.00), (3.49, 7.30, 0.30), 'narancs'),
    fejveg_befoglalo_W260_H100_D8=((3.49, 5.10, 0.00), (3.57, 7.70, 1.00), 'magenta'),
    szabad_sav_60_D=((1.47, 4.90, 0.000), (3.16, 5.50, 0.006), 'zold'),
    szabad_sav_60_E=((1.47, 7.30, 0.000), (3.16, 7.90, 0.006), 'zold'))
for nev, (a, b, s) in JEL.items(): doboz('JEL_' + nev, a, b, s)
doboz('JEL_tervrajz_agyhely_kontur', (1.59, 5.505, 0.0), (3.57, 7.295, 0.012), 'kek', el=True, felulet=False)
VK05 = ('A902-D20', 'A902-D21', 'A902-D22', 'A902-D23', 'A902-D24', 'A902-D25', 'A902-D26', 'A902-K13', 'A902-K14', 'A902-K15', 'A902-K16', 'A902-T02', 'A902-G05', 'A902-ML06')
def vk_mutat(be):
    for c in bpy.data.collections:
        if (c.name.startswith('VK_') and c.name != 'VK_HF_hutes_futes_mezo_NEM_FURUNK') or c.name == 'A902_Villamos_TERV': c.hide_render = not be
    for c in bpy.data.collections:
        if c.name.startswith('VK_'):
            for o in c.objects: o.hide_render = not (be and any(k in o.name for k in VK05))
# felülnézeti jelölők: kiállások a fal teteje fölött, feliratok
fn = bpy.data.collections.new('JELOLO_felulnezet'); sc.collection.children.link(fn)
KI = {'K14': (3.545, 5.319, 'piros'), 'K13': (3.545, 7.51, 'piros'), 'D22': (3.545, 5.24, 'sarga'), 'D23': (3.545, 5.159, 'sarga'),
      'D21': (3.545, 7.589, 'sarga'), 'D20': (3.545, 7.669, 'sarga'), 'ML06': (1.834, 6.049, 'kek')}
def felulnezet_obj(o): fn.objects.link(o)
for k, (x, y, s) in KI.items():
    me = bpy.data.meshes.new('F_' + k); bm = bmesh.new(); bmesh.ops.create_cube(bm, size=1.0); bm.to_mesh(me); bm.free()
    for v in me.vertices: v.co = (x + v.co[0] * 0.07, y + v.co[1] * 0.07, 2.97 + v.co[2] * 0.02)
    o = bpy.data.objects.new('F_' + k, me); me.materials.append(MAT[s][1]); felulnezet_obj(o)
def felirat(t, x, y, meret=0.11):
    cu = bpy.data.curves.new('T_' + t, 'FONT'); cu.body = t; cu.size = meret; cu.align_x = 'CENTER'
    o = bpy.data.objects.new('T_' + t, cu); o.location = (x, y, 3.0); o.rotation_euler = (0, 0, math.pi / 2)
    cu.materials.append(MAT['fekete'][1]); felulnezet_obj(o)
felirat('K14', 3.36, 5.319); felirat('K13', 3.36, 7.51); felirat('D22/D23', 3.83, 5.20); felirat('D20/D21', 3.83, 7.63)
felirat('ML06', 1.70, 6.049); felirat('Cam_11 (3,20; 6,10)', 2.95, 6.10, 0.09); felirat('agytengely y 6,40', 2.25, 6.40, 0.10)
# Cam_11 iránya: nyíl nyugat felé
doboz('F_Cam11_nyil', (2.70, 6.08, 2.96), (3.20, 6.12, 2.99), 'piros', el=False, tomor=True); jc.objects.unlink(bpy.data.objects['F_Cam11_nyil']); fn.objects.link(bpy.data.objects['F_Cam11_nyil'])
doboz('F_agytengely', (1.50, 6.395, 2.96), (3.50, 6.405, 2.97), 'kek', el=False, tomor=True); jc.objects.unlink(bpy.data.objects['F_agytengely']); fn.objects.link(bpy.data.objects['F_agytengely'])
# felülnézeti kamera (ortho), a mennyezet és a 2,95 m fölötti elemek rejtve csak erre a képre
cd = bpy.data.cameras.new('JEL_felulnezet_cam'); cd.type = 'ORTHO'; cd.ortho_scale = 6.2; cd.clip_start = 0.1; cd.clip_end = 30
fc = bpy.data.objects.new('JEL_felulnezet_cam', cd); jc.objects.link(fc); fc.location = (1.79, 6.30, 9.0); fc.rotation_euler = (0, 0, math.pi / 2)
felso = [o for o in bpy.data.objects if o.type == 'MESH' and not o.hide_render and o.name not in fn.objects and bb(o)[2] >= 2.85]
# --- mérések ---
fej = bb(bpy.data.objects['Agy_05_1_TALLASEN_180x200_fejtamla']); ker = bb(bpy.data.objects['Agy_05_1_TALLASEN_180x200_keret'])
def tav(y, a, b): return round(min(abs(y - a), abs(y - b)), 3) if not (a <= y <= b) else 0.0
mer = dict(agy_keret=[round(v, 3) for v in ker], fejtamla=[round(v, 3) for v in fej], agy_tengely_y=round((ker[1] + ker[4]) / 2, 3),
           kiallasok={k: dict(y=y, fejtamla_szelétol_m=tav(y, fej[1], fej[4]), takarja_a_fejtamla=fej[1] <= y <= fej[4]) for k, (x, y, s) in KI.items() if k != 'ML06'})
for n in ('Ejjeli_05_1_a', 'Ejjeli_05_1_b', 'Ejjeli_05_1_a_lampa', 'Ejjeli_05_1_b_lampa'):
    mer[n] = [round(v, 3) for v in bb(bpy.data.objects[n])]
c11 = bpy.data.objects['Cam_11_Master_Panorama']; c04 = bpy.data.objects['Cam_04_Master']
l11 = c11.matrix_world.translation
mer['cam11'] = dict(loc=[round(v, 3) for v in l11], rot=[round(v, 4) for v in c11.rotation_euler], lens=c11.data.lens,
                    az_agy_alapteruletén=bool(ker[0] <= l11.x <= ker[3] and ker[1] <= l11.y <= ker[4]),
                    tav_az_agytengelytol_m=round(abs(l11.y - (ker[1] + ker[4]) / 2), 3), szem_a_matrac_folott_m=round(l11.z - 0.52, 3))
mer['cam04'] = dict(loc=[round(v, 3) for v in c04.matrix_world.translation], rot=[round(v, 4) for v in c04.rotation_euler], lens=c04.data.lens)
log = dict(blender=bpy.app.version_string, fajl=os.path.basename(bpy.data.filepath), sha256=hashlib.sha256(open(bpy.data.filepath, 'rb').read()).hexdigest(),
           cel='05.1 master – ágy y 6,40 ellenőrzés (bútorréteg); JAVASLAT, PR #15', meresek=mer, kepek=[])
for cn, fnev, nezet in [('Cam_04_Master', 'ellenorzes_Cam04_agy640_v2.png', 'kamera'), ('Cam_11_Master_Panorama', 'ellenorzes_Cam11_agy640_v2.png', 'kamera'),
                        ('JEL_felulnezet_cam', 'ellenorzes_05_1_felulnezet_agy640_v2.png', 'felul')]:
    jc.hide_render = False; vk_mutat(nezet == 'kamera'); fn.hide_render = nezet != 'felul'
    for o in felso: o.hide_render = nezet == 'felul'
    sc.camera = bpy.data.objects[cn]; r.filepath = os.path.join(OUT, fnev); t = time.time()
    bpy.ops.render.render(write_still=True)
    log['kepek'].append(dict(kamera=cn, fajl=fnev, mp=round(time.time() - t, 1)))
json.dump(log, open(os.path.join(OUT, 'render_log_agy640_v2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('RENDER KÉSZ', json.dumps(mer['kiallasok'], ensure_ascii=False))
