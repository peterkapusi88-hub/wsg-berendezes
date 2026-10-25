# S02 BiBo konyha (U és A változat) – 2D: pultközök, utak (betolt széknél), a 05.3 ajtó felé maradó út az asztal eltolásával,
# kiállás-ütközések (A902_villamos.csv), kapcsoló-áthelyezési számítás. Claude, 2026-10-25. MÉRETPRÓBA, terv szerinti geometria.
import os, sys, json, csv, importlib.util
from shapely.geometry import box, Point
from shapely.ops import unary_union
from shapely import affinity
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
MOTOR = os.environ.get('WSG_ELRENDEZES_MOTOR', os.path.join(HERE, '..', 'elrendezes_alt', 'elrendezes_alt_a902.py'))
spec = importlib.util.spec_from_file_location('eng', MOTOR); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
KV = {r['azonosito']: r for r in csv.DictReader(open(os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.csv'), encoding='utf-8'))}
import bibo_spec as BS
HUTO = (10.13, 5.05, 10.75, 5.65)
PULT = {'U': [(9.93, 1.35, 10.55, 4.10), (9.05, 1.35, 9.93, 1.97), (8.45, 2.35, 9.07, 2.95), (8.45, 2.95, 9.07, 4.05), HUTO],
        'A': [(9.93, 1.35, 10.55, 4.10), (9.05, 1.35, 9.93, 1.97), (8.45, 2.35, 9.07, 4.05), HUTO]}
TV = unary_union([box(3.67, 7.15, 4.12, 8.05), box(3.67, 4.20, 4.07, 6.90), box(3.67, 4.05, 3.73, 4.20)])
SZEKEK = [(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]
out = dict(valtozatok={}, kiallasok={}, kapcsolo_athelyezes={})
for v, P in PULT.items():
    E.PULT = P
    E.W = unary_union([box(*r) for k in E.JARHATO for r in E.LOCK['rooms'][k]]).difference(unary_union([box(*r) for r in P]))
    E.TV_ZONA = TV
    res = {}
    for dx in (0.0, -0.05, -0.10):
        T = affinity.translate(affinity.scale(Point(0, 0).buffer(1.0, quad_segs=32), 0.45, 0.80), 8.45 + dx, 6.20)
        sz = [(cx + dx, cy, nx, ny) for (cx, cy, nx, ny) in SZEKEK]
        vv = dict(kod='C', stilus='S02', XB=6.60, kanape=E.jattebo_U(6.60), asztal=T, szekek=sz, kerek=False)
        m, betolt, ulo = E.meres(vv)
        res[f'dx{dx:+.2f}'] = dict(utak_betolt=m['ut_betolt_szekkel_m'], utak_ulo=m['ut_ulo_vendegekkel_m'], szekkihuzas=m['szekkihuzas_m'],
                                   huto_oszlop_szek_asztal=round(box(*HUTO).distance(unary_union([T] + betolt)), 3), szek_kanape=m['betolt_szek_kanape_m'],
                                   ML04_asztalkozep=round(T.centroid.distance(Point(8.549, 6.274)), 3))
    # pultközök
    if v == 'U':
        koz = dict(eszaki_resz_K_NY=round(9.93 - 9.07, 3), oszlop_elott=round(9.93 - 9.07, 3), deli_resz_pillér_K=round(9.93 - 9.05, 3), deli_pult_elott_melyseg_a_pillersarokig=round(2.35 - 1.97, 3))
    else:
        koz = dict(eszaki_resz_K_NY=round(9.93 - 9.07, 3), deli_resz_pillér_K=round(9.93 - 9.05, 3), geposzlop_elott=round(4.05 - 1.97, 3))
    out['valtozatok'][v] = dict(utak=res, pultkoz=koz)
# kiállások vs tömbök (2D + magasság), saját szabállyal (a validátor ±12 cm-es körzete a fal túloldalát is beveszi)
def z_of(r):
    try: return float(r['magassag_m'])
    except Exception: return None
CHK = ['A902-K02', 'A902-K03', 'A902-K07', 'A902-K08', 'A902-K09', 'A902-D12', 'A902-D13', 'A902-FL01', 'A902-ML03', 'A902-D02', 'A902-D03', 'A902-D04', 'A902-D05', 'A902-D06', 'A902-D07', 'A902-D08', 'A902-D09', 'A902-D10', 'A902-D14', 'A902-X01']
for v in ('U', 'A'):
    tomb = [e for e in BS.K(v) if e['tipus'] == 'box']
    rr = {}
    for k in CHK:
        r = KV[k]; x = float(r['doboz_x_m'] or r['x_m']); y = float(r['doboz_y_m'] or r['y_m']); z = z_of(r)
        hits = []
        for e in tomb:
            x0, y0, z0, x1, y1, z1 = e['g']
            if x0 - 0.05 <= x <= x1 + 0.05 and y0 - 0.05 <= y <= y1 + 0.05:
                hits.append(dict(id=e['id'], z=[z0, z1]))
        rr[k] = dict(tipus=r['tipus'], kod=r['kod'], x=x, y=y, z=z, tombok=hits)
    out['kiallasok'][v] = rr
# kapcsolócsoport (K07, K08, K09, D12 közös szerelvényhely: x 10,734; y 5,65) – mennyit kell mozdítani
oszlop_eszaki_el = HUTO[3]
for nev, szel in (('függőleges 4-es keret (≈ 8 cm széles) – a 045 fotón függőleges oszlop', 0.08), ('vízszintes 4-es keret (≈ 29 cm)', 0.29)):
    kozep_min = oszlop_eszaki_el + szel / 2 + 0.02
    out['kapcsolo_athelyezes'][nev] = dict(uj_kozep_min_y=round(kozep_min, 3), elmozdulas_eszakra_min_cm=round((kozep_min - 5.65) * 100, 1),
                                         keret_y=[round(kozep_min - szel / 2, 3), round(kozep_min + szel / 2, 3)], ajto_tok_modell_y=6.05,
                                         megj='a valós ajtótok-borítás szélessége ismeretlen (a modellben nincs); becslés 6–8 cm → szabad falsáv kb. 5,65–5,97')
out['kapcsolo_athelyezes']['alternatíva: K-csonk nyugati lapja'] = dict(uj_hely='x 10,55 · y ≈ 4,90 (a K-csonk északi végétől 15 cm), z mint most', elmozdulas='≈ 0,75 m délre + 0,20 m a visszaugrás körül',
                                                                      feltetel='a keleti sor y 4,10-nél ér véget, a K-csonk 0,95 m-es lapja szabad; a tükörsáv csonkítatlan marad')
out['oszlop_max_szelesseg_athelyezes_nelkul_m'] = round((5.65 - 0.04 - 0.01) - 5.05, 3)
json.dump(out, open(os.path.join(HERE, 'utak_kiallasok_bibo.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({v: {k: d['utak_betolt'] | {'huto': d['huto_oszlop_szek_asztal']} for k, d in out['valtozatok'][v]['utak'].items()} for v in out['valtozatok']}, ensure_ascii=False, indent=1))
for v in ('U', 'A'):
    print(v, {k: [h['id'] for h in d['tombok']] for k, d in out['kiallasok'][v].items() if d['tombok']})
print(out['kapcsolo_athelyezes'], out['oszlop_max_szelesseg_athelyezes_nelkul_m'])
