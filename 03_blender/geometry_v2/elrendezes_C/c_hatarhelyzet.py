# =====================================================================================
# A-902 – C elrendezés határhelyzetei (Claude, 2026-10-25, Péter 04:08 CET feltételei)
# - északi (és keleti) székkihúzás behúzott függönnyel is (függöny: a szemöldök belső síkján, y 8,05; 12 cm-es sáv, x 4,44–8,94 – becslés);
# - az asztal kis eltolása (dx, dy) – mennyit javul a kihúzás, mit ront az utakon, hol marad az ML04;
# - TV-fal-bútor 40 és 60 cm; a kanapé végleges helye (S01 XB 6,67 – 60 cm-es TV-szekrénnyel is jó; S02 XB 6,60).
# Motor: ../elrendezes_alt/elrendezes_alt_a902.py (MÉRETPRÓBA, terv szerinti geometria, helyszínen nem mért)
# =====================================================================================
import os, sys, json, math, importlib.util
from shapely.geometry import box, Point
HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('eng', os.path.join(HERE, '..', 'elrendezes_alt', 'elrendezes_alt_a902.py'))
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
FUGGONY = (4.44, 7.93, 8.94, 8.05)
PULT0 = list(E.PULT)
XB_VEGLEGES = {'S01': 6.67, 'S02': 6.60}

def valtozat(st, dx, dy):
    v0 = [v for v in E.valtozatok() if v['kod'] == 'C' and v['stilus'] == st][0]
    v = dict(v0); XB = XB_VEGLEGES[st]; v['XB'] = XB
    v['kanape'] = E.lennon_L(XB) if st == 'S01' else E.jattebo_U(XB)
    x0, y0, x1, y1 = v0['asztal'].bounds
    v['asztal'] = box(x0 + dx, y0 + dy, x1 + dx, y1 + dy)
    v['szekek'] = [(cx + dx, cy + dy, nx, ny) for (cx, cy, nx, ny) in v0['szekek']]
    return v

def mer(st, dx, dy, tv):
    E.TV_ZONA = box(3.67, 4.25, 3.67 + tv, 7.65)
    v = valtozat(st, dx, dy)
    E.PULT = PULT0; m, b, u = E.meres(v)
    E.PULT = PULT0 + [FUGGONY]; kf = E.kihuzas(v); E.PULT = PULT0
    u1, u2 = m['ut_betolt_szekkel_m'], m['ut_ulo_vendegekkel_m']
    ok = all((w or 0) >= 0.90 - 1e-6 for w in u1.values()) and m['szekkihuzas_min_m'] >= 0.90 - 1e-6 and m['kanape_TV_butor_m'] >= 0.60 - 1e-6
    return dict(stilus=st, dx=dx, dy=dy, tv_mely=tv, XB=v['XB'], kotelezo_ok=ok, asztal=[round(c, 3) for c in v['asztal'].bounds],
                kihuzas=m['szekkihuzas_m'], kihuzas_fuggonnyel=kf, eszaki_kihuzas=m['szekkihuzas_m'][5], eszaki_fuggonnyel=kf[5],
                utak_betolt=u1, utak_ulo=u2, szek_kanape=m['betolt_szek_kanape_m'], kanape_TV=m['kanape_TV_butor_m'], nezotav=m['nezotav_m'],
                ML04=m['ML04_eltetes_m'], huto_sarok=m['etkezo_huto_sarok_m'])

if __name__ == '__main__':
    res = []
    for st in ('S01', 'S02'):
        for tv in (0.40, 0.60):
            for dy in (0.0, -0.05, -0.10, -0.15, -0.20):
                for dx in (-0.10, -0.05, 0.0, 0.05):
                    r = mer(st, dx, dy, tv); res.append(r)
    json.dump(res, open(os.path.join(HERE, 'c_hatarhelyzet.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    f = lambda d: '/'.join(f"{(x or 0):.2f}" for x in d.values())
    for r in res:
        print(f"{r['stilus']} TV{r['tv_mely']:.2f} dx{r['dx']:+.2f} dy{r['dy']:+.2f} {'OK ' if r['kotelezo_ok'] else 'NEM'} É-kih {r['eszaki_kihuzas']:.2f}/{r['eszaki_fuggonnyel']:.2f}f min {min(r['kihuzas']):.2f}/{min(r['kihuzas_fuggonnyel']):.2f}f "
              f"betolt[t/k/f/05] {f(r['utak_betolt'])} ulo {f(r['utak_ulo'])} ML04 {r['ML04']:.2f} szék–kanapé {r['szek_kanape']:.2f} TV {r['kanape_TV']:.2f}")
