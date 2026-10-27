# Kerek, hatszemélyes asztal a C elrendezésben (Péter 2026-10-25 04:39): Ø120–150, hat szék 60°-onként, az ML04 alatt / körül.
# Motor: ../elrendezes_alt/elrendezes_alt_a902.py; a kanapé helye a C végleges (S01 XB 6,67; S02 XB 6,60). MÉRETPRÓBA.
import os, sys, json, math
from shapely.geometry import box, Point
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import c_hatarhelyzet as H
E = H.E
def eset(st, D, cx, cy, rot0, tv):
    E.TV_ZONA = box(3.67, 4.25, 3.67 + tv, 7.65)
    v = H.valtozat(st, 0, 0)
    T, sz = E.etkezo_kerek(cx, cy, D / 2, [rot0 + 60 * i for i in range(6)])
    v['asztal'] = T; v['szekek'] = sz; v['kerek'] = True
    m, b, u = E.meres(v)
    E.PULT = H.PULT0 + [H.FUGGONY]; kf = E.kihuzas(v); E.PULT = H.PULT0
    u1 = m['ut_betolt_szekkel_m']
    ok = all((w or 0) >= 0.90 - 1e-6 for w in u1.values()) and m['szekkihuzas_min_m'] >= 0.90 - 1e-6 and m['kanape_TV_butor_m'] >= 0.60 - 1e-6
    return dict(stilus=st, D=D, cx=cx, cy=cy, rot0=rot0, tv=tv, ok=ok, kihuzas=m['szekkihuzas_m'], kihuzas_min=m['szekkihuzas_min_m'], kihuzas_fuggony_min=min(kf),
                utak=u1, ulo=m['ut_ulo_vendegekkel_m'], ML04=m['ML04_eltetes_m'], szek_kanape=m['betolt_szek_kanape_m'])
if __name__ == '__main__':
    res = []
    for st in ('S01', 'S02'):
        for D in (1.50, 1.40, 1.30, 1.20):
            best = None
            for cx in (8.35, 8.45, 8.55, 8.65):
                for cy in (6.05, 6.15, 6.25, 6.35):
                    for rot0 in (0, 30):
                        r = eset(st, D, cx, cy, rot0, 0.60)
                        res.append(r)
                        sc = (r['ok'], r['kihuzas_fuggony_min'], min(x or 0 for x in r['ulo'].values()), -r['ML04'])
                        if best is None or sc > best[0]: best = (sc, r)
            r = best[1]
            print(st, f"Ø{D:.2f}", 'OK ' if r['ok'] else 'NEM', f"c=({r['cx']},{r['cy']}) rot{r['rot0']}", 'kih min', r['kihuzas_min'], 'függ', r['kihuzas_fuggony_min'],
                  'utak', [x for x in r['utak'].values()], 'ülő', [x for x in r['ulo'].values()], 'ML04', r['ML04'], 'szék–kanapé', r['szek_kanape'])
    json.dump(res, open(os.path.join(HERE, 'c_kerek.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
