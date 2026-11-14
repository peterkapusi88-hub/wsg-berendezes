# Kerek asztal méretpróba a C alapelrendezésben (Péter 04:28): Ø150/140/130/120, 6 szék körben, két szögállás; TV-sáv 40 és 60 cm.
import json, itertools, sys, time
import numpy as np
from shapely.geometry import box, Point
from shapely.ops import unary_union
import elrendezes_alt_a902 as E
import opt_alt
out = {}
t0 = time.time()
for TVD in (0.40, 0.60):
    E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
    for R in (0.75, 0.70, 0.65, 0.60):
        for szog in ((30, 90, 150, 210, 270, 330), (0, 60, 120, 180, 240, 300)):
            for st in ('S01', 'S02'):
                jo = []
                for XB, cx, cy in itertools.product(np.round(np.arange(6.20, 7.05, 0.05), 2), np.round(np.arange(7.60, 9.20, 0.05), 2), np.round(np.arange(5.80, 6.80, 0.05), 2)):
                    kan = E.lennon_L(float(XB)) if st == 'S01' else E.jattebo_U(float(XB))
                    T, sz = E.etkezo_kerek(float(cx), float(cy), R, szog)
                    v = dict(kod='C', stilus=st, XB=float(XB), kanape=kan, asztal=T, szekek=sz, kerek=True)
                    g = opt_alt.gyors(v)
                    if g is None: continue
                    bet, kh = g
                    u = E.ut_szelesseg([kan, T, E.TV_ZONA] + bet)
                    if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
                    jo.append((round(T.centroid.distance(Point(*E.ML04)), 3), float(XB), float(cx), float(cy), u, min(kh)))
                jo.sort(key=lambda c: c[0])
                key = f'TV{int(TVD*100)}_R{int(R*200)}_sz{szog[0]}_{st}'
                if jo:
                    b = jo[0]
                    T, sz = E.etkezo_kerek(b[2], b[3], R, szog)
                    v = dict(kod='C', stilus=st, XB=b[1], kanape=E.lennon_L(b[1]) if st == 'S01' else E.jattebo_U(b[1]), asztal=T, szekek=sz, kerek=True)
                    m, bet, ulo = E.meres(v)
                    out[key] = dict(db=len(jo), ML04=b[0], XB=b[1], cx=b[2], cy=b[3], kihuzas_min=b[5], ut_betolt=b[4], ut_ulo=m['ut_ulo_vendegekkel_m'], kanape_TV=m['kanape_TV_butor_m'], nezotav=m['nezotav_m'], asztal_kanape=m['asztal_kanape_m'], ulo_szek_kanape=m['ulo_szek_kanape_m'], huto_betolt=m['huto_elo_szabad_betolt'], huto_ulo=m['huto_elo_szabad_ulo'])
                else:
                    out[key] = dict(db=0)
                print(key, out[key], f'{time.time()-t0:.0f}s', flush=True)
json.dump(out, open('opt_kerek2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
