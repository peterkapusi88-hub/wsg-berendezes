# =====================================================================================
# A-812 – a terv (M1) bútorrajza és Péter elrendezése (2026-10-24 18:14) ugyanazzal az ellenőrzővel, mint a
# kanapé-méretpróba (kanape_meretproba_a8.py, v2 szabályok). 2026-10-24, Claude.
# MÉRETPRÓBA – nem stílusterv. Terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért.
#
# Péter (18:14): „Ott legyen az étkező, ahol a terven; lehet L alakú simán, és fent szekrénysor a 3,89-es falon.
# Az U rész lehet a fix ablak előtt kisebb részben, nagyobb részben pedig a másik oldalon.” (18:16, A-811-re:
# 60 cm mély szekrény, a kanapé annyival lejjebb, hogy a szekrényt éppen meg lehessen közelíteni – itt is így.)
# Bemenet:
#   - a terv bútorrétege (WGR1_meretezett_alaprajzok.pdf, 12. o., 1:100, M1 KORR): egyenes kanapé [0,67; 3,77; 2,67; 4,67],
#     3 fotel, dohányzóasztal, TV-pult [0; 0; 3,22; 0,30], asztal 80 × 160 (x 4,20–5,00, y 0,725–2,325) 3 + 3 + 1 + 1 székkel,
#     betolt székekkel [3,93; 0,26; 5,27; 2,60] – a közepe az ML05 étkezőlámpa (4,60; 1,425) alatt;
#   - a „3,89-es fal” a fülke hátfala (a méret a külső síktól mér; a belső hossz 3,22 m, x 0–3,22, y = 5,60);
#   - a fix üvegmező az erkélyajtó fölött: y 2,705–4,70 (a kétszárnyú ajtó y 0,98–2,705, zsanér a falsíkban).
# Tesztméretek (BECSLÉS): szekrénysor 60 cm mély a fülke hátfalán; kanapé-ülésmélység 1,00 m; a kanapé háta 0,50 m-re
# a szekrény elejétől; TV a gyári blokkon (a terv pultja). Nézőtáv: itt 2,0–4,1 m (a terv saját kanapéja is kb. 4,1 m-re
# van a TV-től) – a fő próba 3,4 m-es felső határa itt nem teljesíthető, ha a kanapé a fülke előtt áll.
# A konyhaút a terv szerinti asztalhelynél a székek és a konyha között 0,53 m (betolt székekkel) – Péter döntése,
# ezért a konyha itt nem kizáró feltétel, csak jelentjük.
# Kimenet: terv_elrendezes_A812.json, terv_elrendezes_A812.png. Futtatás: python3 terv_elrendezes_a812.py
# =====================================================================================
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kanape_meretproba_a8 as K
import terv_elrendezes_a811 as T8
import shapely
from shapely.geometry import box
from shapely.ops import unary_union
from PIL import ImageDraw

LAMPA = (4.60, 1.425)                       # A812-ML05, étkező
TV_PULT = (0.0, 0.0, 3.22, 0.30)            # a terv TV-pultja (G08, D17, D18 mögötte)
ASZTAL = (4.20, 0.725, 5.00, 2.325); ZONA = (3.93, 0.26, 5.27, 2.60)
SZEKRENY60 = (0.0, 5.00, 3.22, 5.60)
NEZO_MAX = 4.10
KONYHA = 'konyha (pult előtti sáv)'

def u(*bs): return unary_union([box(*b) for b in bs])

EL = [
    dict(kod='T812', nev='Terv (M1) – ahogy rajzolva', kanape=u((0.67, 3.77, 2.67, 4.67)), hat_y=4.67,
         egyeb=[box(0.72, 1.57, 1.52, 2.37), box(1.82, 1.57, 2.62, 2.37), box(2.97, 2.67, 3.77, 3.47), box(1.07, 2.77, 2.27, 3.37)],
         szekreny=None, megj='egyenes kanapé 200 × 90, 3 fotel, dohányzóasztal; asztal 80 × 160, 8 szék'),
    dict(kod='P812L', nev='L + szekrénysor 60 cm (Péter)', kanape=u((0.15, 3.50, 3.15, 4.50), (2.15, 2.25, 3.15, 3.50)), hat_y=4.50,
         egyeb=[], szekreny=SZEKRENY60, megj='L 3,00 × 2,25 – hosszú szár a dohányzóasztal jobb oldalán; a háta 0,50 m-re a szekrénytől'),
    dict(kod='P812U', nev='U + szekrénysor 60 cm (Péter)', kanape=u((0.15, 3.50, 3.15, 4.50), (0.15, 2.80, 1.10, 3.50), (2.15, 2.25, 3.15, 3.50)), hat_y=4.50,
         egyeb=[], szekreny=SZEKRENY60, megj='U 3,00 széles; rövid szár (1,70) a fix üveg előtt, hosszú szár (2,25) a másik oldalon; a háta 0,50 m-re a szekrénytől'),
]


def ellenoriz(A, e):
    S = e['kanape']; Tp = box(*TV_PULT); Z = box(*ZONA); C = box(*e['szekreny']) if e['szekreny'] else None
    targyak = dict(kanapé=S, TV=Tp, étkező=Z, **({'szekrénysor': C} if C else {}), **{f'bútor{i + 1}': g for i, g in enumerate(e['egyeb'])})
    hibak = []
    for n, g in targyak.items():
        if not A['P'].buffer(1e-6).contains(g): hibak.append(f'{n}: kilóg a nappaliból')
        if g.intersection(A['tiltott']).area > 1e-4: hibak.append(f'{n}: belelóg az erkélyajtó nyitásába')
    nv = list(targyak)
    for i in range(len(nv)):
        for j in range(i + 1, len(nv)):
            if targyak[nv[i]].intersection(targyak[nv[j]]).area > 1e-6: hibak.append(f'{nv[i]} ∩ {nv[j]}')
    sb = S.bounds
    nezo = round(e['hat_y'] - K.SZEM - K.KEPERNYO, 2)
    if not (K.NEZO[0] <= nezo <= NEZO_MAX): hibak.append(f'nézőtáv {nezo} m')
    eltolas = round(abs((sb[0] + sb[2]) / 2 - (TV_PULT[0] + TV_PULT[2]) / 2), 2)
    akad = list(targyak.values())
    res = dict(kod=e['kod'], nev=e['nev'], megjegyzes=e['megj'], kanape_befoglalo=[round(v, 3) for v in sb], nezotav_m=nezo, tv_eltolas_m=eltolas,
               kanape_tv_sav_m=round(sb[1] - TV_PULT[3], 2), kanape_mogott_m=(round(C.bounds[1] - e['hat_y'], 2) if C else None),
               szekreny=e['szekreny'], geometria_hibak=hibak, szekreny_moge_eso=[], forgatokonyv={})
    if C:
        V = json.load(open(os.path.join(K.REPO, '01_alaprajzok', 'villamos_kiallasok', 'A812_villamos.json'), encoding='utf-8'))
        res['szekreny_moge_eso'] = [f"{k['azonosito']} ({k['tipus']}, x = {k['x_m']:.2f})" for k in V['kiallasok']
                                     if C.bounds[0] - 0.05 <= k['x_m'] <= C.bounds[2] + 0.05 and k['y_m'] >= C.bounds[1] - 0.05 and 'NAPPALI' in k['helyiseg']]
    for fk, mellek in (('A', None), ('B', 0.60)):
        K.MELLEK_UT = mellek; A['ures_tav'] = K.utak_hossza(A, [])
        cm = T8.cel_max(A, akad)
        kell = {n: (min(K.UT, mellek) if (mellek and 'erkélyajtó' in n) else K.UT) for n in cm}
        utak = K.utak_hossza(A, akad)
        okok = [f"{n.split(' (')[0]}: {cm[n] if cm[n] else 0:.2f} m < {kell[n]:.2f}".replace('.', ',') for n in cm if n != KONYHA and not (cm[n] and cm[n] >= kell[n] - 1e-9)]
        for n, v in utak.items():
            if n == KONYHA: continue
            uu = A['ures_tav'][n]
            if v is not None and uu is not None and v > K.KERULO_SZORZO * uu + K.KERULO_PLUSZ: okok.append(f"{n.split(' (')[0]} csak kerülővel: {v:.2f} m".replace('.', ','))
        okok += hibak
        res['forgatokonyv'][fk] = dict(cel_max_szelesseg_m=cm, uthossz_m=utak, ures_uthossz_m=A['ures_tav'], okok=okok, megfelel=not okok)
    K.MELLEK_UT = None
    return res, akad


def rajz(A, e, r, akad, px=80):
    im = K.panel(A, '', None, dict(alak='L'), None, px=px); dr = ImageDraw.Draw(im, 'RGBA')
    x0, y0, x1, y1 = A['C']['nezet']; T = lambda x, y: (round((x - x0) * px), round(62 + (y1 - y) * px))
    def poly(g, fill=None, outline=None, width=1):
        for p in shapely.get_parts(g):
            if p.geom_type == 'Polygon': dr.polygon([T(*c) for c in p.exterior.coords], fill=fill, outline=outline, width=width)
    ok, parts, be = K.szabad_ter(A, akad, K.UT)
    for p, b in zip(parts, be if be is not None else []):
        if b: poly(p, fill=K.SZIN['ut'] + (90,))
    if e['szekreny']: poly(box(*e['szekreny']), fill=(120, 90, 160, 170), outline=(80, 50, 120, 255), width=2)
    poly(e['kanape'], fill=K.SZIN['kanape'] + (110,), outline=K.SZIN['kanape'] + (255,), width=2)
    for g in e['egyeb']: poly(g, fill=K.SZIN['kanape'] + (60,), outline=K.SZIN['kanape'] + (200,))
    poly(box(*TV_PULT), fill=K.SZIN['tv'] + (180,))
    poly(box(*ZONA), fill=K.SZIN['etk'] + (45,), outline=K.SZIN['etk'] + (255,), width=2); poly(box(*ASZTAL), fill=K.SZIN['etk'] + (200,))
    for nev, (lx, ly) in (('ML04', (1.61, 2.80)), ('ML05', LAMPA), ('ML03', (4.601, 3.525))):
        p = T(lx, ly); dr.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill=(255, 210, 0, 255), outline=(0, 0, 0, 255)); dr.text((p[0] + 9, p[1] - 7), nev, fill=(0, 0, 0), font=K.FS)
    fa, fb = r['forgatokonyv']['A'], r['forgatokonyv']['B']
    allapot = lambda f: 'MEGFELEL' if f['megfelel'] else 'NEM – ' + '; '.join(f['okok'])
    dr.rectangle([0, 0, im.size[0], 60], fill=(255, 255, 255, 255))
    dr.text((8, 4), f"{e['kod']} · {e['nev']}", fill=(0, 0, 0), font=K.FB)
    dr.text((8, 22), f"B (erkélyhez 0,60): {allapot(fb)}", fill=(20, 120, 40) if fb['megfelel'] else (200, 30, 30), font=K.F)
    k = fb['cel_max_szelesseg_m'][KONYHA]
    dr.text((8, 41), (f"A (0,90): {allapot(fa)} · nézőtáv {r['nezotav_m']:.2f} · kanapé mögött " + (f"{r['kanape_mogott_m']:.2f}" if r['kanape_mogott_m'] is not None else '–')
                      + f" · konyha {k if k else 0:.2f} (a terv asztalhelye)").replace('.', ','), fill=(60, 60, 60), font=K.FS)
    return im


if __name__ == '__main__':
    A = K.lakas_adat('A812'); eredmeny, panelek = [], []
    for e in EL:
        r, akad = ellenoriz(A, e); eredmeny.append(r); panelek.append(rajz(A, e, r, akad))
        print(e['kod'], 'A:', r['forgatokonyv']['A']['okok'], '| B:', r['forgatokonyv']['B']['okok'], '| utak B:', r['forgatokonyv']['B']['cel_max_szelesseg_m'],
              '| nézőtáv', r['nezotav_m'], 'TV-eltolás', r['tv_eltolas_m'], 'mögött', r['kanape_mogott_m'], r['szekreny_moge_eso'])
    lab = ['MÉRETPRÓBA – nem stílusterv. Terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért. T812 = a terv (M1) bútorrajza; P812L/P812U = Péter elrendezése (2026-10-24 18:14).',
           'Kék: kanapé (halványabb: fotelek, dohányzóasztal); barna: a terv TV-pultja a gyári blokkon; narancs: étkező a terv helyén (betolt székekkel), benne az asztal; lila: szekrénysor 60 cm a fülke hátfalán;',
           'sárga: mennyezeti lámpakiállás (ML05 az étkezőé); piros: erkélyajtó-nyitás; halványzöld: a bejáratból 0,90 m-es úttal elérhető szabad tér. A konyhaút a terv asztalhelyénél 0,53 m (Péter döntése) – nem kizáró.',
           'A = minden célhoz 0,90 m; B = az erkélyajtóhoz 0,60 m-es mellékút. Nézőtáv-határ itt 4,1 m (a terv kanapéja is kb. ennyi).']
    K.lap(panelek, 'A-812 – a terv (M1) bútorrajza és Péter L / U + szekrénysor elrendezése (2026-10-24)', lab).save(os.path.join(K.HERE, 'terv_elrendezes_A812.png'), optimize=True)
    json.dump(dict(datum='2026-10-24', statusz='MÉRETPRÓBA – nem stílusterv; terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért',
                   forras='WGR1_meretezett_alaprajzok.pdf 12. o. bútorrétege (M1 KORR); Péter 2026-10-24 18:14–18:16', tv_pult=TV_PULT, asztal=ASZTAL, etkezo_zona=ZONA,
                   lampa_ML05=LAMPA, eredmeny=eredmeny),
              open(os.path.join(K.HERE, 'terv_elrendezes_A812.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('kész')
