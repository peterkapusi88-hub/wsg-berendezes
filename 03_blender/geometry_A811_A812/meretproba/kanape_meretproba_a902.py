# =====================================================================================
# A-902 – U/L kanapé méretpróba a nappali-étkezőben (2026-10-24, Claude). Péter, 18:23: „Nagyon fontos, hogy a 902-be is
# U, de minimum L alakú legyen a kanapé.” A döntései a többi lakásra: az étkező a terv helyén, a lámpája alatt marad;
# a TV helye szabad (meglévő dugalj kell); szekrénysor a fal mentén, ha befér.
# MÉRETPRÓBA – nem stílusterv. Geometria: 03_blender/geometry_lock_A902_v2b.json (main, terv szerinti), helyszínen nem mért.
# Bemenet:
#   - a terv bútorrétege (WGR1_meretezett_alaprajzok.pdf, 18. o., 1:50, M1 KORR 2): TV-sáv a nyugati falon [3,67; 5,02; 3,97; 7,52],
#     egyenes kanapé [4,55; 5,27; 5,45; 7,27], 2 fotel, dohányzóasztal; asztal 80 × 180, 3 + 3 szék, betolt székekkel
#     [7,98; 5,37; 9,32; 7,17] – a közepe az ML04 étkezőlámpa (8,549; 6,274) alatt; konyhabútor: főzőlapos pult [8,45; 2,35; 9,05; 4,05],
#     jobb oldali pultsor a nappali felé is benyúlva [9,95; 1,35; 10,55; 5,25], sütő/magas elemek [9,05; 1,35; 9,95; 1,95];
#   - 01_alaprajzok/villamos_kiallasok/A902_villamos.json: gyári TV-blokk a nyugati falon (G08 antenna y = 6,054; D16, D17 dugalj),
#     a déli falon a D19 dugalj (x = 7,149) a kapcsolóoszlop (K10–K12, T01, S01; x = 7,15) mellett; a nappali mennyezete
#     hűtő-fűtő mező (A902-HF03), lámpa csak a meglévő kiállásra.
# A konyha célja a két pultsor közti 0,90 m-es munkasáv nappali felőli torka (a sáv maga 0,90 m széles, ezt a 0,90 m-es útpróba
# nem tudja „belülről” bejárni). Feltételek: mint a fő próbában (kanape_meretproba_a8.py, v2): 0,90 m-es út a bejárattól a terasz tolóajtajáig, a konyhába,
# a hálók folyosójára és a 05.3 háló ajtajához (a terasz a fő kültér, ezért ide is 0,90); kerülő legfeljebb 1,5 × üres + 1 m;
# kanapé–TV ≥ 0,60 m; nézőtáv 2,0–3,4 m; a TV középvonala ≤ 0,40 m-rel tér el a kanapéétól; a teraszüveg tolóajtó (nincs nyitási ív).
# TV-falak: 'nyugati' – a gyári blokk (a konzol mögött az antenna és dugalj); 'deli' – a D19 dugalj a konzol jobb vége mellett,
# a konzol a kapcsolóoszlopot (x ≥ 7,00) szabadon hagyja.
# Kimenet: kanape_meretproba_A902.json, kanape_meretproba_A902.png. Futtatás: python3 kanape_meretproba_a902.py
# =====================================================================================
import os, sys, json, time, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kanape_meretproba_a8 as K
import numpy as np, shapely
from shapely.geometry import box
from shapely.ops import unary_union
from skimage.graph import MCP_Geometric
from PIL import ImageDraw

LOCK = json.load(open(os.path.join(K.B, 'geometry_lock_A902_v2b.json'), encoding='utf-8'))
V = json.load(open(os.path.join(K.REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.json'), encoding='utf-8'))
KV = {k['azonosito']: k for k in V['kiallasok']}
PULT = [(8.45, 2.35, 9.05, 4.05), (9.95, 1.35, 10.55, 5.25), (9.05, 1.35, 9.95, 1.95), (8.45, 1.35, 8.95, 2.25)]
ASZTAL = (8.25, 5.37, 9.05, 7.17)
ZONAK = {'terv (betolt székek)': (7.98, 5.37, 9.32, 7.17), 'terv, 0,30 m-rel nyugatra': (7.68, 5.37, 9.02, 7.17), '60 cm széktolás, 0,60 m-rel nyugatra': (7.05, 5.37, 9.05, 7.17)}
LAMPA_ETK = (8.549, 6.274)
CELOK = {K.BEJARAT: (7.30, 3.30, 8.35, 4.05), 'terasz (tolóajtó)': (4.44, 7.30, 8.94, 8.05), 'konyha (a pultsorok közé)': (9.05, 4.05, 9.95, 4.80),
         'hálók folyosója': (3.70, 3.25, 5.00, 3.95), '05.3 háló ajtaja': (10.00, 6.05, 10.75, 6.95)}
JARHATO = ['nappali_etkezo', 'konyha', 'eloter_atjaro', 'kozlekedo', 'eloter']
TV_FALAK = [dict(kod='nyugati', nev='gyári TV-blokk a nyugati falon (antennával)', tengely='x', sik=3.67, irany=+1, tart=(4.05, 8.05),
                 kotelezo=[KV['A902-G08']['y_m']], dug=[KV['A902-D16']['y_m'], KV['A902-D17']['y_m']], vege_max=None),
            dict(kod='deli', nev='déli fal, D19 dugalj a konzol végénél (antenna nélkül)', tengely='y', sik=4.05, irany=+1, tart=(3.67, 7.00),
                 kotelezo=[], dug=[KV['A902-D19']['x_m']], vege_max=7.00)]
TERMEKEK = [dict(kod='KH-SOF-GALA-U', nev='Gala U 300 × 225', alak='U', meret=(3.00, 2.25)),
            dict(kod='U-320x250', nev='U 320 × 250 (generikus)', alak='U', meret=(3.20, 2.50)),
            dict(kod='KH-SOF-BLOK-CORNER', nev='Blok sarok L 290 × 230', alak='L', meret=(2.90, 2.30))]


HALO53 = '05.3 háló ajtaja'
HALO53_UT = float(os.environ.get('WSG_A902_MELLEK', '0.90'))   # a terasz és a 05.3 háló ajtaja felé: 0,90 (szigorú) vagy 0,75 (mellékút, mint A-811-ben)
D19_TAV = float(os.environ.get('WSG_A902_D19', '0.20'))          # a D19 dugalj legfeljebb ennyire lehet a TV-konzol végétől
_cel_eredeti = K.cel_szelesseg
def _cel(n, w): return min(w, HALO53_UT) if n in (HALO53, 'terasz (tolóajtó)') else _cel_eredeti(n, w)
K.cel_szelesseg = _cel


def kerulo_ok(A, akad):
    """Mint K.kerulo_ok (az A-902 céljaival)."""
    d = K.utak_hossza(A, akad); arany = 0.0
    for n, v in d.items():
        u = A['ures_tav'][n]
        if v is None or u is None or v > K.KERULO_SZORZO * u + K.KERULO_PLUSZ: return False, d, None
        arany = max(arany, v / max(u, 0.5))
    return True, d, round(arany, 2)


def lakas():
    P = unary_union([box(*r) for r in LOCK['rooms']['nappali_etkezo']])
    Wj = unary_union([box(*r) for k in JARHATO for r in LOCK['rooms'][k]]).difference(unary_union([box(*r) for r in PULT]))
    A = dict(L='A902', P=P, W=Wj, tiltott=shapely.Polygon(), swings={}, elsav={}, cel_geom={n: box(*r) for n, r in CELOK.items()},
             konyha=unary_union([box(*r) for r in LOCK['rooms']['konyha']]),
             W_szuk={w: Wj.buffer(-w / 2, **K.BUF) for w in sorted(set(K.UT_LEPCSO + [0.60, HALO53_UT]))})
    bx = Wj.bounds; xs = np.arange(bx[0] + K.RASZTER / 2, bx[2], K.RASZTER); ys = np.arange(bx[1] + K.RASZTER / 2, bx[3], K.RASZTER)
    A['rX'], A['rY'] = np.meshgrid(xs, ys)
    A['cel_cella'] = {n: shapely.contains_xy(g, A['rX'], A['rY']) for n, g in A['cel_geom'].items()}
    K.MELLEK_UT = None
    A['ures_tav'] = K.utak_hossza(A, [])
    return A


def jeloltek(A, tv, w, d):
    """Kanapé-befoglalók (S) és TV-konzolok (T) a tv falhoz: w a fallal párhuzamos, d a fal felé mért méret."""
    out = []; s0, s1 = tv['tart']
    for c in np.arange(s0 + K.TV_W / 2, s1 - K.TV_W / 2 + 1e-9, 0.05):
        if tv['vege_max'] is not None and not (c + K.TV_W / 2 <= tv['vege_max'] + 1e-9 and any(0 <= x - (c + K.TV_W / 2) <= D19_TAV for x in tv['dug'])): continue
        if tv['vege_max'] is None and not (all(abs(c - k) <= K.TV_W / 2 for k in tv['kotelezo']) and any(abs(c - k) <= K.TV_W / 2 for k in tv['dug'])): continue
        for o in K.OFFS:
            cs = c + o
            for e in np.arange(tv['sik'] + K.TV_D + K.TV_KANAPE_MIN, tv['sik'] + 6.0, 0.10):      # a kanapé TV felőli éle
                nezo = (e + d - K.SZEM) - (tv['sik'] + K.KEPERNYO)
                if nezo < K.NEZO[0] - 1e-9: continue
                if nezo > K.NEZO[1] + 1e-9: break
                if tv['tengely'] == 'y':
                    S = box(cs - w / 2, e, cs + w / 2, e + d); T = box(c - K.TV_W / 2, tv['sik'], c + K.TV_W / 2, tv['sik'] + K.TV_D)
                else:
                    S = box(e, cs - w / 2, e + d, cs + w / 2); T = box(tv['sik'], c - K.TV_W / 2, tv['sik'] + K.TV_D, c + K.TV_W / 2)
                if A['P'].contains(S) and A['P'].contains(T): out.append(dict(S=S, T=T, nezo=round(nezo, 2), O=o, c=c))
    out.sort(key=lambda j: abs(j['nezo'] - K.NEZO_CEL) + 0.5 * abs(j['O']))
    return out


def keres(A, tv, w, d, Z, elso=False):
    best = None
    for j in jeloltek(A, tv, w, d):
        S, T = j['S'], j['T']
        if S.distance(Z) < K.ETK_MIN - 1e-9 or T.intersects(Z): continue
        akad = [S, T, Z]
        if not K.szabad_ter(A, akad, K.UT)[0]: continue
        kok, utak, arany = kerulo_ok(A, akad)
        if not kok: continue
        u = K.UT if elso else K.max_ut(A, akad)
        pont = (u, -arany, -(abs(j['nezo'] - K.NEZO_CEL) + 0.5 * abs(j['O'])))
        if best is None or pont > best['pont']:
            best = dict(pont=pont, tv=tv, S=S, T=T, ut=u, nezo=j['nezo'], tv_eltolas=j['O'], utak=utak, kerulo_arany=arany, w=w, d=d)
        if elso: return best
        if best['ut'] >= 1.20 and abs(best['nezo'] - K.NEZO_CEL) <= 0.30: break
    return best


def r3(b): return [round(float(v), 3) for v in b]


def alak_poly(S, tv, alak, m=0.95):
    """A befoglalóból a háttámla (a TV-vel szemközti oldalon) és a szárak – jelzés a rajzhoz."""
    x0, y0, x1, y1 = S.bounds
    if tv['tengely'] == 'y':   # a TV délen (kisebb y) – a háttámla északon
        hat = box(x0, y1 - m, x1, y1); bal = box(x0, y0, x0 + m, y1); jobb = box(x1 - m, y0, x1, y1)
    else:                      # a TV nyugaton (kisebb x) – a háttámla keleten
        hat = box(x1 - m, y0, x1, y1); bal = box(x0, y0, x1, y0 + m); jobb = box(x0, y1 - m, x1, y1)
    return unary_union([hat, bal, jobb]) if alak == 'U' else unary_union([hat, jobb])


if __name__ == '__main__':
    t0 = time.time(); A = lakas(); eredmeny = []; legjobbak = {}
    print('üres lakás úthosszak', A['ures_tav'], flush=True)
    for zk, zb in ZONAK.items():
        Z = box(*zb)
        for tm in TERMEKEK:
            for tv in TV_FALAK:
                best = None
                for (w, d) in ([tm['meret'], tm['meret'][::-1]]):
                    b = keres(A, tv, w, d, Z)
                    if b and (best is None or b['pont'] > best['pont']): best = b
                o = None
                if best:
                    cm = __import__('terv_elrendezes_a811').cel_max(A, [best['S'], best['T'], Z])
                    o = dict(kanape_befoglalo=r3(best['S'].bounds), tv_konzol=r3(best['T'].bounds), legszukebb_ut_m=best['ut'], nezotav_m=best['nezo'],
                             tv_eltolas_m=best['tv_eltolas'], kerulo_max_arany=best['kerulo_arany'], uthossz_m=best['utak'], cel_max_szelesseg_m=cm,
                             tajolas=f"{best['w']:.2f} a TV-fallal párhuzamosan × {best['d']:.2f} a TV felé".replace('.', ','))
                    legjobbak[(zk, tm['kod'], tv['kod'])] = (best, Z)
                eredmeny.append(dict(etkezo=zk, etkezo_zona=list(zb), kanape=tm['kod'], kanape_nev=tm['nev'], tv=tv['kod'], tv_nev=tv['nev'], elfer=o is not None, elrendezes=o))
                print(zk, tm['kod'], tv['kod'], 'ELFÉR' if o else 'NEM', o and o['legszukebb_ut_m'], o and o['nezotav_m'], o and o['kanape_befoglalo'], f'{time.time() - t0:.0f}s', flush=True)
    # rajz: a terv asztalhelyével (betolt székek), termékenként a jobb TV-fal
    A['C'] = dict(nezet=(3.2, 0.9, 11.2, 8.6), pult=PULT)
    A['lock'] = LOCK; A['nappali_aljzatok'] = [k for k in V['kiallasok'] if ('NAPPALI' in k['helyiseg'] or 'ÉTKEZ' in k['helyiseg']) and k['tipus'] in ('dugalj', 'antenna_tv_aljzat', 'gyengearamu_aljzat')]
    panelek = []
    for tm in TERMEKEK:
        for tv in TV_FALAK:
            zk = 'terv, 0,30 m-rel nyugatra'; Z = box(*ZONAK[zk]); bz = legjobbak.get((zk, tm['kod'], tv['kod']))
            im = K.panel(A, '', None, dict(alak='L'), None, px=80); dr = ImageDraw.Draw(im, 'RGBA')
            x0, y0, x1, y1 = A['C']['nezet']; T_ = lambda x, y: (round((x - x0) * 80), round(62 + (y1 - y) * 80))
            def poly(g, fill=None, outline=None, width=1):
                for p in shapely.get_parts(g):
                    if p.geom_type == 'Polygon': dr.polygon([T_(*c) for c in p.exterior.coords], fill=fill, outline=outline, width=width)
            if bz:
                best, _ = bz
                ok, parts, be = K.szabad_ter(A, [best['S'], best['T'], Z], K.UT)
                for p, b_ in zip(parts, be if be is not None else []):
                    if b_: poly(p, fill=K.SZIN['ut'] + (90,))
                poly(best['S'], outline=K.SZIN['kanape'] + (255,), width=2)
                poly(alak_poly(best['S'], tv, tm['alak']), fill=K.SZIN['kanape'] + (120,), outline=K.SZIN['kanape'] + (255,))
                poly(best['T'], fill=K.SZIN['tv'] + (180,))
            poly(Z, fill=K.SZIN['etk'] + (45,), outline=K.SZIN['etk'] + (255,), width=2); poly(box(*ASZTAL), fill=K.SZIN['etk'] + (200,))
            for nev, k in (('ML04', 'A902-ML04'), ('ML05', 'A902-ML05')):
                p = T_(KV[k]['x_m'], KV[k]['y_m']); dr.ellipse([p[0] - 7, p[1] - 7, p[0] + 7, p[1] + 7], fill=(255, 210, 0, 255), outline=(0, 0, 0, 255)); dr.text((p[0] + 9, p[1] - 7), nev, fill=(0, 0, 0), font=K.FS)
            dr.rectangle([0, 0, im.size[0], 60], fill=(255, 255, 255, 255))
            dr.text((8, 4), f"{tm['nev']} · TV: {tv['nev']}", fill=(0, 0, 0), font=K.FB)
            if bz:
                best, _ = bz; cm = [e for e in eredmeny if e['etkezo'] == zk and e['kanape'] == tm['kod'] and e['tv'] == tv['kod']][0]['elrendezes']['cel_max_szelesseg_m']
                dr.text((8, 22), f"ELFÉR · legszűkebb út ≥ {best['ut']:.2f} m · nézőtáv {best['nezo']:.2f} m · kerülő ≤ {best['kerulo_arany']:.1f}×".replace('.', ','), fill=(20, 120, 40), font=K.F)
                dr.text((8, 41), ' · '.join(f"{n.split(' (')[0]} {v:.2f}".replace('.', ',') for n, v in cm.items() if v), fill=(60, 60, 60), font=K.FS)
            else:
                dr.text((8, 22), 'NEM FÉR EL a feltételekkel (étkező 0,30 m-rel nyugatra)', fill=(200, 30, 30), font=K.F)
            panelek.append(im)
    lab = ['MÉRETPRÓBA – nem stílusterv. Geometria: geometry_lock_A902_v2b (terv szerinti), helyszínen nem mért. Étkező: a terv asztala betolt székekkel, 0,30 m-rel nyugatra (a terv helyén a 05.3 háló ajtajához csak 0,6 m maradna); konyhapult a terv szerint.',
           'Kék: kanapé-befoglaló (sötétebb: háttámla és szárak, 95 cm – jelzés); barna: TV-konzol 180 × 45; narancs: étkező; halványzöld: a bejáratból 0,90 m-es úttal elérhető szabad tér; sárga: lámpakiállás.',
           'Célok: bejárat, terasz tolóajtó (0,90 m, a fő kültér), konyha, hálók folyosója, 05.3 háló ajtaja. Kerülő ≤ 1,5 × üres + 1 m. Nézőtáv 2,0–3,4 m.']
    K.lap(panelek, 'A-902 – nappali-étkező, U/L kanapé méretpróba, szigorú (minden út 0,90 m; étkező 0,30 m-rel nyugatra) · 2026-10-24', lab).save(os.path.join(K.HERE, 'kanape_meretproba_A902.png'), optimize=True)
    json.dump(dict(datum='2026-10-24', statusz='MÉRETPRÓBA – nem stílusterv; geometry_lock_A902_v2b (terv szerinti), helyszínen nem mért',
                   forras='WGR1_meretezett_alaprajzok.pdf 18. o. bútorrétege (M1 KORR 2); A902_villamos.json; Péter 2026-10-24 18:23', celok=CELOK, pult=PULT,
                   etkezo_zonak=ZONAK, asztal=ASZTAL, lampa_ML04=LAMPA_ETK, ures_uthossz_m=A['ures_tav'], eredmeny=eredmeny),
              open(os.path.join(K.HERE, 'kanape_meretproba_A902.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('kész', f'{time.time() - t0:.0f}s')
