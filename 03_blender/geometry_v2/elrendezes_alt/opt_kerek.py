import json, itertools, time, sys
import numpy as np
from shapely.geometry import box, Point
from shapely.ops import unary_union
import elrendezes_alt_a902 as E
import opt_alt
TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.40; E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
for R in (0.70, 0.65):
    for st in ('S01', 'S02'):
        jo = []
        for XB, cx, cy in itertools.product(np.round(np.arange(6.20, 7.05, 0.05), 2), np.round(np.arange(7.60, 9.00, 0.05), 2), np.round(np.arange(5.95, 6.70, 0.05), 2)):
            s = E.SZEK[st]; kan = E.lennon_L(float(XB)) if st == 'S01' else E.jattebo_U(float(XB))
            T, sz = E.etkezo_kerek(float(cx), float(cy), R, (30, 90, 150, 210, 270, 330))
            v = dict(kod='C', stilus=st, XB=float(XB), kanape=kan, asztal=T, szekek=sz, kerek=True)
            g = opt_alt.gyors(v)
            if g is None: continue
            bet, kh = g
            u = E.ut_szelesseg([kan, T, E.TV_ZONA] + bet)
            if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
            jo.append((round(T.centroid.distance(Point(*E.ML04)), 3), float(XB), float(cx), float(cy), u, min(kh)))
        jo.sort(key=lambda c: c[0])
        b = jo[0] if jo else None
        u2 = None
        if b:
            T, sz = E.etkezo_kerek(b[2], b[3], R, (30, 90, 150, 210, 270, 330))
            v = dict(kod='C', stilus=st, XB=b[1], kanape=E.lennon_L(b[1]) if st == 'S01' else E.jattebo_U(b[1]), asztal=T, szekek=sz, kerek=True)
            u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + E.szek_poligonok(v, 'ulo'))
        print('Ø', int(round(R * 200)), st, 'jó:', len(jo), 'legjobb:', b and (b[0], b[1], b[2], b[3], b[5]), u2, flush=True)
