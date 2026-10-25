# Westwing Wolke L 258×167 a C alapelrendezésben (Toni 160×90, 2+2+1+1), TV-sáv 40/60 – gyors ellenőrzés a PR #18 motorjával
import json, sys, itertools
import numpy as np
from shapely.geometry import box
from shapely.ops import unary_union
import elrendezes_alt_a902 as E, opt_alt
def wolke_L(XB, YS=5.01, YN=7.59, D=0.95, CH=1.67, CW=0.95):
    return unary_union([box(XB - D, YS + CW, XB, YN), box(XB - CH, YS, XB, YS + CW)])
out={}
for TVD in (0.40, 0.60):
    E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
    best=None
    for XB in np.round(np.arange(6.20, 6.70, 0.05), 2):
        cx, cy, Lh = 8.45, 6.30, 1.60
        y0, y1 = cy - Lh/2, cy + Lh/2; T = box(cx-0.45, y0, cx+0.45, y1)
        sz = [(cx-0.45, cy+dd, -1, 0) for dd in (-0.10, 0.50)] + [(cx+0.45, cy+dd, 1, 0) for dd in (-0.10, 0.50)] + [(cx, y0, 0, -1), (cx, y1, 0, 1)]
        v = dict(kod='C', stilus='S01', XB=float(XB), kanape=wolke_L(float(XB)), asztal=T, szekek=sz, kerek=False)
        g = opt_alt.gyors(v)
        if g is None: continue
        m, bet, ulo = E.meres(v)
        u = m['ut_betolt_szekkel_m']
        if any((x or 0) < 0.90-1e-6 for x in u.values()): continue
        best = dict(XB=float(XB), kanape_TV=m['kanape_TV_butor_m'], nezotav=m['nezotav_m'], kihuzas_min=m['szekkihuzas_min_m'], ut_betolt=u, ut_ulo=m['ut_ulo_vendegekkel_m'], ulo_szek_kanape=m['ulo_szek_kanape_m'], ML04=m['ML04_eltetes_m'])
    out[f'TV{int(TVD*100)}'] = best or 'nincs megoldás'
    print(f'TV{int(TVD*100)}', out[f'TV{int(TVD*100)}'])
json.dump(out, open('wolke_c.json','w'), ensure_ascii=False, indent=1)
