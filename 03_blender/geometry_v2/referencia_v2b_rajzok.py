# A-902 v2b – ellenőrző rajzok a semleges referenciarenderhez (2026-10-24, Claude)
# 1) Cam_02 ellenőrző kép: a renderre vetítve a terv szerinti kiállások, a hűtő-fűtő mező,
#    a fő méretek és a bizonytalan elemek (vetítés a lock v2b kameraparamétereiből).
# 2) Felülnézet: v2b falak, nyílások, kiállások, HF-mezők, a Cam_02 látómezeje.
# Csak olvas: lock v2b, villamos JSON, render PNG. Futtatás:
#   python3 referencia_v2b_rajzok.py <repo> <render_Cam02.png> <kimeneti mappa>
import sys, os, json, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont

REPO, RENDER, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
os.makedirs(OUT, exist_ok=True)
LOCK = json.load(open(os.path.join(REPO, '03_blender', 'geometry_lock_A902_v2b.json'), encoding='utf-8'))
VILL = json.load(open(os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.json'), encoding='utf-8'))
H = LOCK['H']


def font(sz, bold=False):
    p = '/usr/share/fonts/truetype/dejavu/DejaVuSans%s.ttf' % ('-Bold' if bold else '')
    return ImageFont.truetype(p, sz)


# ------------------------------------------------------------------ kamera (lock v2b)
def cam_basis(name):
    c = LOCK['cameras'][name]
    a, b, g = c['rot']
    Rx = np.array([[1, 0, 0], [0, math.cos(a), -math.sin(a)], [0, math.sin(a), math.cos(a)]])
    Ry = np.array([[math.cos(b), 0, math.sin(b)], [0, 1, 0], [-math.sin(b), 0, math.cos(b)]])
    Rz = np.array([[math.cos(g), -math.sin(g), 0], [math.sin(g), math.cos(g), 0], [0, 0, 1]])
    R = Rz @ Ry @ Rx
    return np.array(c['loc'], float), R, c['lens_mm'], c['sensor_width']


C2, R2, F2, SW2 = cam_basis('Cam_02_Nappali_terasz')
W, Hh = 1600, 1000


def to_cam(P):
    d = np.asarray(P, float) - C2
    return np.array([d @ R2[:, 0], d @ R2[:, 1], d @ R2[:, 2]])


def proj_cam(pc):
    k = (F2 / -pc[2]) * (W / SW2)
    return (W / 2 + pc[0] * k, Hh / 2 - pc[1] * k)


def proj(P):
    pc = to_cam(P)
    return proj_cam(pc) if pc[2] < -0.05 else None


def clip_poly(pts_w, near=-0.06):
    P = [to_cam(p) for p in pts_w]
    out = []
    for i in range(len(P)):
        a, b = P[i], P[(i + 1) % len(P)]
        ina, inb = a[2] < near, b[2] < near
        if ina: out.append(a)
        if ina != inb:
            t = (near - a[2]) / (b[2] - a[2])
            out.append(a + t * (b - a))
    return [proj_cam(p) for p in out]


def lerp_line(p0, p1, n=40):
    p0, p1 = np.asarray(p0, float), np.asarray(p1, float)
    pts = [proj(p0 + (p1 - p0) * t) for t in np.linspace(0, 1, n)]
    return [p for p in pts if p and -50 < p[0] < W + 50 and -50 < p[1] < Hh + 50]


V = {k['azonosito']: k for k in VILL['kiallasok']}


def wallpos(v, z):
    x = v['doboz_x_m'] if v['doboz_x_m'] != '' else v['x_m']
    y = v['doboz_y_m'] if v['doboz_y_m'] != '' else v['y_m']
    return (x, y, z)


# ------------------------------------------------------------------ 1) Cam_02 ellenőrző kép
def annotate():
    base = Image.open(RENDER).convert('RGB').resize((W, Hh), Image.LANCZOS)
    ov = Image.new('RGBA', (W, Hh), (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    # hűtő-fűtő mező a mennyezeten (HF03) – vonalkázott kitöltés
    hf = next(z for z in VILL['hutes_futes_zonak'] if z['azonosito'] == 'A902-HF03')
    x0, y0, x1, y1 = hf['x_min'], hf['y_min'], hf['x_max'], hf['y_max']
    zc = H - 0.003
    poly = clip_poly([(x0, y0, zc), (x1, y0, zc), (x1, y1, zc), (x0, y1, zc)])
    if len(poly) >= 3:
        d.polygon(poly, fill=(40, 170, 230, 70))
        mask = Image.new('L', (W, Hh), 0); ImageDraw.Draw(mask).polygon(poly, fill=255)
        hatch = Image.new('RGBA', (W, Hh), (0, 0, 0, 0)); hd = ImageDraw.Draw(hatch)
        for k in range(-Hh, W, 26):
            hd.line([(k, 0), (k + Hh, Hh)], fill=(20, 120, 200, 120), width=2)
        ov.paste(hatch, (0, 0), mask)
        for e in ((x0, y0, x1, y0), (x1, y0, x1, y1), (x1, y1, x0, y1), (x0, y1, x0, y0)):
            pts = lerp_line((e[0], e[1], zc), (e[2], e[3], zc), 80)
            if len(pts) > 1: d.line(pts, fill=(10, 110, 200, 255), width=3)
    labels = []

    def lab(P, text, col, anchor_off=(30, -40), r=9, shape='o'):
        p = proj(P)
        if not p: return
        x, y = p
        if shape == 'o':
            d.ellipse([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(0, 0, 0, 255), width=2)
        else:
            d.rectangle([x - r, y - r, x + r, y + r], fill=col + (255,), outline=(0, 0, 0, 255), width=2)
        labels.append((x, y, x + anchor_off[0], y + anchor_off[1], text, col))

    # mennyezeti és fali lámpakiállás
    ml = V['A902-ML05']; lab((ml['x_m'], ml['y_m'], H), 'ML05 „n,p” mennyezeti lámpakiállás\nfüggeszték csak ide (x 5,62 · y 6,27)', (255, 200, 40), (40, 60))
    fl = V['A902-FL02']; lab((3.67, fl['y_m'], 2.85), 'FL02 fali lámpakiállás, 2,85 m\n(x 3,68 · y 7,85)', (255, 200, 40), (-330, 55))
    # TV-blokk a nyugati válaszfalon (magasság nincs a rajzon)
    tv = [(3.67, y, z) for (y, z) in ((6.03, 0.18), (6.52, 0.18), (6.52, 0.55), (6.03, 0.55))]
    pp = [proj(p) for p in tv]
    if all(pp):
        d.polygon(pp, fill=(220, 60, 200, 90), outline=(170, 20, 150, 255))
        cx, cy = sum(p[0] for p in pp) / 4, sum(p[1] for p in pp) / 4
        labels.append((cx, cy, cx - 250, cy + 150, 'gyári TV-blokk: RJ45 G01–G04, antenna G08, dugalj D16–D17\n(y 6,03–6,52; magasság nincs a rajzon, itt 0,2–0,55 m)\nA TV helye szabad (Péter): csak dugalj kell, pl. D19 a déli falon', (220, 60, 200)))
    lab(wallpos(V['A902-D18'], 0.30), 'D18 dugalj\n(magasság nincs a rajzon)', (70, 200, 90), (10, -170), 7, 's')
    d15 = V['A902-D15']; lab((d15['doboz_x_m'], 8.05, 0.30), 'D15 dugalj', (70, 200, 90), (-40, 70), 7, 's')
    lab((V['A902-R02']['x_m'], 8.05, 2.70), 'R02 – motoros redőny kiállása (műszaki melléklet)', (255, 140, 40), (10, -60), 7, 's')
    # méretek
    dims = []
    g0, g1 = proj((4.44, 8.05, 0.02)), proj((4.44, 8.05, 2.53))
    if g0 and g1:
        d.line([g0, g1], fill=(255, 255, 255, 255), width=3)
        dims.append((g1[0] + 8, (g0[1] + g1[1]) / 2 - 10, 'üvegfal 2,53 m (terv)'))
    c0, c1 = proj((3.69, 7.6, 0.0)), proj((3.69, 7.6, H))
    if c0 and c1:
        d.line([c0, c1], fill=(255, 255, 255, 255), width=3)
        cm_ = proj((3.69, 7.6, 1.55)); dims.append((cm_[0] - 178, cm_[1], 'belmagasság\n2,90–2,93 m (mért)'))
    w0, w1 = proj((3.70, 4.30, 0.02)), proj((3.70, 8.03, 0.02))
    if w0 and w1:
        d.line([w0, w1], fill=(255, 255, 255, 255), width=3)
        wl = proj((3.70, 5.2, 1.25))
        dims.append((wl[0] - 60, wl[1], 'nyugati válaszfal: 4,00 m (y 4,05–8,05)\n10 cm vastag, anyaga ismeretlen'))
    s0 = proj((4.44, 8.20, 2.90)); s1 = proj((4.44, 8.20, 2.53))
    img = Image.alpha_composite(base.convert('RGBA'), ov)
    d2 = ImageDraw.Draw(img)
    f_lab, f_dim = font(17, True), font(16, True)
    for (x, y, tx, ty, text, col) in labels:
        d2.line([(x, y), (tx, ty)], fill=(0, 0, 0, 255), width=2)
        bb = d2.multiline_textbbox((tx, ty), text, font=f_lab, spacing=3)
        d2.rectangle([bb[0] - 6, bb[1] - 4, bb[2] + 6, bb[3] + 4], fill=(255, 255, 255, 235), outline=col + (255,), width=3)
        d2.multiline_text((tx, ty), text, fill=(15, 15, 15), font=f_lab, spacing=3)
    for (x, y, text) in dims:
        bb = d2.multiline_textbbox((x, y), text, font=f_dim, spacing=2)
        d2.rectangle([bb[0] - 5, bb[1] - 3, bb[2] + 5, bb[3] + 3], fill=(30, 30, 30, 215))
        d2.multiline_text((x, y), text, fill=(255, 255, 255), font=f_dim, spacing=2)
    # HF felirat a mennyezeten
    t = 'HF03 mennyezeti hűtő-fűtő mező (x 3,77–9,80 · y 4,05–8,05) – NEM FÚRHATÓ\na teljes látható mennyezet ebbe esik; függeszték csak az ML05 kiállásra'
    bb = d2.multiline_textbbox((24, 18), t, font=f_lab, spacing=3)
    d2.rectangle([bb[0] - 6, bb[1] - 4, bb[2] + 6, bb[3] + 4], fill=(10, 110, 200, 230))
    d2.multiline_text((24, 18), t, fill=(255, 255, 255), font=f_lab, spacing=3)
    # bizonytalan elemek a képen
    unc = [((5.8, 8.27, 1.3), 'BIZONYTALAN (K5): az üvegfal osztása, nyitható\nszárnyai és a küszöb a ME-BAL-045 fotón eltérhet'),
           ((7.2, 9.6, -0.15), 'ELŐZETES: a tetőkert v2 modellje (szintek, lépcső,\nszegély) videóból; a távoli kilátás NINCS modellezve')]
    for P, t in unc:
        p = proj(P)
        if not p: continue
        bb = d2.multiline_textbbox((p[0], p[1]), t, font=f_lab, spacing=3)
        px = min(p[0], W - 12 - (bb[2] - bb[0])); py = min(p[1], Hh - 12 - (bb[3] - bb[1]))
        bb = d2.multiline_textbbox((px, py), t, font=f_lab, spacing=3)
        d2.rectangle([bb[0] - 6, bb[1] - 4, bb[2] + 6, bb[3] + 4], fill=(255, 236, 200, 240), outline=(230, 120, 20), width=3)
        d2.multiline_text((px, py), t, fill=(120, 50, 0), font=f_lab, spacing=3)
    # fejléc + lábléc
    head, foot = 64, 178
    sheet = Image.new('RGB', (W, Hh + head + foot), (248, 248, 246))
    sheet.paste(img.convert('RGB'), (0, head))
    ds = ImageDraw.Draw(sheet)
    ds.text((16, 10), 'A-902 · Cam_02 nappali → terasz · v2b semleges referencia – ELLENŐRZŐ RÁRAJZOLÁS', fill=(20, 20, 20), font=font(24, True))
    ds.text((16, 40), 'Geometria: TERV SZERINT (lock v2b, M1 KORR 2), helyszínen NEM mért · Validator v2: PASS (0 hiba, 0 figyelmeztetés) · kiállások: TERV SZERINT', fill=(150, 30, 30), font=font(15))
    y = Hh + head + 10
    rows = ['Jelmagyarázat: sárga kör = lámpakiállás · zöld négyzet = dugalj · lila = TV-blokk · kék vonalkázás = hűtő-fűtő mező (fúrni tilos) · narancs = bizonytalan / nem igazolt',
            'Kamera: Cam_02 – hely [8,30; 4,40; 1,55] m, forgatás [1,479; 0; 0,858] rad, 20 mm, 36 mm szenzor, 1600×1000 (kamera-paraméterlap v2b).',
            'A kamera mögött (nem látszik): fő kapcsolóoszlop K10–K12 + T01 termosztát + S01 mozgásérzékelő + D19 dugalj a déli falon (x 7,15) – nem takarható.',
            'Padló: Egger Grey Treviso Oak EL2184 (dokumentum + fotó); a képen procedurális közelítés: 1292×193 mm deszka (nem mért), É–D irány a fotók alapján becsülve.',
            'Fal/mennyezet fehér, profil belül fehér, ajtó világosszürke (IGAZOLT-F). Fény: egyenletes borult ég, nap nélkül – nem a valós napállás.',
            'Bútor nincs a képen. A kép összehasonlító alap, nem kivitelezési terv: státusz ELŐSZŰRT ALAP – TERV SZERINT, NEM HELYSZÍNI.']
    for r_ in rows:
        ds.text((16, y), r_, fill=(30, 30, 30), font=font(15)); y += 27
    out = os.path.join(OUT, 'A902_semlegesv2b_1_nappali_ellenorzo.png')
    sheet.save(out)
    print(out, sheet.size)


# ------------------------------------------------------------------ 2) felülnézet
def plan():
    S, M = 95, 70        # px/m, margó
    xs = [b[0] for b in LOCK['walls'].values()] + [b[3] for b in LOCK['walls'].values()]
    ys = [b[1] for b in LOCK['walls'].values()] + [b[4] for b in LOCK['walls'].values()]
    X0, X1, Y0, Y1 = min(xs), max(xs), min(ys), max(ys) + 2.2
    Wp, Hp = int((X1 - X0) * S) + 2 * M, int((Y1 - Y0) * S) + 2 * M + 150
    im = Image.new('RGB', (Wp, Hp), (252, 252, 250)); d = ImageDraw.Draw(im, 'RGBA')

    def P(x, y):
        return (M + (x - X0) * S, M + (Y1 - y) * S)

    for rn, rects in LOCK['rooms'].items():
        for r in rects:
            a, b = P(r[0], r[3]), P(r[2], r[1])
            d.rectangle([a, b], fill=(235, 235, 232, 255))
    for z in VILL['hutes_futes_zonak']:
        a, b = P(z['x_min'], z['y_max']), P(z['x_max'], z['y_min'])
        d.rectangle([a, b], fill=(40, 170, 230, 45), outline=(20, 120, 200, 200), width=3)
    for n, bb in LOCK['walls'].items():
        if n.startswith('Plafon'): continue
        a, b = P(bb[0], bb[4]), P(bb[3], bb[1])
        col = (60, 60, 60, 255) if bb[2] < 0.05 else (150, 150, 150, 120)
        if bb[5] - bb[2] < 1.0 and bb[2] < 0.05: col = (120, 120, 120, 255)
        d.rectangle([a, b], fill=col)
    for n, bb in LOCK['openings'].items():
        a, b = P(bb[0], bb[4]), P(bb[3], bb[1])
        col = (30, 140, 220, 255) if 'uveg' in n else (180, 180, 180, 255) if n.startswith('Ajto') else (90, 160, 230, 255)
        d.rectangle([a, b], fill=col)
    for z in VILL['hutes_futes_zonak']:
        a = P(z['x_min'], z['y_max'])
        d.text((a[0] + 4, a[1] + 3), z['azonosito'].replace('A902-', ''), fill=(20, 110, 190), font=font(13, True))
    # kiállások
    for k in VILL['kiallasok']:
        x = k['doboz_x_m'] if k['doboz_x_m'] != '' else k['x_m']; y = k['doboz_y_m'] if k['doboz_y_m'] != '' else k['y_m']
        p = P(x, y)
        t = k['tipus']
        if t == 'mennyezeti_lampakiallas':
            d.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill=(255, 200, 40), outline=(0, 0, 0), width=2)
            d.line([(p[0] - 5, p[1] - 5), (p[0] + 5, p[1] + 5)], fill=(0, 0, 0), width=2); d.line([(p[0] - 5, p[1] + 5), (p[0] + 5, p[1] - 5)], fill=(0, 0, 0), width=2)
            d.text((p[0] + 8, p[1] - 18), k['azonosito'].replace('A902-', '') + ' ' + k['aramkor'], fill=(120, 80, 0), font=font(12, True))
        elif t == 'fali_lampakiallas':
            d.ellipse([p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6], fill=(255, 200, 40), outline=(0, 0, 0), width=2)
            d.text((p[0] + 7, p[1] + 2), k['azonosito'].replace('A902-', ''), fill=(120, 80, 0), font=font(12, True))
        elif t in ('dugalj',):
            d.rectangle([p[0] - 3, p[1] - 3, p[0] + 3, p[1] + 3], fill=(50, 170, 70))
        elif t in ('gyengearamu_aljzat', 'antenna_tv_aljzat'):
            d.rectangle([p[0] - 4, p[1] - 4, p[0] + 4, p[1] + 4], fill=(200, 50, 180))
        elif t in ('kapcsolo', 'termosztat', 'hangjelzo_vagy_erzekelo', 'BK_doboz', 'lakaselosztó', 'kaputelefon_belteri', 'kezelo_billentyuzet'):
            d.polygon([(p[0], p[1] - 5), (p[0] + 5, p[1] + 4), (p[0] - 5, p[1] + 4)], fill=(220, 40, 40))
    # Cam_02 látómező
    c = LOCK['cameras']['Cam_02_Nappali_terasz']
    cx, cy = c['loc'][0], c['loc'][1]
    fwd = R2 @ np.array([0, 0, -1.0]); h = math.atan2(fwd[1], fwd[0])
    half = math.atan(SW2 / 2 / F2)
    def hit(a_):
        dx, dy = math.cos(a_), math.sin(a_)
        ts = [t for t in ((3.67 - cx) / dx if dx < 0 else 1e9, (8.35 - cy) / dy if dy > 0 else 1e9) if t > 0]
        t = min(ts)
        return (cx + t * dx, cy + t * dy)
    fa, fb_ = hit(h + half), hit(h - half)
    poly = [P(cx, cy), P(*fa)] + ([P(3.67, 8.35)] if fa[0] <= 3.68 and fb_[1] >= 8.34 else []) + [P(*fb_)]
    d.polygon(poly, fill=(220, 30, 30, 40))
    for e_ in (fa, fb_):
        d.line([P(cx, cy), P(*e_)], fill=(220, 30, 30, 220), width=3)
    pc = P(cx, cy); d.ellipse([pc[0] - 9, pc[1] - 9, pc[0] + 9, pc[1] + 9], fill=(220, 30, 30))
    d.text((pc[0] + 10, pc[1] + 6), 'Cam_02 (z 1,55 m, 20 mm, vízszintes látószög 84°)', fill=(200, 20, 20), font=font(14, True))
    for c3, lbl in (('Cam_03_Etkezo_konyha', 'Cam_03'), ('Cam_04_Master', 'Cam_04')):
        cc = LOCK['cameras'][c3]; p = P(cc['loc'][0], cc['loc'][1])
        d.ellipse([p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6], fill=(150, 30, 30)); d.text((p[0] + 8, p[1] - 6), lbl, fill=(150, 30, 30), font=font(13, True))
    # helyiségnevek
    for rn, txt in (('nappali_etkezo', 'NAPPALI–ÉTKEZŐ'), ('konyha', 'KONYHA'), ('05_1', '05.1 MASTER'), ('05_2', '05.2'), ('05_3', '05.3'), ('furdo_06_1', '06.1'), ('furdo_06_2', '06.2'), ('eloter', 'ELŐTÉR'), ('wc', 'WC')):
        r = LOCK['rooms'][rn][0] if rn != 'nappali_etkezo' else LOCK['rooms'][rn][1]
        p = P((r[0] + r[2]) / 2, (r[1] + r[3]) / 2)
        d.text((p[0] - 40, p[1] - 8), txt, fill=(90, 90, 90), font=font(14, True))
    p = P(6.6, 9.4); d.text((p[0] - 60, p[1]), 'TERASZ (v2, ELŐZETES)', fill=(80, 120, 80), font=font(14, True))
    # lépték
    a = P(X0 + 0.2, Y0 - 0.25); d.line([a, (a[0] + 5 * S, a[1])], fill=(0, 0, 0), width=3)
    for i in range(6):
        d.line([(a[0] + i * S, a[1] - 6), (a[0] + i * S, a[1] + 6)], fill=(0, 0, 0), width=2)
        d.text((a[0] + i * S - 4, a[1] + 9), str(i) + (' m' if i == 5 else ''), fill=(0, 0, 0), font=font(14))
    y = Hp - 120
    for r_ in ('A-902 v2b felülnézet – falak, nyílások és helyiségek a lock v2b szerint (TERV SZERINT, M1 KORR 2, vakolatlan síkok); helyszínen NEM mért',
               'sárga ⊗ = mennyezeti lámpakiállás · sárga kör = fali lámpakiállás · zöld = dugalj · lila = TV/gyengeáram · piros háromszög = kapcsoló/termosztát/érzékelő (nem takarható)',
               'kék keret = mennyezeti hűtő-fűtő mező (HF01–HF05, panelszél ±10 cm) – nem fúrható · világosszürke = alacsony fal (konyha 0,85 m) · piros kúp = Cam_02 látómező',
               'Forrás: 03_blender/geometry_lock_A902_v2b.json, 01_alaprajzok/villamos_kiallasok/A902_villamos.json (2026-10-24)'):
        d.text((M, y), r_, fill=(30, 30, 30), font=font(14)); y += 24
    out = os.path.join(OUT, 'A902_semlegesv2b_0_felulnezet_Cam02.png')
    im.save(out)
    print(out, im.size)


if __name__ == '__main__':
    annotate()
    plan()
