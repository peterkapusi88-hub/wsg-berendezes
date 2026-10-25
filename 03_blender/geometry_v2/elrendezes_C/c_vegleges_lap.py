# A-902 C elrendezés – végleges méretpróba-lap (S01, S02; TV-fal 60 cm-es felső eset) a kamerák helyével és látószögével. Claude, 2026-10-25.
import os, sys, json, math
from shapely.geometry import box
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import c_hatarhelyzet as H
E = H.E
OUTD = os.path.join(HERE, '..', '..', '..', '04_renderek', 'A902_kameracsomag_C'); os.makedirs(OUTD, exist_ok=True)
DY = {'S01': -0.10, 'S02': 0.0}
KAM = [('Cam_12 v3', (4.40, 7.88), -48.0, 22.0, (200, 30, 30)), ('Cam_12 v2 (régi)', (3.95, 7.90), -45.0, 22.0, (150, 150, 150)),
       ('Cam_03 K1', (9.45, 7.55), -90.0, 20.0, (30, 120, 200)), ('Cam_02', (8.30, 4.40), 139.14, 20.0, (40, 150, 60))]
rogz = {}; panelek = []
for st in ('S01', 'S02'):
    E.TV_ZONA = box(3.67, 4.25, 4.27, 7.65)
    v = H.valtozat(st, 0.0, DY[st]); v['cim'] = 'C – végleges méretpróba (TV-fal legfeljebb 60 cm)'
    r60 = H.mer(st, 0.0, DY[st], 0.60); r40 = H.mer(st, 0.0, DY[st], 0.40)
    E.TV_ZONA = box(3.67, 4.25, 4.27, 7.65); m, b, u = E.meres(v)
    im = E.panel(v, m, b, u); dr = ImageDraw.Draw(im, 'RGBA')
    x0, y0, x1, y1 = E.NEZET; T_ = lambda x, y: (round((x - x0) * E.PX), round(E.FEJ + (y1 - y) * E.PX))
    dr.rectangle([T_(H.FUGGONY[0], H.FUGGONY[3]), T_(H.FUGGONY[2], H.FUGGONY[1])], fill=(160, 60, 160, 90))   # függönysáv (becslés)
    F = ImageFont.truetype(E.FONTB, 15)
    for nev, (cx, cy), th, lens, col in KAM:
        fov = math.degrees(2 * math.atan(18.0 / lens)); Lh = 2.2
        a1, a2 = math.radians(th + fov / 2), math.radians(th - fov / 2)
        p = [T_(cx, cy), T_(cx + Lh * math.cos(a1), cy + Lh * math.sin(a1)), T_(cx + Lh * math.cos(a2), cy + Lh * math.sin(a2))]
        dr.polygon(p, fill=col + (45,), outline=col + (255,)); q = T_(cx, cy); dr.ellipse([q[0] - 6, q[1] - 6, q[0] + 6, q[1] + 6], fill=col + (255,))
        off = {'Cam_12 v3': (10, -24), 'Cam_12 v2 (régi)': (-40, 12), 'Cam_03 K1': (8, 6), 'Cam_02': (8, 6)}[nev]; dr.text((q[0] + off[0], q[1] + off[1]), nev, fill=col, font=F)
    panelek.append(im)
    rogz[st] = dict(kanape=('Westwing Lennon L 238×180 (jobbos), háttámla x ' if st == 'S01' else 'IKEA JÄTTEBO U 285×160, háttámla x ') + f"{v['XB']:.2f}",
                    kanape_befoglalo=[round(c, 3) for c in v['kanape'].bounds], asztal=('Westwing Toni ovális 160×90' if st == 'S01' else 'Westwing Anouk 180×90'),
                    asztal_befoglalo=r60['asztal'], szekek_el_kozeppont_normalis=[list(s) for s in v['szekek']],
                    szek=('6 × Kave Home Eamy 55×53' if st == 'S01' else '6 × Kave Home Ciselia 52,5×55'),
                    meres_TV60=dict((k, r60[k]) for k in ('kihuzas', 'kihuzas_fuggonnyel', 'utak_betolt', 'utak_ulo', 'szek_kanape', 'kanape_TV', 'nezotav', 'ML04', 'huto_sarok', 'kotelezo_ok')),
                    meres_TV40=dict((k, r40[k]) for k in ('utak_betolt', 'utak_ulo', 'szek_kanape', 'kanape_TV', 'nezotav', 'kotelezo_ok')))
W_ = sum(p.width for p in panelek) + 20; Hh = max(p.height for p in panelek) + 80
lap = Image.new('RGB', (W_, Hh), 'white'); d = ImageDraw.Draw(lap)
d.text((10, 8), 'A-902 – C elrendezés: végleges méretpróba és kamerák · MÉRETPRÓBA (terv szerint, helyszínen nem mért)', fill=(0, 0, 0), font=ImageFont.truetype(E.FONTB, 22))
d.text((10, 40), 'Barna: TV-fal 60 cm-es felső eset · lila sáv: behúzott függöny (becslés, 12 cm) · ékek: a kamerák látószöge · bal: S01, jobb: S02', fill=(60, 60, 60), font=ImageFont.truetype(E.FONT, 16))
xx = 0
for p in panelek: lap.paste(p, (xx, 75)); xx += p.width + 20
lap.save(os.path.join(OUTD, 'A902_C_vegleges_alaprajz_kamerak.png'))
json.dump(dict(statusz='MÉRETPRÓBA – rögzített továbbtervezési alap (Péter 2026-10-25 04:08), nem kivitelezési terv; terv szerinti geometria, helyszínen nem mért',
               tv_fal='W01: legfeljebb 60 cm mély, mennyezetig érő zárt szekrény (felső lehetőség, nem kötelező); a képernyő a falsíkon vagy a fülkében (x ≈ 3,77)',
               valtozatok=rogz), open(os.path.join(HERE, 'elrendezes_C_A902_rogzitett.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
