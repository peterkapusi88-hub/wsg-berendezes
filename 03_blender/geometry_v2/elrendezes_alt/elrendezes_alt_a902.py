# =====================================================================================
# A-902 – nappali–étkező elrendezési alternatívák (Claude, 2026-10-25). Péter 02:33 és 02:52 CET:
# „A 36–38 cm-es közlekedőt nem fogadom el. Készítsd el a 2–3 valóban használható alternatívát, hat étkezőhellyel,
#  a székek kihúzásához és a közlekedéshez szükséges valós méretekkel.” Lennon L (S01) és JÄTTEBO U (S02) marad.
# MÉRETPRÓBA – nem stílusterv és nem kivitelezési terv. Geometria: 03_blender/geometry_lock_A902_v2b.json (terv szerinti,
# helyszínen nem mért); kiállások: 01_alaprajzok/villamos_kiallasok/A902_villamos.csv; konyhapult: a terv bútorrétege
# (WGR1 18. o., M1 KORR 2), mint a kanape_meretproba_a902.py-ban.
# Szabályok (promptsablon v3.1 §1, Péter 02:33): fő út ≥ 0,90 m; mellékút 0,75 m csak az asztal terasz felőli oldalán;
# székkihúzás ≥ 0,90 m az asztal élétől; kanapé–TV-bútor ≥ 0,60 m; nézőtáv 2,0–3,4 m.
# Futtatás: python3 elrendezes_alt_a902.py  → elrendezes_alt_A902_v1.json / .png
# =====================================================================================
import os, json, math
import numpy as np, shapely
from shapely.geometry import box, Point, LineString, Polygon
from shapely.ops import unary_union
from shapely import affinity
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__)); B = os.path.dirname(os.path.dirname(HERE)); REPO = os.path.dirname(B)
LOCK = json.load(open(os.path.join(B, 'geometry_lock_A902_v2b.json'), encoding='utf-8'))
import csv
KV = {r['azonosito']: r for r in csv.DictReader(open(os.path.join(REPO, '01_alaprajzok', 'villamos_kiallasok', 'A902_villamos.csv'), encoding='utf-8'))}
ML04 = (float(KV['A902-ML04']['x_m']), float(KV['A902-ML04']['y_m'])); ML05 = (float(KV['A902-ML05']['x_m']), float(KV['A902-ML05']['y_m']))

PULT = [(8.45, 2.35, 9.05, 4.05), (9.95, 1.35, 10.55, 5.25), (9.05, 1.35, 9.95, 1.95), (8.45, 1.35, 8.95, 2.25)]   # terv szerinti konyhabútor
HUTO_ELO = box(9.35, 4.65, 9.95, 5.25)            # a hűtő (D13, y 5,20) ajtaja előtti 60 cm-es kezelősáv
TV_ZONA = box(3.67, 4.25, 4.07, 7.65)             # TV-fal bútorsáv a kanapé előtt: legfeljebb 40 cm mély (mint a V3 KI3-L/BN3-L); ez a változatok feltétele
KEPERNYO_X = 3.77; SZEM = 0.50
JARHATO = ['nappali_etkezo', 'konyha', 'eloter_atjaro', 'kozlekedo', 'eloter']
W = unary_union([box(*r) for k in JARHATO for r in LOCK['rooms'][k]]).difference(unary_union([box(*r) for r in PULT]))
CELOK = {'bejárat': box(7.30, 3.30, 8.35, 4.05),
         'terasz (tolóajtó, keleti rész)': box(6.69, 7.60, 8.94, 8.05),
         'konyha (a pultsorok közé)': box(9.05, 4.05, 9.95, 4.80),
         'hálók folyosója': box(3.70, 3.25, 5.00, 3.95),
         '05.3 háló ajtaja': box(10.00, 6.05, 10.75, 6.95)}
SZELESSEG = [round(0.50 + 0.05 * i, 2) for i in range(19)]
BUF = dict(join_style='round', quad_segs=8)

# ---------------------------------------------------------------- termékek (valós méret; forrás: V3 r1 / STYLE10-002 rekordok)
def lennon_L(XB, YS=5.21, YN=7.59, D=0.95, CH=1.80, CW=0.95):
    """Westwing Lennon jobbos L 238×180×68: háttámla kelet (XB) felé, a sarokrész a déli végen nyugat felé."""
    return unary_union([box(XB - D, YS + CW, XB, YN), box(XB - CH, YS, XB, YS + CW)])
def jattebo_U(X1, Y0=4.975, Y1=7.825, D=0.95, AR=1.60):
    """IKEA JÄTTEBO U 285×160×71: háttámla kelet (X1) felé, nyitott oldal nyugatra (a TV felé)."""
    return unary_union([box(X1 - D, Y0, X1, Y1), box(X1 - AR, Y0, X1 - D, Y0 + D), box(X1 - AR, Y1 - D, X1 - D, Y1)])
SZEK = {'S01': dict(nev='Kave Home Eamy', sz=0.55, mely=0.53), 'S02': dict(nev='Kave Home Ciselia', sz=0.525, mely=0.55)}
BETOL = 0.18     # a betolt szék ennyivel van az asztal alatt
ULO = 0.60       # ülő vendég: az asztal élétől ennyi a foglalt sáv

def szek_teglalap(cx, cy, nx, ny, sz, mely, tav):
    """Szék az asztal élétől 'tav' távolságra kezdődő mélység-sávban: (cx,cy) az élen lévő középpont, (nx,ny) kifelé mutató normális."""
    tx, ty = -ny, nx
    a = (cx + nx * tav, cy + ny * tav); b = (cx + nx * (tav + mely), cy + ny * (tav + mely))
    return Polygon([(a[0] - tx * sz / 2, a[1] - ty * sz / 2), (a[0] + tx * sz / 2, a[1] + ty * sz / 2),
                    (b[0] + tx * sz / 2, b[1] + ty * sz / 2), (b[0] - tx * sz / 2, b[1] - ty * sz / 2)])

def etkezo_teglalap(x0, y0, x1, y1, tengely, poz, sz, mely):
    """Téglalap/ovális asztal. tengely='y': a hosszoldalak kelet/nyugat felé (székek x irányban); 'x': észak/dél felé."""
    T = box(x0, y0, x1, y1); szekek = []
    for p in poz:
        if tengely == 'y':
            szekek += [(x0, p, -1, 0), (x1, p, 1, 0)]
        else:
            szekek += [(p, y1, 0, 1), (p, y0, 0, -1)]
    return T, szekek

def etkezo_kerek(cx, cy, r, szogek):
    T = Point(cx, cy).buffer(r, quad_segs=32); szekek = []
    for a in szogek:
        nx, ny = math.cos(math.radians(a)), math.sin(math.radians(a))
        szekek.append((cx + nx * r, cy + ny * r, nx, ny))
    return T, szekek

# ---------------------------------------------------------------- alternatívák
def valtozatok():
    """Végleges paraméterek: opt_alt2 / opt_b2 / opt_c2 / opt_c160 és xb_max.py (TV-sáv 40 cm) keresése alapján."""
    V = []
    for st in ('S01', 'S02'):
        s = SZEK[st]
        kan = (lambda xb: lennon_L(xb)) if st == 'S01' else (lambda xb: jattebo_U(xb))
        kan_nev = 'Westwing Lennon L 238×180 (jobbos)' if st == 'S01' else 'IKEA JÄTTEBO U 285×160'
        if st == 'S01':
            ref_asztal = (7.90, 5.27, 8.80, 7.27); ref_poz = (5.60, 6.27, 6.94); asztal_nev = 'Westwing Toni ovális 200×90'
        else:
            ref_asztal = (7.90, 5.37, 8.80, 7.17); ref_poz = (5.67, 6.27, 6.87); asztal_nev = 'Westwing Anouk 180×90'
        # R – mostani V3 / P902_24A (a termékek a 2,40 × 3,00-as U-befoglaló keleti élén)
        T, sz = etkezo_teglalap(*ref_asztal, 'y', ref_poz, s['sz'], s['mely'])
        V.append(dict(kod='R', stilus=st, cim='R – mostani (P902_24A, V3-tömb) – NEM ELFOGADHATÓ', XB=7.17, kanape=kan(7.17), kanape_nev=kan_nev,
                      asztal=T, asztal_nev=asztal_nev, szekek=sz, kerek=False))
        # A – hosszanti asztal 3+3, termékcsere nélkül; a kanapé nyugatabbra, az asztal 0,10 m-rel nyugatabbra a P902_24A-nál
        if st == 'S01':
            XB, cx, cy, Lh, d = 6.50, 8.25, 6.25, 2.00, 0.67
        else:
            XB, cx, cy, Lh, d = 6.40, 8.25, 6.30, 1.80, 0.60
        T, sz = etkezo_teglalap(cx - 0.45, cy - Lh / 2, cx + 0.45, cy + Lh / 2, 'y', (cy - d, cy, cy + d), s['sz'], s['mely'])
        V.append(dict(kod='A', stilus=st, cim='A – hosszanti asztal 3+3, termékcsere nélkül', XB=XB, kanape=kan(XB), kanape_nev=kan_nev,
                      asztal=T, asztal_nev=asztal_nev, szekek=sz, kerek=False))
        # B – keresztbe fordított asztal 3+3
        if st == 'S01':
            XB, cx, cy, Lh, nev = 6.50, 8.00, 6.25, 1.80, '180×90-es asztal (a Toni 200 helyett; termék kutatandó)'
        else:
            XB, cx, cy, Lh, nev = 6.35, 8.20, 6.25, 1.80, asztal_nev + ' (elforgatva)'
        T, sz = etkezo_teglalap(cx - Lh / 2, cy - 0.45, cx + Lh / 2, cy + 0.45, 'x', (cx - 0.60, cx, cx + 0.60), s['sz'], s['mely'])
        V.append(dict(kod='B', stilus=st, cim='B – keresztbe fordított asztal 3+3', XB=XB, kanape=kan(XB), kanape_nev=kan_nev,
                      asztal=T, asztal_nev=nev, szekek=sz, kerek=False))
        # C – hosszanti asztal 2+2+1+1, az ML04 alatt
        if st == 'S01':
            XB, cx, cy, Lh, nev = 6.60, 8.45, 6.30, 1.60, 'Westwing Toni ovális 160×90'
        else:
            XB, cx, cy, Lh, nev = 6.60, 8.45, 6.25, 1.80, asztal_nev
        y0, y1 = cy - Lh / 2, cy + Lh / 2; T = box(cx - 0.45, y0, cx + 0.45, y1)
        sz = [(cx - 0.45, cy + dd, -1, 0) for dd in (-0.10, 0.50)] + [(cx + 0.45, cy + dd, 1, 0) for dd in (-0.10, 0.50)] + [(cx, y0, 0, -1), (cx, y1, 0, 1)]
        V.append(dict(kod='C', stilus=st, cim='C – hosszanti asztal 2+2+1+1, az ML04 alatt', XB=XB, kanape=kan(XB), kanape_nev=kan_nev,
                      asztal=T, asztal_nev=nev, szekek=sz, kerek=False))
    return V

# ---------------------------------------------------------------- mérések
def szek_poligonok(v, mod):
    s = SZEK[v['stilus']]; out = []
    for (cx, cy, nx, ny) in v['szekek']:
        if mod == 'betolt': out.append(szek_teglalap(cx, cy, nx, ny, s['sz'], s['mely'], -BETOL))
        else: out.append(szek_teglalap(cx, cy, nx, ny, s['sz'], ULO - s['mely'], 0.0).union(szek_teglalap(cx, cy, nx, ny, s['sz'], s['mely'], ULO - s['mely'])))
    return out

def ut_szelesseg(akad):
    out = {n: None for n in CELOK if n != 'bejárat'}
    AK = unary_union(akad)
    for w in SZELESSEG:
        E = W.buffer(-w / 2, **BUF).difference(AK.buffer(w / 2, **BUF))
        parts = list(shapely.get_parts(E))
        be = [p for p in parts if p.intersects(CELOK['bejárat'])]
        if not be: break
        for n in out:
            if any(p.intersects(CELOK[n]) for p in be): out[n] = w
    return out

def kihuzas(v):
    """Székenként: az asztal élétől kifelé mennyi a szabad hely a széksávban (falig, pultig, kanapéig, TV-bútorig) – cél ≥ 0,90."""
    s = SZEK[v['stilus']]; akad = unary_union([v['kanape'], TV_ZONA] + [box(*r) for r in PULT])
    kulso = box(2.0, 0.0, 12.0, 9.5).difference(unary_union([box(*r) for k in ('nappali_etkezo', 'konyha', 'eloter_atjaro') for r in LOCK['rooms'][k]]))
    blok = akad.union(kulso); out = []
    for (cx, cy, nx, ny) in v['szekek']:
        tx, ty = -ny, nx
        el = LineString([(cx - tx * s['sz'] / 2, cy - ty * s['sz'] / 2), (cx + tx * s['sz'] / 2, cy + ty * s['sz'] / 2)])
        sav = szek_teglalap(cx, cy, nx, ny, s['sz'], 3.0, 0.0)
        X = sav.intersection(blok)
        out.append(round(el.distance(X), 3) if not X.is_empty else 3.0)
    return out

def meres(v):
    S, T = v['kanape'], v['asztal']
    betolt, ulo = szek_poligonok(v, 'betolt'), szek_poligonok(v, 'ulo')
    tv_tav = round(S.distance(TV_ZONA), 3)
    nezo = round((v['XB'] - SZEM) - KEPERNYO_X, 2)
    m = dict(kanape_TV_butor_m=tv_tav, nezotav_m=nezo, asztal_kanape_m=round(T.distance(S), 3),
             betolt_szek_kanape_m=round(unary_union(betolt).distance(S), 3), ulo_szek_kanape_m=round(unary_union(ulo).distance(S), 3),
             szekkihuzas_m=kihuzas(v), ML04_eltetes_m=round(T.centroid.distance(Point(*ML04)), 2),
             huto_elo_szabad_betolt=not unary_union(betolt).intersects(HUTO_ELO), huto_elo_szabad_ulo=not unary_union(ulo).intersects(HUTO_ELO),
             kanape_uveg_m=round(8.05 - S.bounds[3], 3), etkezo_huto_sarok_m=round(unary_union([T] + betolt).distance(box(9.95, 4.65, 10.55, 5.25)), 3))
    m['szekkihuzas_min_m'] = min(m['szekkihuzas_m'])
    m['ut_betolt_szekkel_m'] = ut_szelesseg([S, T, TV_ZONA] + betolt)
    m['ut_ulo_vendegekkel_m'] = ut_szelesseg([S, T, TV_ZONA] + ulo)
    return m, betolt, ulo

# ---------------------------------------------------------------- rajz
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'; FONTB = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
F = ImageFont.truetype(FONT, 15); FS = ImageFont.truetype(FONT, 13); FB = ImageFont.truetype(FONTB, 18); FT = ImageFont.truetype(FONTB, 26)
NEZET = (3.35, 2.15, 11.15, 8.45); PX = 92; FEJ = 150

def panel(v, m, betolt, ulo):
    x0, y0, x1, y1 = NEZET; Wp, Hp = int((x1 - x0) * PX), int((y1 - y0) * PX) + FEJ
    im = Image.new('RGB', (Wp, Hp), (255, 255, 255)); dr = ImageDraw.Draw(im, 'RGBA')
    T_ = lambda x, y: (round((x - x0) * PX), round(FEJ + (y1 - y) * PX))
    def poly(g, fill=None, outline=None, width=1):
        for p in shapely.get_parts(g):
            if p.is_empty or p.geom_type != 'Polygon': continue
            dr.polygon([T_(*c) for c in p.exterior.coords], fill=fill, outline=outline, width=width)
    poly(W, fill=(244, 244, 244, 255))
    # 0,90-es út (betolt székekkel) – a bejáratból elérhető szabad sáv
    AK = unary_union([v['kanape'], v['asztal'], TV_ZONA] + betolt)
    E = W.buffer(-0.45, **BUF).difference(AK.buffer(0.45, **BUF))
    for p in shapely.get_parts(E):
        if p.intersects(CELOK['bejárat']): poly(p.buffer(0.45, **BUF).intersection(W).difference(AK), fill=(150, 215, 150, 110))
    for r in PULT: poly(box(*r), fill=(214, 196, 150, 255), outline=(150, 120, 60, 255))
    poly(HUTO_ELO, outline=(150, 120, 60, 200))
    for n, wl in LOCK['walls'].items():
        if wl[2] > 0.5: continue
        if not (wl[3] > x0 and wl[0] < x1 and wl[4] > y0 and wl[1] < y1): continue
        col = (170, 170, 170, 255) if wl[5] < 1.0 else (60, 60, 60, 255)
        dr.rectangle([T_(wl[0], wl[4]), T_(wl[3], wl[1])], fill=col)
    for n, o in LOCK['openings'].items():
        if n.startswith('Uvegfal_nappali_terasz_uveg'): dr.rectangle([T_(o[0], o[4] + 0.03), T_(o[3], o[1] - 0.03)], fill=(120, 180, 230, 255))
    poly(CELOK['terasz (tolóajtó, keleti rész)'], outline=(30, 120, 200, 200))
    poly(TV_ZONA, fill=(128, 70, 15, 200))
    poly(v['kanape'], fill=(60, 110, 200, 200), outline=(30, 60, 140, 255), width=2)
    for g in ulo: poly(g, outline=(220, 120, 0, 150))
    for g in betolt: poly(g, fill=(240, 160, 60, 230), outline=(160, 80, 0, 255))
    poly(v['asztal'], fill=(200, 120, 30, 255), outline=(120, 60, 0, 255), width=2)
    for nev, p in (('ML04', ML04), ('ML05', ML05)):
        q = T_(*p); dr.ellipse([q[0] - 7, q[1] - 7, q[0] + 7, q[1] + 7], fill=(255, 210, 0, 255), outline=(0, 0, 0, 255)); dr.text((q[0] + 9, q[1] - 8), nev, fill=(0, 0, 0), font=FS)
    # méretvonalak
    def meretvonal(a, b, szoveg, szin=(200, 20, 20)):
        pa, pb = T_(*a), T_(*b); dr.line([pa, pb], fill=szin + (255,), width=3)
        for p in (pa, pb): dr.ellipse([p[0] - 3, p[1] - 3, p[0] + 3, p[1] + 3], fill=szin + (255,))
        mx, my = (pa[0] + pb[0]) / 2, (pa[1] + pb[1]) / 2
        tb = dr.textbbox((0, 0), szoveg, font=FB); w_, h_ = tb[2] - tb[0], tb[3] - tb[1]
        dr.rectangle([mx - w_ / 2 - 3, my - h_ / 2 - 4, mx + w_ / 2 + 3, my + h_ / 2 + 4], fill=(255, 255, 255, 235))
        dr.text((mx - w_ / 2, my - h_ / 2 - 3), szoveg, fill=szin, font=FB)
    from shapely.ops import nearest_points
    BS = unary_union(betolt)
    a, b = nearest_points(v['kanape'], BS); meretvonal((a.x, a.y), (b.x, b.y), f"{a.distance(b):.2f}".replace('.', ','))
    a, b = nearest_points(v['kanape'], TV_ZONA); meretvonal((a.x, a.y), (b.x, b.y), f"{a.distance(b):.2f}".replace('.', ','), (110, 60, 10))
    a, b = nearest_points(unary_union([v['asztal']] + betolt), box(9.95, 4.65, 10.55, 5.25)); meretvonal((a.x, a.y), (b.x, b.y), f"{a.distance(b):.2f}".replace('.', ','), (120, 40, 160))
    # fejléc
    dr.rectangle([0, 0, Wp, FEJ], fill=(255, 255, 255, 255))
    u1, u2 = m['ut_betolt_szekkel_m'], m['ut_ulo_vendegekkel_m']
    f = lambda x: '–' if x is None else f"{x:.2f}".replace('.', ',')
    hiba = []
    for n, w in u1.items():
        if (w or 0) < 0.90 - 1e-6: hiba.append(f"{n.split(' (')[0]} {f(w)}")
    if m['szekkihuzas_min_m'] < 0.90 - 1e-6: hiba.append(f"székkihúzás {f(m['szekkihuzas_min_m'])}")
    if m['kanape_TV_butor_m'] < 0.60 - 1e-6: hiba.append(f"kanapé–TV {f(m['kanape_TV_butor_m'])}")
    m['kotelezo_teljesul'] = not hiba
    dr.text((10, 6), f"{v['stilus']} · {v['cim']}", fill=(0, 0, 0), font=FB)
    dr.text((10, 31), 'Kötelező méretek: MIND TELJESÜL' if not hiba else 'NEM TELJESÜL: ' + ', '.join(hiba), fill=(20, 120, 40) if not hiba else (200, 30, 30), font=FB)
    dr.text((10, 56), f"szék–kanapé {f(m['betolt_szek_kanape_m'])} m · székkihúzás ≥ {f(m['szekkihuzas_min_m'])} m · kanapé–TV {f(m['kanape_TV_butor_m'])} m · nézőtáv {f(m['nezotav_m'])} m", fill=(30, 30, 30), font=F)
    dr.text((10, 77), f"utak betolt székkel: terasz {f(u1['terasz (tolóajtó, keleti rész)'])} · konyha {f(u1['konyha (a pultsorok közé)'])} · folyosó {f(u1['hálók folyosója'])} · 05.3 {f(u1['05.3 háló ajtaja'])}", fill=(30, 30, 30), font=F)
    dr.text((10, 98), f"ülő vendégekkel: terasz {f(u2['terasz (tolóajtó, keleti rész)'])} · konyha {f(u2['konyha (a pultsorok közé)'])} · folyosó {f(u2['hálók folyosója'])} · 05.3 {f(u2['05.3 háló ajtaja'])}", fill=(30, 30, 30), font=F)
    dr.text((10, 119), f"ML04 lámpa {f(m['ML04_eltetes_m'])} m-re az asztal közepétől · {v['asztal_nev']} · 6 × {SZEK[v['stilus']]['nev']}", fill=(90, 90, 90), font=FS)
    return im

if __name__ == '__main__':
    eredmeny = []; panelek = {}
    for v in valtozatok():
        m, betolt, ulo = meres(v)
        eredmeny.append(dict(kod=v['kod'], stilus=v['stilus'], cim=v['cim'], kanape=v['kanape_nev'], kanape_hat_x=v['XB'], kanape_befoglalo=[round(t, 3) for t in v['kanape'].bounds],
                             asztal=v['asztal_nev'], asztal_befoglalo=[round(t, 3) for t in v['asztal'].bounds], **m))
        panelek[(v['stilus'], v['kod'])] = panel(v, m, betolt, ulo)
        print(v['stilus'], v['kod'], json.dumps({k: m[k] for k in ('betolt_szek_kanape_m', 'ulo_szek_kanape_m', 'szekkihuzas_min_m', 'kanape_TV_butor_m', 'nezotav_m', 'ML04_eltetes_m', 'huto_elo_szabad_betolt', 'huto_elo_szabad_ulo')}, ensure_ascii=False),
              m['ut_betolt_szekkel_m'], m['ut_ulo_vendegekkel_m'], flush=True)
    kod = ['R', 'A', 'B', 'C']; p0 = panelek[('S01', 'R')]; w, h = p0.size
    lap = Image.new('RGB', (w * 4 + 50, h * 2 + 150), (255, 255, 255)); d = ImageDraw.Draw(lap)
    d.text((20, 14), 'A-902 nappali–étkező – elrendezési alternatívák (MÉRETPRÓBA, nem stílusterv) · 2026-10-25', fill=(0, 0, 0), font=FT)
    d.text((20, 52), 'Terv szerinti geometria (lock v2b), helyszínen nem mért. Kék: kanapé · barna: TV-bútorsáv 40 cm · narancs: asztal és betolt székek (vékony körvonal: ülő vendég, 60 cm) · bézs: konyhapult a terv szerint · zöld: a bejáratból 0,90 m-es úttal bejárható tér.', fill=(60, 60, 60), font=F)
    d.text((20, 76), 'Piros: kanapé – legközelebbi betolt szék. Barna: kanapé – TV-bútor (a TV-bútor a kanapé előtt legfeljebb 40 cm mély). Lila: étkező – hűtőoszlop sarka (a 05.3 háló felé vezető út szűkülete). Terasz-cél: a tolóajtó keleti része (Péter 2026-10-24 18:43; hétfőn ellenőrizendő). Székkihúzás: az asztal élétől a széksávban mért szabad hely (cél ≥ 0,90 m).', fill=(60, 60, 60), font=F)
    for i, st in enumerate(('S01', 'S02')):
        for j, k in enumerate(kod):
            lap.paste(panelek[(st, k)], (20 + j * (w + 3), 110 + i * (h + 20)))
    out = os.path.join(HERE, 'elrendezes_alt_A902_v1.png'); lap.save(out, optimize=True)
    json.dump(dict(datum='2026-10-25', statusz='MÉRETPRÓBA – nem stílusterv, nem kivitelezési terv; geometry_lock_A902_v2b (terv szerinti), helyszínen nem mért',
                   szabalyok=dict(fo_ut_m=0.90, mellekut_m=0.75, szekkihuzas_m=0.90, kanape_tv_min_m=0.60, nezotav_m=[2.0, 3.4], ulo_vendeg_sav_m=ULO, betolt_szek_m=BETOL),
                   celok={k: list(g.bounds) for k, g in CELOK.items()}, pult=PULT, tv_zona=list(TV_ZONA.bounds), eredmeny=eredmeny),
              open(os.path.join(HERE, 'elrendezes_alt_A902_v1.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('kész', out)
