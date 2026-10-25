# =====================================================================================
# A-902 elrendezési alternatívák – érzékenységvizsgálat: mélyebb TV-fal-bútor (40 → 60 cm) a kanapé előtt (Claude, 2026-10-25 03:56 CET)
# Miért: az elrendezes_alt_a902.py 40 cm mély TV-bútorsávval számol; az Astra V3.1-brief (r2, §11.4) a W01-en
# legfeljebb 60 cm mély, mennyezetig érő zárt szekrényt is megenged.
# Módszer: ugyanaz a motor és ugyanazok a kötelező méretek; a bútorsáv mélysége 40–60 cm a kanapé teljes hossza előtt;
# a kanapé legfeljebb 30 cm-rel keletebbre mehet; az asztal és a székek helye változatlan.
# Futtatás: python3 tv_melyseg.py  → tv_melyseg.json  (MÉRETPRÓBA, terv szerinti geometria, helyszínen nem mért)
# =====================================================================================
import os, sys, json, importlib.util
from shapely.geometry import box
HERE = os.path.dirname(os.path.abspath(__file__))
ENG = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'elrendezes_alt_a902.py')
OUT = sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, 'tv_melyseg.json')
spec = importlib.util.spec_from_file_location('eng', ENG); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
V = E.valtozatok()
KZ = {'S01': 1.80, 'S02': 1.60}   # a kanapé legnyugatibb pontja XB-től (Lennon fekvőrész vége / JÄTTEBO karfavégek)
out = []
for v0 in V:
    if v0['kod'] == 'R': continue
    st = v0['stilus']
    for d in (0.40, 0.45, 0.50, 0.55, 0.60):
        E.TV_ZONA = box(3.67, 4.25, 3.67 + d, 7.65)
        xb_min = round(3.67 + d + 0.60 + KZ[st], 3)
        best = None
        for k in range(0, 31):
            XB = round(max(v0['XB'], xb_min) + 0.01 * k, 3)
            v = dict(v0); v['XB'] = XB; v['kanape'] = E.lennon_L(XB) if st == 'S01' else E.jattebo_U(XB)
            m, b, u = E.meres(v)
            u1 = m['ut_betolt_szekkel_m']
            ok = all((w or 0) >= 0.90 - 1e-6 for w in u1.values()) and m['szekkihuzas_min_m'] >= 0.90 - 1e-6 and m['kanape_TV_butor_m'] >= 0.60 - 1e-6
            if ok:
                best = dict(XB=XB, eltolas_kelet_m=round(XB - v0['XB'], 2), szek_kanape=m['betolt_szek_kanape_m'], kanape_TV=m['kanape_TV_butor_m'],
                            nezotav_fali_TV=m['nezotav_m'], utak=u1, ulo=m['ut_ulo_vendegekkel_m'], kihuzas_min=m['szekkihuzas_min_m'])
                break
        out.append(dict(alt=v0['kod'], stilus=st, tv_mely_m=d, eredeti_XB=v0['XB'], megoldas=best))
        r = best
        print(f"{v0['kod']} {st} TV {d:.2f}: " + ("NINCS megoldás (XB ≤ +0,30)" if not r else
              f"OK XB {r['XB']:.2f} (kelet +{r['eltolas_kelet_m']:.2f}) szék–kanapé {r['szek_kanape']:.2f} kanapé–TV {r['kanape_TV']:.2f} nézőtáv {r['nezotav_fali_TV']:.2f} "
              f"utak {[round(x or 0,2) for x in r['utak'].values()]} ülő {[round(x or 0,2) for x in r['ulo'].values()]}"))
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
