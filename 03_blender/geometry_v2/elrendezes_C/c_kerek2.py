# Kerek asztal 2. kör: szélesebb középpont-tartomány, és a kanapé a TV-fal mélységéhez szükséges legnyugatibb helyen (XB = 3,67 + TV + 0,60 + kanapémélység).
import os, sys, json
from shapely.geometry import box
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import c_hatarhelyzet as H, c_kerek as K
E = H.E
MELY = {'S01': 1.80, 'S02': 1.60}
res = []; best = {}
for st in ('S01', 'S02'):
    for tv in (0.04, 0.40, 0.60):
        H.XB_VEGLEGES[st] = round(3.67 + tv + 0.60 + MELY[st], 2)
        for D in (1.50, 1.40, 1.30, 1.20):
            for cx in (8.15, 8.25, 8.35, 8.45, 8.55):
                for cy in (6.05, 6.20, 6.35, 6.50, 6.65):
                    for rot0 in (0, 30):
                        r = K.eset(st, D, cx, cy, rot0, tv); r['XB'] = H.XB_VEGLEGES[st]; res.append(r)
                        sc = (r['ok'], min(r['kihuzas_fuggony_min'], 0.95), min((x or 0) for x in r['ulo'].values()), -r['ML04'])
                        k = (st, tv, D)
                        if k not in best or sc > best[k][0]: best[k] = (sc, r)
for (st, tv, D), (sc, r) in sorted(best.items()):
    print(st, f"TV{tv:.2f} XB{r['XB']:.2f} Ø{D:.2f}", 'OK ' if r['ok'] else 'NEM', f"c=({r['cx']},{r['cy']}) rot{r['rot0']}", 'kih', r['kihuzas_min'], 'függ', r['kihuzas_fuggony_min'],
          'utak', list(r['utak'].values()), 'ülő', list(r['ulo'].values()), 'ML04', r['ML04'], 'sz–k', r['szek_kanape'])
json.dump(res, open(os.path.join(HERE, 'c_kerek2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
