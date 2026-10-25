# =====================================================================================
# Integrátori méretpróba – Opus 5.5 V3.1 VÉGLEGES forrás (PR #22 @ 7d3c67f), S04–S10 nappali–étkező, 2D közlekedés.
# Claude integrátor, 2026-10-25. Motor: ../geometry_v2/elrendezes_alt/elrendezes_alt_a902.py (csak olvasva; fontútvonal macOS-re cserélve).
# Prioritás (Péter): S04 Lilo, S05 Melva, S07 Wolke 256 × 118, S08 torony–kanapé, S09 karfás végszék, S10 mesa-bútortestek; + S06 (U + Ø90 asztal).
# A termékméret a 40-es elemlistából; ahol a gyártó belső mérete (ülésmélység, sarokelem szélessége) nincs megadva, „FELT” jelöli.
# Teraszajtó: középső szárny / csak keleti 0,93 m-es szárny (5+1-gyel is). MÉRETPRÓBA – terv szerinti geometria, helyszínen nem mért.
# =====================================================================================
import os, json, types
from shapely.geometry import box, Point
from shapely.ops import unary_union

HERE = os.path.dirname(os.path.abspath(__file__))
ENG = os.path.join(HERE, '..', 'geometry_v2', 'elrendezes_alt', 'elrendezes_alt_a902.py')
src = open(ENG, encoding='utf-8').read()
src = src.replace('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', '/System/Library/Fonts/Supplemental/Arial.ttf')
src = src.replace('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', '/System/Library/Fonts/Supplemental/Arial Bold.ttf')
E = types.ModuleType('eng'); E.__file__ = os.path.abspath(ENG); exec(compile(src, ENG, 'exec'), E.__dict__)

TERASZ = {'kozepso': E.CELOK['terasz (tolóajtó, keleti rész)'], 'keleti': box(7.98, 7.55, 8.91, 8.05)}
ASZTAL = (8.00, 5.40, 8.90, 7.00)
SZEK_POZ = [(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]
VEG_DEL, VEG_ESZAK = (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)
PANEL = box(3.67, 4.05, 3.71, 8.05)

def L_kanape(XB, YS, YN, D, CH, CW):
    """L: háttámla kelet (XB), hosszú ülés É–D, a sarokrész (chaise) a déli végén nyugat felé CH mélyen, CW szélesen."""
    return unary_union([box(XB - D, YS + CW, XB, YN), box(XB - CH, YS, XB, YS + CW)])

def stilus(kod):
    """(kanapé, TV-sáv, székméret, extra akadály dict, megjegyzés) – a 7d3c67f specifikáció szerint."""
    if kod.startswith('S04'):
        YN = 7.59 if kod == 'S04' else 7.70
        return dict(kanape=L_kanape(6.67, YN - 2.60, YN, 1.00, 1.76, 1.00), kanape_nev=f'Westwing Lilo L 260 × 176 (FELT: ülésmélység 100, sarokelem 100; északi vég y {YN})',
                    tv=unary_union([PANEL, box(3.71, 4.10, 4.11, 7.90)]), szek=(0.55, 0.52, 'Westwing Calan'),
                    extra={'dohanyzo_Lesley_FELT_O80': Point(6.67 - 1.00 - 0.47 - 0.40, 6.95).buffer(0.40), 'olivafa_W02_sarok_O45': Point(5.45, 4.285).buffer(0.225)})
    if kod == 'S05':
        return dict(kanape=L_kanape(6.67, 5.21, 7.59, 0.90, 1.43, 0.90), kanape_nev='Westwing Melva L 238 × 143 (FELT: ülésmélység 90, sarok délen)',
                    tv=unary_union([PANEL, box(3.67, 4.75, 4.12, 7.75)]), szek=(0.55, 0.55, 'Westwing Samantha'),
                    extra={'dohanyzo_Antigua_O78': Point(6.67 - 0.90 - 0.47 - 0.39, 6.85).buffer(0.39)})
    if kod == 'S06':
        return dict(kanape=E.jattebo_U(6.60), kanape_nev='IKEA JÄTTEBO U 285 × 160',
                    tv=unary_union([PANEL, box(3.67, 4.05, 4.12, 8.05)]), szek=(0.55, 0.53, 'Kave Home Eamy'),
                    extra={'dohanyzo_Sculpt_O90_a_U_szajaban': Point(6.60 - 0.95 - 0.47 - 0.45, 6.40).buffer(0.45)})
    if kod == 'S07':
        return dict(kanape=L_kanape(6.67, 7.59 - 2.56, 7.59, 0.95, 1.18, 0.95), kanape_nev='Westwing Wolke Teddy 256 × 118 (FELT: ülésmélység 95, rövid szár délen)',
                    tv=unary_union([PANEL, box(3.71, 4.85, 4.16, 7.65)]), szek=(0.56, 0.51, 'Westwing Adrien'),
                    extra={'dohanyzo_Sheffield_O80': Point(6.67 - 0.95 - 0.47 - 0.40, 6.85).buffer(0.40)})
    if kod.startswith('S08'):
        y0 = {'S08': 4.45, 'S08_torony_deli_vegre': 4.15}[kod]
        return dict(kanape=E.lennon_L(6.67), kanape_nev='Westwing Lennon L 238 × 180',
                    tv=unary_union([PANEL, box(3.71, y0, 4.31, y0 + 0.60), box(3.71, 5.05, 4.11, 7.45)]), szek=(0.56, 0.51, 'Westwing Adrien'),
                    extra={'dohanyzo_Naruto_140x80': box(6.67 - 0.95 - 0.47 - 0.80, 6.30, 6.67 - 0.95 - 0.47, 7.70)},
                    torony=box(3.71, y0, 4.31, y0 + 0.60))
    if kod == 'S09':
        return dict(kanape=E.lennon_L(6.67), kanape_nev='Westwing Lennon L 238 × 180',
                    tv=unary_union([PANEL, box(3.67, 4.05, 4.02, 4.85), box(3.67, 7.25, 4.02, 8.05), box(3.67, 4.85, 4.07, 7.25)]), szek=(0.55, 0.52, 'Westwing Calan oldalszék'),
                    veg=(0.66, 0.60, 'Westwing Calan karfás végszék (FELT: mélység 60)'),
                    extra={'Orlia_kisasztalok_FELT_O55': Point(6.67 - 0.95 - 0.47 - 0.28, 6.90).buffer(0.28)})
    if kod == 'S10':
        return dict(kanape=E.jattebo_U(6.60), kanape_nev='IKEA JÄTTEBO U 285 × 160',
                    tv=unary_union([PANEL, box(3.67, 4.05, 4.12, 8.05)]), szek=(0.46, 0.56, 'Westwing Sissi'),
                    extra={'dohanyzo_Adularia_85x85_a_U_ban': box(6.60 - 0.95 - 0.45 - 0.85, 5.975, 6.60 - 0.95 - 0.45, 6.825)})

def mer(kod, terasz, otperegy=False, extra_be=True):
    s = stilus(kod); st = kod[:3]
    E.SZEK[st] = dict(nev=s['szek'][2], sz=s['szek'][0], mely=s['szek'][1])
    szekek = [p for p in SZEK_POZ if not (otperegy and p == VEG_ESZAK)]
    v = dict(stilus=st, XB=6.67 if 'Lennon' in s['kanape_nev'] or 'L ' in s['kanape_nev'] else 6.60, kanape=s['kanape'], asztal=box(*ASZTAL), szekek=szekek, kerek=False)
    E.TV_ZONA = s['tv']
    cel0 = dict(E.CELOK); E.CELOK = {k: g for k, g in cel0.items() if not k.startswith('terasz')}; E.CELOK['terasz'] = TERASZ[terasz]
    try:
        if 'veg' in s:   # S09: az oldalszékek és a két karfás végszék külön mérettel
            v_old = dict(v, szekek=[p for p in szekek if p not in (VEG_DEL, VEG_ESZAK)])
            v_veg = dict(v, szekek=[p for p in szekek if p in (VEG_DEL, VEG_ESZAK)], stilus='S09V')
            E.SZEK['S09V'] = dict(nev=s['veg'][2], sz=s['veg'][0], mely=s['veg'][1])
            m, b1, u1 = E.meres(v_old); b2 = E.szek_poligonok(v_veg, 'betolt'); u2 = E.szek_poligonok(v_veg, 'ulo')
            betolt, ulo = b1 + b2, u1 + u2; kih = E.kihuzas(v_old) + E.kihuzas(v_veg)
        else:
            m, betolt, ulo = E.meres(v); kih = E.kihuzas(v)
        ext = list(s['extra'].values()) if extra_be else []
        ut = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + betolt + ext)
        ut_ulo = E.ut_szelesseg([v['kanape'], v['asztal'], E.TV_ZONA] + ulo + ext)
    finally:
        E.CELOK = cel0
    r = dict(kod=kod, kanape=s['kanape_nev'], terasz=terasz, ules='5+1' if otperegy else '2+2+1+1', extra=list(s['extra']) if extra_be else [],
             utak_betolt=ut, utak_ulo=ut_ulo, szekkihuzas=kih, szekkihuzas_min=round(min(kih), 3),
             kanape_TV_butor=round(v['kanape'].distance(E.TV_ZONA), 3), W02_kanape=round(v['kanape'].distance(box(5.18, 4.00, 7.32, 4.05)), 3),
             kanape_uveg=round(8.05 - v['kanape'].bounds[3], 3), extra_TV_butor={k: round(g.distance(E.TV_ZONA), 3) for k, g in s['extra'].items()},
             extra_kanape={k: round(g.distance(v['kanape']), 3) for k, g in s['extra'].items()})
    if 'torony' in s: r['kanape_torony'] = round(v['kanape'].distance(s['torony']), 3)
    r['kotelezo_ok'] = all((w or 0) >= 0.90 - 1e-6 for w in ut.values()) and r['szekkihuzas_min'] >= 0.90 - 1e-6 and r['kanape_TV_butor'] >= 0.60 - 1e-6
    return r

ES = []
for kod in ('S04', 'S04_eszakra_7.70', 'S05', 'S06', 'S07', 'S08', 'S08_torony_deli_vegre', 'S09', 'S10'):
    for terasz in ('kozepso', 'keleti'):
        ES.append(mer(kod, terasz))
        if kod == 'S04': ES.append(mer(kod, terasz, extra_be=False))
        if terasz == 'keleti': ES.append(mer(kod, terasz, otperegy=True))
json.dump(ES, open(os.path.join(HERE, '03_kozlekedes_2d_opus_S04_S10.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
f = lambda d: ' / '.join(f"{k.split(' ')[0]} {(w or 0):.2f}" for k, w in d.items())
for r in ES:
    extra = ' torony %.2f' % r['kanape_torony'] if 'kanape_torony' in r else ''
    print(f"{r['kod']:22s} {r['terasz']:7s} {r['ules']:8s} {'OK ' if r['kotelezo_ok'] else 'NEM'} {f(r['utak_betolt'])} | kih {r['szekkihuzas_min']:.2f} | kanapé–TV {r['kanape_TV_butor']:.2f}{extra} | W02 {r['W02_kanape']:.2f} | üveg {r['kanape_uveg']:.2f} | {'extra' if r['extra'] else 'extra nélkül'} {r['extra_TV_butor']}")
