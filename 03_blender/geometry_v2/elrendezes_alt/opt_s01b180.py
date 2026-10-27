import itertools, sys, json
import numpy as np
from shapely.geometry import box, Point
import elrendezes_alt_a902 as E
import opt_alt
TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.40; E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
res = {}
for Lh, poz_d in ((1.80, 0.60), (1.60, 0.55)):
    jo = []
    for XB, cx, cy in itertools.product(np.round(np.arange(6.30, 7.05, 0.05), 2), np.round(np.arange(7.80, 9.00, 0.05), 2), np.round(np.arange(5.95, 6.70, 0.05), 2)):
        s = E.SZEK['S01']; kan = E.lennon_L(float(XB))
        T, sz = E.etkezo_teglalap(cx - Lh / 2, cy - 0.45, cx + Lh / 2, cy + 0.45, 'x', (cx - poz_d, cx, cx + poz_d), s['sz'], s['mely'])
        v = dict(kod='B', stilus='S01', XB=float(XB), kanape=kan, asztal=T, szekek=sz, kerek=False)
        g = opt_alt.gyors(v)
        if g is None: continue
        bet, kh = g
        u = E.ut_szelesseg([kan, T, E.TV_ZONA] + bet)
        if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
        jo.append((round(T.centroid.distance(Point(*E.ML04)), 3), float(XB), float(cx), float(cy), min(kh)))
    jo.sort(key=lambda c: c[0]); b = jo[0] if jo else None
    u2 = None
    if b:
        s = E.SZEK['S01']; T, sz = E.etkezo_teglalap(b[2] - Lh / 2, b[3] - 0.45, b[2] + Lh / 2, b[3] + 0.45, 'x', (b[2] - poz_d, b[2], b[2] + poz_d), s['sz'], s['mely'])
        v = dict(kod='B', stilus='S01', XB=b[1], kanape=E.lennon_L(b[1]), asztal=T, szekek=sz, kerek=False)
        u2 = E.ut_szelesseg([v['kanape'], T, E.TV_ZONA] + E.szek_poligonok(v, 'ulo'))
    print('S01 B asztal', Lh, 'jó:', len(jo), 'legjobb:', b, u2, flush=True)
