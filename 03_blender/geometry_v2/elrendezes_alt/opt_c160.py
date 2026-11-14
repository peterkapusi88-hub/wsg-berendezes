import itertools, sys, json
import numpy as np
from shapely.geometry import box
import elrendezes_alt_a902 as E
import opt_alt
from opt_c2 import epit_c
TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.40; E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
PAROK = [(-0.30, 0.30), (-0.25, 0.35), (-0.20, 0.40), (-0.15, 0.45), (-0.10, 0.50), (-0.35, 0.25)]
out = {}
for st in ('S01', 'S02'):
    Lh = 1.60; szw = E.SZEK[st]['sz']; jo = []
    for XB, cx, cy, ny, k in itertools.product(np.round(np.arange(6.30, 6.80, 0.05), 2), np.round(np.arange(8.35, 8.70, 0.05), 2), np.round(np.arange(6.00, 6.50, 0.05), 2), PAROK, PAROK):
        if abs(ny[1] - ny[0]) < szw + 0.03 or abs(k[1] - k[0]) < szw + 0.03: continue
        if any(abs(d) + szw / 2 > Lh / 2 + 0.02 for d in ny + k): continue
        v = epit_c(st, float(XB), float(cx), float(cy), Lh, ny, k); g = opt_alt.gyors(v)
        if g is None: continue
        bet, kh = g
        u = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + bet)
        if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
        c = v['asztal'].centroid; ker, hos = abs(c.x - E.ML04[0]), abs(c.y - E.ML04[1])
        jo.append((round(ker + 0.4 * hos, 3), round(ker, 3), round(hos, 3), float(XB), float(cx), float(cy), ny, k, min(kh), ny == k))
    jo.sort(key=lambda c: (c[0], not c[9])); top = []
    for b in jo[:15]:
        v = epit_c(st, b[3], b[4], b[5], Lh, b[6], b[7]); u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + E.szek_poligonok(v, 'ulo'))
        top.append(dict(pont=b[0], kereszt=b[1], hossz=b[2], XB=b[3], cx=b[4], cy=b[5], ny=b[6], k=b[7], kihuzas_min=b[8], szimmetrikus=b[9], ut_ulo=u2))
    top.sort(key=lambda r: (r['pont'] - 0.05 * min((x or 0) for x in r['ut_ulo'].values())))
    out[st] = dict(db=len(jo), top=top); print(st, 'jó:', len(jo)); [print('  ', t) for t in top[:3]]
json.dump(out, open(f'opt_c160_TV{int(round(TVD * 100))}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
