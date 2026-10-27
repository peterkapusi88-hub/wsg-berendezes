# Finomított keresés: kemény feltétel – minden fő út ≥ 0,90 (betolt székek), székkihúzás ≥ 0,90, kanapé–TV ≥ 0,60, nézőtáv ≥ 2,0;
# cél: az ML04 lámpa minél közelebb az asztal közepéhez, utána az ülő vendégekkel mért legszűkebb út.
import json, math, itertools, time, sys
import numpy as np
from shapely.geometry import box, Point
from shapely.ops import unary_union
import elrendezes_alt_a902 as E
from opt_alt import epit, gyors

TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.40; E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65)
import opt_alt; opt_alt.E.TV_ZONA = E.TV_ZONA
t0 = time.time(); out = {}
for st in ('S01', 'S02'):
    for cs in ('A', 'B', 'C'):
        jo = []
        for XB, cx, cy in itertools.product(np.round(np.arange(6.20, 7.05, 0.05), 2), np.round(np.arange(7.60, 9.00, 0.05), 2), np.round(np.arange(5.95, 6.70, 0.05), 2)):
            v = epit(st, cs, float(XB), float(cx), float(cy)); g = gyors(v)
            if g is None: continue
            bet, kh = g
            u = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + bet)
            if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
            jo.append((round(v['asztal'].centroid.distance(Point(*E.ML04)), 3), float(XB), float(cx), float(cy), u, min(kh)))
        jo.sort(key=lambda c: c[0])
        res = []
        for c in jo[:12]:
            v = epit(st, cs, c[1], c[2], c[3]); ulo = E.szek_poligonok(v, 'ulo')
            u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + ulo)
            res.append(dict(ML04=c[0], XB=c[1], cx=c[2], cy=c[3], ut_betolt=c[4], ut_ulo=u2, kihuzas_min=c[5],
                            kanape_tv=round(v['kanape'].distance(E.TV_ZONA), 3), nezo=round(c[1] - E.SZEM - E.KEPERNYO_X, 2)))
        res.sort(key=lambda r: (r['ML04'], -min((x or 0) for x in r['ut_ulo'].values())))
        out[f'{st}_{cs}'] = res
        b = res[0] if res else None
        print(st, cs, 'jó jelölt:', len(jo), '| legjobb:', b and (b['ML04'], b['XB'], b['cx'], b['cy'], b['kanape_tv'], b['nezo'], b['kihuzas_min'], b['ut_ulo']), f'{time.time() - t0:.0f}s', flush=True)
json.dump(out, open(f'opt_alt2_TV{int(round(TVD * 100))}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
