# KEP-004 V3_TEST Gate – kontrollpont-mérés és nagyított bizonyítéklapok (Claude, 2026-10-25).
# A Cam_02 vetítéséből (gate_atfedes.proj) számolt modellvonalakat rajzolja a képekre, és automatikusan méri:
#   - fal–mennyezet vonal (legerősebb világos→sötét lépcső a modellvonal ±110 px-es sávjában),
#   - ablakfej / üveg felső éle (legerősebb él a modellvonal ±90 px-es sávjában; az alapkép saját mérésével korrigálva),
#   - TV sötét téglalapja (befoglaló doboz), padló/fal/mennyezet/ég átlagos CIELAB-értéke.
# A küszöbvonal (üveg alsó éle) és a bútormagasságok leolvasása a nagyított lapokról KÉZI – az auditban így jelölve.
# Használat: python3 -I kontrollpont_lapok.py <gate_mappa>   (a mappában: alap.png, S01_V3TEST.png, S02_V3TEST.png,
#            S01_V3r1_masik.png, S02_V3r1_masik.png, V2_S01_r1.png; a tömblog útvonala lent)
import sys, os, json
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from skimage import color
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_atfedes import proj, box
W, H = 1600, 1000
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
LOG = os.path.join(REPO, '03_blender/geometry_v2/tomeg_cam02_v3test/tomeg_cam02_V3TEST_log_v1.json')
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
KEPEK = [('alap.png', 'alapkép (Blender v2b-1)'), ('S01_V3TEST.png', 'S01 V3_TEST (r2)'), ('S02_V3TEST.png', 'S02 V3_TEST (r2)'),
         ('S01_V3r1_masik.png', 'S01 V3_r1 (másik munkamenet)'), ('S02_V3r1_masik.png', 'S02 V3_r1 (másik munkamenet)'),
         ('V2_S01_r1.png', 'V2 S01 próbakép (01:04)')]
PADLO = {'alap.png': [(400, 800, 600, 950)], 'S01_V3TEST.png': [(40, 880, 150, 990), (640, 665, 740, 690), (780, 655, 850, 680)],
         'S02_V3TEST.png': [(10, 900, 170, 990), (750, 655, 790, 672)], 'S01_V3r1_masik.png': [(40, 880, 150, 990), (700, 640, 800, 670)],
         'S02_V3r1_masik.png': [(10, 900, 170, 990)], 'V2_S01_r1.png': [(1480, 900, 1590, 990)]}
PADLO_REF = os.path.join(REPO, '08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg')
CEIL = [((3.67, 4.30, 2.90), (3.67, 8.05, 2.90)), ((3.67, 8.05, 2.90), (12.0, 8.05, 2.90))]
HEAD = [((4.38, 8.05, 2.53), (12.0, 8.05, 2.53))]

def betolt(p, szurke=False, blur=0):
    im = Image.open(p).convert('RGB').resize((W, H), Image.LANCZOS)
    if szurke:
        g = im.convert('L')
        if blur: g = g.filter(ImageFilter.GaussianBlur(blur))
        return np.asarray(g).astype(float)
    return im

def vonal_y(szakaszok, x):
    for A, B in szakaszok:
        A = np.array(A, float); B = np.array(B, float)
        pts = [proj(A + (B - A) * t) for t in np.linspace(0, 1, 6001)]
        pts = [p for p in pts if p is not None]
        xs = np.array([p[0] for p in pts]); ys = np.array([p[1] for p in pts])
        i = int(np.argmin(np.abs(xs - x)))
        if abs(xs[i] - x) < 1.0: return float(ys[i])
    return None

def el_kereses(a, x, ym, felfele_sotetedik=True, sav=110):
    col = a[:, x - 3:x + 4].mean(1)
    lo, hi = int(max(3, ym - sav)), int(min(H - 4, ym + sav))
    g = col[lo + 3:hi + 3] - col[lo - 3:hi - 3]
    return lo + int(np.argmin(g) if felfele_sotetedik else np.argmax(np.abs(g)))

def tv_doboz(a):
    from scipy import ndimage
    sub = a[250:650, 300:720] < 28
    lab, n = ndimage.label(sub)
    if n == 0: return None
    sz = ndimage.sum(sub, lab, range(1, n + 1)); k = int(np.argmax(sz)) + 1
    ys, xs = np.where(lab == k)
    return [int(xs.min() + 300), int(ys.min() + 250), int(xs.max() + 300), int(ys.max() + 250)]

def lab_atlag(im, r):
    x0, y0, x1, y1 = r
    a = np.asarray(im).astype(float)[y0:y1, x0:x1].reshape(1, -1, 3) / 255.0
    return [round(float(v), 1) for v in color.rgb2lab(a).reshape(-1, 3).mean(0)]

def seg(d, A, B, col, w=1, n=80, ox=0, oy=0, s=1.0):
    pts = [proj(np.array(A) + (np.array(B) - np.array(A)) * t / n) for t in range(n + 1)]
    pts = [((p[0] - ox) * s, (p[1] - oy) * s) for p in pts if p is not None]
    if len(pts) > 1: d.line(pts, fill=col, width=w)

def felirat(d, xy, t, f):
    d.text(xy, t, fill=(255, 255, 0), font=f, stroke_width=2, stroke_fill=(0, 0, 0))

def racs(tiles, oszlop, hezag=10):
    w = max(t.width for t in tiles); h = max(t.height for t in tiles); sor = (len(tiles) + oszlop - 1) // oszlop
    lap = Image.new('RGB', (oszlop * w + (oszlop - 1) * hezag, sor * h + (sor - 1) * hezag), 'white')
    for i, t in enumerate(tiles):
        r, c = divmod(i, oszlop); lap.paste(t, (c * (w + hezag), r * (h + hezag)))
    return lap

if __name__ == '__main__':
    g = sys.argv[1]
    f = ImageFont.truetype(FONT, 14)
    L = json.load(open(LOG, encoding='utf-8'))
    meres = {'modszer': 'lásd a fájl fejlécét; px a 1600×1000-es keretben; negatív Δ = a képen feljebb', 'kepek': {}}
    xs_c = [750, 800, 1000, 1100, 1200]; xs_h = [1000, 1450]
    alap_g = betolt(os.path.join(g, 'alap.png'), True, 2)
    alap_head = {x: el_kereses(alap_g, x, vonal_y(HEAD, x), False, 90) for x in xs_h}
    for fn, nev in KEPEK:
        p = os.path.join(g, fn)
        if not os.path.exists(p): continue
        a2 = betolt(p, True, 2); a0 = betolt(p, True, 0); im = betolt(p)
        m = {'nev': nev}
        m['mennyezet'] = {x: {'modell': round(vonal_y(CEIL, x)), 'kep': el_kereses(a2, x, vonal_y(CEIL, x))} for x in xs_c}
        for x in xs_c: m['mennyezet'][x]['delta'] = m['mennyezet'][x]['kep'] - m['mennyezet'][x]['modell']
        m['ablakfej_az_alapkephez'] = {x: el_kereses(a2, x, vonal_y(HEAD, x), False, 90) - alap_head[x] for x in xs_h}
        m['tv_doboz'] = tv_doboz(a0) if fn != 'alap.png' else None
        m['lab'] = {'mennyezet': lab_atlag(im, (600, 10, 900, 40)), 'eg': lab_atlag(im, (1250, 260, 1450, 300)),
                    'W04_piller': lab_atlag(im, (775, 330, 825, 560)), 'padlo': [lab_atlag(im, r) for r in PADLO.get(fn, [])]}
        meres['kepek'][fn] = m
    if os.path.exists(PADLO_REF):
        ref = Image.open(PADLO_REF).convert('RGB'); rw, rh = ref.size
        meres['padlo_referencia_ME-BAL-080_kozep50'] = lab_atlag(ref, (rw // 4, rh // 4, 3 * rw // 4, 3 * rh // 4))
    tiles = []
    for fn, nev in KEPEK:
        p = os.path.join(g, fn)
        if not os.path.exists(p): continue
        im = betolt(p); d = ImageDraw.Draw(im)
        for r in PADLO.get(fn, []): d.rectangle(r, outline=(255, 0, 0), width=4)
        t = im.resize((640, 400), Image.LANCZOS); felirat(ImageDraw.Draw(t), (6, 4), nev + ' – padlóminta-területek (piros)', f); tiles.append(t)
    racs(tiles, 3).save(os.path.join(g, 'kp6_padlo_mintateruletek.jpg'), quality=85)
    meres['modell_tv_65'] = {'TL': [round(v) for v in proj((3.72, 5.625, 1.68))], 'BR': [round(v) for v in proj((3.72, 7.075, 0.85))]}
    json.dump(meres, open(os.path.join(g, 'kontrollpontok_meres.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    # kp1 – fal–mennyezet sarok és homlokzati mennyezet/ablakfej (alap, S01, S02)
    tiles = []
    for fn in ['alap.png', 'S01_V3TEST.png', 'S02_V3TEST.png']:
        im = betolt(os.path.join(g, fn)); d = ImageDraw.Draw(im)
        for A, B in CEIL + [((3.67, 8.05, 0), (3.67, 8.05, 2.90))]: seg(d, A, B, (255, 0, 0))
        seg(d, (4.38, 8.05, 2.53), (12.0, 8.05, 2.53), (255, 140, 0))
        for (x0, y0, x1, y1) in [(560, 60, 960, 330), (1200, 0, 1600, 270)]:
            c = im.crop((x0, y0, x1, y1)).resize(((x1 - x0) * 2, (y1 - y0) * 2), Image.LANCZOS); dd = ImageDraw.Draw(c)
            for yy in range(y0, y1, 20):
                dd.line([(0, (yy - y0) * 2), (10, (yy - y0) * 2)], fill=(0, 255, 0))
                if yy % 100 == 0: dd.text((12, (yy - y0) * 2 - 7), str(yy), fill=(0, 255, 0), font=f)
            felirat(dd, (6, 6), f'{fn[:-4]}  x{x0}–{x1} y{y0}–{y1} · piros: modell mennyezet/sarok · narancs: üvegfej z 2,53', f)
            tiles.append(c)
    racs(tiles, 2).save(os.path.join(g, 'kp1_mennyezet_ablakfej_zoom.jpg'), quality=88)
    # kp2 – sarok és üveg alsó éle (küszöb) hat képen
    tiles = []
    for fn, nev in KEPEK:
        im = betolt(os.path.join(g, fn)); d = ImageDraw.Draw(im)
        seg(d, (3.67, 6.0, 0), (3.67, 8.05, 0), (255, 40, 40), 2); seg(d, (3.67, 8.05, 0), (3.67, 8.05, 1.0), (255, 40, 40), 2)
        seg(d, (3.67, 8.05, 0), (6.0, 8.05, 0), (255, 40, 40), 2); seg(d, (4.38, 8.21, 0), (6.0, 8.21, 0), (255, 140, 0), 2)
        x0, y0, x1, y1 = 740, 540, 1060, 760
        c = im.crop((x0, y0, x1, y1)).resize((512, 352), Image.LANCZOS); dd = ImageDraw.Draw(c)
        for yy in range(y0, y1, 20):
            dd.line([(0, (yy - y0) * 1.6), (6, (yy - y0) * 1.6)], fill=(0, 255, 0))
            if yy % 40 == 0: dd.text((8, (yy - y0) * 1.6 - 7), str(yy), fill=(0, 255, 0), font=f)
        felirat(dd, (60, 4), nev, f); tiles.append(c)
    lap = racs(tiles, 3); dd = ImageDraw.Draw(lap)
    lap.save(os.path.join(g, 'kp2_sarok_kuszob_zoom.jpg'), quality=88)
    # kp3 – alsó szekrény (KI3-L / BN3-L) magassága: cián 48/50 cm, lila 60 cm, narancs 70 cm
    tiles = []
    for fn, kod in [('S01_V3TEST.png', 'S01'), ('S02_V3TEST.png', 'S02'), ('alap.png', 'alap')]:
        im = betolt(os.path.join(g, fn)); x0, y0, x1, y1 = 200, 520, 800, 800; s = 1.3
        c = im.crop((x0, y0, x1, y1)).resize((int(600 * s), int(280 * s)), Image.LANCZOS); d = ImageDraw.Draw(c)
        ya, yb, zt = (5.25, 7.65, 0.50) if kod == 'S02' else (5.15, 7.55, 0.48)
        for A, B in [((4.07, ya, zt), (4.07, yb, zt)), ((4.07, ya, 0), (4.07, yb, 0)), ((3.67, ya, zt), (4.07, ya, zt)),
                     ((4.07, ya, 0), (4.07, ya, zt)), ((4.07, yb, 0), (4.07, yb, zt))]:
            seg(d, A, B, (0, 230, 255), 2, ox=x0, oy=y0, s=s)
        seg(d, (4.07, ya, 0.60), (4.07, yb, 0.60), (255, 0, 255), 1, ox=x0, oy=y0, s=s)
        seg(d, (4.07, ya, 0.70), (4.07, yb, 0.70), (255, 140, 0), 1, ox=x0, oy=y0, s=s)
        seg(d, (3.67, 4.30, 0), (3.67, 8.05, 0), (255, 40, 40), 2, ox=x0, oy=y0, s=s)
        felirat(d, (6, 4), f'{kod}: cián = alsó szekrény előlapja (48/50 cm), lila = 60 cm, narancs = 70 cm, piros = fal–padló', f)
        tiles.append(c)
    racs(tiles, 1).save(os.path.join(g, 'kp3_also_szekreny_magassag_zoom.jpg'), quality=88)
    # kp4 – étkező: a nyugati székek támlájának teteje (sárga) és az 1b étkező-/kanapétömbök
    tiles = []
    for fn, kod in [('S01_V3TEST.png', 'S01'), ('S02_V3TEST.png', 'S02')]:
        im = betolt(os.path.join(g, fn)); d = ImageDraw.Draw(im)
        for nev, bb in L['stilus'][kod]['tomegek'].items():
            if 'etkezo' in nev or 'kanape' in nev: box(d, bb[:3], bb[3:], (255, 0, 255) if 'etkezo' in nev else (0, 230, 255), 2)
        for nev, bb in L['stilus'][kod]['tomegek'].items():
            if 'szekny' in nev and '_hat' in nev:
                p = proj(((bb[0] + bb[3]) / 2, (bb[1] + bb[4]) / 2, bb[5]))
                if p: d.ellipse([p[0] - 6, p[1] - 6, p[0] + 6, p[1] + 6], fill=(255, 255, 0))
        c = im.crop((900, 520, 1600, 1000)); felirat(ImageDraw.Draw(c), (8, 6), f'{kod}: lila = étkező (1b), cián = kanapé, sárga = nyugati széktámlák teteje', f)
        tiles.append(c)
    racs(tiles, 1).save(os.path.join(g, 'kp4_etkezo_pozicio_zoom.jpg'), quality=88)
    # kp5 – nyugati fal bal része: magas szekrény, TV-háttér, alsó szekrény (1b-tömbök cián)
    tiles = []
    for fn, kod in [('S01_V3TEST.png', 'S01'), ('S02_V3TEST.png', 'S02')]:
        im = betolt(os.path.join(g, fn)); x0, y0, x1, y1 = 0, 120, 420, 820
        c = im.crop((x0, y0, x1, y1)); d = ImageDraw.Draw(c)
        bx = [(3.67, 4.35, 0, 3.97, 4.95, 2.2), (3.67, 5.05, 0.55, 3.71, 7.65, 2.45), (3.67, 5.15, 0, 4.07, 7.55, 0.48)] if kod == 'S01' else \
             [(3.67, 4.25, 0, 3.99, 4.7, 2.2), (3.67, 4.7, 0, 3.99, 5.15, 0.4), (3.67, 4.7, 0.4, 3.99, 5.15, 2.2), (3.67, 5.25, 0.55, 3.71, 7.65, 2.45), (3.67, 5.25, 0, 4.07, 7.65, 0.5)]
        for a0_, b0_, c0_, a1_, b1_, c1_ in bx:
            V = [(a0_, b0_, c0_), (a1_, b0_, c0_), (a1_, b1_, c0_), (a0_, b1_, c0_), (a0_, b0_, c1_), (a1_, b0_, c1_), (a1_, b1_, c1_), (a0_, b1_, c1_)]
            for i, j in [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6), (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]:
                seg(d, V[i], V[j], (0, 230, 255), 1, ox=x0, oy=y0)
        for yy in range(y0, y1, 50):
            d.line([(0, yy - y0), (8, yy - y0)], fill=(0, 255, 0)); d.text((10, yy - y0 - 7), str(yy), fill=(0, 255, 0), font=f)
        felirat(d, (6, 4), f'{kod}: nyugati fal bal része – cián: 1b-tömbök (magas szekrény 2,20 m)', f); tiles.append(c)
    racs(tiles, 2).save(os.path.join(g, 'kp5_nyugati_fal_bal_zoom.jpg'), quality=88)
    for fn, m in meres['kepek'].items():
        print(fn.ljust(20), 'mennyezet Δ', [m['mennyezet'][x]['delta'] for x in xs_c], '| ablakfej Δ(alaphoz)', [m['ablakfej_az_alapkephez'][x] for x in xs_h],
              '| TV', m['tv_doboz'], '| mennyezet L*', m['lab']['mennyezet'][0], 'ég L*', m['lab']['eg'][0])
