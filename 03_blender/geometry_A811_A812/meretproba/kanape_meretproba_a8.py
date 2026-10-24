# =====================================================================================
# A-811 / A-812 – kanapé-méretpróba (U és L) a nappali-étkezőben (2026-10-24, Claude)
# MÉRETPRÓBA – nem stílusterv és nem elrendezési javaslat. Kérdés: a „minimum L, inkább U” kanapé (CLAUDE.md, Péter
# 2026-10-24) elfér-e a TV-vel, egy étkezővel és a szükséges közlekedéssel; ha nem, mekkora U/L befoglaló fér el,
# és mi változik, ha a TV nem a gyári TV-blokkra, hanem egy másik fal meglévő dugaljára kerül (antenna nélkül, WiFi).
#
# Bemenet (csak repóadat, TERV SZERINT):
#   03_blender/geometry_lock_<L>.json – helyiségek, erkélyajtók nyitása (a PR #9 alaprajzi modellje);
#   01_alaprajzok/villamos_kiallasok/<L>_villamos.json – antenna- és erősáramú aljzatok.
# Termék: csak a két, mindkét befoglaló méretével ismert kanapé az árkönyvtárból (PR #8, 2026-10-24):
#   KH-SOF-GALA-U 300 × 225 cm, KH-SOF-BLOK-CORNER 290 × 230 cm. A többi L-kanapé (Martina 287, Blok 330, Neom 263)
#   mélysége nem ismert → nem próbálható.
# Tesztméretek és feltételek (BECSLÉS, nem termékadat):
#   - TV-konzol 180 × 45 cm a TV falán; legalább egy meglévő dugalj a konzol mögé esik (|Δx| ≤ 0,90 m); a gyári
#     TV-blokknál az antennaaljzat is;
#   - nézőtáv 2,0–3,4 m (szem a kanapé hátától 0,50 m-re, falra szerelt TV képernyője a faltól 0,10 m-re);
#   - a TV középvonala legfeljebb 0,40 m-rel tér el a kanapé-befoglaló középvonalától;
#   - a kanapé nyitott oldala és a TV-konzol között ≥ 0,60 m;
#   - az erkélyajtók nyitási negyedköre (+5 cm) bútormentes; az ajtóhoz vezető utat a közlekedés-ellenőrzés adja
#     (v2, 17:35: a korábbi külön 0,80 m-es sáv a szárnyak előtt kettős számolás volt, kivéve);
#   - étkezőzóna a GOAL 5. pont szerint („étkezőszék hátratolás 90”): 6 fős = 180 × 90 asztal, 3 + 3 szék a hosszú
#     oldalakon, 90 cm hátratolás → 180 × 270 cm; 4 fős = Ø100 kerek asztal + 90 cm → Ø280. Érzékenységi („szoros”)
#     változat 60 cm-rel (180 × 210, Ø220) – ez a GOAL-szabály alatt van. Az étkezőzóna és a kanapé, illetve a
#     TV-konzol között ≥ 0,60 m;
#   - közlekedés: legalább 0,90 m széles, összefüggő út a bejárattól minden erkélyajtóig, a konyháig és a hálók
#     folyosójáig. Számítás: a járható terület a falaktól és a bútoroktól fél útszélességgel szűkítve (Minkowski);
#     a „legszűkebb út” a 0,90 … 1,40 m-es próbák közül a legnagyobb, amelyik még átmegy. A célpontok a helyiség-
#     csatlakozások nappali felőli 0,75 m-es sávjai, így az előtér és a folyosó saját szélessége nem torzít.
#     A konyha járható, a villamos kiállások (TERV SZERINT konyhatechnológia) szerinti 60 cm-es pultsávokkal – A-811
#     U-, A-812 L-konyha (BECSLÉS; a konyha berendezése a stílusterv része); a konyhacél a pultok előtti sáv.
#   - kerülő: a bejárattól minden célig vezető legrövidebb út (5 cm-es rácson, a 0,90 m-es út szabad terében) legfeljebb
#     1,5 × az üres lakásbeli + 1,0 m lehet – így nem fogadunk el olyan elrendezést, ahol pl. a konyhába a kanapé körül
#     kell kerülni.
# Kimenet: kanape_meretproba_A811_A812.json, kanape_meretproba_<L>_<változat>.png (ebben a mappában)
# Futtatás: python3 kanape_meretproba_a8.py
# =====================================================================================
import os, json, math, time
import numpy as np
import shapely
from shapely.geometry import box, Point, Polygon
from shapely.ops import unary_union
from PIL import Image, ImageDraw, ImageFont
from skimage.graph import MCP_Geometric

HERE = os.path.dirname(os.path.abspath(__file__)); GEO = os.path.dirname(HERE); B = os.path.dirname(GEO); REPO = os.path.dirname(B)

TERMEKEK = [
    dict(kod='KH-SOF-GALA-U', nev='Gala U 300 × 225', alak='U', meret=(3.00, 2.25),
         forras='Kave Home Gala 5 személyes sarokkanapé + végmodul, 300 × 225 cm (árkönyvtár, PR #8, 2026-10-24; webshop-keresőkártya). '
                'Az árkönyvtár „U-szerű”-nek írja; a modulkiosztás a termékoldalon ellenőrizendő. A próba a befoglalóval számol.'),
    dict(kod='KH-SOF-BLOK-CORNER', nev='Blok sarok L 290 × 230', alak='L', meret=(2.90, 2.30),
         forras='Kave Home Blok 3 személyes sarokkanapé, 290 × 230 cm (árkönyvtár, PR #8, 2026-10-24; webshop-keresőkártya).'),
]
ETKEZOK = [
    dict(kod='6', nev='6 fős étkező', leiras='180 × 90 asztal, 3 + 3 szék, 90 cm hátratolás (GOAL 5.) → 180 × 270 cm', alak='teglalap', meret=(1.80, 2.70), asztal=(1.80, 0.90), szoros='6s'),
    dict(kod='4', nev='4 fős kerek étkező', leiras='Ø100 kerek asztal, 90 cm hátratolás (GOAL 5.) → Ø280', alak='kor', r=1.40, asztal_r=0.50, szoros='4s'),
    dict(kod='0', nev='étkező nélkül', leiras='csak kanapé + TV', alak=None),
    dict(kod='6s', nev='6 fős étkező, SZOROS', leiras='180 × 90, 60 cm hátratolás → 180 × 210 cm (a GOAL 90 cm-es szabálya alatt)', alak='teglalap', meret=(1.80, 2.10), asztal=(1.80, 0.90)),
    dict(kod='4s', nev='4 fős kerek, SZOROS', leiras='Ø100, 60 cm hátratolás → Ø220 (a GOAL-szabály alatt)', alak='kor', r=1.10, asztal_r=0.50),
]
EK = {E['kod']: E for E in ETKEZOK}
PANEL_ETK = ['6', '4', '0']   # a képen: ha a GOAL-változat nem fér el, a szoros változatot mutatjuk, jelölve
TV_W, TV_D = 1.80, 0.45
NEZO = (2.0, 3.4); NEZO_CEL = 2.7; SZEM = 0.50; KEPERNYO = 0.10
TV_KANAPE_MIN = 0.60; UT = 0.90; UT_LEPCSO = [0.90, 1.00, 1.10, 1.20, 1.30, 1.40]
ETK_MIN = 0.05   # v2: az étkezőzóna már tartalmazza a széktolás 90 (ill. 60) cm-ét – a kanapé háta közvetlenül mellé jöhet
BUF = dict(join_style='round', quad_segs=8)   # v2: az út szélessége körrel (a sarkoknál nem négyzetes többlet)
BEJARAT = 'bejárat (előtér felől)'
STEP = 0.10; OFFS = (-0.40, -0.20, 0.0, 0.20, 0.40)          # rácslépés; a TV középvonalának eltolása a kanapéhoz képest
RASZTER = 0.05; KERULO_SZORZO, KERULO_PLUSZ = 1.5, 1.0           # kerülő-feltétel: d ≤ 1,5 · d_üres + 1,0 m
# forgatókönyv: A = szigorú (minden célhoz 0,90 m-es közlekedő); B = az erkélyajtókhoz 0,60 m-es mellékút (GOAL 5.:
# „Közlekedő 90–120 cm, mellék 60–90”), a konyhához és a hálókhoz továbbra is 0,90 m
FK = os.environ.get('WSG_FORGATOKONYV', 'A'); assert FK in ('A', 'B')
MELLEK_UT = 0.60 if FK == 'B' else None
FK_NEV = {'A': 'A – szigorú: minden célhoz 0,90 m', 'B': 'B – az erkélyajtókhoz 0,60 m-es mellékút, a konyhához és a hálókhoz 0,90 m'}[FK]
FK_ROVID = {'A': 'A – szigorú', 'B': 'B – erkélyhez 60 cm-es mellékút'}[FK]


def cel_szelesseg(n, w):
    return min(w, MELLEK_UT) if (MELLEK_UT and 'erkélyajtó' in n) else w

# TV-falak: y = a falsík, x = a konzol helye (tól–ig), irany = +1, ha a kanapé a fal fölött (nagyobb y) van, −1, ha alatta;
# dug = a falon lévő meglévő dugaljak x-e (a villamos JSON-ból ellenőrizve), ant = az antennaaljzat x-e (csak a gyári blokknál kötelező).
LAKAS = {
    # pult: a konyha villamos kiállásai (TERV SZERINT, M1 konyhatechnológia) szerinti pultsávok, 60 cm – A-811: U-konyha
    # (alsó fal: főzőlap-bekötés X01 és dugaljak; jobb fal: D06, FL01; felső fal: D03–D05); A-812: L-konyha (jobb fal:
    # X01, D06–D11; felső fal: D04, D05, FL01) + hűtő-oszlop az akna mellett (D12) – BECSLÉS, a konyha a stílusterv része
    'A811': dict(jarhato=['nappali_etkezo', 'eloter', 'kozlekedo', 'konyha'], pult=[[6.17, 8.55, 8.25, 9.15], [7.65, 9.15, 8.25, 11.55], [6.17, 10.95, 7.65, 11.55]],
                 celok={BEJARAT: (5.42, 6.75, 6.92, 8.40), 'egyszárnyú erkélyajtó': (0.0, 6.85, 0.75, 7.63),
                        'kétszárnyú erkélyajtó': (0.0, 8.66, 0.75, 10.38), 'konyha (pult előtti sáv)': (6.17, 9.15, 7.65, 10.95),
                        'hálók folyosója': (5.12, 6.40, 6.17, 7.40)},
                 tv=[dict(kod='gyari', nev='gyári TV-blokk (rajzon alsó fal, y = 6,651), antennával', y=6.651, x=(0.0, 4.60), irany=+1,
                          dug=['A811-D15', 'A811-D16'], ant='A811-G07'),
                     dict(kod='felso', nev='felső külső fal (y = 11,55), meglévő dugaljra, antenna nélkül', y=11.55, x=(0.0, 6.17), irany=-1,
                          dug=['A811-D10', 'A811-D11', 'A811-D12'], ant=None)],
                 nezet=(-0.75, 5.35, 8.75, 12.05),
                 megj='A gyári TV-blokk falának sarkán (x ≈ 5,0) kapcsolóoszlop, termosztát és érzékelő – ott a konzol nem lehet (x ≤ 4,60).'),
    'A812': dict(jarhato=['nappali_etkezo', 'eloter', 'kozlekedo', 'konyha'], pult=[[7.65, 0.0, 8.25, 2.80], [6.20, 2.20, 7.65, 2.80], [5.80, 0.0, 6.45, 0.60]],
                 celok={BEJARAT: (6.47, 2.95, 7.60, 4.05), 'kétszárnyú erkélyajtó': (0.0, 0.98, 0.75, 2.70),
                        'konyha (pult előtti sáv)': (5.80, 0.60, 7.65, 2.20), 'hálók folyosója': (6.17, 3.95, 7.22, 4.95)},
                 tv=[dict(kod='gyari', nev='gyári TV-blokk (rajzon alsó fal, y = 0), antennával', y=0.0, x=(0.0, 5.80), irany=+1,
                          dug=['A812-D17', 'A812-D18'], ant='A812-G08'),
                     dict(kod='also_d19', nev='ugyanez a fal, D19 dugaljra (x = 4,60), antenna nélkül', y=0.0, x=(0.0, 5.80), irany=+1,
                          dug=['A812-D19'], ant=None),
                     dict(kod='felso', nev='felső fal (y = 4,70, x 3,32–5,47), D15 dugaljra, antenna nélkül', y=4.70, x=(3.32, 5.47), irany=-1,
                          dug=['A812-D15'], ant=None),
                     dict(kod='fulke', nev='fülke felső külső fala (y = 5,60, x 0–3,22), D13 dugaljra, antenna nélkül', y=5.60, x=(0.0, 3.22), irany=-1,
                          dug=['A812-D13'], ant=None)],
                 nezet=(-1.05, -0.55, 8.75, 6.15),
                 megj='x > 5,80 a konyha; a nappali felső-bal részén 3,22 × 0,90 m-es fülke (y 4,70–5,60).'),
}


def negyedkor(m, puffer=0.05):
    hx, hy = m['zsaner']; r = m['r'] + puffer; lo, hi = m['nyilas']
    d1 = (0, 1 if abs(hy - lo) <= abs(hy - hi) else -1) if m['fal'] == 'y' else (1 if abs(hx - lo) <= abs(hx - hi) else -1, 0)
    d2 = {'+x': (1, 0), '-x': (-1, 0), '+y': (0, 1), '-y': (0, -1)}[m['irany']]
    pts = [(hx, hy)] + [(hx + r * (math.cos(t) * d1[0] + math.sin(t) * d2[0]), hy + r * (math.cos(t) * d1[1] + math.sin(t) * d2[1]))
                        for t in [i * math.pi / 2 / 24 for i in range(25)]]
    return Polygon(pts)


def lakas_adat(L):
    C = LAKAS[L]
    lock = json.load(open(os.path.join(B, f'geometry_lock_{L}.json'), encoding='utf-8'))
    V = json.load(open(os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', f'{L}_villamos.json'), encoding='utf-8'))
    K = {k['azonosito']: k for k in V['kiallasok']}
    P = unary_union([box(*r) for r in lock['rooms']['nappali_etkezo']])
    # járható terület: nappali, előtér, közlekedő és a konyha – a konyhában a nyitott oldallal szemközti falon 60 cm-es
    # pultsávval (egysoros konyha feltételezve; L/U-konyha vagy sziget ennél kevesebb helyet hagy – BECSLÉS)
    Wj = unary_union([box(*r) for k in C['jarhato'] for r in lock['rooms'][k]]).difference(unary_union([box(*r) for r in C['pult']]))
    ajtok = {n: m for n, m in lock['openings_meta'].items() if n.startswith('Erkelyajto') and negyedkor(m).intersects(P)}
    swings = {n: negyedkor(m) for n, m in ajtok.items()}
    elsav = {}   # v2: nincs külön sáv a szárnyak előtt
    tiltott = unary_union(list(swings.values()))
    tvk = []
    for t in C['tv']:
        for a in t['dug'] + ([t['ant']] if t['ant'] else []):           # a megadott aljzat valóban a TV falán, a nappali felől van-e
            k = K[a]; assert 'NAPPALI' in k['helyiseg'] and 0 <= (k['y_m'] - t['y']) * t['irany'] <= 0.50 and t['x'][0] - 0.3 <= k['x_m'] <= t['x'][1] + 0.3, (L, a, k)
        tvk.append(dict(t, x_dug=np.array([K[a]['x_m'] for a in t['dug']]), x_ant=(K[t['ant']]['x_m'] if t['ant'] else None),
                        aljzatok=[K[a] for a in t['dug'] + ([t['ant']] if t['ant'] else [])]))
    A = dict(L=L, C=C, lock=lock, P=P, W=Wj, ajtok=ajtok, swings=swings, elsav=elsav, tiltott=tiltott, tv=tvk,
             nappali_aljzatok=[k for k in V['kiallasok'] if 'NAPPALI' in k['helyiseg'] and k['tipus'] in ('dugalj', 'antenna_tv_aljzat', 'gyengearamu_aljzat')],
             cel_geom={n: box(*r) for n, r in C['celok'].items()}, konyha=unary_union([box(*r) for r in lock['rooms']['konyha']]),
             W_szuk={w: Wj.buffer(-w / 2, **BUF) for w in sorted(set(UT_LEPCSO + [0.60]))})
    A['etk'] = {E['kod']: etkezo_jeloltek(A, E) for E in ETKEZOK if E['alak']}
    # raszter a kerülő-számításhoz (cellaközéppontok a járható terület befoglalóján)
    bx = Wj.bounds; xs = np.arange(bx[0] + RASZTER / 2, bx[2], RASZTER); ys = np.arange(bx[1] + RASZTER / 2, bx[3], RASZTER)
    A['rX'], A['rY'] = np.meshgrid(xs, ys)
    A['cel_cella'] = {n: shapely.contains_xy(g, A['rX'], A['rY']) for n, g in A['cel_geom'].items()}
    A['ures_tav'] = utak_hossza(A, [])
    return A


def szabad_resz(A, akadalyok, w):
    E = A['W_szuk'][w]
    if akadalyok: E = E.difference(shapely.union_all([o.buffer(w / 2, **BUF) for o in akadalyok]))
    return E


def utak_hossza(A, akadalyok, w=UT):
    """A bejárattól az egyes célokig vezető legrövidebb út hossza (m) a cél útszélességének szabad terében; None = nem érhető el."""
    out, mezok = {}, {}
    for n in A['cel_geom']:
        if n == BEJARAT: continue
        ww = cel_szelesseg(n, w)
        if ww not in mezok:
            E = szabad_resz(A, akadalyok, ww)
            szabad = shapely.contains_xy(E, A['rX'], A['rY']) if not E.is_empty else np.zeros_like(A['rX'], bool)
            ind = np.argwhere(szabad & A['cel_cella'][BEJARAT])
            tav = MCP_Geometric(np.where(szabad, 1.0, np.inf)).find_costs([tuple(i) for i in ind])[0] if len(ind) else None
            mezok[ww] = (szabad, tav)
        szabad, tav = mezok[ww]
        t = tav[szabad & A['cel_cella'][n]] if tav is not None else np.array([])
        out[n] = round(float(t.min()) * RASZTER, 2) if len(t) and np.isfinite(t.min()) else None
    return out


def kerulo_ok(A, akadalyok):
    d = utak_hossza(A, akadalyok); arany = 0.0
    for n, v in d.items():
        u = A['ures_tav'][n]
        if v is None or u is None or v > KERULO_SZORZO * u + KERULO_PLUSZ: return False, d, None
        arany = max(arany, v / max(u, 0.5))
    return True, d, round(arany, 2)


def etkezo_jeloltek(A, E):
    P = A['P']; bx = P.bounds
    if E['alak'] == 'teglalap':
        G = []
        for aw, ad in (E['meret'], E['meret'][::-1]):
            X, Y = [a.ravel() for a in np.meshgrid(np.arange(bx[0], bx[2] - aw + 1e-9, STEP), np.arange(bx[1], bx[3] - ad + 1e-9, STEP), indexing='ij')]
            G.append(shapely.box(X, Y, X + aw, Y + ad))
        G = np.concatenate(G)
    else:
        r = E['r']
        X, Y = [a.ravel() for a in np.meshgrid(np.arange(bx[0] + r, bx[2] - r + 1e-9, STEP), np.arange(bx[1] + r, bx[3] - r + 1e-9, STEP), indexing='ij')]
        G = shapely.buffer(shapely.points(X, Y), r, quad_segs=12)
    G = G[shapely.contains(A['P'], G) & ~shapely.intersects(A['tiltott'], G)]
    kd = shapely.distance(G, A['konyha'])
    o = np.argsort(kd, kind='stable')
    return G[o], kd[o]


def kanape_jeloltek(A, tv, w, d, offs=OFFS):
    P = A['P']; bx = P.bounds; s = tv['irany']; ytv = tv['y']
    xs = np.round(np.arange(bx[0], bx[2] - w + 1e-9, STEP), 3)
    if s > 0: ys = np.round(np.arange(ytv + TV_D + TV_KANAPE_MIN, bx[3] - d + 1e-9, STEP), 3)
    else:     ys = np.round(np.arange(ytv - TV_D - TV_KANAPE_MIN - d, bx[1] - 1e-9, -STEP), 3)
    if not len(xs) or not len(ys): return []
    X, Y, O = [a.ravel() for a in np.meshgrid(xs, ys, np.array(offs), indexing='ij')]
    c = X + w / 2 + O
    nezo = (Y + d - SZEM) - (ytv + KEPERNYO) if s > 0 else (ytv - KEPERNYO) - (Y + SZEM)
    ok = (nezo >= NEZO[0] - 1e-9) & (nezo <= NEZO[1] + 1e-9) & (c - TV_W / 2 >= tv['x'][0] - 1e-9) & (c + TV_W / 2 <= tv['x'][1] + 1e-9)
    ok &= np.min(np.abs(c[:, None] - tv['x_dug'][None, :]), axis=1) <= TV_W / 2 + 1e-9
    if tv['x_ant'] is not None: ok &= np.abs(c - tv['x_ant']) <= TV_W / 2 + 1e-9
    X, Y, O, c, nezo = [a[ok] for a in (X, Y, O, c, nezo)]
    if not len(X): return []
    S = shapely.box(X, Y, X + w, Y + d)
    T = shapely.box(c - TV_W / 2, ytv, c + TV_W / 2, ytv + TV_D) if s > 0 else shapely.box(c - TV_W / 2, ytv - TV_D, c + TV_W / 2, ytv)
    ok = shapely.contains(P, S) & ~shapely.intersects(A['tiltott'], S) & shapely.contains(P, T) & ~shapely.intersects(A['tiltott'], T)
    out = [dict(S=S[i], T=T[i], nezo=round(float(nezo[i]), 3), O=float(O[i])) for i in np.nonzero(ok)[0]]
    out.sort(key=lambda j: (abs(j['nezo'] - NEZO_CEL) + 0.5 * abs(j['O'])))
    return out


def szabad_ter(A, akadalyok, w):
    """Összefüggő-e a bejárattól minden célig a cél útszélességének (w, ill. a B forgatókönyvben az erkélyajtóhoz 0,60) szabad tere.
    A visszaadott részek a w szélességhez tartoznak (rajzhoz)."""
    cache = {}
    def resz(ww):
        if ww not in cache:
            parts = shapely.get_parts(szabad_resz(A, akadalyok, ww))
            cache[ww] = (parts, shapely.intersects(parts, A['cel_geom'][BEJARAT]) if len(parts) else None)
        return cache[ww]
    ok = True
    for n, g in A['cel_geom'].items():
        if n == BEJARAT: continue
        parts, be = resz(cel_szelesseg(n, w))
        if not len(parts) or not be.any() or not (shapely.intersects(parts, g) & be).any(): ok = False; break
    parts, be = resz(w)
    return ok, parts, be


def max_ut(A, akadalyok):
    best = None
    for w in UT_LEPCSO:
        if szabad_ter(A, akadalyok, w)[0]: best = w
        else: break
    return best


def keres(A, tv, w, d, E, elso=False):
    """A legjobb elrendezés (vagy elso=True esetén az első megfelelő) a (w × d) befoglalójú kanapéhoz, a tv falhoz és az E étkezőhöz."""
    best = None
    G, kd = A['etk'][E['kod']] if E['alak'] else (None, None)
    for j in kanape_jeloltek(A, tv, w, d):
        S, T = j['S'], j['T']
        if not szabad_ter(A, [S, T], UT)[0]: continue            # ha már a kanapé + TV elzárja az utat, étkezővel sem lesz jobb
        if E['alak'] is None:
            cands = [(None, 0.0)]
        else:
            ok = (shapely.distance(G, S) >= ETK_MIN - 1e-9) & (shapely.distance(G, T) >= ETK_MIN - 1e-9)
            cands = [(G[i], float(kd[i])) for i in np.nonzero(ok)[0]]
        talalt = 0
        for g, k in cands:
            akad = [S, T] + ([g] if g is not None else [])
            if not szabad_ter(A, akad, UT)[0]: continue
            kok, utak, arany = kerulo_ok(A, akad)
            if not kok: continue
            u = UT if elso else max_ut(A, akad)
            pont = (u, -arany, -round(abs(j['nezo'] - NEZO_CEL) + 0.5 * abs(j['O']), 2), -k)
            if best is None or pont > best['pont']:
                best = dict(pont=pont, tv=tv, S=S, T=T, G=g, ut=u, nezo=j['nezo'], tv_eltolas=j['O'], konyha_tav=round(k, 2), w=w, d=d,
                            utak=utak, kerulo_arany=arany)
            if elso: return best
            talalt += 1
            if talalt >= 6: break
        if best and best['ut'] >= 1.20 and abs(best['nezo'] - NEZO_CEL) <= 0.30 and best['tv_eltolas'] == 0: break
    return best


def r2(b): return [round(float(v), 3) for v in b]


def kiir(best, E):
    if not best: return None
    S, T = best['S'], best['T']
    sav = S.bounds[1] - T.bounds[3] if best['tv']['irany'] > 0 else T.bounds[1] - S.bounds[3]
    o = dict(tv_fal=best['tv']['nev'], tv_aljzatok=[a['azonosito'] for a in best['tv']['aljzatok']], kanape_befoglalo=r2(S.bounds),
             kanape_tajolas=f"{best['w']:.2f} m a TV-fallal párhuzamosan × {best['d']:.2f} m a TV felé".replace('.', ','),
             tv_konzol=r2(T.bounds), legszukebb_ut_m=best['ut'], nezotav_m=best['nezo'], tv_eltolas_m=best['tv_eltolas'], kanape_tv_sav_m=round(sav, 2),
             uthossz_m=best['utak'], kerulo_max_arany=best['kerulo_arany'])
    if best['G'] is not None:
        g = best['G']
        o['etkezo_zona'] = r2(g.bounds) if E['alak'] == 'teglalap' else dict(kozep=r2(g.centroid.coords[0]), r=E['r'])
        o['etkezo_kanape_tav_m'] = round(g.distance(S), 2)
        o['etkezo_konyha_tav_m'] = best['konyha_tav']
    return o


# ----------------------------------------------------------------------------------------- rajz
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
F = ImageFont.truetype(FONT, 14); FS = ImageFont.truetype(FONT, 11); FB = ImageFont.truetype(FONTB, 15); FT = ImageFont.truetype(FONTB, 22)
SZIN = dict(kanape=(60, 110, 200), tv=(128, 70, 15), etk=(220, 120, 0), ajto=(220, 60, 60), cel=(20, 140, 40), ut=(120, 205, 120))


def panel(A, cim, best, termek, E, px=62):
    x0, y0, x1, y1 = A['C']['nezet']; Wp, Hp = int((x1 - x0) * px), int((y1 - y0) * px) + 62
    im = Image.new('RGB', (Wp, Hp), (255, 255, 255)); dr = ImageDraw.Draw(im, 'RGBA')
    T = lambda x, y: (round((x - x0) * px), round(62 + (y1 - y) * px))
    def poly(g, fill=None, outline=None, width=1):
        for p in shapely.get_parts(g):
            if p.is_empty or p.geom_type != 'Polygon': continue
            dr.polygon([T(*c) for c in p.exterior.coords], fill=fill, outline=outline, width=width)
    poly(A['W'], fill=(246, 246, 246, 255)); poly(A['konyha'].intersection(A['W']), fill=(250, 244, 220, 255))
    for r in A['C']['pult']: poly(box(*r), fill=(205, 185, 140, 255), outline=(150, 120, 60, 255))   # feltételezett pultsáv
    kc = A['konyha'].centroid; dr.text((T(kc.x, kc.y)[0] - 22, T(kc.x, kc.y)[1] - 8), 'konyha', fill=(150, 120, 40), font=FS)
    if best:
        ok, parts, be = szabad_ter(A, [best['S'], best['T']] + ([best['G']] if best['G'] is not None else []), UT)
        for p, b in zip(parts, be if be is not None else []):
            if b: poly(p, fill=SZIN['ut'] + (90,))
    for g in A['swings'].values(): poly(g, fill=SZIN['ajto'] + (45,), outline=SZIN['ajto'] + (160,))
    for g in A['elsav'].values(): poly(g.intersection(A['W']), fill=SZIN['ajto'] + (25,))
    for n, wl in A['lock']['walls'].items():
        if wl[2] > 0.5 or n.startswith('Plafon'): continue
        dr.rectangle([T(wl[0], wl[4]), T(wl[3], wl[1])], fill=(70, 70, 70, 255))
    for n, o in A['lock']['openings'].items():
        if n.endswith('_also') and ('Uvegfal' in n or 'Ablak' in n): dr.rectangle([T(o[0] - 0.02, o[4]), T(o[3] + 0.02, o[1])], fill=(80, 150, 230, 255))
    for g in A['cel_geom'].values(): b = g.bounds; dr.rectangle([T(b[0], b[3]), T(b[2], b[1])], outline=SZIN['cel'] + (200,), width=1)
    hasznalt = {a['azonosito'] for a in best['tv']['aljzatok']} if best else set()
    for k in A['nappali_aljzatok']:
        p = T(k['x_m'], k['y_m']); col = (255, 115, 0) if k['tipus'] == 'dugalj' else SZIN['tv']; r = 5 if k['azonosito'] in hasznalt else 3
        dr.ellipse([p[0] - r, p[1] - r, p[0] + r, p[1] + r], fill=col + (255,), outline=(0, 0, 0, 255) if r == 5 else None)
    if best:
        S = best['S']; sx0, sy0, sx1, sy1 = S.bounds; m = 0.95; s = best['tv']['irany']
        poly(S, fill=SZIN['kanape'] + (55,), outline=SZIN['kanape'] + (255,), width=2)
        hat = box(sx0, sy1 - m, sx1, sy1) if s > 0 else box(sx0, sy0, sx1, sy0 + m)
        ay0, ay1 = (sy0, sy1 - m) if s > 0 else (sy0 + m, sy1)
        mods = [hat, box(sx1 - m, ay0, sx1, ay1)] + ([box(sx0, ay0, sx0 + m, ay1)] if termek['alak'] == 'U' else [])
        for g in mods: poly(g, fill=SZIN['kanape'] + (110,), outline=SZIN['kanape'] + (255,))
        poly(best['T'], fill=SZIN['tv'] + (180,))
        if best['G'] is not None:
            g = best['G']; poly(g, fill=SZIN['etk'] + (45,), outline=SZIN['etk'] + (255,), width=2)
            if E['alak'] == 'teglalap':
                gx0, gy0, gx1, gy1 = g.bounds; cx, cy = (gx0 + gx1) / 2, (gy0 + gy1) / 2
                # az első tájolásban a zóna x-mérete = meret[0] és az asztal hossza x irányú; elforgatva fordítva
                tw, td = (E['asztal'][0], E['asztal'][1]) if abs((gx1 - gx0) - E['meret'][0]) < 1e-6 else (E['asztal'][1], E['asztal'][0])
                poly(box(cx - tw / 2, cy - td / 2, cx + tw / 2, cy + td / 2), fill=SZIN['etk'] + (200,))
            else:
                poly(g.centroid.buffer(E['asztal_r'], quad_segs=12), fill=SZIN['etk'] + (200,))
    dr.rectangle([0, 0, Wp, 60], fill=(255, 255, 255, 255))
    dr.text((8, 4), cim, fill=(0, 0, 0), font=FB)
    if best:
        t = f"ELFÉR · legszűkebb út ≥ {best['ut']:.2f} m · kerülő ≤ {best['kerulo_arany']:.1f}× · nézőtáv {best['nezo']:.2f} m".replace('.', ',')
        dr.text((8, 24), t, fill=(20, 120, 40), font=F)
        dr.text((8, 42), f"TV: {best['tv']['nev']}", fill=(60, 60, 60), font=FS)
    else:
        dr.text((8, 24), 'NEM FÉR EL a feltételekkel', fill=(200, 30, 30), font=F)
        dr.text((8, 42), ('(0,90 m-es út mindenhova' if FK == 'A' else '(0,90 m konyhához, 0,60 m erkélyhez') + ', kerülő nélkül; nézőtáv 2,0–3,4 m; ajtónyitás; TV dugaljnál)', fill=(120, 60, 60), font=FS)
    dr.rectangle([0, 0, Wp - 1, Hp - 1], outline=(150, 150, 150))
    return im


def lap(panelek, cim, labjegyzet):
    pw, ph = panelek[0].size; cols = 3; rows = math.ceil(len(panelek) / cols)
    im = Image.new('RGB', (pw * cols + 20, 44 + rows * (ph + 10) + 22 * len(labjegyzet) + 16), (255, 255, 255)); dr = ImageDraw.Draw(im)
    dr.text((10, 8), cim, fill=(0, 0, 0), font=FT)
    for i, p in enumerate(panelek): im.paste(p, (10 + (i % cols) * pw, 44 + (i // cols) * (ph + 10)))
    yb = 44 + rows * (ph + 10) + 4
    for i, t in enumerate(labjegyzet): dr.text((12, yb + 22 * i), t, fill=(40, 40, 40), font=F)
    return im


LAB = ['MÉRETPRÓBA – nem stílusterv. Terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért. Kék: kanapé-befoglaló (sötétebb: ülőmodulok, 95 cm – BECSLÉS, a valós',
       'modulkiosztás a termékoldalon ellenőrizendő); barna: TV-konzol 180 × 45 (tesztméret); pötty: a nappali aljzatai (narancs dugalj, barna antenna/adat; nagy = a TV-hez használt);',
       'narancs: étkezőzóna széktolással, benne az asztal; piros: erkélyajtó-nyitás; zöld keret: közlekedési célok (bejárat, erkélyajtók, konyha,',
       'hálók folyosója); halványzöld: a bejárattól elérhető szabad tér 0,90 m-es útra (az út középvonala ebben a sávban mozoghat); bézs: a konyha feltételezett',
       'pultsávja (a villamos kiállások szerint, 60 cm). Kilátás, stílus, anyag: nem tárgya.']


# ----------------------------------------------------------------------------------------- futás
def legjobb(A, tm, E, tvlista):
    lj = None
    for tv in tvlista:
        for (w, d) in ([tm['meret']] if tm['alak'] == 'U' else [tm['meret'], tm['meret'][::-1]]):
            b = keres(A, tv, w, d, E)
            if b and (lj is None or b['pont'] > lj['pont']): lj = b
    return lj


def best_jsonbol(A, o):
    """A JSON-ban rögzített elrendezésből a rajzhoz szükséges adatok (a TV-falak mind y = állandó síkúak)."""
    if not o: return None
    tv = next(t for t in A['tv'] if t['nev'] == o['tv_fal'])
    S = box(*o['kanape_befoglalo']); T = box(*o['tv_konzol']); G = None
    if 'etkezo_zona' in o:
        z = o['etkezo_zona']; G = box(*z) if isinstance(z, list) else Point(*z['kozep']).buffer(z['r'], quad_segs=12)
    b = S.bounds
    return dict(tv=tv, S=S, T=T, G=G, ut=o['legszukebb_ut_m'], nezo=o['nezotav_m'], kerulo_arany=o['kerulo_max_arany'], w=b[2] - b[0], d=b[3] - b[1])


def kepek(A, L, RL, valt):
    panelek = []
    for tm in TERMEKEK:
        res = RL['termekek'][tm['kod']][valt]
        for k in PANEL_ETK:
            E = EK[k]; o = res[k]['elrendezes']; cim = f"{tm['nev']} + {E['nev']}"
            if o is None and E.get('szoros') and res[E['szoros']]['elrendezes']:
                E = EK[E['szoros']]; o = res[E['kod']]['elrendezes']; cim = f"{tm['nev']} + {E['nev']} (90 cm-rel nem fér el)"
            panelek.append(panel(A, cim, best_jsonbol(A, o), tm, E))
    cim = f"{L} – nappali-étkező, U/L kanapé méretpróba – " + ('TV a gyári TV-blokkon' if valt == 'gyari_tv' else 'TV más fal meglévő dugaljára (Péter: a TV helye szabad)')
    lap(panelek, cim + f' · {FK_ROVID} (2026-10-24)', LAB + [f'Forgatókönyv {FK_NEV}.' + (' A zöld sáv a 0,90 m-es utat mutatja; az erkélyajtóhoz vezető 0,60 m-es mellékút ezen kívül is futhat.' if FK == 'B' else '')]).save(os.path.join(HERE, f'kanape_meretproba_{L}_{valt}_{FK}.png'), optimize=True)


if __name__ == '__main__':
    import sys
    JS = os.path.join(HERE, f'kanape_meretproba_A811_A812_{FK}.json')
    if '--kepek' in sys.argv:   # csak újrarajzolás a mentett eredményből
        D = json.load(open(JS, encoding='utf-8'))
        for L in LAKAS:
            A = lakas_adat(L)
            for valt in ('gyari_tv', 'mas_tv_fal'): kepek(A, L, D['eredmeny'][L], valt)
        print('képek kész'); raise SystemExit
    t0 = time.time(); eredmeny = {}
    for L in LAKAS:
        A = lakas_adat(L)
        R = dict(megjegyzes=LAKAS[L]['megj'], nappali_m2=round(A['P'].area, 2), ures_lakas_legszukebb_ut_m=max_ut(A, []), ures_lakas_uthossz_m=A['ures_tav'],
                 tv_falak=[t['nev'] for t in A['tv']], termekek={}, max_befoglalo={})
        for valt, tvlista in (('gyari_tv', [t for t in A['tv'] if t['kod'] == 'gyari']), ('mas_tv_fal', [t for t in A['tv'] if t['kod'] != 'gyari'])):
            for tm in TERMEKEK:
                R['termekek'].setdefault(tm['kod'], {}).setdefault(valt, {})
                for E in ETKEZOK:
                    lj = legjobb(A, tm, E, tvlista)
                    R['termekek'][tm['kod']][valt][E['kod']] = dict(etkezo=E['nev'], leiras=E['leiras'], elfer=lj is not None, elrendezes=kiir(lj, E))
                    print(L, valt, tm['kod'], E['kod'], 'ELFÉR' if lj else 'NEM', (lj or {}).get('ut'), (lj or {}).get('kerulo_arany'), (lj or {}).get('nezo'),
                          lj and lj['tv']['kod'], f'{time.time() - t0:.0f}s', flush=True)
            kepek(A, L, R, valt)
            # keresési korlát: mekkora befoglaló fér el (nem termékméret!) – W a TV-fallal párhuzamos, D a TV felé
            R['max_befoglalo'][valt] = {}
            for E in [EK[k] for k in ('6', '4', '0')]:   # a szoros változatokra nem futtatjuk (idő)
                R['max_befoglalo'][valt][E['kod']] = {}
                for d in (1.60, 2.25):
                    talalt = None
                    # növekvő W, az első kudarcnál megáll: pontos, mert ha a W szélességű kanapé elfér, akkor az ugyanazzal a
                    # középvonallal elhelyezett keskenyebb is (a befoglalója részhalmaz, a nézőtáv és a TV-eltolás nem változik)
                    for w in np.round(np.arange(2.20, 3.85, 0.10), 2):
                        if any(keres(A, tv, float(w), d, E, elso=True) for tv in tvlista): talalt = float(w)
                        else: break
                    R['max_befoglalo'][valt][E['kod']][f'{d:.2f}'] = talalt
                    print(L, valt, 'max', E['kod'], d, talalt, f'{time.time() - t0:.0f}s', flush=True)
        eredmeny[L] = R
    json.dump(dict(datum='2026-10-24', statusz='MÉRETPRÓBA – nem stílusterv; terv szerinti geometria (PR #9, geometria v2 lock), helyszínen nem mért',
                   forgatokonyv=FK_NEV, kanapek=TERMEKEK, etkezok=ETKEZOK,
                   feltetelek=dict(tv_konzol_m=[TV_W, TV_D], nezotav_m=list(NEZO), szem_a_kanape_hatatol_m=SZEM, kepernyo_a_faltol_m=KEPERNYO,
                                   tv_eltolas_max_m=max(OFFS), kanape_tv_sav_min_m=TV_KANAPE_MIN, etkezo_tav_min_m=ETK_MIN, ut_min_m=UT, racs_m=STEP,
                                   mellekut_erkelyhez_m=MELLEK_UT,
                                   erkelyajto='nyitási negyedkör + 5 cm bútormentes; az ajtóhoz vezető utat a közlekedés-ellenőrzés adja',
                                   utszelesseg='kör alakú (Euklideszi) puffer – a sarkoknál nincs négyzetes többlet',
                                   kerulo=f'a bejárattól minden célig: út ≤ {KERULO_SZORZO} × az üres lakásbeli + {KERULO_PLUSZ} m (5 cm-es rács)',
                                   konyha_pult={L: LAKAS[L]['pult'] for L in LAKAS},
                                   celok={L: LAKAS[L]['celok'] for L in LAKAS}),
                   eredmeny=eredmeny),
              open(JS, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('kész', f'{time.time() - t0:.0f}s')
