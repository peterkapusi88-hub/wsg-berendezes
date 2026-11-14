# Ha csak a legkeletibb, 0,93 m-es teraszszárny (x 7,98–8,91) nyílik: mely hatszemélyes elrendezés tartja meg a terasz elérését (≥ 0,90 m betolt székkel)?
import os, sys, json
from shapely.geometry import box
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import c_hatarhelyzet as H
E = H.E
KELETI = box(7.98, 7.55, 8.91, 8.05)
def mer(v, tv=0.60):
    E.TV_ZONA = box(3.67, 4.25, 3.67 + tv, 7.65)
    E.CELOK['terasz_keleti_szarny'] = KELETI
    m, b, u = E.meres(v); del E.CELOK['terasz_keleti_szarny']
    E.CELOK['terasz_keleti_szarny'] = KELETI
    kk = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + b)['terasz_keleti_szarny']; ku = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + u)['terasz_keleti_szarny']
    del E.CELOK['terasz_keleti_szarny']
    u1 = m['ut_betolt_szekkel_m']
    ok = all((w or 0) >= 0.90 - 1e-6 for w in u1.values()) and m['szekkihuzas_min_m'] >= 0.90 - 1e-6 and m['kanape_TV_butor_m'] >= 0.60 - 1e-6 and (kk or 0) >= 0.90 - 1e-6
    return dict(ok=ok, keleti_betolt=kk, keleti_ulo=ku, utak=u1, ulo=m['ut_ulo_vendegekkel_m'], kih=m['szekkihuzas_min_m'], ML04=m['ML04_eltetes_m'], asztal=[round(c, 2) for c in v['asztal'].bounds])
res = []
for st in ('S01', 'S02'):
    for L in (1.60, 1.80):
        for dx in (-0.20, -0.10, 0.0):
            for dy in (0.0, -0.10, -0.20, -0.30):
                for elrend in ('2+2+1+1', '3+3'):
                    v = H.valtozat(st, 0, 0); cx, cy = 8.45 + dx, 6.20 + dy
                    v['asztal'] = box(cx - 0.45, cy - L / 2, cx + 0.45, cy + L / 2)
                    if elrend == '2+2+1+1':
                        v['szekek'] = [(cx - 0.45, cy - 0.10, -1, 0), (cx - 0.45, cy + 0.50, -1, 0), (cx + 0.45, cy - 0.10, 1, 0), (cx + 0.45, cy + 0.50, 1, 0), (cx, cy - L / 2, 0, -1), (cx, cy + L / 2, 0, 1)]
                    else:
                        if L < 1.79: continue
                        v['szekek'] = [(cx - 0.45, cy + d, -1, 0) for d in (-0.60, 0.0, 0.60)] + [(cx + 0.45, cy + d, 1, 0) for d in (-0.60, 0.0, 0.60)]
                    r = mer(v); r.update(stilus=st, L=L, dx=dx, dy=dy, elrend=elrend); res.append(r)
for r in res:
    if r['ok']: print('OK ', r['stilus'], r['elrend'], f"L{r['L']:.2f} dx{r['dx']:+.2f} dy{r['dy']:+.2f}", 'keleti', r['keleti_betolt'], '/', r['keleti_ulo'], 'utak', list(r['utak'].values()), 'ülő', list(r['ulo'].values()), 'kih', r['kih'], 'ML04', r['ML04'])
best = {}
for r in res:
    k = (r['stilus'], r['elrend'], r['L'])
    s = ((r['keleti_betolt'] or 0), min((x or 0) for x in r['utak'].values()))
    if k not in best or s > best[k][0]: best[k] = (s, r)
for k, (s, r) in best.items(): print('legjobb', k, r['ok'], 'keleti', r['keleti_betolt'], 'utak', list(r['utak'].values()), 'dx', r['dx'], 'dy', r['dy'], 'ML04', r['ML04'])
json.dump(res, open(os.path.join(HERE, 'c_keleti_szarny.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
