# Cam_12 v3 korrekció – emberi ellenőrzésre szánt jelölt képek, alaprajzi tömbvázlat és régi/új összevetés (PIL, shapely).
# A ChatGPT-csomagba NEM ezek kerülnek (ott a tiszta képek), ezek a dokumentációhoz. Claude, 2026-10-25.
import os, sys, json
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
R = os.path.join(REPO, '04_renderek', 'A902_cam12_v3_korrekcio')
import blokk_spec as BS
L = json.load(open(os.path.join(HERE, 'naplok', 'cam12v3_korr_log.json'), encoding='utf-8'))
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
f14, f16, f20, f26 = (ImageFont.truetype(F, 14), ImageFont.truetype(FB, 16), ImageFont.truetype(FB, 20), ImageFont.truetype(FB, 26))
def cimke(dr, x, y, t, fill=(255, 255, 255), bg=(200, 30, 30)):
    w = dr.textlength(t, font=f16); x = max(4, min(1596 - w - 8, x)); y = max(4, min(970, y))
    dr.rectangle([x - 4, y - 2, x + w + 4, y + 20], fill=bg); dr.text((x, y), t, font=f16, fill=fill)
# 1) semleges + fix elemek
im = Image.open(os.path.join(R, 'A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png')).convert('RGB'); dr = ImageDraw.Draw(im)
V = L['vetites']
jel = [('05.3 ajtó (szürke) + szemöldöksáv 2,10–2,90', V['05.3 ajtó déli tok (y 6,05) alj/teteje'][1]['px'], -150, -40),
       ('W03-a (1,00 m) – hűtőoszlop helye', [278, 450], 0, 0), ('0,20 m visszaugrás', V['W03-a / K-csonk sarok (x 10,75→10,55; y 5,05)'][2]['px'], -60, 130),
       ('K-csonk + K-pultfal (konyha keleti fala)', [560, 420], 0, 0), ('FL01', V['FL01 konyhai fali pont (10,534; 3,149)'][0]['px'], 0, 0),
       ('mellvéd ~0,85 m (vége)', V['mellvéd északi vége (x 8,35–8,45; y 4,05), teteje 0,85'][0]['px'], -80, 30),
       ('előtér-átjáró, szemöldök 2,10', V['átjáró szemöldök (x 7,30–8,45; z 2,10)'][1]['px'], 0, -60),
       ('W02 (2,10 × 2,90) – szemből', [1100, 420], 0, 0), ('kapcsolóoszlop x 7,149', V['kapcsolóoszlop K10–K12/T01 (x 7,149)'][0]['px'], 10, 0),
       ('W07 visszafordulás x 5,20', V['W07 visszafordulás (x 5,20; y 2,75–4,05)'][1]['px'], -230, 220), ('közlekedő torka', [1530, 600], -60, -120),
       ('akna-csík', V['akna-sarok (x 9,80; y 7,025)'][1]['px'], 0, 120), ('ML04', V['ML04 (8,549; 6,274) mennyezet'][0]['px'], 0, 10)]
for t, p, dx, dy in jel:
    x, y = p[0], p[1]
    dr.ellipse([x - 5, y - 5, x + 5, y + 5], fill=(200, 30, 30)); cimke(dr, x + dx + 8, y + dy - 10, t)
dr.rectangle([0, 0, 1600, 36], fill=(20, 20, 20)); dr.text((10, 6), 'A-902 Cam_12 v3 KORR – semleges alapkép, a fix elemek jelölése (csak dokumentáció; a ChatGPT-csomagban jelöletlen kép megy)', font=f20, fill=(255, 255, 255))
im.save(os.path.join(R, 'A902_Cam12v3_KORR_semleges_JELOLT.jpg'), quality=90)
# 2) tömbrenderek jelölve
FO = {'S01': ['S01_SO_01b', 'S01_DI_01', 'S01_DI_02e_ules', 'S01_DI_03', 'S01_KO_K1', 'S01_KO_K2', 'S01_KO_K3', 'S01_KO_NY', 'S01_ET_01', 'S01_ET_03', 'S01_ET_02', 'S01_W02_02', 'S01_W02_04', 'S01_W02_03'],
      'S02': ['S02_SO_01a', 'S02_SO_02', 'S02_DI_01', 'S02_DI_02e_ules', 'S02_DI_03', 'S02_KO_K1', 'S02_KO_K2', 'S02_KO_K3', 'S02_KO_NY', 'S02_ET_01', 'S02_ET_02', 'S02_W02_02', 'S02_W02_03', 'S02_W02_04']}
ID = {e['id'].replace('-', '_'): e for e in BS.K}
for st, lst in FO.items():
    im = Image.open(os.path.join(R, f'A902_{st}_Cam12v3_KORR_tombrender.png')).convert('RGB'); dr = ImageDraw.Draw(im); yoff = {}
    for n in lst:
        b = L['blokkok'].get(n, {}).get('kep_px')
        if not b: continue
        e = ID.get(n) or ID.get(n.rsplit('_', 1)[0])
        x = (b[0] + b[2]) / 2; y = (b[1] + b[3]) / 2
        if n.endswith('_ules'): t = f"{e['id'][:-1]}a–f: {e['nev'].split(' #')[0]}"
        else: t = f"{e['id']}: {e['nev'][:58]}"
        k = (round(x / 150), round(y / 60)); y += 24 * yoff.get(k, 0); yoff[k] = yoff.get(k, 0) + 1
        cimke(dr, x - 60, y, t, bg=(30, 60, 160))
    dr.rectangle([0, 0, 1600, 36], fill=(20, 20, 20)); dr.text((10, 6), f'A-902 Cam_12 v3 – {st} tömbrender (méretpróba, KONCEPCIÓ – NEM VALIDÁLT); tétellista: 10_BLOKK_VALIDALAS.md', font=f20, fill=(255, 255, 255))
    im.save(os.path.join(R, f'A902_{st}_Cam12v3_KORR_tombrender_JELOLT.jpg'), quality=90)
# 3) alaprajzi tömbvázlat (felülnézet) a lock falaival
# a falak (walls) a main és a k13 lockban azonosak (ellenőrizve); a kameraadat a k13-ból jön, itt nem kell
LOCK = json.load(open(os.environ.get('WSG_LOCK', os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json')), encoding='utf-8'))
X0, Y0, X1, Y1, PX = 3.2, 0.9, 11.4, 8.6, 110
U = json.load(open(os.path.join(HERE, 'utak_blokk_S01_S02.json'), encoding='utf-8'))
for st in ('S01', 'S02'):
    W_, H_ = int((X1 - X0) * PX), int((Y1 - Y0) * PX) + 130
    im = Image.new('RGB', (W_, H_), (255, 255, 255)); dr = ImageDraw.Draw(im)
    T = lambda x, y: (round((x - X0) * PX), round(120 + (Y1 - y) * PX))
    for n, w in LOCK['walls'].items():
        if n.startswith('Plafon'): continue
        a, b = T(w[0], w[4]), T(w[3], w[1])
        dr.rectangle([a, b], fill=(150, 150, 150) if w[5] > 1.0 else (205, 205, 205), outline=(90, 90, 90))
    for e in BS.K:
        if e['st'] != st or e['tipus'] == 'chair' and False: continue
        g = e['g']; c = tuple(int(255 * v) for v in e['szin'])
        if e['tipus'] == 'box':
            if e['reteg'] == 'felulet': dr.rectangle([T(g[0] - 0.03, g[4] + 0.03), T(g[3] + 0.03, g[1] - 0.03)], outline=c, width=3); continue
            if g[2] >= 1.4: dr.rectangle([T(g[0], g[4]), T(g[3], g[1])], outline=(40, 40, 40), width=2); continue
            dr.rectangle([T(g[0], g[4]), T(g[3], g[1])], fill=c, outline=(30, 30, 30))
        elif e['tipus'] == 'ell':
            cx, cy, z0, rx, ry, z1 = g
            if z0 > 1.0: dr.ellipse([T(cx - rx, cy + ry), T(cx + rx, cy - ry)], outline=(200, 120, 0), width=2)
            else: dr.ellipse([T(cx - rx, cy + ry), T(cx + rx, cy - ry)], fill=c, outline=(30, 30, 30))
        else:
            cx, cy, nx, ny, sz, mely, ul, h = g; tx, ty = -ny, nx; a0, a1 = -0.18, -0.18 + mely
            P = lambda t, q: (cx + nx * t + tx * q, cy + ny * t + ty * q)
            pts = [P(a0, -sz / 2), P(a0, sz / 2), P(a1, sz / 2), P(a1, -sz / 2)]
            dr.polygon([T(*p) for p in pts], fill=c, outline=(30, 30, 30))
    # kamera és látómező
    import math
    cx, cy = 4.40, 7.88
    for a in (-48 - 39.29, -48 + 39.29):
        dr.line([T(cx, cy), T(cx + 6 * math.cos(math.radians(a)), cy + 6 * math.sin(math.radians(a)))], fill=(220, 0, 0), width=2)
    dr.ellipse([T(cx - 0.08, cy + 0.08), T(cx + 0.08, cy - 0.08)], fill=(220, 0, 0)); dr.text(T(cx - 0.6, cy + 0.45), 'Cam_12 v3', font=f16, fill=(220, 0, 0))
    u = U[st]; ut = u['utak_betolt_doh_asztallal']
    sor = [f'{st} tömb – felülnézet (lock v2b-1-k13)', f'Utak betolt székkel: terasz {ut["terasz (tolóajtó, keleti rész)"]:.2f} · konyha {ut["konyha (a pultsorok közé)"]:.2f} · folyosó {ut["hálók folyosója"]:.2f} · 05.3 ajtó {ut["05.3 háló ajtaja"]:.2f} m (cél ≥ 0,90)',
           f'kanapé–TV-bútor {u["kanape_TV_butor"]:.2f} · dohányzóasztal–kanapé {u["doh_kanape"]:.2f} · dohányzóasztal–TV {u["doh_TV"]:.2f} · hűtőoszlop–étkező {u["huto_oszlop_asztal_szek"]:.2f} · pultköz {u["konyha_pultkoz"]:.2f} m · kamera állóhely szabad: {"igen" if u["kamera_allohely_szabad"] else "NEM"}',
           'körvonal: ≥ 1,40 m-en lévő elem (felső szekrény), narancs kör: függeszték, színes keret: ≤ 2 mm-es tapéta / felület']
    sor = sor[:2] + [sor[2].split(' · dohányzóasztal–TV')[0], 'dohányzóasztal–TV' + sor[2].split(' · dohányzóasztal–TV')[1]] + sor[3:]
    for i, s in enumerate(sor): dr.text((10, 4 + 22 * i), s, font=f16 if i == 0 else f14, fill=(20, 20, 20))
    im.save(os.path.join(R, f'A902_{st}_Cam12v3_KORR_tomb_felulnezet.png'))
# 4) régi (k13, a ChatGPT-nek ténylegesen küldött) vs új semleges
old = os.environ.get('WSG_REGI_CAM12', os.path.join(REPO, '04_renderek', 'A902_kameracsomag_C', 'A902_Alap-v2b1k13_blender_12_nappali-hero_JAVASLAT_v3.png'))
if os.path.exists(old):
    a = Image.open(old).convert('RGB').resize((800, 500)); b = Image.open(os.path.join(R, 'A902_Alap-v2b1k13_blender_12_nappali-hero_v3_KORR_semleges.png')).convert('RGB').resize((800, 500))
    s1 = Image.open(os.path.join(R, 'A902_S01_Cam12v3_KORR_tombrender.png')).convert('RGB').resize((800, 500)); s2 = Image.open(os.path.join(R, 'A902_S02_Cam12v3_KORR_tombrender.png')).convert('RGB').resize((800, 500))
    k = Image.new('RGB', (1600, 1080), (255, 255, 255)); d = ImageDraw.Draw(k)
    for im_, xy, t in ((a, (0, 40), 'RÉGI image 1 (k13, sha 66a9c6af…) – fehér a fehéren'), (b, (800, 40), 'ÚJ image 1 – Cam_12 v3 KORR semleges (azonos kamera)'),
                      (s1, (0, 580), 'ÚJ image 1b – S01 tömbrender'), (s2, (800, 580), 'S02 tömbrender (nem része az S01-csomagnak)')):
        k.paste(im_, xy); d.text((xy[0] + 8, xy[1] - 30), t, font=f20, fill=(20, 20, 20))
    k.save(os.path.join(R, 'A902_Cam12v3_KORR_osszevetes_regi_uj.jpg'), quality=88)
print('kész')
