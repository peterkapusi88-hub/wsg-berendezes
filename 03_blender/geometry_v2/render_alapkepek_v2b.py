# =====================================================================================
# A-902 v2b – bútor nélküli alapképek a rögzített kamerákból (Astra B fázis bemenete) +
# felülnézeti ellenőrző kép a kiállás-réteggel. 2026-10-24, Claude.
# Csak a betöltött fájl MEMÓRIÁBELI példányán változtat (láthatóság, renderbeállítás); NEM MENT.
# Futtatás háttér-Blenderrel (5.2.3), CSAK KÉZZEL:
#   WSG_KEZI_FUTTATAS=1 <Blender> -b <v2b.blend> --python render_alapkepek_v2b.py -- <kimeneti mappa> [<változat>]
# Változat: „semleges” (alap, a B fázis referenciája) = egyenletes szórt nappali fény (egyszínű égbolt), nap és belső
#   lámpák nélkül, AgX Medium High Contrast, expozíció +0,75 – a 2026-10-24-i expozíció-sorozat alapján a falak
#   fehérek és semlegesek (sRGB ~200–206), a padló szürkésbarna (~143–146). „lock” = a lock render-beállításai
#   (égbolt-textúra, nap, belső lámpák, expozíció −1,0) – kékes, sötét; csak összehasonlításra.
# =====================================================================================
import os as _os
if _os.environ.get('WSG_KEZI_FUTTATAS') != '1':
    raise SystemExit('Csak kézi futtatás: WSG_KEZI_FUTTATAS=1')
import bpy, sys, os, json, time

args = sys.argv[sys.argv.index('--') + 1:] if '--' in sys.argv else []
OUT = args[0]; VALTOZAT = args[1] if len(args) > 1 else 'semleges'
PROBA = _os.environ.get('WSG_PROBA') == '1'   # beállítás-ellenőrzés renderelés nélkül
def kep():
    if not PROBA: bpy.ops.render.render(write_still=True)
os.makedirs(OUT, exist_ok=True)
sc = bpy.context.scene; r = sc.render; vs = sc.view_settings
# beépített szaniter marad (a lakás része); minden más bútor és stílusréteg rejtve
MARAD = ('Kad', 'Kezmoso', 'Mosdo_', 'WC_', 'Zuhany', 'Torolkozoszarito')
for c in bpy.data.collections:
    if c.name.startswith('Stil_'): c.hide_render = True
for o in bpy.data.collections['A902_Butor'].objects:
    if not o.name.startswith(MARAD): o.hide_render = True
vk = bpy.data.collections.get('A902_Villamos_TERV')
if vk: vk.hide_render = True
# A stílusréteg anyaga falon is maradhatott: a v2b fájlban a nappali nyugati fala (Fal_05_1_nappali_0) és a 05.1 északi
# fala (Kulso_E_05_1_0) Zenit-tapétát (Z_tapeta_greige) hordoz (a PR #8 ellenőrzése, 2026-10-24). Az alapképen minden fal a
# meglévő fehér festés: a renderhez Fal_feher-re cseréljük – csak a memóriában, a fájlt nem mentjük.
FAL_FEHER = bpy.data.materials['Fal_feher']; falanyag_csere = []
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): continue
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher':
            falanyag_csere.append([o.name, s.material.name]); s.material = FAL_FEHER

def lock_beallitas():
    r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
    vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.exposure = -1.0; vs.gamma = 1.0
    r.image_settings.file_format = 'PNG'
    if VALTOZAT == 'semleges':
        nt = sc.world.node_tree; bg = nt.nodes['Background']
        for l in list(nt.links):
            if l.to_node == bg and l.to_socket.name == 'Color': nt.links.remove(l)
        bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0
        for o in bpy.data.objects:
            if o.type == 'LIGHT': o.hide_render = True
        vs.exposure = 0.75

log = dict(blender=bpy.app.version_string, fajl=bpy.data.filepath, valtozat=VALTOZAT, kepek=[],
           rejtve=dict(stilusretegek=[c.name for c in bpy.data.collections if c.name.startswith('Stil_')],
                       butor=sum(1 for o in bpy.data.collections['A902_Butor'].objects if o.hide_render),
                       megtartott_szaniter=sorted(o.name for o in bpy.data.collections['A902_Butor'].objects if not o.hide_render)),
           fenyek=None, falanyag_csere=falanyag_csere)
KAM = [('Cam_02_Nappali_terasz', 'A902_Alap-v2b_blender_02_nappali-terasz.png'),
       ('Cam_03_Etkezo_konyha', 'A902_Alap-v2b_blender_03_etkezo-konyha.png'),
       ('Cam_04_Master', 'A902_Alap-v2b_blender_04_master.png')]
lock_beallitas()
log['fenyek'] = sorted(o.name for o in bpy.data.objects if o.type == 'LIGHT' and not o.hide_render)
log['beallitas'] = dict(motor=r.engine, felbontas=[r.resolution_x, r.resolution_y], view=vs.view_transform, look=vs.look, expozicio=vs.exposure,
                       egbolt='egyszínű (0,86/0,88/0,92), erősség 1,0' if VALTOZAT == 'semleges' else 'Nishita égbolt-textúra, 0,15')
for cam, fn in KAM:
    sc.camera = bpy.data.objects[cam]; r.filepath = os.path.join(OUT, fn); t = time.time()
    kep()
    log['kepek'].append(dict(kamera=cam, fajl=fn, mp=round(time.time() - t, 1)))

# felülnézet: mennyezet rejtve, kiállás-réteg látható, tárgyszínek (Workbench, lapos fény)
if vk: vk.hide_render = False
for o in bpy.data.collections['A902_Falak'].objects:
    if o.name.startswith('Plafon'): o.hide_render = True
    else: o.color = (0.18, 0.18, 0.18, 1)          # csak a felülnézethez: sötét fal, világos padló (nem mentjük)
for o in bpy.data.collections['A902_Nyilaszarok'].objects: o.color = (0.55, 0.62, 0.70, 1)
for o in bpy.data.collections['A902_Padlo'].objects: o.color = (0.97, 0.97, 0.97, 1)
for o in bpy.data.collections['A902_Terasz_v2_ELOZETES'].objects: o.color = (0.85, 0.88, 0.85, 1)
r.engine = 'BLENDER_WORKBENCH'
sh = sc.display.shading; sh.light = 'FLAT'; sh.color_type = 'OBJECT'
vs.view_transform = 'Standard'; vs.look = 'None'; vs.exposure = 0.0
r.resolution_x, r.resolution_y = 2400, 1500
sc.camera = bpy.data.objects['Cam_06_Alaprajz_lakas']
fn = 'A902_Alap-v2b_blender_06_alaprajz-kiallasok.png'; r.filepath = os.path.join(OUT, fn); t = time.time()
kep()
log['kepek'].append(dict(kamera='Cam_06_Alaprajz_lakas', fajl=fn, mp=round(time.time() - t, 1), megjegyzes='Workbench, tárgyszín, mennyezet rejtve'))
json.dump(log, open(os.path.join(OUT, 'render_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('RENDER KÉSZ', json.dumps(log, ensure_ascii=False))
