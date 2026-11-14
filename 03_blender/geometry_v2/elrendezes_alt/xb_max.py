# A kiválasztott asztalhelyekhez a lehető legkeletibb kanapé-hát (nagyobb TV-távolság), ha minden fő út ≥ 0,90 (betolt szék)
# és ülő vendégekkel is marad ≥ 0,75 m-es út a terasz felé.
import sys, json
import numpy as np
from shapely.geometry import box
import elrendezes_alt_a902 as E
import opt_alt
from opt_c2 import epit_c
from opt_b2 import epit_b
E.TV_ZONA = box(3.67, 4.25, 4.07, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
def epit_a(st, XB, cx, cy):
    return opt_alt.epit(st, 'A', XB, cx, cy)
JEL = {('S01', 'A'): lambda xb: epit_a('S01', xb, 8.25, 6.25), ('S02', 'A'): lambda xb: epit_a('S02', xb, 8.25, 6.30),
       ('S01', 'B'): lambda xb: epit_b('S01', xb, 8.00, 6.25), ('S02', 'B'): lambda xb: epit_b('S02', xb, 8.20, 6.25),
       ('S01', 'C'): lambda xb: epit_c('S01', xb, 8.45, 6.30, 1.60, (-0.10, 0.50), (-0.10, 0.50)),
       ('S02', 'C'): lambda xb: epit_c('S02', xb, 8.45, 6.25, 1.80, (-0.10, 0.50), (-0.10, 0.50)),
       ('S02', 'C160'): lambda xb: epit_c('S02', xb, 8.45, 6.30, 1.60, (-0.10, 0.50), (-0.10, 0.50))}
out = {}
for k, f in JEL.items():
    best = None
    for xb in np.round(np.arange(6.20, 7.20, 0.05), 2):
        v = f(float(xb)); g = opt_alt.gyors(v)
        if g is None: continue
        bet, kh = g
        u = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + bet)
        if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
        u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + E.szek_poligonok(v, 'ulo'))
        rec = dict(XB=float(xb), ut=u, ut_ulo=u2, kihuzas_min=min(kh), tv=round(v['kanape'].distance(E.TV_ZONA), 3), nezo=round(float(xb) - 0.5 - 3.77, 2))
        if (u2['terasz (tolóajtó, keleti rész)'] or 0) >= 0.75 - 1e-6: best = rec      # a legkeletibb, amely még megfelel
        elif best is None: best = dict(rec, megjegyzes='ülve a terasz felé < 0,75')
    out['_'.join(k)] = best; print(k, best, flush=True)
json.dump(out, open('xb_max_TV40.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
