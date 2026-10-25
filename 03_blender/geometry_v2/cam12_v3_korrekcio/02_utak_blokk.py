# Cam_12 v3 korrekció – S01/S02 tömbök közlekedő- és távolságmérése (2D, shapely), a C elrendezés motorjával
# (../elrendezes_alt/elrendezes_alt_a902.py), de a FABLE-konyhával (keleti sor 9,93–10,55 × 1,35–4,10; nyugati sor 8,45–9,07 × 2,35–4,05;
# hűtőoszlop a W03-a előtt 10,13–10,75 × 5,05–5,65) és a Fable TV-fal-bútorával. Claude, 2026-10-25. MÉRETPRÓBA, terv szerinti geometria.
import os, sys, json, importlib.util
from shapely.geometry import box, Point
from shapely.ops import unary_union
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
# a motor a competition/baseline-20261025-v3 (és fable51) ágon van: 03_blender/geometry_v2/elrendezes_alt/elrendezes_alt_a902.py (a main-en nincs)
MOTOR = os.environ.get('WSG_ELRENDEZES_MOTOR', os.path.join(HERE, '..', 'elrendezes_alt', 'elrendezes_alt_a902.py'))
spec = importlib.util.spec_from_file_location('eng', MOTOR)
E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
import blokk_spec as BS
PULT_F = [(9.93, 1.35, 10.55, 4.10), (8.45, 2.35, 9.07, 4.05), (10.13, 5.05, 10.75, 5.65)]
E.PULT = PULT_F
E.W = unary_union([box(*r) for k in E.JARHATO for r in E.LOCK['rooms'][k]]).difference(unary_union([box(*r) for r in PULT_F]))
TV = {'S01': unary_union([box(3.67, 4.05, 4.12, 5.25), box(3.67, 5.25, 4.07, 7.65), box(3.67, 5.25, 3.71, 8.05)]),
      'S02': unary_union([box(3.67, 7.15, 4.12, 8.05), box(3.67, 4.20, 4.07, 6.90), box(3.67, 4.05, 3.73, 4.20), box(3.67, 4.20, 3.71, 6.90)])}
DOH = {'S01': box(4.67, 6.275, 5.27, 7.475), 'S02': Point(5.15, 6.40).buffer(0.40, quad_segs=32)}
CAMSPOT = box(4.30, 7.75, 4.50, 8.05)
SZEKEK = [(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]
out = {}
for st in ('S01', 'S02'):
    XB = 6.67 if st == 'S01' else 6.60
    S = E.lennon_L(XB) if st == 'S01' else E.jattebo_U(XB)
    T = Point(0, 0).buffer(1.0, quad_segs=32)
    from shapely import affinity
    T = affinity.translate(affinity.scale(T, 0.45, 0.80), 8.45, 6.20)    # Toni 160×90 ovális (ellipszis-közelítés)
    v = dict(kod='C', stilus=st, XB=XB, kanape=S, asztal=T, szekek=SZEKEK, kerek=False)
    E.TV_ZONA = TV[st]
    m, betolt, ulo = E.meres(v)
    kf = None
    E.PULT = PULT_F + [(4.44, 7.93, 8.94, 8.05)]; kf = E.kihuzas(v); E.PULT = PULT_F
    D = DOH[st]
    # utak a dohányzóasztallal együtt (a motor nem tartalmazza)
    u_doh = E.ut_szelesseg([S, T, TV[st], D] + betolt)
    r = dict(kanape=('Lennon L' if st == 'S01' else 'JÄTTEBO U'), XB=XB,
             utak_betolt_szekkel=m['ut_betolt_szekkel_m'], utak_ulo_vendegekkel=m['ut_ulo_vendegekkel_m'], utak_betolt_doh_asztallal=u_doh,
             szekkihuzas=m['szekkihuzas_m'], szekkihuzas_fuggonnyel=kf, kanape_TV_butor=m['kanape_TV_butor_m'], nezotav=m['nezotav_m'],
             betolt_szek_kanape=m['betolt_szek_kanape_m'], ML04_asztalkozep=m['ML04_eltetes_m'], kanape_uveg=m['kanape_uveg_m'],
             doh_kanape=round(D.distance(S), 3), doh_TV=round(D.distance(TV[st]), 3), kamera_allohely_szabad=not CAMSPOT.intersects(unary_union([S, D, TV[st]])),
             huto_oszlop_asztal_szek=round(box(10.13, 5.05, 10.75, 5.65).distance(unary_union([T] + betolt)), 3),
             huto_ajto_kezelosav_szabad=not box(9.53, 5.05, 10.13, 5.65).intersects(unary_union([T] + betolt)),
             konyha_pultkoz=round(9.93 - 9.07, 3))
    r['kotelezo'] = dict(fo_utak_090=all((w or 0) >= 0.90 - 1e-6 for w in u_doh.values()), szekkihuzas_090=min(m['szekkihuzas_m']) >= 0.90 - 1e-6,
                         kanape_TV_060=m['kanape_TV_butor_m'] >= 0.60 - 1e-6, doh_kanape_045=r['doh_kanape'] >= 0.45 - 1e-6, doh_TV_060=r['doh_TV'] >= 0.60 - 1e-6)
    out[st] = r
json.dump(out, open(os.path.join(HERE, 'utak_blokk_S01_S02.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
