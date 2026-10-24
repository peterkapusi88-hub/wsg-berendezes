# =====================================================================================
# A-811 / A-812 – Blender-alapmodell építése a tervgeometriából (ELŐZETES, 2026-10-24, Claude)
# Bemenet : 03_blender/geometry_A811_A812/<LAKÁS>_geometria_ELOZETES.json  (a8_geometria.py kimenete)
#           01_alaprajzok/villamos_kiallasok/<LAKÁS>_villamos.json           (kiállás-réteg)
#           03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend         (CSAK olvasva: közös anyagok átvétele)
# Kimenet : 03_blender/WSG_<LAKÁS>_alaprajz_ELOZETES_20261024.blend  (új fájl)
#           03_blender/geometry_lock_<LAKÁS>.json                     (lock a validátor v2-höz)
#           03_blender/geometry_A811_A812/<LAKÁS>_kiallas_reteg_ellenorzes.json
# Tartalom: falak, pillérek, aknák, szemöldökök, mennyezet, padló (helyiségenként + küszöbök + ablakmélyedés),
#   beltéri ajtók (tok + csukott lap), homlokzati üvegfalak (profilok + üvegtáblák), erkély (ELŐZETES), kamerák,
#   semleges renderbeállítás, kiállás-réteg (renderben rejtve). Bútor, szaniter, konyha NINCS.
# Élő fájl (~/Downloads/WSG_A902_stilusok.blend): NEM érinti. Az A-902 v2b fájlt csak olvassa.
# Futtatás (bpy 5.2.3), CSAK KÉZZEL:
#   WSG_KEZI_FUTTATAS=1 WSG_LAKAS=A811 python3 -c "import sys,bpy; sys.argv=['x','<repo>']; exec(open('<ez a fájl>').read())"
# =====================================================================================
import os as _os
if _os.environ.get('WSG_KEZI_FUTTATAS') != '1':
    raise SystemExit('Csak kézi futtatás: WSG_KEZI_FUTTATAS=1')
import bpy, bmesh, json, os, sys, math, datetime

REPO = sys.argv[1]
L = _os.environ.get('WSG_LAKAS', 'A811'); assert L in ('A811', 'A812')
B = os.path.join(REPO, '03_blender'); GD = os.path.join(B, 'geometry_A811_A812')
G = json.load(open(os.path.join(GD, f'{L}_geometria_ELOZETES.json'), encoding='utf-8'))
VJ = os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', f'{L}_villamos.json')
A902 = os.path.join(B, 'WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend')
OUT = os.path.join(B, f'WSG_{L}_alaprajz_ELOZETES_20261024.blend')
LOCK = os.path.join(B, f'geometry_lock_{L}.json')
H = G['H']

bpy.ops.wm.read_factory_settings(use_empty=True)
sc = bpy.context.scene; sc.name = f'WSG_{L}'
sc.unit_settings.system = 'METRIC'; sc.unit_settings.length_unit = 'METERS'

# ---------------------------------------------------------------- anyagok: a közöseket az A-902 v2b-ből vesszük át (azonos megjelenés)
KOZOS = ['Fal_feher', 'Plafon_feher', 'Uveg', 'v2b_nyilaszaro_profil_belul_feher', 'v2b_belteri_ajtolap_vilagosszurke',
         'v2b_belteri_ajtotok_szurke', 'v2b_bejarati_ajto_belul_feher', 'v2_greslap_vilagosszurke', 'v2_korlat_antracit',
         'v2_parketta_GreyTreviso_EL2184_foto', 'v2_furdo_kohatasu_vilagos_meleg_szurke']
with bpy.data.libraries.load(A902, link=False) as (src, dst):
    dst.materials = [m for m in src.materials if m in KOZOS]
MAT = {m.name: m for m in bpy.data.materials}
assert all(k in MAT for k in KOZOS), [k for k in KOZOS if k not in MAT]
# parketta: Egger Grey Soria Oak EL2065 (A-811/A-812) – az A-902 eljárási anyag másolata, melegebb szürke tónussal (BECSLÉS)
park = MAT['v2_parketta_GreyTreviso_EL2184_foto'].copy(); park.name = 'A8_parketta_GreySoria_EL2065_BECSLES'
for n in park.node_tree.nodes:
    if n.type == 'VALTORGB':
        e = n.color_ramp.elements; e[0].color = (0.150, 0.138, 0.124, 1); e[-1].color = (0.232, 0.215, 0.195, 1)
park['forras'] = 'Egger EL2065 Grey Soria Oak (burkolatkiosztási terv); tónus: az Egger leírása szerint meleg szürke – helyszíni fotó nélkül BECSLÉS'
bpy.data.materials.remove(MAT['v2_parketta_GreyTreviso_EL2184_foto'])
ker = MAT['v2_furdo_kohatasu_vilagos_meleg_szurke']; ker.name = 'A8_keramia_GlitchSalt_60x60_BECSLES'
ker['forras'] = 'Glitch Salt matt 60×60 (03285A), burkolatkiosztási terv; tónus BECSLÉS'
MAT = {m.name: m for m in bpy.data.materials}
M_FAL, M_PLAF, M_UVEG = MAT['Fal_feher'], MAT['Plafon_feher'], MAT['Uveg']
M_PROF, M_LAP, M_TOK, M_BEJ = (MAT['v2b_nyilaszaro_profil_belul_feher'], MAT['v2b_belteri_ajtolap_vilagosszurke'],
                               MAT['v2b_belteri_ajtotok_szurke'], MAT['v2b_bejarati_ajto_belul_feher'])
M_PADLO = {'parketta': park, 'keramia': ker}
M_GRES, M_KORL = MAT['v2_greslap_vilagosszurke'], MAT['v2_korlat_antracit']


def coll(name, parent=None):
    c = bpy.data.collections.new(name); (parent or sc.collection).children.link(c); return c
C_FAL, C_NY, C_P, C_E, C_BU = (coll(f'{L}_Falak'), coll(f'{L}_Nyilaszarok'), coll(f'{L}_Padlo'),
                               coll(f'{L}_Erkely_ELOZETES'), coll(f'{L}_Butor'))
C_BU['megj'] = 'üres: a stílusrétegek (Stil_*) és bútorok ide/külön gyűjteménybe kerülnek'


def box(name, b, mat, c, props=None):
    x0, y0, z0, x1, y1, z1 = b
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    f = [(0, 3, 2, 1), (4, 5, 6, 7), (0, 1, 5, 4), (1, 2, 6, 5), (2, 3, 7, 6), (3, 0, 4, 7)]
    me = bpy.data.meshes.new(name); me.from_pydata(v, [], f); me.update()
    o = bpy.data.objects.new(name, me); c.objects.link(o); me.materials.append(mat)
    for k, val in (props or {}).items(): o[k] = val
    return o


# ---------------------------------------------------------------- falak, aknák, szemöldökök, mennyezet
for n, r in G['walls'].items():
    box(n, [r[0], r[1], 0, r[2], r[3], H], M_FAL, C_FAL, {'statusz': 'TERV SZERINT', 'forras': 'vektoros falsáv'})
for n, r in G['aknak'].items():
    box(n, [r[0], r[1], 0, r[2], r[3], H], M_FAL, C_FAL, {'statusz': 'TERV SZERINT', 'megj': 'gépészeti akna / tömb – nem használható tér'})
for n, b in G['szemoldok'].items():
    box(n, b, M_FAL, C_FAL, {'statusz': 'TERV SZERINT (nyílásmagasság a rajzi feliratból)'})
for i, r in enumerate(G['plafon']):
    box(f'Plafon_{"ABCDEFG"[i]}', [r[0], r[1], H, r[2], r[3], H + 0.25], M_PLAF, C_FAL)

# ---------------------------------------------------------------- padló: helyiségenként, küszöbök, ablakmélyedés
for k, s in G['szobak'].items():
    for i, r in enumerate(s['r']):
        n = f'P_{k}' + (f'_{i + 1}' if len(s['r']) > 1 else '')
        box(n, [r[0], r[1], -0.02, r[2], r[3], 0.0], M_PADLO[s['padlo']], C_P, {'helyiseg': s['nev'], 'padlo': G['padloanyag'][s['padlo']]})
for n, q in G['kuszob'].items():
    r = q['r']; box(n, [r[0], r[1], -0.02, r[2], r[3], 0.0], M_PADLO[q['anyag']], C_P, {'megj': 'padló az ajtónyílásban'})
for n, w in G['ablakok'].items():
    (f0, f1), (b0, b1), (x0, x1) = w['f'], w['b'], w['fal']
    box(f'P_ablakmelyedes_{n}', [b1, f0, -0.02, x1, f1, 0.0], park, C_P, {'megj': 'padló a tok és a belső falsík között (a megvalósulási terv m²-e ezt beszámítja)'})

# ---------------------------------------------------------------- beltéri ajtók: tok + csukott lap (mint az A-902 v2b-ben)
def door_boxes(axis, a0, a1, w0, w1, h=2.10):
    wc = (w0 + w1) / 2
    if axis == 'x':
        return {'tok_b': [a0, w0, 0, a0 + .03, w1, h], 'tok_j': [a1 - .03, w0, 0, a1, w1, h],
                'tok_f': [a0, w0, h - .03, a1, w1, h], 'lap': [a0 + .03, wc - .02, 0, a1 - .03, wc + .02, h - .02]}
    return {'tok_b': [w0, a0, 0, w1, a0 + .03, h], 'tok_j': [w0, a1 - .03, 0, w1, a1, h],
            'tok_f': [w0, a0, h - .03, w1, a1, h], 'lap': [wc - .02, a0 + .03, 0, wc + .02, a1 - .03, h - .02]}
for n, a in G['ajtok'].items():
    bej = n == 'Ajto_bejarat'
    for part, b in door_boxes(a['fal'], a['nyilas'][0], a['nyilas'][1], a['fal_sik'][0], a['fal_sik'][1], a['magassag']).items():
        m = M_BEJ if bej else (M_LAP if part == 'lap' else M_TOK)
        box(f'{n}_{part}', b, m, C_NY, {'nevleges': a['nevleges'], 'statusz': 'TERV SZERINT; szín: az A-902 fotója alapján feltételezve' if not bej else 'TERV SZERINT'})

# ---------------------------------------------------------------- homlokzati üvegfalak: alsó/felső tok, profilok (az üvegek közti tömör sávok), üvegtáblák
for n, w in G['ablakok'].items():
    (f0, f1), (b0, b1), Hn = w['f'], w['b'], w['Hn']; bc = (b0 + b1) / 2
    box(f'{n}_also', [b0, f0, 0, b1, f1, 0.05], M_PROF, C_NY)
    box(f'{n}_felso', [b0, f0, Hn - 0.05, b1, f1, Hn], M_PROF, C_NY)
    edges = [f0] + [v for g in w['uvegek'] for v in g] + [f1]
    for i in range(0, len(edges), 2):
        a0, a1 = edges[i], edges[i + 1]
        if a1 - a0 > 0.004: box(f'{n}_profil{i // 2}', [b0, a0, 0, b1, a1, Hn], M_PROF, C_NY, {'megj': 'tok/szárnyprofil vagy osztó (rajzi vonalakból)'})
    for i, g in enumerate(w['uvegek']):
        box(f'{n}_uveg{i}', [bc - 0.014, g[0], 0.05, bc + 0.014, g[1], Hn - 0.05], M_UVEG, C_NY)

# ---------------------------------------------------------------- erkély (ELŐZETES): lemez, korlát, osztó
E = G['erkely']; ez = E['z']
for i, r in enumerate(E['lapok']):
    box(f'Erkely_lemez_{i + 1}', [r[0], r[1], ez - 0.20, r[2], r[3], ez], M_GRES, C_E, {'statusz': 'ELŐZETES – kontúr a rajzból, szint nem igazolt'})
# a lemez a homlokzati üvegfal tokjáig fut (ne legyen rés az üveg előtt)
for n, w in G['ablakok'].items():
    if w['fal'][0] < 0 and w['b'][0] < 0:
        box(f'Erkely_lemez_ablak_elott_{n}', [-0.475, w['f'][0], ez - 0.20, w['b'][0], w['f'][1], ez], M_GRES, C_E, {'statusz': 'ELŐZETES'})


def korlat(name, irany, c, a0, a1, z0, hk=1.10):
    bm = bmesh.new()
    def kocka(x0, y0, zz0, x1, y1, zz1):
        r = bmesh.ops.create_cube(bm, size=1.0)
        for v in r['verts']:
            v.co.x = x0 if v.co.x < 0 else x1; v.co.y = y0 if v.co.y < 0 else y1; v.co.z = zz0 if v.co.z < 0 else zz1
    t = 0.02
    def seg(p0, p1, zz0, zz1, w=0.04):   # a vonal mentén futó rúd
        if irany == 'x': kocka(c - w / 2, p0, zz0, c + w / 2, p1, zz1)
        else: kocka(p0, c - w / 2, zz0, p1, c + w / 2, zz1)
    seg(a0, a1, z0 + hk - 0.04, z0 + hk)            # kapaszkodó
    seg(a0, a1, z0 + 0.06, z0 + 0.10)                # alsó rúd
    n = max(1, int((a1 - a0) / 0.12))
    for i in range(n + 1):                            # függőleges pálcák 12 cm-enként
        p = a0 + (a1 - a0) * i / n
        if irany == 'x': kocka(c - t / 2, p - t / 2, z0 + 0.06, c + t / 2, p + t / 2, z0 + hk - 0.04)
        else: kocka(p - t / 2, c - t / 2, z0 + 0.06, p + t / 2, c + t / 2, z0 + hk - 0.04)
    me = bpy.data.meshes.new(name); bm.to_mesh(me); bm.free()
    o = bpy.data.objects.new(name, me); C_E.objects.link(o); me.materials.append(M_KORL)
    o['statusz'] = 'ELŐZETES – típus és magasság NEM IGAZOLT (az A-902 tetőterasz-korlátjához hasonló pálcás korlát feltételezve)'
    return o
for i, (irany, c, a0, a1) in enumerate(E['korlat']):   # c = a korlát tengelye (állandó x vagy y), a0..a1 a futása
    korlat(f'Erkely_korlat_{i + 1}', irany, c, min(a0, a1), max(a0, a1), ez)
for i, r in enumerate(E['valaszfal']):
    box(f'Erkely_oszto_{i + 1}', [r[0], r[1], ez, r[2], r[3], ez + 1.10], M_FAL, C_E, {'statusz': 'ELŐZETES – a rajzon sraffozott osztó; magasság NEM IGAZOLT (1,10 m feltételezve)'})

# ---------------------------------------------------------------- kamerák
def kamera(name, loc, cel, lens=20.0):
    cd = bpy.data.cameras.new(name); cd.lens = lens; cd.sensor_width = 36.0; cd.sensor_height = 24.0
    cd.clip_start = 0.1; cd.clip_end = 200.0
    o = bpy.data.objects.new(name, cd); sc.collection.objects.link(o)
    dx, dy, dz = cel[0] - loc[0], cel[1] - loc[1], cel[2] - loc[2]
    o.location = loc
    o.rotation_euler = (round(math.pi / 2 + math.atan2(dz, math.hypot(dx, dy)), 4), 0.0, round(math.atan2(-dx, dy), 4))
    return o
for n, k in G['kamerak'].items():
    o = kamera(n, k['loc'], k['cel']); o['statusz'] = k['statusz']
# felülnézetek: a lakás + erkély befoglalója
xs = [v for r in list(G['walls'].values()) + E['lapok'] for v in (r[0], r[2])]; ys = [v for r in list(G['walls'].values()) + E['lapok'] for v in (r[1], r[3])]
cx, cy = (min(xs) + max(xs)) / 2, (min(ys) + max(ys)) / 2; sx, sy = max(xs) - min(xs), max(ys) - min(ys)
for n, s in (('Cam_01_Felulnezet', 1.06), ('Cam_06_Alaprajz_lakas', 1.02)):
    cd = bpy.data.cameras.new(n); cd.type = 'ORTHO'; cd.ortho_scale = round(max(sx, sy) * s, 2); cd.clip_start = 0.1; cd.clip_end = 200.0
    cd.sensor_width = 36.0; cd.sensor_height = 24.0
    o = bpy.data.objects.new(n, cd); sc.collection.objects.link(o); o.location = (round(cx, 3), round(cy, 3), 40.0)
    o['statusz'] = 'ellenőrző felülnézet' if n.startswith('Cam_01') else 'ellenőrző alaprajz (kiállás-réteggel)'
sc.camera = bpy.data.objects['Cam_02_Nappali_erkely']

# ---------------------------------------------------------------- render: semleges (a B fázis referenciája, mint az A-902 alapképein)
r = sc.render; vs = sc.view_settings
r.engine = 'BLENDER_EEVEE'; r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, 100
r.image_settings.file_format = 'PNG'
sc.eevee.use_raytracing = True; sc.eevee.taa_render_samples = 32   # mint az A-902 v2b-ben (sugárkövetés nélkül a beltér egyenletesen „kivilágosodik”)
vs.view_transform = 'AgX'; vs.look = 'AgX - Medium High Contrast'; vs.exposure = 0.75; vs.gamma = 1.0
w = bpy.data.worlds.new('Vilag_semleges'); sc.world = w; w.use_nodes = True
bg = w.node_tree.nodes['Background']; bg.inputs['Color'].default_value = (0.86, 0.88, 0.92, 1); bg.inputs['Strength'].default_value = 1.0

# ---------------------------------------------------------------- kiállás-réteg (az A-902 add_kiallas_reteg.py logikája, lakásra paraméterezve)
D = json.load(open(VJ, encoding='utf-8'))
ALAP_Z = {'kapcsolo': 1.10, 'dugalj': 0.30, 'gyengearamu_aljzat': 0.30, 'antenna_tv_aljzat': 0.30, 'termosztat': 1.50,
          'hangjelzo_vagy_erzekelo': 2.20, 'kaputelefon_belteri': 1.50, 'kezelo_billentyuzet': 1.50, 'BK_doboz': 1.50,
          'lakaselosztó': 1.60, 'R_jelu_kiallas': 2.55, 'ventilator_kiallas': 2.30, 'fali_lampakiallas': 2.00,
          'fix_bekotes': 0.60, 'bejarati_ajto_eszkoz': 2.05, 'EPH_csatlakozo': 0.30, 'csengo_kulso': 1.40}
ALM = ({'01 ELŐTÉR': 2.40, '08 WC': 2.40, '06.1 FÜRDŐ': 2.40, '06.2 FÜRDŐ': 2.40} if L == 'A811' else
       {'01 ELŐTÉR': 2.50, '06.1 FÜRDŐ (HTH)': 2.40, '06.2 FÜRDŐ': 2.40, '08/09 FÜRDŐ': 2.40})
ALM_FORRAS = ('a rajz zöld felirata (A-811 WC: „imp. gk. álm. as.: +2,40 m”); az előtérben és a fürdőkben Péter átvételi összesítője (min. 2,40 m)' if L == 'A811'
              else 'a rajz zöld felirata (A-812 előtér: „gk. álm. as.: +2,50 m”); a fürdőkben Péter átvételi összesítője (min. 2,40 m)')
CSOP = {'mennyezeti_lampakiallas': ('VK_ML_mennyezeti_lampa', (0.10, 0.30, 1.00, 1)), 'fali_lampakiallas': ('VK_FL_fali_lampa', (0.65, 0.10, 0.80, 1)),
        'kapcsolo': ('VK_K_kapcsolo', (0.05, 0.60, 0.10, 1)), 'dugalj': ('VK_D_dugalj', (1.00, 0.45, 0.00, 1)),
        'gyengearamu_aljzat': ('VK_G_informatika_TV', (0.50, 0.28, 0.05, 1)), 'antenna_tv_aljzat': ('VK_G_informatika_TV', (0.50, 0.28, 0.05, 1)),
        'termosztat': ('VK_T_termosztat', (0.40, 0.40, 0.40, 1)), 'R_jelu_kiallas': ('VK_R_redony', (0.00, 0.65, 0.75, 1)),
        'ventilator_kiallas': ('VK_V_ventilator', (0.00, 0.45, 0.45, 1))}
EGYEB = ('VK_S_riaszto_kaputelefon_egyeb', (0.85, 0.00, 0.35, 1)); HF = ('VK_HF_hutes_futes_mezo_NEM_FURUNK', (0.25, 0.35, 1.00, 1))
fo = coll(f'{L}_Villamos_TERV'); fo.hide_render = True
fo['forras'] = f'01_alaprajzok/villamos_kiallasok/{L}_villamos.json'; fo['statusz'] = 'TERV SZERINT – helyszínen ellenőrizendő; a z érték, ahol nincs a rajzon, becslés'
alg, anyagok = {}, {}
def gyujt(nev):
    if nev not in alg: alg[nev] = coll(nev, fo)
    return alg[nev]
def anyag(nev, rgba):
    if nev not in anyagok:
        m = bpy.data.materials.new('VK_' + nev); m.diffuse_color = rgba; m.use_nodes = True
        m.node_tree.nodes['Principled BSDF'].inputs['Base Color'].default_value = rgba; anyagok[nev] = m
    return anyagok[nev]
def jelolo(nev, cx, cy, cz, sx, sy, sz, kor=False, n=16):
    if kor:
        v = [(sx * math.cos(2 * math.pi * i / n), sx * math.sin(2 * math.pi * i / n), z) for z in (-sz / 2, sz / 2) for i in range(n)]
        f = [tuple(range(n - 1, -1, -1)), tuple(range(n, 2 * n))] + [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
    else:
        x0, x1, y0, y1, z0, z1 = -sx / 2, sx / 2, -sy / 2, sy / 2, -sz / 2, sz / 2
        v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
        f = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
    me = bpy.data.meshes.new(nev); me.from_pydata(v, [], f); me.update()
    o = bpy.data.objects.new(nev, me); o.location = (cx, cy, cz); return o
szam = lambda v: isinstance(v, (int, float))
falak = []
for o in C_FAL.objects:
    if o.name.startswith('Plafon') or 'szemoldok' in o.name: continue
    p = [o.matrix_world @ v.co for v in o.data.vertices]
    falak.append((min(q.x for q in p), min(q.y for q in p), max(q.x for q in p), max(q.y for q in p)))
def falsik_tav(x, y):
    best = (99, (x, y))
    for a, b, c, d in falak:
        px, py = min(max(x, a), c), min(max(y, b), d); dd = math.hypot(x - px, y - py)
        if dd < best[0]: best = (dd, (px, py))
    return best
szobak = [r for s in G['szobak'].values() for r in s['r']]
ell = dict(lakas=G['lakas'], jelolok=0, tipusonként={}, falra_illesztve=[], kulso_homlokzaton=[], mennyezet_kivul=[], almennyezet=dict(magassag=ALM, forras=ALM_FORRAS))
for k in D['kiallasok']:
    t = k['tipus']; gnev, rgba = CSOP.get(t, EGYEB)
    x = k['doboz_x_m'] if szam(k.get('doboz_x_m')) else k['x_m']; y = k['doboz_y_m'] if szam(k.get('doboz_y_m')) else k['y_m']
    cimke = (k.get('aramkor') or k.get('kod') or '').replace(',', '')
    nev = f"VK_{k['azonosito']}" + (f'_{cimke}' if cimke else '')
    if t == 'mennyezeti_lampakiallas':
        zz = ALM.get(k['helyiseg'], H); z = zz - 0.012
        zf = f'álmennyezet alatt ({zz:.2f} m; {ALM_FORRAS})' if k['helyiseg'] in ALM else f'mennyezet ({H} m, lock)'
        o = jelolo(nev, x, y, z, 0.07, 0, 0.02, kor=True)
        if not any(r[0] <= x <= r[2] and r[1] <= y <= r[3] for r in szobak): ell['mennyezet_kivul'].append(k['azonosito'])
    else:
        if szam(k.get('magassag_m')): z, zf = float(k['magassag_m']), 'rajz („m=…”)'
        else: z, zf = ALAP_Z.get(t, 1.0), 'BECSLÉS (a rajzon nincs magasság)'
        il = None
        if t not in ('R_jelu_kiallas',):
            dd, (px, py) = falsik_tav(x, y)
            if 'ERKÉLY' in k['helyiseg'] or t == 'csengo_kulso':
                if dd > 0.06: ell['kulso_homlokzaton'].append([k['azonosito'], t, round(dd, 3)])
            elif dd > 0.06:
                ell['falra_illesztve'].append([k['azonosito'], t, round(dd, 3)]); il = (x, y, round(dd * 100)); x, y = px, py
        o = jelolo(nev, x, y, z, 0.08, 0.08, 0.08)
        if il: o['x_terv'], o['y_terv'], o['falra_illesztve_cm'] = il
    o.color = rgba; o.data.materials.append(anyag(gnev, rgba))
    for kk in ('azonosito', 'tipus', 'helyiseg', 'aramkor', 'kod', 'statusz', 'forras'): o[kk] = str(k.get(kk, ''))
    o['z_m'] = round(z, 3); o['z_forras'] = zf
    gyujt(gnev).objects.link(o); ell['jelolok'] += 1; ell['tipusonként'][t] = ell['tipusonként'].get(t, 0) + 1
hc = gyujt(HF[0]); hm = anyag(HF[0], HF[1])
for z in D['hutes_futes_zonak']:
    x0, y0, x1, y1 = z['x_min'], z['y_min'], z['x_max'], z['y_max']; zz = H - 0.005; wd = 0.025
    db = [jelolo(f"VK_{z['azonosito']}_keret_a", (x0 + x1) / 2, y0, zz, x1 - x0, wd, 0.006), jelolo(f"VK_{z['azonosito']}_keret_f", (x0 + x1) / 2, y1, zz, x1 - x0, wd, 0.006),
          jelolo(f"VK_{z['azonosito']}_keret_b", x0, (y0 + y1) / 2, zz, wd, y1 - y0, 0.006), jelolo(f"VK_{z['azonosito']}_keret_j", x1, (y0 + y1) / 2, zz, wd, y1 - y0, 0.006)]
    for i, (a, b) in enumerate((((x0, y0), (x1, y1)), ((x0, y1), (x1, y0)))):
        o = jelolo(f"VK_{z['azonosito']}_atlo{i + 1}", (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, zz, math.dist(a, b), wd, 0.006)
        o.rotation_euler[2] = math.atan2(b[1] - a[1], b[0] - a[0]); db.append(o)
    for o in db:
        o.color = HF[1]; o.data.materials.append(hm); o['azonosito'] = z['azonosito']; o['helyiseg'] = z['helyiseg']
        o['statusz'] = z['statusz']; o['megjegyzes'] = 'mennyezeti hűtő-fűtő mező a födémben – ide nem fúrunk'; hc.objects.link(o)
ell['hutes_futes_mezo'] = len(D['hutes_futes_zonak'])

# ---------------------------------------------------------------- mentés + lock
bpy.context.view_layer.update()
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=False)
def wb(o):
    p = [o.matrix_world @ v.co for v in o.data.vertices]
    return [round(min(q[i] for q in p), 3) for i in range(3)] + [round(max(q[i] for q in p), 3) for i in range(3)]
def boxes(c, only_visible=False):
    return {o.name: wb(o) for o in c.objects if o.type == 'MESH' and not (only_visible and o.hide_render)}
def cam_params(o):
    c = o.data
    return dict(tipus=c.type, lens_mm=round(c.lens, 3), sensor_width=round(c.sensor_width, 3), sensor_height=round(c.sensor_height, 3),
                sensor_fit=c.sensor_fit, shift_x=round(c.shift_x, 4), shift_y=round(c.shift_y, 4), clip_start=round(c.clip_start, 4),
                clip_end=round(c.clip_end, 2), ortho_scale=round(c.ortho_scale, 3), dof=bool(c.dof.use_dof),
                loc=[round(v, 4) for v in o.location], rot=[round(v, 4) for v in o.rotation_euler], rot_mode=o.rotation_mode,
                scale=[round(v, 4) for v in o.scale], parent=None, statusz=o.get('statusz', ''))
meta = {}
for n, a in G['ajtok'].items():
    meta[n] = dict(tipus='nyilo', fal=a['fal'], nyilas=a['nyilas'], fal_sik=a['fal_sik'], irany=a['irany'], zsaner=a['zsaner'], r=a['r'],
                   nevleges=a['nevleges'], megj=a.get('megj', ''))
for n, w in G['ablakok'].items():
    for s in w['nyilo']:
        meta[s['nev']] = dict(tipus=s.get('tipus', 'nyilo+fix'), fal='y', nyilas=s['nyilas'], fal_sik=w['fal'], irany=s['irany'], zsaner=s['zsaner'],
                              r=s['r'], megj=f"{n} nyíló szárnya ({w['nevleges']})" + (' – ablak: csak a nyitási negyedkör számít' if s.get('tipus') == 'ablak' else ''))
lock = dict(
    lakas=G['lakas'], gyujtemeny_elotag=L, verzio=f"{G['lakas']} geometria v1 – alaprajz szerinti, ELŐZETES (helyszínen nem mért)",
    datum=datetime.date.today().isoformat(),
    forras=dict(blend=os.path.basename(OUT), geometria=f'geometry_A811_A812/{L}_geometria_ELOZETES.json', terv=f"WGR1 méretezett alaprajz {G['forras']['oldal']}. old. {G['forras']['leptek']} – {G['forras']['rajz']}",
                pdf_sha256=G['forras']['pdf_sha256'], megj=G['meretek']),
    origin=G['koordinata']['origo'], koordinata=G['koordinata'], H=H, H_forras=G['H_forras'], tolerance_m=0.01,
    rooms={k: s['r'] for k, s in G['szobak'].items()}, room_nevek={k: s['nev'] for k, s in G['szobak'].items()},
    room_terv_m2={m['helyiseg']: dict(terv=m['terv_m2'], modell=m['modell_m2'], szobak=m['szobak']) for m in G['m2_osszevetes']},
    walls=boxes(C_FAL), openings=boxes(C_NY), openings_meta=meta, floors=boxes(C_P, True),
    erkely_targyak=boxes(C_E),
    terrace_zones={f'erkely_{i + 1}': dict(r=r, z=E['z'], butorozhato=True, megj='ELŐZETES') for i, r in enumerate(E['lapok'])},
    cameras={o.name: cam_params(o) for o in sc.objects if o.type == 'CAMERA'},
    render=dict(resolution_x=r.resolution_x, resolution_y=r.resolution_y, percentage=r.resolution_percentage, pixel_aspect=[r.pixel_aspect_x, r.pixel_aspect_y],
                scene_camera=sc.camera.name, engine=r.engine, raytracing=sc.eevee.use_raytracing, taa_samples=sc.eevee.taa_render_samples,
                view_transform=vs.view_transform, look=vs.look, exposure=round(vs.exposure, 3), gamma=round(vs.gamma, 3),
                vilag='egyszínű (0,86/0,88/0,92), erősség 1,0; nincs nap és belső lámpa'),
    statusz=dict(falak_nyilasok='TERV SZERINT (vektoros rajz; helyszínen nem mért)', belmagassag=f'{H} m (Kémeri mérés: ' + G['H_forras'].split('mérése ')[1].split(' (')[0] + ')',
                 anyagok='fal, mennyezet, nyílászáró: az A-902 v2b anyagai (fotóval igazolt az A-902-ben); parketta és kerámia: BECSLÉS',
                 erkely='ELŐZETES (kontúr a rajzból; szint, korlát, osztó NEM IGAZOLT)', szaniter='nincs modellezve', konyha='nincs (a lakás konyhabútor nélkül kerül átadásra)'))
json.dump(lock, open(LOCK, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(ell, open(os.path.join(GD, f'{L}_kiallas_reteg_ellenorzes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KESZ', OUT, '| falak', len(lock['walls']), '| nyílászáró-elem', len(lock['openings']), '| padló', len(lock['floors']),
      '| erkély', len(lock['erkely_targyak']), '| kamerák', len(lock['cameras']), '| kiállás', ell['jelolok'], '| HF', ell['hutes_futes_mezo'])
