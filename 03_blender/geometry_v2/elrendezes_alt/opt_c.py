# C-család: hosszanti asztal 2+2+1+1 székkel (két-két szék a hosszoldalakon, egy-egy a végeken), cél: az ML04 alatt.
import itertools, sys, json
import numpy as np
from shapely.geometry import box, Point
import elrendezes_alt_a902 as E
import opt_alt
TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.40; E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
def epit_c(st, XB, cx, cy, Lh, dny, dk):
    s = E.SZEK[st]; kan = E.lennon_L(XB) if st == 'S01' else E.jattebo_U(XB)
    y0, y1 = cy - Lh / 2, cy + Lh / 2
    T = box(cx - 0.45, y0, cx + 0.45, y1)
    sz = [(cx - 0.45, cy + d, -1, 0) for d in dny] + [(cx + 0.45, cy + d, 1, 0) for d in dk] + [(cx, y0, 0, -1), (cx, y1, 0, 1)]
    return dict(kod='C', stilus=st, XB=XB, kanape=kan, asztal=T, szekek=sz, kerek=False)
def vizualis(T):
    c = T.centroid; dx, dy = abs(c.x - E.ML04[0]), abs(c.y - E.ML04[1]); return round(dx, 3), round(dy, 3)   # N–S asztal: dx = keresztirány
out = {}
for st in ('S01', 'S02'):
    for Lh in (1.80, 2.00):
        jo = []
        for XB, cx, cy, ny, k in itertools.product(np.round(np.arange(6.30, 7.05, 0.05), 2), np.round(np.arange(8.30, 8.80, 0.05), 2), np.round(np.arange(5.95, 6.55, 0.05), 2),
                                                   ((-0.45, 0.45), (-0.30, 0.45), (0.0, 0.55)), ((-0.45, 0.45), (-0.30, 0.45), (0.0, 0.55), (0.10, 0.60))):
            v = epit_c(st, float(XB), float(cx), float(cy), Lh, ny, k)
            # a hosszoldali széknek a táblán belül kell lennie
            if any(abs(d) + E.SZEK[st]['sz'] / 2 > Lh / 2 + 0.02 for d in ny + k): continue
            g = opt_alt.gyors(v)
            if g is None: continue
            bet, kh = g
            from shapely.ops import unary_union
            if any(bet[i].intersects(bet[j]) for i in range(len(bet)) for j in range(i + 1, len(bet))): continue
            u = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + bet)
            if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
            kereszt, hossz = vizualis(v['asztal'])
            jo.append((round(kereszt + 0.4 * hossz, 3), kereszt, hossz, float(XB), float(cx), float(cy), ny, k, min(kh)))
        jo.sort(key=lambda c: c[0]); b = jo[0] if jo else None; u2 = None
        if b:
            v = epit_c(st, b[3], b[4], b[5], Lh, b[6], b[7]); u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + E.szek_poligonok(v, 'ulo'))
        out[f'{st}_{Lh}'] = dict(db=len(jo), legjobb=b, ulo=u2)
        print(st, 'asztal', Lh, 'jó:', len(jo), 'legjobb:', b, u2, flush=True)
json.dump(out, open(f'opt_c_TV{int(round(TVD * 100))}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
