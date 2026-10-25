# Gyors keresés: melyik kanapé-hely (XB) és asztalközép (cx, cy) adja a legjobb utakat családonként (A hosszanti, B keresztbe, C kerek).
import json, math, itertools, time, sys
import numpy as np
from shapely.geometry import box, Point
from shapely.ops import unary_union
import elrendezes_alt_a902 as E

TVD = float(sys.argv[1]) if len(sys.argv) > 1 else 0.45
E.TV_ZONA = box(3.67, 4.25, 3.67 + TVD, 7.65)

def epit(st, csalad, XB, cx, cy):
    s = E.SZEK[st]
    kan = E.lennon_L(XB) if st == 'S01' else E.jattebo_U(XB)
    if csalad == 'A':
        Lh = 2.00 if st == 'S01' else 1.80; poz = (cy - 0.67, cy, cy + 0.67) if st == 'S01' else (cy - 0.60, cy, cy + 0.60)
        T, sz = E.etkezo_teglalap(cx - 0.45, cy - Lh / 2, cx + 0.45, cy + Lh / 2, 'y', poz, s['sz'], s['mely'])
    elif csalad == 'B':
        Lh = 2.00 if st == 'S01' else 1.80; poz = (cx - 0.65, cx, cx + 0.65) if st == 'S01' else (cx - 0.60, cx, cx + 0.60)
        T, sz = E.etkezo_teglalap(cx - Lh / 2, cy - 0.45, cx + Lh / 2, cy + 0.45, 'x', poz, s['sz'], s['mely'])
    else:
        T, sz = E.etkezo_kerek(cx, cy, 0.75, (30, 90, 150, 210, 270, 330))
    return dict(kod=csalad, stilus=st, XB=XB, kanape=kan, asztal=T, szekek=sz, kerek=(csalad == 'C'), cim='', kanape_nev='', asztal_nev='')

def gyors(v):
    S, T = v['kanape'], v['asztal']
    if S.distance(E.TV_ZONA) < 0.60 - 1e-6: return None
    if (v['XB'] - E.SZEM) - E.KEPERNYO_X < 2.0 - 1e-6: return None
    if not E.W.buffer(1e-6).contains(T): return None
    bet = E.szek_poligonok(v, 'betolt')
    if unary_union(bet).intersects(S) or not all(E.W.buffer(1e-6).contains(g) for g in bet): return None
    kh = E.kihuzas(v)
    if min(kh) < 0.90 - 1e-6: return None
    return bet, kh

if __name__ == '__main__':
    t0 = time.time(); best = {}
    for st in ('S01', 'S02'):
        for cs in ('A', 'B', 'C'):
            cands = []
            XBs = np.round(np.arange(6.20, 7.05, 0.05), 2)
            cxs = np.round(np.arange(7.60, 9.00, 0.05), 2); cys = np.round(np.arange(5.95, 6.70, 0.05), 2)
            for XB, cx, cy in itertools.product(XBs, cxs, cys):
                v = epit(st, cs, float(XB), float(cx), float(cy)); g = gyors(v)
                if g is None: continue
                bet, kh = g
                u = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + bet)
                if any(x is None for x in u.values()): continue
                mn = min(u.values())
                cands.append((mn, -abs(v['asztal'].centroid.distance(Point(*E.ML04))), float(XB), float(cx), float(cy), u, min(kh)))
            cands.sort(key=lambda c: (c[0], c[1]), reverse=True)
            best[(st, cs)] = cands[:5]
            print(st, cs, len(cands), 'legjobb:', [(c[0], round(-c[1], 2), c[2], c[3], c[4], c[6]) for c in cands[:5]], f'{time.time() - t0:.0f}s', flush=True)
    json.dump({f'{k[0]}_{k[1]}': [dict(min_ut=c[0], ML04=round(-c[1], 3), XB=c[2], cx=c[3], cy=c[4], utak=c[5], kihuzas_min=c[6]) for c in v] for k, v in best.items()},
              open(f'opt_alt_TV{int(TVD*100)}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
