# =====================================================================================
# Integrátori méretpróba – Opus 5.5 V3.1 (PR #22) S01 Kyoto Ink / S02 BiBo Nocturne, 2D közlekedés (Claude integrátor, 2026-10-25)
# Motor: ../geometry_v2/elrendezes_alt/elrendezes_alt_a902.py (csak olvasva; a Linux-fontútvonal macOS-re cserélve, semmi más).
# Bemenet: az Opus-ág b24bee7 S01/S02 specifikációja és Cam_02/Cam_12 promptja (a 7d3c67f-et a munkamenet nem érte el).
# Esetek: (1) Opus-alap, (2) + a promptban leírt, de nem méretezett dohányzóasztal (feltételezett méret), (3) + a W02 melletti
# növény (feltételezett Ø45 cm-es kaspó), (4) S02: + a 1,8 cm-es navy lábazati sáv; teraszajtó: középső szárny / csak keleti
# 0,93 m-es szárny; a keleti esetben 5+1 is. MÉRETPRÓBA – terv szerinti geometria, helyszínen nem mért.
# Futtatás: <venv>/bin/python 01_kozlekedes_2d_opus_S01_S02.py  → 01_kozlekedes_2d_opus_S01_S02.json
# =====================================================================================
import os, sys, json, types, copy
from shapely.geometry import box, Point
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
ENG = os.path.join(HERE, '..', 'geometry_v2', 'elrendezes_alt', 'elrendezes_alt_a902.py')
src = open(ENG, encoding='utf-8').read()
src = src.replace('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf')
src = src.replace('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf')
E = types.ModuleType('eng'); E.__file__ = os.path.abspath(ENG); exec(compile(src, ENG, 'exec'), E.__dict__)

FUGGONY_SZEMOLDOK = box(4.44, 7.93, 8.94, 8.05)          # c_hatarhelyzet.py: függöny a szemöldök belső síkján (becslés)
TERASZ_KOZEPSO = E.CELOK['terasz (tolóajtó, keleti rész)']  # a motor alapcélja (6,69–8,94)
TERASZ_KELETI = box(7.98, 7.55, 8.91, 8.05)               # c_keleti_szarny.py: csak a legkeletibb 0,93 m-es szárny
SZEKEK_C = [(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]
TONI160 = (8.00, 5.40, 8.90, 7.00)

# --- TV-falak az Opus 30_TV_FAL_KONCEPCIOK szerint (koordinátát Opus nem adott – integrátori hozzárendelés)
TV_KI_A = unary_union([box(3.67, 4.05, 3.71, 8.05),       # KI-A3 washi-panelmező ≤ 4 cm
                       box(3.67, 4.45, 4.11, 5.05),       # KI-A2 torony 60 × 40 a D18 (y 4,75) előtt, a panel elé állítva
                       box(3.71, 5.05, 4.13, 7.65)])      # KI-A1 úszó pad 260 × 42, az üvegsarok előtt 40 cm-rel végződik
TV_BN_A = unary_union([box(3.67, 4.05, 4.12, 4.85),       # BN-A1 déli kabinet 80 × 45 a D18 előtt
                       box(3.67, 7.35, 4.07, 8.05),       # BN-A2 északi kabinet 70 × 40 az üvegsaroknál
                       box(3.67, 4.85, 3.71, 7.35),       # BN-A3 ezüst textilmező ≤ 4 cm
                       box(3.71, 5.00, 4.11, 7.20)])      # BN-A4 úszó pad 220 × 40 (a két tükörrés között középen)

def alap(st):
    if st == 'S01':
        return dict(stilus='S01', XB=6.67, kanape=E.lennon_L(6.67), kanape_nev='Westwing Lennon jobbos L 238×180',
                    asztal=box(*TONI160), asztal_nev='Westwing Toni ovális 160×90 (befoglaló)', szekek=list(SZEKEK_C), kerek=False, tv=TV_KI_A)
    return dict(stilus='S02', XB=6.60, kanape=E.jattebo_U(6.60), kanape_nev='IKEA JÄTTEBO U 285×160',
                asztal=box(*TONI160), asztal_nev='Westwing Toni ovális 160×90, fekete (befoglaló; a fekete változat nem igazolt)', szekek=list(SZEKEK_C), kerek=False, tv=TV_BN_A)

EXTRA = {
    # S01: „low round dark-wood coffee table about 45–50 cm in front of the sofa” – méret nincs; feltételezés Ø80, a fő ülés elé
    'S01_dohanyzoasztal_O80': lambda: Point(5.72 - 0.47 - 0.40, 6.85).buffer(0.40, quad_segs=24),
    # S02: „oval smoked-glass coffee table 45–50 cm in front of the seat inside the U” – a U belseje csak 0,95 × 0,65 m;
    # feltételezés 60 × 60, a U szájában (a hátsó ülés elejétől 0,45 m)
    'S02_dohanyzoasztal_60x60': lambda: box(4.60, 6.10, 5.20, 6.70),
    # „one tall plant … in the south-west corner beside W02” / „tall olive tree … in the corner beside W02” – Ø45 kaspó
    'noveny_W02_DNy_sarok_O45': lambda: Point(5.45, 4.05 + 0.225 + 0.01).buffer(0.225, quad_segs=24),
    # S02 navy lábazati sáv: 1,8 cm a W02 teljes hosszán
    'S02_navy_labazat_18mm': lambda: box(5.18, 4.05, 7.32, 4.068),
    # S01 W02-mű: 4 cm mély keret, alsó éle z 0,45 (a padlószinti szabály szerint ≤ 4 cm) – a kapcsolóoszloptól ≥ 30 cm-re
    'S01_W02_mu_4cm': lambda: box(5.30, 4.05, 6.50, 4.09),
}

def mer(v, extra, terasz, otperegy=False, fuggony=False):
    v = dict(v); v['szekek'] = [s for s in v['szekek'] if not (otperegy and s == (8.45, 7.00, 0, 1))]
    E.TV_ZONA = v['tv']
    akad_extra = [EXTRA[k]() for k in extra]
    cel_tmp = dict(E.CELOK)
    E.CELOK = {k: g for k, g in cel_tmp.items() if k != 'terasz (tolóajtó, keleti rész)'}
    E.CELOK['terasz'] = TERASZ_KOZEPSO if terasz == 'kozepso' else TERASZ_KELETI
    pult0 = list(E.PULT)
    if fuggony: E.PULT = pult0 + [FUGGONY_SZEMOLDOK.bounds]
    try:
        m, betolt, ulo = E.meres(v)
        u1 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + betolt + akad_extra)
        u2 = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + ulo + akad_extra)
        kih = E.kihuzas(v)
    finally:
        E.CELOK = cel_tmp; E.PULT = pult0
    tv_front = max(g.bounds[2] for g in (getattr(v['tv'], 'geoms', None) or [v['tv']]))
    r = dict(stilus=v['stilus'], extra=extra, terasz=terasz, ules='5+1' if otperegy else '2+2+1+1', fuggony_szemoldokben=fuggony,
             utak_betolt_szekkel=u1, utak_ulo_vendegekkel=u2, szekkihuzas=kih, szekkihuzas_min=min(kih),
             kanape_TV_butor=round(v['kanape'].distance(E.TV_ZONA), 3), tv_butor_front_x=round(tv_front, 3),
             nezotav=m['nezotav_m'], ML04_eltetes=m['ML04_eltetes_m'], kanape_uveg=m['kanape_uveg_m'],
             W02_kanape_tav=round(v['kanape'].distance(box(5.18, 4.00, 7.32, 4.05)), 3),
             extra_kanape_tav={k: round(EXTRA[k]().distance(v['kanape']), 3) for k in extra},
             extra_TV_tav={k: round(EXTRA[k]().distance(E.TV_ZONA), 3) for k in extra})
    r['fo_utak_ok'] = all((w or 0) >= 0.90 - 1e-6 for w in u1.values())
    r['kotelezo_ok'] = r['fo_utak_ok'] and r['szekkihuzas_min'] >= 0.90 - 1e-6 and r['kanape_TV_butor'] >= 0.60 - 1e-6
    return r

ESETEK = []
for st in ('S01', 'S02'):
    v = alap(st)
    dohany = 'S01_dohanyzoasztal_O80' if st == 'S01' else 'S02_dohanyzoasztal_60x60'
    falsav = ['S01_W02_mu_4cm'] if st == 'S01' else ['S02_navy_labazat_18mm']
    for terasz in ('kozepso', 'keleti'):
        for extra in ([], [dohany], falsav, falsav + [dohany], falsav + [dohany, 'noveny_W02_DNy_sarok_O45']):
            ESETEK.append(mer(v, extra, terasz))
        ESETEK.append(mer(v, falsav + [dohany], terasz, fuggony=True))
        if terasz == 'keleti':
            ESETEK.append(mer(v, falsav + [dohany], terasz, otperegy=True))
            ESETEK.append(mer(v, falsav + [dohany, 'noveny_W02_DNy_sarok_O45'], terasz, otperegy=True))

out = os.path.join(HERE, '01_kozlekedes_2d_opus_S01_S02.json')
json.dump(ESETEK, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
f = lambda d: ' / '.join(f"{k.split(' ')[0]} {(w or 0):.2f}" for k, w in d.items())
for r in ESETEK:
    print(f"{r['stilus']} {r['terasz']:7s} {r['ules']:8s} {'F' if r['fuggony_szemoldokben'] else ' '} {'OK ' if r['kotelezo_ok'] else 'NEM'} "
          f"betolt: {f(r['utak_betolt_szekkel'])} | kih.min {r['szekkihuzas_min']:.2f} | kanapé–TV {r['kanape_TV_butor']:.2f} | W02–kanapé {r['W02_kanape_tav']:.2f} | {'+'.join(r['extra']) or 'alap'}")
