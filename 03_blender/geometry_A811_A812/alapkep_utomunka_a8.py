# A-811 / A-812 alapképek utómunkája (2026-10-24, Claude):
#  1) a Blender-PNG-k metaadat nélkül (a „File” mező a Mac helyi útvonalát tartalmazná) a 04_renderek/<LAKÁS>_alap_v1/ mappába;
#  2) a felülnézeti ellenőrző képre 1 m-es rács, tengelyfeliratok, ML- és HF-azonosítók és jelmagyarázat kerül.
# Futtatás: python3 alapkep_utomunka_a8.py <render-kimenet mappa (out_A811 / out_A812 szülője)> <repo>
import sys, os, json, math
from PIL import Image, ImageDraw, ImageFont
SRC, REPO = sys.argv[1], sys.argv[2]
F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 15)
FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 12)
FB = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 17)
for L in ('A811', 'A812'):
    src = os.path.join(SRC, f'out_{L}'); dst = os.path.join(REPO, '04_renderek', f'{L}_alap_v1'); os.makedirs(dst, exist_ok=True)
    lock = json.load(open(os.path.join(REPO, '03_blender', f'geometry_lock_{L}.json'), encoding='utf-8'))
    V = json.load(open(os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', f'{L}_villamos.json'), encoding='utf-8'))
    for fn in sorted(os.listdir(src)):
        if not fn.endswith('.png'): continue
        im = Image.open(os.path.join(src, fn)).convert('RGB')
        if '_06_' in fn:
            cam = lock['cameras']['Cam_06_Alaprajz_lakas']; W, H = im.size
            k = max(W, H) / cam['ortho_scale']; cx, cy = cam['loc'][0], cam['loc'][1]
            P = lambda x, y: (W / 2 + (x - cx) * k, H / 2 - (y - cy) * k)
            d = ImageDraw.Draw(im, 'RGBA')
            x0 = math.floor(cx - W / 2 / k); x1 = math.ceil(cx + W / 2 / k); y0 = math.floor(cy - H / 2 / k); y1 = math.ceil(cy + H / 2 / k)
            for x in range(x0, x1 + 1):
                d.line([P(x, y0), P(x, y1)], fill=(0, 90, 255, 60), width=1); d.text((P(x, 0)[0] + 3, 4), f'{x}', fill=(0, 60, 200, 255), font=FS)
            for y in range(y0, y1 + 1):
                d.line([P(x0, y), P(x1, y)], fill=(0, 90, 255, 60), width=1); d.text((4, P(0, y)[1] - 14), f'{y}', fill=(0, 60, 200, 255), font=FS)
            for z in V['hutes_futes_zonak']:
                d.text(P(z['x_min'] + 0.08, z['y_max'] - 0.08), z['azonosito'].split('-')[1], fill=(40, 70, 230, 255), font=FS)
            for kk in V['kiallasok']:
                if kk['tipus'] == 'mennyezeti_lampakiallas':
                    p = P(kk['x_m'], kk['y_m']); d.text((p[0] + 9, p[1] - 8), kk['azonosito'].split('-')[1], fill=(10, 40, 180, 255), font=FS)
            leg = [((60, 120, 255), 'mennyezeti lámpakiállás (ML)'), ((170, 30, 210), 'fali lámpakiállás'), ((15, 150, 25), 'kapcsoló'),
                   ((255, 115, 0), 'dugalj'), ((128, 70, 15), 'TV / informatika'), ((0, 165, 190), 'redőny'), ((215, 0, 90), 'riasztó, kaputelefon, egyéb'),
                   ((100, 120, 255), 'hűtő-fűtő mező (HF) – ide nem fúrunk')]
            # jelmagyarázat a kép jobb oldalára fűzött sávban (ne takarja a lakást)
            im2 = Image.new('RGB', (W + 360, H), (255, 255, 255)); im2.paste(im, (0, 0)); im = im2; d = ImageDraw.Draw(im, 'RGBA')
            bx, by = W + 20, 40
            d.rectangle([bx - 10, by - 10, W + 350, by + 34 + 22 * len(leg) + 10], fill=(255, 255, 255, 255), outline=(80, 80, 80, 255))
            d.text((bx, by - 4), f"{lock['lakas']} – kiállások TERV SZERINT", fill=(0, 0, 0, 255), font=FB)
            for i, (c, t) in enumerate(leg):
                yy = by + 28 + 22 * i; d.rectangle([bx, yy, bx + 14, yy + 14], fill=c + (255,)); d.text((bx + 22, yy - 1), t, fill=(0, 0, 0, 255), font=F)
            for i, t in enumerate(['Ellenőrző felülnézet (Workbench),', 'nem Astrának szól.', 'Koordináták: x rajzon jobbra,', 'y rajzon felfelé, méterben;', 'a rács 1 m.',
                                   'A jelölők helye a villamos JSON', 'szerinti; a falra illesztettek', 'eredeti pontja a .blend-ben.']):
                d.text((bx, by + 60 + 22 * len(leg) + 22 * i), t, fill=(0, 0, 0, 255), font=F)
        im.save(os.path.join(dst, fn), optimize=True)   # metaadat nélkül
        print(L, fn, im.size)
    lg = json.load(open(os.path.join(src, f'render_log_{L}.json'), encoding='utf-8'))
    json.dump(lg, open(os.path.join(dst, f'render_log_{L}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
