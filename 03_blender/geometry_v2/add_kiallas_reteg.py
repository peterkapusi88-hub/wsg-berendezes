# =====================================================================================
# A-902 v2b – villamos kiállás-réteg (jelölők) a Blender-modellbe, TERV SZERINT (2026-10-24)
# Forrás: 01_alaprajzok/villamos_kiallasok/A902_villamos.json (kiállások + hűtő-fűtő mezők).
# Csak egy új gyűjteményt ad hozzá: A902_Villamos_TERV (renderben REJTVE, nézetben látható).
# A falak, nyílászárók, padló, terasz és kamerák nem változnak – a validátor v2 LOCK/TERASZ/KAMERA
# eredménye ugyanaz marad. Újrafuttatva a régi réteget törli és újraépíti (idempotens).
# CSAK KÉZI futtatásra:
#   WSG_KEZI_FUTTATAS=1 python3 -c "import sys,bpy; sys.argv=['x','<repo>']; exec(open('<repo>/03_blender/geometry_v2/add_kiallas_reteg.py').read())"
# Kimenet: a v2b .blend frissítve + 03_blender/geometry_v2/kiallas_reteg_ellenorzes.json
# =====================================================================================
import os as _os
if _os.environ.get('WSG_KEZI_FUTTATAS') != '1':
    raise SystemExit('Csak kézi futtatás: WSG_KEZI_FUTTATAS=1')
import bpy, json, os, sys, math

REPO = sys.argv[1]
BLEND = os.path.join(REPO, '03_blender', 'WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend')
VJ = os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.json')
LOCK = json.load(open(os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json'), encoding='utf-8'))
H = LOCK.get('H', 2.90)
GYUJT = 'A902_Villamos_TERV'

bpy.ops.wm.open_mainfile(filepath=BLEND)
D = json.load(open(VJ, encoding='utf-8'))

# szerelési magasság, ha a rajzon nincs „m=…” – BECSLÉS (szokásos érték), a jelölőn z_forras-ként rögzítve
ALAP_Z = {'kapcsolo': 1.10, 'dugalj': 0.30, 'gyengearamu_aljzat': 0.30, 'antenna_tv_aljzat': 0.30, 'termosztat': 1.50,
          'hangjelzo_vagy_erzekelo': 2.20, 'kaputelefon_belteri': 1.50, 'kezelo_billentyuzet': 1.50, 'BK_doboz': 1.50,
          'lakaselosztó': 1.60, 'R_jelu_kiallas': 2.75, 'ventilator_kiallas': 2.30, 'fali_lampakiallas': 2.00,
          'fix_bekotes': 0.60, 'bejarati_ajto_eszkoz': 2.05, 'EPH_csatlakozo': 0.30, 'jakuzzi_aramkiallas': 0.40}
ALMENNYEZET = ('01 ELŐTÉR', '08 WC', '06.1 FÜRDŐ', '06.2 FÜRDŐ')   # Péter átvételi összesítője: álmennyezet, min. 2,40 m
# (al-gyűjtemény, szín RGBA) típusonként
CSOP = {'mennyezeti_lampakiallas': ('VK_ML_mennyezeti_lampa', (0.10, 0.30, 1.00, 1)),
        'fali_lampakiallas': ('VK_FL_fali_lampa', (0.65, 0.10, 0.80, 1)),
        'kapcsolo': ('VK_K_kapcsolo', (0.05, 0.60, 0.10, 1)),
        'dugalj': ('VK_D_dugalj', (1.00, 0.45, 0.00, 1)),
        'gyengearamu_aljzat': ('VK_G_informatika_TV', (0.50, 0.28, 0.05, 1)),
        'antenna_tv_aljzat': ('VK_G_informatika_TV', (0.50, 0.28, 0.05, 1)),
        'termosztat': ('VK_T_termosztat', (0.40, 0.40, 0.40, 1)),
        'R_jelu_kiallas': ('VK_R_redony', (0.00, 0.65, 0.75, 1)),
        'ventilator_kiallas': ('VK_V_ventilator', (0.00, 0.45, 0.45, 1))}
EGYEB = ('VK_S_riaszto_kaputelefon_egyeb', (0.85, 0.00, 0.35, 1))
HF = ('VK_HF_hutes_futes_mezo_NEM_FURUNK', (0.25, 0.35, 1.00, 1))

def torol(c):
    for ch in list(c.children): torol(ch)
    for o in list(c.objects): bpy.data.objects.remove(o, do_unlink=True)
    bpy.data.collections.remove(c)
if bpy.data.collections.get(GYUJT): torol(bpy.data.collections[GYUJT])
fo = bpy.data.collections.new(GYUJT); bpy.context.scene.collection.children.link(fo)
fo.hide_render = True
fo['forras'] = '01_alaprajzok/villamos_kiallasok/A902_villamos.json'
fo['statusz'] = 'TERV SZERINT – helyszínen ellenőrizendő; a z érték, ahol nincs a rajzon, becslés'
alg = {}
def gyujt(nev):
    if nev not in alg:
        c = bpy.data.collections.new(nev); fo.children.link(c); alg[nev] = c
    return alg[nev]
anyagok = {}
def anyag(nev, rgba):
    if nev in anyagok: return anyagok[nev]
    m = bpy.data.materials.get('VK_' + nev) or bpy.data.materials.new('VK_' + nev)
    m.diffuse_color = rgba; m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    if b: b.inputs['Base Color'].default_value = rgba
    anyagok[nev] = m; return m

def doboz(nev, cx, cy, cz, sx, sy, sz):
    # a háló az objektum origója körül, az origó a jelölő helye (kijelölésnél és exportnál ez a pont)
    x0, x1, y0, y1, z0, z1 = -sx / 2, sx / 2, -sy / 2, sy / 2, -sz / 2, sz / 2
    v = [(x0, y0, z0), (x1, y0, z0), (x1, y1, z0), (x0, y1, z0), (x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)]
    f = [(0, 1, 2, 3), (4, 7, 6, 5), (0, 4, 5, 1), (1, 5, 6, 2), (2, 6, 7, 3), (3, 7, 4, 0)]
    me = bpy.data.meshes.new(nev); me.from_pydata(v, [], f); me.update()
    o = bpy.data.objects.new(nev, me); o.location = (cx, cy, cz)
    return o

def korong(nev, cx, cy, cz, r, h, n=16):
    v, f = [], []
    for z in (-h / 2, h / 2):
        v += [(r * math.cos(2 * math.pi * i / n), r * math.sin(2 * math.pi * i / n), z) for i in range(n)]
    f.append(tuple(range(n - 1, -1, -1))); f.append(tuple(range(n, 2 * n)))
    f += [(i, (i + 1) % n, n + (i + 1) % n, n + i) for i in range(n)]
    me = bpy.data.meshes.new(nev); me.from_pydata(v, [], f); me.update()
    o = bpy.data.objects.new(nev, me); o.location = (cx, cy, cz)
    return o

def szam(v):
    return isinstance(v, (int, float))

ell = dict(jelolok=0, tipusonként={}, falra_illesztve=[], kulso_homlokzaton=[], mennyezet_kivul=[])
falak = []
for o in bpy.data.collections['A902_Falak'].objects:
    if o.type == 'MESH' and not o.name.startswith('Plafon'):
        pts = [o.matrix_world @ v.co for v in o.data.vertices]
        falak.append((o.name, min(p.x for p in pts), min(p.y for p in pts), max(p.x for p in pts), max(p.y for p in pts)))
def falsik_tav(x, y):
    # a legközelebbi fal (2D befoglaló téglalap) távolsága és legközelebbi pontja
    best = (99, (x, y))
    for n, a, b, c, d in falak:
        px, py = min(max(x, a), c), min(max(y, b), d)
        dd = math.hypot(x - px, y - py)
        if dd < best[0]: best = (dd, (px, py))
    return best
szobak = [r for rr in LOCK['rooms'].values() for r in (rr if isinstance(rr[0], list) else [rr])]

for k in D['kiallasok']:
    t = k['tipus']; gnev, rgba = CSOP.get(t, EGYEB)
    x = k['doboz_x_m'] if szam(k.get('doboz_x_m')) else k['x_m']
    y = k['doboz_y_m'] if szam(k.get('doboz_y_m')) else k['y_m']
    cimke = (k.get('aramkor') or k.get('kod') or '').replace(',', '')
    nev = f"VK_{k['azonosito']}" + (f"_{cimke}" if cimke else '')
    if t == 'mennyezeti_lampakiallas':
        z = (2.40 if k['helyiseg'] in ALMENNYEZET else H) - 0.012
        zf = 'álmennyezet alatt, becslés (min. 2,40 m)' if k['helyiseg'] in ALMENNYEZET else f'mennyezet ({H} m, lock)'
        o = korong(nev, x, y, z, 0.07, 0.02)
        if not any(r[0] <= x <= r[2] and r[1] <= y <= r[3] for r in szobak):
            ell['mennyezet_kivul'].append(k['azonosito'])
    else:
        if szam(k.get('magassag_m')):
            z, zf = float(k['magassag_m']), 'rajz („m=…”)'
        else:
            z, zf = ALAP_Z.get(t, 1.0), 'BECSLÉS (a rajzon nincs magasság)'
        illesztve = None
        if t not in ('R_jelu_kiallas', 'jakuzzi_aramkiallas'):
            dd, (px, py) = falsik_tav(x, y)
            if any(sz in k['helyiseg'] for sz in ('TERASZ', 'ERKÉLY')):
                # kültéri szerelvény a homlokzat külső (hőszigetelt) síkján; a modell fala csak a szerkezetet mutatja
                if dd > 0.06: ell['kulso_homlokzaton'].append([k['azonosito'], t, round(dd, 3)])
            elif dd > 0.06:
                # doboz nélküli (vagy nem a falsíkon talált) jel: a legközelebbi falsíkra illesztve, a tervi pont megmarad
                ell['falra_illesztve'].append([k['azonosito'], t, round(dd, 3)])
                illesztve = (x, y, round(dd * 100)); x, y = px, py
        o = doboz(nev, x, y, z, 0.08, 0.08, 0.08)
        if illesztve:
            o['x_terv'], o['y_terv'], o['falra_illesztve_cm'] = illesztve
    o.color = rgba
    o.data.materials.append(anyag(gnev, rgba))
    for kk in ('azonosito', 'tipus', 'helyiseg', 'aramkor', 'kod', 'statusz', 'forras'):
        o[kk] = str(k.get(kk, ''))
    o['z_m'] = round(z, 3); o['z_forras'] = zf
    gyujt(gnev).objects.link(o)
    ell['jelolok'] += 1; ell['tipusonként'][t] = ell['tipusonként'].get(t, 0) + 1

# hűtő-fűtő mezők: keret + két átló (mint a rajzon), a mennyezet síkja alatt 3 mm-rel
hc = gyujt(HF[0]); hm = anyag(HF[0], HF[1])
for z in D['hutes_futes_zonak']:
    x0, y0, x1, y1 = z['x_min'], z['y_min'], z['x_max'], z['y_max']; zz = H - 0.005; w = 0.025
    darabok = [doboz(f"VK_{z['azonosito']}_keret_D", (x0 + x1) / 2, y0, zz, x1 - x0, w, 0.006),
               doboz(f"VK_{z['azonosito']}_keret_E", (x0 + x1) / 2, y1, zz, x1 - x0, w, 0.006),
               doboz(f"VK_{z['azonosito']}_keret_Ny", x0, (y0 + y1) / 2, zz, w, y1 - y0, 0.006),
               doboz(f"VK_{z['azonosito']}_keret_K", x1, (y0 + y1) / 2, zz, w, y1 - y0, 0.006)]
    for i, (a, b) in enumerate((((x0, y0), (x1, y1)), ((x0, y1), (x1, y0)))):
        L = math.dist(a, b); o = doboz(f"VK_{z['azonosito']}_atlo{i + 1}", (a[0] + b[0]) / 2, (a[1] + b[1]) / 2, zz, L, w, 0.006)
        o.rotation_euler[2] = math.atan2(b[1] - a[1], b[0] - a[0]); darabok.append(o)
    for o in darabok:
        o.color = HF[1]; o.data.materials.append(hm)
        o['azonosito'] = z['azonosito']; o['helyiseg'] = z['helyiseg']; o['statusz'] = z['statusz']
        o['megjegyzes'] = 'mennyezeti hűtő-fűtő mező a födémben – ide nem fúrunk'
        hc.objects.link(o)

bpy.ops.wm.save_mainfile(filepath=BLEND)
ell['hutes_futes_mezo'] = len(D['hutes_futes_zonak'])
json.dump(ell, open(os.path.join(REPO, '03_blender', 'geometry_v2', 'kiallas_reteg_ellenorzes.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('KIÁLLÁS-RÉTEG KÉSZ', json.dumps(ell, ensure_ascii=False))
