# A-811 / A-812 geometria – ellenőrző kép: a kinyert falak, aknák, nyílászárók, helyiségek, erkély és kamerák a
# méretezett alaprajz fölé rajzolva. Futtatás: python3 a8_ellenorzo_kep.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf
# Kimenet: <lakás>_geometria_ellenorzes.png (a rajzlap szövegmezője és a vevői adatok nincsenek a kivágásban).
import sys, os, json, math
import pymupdf
from PIL import Image, ImageDraw, ImageFont
PDF = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
CROP = {'A811': (-2.3, -0.7, 8.85, 12.05), 'A812': (-2.3, -1.25, 9.3, 17.35)}
PX = {'A811': 110, 'A812': 85}
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 14)
for flat in ('A811', 'A812'):
    G = json.load(open(os.path.join(HERE, f'{flat}_geometria_ELOZETES.json'), encoding='utf-8'))
    k = G['koordinata']; M = k['pt_per_m']; X0, Y0 = k['X0_pt'], k['Y0_pt']; c = CROP[flat]; px = PX[flat]
    pg = pymupdf.open(PDF)[G['forras']['oldal'] - 1]
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(px / M, px / M), clip=pymupdf.Rect(X0 + c[0] * M, Y0 - c[3] * M, X0 + c[2] * M, Y0 - c[1] * M), alpha=False)
    im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples).convert('RGBA')
    im = Image.alpha_composite(im, Image.new('RGBA', im.size, (255, 255, 255, 150)))
    lay = Image.new('RGBA', im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    P = lambda x, y: ((x - c[0]) * px, (c[3] - y) * px)
    rect = lambda r, **kw: d.rectangle([P(r[0], r[3]), P(r[2], r[1])], **kw)
    for e in G['erkely']['lapok']: rect(e, fill=(120, 200, 120, 60), outline=(40, 140, 40, 200))
    for kk, s in G['szobak'].items():
        for r in s['r']: rect(r, fill=(80, 140, 255, 28), outline=(40, 90, 230, 160))
    for n, r in G['walls'].items(): rect(r, fill=(255, 120, 0, 150), outline=(190, 60, 0, 255))
    for n, r in G['aknak'].items(): rect(r, fill=(110, 110, 110, 170), outline=(40, 40, 40, 255))
    for n, a in G['ajtok'].items():
        (a0, a1), (w0, w1) = a['nyilas'], a['fal_sik']
        rect([a0, w0, a1, w1] if a['fal'] == 'x' else [w0, a0, w1, a1], fill=(0, 200, 90, 150))
    def iv(h, r, irany, nyilas, tengely, szin):
        # negyedkör: a zsanértól a nyílás másik vége felé (zárt állás) és a nyitás iránya felé
        hx, hy = h
        if tengely == 'y': d1 = (0, 1 if abs(hy - nyilas[0]) < abs(hy - nyilas[1]) else -1)
        else: d1 = (1 if abs(hx - nyilas[0]) < abs(hx - nyilas[1]) else -1, 0)
        d2 = {'+x': (1, 0), '-x': (-1, 0), '+y': (0, 1), '-y': (0, -1)}[irany]
        pts = [(hx + r * (math.cos(t) * d1[0] + math.sin(t) * d2[0]), hy + r * (math.cos(t) * d1[1] + math.sin(t) * d2[1])) for t in [i * math.pi / 40 for i in range(21)]]
        d.line([P(*p) for p in pts], fill=szin, width=2); d.line([P(hx, hy), P(*pts[-1])], fill=szin, width=2)
    for n, a in G['ajtok'].items(): iv(a['zsaner'], a['r'], a['irany'], a['nyilas'], 'x' if a['fal'] == 'x' else 'y', (0, 150, 60, 255))
    for n, w in G['ablakok'].items():
        f0, f1 = w['f']; b0, b1 = w['b']
        rect([b0, f0, b1, f1], fill=(0, 120, 255, 120), outline=(0, 60, 200, 255))
        for g in w['uvegek']: rect([(b0 + b1) / 2 - 0.012, g[0], (b0 + b1) / 2 + 0.012, g[1]], fill=(150, 230, 255, 255))
        for s in w['nyilo']: iv(s['zsaner'], s['r'], s['irany'], s['nyilas'], 'y', (0, 90, 220, 255))
    for n, cam in G['kamerak'].items():
        (x, y, z), (tx, ty, tz) = cam['loc'], cam['cel']
        a = math.atan2(ty - y, tx - x); L = 1.2; hw = math.radians(42)
        d.polygon([P(x, y), P(x + L * math.cos(a - hw), y + L * math.sin(a - hw)), P(x + L * math.cos(a + hw), y + L * math.sin(a + hw))], fill=(230, 0, 60, 60), outline=(200, 0, 40, 255))
        d.text(P(x + 0.08, y + 0.12), n.replace('Cam_', 'C'), fill=(180, 0, 30, 255), font=F)
    for kk, s in G['szobak'].items():
        r = max(s['r'], key=lambda q: (q[2] - q[0]) * (q[3] - q[1]))
        d.text(P(r[0] + 0.08, r[3] - 0.12), s['nev'], fill=(0, 40, 160, 255), font=FB)
    im = Image.alpha_composite(im, lay).convert('RGB')
    d2 = ImageDraw.Draw(im)
    d2.rectangle([0, 0, im.width, 26], fill=(255, 255, 255))
    d2.text((8, 5), f"{G['lakas']} geometria v1 – ELŐZETES (tervből) · narancs: fal · szürke: akna · zöld: ajtó + nyitás · kék: üvegfal + szárny · keret: helyiség · piros: kamera",
            fill=(0, 0, 0), font=F)
    im.save(os.path.join(HERE, f'{flat}_geometria_ellenorzes.png'), optimize=True); print(flat, im.size)
