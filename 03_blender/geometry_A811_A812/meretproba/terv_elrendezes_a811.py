# =====================================================================================
# A-811 – a terv (M1) saját bútorrajza és Péter javaslata (L-kanapé + szekrénysor a fal mentén) ugyanazzal az
# ellenőrzővel, mint a kanapé-méretpróba (kanape_meretproba_a8.py, v2 szabályok). 2026-10-24, Claude.
# MÉRETPRÓBA – nem stílusterv. Terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért.
#
# Bemenet:
#   - a terv bútorrétege (WGR1_meretezett_alaprajzok.pdf, 5. o., 'VK_ÉP_Berendezés Mobília' és '… Konyhabútor',
#     M1 = Andrea átterve): L-kanapé [0,78; 8,20; 3,37; 10,70] (2,59 × 2,50), TV-pult [0,72; 6,65; 3,02; 6,95]
#     (2,30 × 0,30), 4 fős asztal 160 × 80 [4,47; 8,56; 6,07; 9,36], a betolt székekkel [4,47; 8,28; 6,07; 9,62];
#     a konyha felső sora (magas szekrények) x 4,90-től a nappali felé is benyúlik [4,90; 10,95; 6,17; 11,55];
#   - Péter, 2026-10-24 17:40: „simán elfér az L alakú kanapé, sőt mögé még egy szekrény is végig a fal mentén”.
# A javaslat-változatok (P…) tesztméretei BECSLÉS: szekrénysor 40 cm mély a felső fal mentén x 0–4,90 (ott
# csatlakozik a konyha magas szekrényeihez); 6 fős asztal 180 × 90, 3 + 3 szék, 90 cm széktolás; 4 fős 160 × 80,
# 2 + 2 szék, 90 cm; TV-konzol 180 × 45 a gyári TV-blokk elé (G07 antenna, D15, D16 mögötte).
# Kimenet: terv_elrendezes_A811.json, terv_elrendezes_A811.png (ebben a mappában).
# Futtatás: python3 terv_elrendezes_a811.py
# =====================================================================================
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kanape_meretproba_a8 as K
import shapely
from shapely.geometry import box
from shapely.ops import unary_union
from PIL import ImageDraw

HERE = K.HERE
KONYHA_FELSO = box(4.90, 10.95, 6.17, 11.55)   # a terv konyhabútor-rétege: a felső sor a nappali felé benyúló része
FAL_Y = 11.55                                  # felső (külső) fal belső síkja
TV_FAL_Y = 6.651
ETK_LAMPA = (5.27, 8.95)   # A811-ML04, mennyezeti lámpakiállás (g kör) – a nappali mennyezete hűtő-fűtő mező (A811-HF03): máshova nem fúrunk
HF03 = (0.131, 7.924, 6.6, 11.55)
KONZOL = (1.05, TV_FAL_Y, 2.85, TV_FAL_Y + 0.45)   # 180 × 45, közép x = 1,95 (G07 1,675; D15 1,87; D16 2,07 mögötte)

EL = [
    dict(kod='T0', nev='Terv (M1) – ahogy rajzolva', S=(0.78, 8.20, 3.37, 10.70), T=(0.72, TV_FAL_Y, 3.02, TV_FAL_Y + 0.30),
         asztal=(4.47, 8.56, 6.07, 9.36), zona=(4.47, 8.28, 6.07, 9.62), szekreny=None,
         megj='4 fős asztal 160 × 80, a székek betolva (a terv rajza); TV-pult 230 × 30 (terv)'),
    dict(kod='T0SZ', nev='Terv + szekrénysor 40 cm', S=(0.78, 8.05, 3.37, 10.55), T=(0.72, TV_FAL_Y, 3.02, TV_FAL_Y + 0.30),
         asztal=(4.47, 8.56, 6.07, 9.36), zona=(4.47, 8.28, 6.07, 9.62), szekreny=(0.0, FAL_Y - 0.40, 4.90, FAL_Y),
         megj='a terv elrendezése, a kanapé 15 cm-rel a TV felé; szekrénysor 40 cm a felső fal mentén, x 0–4,90'),
    dict(kod='T0SZ9', nev='Terv + szekrénysor, kanapé 0,94 m-re a faltól', S=(0.94, 8.05, 3.53, 10.55), T=(0.72, TV_FAL_Y, 3.02, TV_FAL_Y + 0.30),
         asztal=(4.47, 8.56, 6.07, 9.36), zona=(4.47, 8.28, 6.07, 9.62), szekreny=(0.0, FAL_Y - 0.40, 4.90, FAL_Y),
         megj='mint T0SZ, de a kanapé 16 cm-rel jobbra, hogy a nagy erkélyajtóhoz is 0,90 m-es út vezessen'),
    dict(kod='T60', nev='Terv – 60 cm széktolással', S=(0.78, 8.20, 3.37, 10.70), T=(0.72, TV_FAL_Y, 3.02, TV_FAL_Y + 0.30),
         asztal=(4.47, 8.56, 6.07, 9.36), zona=(4.47, 7.96, 6.07, 9.96), szekreny=None, megj='a terv asztala, 2 + 2 szék 60 cm-es hátratolással'),
    dict(kod='T90', nev='Terv – 90 cm széktolással (GOAL 5.)', S=(0.78, 8.20, 3.37, 10.70), T=(0.72, TV_FAL_Y, 3.02, TV_FAL_Y + 0.30),
         asztal=(4.47, 8.56, 6.07, 9.36), zona=(4.47, 7.66, 6.07, 10.26), szekreny=None, megj='a terv asztala, 2 + 2 szék 90 cm-es hátratolással'),
    dict(kod='P6', nev='L (terv) + szekrénysor 40 cm + 6 fős', S=(0.78, 8.05, 3.37, 10.55), T=KONZOL,
         asztal=(3.42, 9.05, 5.22, 9.95), zona=(3.42, 8.15, 5.22, 10.85), szekreny=(0.0, FAL_Y - 0.40, 4.90, FAL_Y),
         megj='a terv L-je 15 cm-rel a TV felé; 180 × 90 asztal, 3 + 3 szék, 90 cm; szekrénysor 40 cm, x 0–4,90'),
    dict(kod='P4', nev='L (terv) + szekrénysor 40 cm + 4 fős', S=(0.90, 8.05, 3.49, 10.55), T=KONZOL,
         asztal=(3.54, 9.05, 5.14, 9.85), zona=(3.54, 8.15, 5.14, 10.75), szekreny=(0.0, FAL_Y - 0.40, 4.90, FAL_Y),
         megj='a terv L-je 12 cm-rel jobbra és 15 cm-rel a TV felé; 160 × 80 asztal, 2 + 2 szék, 90 cm; szekrénysor 40 cm'),
]
SZELESSEGEK = [round(0.50 + 0.05 * i, 2) for i in range(19)]   # 0,50 … 1,40


def cel_max(A, akad):
    """Célonként a legnagyobb útszélesség (5 cm-es lépés), amellyel a bejáratból elérhető."""
    out = {n: None for n in A['cel_geom'] if n != K.BEJARAT}
    for w in SZELESSEGEK:
        E = A['W'].buffer(-w / 2, **K.BUF)
        if akad: E = E.difference(unary_union([o.buffer(w / 2, **K.BUF) for o in akad]))
        parts = shapely.get_parts(E)
        if not len(parts): break
        be = shapely.intersects(parts, A['cel_geom'][K.BEJARAT])
        for n in out:
            if (shapely.intersects(parts, A['cel_geom'][n]) & be).any(): out[n] = w
    return out


def ellenoriz(A, e):
    S, T, Z = box(*e['S']), box(*e['T']), box(*e['zona'])
    C = box(*e['szekreny']) if e['szekreny'] else None
    targyak = dict(kanapé=S, TV=T, étkező=Z, **({'szekrénysor': C} if C else {}))
    hibak = []
    for n, g in targyak.items():
        if not A['P'].buffer(1e-6).contains(g): hibak.append(f'{n}: kilóg a nappaliból')
        if g.intersects(A['tiltott']): hibak.append(f'{n}: belelóg egy erkélyajtó nyitásába')
        if n != 'szekrénysor' and g.intersects(KONYHA_FELSO): hibak.append(f'{n}: ütközik a konyha felső sorával')
    nevek = list(targyak)
    for i in range(len(nevek)):
        for j in range(i + 1, len(nevek)):
            if targyak[nevek[i]].intersection(targyak[nevek[j]]).area > 1e-6: hibak.append(f'{nevek[i]} ∩ {nevek[j]}')
    sofa_tv = round(S.bounds[1] - T.bounds[3], 2)
    if sofa_tv < K.TV_KANAPE_MIN - 1e-9: hibak.append(f'kanapé–TV {sofa_tv} m < {K.TV_KANAPE_MIN}')
    nezo = round(S.bounds[3] - K.SZEM - (TV_FAL_Y + K.KEPERNYO), 2)
    eltolas = round(abs((S.bounds[0] + S.bounds[2]) / 2 - (T.bounds[0] + T.bounds[2]) / 2), 2)
    tv_aljzat = [a['azonosito'] for a in A['tv'][0]['aljzatok'] if T.bounds[0] - 1e-9 <= a['x_m'] <= T.bounds[2] + 1e-9]
    hat_mogott = round((C.bounds[1] if C else FAL_Y) - S.bounds[3], 2)
    ax0, ay0, ax1, ay1 = e['asztal']; lx, ly = ETK_LAMPA
    lampa_tav = round(((lx - (ax0 + ax1) / 2) ** 2 + (ly - (ay0 + ay1) / 2) ** 2) ** 0.5, 2)
    lampa_folott = bool(ax0 + 0.20 <= lx <= ax1 - 0.20 and ay0 + 0.10 <= ly <= ay1 - 0.10)
    akad = [S, T, Z, KONYHA_FELSO] + ([C] if C else [])
    res = dict(kod=e['kod'], nev=e['nev'], megjegyzes=e['megj'], kanape=e['S'], tv=e['T'], asztal=e['asztal'], etkezo_zona=e['zona'],
               szekrenysor=e['szekreny'], geometria_hibak=hibak, kanape_tv_sav_m=sofa_tv, nezotav_m=nezo, tv_eltolas_m=eltolas,
               tv_moge_eso_aljzatok=tv_aljzat, kanape_mogott_m=hat_mogott,
               etkezo_lampa_ML04_asztalkozeptol_m=lampa_tav, etkezo_lampa_az_asztal_folott=lampa_folott, szekreny_moge_eso=[], forgatokonyv={})
    if C:
        for k in A['nappali_aljzatok'] + [k for k in json.load(open(os.path.join(K.REPO, '01_alaprajzok', 'villamos_kiallasok', 'A811_villamos.json'), encoding='utf-8'))['kiallasok']
                                           if k['tipus'] in ('kapcsolo', 'fali_lampakiallas')]:
            if C.bounds[0] - 0.05 <= k['x_m'] <= C.bounds[2] + 0.05 and k['y_m'] >= C.bounds[1] - 0.30:
                res['szekreny_moge_eso'].append(f"{k['azonosito']} ({k['tipus']}, x = {k['x_m']:.2f}" + (f", m = {k['magassag_m']}" if k.get('magassag_m') not in ('', None) else '') + ')')
    for fk, mellek in (('A', None), ('B', 0.60)):
        K.MELLEK_UT = mellek
        A['ures_tav'] = K.utak_hossza(A, [])
        cm = cel_max(A, akad)
        kok, utak, arany = K.kerulo_ok(A, akad)
        kell = {n: (min(K.UT, mellek) if (mellek and 'erkélyajtó' in n) else K.UT) for n in cm}
        ok_ut = all(cm[n] is not None and cm[n] >= kell[n] - 1e-9 for n in cm)
        rov = lambda n: n.split(' (')[0].replace('egyszárnyú erkélyajtó', 'erkély 1').replace('kétszárnyú erkélyajtó', 'erkély 2')
        okok = [f"{rov(n)}: {cm[n] if cm[n] else 0:.2f} m < {kell[n]:.2f}".replace('.', ',') for n in cm if not (cm[n] and cm[n] >= kell[n] - 1e-9)]
        if ok_ut and not kok:
            okok += [f"{rov(n)} csak kerülővel: {v:.2f} m (üresen {A['ures_tav'][n]:.2f})".replace('.', ',') for n, v in utak.items()
                     if v is not None and A['ures_tav'][n] is not None and v > K.KERULO_SZORZO * A['ures_tav'][n] + K.KERULO_PLUSZ]
            okok += [f"{rov(n)}: az út éppen a határon (5 cm-es raszteren nem járható)" for n, v in utak.items() if v is None]
        okok += hibak
        res['forgatokonyv'][fk] = dict(cel_max_szelesseg_m=cm, kell_m=kell, uthossz_m=utak, ures_uthossz_m=A['ures_tav'], kerulo_ok=kok,
                                       kerulo_max_arany=arany, megfelel=bool(ok_ut and kok and not hibak), okok=okok)
    K.MELLEK_UT = None
    return res, akad


def rajz(A, e, r, akad, px=80):
    im = K.panel(A, '', None, dict(alak='L'), None, px=px); dr = ImageDraw.Draw(im, 'RGBA')
    x0, y0, x1, y1 = A['C']['nezet']; T = lambda x, y: (round((x - x0) * px), round(62 + (y1 - y) * px))
    def rect(b, fill=None, outline=None, width=1): dr.rectangle([T(b[0], b[3]), T(b[2], b[1])], fill=fill, outline=outline, width=width)
    ok, parts, be = K.szabad_ter(A, akad, K.UT)
    for p, b in zip(parts, be if be is not None else []):
        if b and p.geom_type == 'Polygon': dr.polygon([T(*c) for c in p.exterior.coords], fill=K.SZIN['ut'] + (90,))
    rect(KONYHA_FELSO.bounds, fill=(205, 185, 140, 255), outline=(150, 120, 60, 255))
    if e['szekreny']: rect(e['szekreny'], fill=(120, 90, 160, 170), outline=(80, 50, 120, 255), width=2)
    sx0, sy0, sx1, sy1 = e['S']; m = 0.95
    rect(e['S'], fill=K.SZIN['kanape'] + (55,), outline=K.SZIN['kanape'] + (255,), width=2)
    for b in ((sx0, sy1 - m, sx1, sy1), (sx0, sy0, sx0 + m, sy1 - m)):          # háttámla felül, récamier a bal oldalon (mint a terv rajzán)
        rect(b, fill=K.SZIN['kanape'] + (110,), outline=K.SZIN['kanape'] + (255,))
    rect(e['T'], fill=K.SZIN['tv'] + (180,))
    rect(e['zona'], fill=K.SZIN['etk'] + (45,), outline=K.SZIN['etk'] + (255,), width=2); rect(e['asztal'], fill=K.SZIN['etk'] + (200,))
    rect(HF03, outline=(40, 90, 220, 150), width=1)
    for nev, (lx, ly) in (('ML03', (2.21, 8.95)), ('ML04', ETK_LAMPA)):
        p = T(lx, ly); dr.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill=(255, 210, 0, 255), outline=(0, 0, 0, 255))
        dr.text((p[0] + 9, p[1] - 7), nev, fill=(0, 0, 0), font=K.FS)
    fa, fb = r['forgatokonyv']['A'], r['forgatokonyv']['B']
    cm = fb['cel_max_szelesseg_m']
    dr.rectangle([0, 0, im.size[0], 60], fill=(255, 255, 255, 255))
    dr.text((8, 4), f"{e['kod']} · {e['nev']}", fill=(0, 0, 0), font=K.FB)
    allapot = lambda f: 'MEGFELEL' if f['megfelel'] else 'NEM – ' + '; '.join(f['okok'])
    szin = (20, 120, 40) if fb['megfelel'] else (200, 30, 30)
    dr.text((8, 22), f"B (erkélyhez 0,60): {allapot(fb)}", fill=szin, font=K.F)
    dr.text((8, 41), (f"A (0,90 mindenhova): {allapot(fa)} · nézőtáv {r['nezotav_m']:.2f} · kanapé–TV {r['kanape_tv_sav_m']:.2f} · mögötte {r['kanape_mogott_m']:.2f}"
                      f" · ML04–asztalközép {r['etkezo_lampa_ML04_asztalkozeptol_m']:.2f} m").replace('.', ','), fill=(60, 60, 60), font=K.FS)
    # méretfeliratok
    dr.text(T(sx0 + 0.05, sy1 - 0.05), f'{sx1 - sx0:.2f} × {sy1 - sy0:.2f}'.replace('.', ','), fill=(20, 40, 120), font=K.FS)
    if e['szekreny']:
        dr.text(T(0.05, FAL_Y + 0.12), f"szekrénysor {e['szekreny'][2] - e['szekreny'][0]:.2f} × 0,40 · mögötte a kanapé: {r['kanape_mogott_m']:.2f} m".replace('.', ','), fill=(80, 50, 120), font=K.FS)
    else:
        dr.text(T(0.05, FAL_Y + 0.12), f"a kanapé háta és a fal között: {r['kanape_mogott_m']:.2f} m".replace('.', ','), fill=(80, 50, 120), font=K.FS)
    dr.text(T(e['zona'][0] + 0.03, e['zona'][1] + 0.22), f"{e['asztal'][2] - e['asztal'][0]:.2f} × {e['asztal'][3] - e['asztal'][1]:.2f}".replace('.', ','), fill=(140, 70, 0), font=K.FS)
    return im


if __name__ == '__main__':
    A = K.lakas_adat('A811')
    eredmeny, panelek = [], []
    for e in EL:
        r, akad = ellenoriz(A, e)
        eredmeny.append(r); panelek.append(rajz(A, e, r, akad))
        fa, fb = r['forgatokonyv']['A'], r['forgatokonyv']['B']
        print(e['kod'], 'A:', fa['megfelel'], fa['cel_max_szelesseg_m'], 'kerülő', fa['kerulo_ok'], fa['kerulo_max_arany'],
              '| lámpa', r['etkezo_lampa_ML04_asztalkozeptol_m'], r['etkezo_lampa_az_asztal_folott'], '| B:', fb['megfelel'], 'kerülő', fb['kerulo_ok'], fb['kerulo_max_arany'], '| hibák', r['geometria_hibak'],
              '| nézőtáv', r['nezotav_m'], 'kanapé–TV', r['kanape_tv_sav_m'], 'mögött', r['kanape_mogott_m'], '| szekrény mögött', r['szekreny_moge_eso'])
    lab = ['MÉRETPRÓBA – nem stílusterv. Terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért. T… = a terv (M1) bútorrajza; P… = Péter javaslata (L + szekrénysor), tesztméretekkel (BECSLÉS).',
           'Kék: kanapé (sötétebb: háttámla és récamier, 95 cm – jelzés); barna: TV-pult/-konzol; narancs: étkezőzóna széktolással, benne az asztal; lila: szekrénysor 40 cm;',
           'bézs: konyhapult (a felső sor x 4,90-től a terv konyhabútor-rétege szerint); piros: erkélyajtó-nyitás; halványzöld: a bejáratból 0,90 m-es úttal elérhető szabad tér.',
           'Sárga pont: mennyezeti lámpakiállás (ML03 nappali, ML04 étkező); kék keret: mennyezeti hűtő-fűtő mező (A811-HF03) – ide nem fúrunk, a lámpa csak a meglévő kiállásra kerülhet.',
           'A = minden célhoz 0,90 m; B = az erkélyajtókhoz 0,60 m-es mellékút (GOAL 5.: „mellék 60–90”). Kerülő: az út ≤ 1,5 × az üres lakásbeli + 1,0 m. A szekrénysor a K03 kapcsolót (x = 4,60) érinti.']
    K.lap(panelek, 'A-811 – a terv (M1) bútorrajza és az L + szekrénysor javaslat ugyanazzal az ellenőrzővel (2026-10-24)', lab).save(os.path.join(HERE, 'terv_elrendezes_A811.png'), optimize=True)
    json.dump(dict(datum='2026-10-24', statusz='MÉRETPRÓBA – nem stílusterv; terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért',
                   forras='WGR1_meretezett_alaprajzok.pdf 5. o. bútorrétegei (M1); Péter 2026-10-24 17:40 (L + szekrénysor a fal mentén)',
                   konyha_felso_sor=list(KONYHA_FELSO.bounds), eredmeny=eredmeny),
              open(os.path.join(HERE, 'terv_elrendezes_A811.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('kész')
