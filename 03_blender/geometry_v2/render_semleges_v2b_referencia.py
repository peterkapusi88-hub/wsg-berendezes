# =====================================================================================
# A-902 v2b – SEMLEGES, ALAPRAJZHŰ REFERENCIARENDER (2026-10-24, Claude)
# Státusz: TERV SZERINTI geometria (lock v2b), helyszínen NEM mért. A kép referencia az
# összehasonlító stílusképekhez, nem kivitelezési bizonyíték. Bizonytalan elemek:
# 04_renderek/semleges_v2b/REFERENCIA_KARTYA_A902_Cam02_v2b.md
#
# Mit csinál (csak a MÁSOLATON, a geometriához és a kamerákhoz nem nyúl):
#  - elrejti a régi bútort, a Zenit/Lake Forest réteget, a régi sík teraszt, a narancs JELÖLŐ-ket,
#    a mesterséges fényeket és a napot;
#  - fehér fal és mennyezet (a nyugati válaszfalon maradt Z_tapeta_greige is fehér lesz);
#  - padló: procedurális Egger Grey Treviso Oak EL2184 közelítés (Classic 8/32 4V, 1292×193 mm
#    feltételezett deszka, É–D irány a ME-BAL-045/046 fotók alapján becsülve), azonos dekorú
#    6 cm-es szegőléc külön gyűjteményben (Ref_v2b_szegelyleces);
#  - üveg: átlátszó + Fresnel-tükröződés; ég: egyenletes, semleges, nap nélkül (borult ég),
#    a horizont alatt semleges szürke talaj; portálfények a külső üvegezésekben (zajcsökkentés);
#  - lefuttatja a geometry_validator_v2-t (lock v2b + villamos kiállások), majd renderel.
# Az élő ~/Downloads/WSG_A902_stilusok.blend-hez és a repóbeli .blend-ekhez nem nyúl, nem ment rájuk.
#
# Futtatás (bpy 5.2.3 modul vagy Blender 5.2 háttérben), CSAK kézi indításra:
#   WSG_KEZI_FUTTATAS=1 WSG_BLEND=<v2b MÁSOLAT.blend> WSG_REPO=<repo> WSG_OUT=<kimeneti mappa> \
#   WSG_CAMS=Cam_02_Nappali_terasz[,Cam_03_Etkezo_konyha,...] WSG_PRESET=final|test WSG_EXPOSURE=<EV> \
#   python3 render_semleges_v2b_referencia.py
#   (Blenderrel: WSG_... Blender -b -P render_semleges_v2b_referencia.py)
# Kimenet: <kamera>.png, kamera_parameterek.json, validator_v2b_referencia.json, beallitasok.json
# =====================================================================================
import os
if os.environ.get('WSG_KEZI_FUTTATAS') != '1':
    raise SystemExit('Kézi referenciarender – futtatás csak WSG_KEZI_FUTTATAS=1 mellett.')
import bpy, json, math, runpy, hashlib, time
from mathutils import Vector

BLEND = os.environ['WSG_BLEND']
REPO = os.environ['WSG_REPO']
OUT = os.environ['WSG_OUT']
CAMS = [c for c in os.environ.get('WSG_CAMS', 'Cam_02_Nappali_terasz').split(',') if c]
PRESET = os.environ.get('WSG_PRESET', 'test')
EXPOSURE = float(os.environ.get('WSG_EXPOSURE', '0.0'))
SAVE_BLEND = os.environ.get('WSG_SAVE_BLEND', '0') == '1'
os.makedirs(OUT, exist_ok=True)

LOCK = os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json')
VILL = os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.json')
VALIDATOR = os.path.join(REPO, '03_blender', 'geometry_validator_v2.py')

sha = hashlib.sha256(open(BLEND, 'rb').read()).hexdigest()
bpy.ops.wm.open_mainfile(filepath=BLEND)
sc = bpy.context.scene
log = dict(bemenet=BLEND, bemenet_sha256=sha, preset=PRESET, exposure=EXPOSURE, rejtve=[], anyag=[], uj=[])

# ---------------------------------------------------------------- 1) rejtés (csak render)
for cname in ('A902_Butor', 'Stil_LakeForest', 'Stil_Zenit', 'A902_Terasz', 'Collection'):
    c = bpy.data.collections.get(cname)
    if c:
        c.hide_render = True
        log['rejtve'].append(cname)
for o in bpy.data.objects:
    if o.type == 'LIGHT' and (o.name.startswith('L_') or o.name == 'Nap'):
        o.hide_render = True; log['rejtve'].append(o.name)
    elif o.type == 'MESH' and any(s.material and s.material.name == 'v2_JELOLO_narancs' for s in o.material_slots):
        o.hide_render = True; log['rejtve'].append(o.name)


# ---------------------------------------------------------------- 2) anyagok
def principled(m):
    m.use_nodes = True
    nt = m.node_tree
    b = nt.nodes.get('Principled BSDF')
    return nt, b


def set_flat(name, rgb, rough):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    nt, b = principled(m)
    for l in list(b.inputs['Base Color'].links):
        nt.links.remove(l)
    b.inputs['Base Color'].default_value = (*rgb, 1)
    b.inputs['Roughness'].default_value = rough
    return m


WHITE = (0.82, 0.82, 0.82)          # matt fehér falfesték (albedó ~0,82), semleges
m_fal = set_flat('Fal_feher', WHITE, 0.92)
set_flat('Plafon_feher', WHITE, 0.95)
log['anyag'].append('Fal_feher, Plafon_feher → semleges fehér 0,82')
# a stílusrétegből a falra ragadt tapéta → fehér (a valóságban fehér, IGAZOLT-F)
for o in bpy.data.collections['A902_Falak'].objects:
    for s in o.material_slots:
        if s.material and s.material.name != 'Fal_feher' and not o.name.startswith('Plafon'):
            log['anyag'].append(f'{o.name}: {s.material.name} → Fal_feher')
            s.material = m_fal
set_flat('v2b_nyilaszaro_profil_belul_feher', (0.80, 0.80, 0.79), 0.4)
set_flat('v2b_belteri_ajtolap_vilagosszurke', (0.50, 0.51, 0.52), 0.45)
set_flat('v2b_belteri_ajtotok_szurke', (0.42, 0.43, 0.44), 0.45)


def node(nt, typ, loc=(0, 0), **kw):
    n = nt.nodes.new(typ)
    n.location = loc
    for k, v in kw.items():
        setattr(n, k, v)
    return n


def math_node(nt, op, a=None, b=None, loc=(0, 0)):
    n = node(nt, 'ShaderNodeMath', loc, operation=op)
    for i, v in enumerate((a, b)):
        if v is None:
            continue
        if isinstance(v, (int, float)):
            n.inputs[i].default_value = v
        else:
            nt.links.new(v, n.inputs[i])
    return n.outputs[0]


def mix_rgb(nt, fac, a, b, loc=(0, 0)):
    n = node(nt, 'ShaderNodeMix', loc, data_type='RGBA')
    (nt.links.new(fac, n.inputs[0]) if not isinstance(fac, (int, float)) else n.inputs[0].__setattr__('default_value', fac))
    for idx, v in ((6, a), (7, b)):
        if isinstance(v, tuple):
            n.inputs[idx].default_value = (*v, 1)
        else:
            nt.links.new(v, n.inputs[idx])
    return n.outputs[2]


def white1d(nt, w_socket, loc=(0, 0)):
    n = node(nt, 'ShaderNodeTexWhiteNoise', loc, noise_dimensions='1D')
    nt.links.new(w_socket, n.inputs['W'])
    return n.outputs['Value']


# deszka: 1292 × 193 mm (Egger Classic 8 mm formátum – a konkrét tételen NEM igazolt), hossza É–D (y) irányban
PL_W, PL_L, GROOVE = 0.193, 1.292, 0.0016
C_DARK, C_LIGHT = (0.160, 0.153, 0.143), (0.222, 0.214, 0.201)   # lineáris albedó; átlag ~0,19 (sRGB ~120) – hűvös szürkésbarna


def build_parquet(m):
    m.use_nodes = True
    nt = m.node_tree
    nt.nodes.clear()
    out = node(nt, 'ShaderNodeOutputMaterial', (1400, 0))
    bsdf = node(nt, 'ShaderNodeBsdfPrincipled', (1150, 0))
    nt.links.new(bsdf.outputs[0], out.inputs[0])
    geo = node(nt, 'ShaderNodeNewGeometry', (-1200, 0))
    sep = node(nt, 'ShaderNodeSeparateXYZ', (-1000, 0))
    nt.links.new(geo.outputs['Position'], sep.inputs[0])
    x, y = sep.outputs['X'], sep.outputs['Y']
    xw = math_node(nt, 'DIVIDE', x, PL_W, (-800, 200))
    row = math_node(nt, 'FLOOR', xw, None, (-650, 200))
    u = math_node(nt, 'FRACT', xw, None, (-650, 300))
    roff = white1d(nt, math_node(nt, 'ADD', row, 0.37, (-500, 200)), (-350, 200))
    yy = math_node(nt, 'ADD', y, math_node(nt, 'MULTIPLY', roff, PL_L, (-200, 200)), (-50, 100))
    yl = math_node(nt, 'DIVIDE', yy, PL_L, (100, 100))
    idx = math_node(nt, 'FLOOR', yl, None, (250, 100))
    v = math_node(nt, 'FRACT', yl, None, (250, 0))
    pid = math_node(nt, 'ADD', math_node(nt, 'MULTIPLY', row, 31.17), math_node(nt, 'MULTIPLY', idx, 7.31), (400, 100))
    r1 = white1d(nt, pid, (550, 150))
    r2 = white1d(nt, math_node(nt, 'ADD', pid, 113.7), (550, 50))
    # erezet: hosszanti finom csíkok + nagyobb „katedrális” rajzolat + ritka göcs
    vec = node(nt, 'ShaderNodeCombineXYZ', (400, -200))
    nt.links.new(math_node(nt, 'MULTIPLY', x, 1.0), vec.inputs[0])
    nt.links.new(math_node(nt, 'MULTIPLY', yy, 0.025), vec.inputs[1])
    nt.links.new(math_node(nt, 'MULTIPLY', r2, 40.0), vec.inputs[2])
    fine = node(nt, 'ShaderNodeTexNoise', (600, -200), noise_dimensions='3D')
    fine.inputs['Scale'].default_value = 240.0; fine.inputs['Detail'].default_value = 6.0
    fine.inputs['Roughness'].default_value = 0.62; fine.inputs['Distortion'].default_value = 0.25
    nt.links.new(vec.outputs[0], fine.inputs['Vector'])
    broad = node(nt, 'ShaderNodeTexNoise', (600, -450), noise_dimensions='3D')
    broad.inputs['Scale'].default_value = 22.0; broad.inputs['Detail'].default_value = 3.0
    broad.inputs['Distortion'].default_value = 1.2
    nt.links.new(vec.outputs[0], broad.inputs['Vector'])
    knotv = node(nt, 'ShaderNodeCombineXYZ', (400, -650))
    nt.links.new(math_node(nt, 'MULTIPLY', x, 1.0), knotv.inputs[0])
    nt.links.new(math_node(nt, 'MULTIPLY', yy, 0.35), knotv.inputs[1])
    vor = node(nt, 'ShaderNodeTexVoronoi', (600, -650), feature='F1')
    vor.inputs['Scale'].default_value = 3.2
    nt.links.new(knotv.outputs[0], vor.inputs['Vector'])
    knot = math_node(nt, 'SUBTRACT', 1.0, math_node(nt, 'MULTIPLY', vor.outputs['Distance'], 9.0), (800, -650))
    knot = math_node(nt, 'MAXIMUM', knot, 0.0, (950, -650))
    g = math_node(nt, 'ADD', math_node(nt, 'MULTIPLY', fine.outputs['Fac'], 0.65), math_node(nt, 'MULTIPLY', broad.outputs['Fac'], 0.35), (800, -300))
    shade = math_node(nt, 'ADD', 0.72, math_node(nt, 'MULTIPLY', g, 0.56), (950, -300))          # 0,72…1,28 → ~±28% (erősen erezett dekor)
    shade = math_node(nt, 'MULTIPLY', shade, math_node(nt, 'SUBTRACT', 1.0, math_node(nt, 'MULTIPLY', knot, 0.60)), (1000, -400))
    tone = math_node(nt, 'ADD', 0.15, math_node(nt, 'MULTIPLY', r1, 0.7), (700, 150))
    base = mix_rgb(nt, tone, C_DARK, C_LIGHT, (850, 150))
    col = node(nt, 'ShaderNodeVectorMath', (1000, 150), operation='SCALE')
    nt.links.new(base, col.inputs[0]); nt.links.new(shade, col.inputs['Scale'])
    # 4V él: a hosszanti és a végillesztésnél sötétebb, keskeny horony
    du = math_node(nt, 'MULTIPLY', math_node(nt, 'MINIMUM', u, math_node(nt, 'SUBTRACT', 1.0, u)), PL_W)
    dv = math_node(nt, 'MULTIPLY', math_node(nt, 'MINIMUM', v, math_node(nt, 'SUBTRACT', 1.0, v)), PL_L)
    gr = math_node(nt, 'MAXIMUM', math_node(nt, 'LESS_THAN', du, GROOVE), math_node(nt, 'LESS_THAN', dv, GROOVE), (1000, 350))
    final = mix_rgb(nt, gr, col.outputs[0], (0.045, 0.042, 0.039), (1100, 250))
    nt.links.new(final, bsdf.inputs['Base Color'])
    rough = math_node(nt, 'ADD', 0.38, math_node(nt, 'MULTIPLY', g, 0.16))
    nt.links.new(rough, bsdf.inputs['Roughness'])
    bump = node(nt, 'ShaderNodeBump', (1000, -150))
    bump.inputs['Strength'].default_value = 0.08; bump.inputs['Distance'].default_value = 0.0006
    nt.links.new(math_node(nt, 'SUBTRACT', fine.outputs['Fac'], math_node(nt, 'MULTIPLY', gr, 3.0)), bump.inputs['Height'])
    nt.links.new(bump.outputs[0], bsdf.inputs['Normal'])
    return m


pm = bpy.data.materials['v2_parketta_GreyTreviso_EL2184_foto']
build_parquet(pm)
log['anyag'].append('v2_parketta_GreyTreviso_EL2184_foto → procedurális deszka 1292×193, É–D, 4V horony (KÖZELÍTÉS)')

# szegőléc: azonos dekor (egyszerűsítve: a deszkák átlagtónusa + hosszanti erezet)
ms = bpy.data.materials.get('v2b_ref_szegelyleces_EL2184') or bpy.data.materials.new('v2b_ref_szegelyleces_EL2184')
ms.use_nodes = True
nt = ms.node_tree; nt.nodes.clear()
o_ = node(nt, 'ShaderNodeOutputMaterial', (600, 0)); b_ = node(nt, 'ShaderNodeBsdfPrincipled', (350, 0))
nt.links.new(b_.outputs[0], o_.inputs[0])
tc = node(nt, 'ShaderNodeTexCoord', (-400, 0)); mp = node(nt, 'ShaderNodeMapping', (-200, 0))
mp.inputs['Scale'].default_value = (0.03, 0.03, 1.0)
nt.links.new(tc.outputs['Object'], mp.inputs[0])
nz = node(nt, 'ShaderNodeTexNoise', (0, 0)); nz.inputs['Scale'].default_value = 300.0; nz.inputs['Detail'].default_value = 5.0
nt.links.new(mp.outputs[0], nz.inputs['Vector'])
nt.links.new(mix_rgb(nt, nz.outputs['Fac'], (0.15, 0.144, 0.134), (0.215, 0.207, 0.194), (200, 150)), b_.inputs['Base Color'])
b_.inputs['Roughness'].default_value = 0.45

# üveg: átlátszó + Fresnel-tükröződés (a fény átjut, gyors)
mg = bpy.data.materials['Uveg']
mg.use_nodes = True
nt = mg.node_tree; nt.nodes.clear()
o_ = node(nt, 'ShaderNodeOutputMaterial', (400, 0))
tr = node(nt, 'ShaderNodeBsdfTransparent', (0, 100)); tr.inputs[0].default_value = (0.93, 0.955, 0.95, 1)
gl = node(nt, 'ShaderNodeBsdfGlossy', (0, -100)); gl.inputs['Roughness'].default_value = 0.0
fr = node(nt, 'ShaderNodeFresnel', (0, 250)); fr.inputs['IOR'].default_value = 1.52
gm = node(nt, 'ShaderNodeNewGeometry', (-200, 350))   # hátoldali lapon csak átengedés (különben teljes visszaverődés → fekete folt)
fac = math_node(nt, 'MULTIPLY', fr.outputs[0], math_node(nt, 'SUBTRACT', 1.0, gm.outputs['Backfacing']), (150, 250))
mx = node(nt, 'ShaderNodeMixShader', (200, 0))
nt.links.new(fac, mx.inputs[0]); nt.links.new(tr.outputs[0], mx.inputs[1]); nt.links.new(gl.outputs[0], mx.inputs[2])
nt.links.new(mx.outputs[0], o_.inputs[0])
log['anyag'].append('Uveg → átlátszó + Fresnel (IOR 1,52)')

# ---------------------------------------------------------------- 3) ég: egyenletes, semleges, nap nélkül
w = sc.world
w.use_nodes = True
nt = w.node_tree; nt.nodes.clear()
o_ = node(nt, 'ShaderNodeOutputWorld', (600, 0)); bg = node(nt, 'ShaderNodeBackground', (400, 0))
tc = node(nt, 'ShaderNodeTexCoord', (-400, 0)); sp = node(nt, 'ShaderNodeSeparateXYZ', (-200, 0))
nt.links.new(tc.outputs['Generated'], sp.inputs[0])
mr = node(nt, 'ShaderNodeMapRange', (0, 0))
mr.inputs['From Min'].default_value = -0.03; mr.inputs['From Max'].default_value = 0.03
nt.links.new(sp.outputs['Z'], mr.inputs['Value'])
nt.links.new(mix_rgb(nt, mr.outputs['Result'], (0.22, 0.22, 0.22), (1.0, 1.0, 1.0), (200, 0)), bg.inputs['Color'])
bg.inputs['Strength'].default_value = 1.0
nt.links.new(bg.outputs[0], o_.inputs[0])
log['uj'].append('World: egyenletes semleges ég (1,0) + semleges talaj a horizont alatt (0,22), nap nélkül')

# ---------------------------------------------------------------- 4) portálok a külső üvegezésekben (csak mintavételezés)
pc = bpy.data.collections.new('Ref_v2b_portalok'); sc.collection.children.link(pc)


def portal(name, loc, rot, sx, sy):
    ld = bpy.data.lights.new(name, 'AREA'); ld.shape = 'RECTANGLE'; ld.size = sx; ld.size_y = sy
    ld.cycles.is_portal = True
    ob = bpy.data.objects.new(name, ld); ob.location = loc; ob.rotation_euler = rot
    pc.objects.link(ob)
    log['uj'].append(f'portál {name}')


portal('Portal_nappali_E', (6.69, 8.36, 1.27), (-math.pi / 2, 0, 0), 4.50, 2.53)
portal('Portal_05_3_E', (12.96, 8.36, 1.27), (-math.pi / 2, 0, 0), 1.80, 2.53)
portal('Portal_05_1_Ny', (-0.31, 6.10, 1.285), (0, -math.pi / 2, 0), 2.57, 3.65)
portal('Portal_05_2_Ny', (-0.31, 1.00, 1.285), (0, -math.pi / 2, 0), 2.57, 1.88)

# ---------------------------------------------------------------- 5) szegőléc a parkettás helyiségekben (lockon kívüli gyűjtemény)
lock = json.load(open(LOCK, encoding='utf-8'))
sk = bpy.data.collections.new('Ref_v2b_szegelyleces'); sc.collection.children.link(sk)
SK_H, SK_T = 0.06, 0.013
walls = [bb for n, bb in lock['walls'].items() if bb[2] < 0.05 and not n.startswith('Plafon')]
PARQUET_ROOMS = ('nappali_etkezo', 'konyha', 'eloter', 'eloter_atjaro', 'kozlekedo', '05_1', '05_1_eszaki', '05_2', '05_2_gardrob', '05_3')
segs = []
for rn in PARQUET_ROOMS:
    for (x0, y0, x1, y1) in lock['rooms'].get(rn, []):
        for axis, c, a0, a1, inward in (('y', y0, x0, x1, +1), ('y', y1, x0, x1, -1), ('x', x0, y0, y1, +1), ('x', x1, y0, y1, -1)):
            for bb in walls:
                if axis == 'y':
                    face = bb[4] if inward > 0 else bb[1]
                    lo, hi = max(a0, bb[0]), min(a1, bb[3])
                else:
                    face = bb[3] if inward > 0 else bb[0]
                    lo, hi = max(a0, bb[1]), min(a1, bb[4])
                if abs(face - c) < 0.02 and hi - lo > 0.05:
                    segs.append((axis, c, lo, hi, inward))
# átfedések összevonása tengelyenként
merged = {}
for axis, c, lo, hi, inw in segs:
    merged.setdefault((axis, round(c, 3), inw), []).append((lo, hi))
nseg = 0
for (axis, c, inw), iv in merged.items():
    iv.sort(); cur = [list(iv[0])]
    for lo, hi in iv[1:]:
        if lo <= cur[-1][1] + 0.005: cur[-1][1] = max(cur[-1][1], hi)
        else: cur.append([lo, hi])
    for lo, hi in cur:
        me = bpy.data.meshes.new('szegely'); ob = bpy.data.objects.new(f'Ref_szegely_{axis}{c:.2f}_{lo:.2f}', me)
        if axis == 'y':
            ymin, ymax = (c, c + SK_T) if inw > 0 else (c - SK_T, c)
            xs, ys = (lo, hi), (ymin, ymax)
        else:
            xmin, xmax = (c, c + SK_T) if inw > 0 else (c - SK_T, c)
            xs, ys = (xmin, xmax), (lo, hi)
        v = [(xs[i], ys[j], z) for z in (0.0, SK_H) for j in (0, 1) for i in (0, 1)]
        f = [(0, 1, 3, 2), (4, 6, 7, 5), (0, 4, 5, 1), (2, 3, 7, 6), (0, 2, 6, 4), (1, 5, 7, 3)]
        me.from_pydata(v, [], f); me.materials.append(ms)
        sk.objects.link(ob); nseg += 1
log['uj'].append(f'szegőléc: {nseg} szakasz, 6 cm, a padló dekorjával (IGAZOLT-F), lockon kívül')

# ---------------------------------------------------------------- 6) validátor (lock v2b + villamos)
os.environ['WSG_LOCK'] = LOCK
os.environ['WSG_VILLAMOS'] = VILL
os.environ['WSG_REPORT_JSON'] = os.path.join(OUT, 'validator_v2b_referencia.json')
sc.camera = bpy.data.objects[CAMS[0]]
ns = runpy.run_path(VALIDATOR)
res = ns.get('result') or {}
log['validator'] = dict(errors=len(res.get('errors', [])), warnings=len(res.get('warnings', [])), ok=res.get('ok', []))
print('VALIDATOR', log['validator']['errors'], 'hiba', log['validator']['warnings'], 'figyelmeztetés')

# ---------------------------------------------------------------- 6b) csak renderhez, a validátor UTÁN: profil-átfedés
# A függőleges és a vízszintes nyílászáró-profilok egymásba érő, egysíkú dobozok -> a metszésüknél
# fekete foltot ad a Cycles. A vízszintes profilok (_also, _felso) mélységét 2 mm-rel növeljük
# (1-1 mm mindkét oldalon), így a látható lapjuk a függőleges profilé elé kerül. Δ = 1 mm (< 1 cm lock-tűrés).
nudged = []
for o in bpy.data.collections['A902_Nyilaszarok'].objects:
    n = o.name
    if o.type != 'MESH' or not (n.startswith('Uvegfal_') or n.startswith('Erkelyajto_')) or not (n.endswith('_also') or n.endswith('_felso')):
        continue
    M = o.matrix_world; Mi = M.inverted()
    pts = [M @ v.co for v in o.data.vertices]
    ext = [max(p[i] for p in pts) - min(p[i] for p in pts) for i in range(2)]
    ax = 0 if ext[0] < ext[1] else 1
    lo_, hi_ = min(p[ax] for p in pts), max(p[ax] for p in pts)
    c_, d_ = (lo_ + hi_) / 2, hi_ - lo_
    k_ = (d_ + 0.002) / d_
    for v, p in zip(o.data.vertices, pts):
        q = p.copy(); q[ax] = c_ + (p[ax] - c_) * k_
        v.co = Mi @ q
    nudged.append(n)
log['render_only'] = dict(profil_melyseg_plusz_2mm=nudged)

# ---------------------------------------------------------------- 7) render
r = sc.render
sc.render.engine = 'CYCLES'
sc.cycles.device = 'CPU'
sc.cycles.use_adaptive_sampling = True
if PRESET == 'final':
    sc.cycles.samples, sc.cycles.adaptive_threshold, sc.cycles.adaptive_min_samples, pct = 400, 0.018, 64, 100
elif PRESET == 'mid':
    sc.cycles.samples, sc.cycles.adaptive_threshold, sc.cycles.adaptive_min_samples, pct = 256, 0.03, 32, 50
else:
    sc.cycles.samples, sc.cycles.adaptive_threshold, sc.cycles.adaptive_min_samples, pct = 64, 0.05, 16, 25
sc.cycles.use_denoising = True
sc.cycles.denoiser = 'OPENIMAGEDENOISE'
sc.cycles.max_bounces = 12; sc.cycles.diffuse_bounces = 6; sc.cycles.glossy_bounces = 4
sc.cycles.transmission_bounces = 8; sc.cycles.transparent_max_bounces = 16
sc.cycles.caustics_reflective = False; sc.cycles.caustics_refractive = False
sc.cycles.sample_clamp_indirect = 10.0
r.resolution_x, r.resolution_y, r.resolution_percentage = 1600, 1000, pct
sc.view_settings.view_transform = os.environ.get('WSG_VIEW', 'AgX')
sc.view_settings.look = os.environ.get('WSG_LOOK', 'None')
sc.view_settings.exposure = EXPOSURE
sc.view_settings.gamma = 1.0
r.image_settings.file_format = 'PNG'; r.image_settings.color_depth = '8'
cams = {}
for cn in CAMS:
    cam = bpy.data.objects[cn]
    sc.camera = cam
    r.filepath = os.path.join(OUT, f'{cn}.png')
    t0 = time.time()
    bpy.ops.render.render(write_still=True)
    d = cam.data
    cams[cn] = dict(matrix_world=[list(row) for row in cam.matrix_world], lens=d.lens, sensor_width=d.sensor_width,
                    sensor_height=d.sensor_height, sensor_fit=d.sensor_fit, shift=[d.shift_x, d.shift_y],
                    res=[r.resolution_x, r.resolution_y], pct=pct, render_s=round(time.time() - t0, 1))
    print('RENDER', cn, cams[cn]['render_s'], 's')
json.dump(cams, open(os.path.join(OUT, 'kamera_parameterek.json'), 'w'), indent=1)
log['render'] = dict(engine='CYCLES CPU', samples=sc.cycles.samples, adaptive=sc.cycles.adaptive_threshold, denoise='OIDN',
                     view=sc.view_settings.view_transform, look=sc.view_settings.look, exposure=EXPOSURE, res=[1600, 1000], pct=pct)
json.dump(log, open(os.path.join(OUT, 'beallitasok.json'), 'w'), ensure_ascii=False, indent=1)
if SAVE_BLEND:
    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(OUT, 'WSG_A902_v2b_semleges_referencia.blend'), copy=True)
print('KESZ', OUT)
