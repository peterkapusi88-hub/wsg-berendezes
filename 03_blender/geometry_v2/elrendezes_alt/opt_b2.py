import itertools, sys, json
import numpy as np
from shapely.geometry import box
import elrendezes_alt_a902 as E
import opt_alt
TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.40; E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65); opt_alt.E.TV_ZONA = E.TV_ZONA
def epit_b(st, XB, cx, cy, Lh=1.80, dp=0.60):
    s = E.SZEK[st]; kan = E.lennon_L(XB) if st == 'S01' else E.jattebo_U(XB)
    T, sz = E.etkezo_teglalap(cx - Lh / 2, cy - 0.45, cx + Lh / 2, cy + 0.45, 'x', (cx - dp, cx, cx + dp), s['sz'], s['mely'])
    return dict(kod='B', stilus=st, XB=XB, kanape=kan, asztal=T, szekek=sz, kerek=False)
if __name__ == '__main__':
    out = {}
    for st in ('S01', 'S02'):
        jo = []
        for XB, cx, cy in itertools.product(np.round(np.arange(6.30, 6.80, 0.05), 2), np.round(np.arange(7.90, 8.70, 0.05), 2), np.round(np.arange(6.00, 6.65, 0.05), 2)):
            v = epit_b(st, float(XB), float(cx), float(cy)); g = opt_alt.gyors(v)
            if g is None: continue
            bet, kh = g
            u = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + bet)
            if any((x or 0) < 0.90 - 1e-6 for x in u.values()): continue
            c = v['asztal'].centroid; hos, ker = abs(c.x - E.ML04[0]), abs(c.y - E.ML04[1])   # E–W asztal: dx = hosszirány
            jo.append((round(ker + 0.4 * hos, 3), round(ker, 3), round(hos, 3), float(XB), float(cx), float(cy), min(kh)))
        jo.sort(key=lambda c: c[0]); top = []
        for b in jo[:12]:
            v = epit_b(st, b[3], b[4], b[5]); u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + E.szek_poligonok(v, 'ulo'))
            top.append(dict(pont=b[0], kereszt=b[1], hossz=b[2], XB=b[3], cx=b[4], cy=b[5], kihuzas_min=b[6], ut_ulo=u2))
        top.sort(key=lambda r: (r['pont'] - 0.05 * min((x or 0) for x in r['ut_ulo'].values())))
        out[st] = dict(db=len(jo), top=top); print(st, 'jó:', len(jo)); [print('  ', t) for t in top[:3]]
    json.dump(out, open(f'opt_b2_TV{int(round(TVD * 100))}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
