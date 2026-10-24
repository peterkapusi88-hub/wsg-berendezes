"""A-902 terasz v2 – ELŐZETES Blender-réteg a megvalósulási tervből (2026-07-08) + a helyszíni videóból (2026-10-21).
Háttér-Blenderben fut (blender --background <mentett másolat>), a végén ÚJ fájlba ment. Élő fájlt nem ír felül.
Forrásadat: A902_geometria_v2_ELOZETES.json → 'terrace'. z: a belső kész padló = 0.
"""
import bpy, bmesh, json, math, os
V2 = json.load(open(os.environ.get('WSG_V2_JSON', '/Users/peterkapusi/Downloads/wsg-berendezes/03_blender/geometry_v2/A902_geometria_v2_ELOZETES.json')))
T = V2['terrace']
CN = 'A902_Terasz_v2_ELOZETES'

def coll(name):
    c = bpy.data.collections.get(name) or bpy.data.collections.new(name)
    if c.name not in bpy.context.scene.collection.children: bpy.context.scene.collection.children.link(c)
    return c

def mat(name, rgb, rough=0.6, metal=0.0, noise=None, alpha=1.0):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True; nt = m.node_tree; b = nt.nodes['Principled BSDF']
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Roughness'].default_value = rough; b.inputs['Metallic'].default_value = metal
    if alpha < 1:
        b.inputs['Alpha'].default_value = alpha
        try: m.surface_render_method = 'BLENDED'
        except Exception: m.blend_method = 'BLEND'
    if noise:
        sc, col2 = noise
        n = nt.nodes.new('ShaderNodeTexNoise'); n.inputs['Scale'].default_value = sc
        r = nt.nodes.new('ShaderNodeValToRGB'); r.color_ramp.elements[0].color = (*rgb, 1); r.color_ramp.elements[1].color = (*col2, 1)
        nt.links.new(n.outputs['Fac'], r.inputs['Fac']); nt.links.new(r.outputs['Color'], b.inputs['Base Color'])
    return m

def box(name, x0, y0, z0, x1, y1, z1, m, c):
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1.0)
    for v in bm.verts:
        v.co.x = x0 if v.co.x < 0 else x1; v.co.y = y0 if v.co.y < 0 else y1; v.co.z = z0 if v.co.z < 0 else z1
    bm.to_mesh(me); bm.free(); me.materials.append(m)
    o = bpy.data.objects.new(name, me); c.objects.link(o); return o

def bars(name, p0, p1, z0, h, m, c, step=0.12, t=0.02):
    """függőleges pálcás korlát egy mesh-ben: pálcák + felső és alsó övrúd"""
    me = bpy.data.meshes.new(name); bm = bmesh.new()
    L = math.dist(p0, p1); n = max(2, int(L / step))
    dx, dy = (p1[0]-p0[0])/L, (p1[1]-p0[1])/L
    def cube(cx, cy, cz, sx, sy, sz):
        r = bmesh.ops.create_cube(bm, size=1.0)
        for v in r['verts']: v.co.x = cx + v.co.x*sx; v.co.y = cy + v.co.y*sy; v.co.z = cz + v.co.z*sz
    for i in range(n+1):
        x = p0[0]+dx*L*i/n; y = p0[1]+dy*L*i/n; cube(x, y, z0+h/2, t, t, h)
    cx, cy = (p0[0]+p1[0])/2, (p0[1]+p1[1])/2
    sx = abs(p1[0]-p0[0])+t; sy = abs(p1[1]-p0[1])+t
    cube(cx, cy, z0+h-0.02, max(sx, 0.05), max(sy, 0.05), 0.04)   # felső öv
    cube(cx, cy, z0+0.10, max(sx, 0.04), max(sy, 0.04), 0.03)     # alsó öv
    bm.to_mesh(me); bm.free(); me.materials.append(m)
    o = bpy.data.objects.new(name, me); c.objects.link(o); return o

c = coll(CN)
M = dict(
    gres = mat('v2_greslap_vilagosszurke', (0.62, 0.62, 0.60), 0.55, noise=(18, (0.57, 0.57, 0.56))),
    wpc = mat('v2_WPC_sotet_szurkesbarna', (0.16, 0.13, 0.11), 0.7, noise=(60, (0.12, 0.10, 0.09))),
    green = mat('v2_zoldtető_fu_szukkulens', (0.24, 0.36, 0.12), 0.9, noise=(9, (0.38, 0.34, 0.24))),
    beton = mat('v2_beton_szegely', (0.66, 0.65, 0.62), 0.8),
    korlat = mat('v2_korlat_antracit', (0.06, 0.065, 0.07), 0.45, 0.6),
    jel = mat('v2_JELOLO_narancs', (1.0, 0.45, 0.05), 0.5, alpha=0.35),
)
Z_G, Z_W, Z_Z = -0.15, 0.47, 0.77   # greslap, WPC, zöldtető felszín (zöldtető: ELŐZETES)
SLAB = -0.45                         # födém teteje (nem igazolt, csak vizuális tömeg)

# 1) greslap teraszok
for k in ('T09_greslap_Ny', 'T10_greslap_K'):
    x0, y0, x1, y1 = T[k]['box']; box('v2_'+k, x0, y0, SLAB, x1, y1, Z_G, M['gres'], c)
# 2) WPC dobogó (tömör tömeg a greslap szintjéről)
for k in ('T11_WPC_kozepso', 'T11_WPC_harant', 'T11_WPC_eszaki_nyelv', 'T11_WPC_panorama_pont'):
    x0, y0, x1, y1 = T[k]['box']; box('v2_'+k, x0, y0, SLAB, x1, y1, Z_W, M['wpc'], c)
# 3) lépcsők a harántsávra (3 fok + dobogó; fokmélység 0.30 – ELŐZETES)
for k in ('Lepcso_Ny', 'Lepcso_K'):
    x0, y0, x1, y1 = T[k]['box']; rise = (Z_W - Z_G)/4
    for i in range(3):
        yy0 = 12.40 - 0.30*(3-i); box(f'v2_{k}_fok{i+1}', x0, yy0, SLAB, x1, 12.40, Z_G + rise*(i+1), M['wpc'], c)
# 4) zöldtető: a WPC-nyelv és az északi pihenő kivágásával, betonszegéllyel
gx0, gy0, gx1, gy1 = T['Zoldtető']['box']
# Zöldtető: két szélén SÍK FŰ (esőztető), középen ENYHÉN DOMBOS évelő-ágyás (videó IMG_2481 + IMG_2498). Zónahatár ELŐZETES.
MX0, MX1 = 7.62, 12.00          # domb-zóna x (becslés a videóból)
M['mulch'] = mat('v2_zoldtető_agyas_mulcs_kavics', (0.30, 0.24, 0.18), 0.95, noise=(25, (0.55, 0.53, 0.50)))
M['novi'] = mat('v2_evelo_levelzet', (0.20, 0.33, 0.12), 0.8, noise=(30, (0.33, 0.42, 0.18)))
M['virag'] = mat('v2_evelo_virag', (0.78, 0.55, 0.60), 0.7)
box('v2_Zoldtető_fu_Ny', gx0, gy0, Z_W-0.05, MX0, gy1, Z_Z, M['green'], c)
box('v2_Zoldtető_fu_K', MX1, gy0, Z_W-0.05, gx1, 18.95, Z_Z, M['green'], c)
box('v2_Zoldtető_fu_EK', 11.42, 18.95, Z_W-0.05, gx1, gy1, Z_Z, M['green'], c)
for nm, b in {'agyas_D_Ny': (MX0, gy0, 9.17, 14.58), 'agyas_D_K': (11.51, gy0, MX1, 14.58)}.items():
    box('v2_Zoldtető_'+nm, b[0], b[1], Z_W-0.05, b[2], b[3], Z_Z, M['mulch'], c)
# domb: rácsháló, középen +0.25 m (ELŐZETES)
me = bpy.data.meshes.new('v2_Zoldtető_domb_agyas'); bm = bmesh.new()
x0d, y0d, x1d, y1d = MX0, 14.58, MX1, 18.83
bmesh.ops.create_grid(bm, x_segments=36, y_segments=30, size=0.5)
for v in bm.verts:
    u, w = v.co.x + 0.5, v.co.y + 0.5
    v.co.x = x0d + u*(x1d-x0d); v.co.y = y0d + w*(y1d-y0d)
    v.co.z = Z_Z + 0.25*(math.sin(math.pi*u)**1.5)*(math.sin(math.pi*w)**1.5)
bm.to_mesh(me); bm.free(); me.materials.append(M['mulch'])
o = bpy.data.objects.new(me.name, me); c.objects.link(o)
box('v2_Zoldtető_domb_alap', x0d, y0d, Z_W-0.05, x1d, y1d, Z_Z-0.01, M['mulch'], c)
import random; random.seed(902)
bmp = bmesh.new()
for i in range(70):
    u, w = random.uniform(0.08, 0.92), random.uniform(0.08, 0.92)
    x = x0d + u*(x1d-x0d); y = y0d + w*(y1d-y0d)
    z = Z_Z + 0.25*(math.sin(math.pi*u)**1.5)*(math.sin(math.pi*w)**1.5)
    r = random.uniform(0.12, 0.24)
    res = bmesh.ops.create_icosphere(bmp, subdivisions=1, radius=r)
    for v in res['verts']: v.co.x += x; v.co.y += y; v.co.z = z + r*0.55 + v.co.z*0.6
me2 = bpy.data.meshes.new('v2_Evelok_ELOZETES'); bmp.to_mesh(me2); bmp.free(); me2.materials.append(M['novi'])
c.objects.link(bpy.data.objects.new(me2.name, me2))
bmv = bmesh.new()
for i in range(28):
    u, w = random.uniform(0.15, 0.85), random.uniform(0.15, 0.85)
    x = x0d + u*(x1d-x0d); y = y0d + w*(y1d-y0d); z = Z_Z + 0.25*(math.sin(math.pi*u)**1.5)*(math.sin(math.pi*w)**1.5)
    res = bmesh.ops.create_icosphere(bmv, subdivisions=1, radius=0.06)
    for v in res['verts']: v.co.x += x; v.co.y += y; v.co.z += z + 0.32
me3 = bpy.data.meshes.new('v2_Evelo_viragok_ELOZETES'); bmv.to_mesh(me3); bmv.free(); me3.materials.append(M['virag'])
c.objects.link(bpy.data.objects.new(me3.name, me3))
box('JELOLO_ontozoszelep_akna', 9.17, 13.30, Z_W, 9.45, 13.41, Z_W+0.30, M['jel'], c)
box('v2_Szegely_beton_D', 3.44, 13.41, Z_W, 16.27, 13.53, Z_Z+0.05, M['beton'], c)
box('v2_Szegely_beton_nyelv_Ny', 9.17, 13.41, Z_W, 9.29, 14.46, Z_Z+0.05, M['beton'], c)
box('v2_Szegely_beton_nyelv_K', 11.39, 13.41, Z_W, 11.51, 14.46, Z_Z+0.05, M['beton'], c)
box('v2_Szegely_beton_nyelv_E', 9.17, 14.46, Z_W, 11.51, 14.58, Z_Z+0.05, M['beton'], c)
box('v2_Szegely_beton_pihenő', 7.50, 18.83, Z_W, 11.54, 18.95, Z_Z+0.05, M['beton'], c)
# 5) korlát (antracit pálcás, ~1.10 m, ELŐZETES magasság) – a helyi járófelület fölött
kx = T['Korlat']['vonal']
bars('v2_Korlat_Ny_greslap', (kx['Ny'], 8.55), (kx['Ny'], 12.40), Z_G, 1.10, M['korlat'], c)
bars('v2_Korlat_Ny_kert', (kx['Ny'], 12.40), (kx['Ny'], kx['É']), Z_W, 1.10, M['korlat'], c)
bars('v2_Korlat_K_greslap', (kx['K'], 8.55), (kx['K'], 12.40), Z_G, 1.10, M['korlat'], c)
bars('v2_Korlat_K_kert', (kx['K'], 12.40), (kx['K'], kx['É']), Z_W, 1.10, M['korlat'], c)
bars('v2_Korlat_E', (kx['Ny'], kx['É']), (kx['K'], kx['É']), Z_W, 1.10, M['korlat'], c)
box('v2_Mellved_Ny', 2.83, 8.50, SLAB, kx['Ny'], 20.61, Z_W, M['beton'], c)
box('v2_Mellved_K', kx['K'], 8.50, SLAB, 16.86, 20.61, Z_W, M['beton'], c)
box('v2_Mellved_E', 2.83, kx['É'], SLAB, 16.86, 20.61, Z_W, M['beton'], c)
# 6) jakuzzi-előkészítés JELÖLŐ (nem tárgy!) + kiállások
x0, y0, x1, y1 = T['Jakuzzi_elokeszites']['box']
box('JELOLO_jakuzzi_elokeszites_2x2_ELOZETES', x0, y0, Z_G, x1, y1, Z_G+0.02, M['jel'], c)
box('JELOLO_aramkiallas', 3.77, 9.64, Z_G, 3.87, 9.74, Z_G+0.6, M['jel'], c)
box('JELOLO_fagymentes_csap', 4.09, 8.95, Z_G, 4.19, 9.05, Z_G+0.5, M['jel'], c)

# 7) régi (brosúra-alapú) terasz elrejtése – NEM törlés
hidden = []
old = bpy.data.collections.get('A902_Terasz')
if old:
    for o in list(old.all_objects):
        if o is None: continue
        o.hide_render = True; o.hide_viewport = True; hidden.append(o.name)
for n in ('T_09_greslap', 'T_10_greslap', 'T_11_fa', 'T_12_kert', 'T_12_kert_b'):
    o = bpy.data.objects.get(n)
    if o: o.hide_render = True; o.hide_viewport = True; hidden.append(n)
for o in bpy.data.objects:   # stílusréteg teraszbútorai (y > 8.4) – elrejtve, mert a régi síkterasz-feltételezésre épültek
    if o.users_collection and o.users_collection[0].name.startswith(('Stil_', 'A902_Butor')) and o.type == 'MESH':
        ys = [ (o.matrix_world @ v.co).y for v in o.data.vertices ] if o.data.vertices else [0]
        if min(ys) > 8.45: o.hide_render = True; o.hide_viewport = True; hidden.append(o.name)

# 8) kamerák
def cam(name, loc, rot_deg, lens=20, ortho=None):
    cd = bpy.data.cameras.get(name) or bpy.data.cameras.new(name)
    cd.lens = lens
    if ortho: cd.type = 'ORTHO'; cd.ortho_scale = ortho
    o = bpy.data.objects.get(name) or bpy.data.objects.new(name, cd)
    if o.name not in c.objects: c.objects.link(o)
    o.location = loc; o.rotation_euler = [math.radians(a) for a in rot_deg]; return o
cam('Cam_07_Terasz_v2_greslaprol', (12.8, 9.3, Z_G+1.6), (84, 0, 32), lens=16)
cam('Cam_08_Terasz_v2_madarnezet', (18.5, 23.0, 9.0), (52, 0, 140), lens=20)
cam('Cam_09_Terasz_v2_felulnezet', (9.85, 14.5, 40), (0, 0, 0), ortho=15.5)

bpy.context.scene.render.resolution_x, bpy.context.scene.render.resolution_y = 1600, 1000
result = {'collection': CN, 'objects': len(c.objects), 'hidden': len(hidden), 'hidden_sample': hidden[:12]}
