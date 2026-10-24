#!/usr/bin/env python3
"""WSG – villamos kiállások kinyerése a méretezett alaprajzokból (vektoros PDF), v2.

Forrás: WGR1_meretezett_alaprajzok.pdf (Péter összeállítása, 2026.10.20.; a fejlesztő
M1/KORR rajzi mellékletei). Vevői adat, ezért NINCS a repóban. Futtatás:
    python3 villamos_kinyeres.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf
Kimenet a szülőmappába: <LAKÁS>_villamos.json/.csv, <LAKÁS>_hutes_futes_zonak.csv,
<LAKÁS>_villamos_atfedes.png. Csak olvas; Blender-fájlhoz nem nyúl.
"""
import sys, os, math, json, csv, re, collections, hashlib
import pymupdf
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
PDF = sys.argv[1] if len(sys.argv) > 1 else os.environ.get('WSG_PDF')
if not PDF or not os.path.exists(PDF):
    sys.exit('Add meg a WGR1_meretezett_alaprajzok.pdf helyi útvonalát.')

R = lambda *a: list(a)
FLATS = {
 'A902': dict(page=18, scale=50, X0=157.3, Y0=626.4, dosszie=176,
   verzio='M1 KORR 2 (rajz 2025.12.15., kiküldve 2025.12.18.; tartalmazza a 2025.10.13-i KORR-t)',
   origo='x=0: 05.1 szoba homlokzati (rajzon bal) belső falsíkja; y=0: 05.2 szoba rajzon alsó belső falsíkja. Azonos a Blender-modell (WSG_A902_*) koordinátáival.',
   rooms=[('05.2 SZOBA', R(0, 0, 3.65, 2.65)), ('05.2 SZOBA (gardróbfülke)', R(0, 2.65, 2.42, 3.35)),
          ('05.1 SZOBA', R(0, 3.45, 2.42, 3.95)), ('05.1 SZOBA', R(0, 3.95, 3.57, 8.05)), ('05.1 SZOBA (északi fülke)', R(0, 8.05, 3.02, 8.95)),
          ('07 KÖZLEKEDŐ', R(2.52, 2.75, 5.00, 3.95)), ('07 KÖZLEKEDŐ', R(5.00, 2.75, 5.20, 2.95)), ('07 KÖZLEKEDŐ', R(5.00, 3.45, 5.20, 3.95)),
          ('04 NAPPALI', R(3.67, 4.05, 8.00, 8.05)), ('04 NAPPALI', R(3.67, 3.95, 5.20, 4.05)),
          ('03 ÉTKEZŐ', R(8.00, 4.05, 10.55, 5.05)), ('03 ÉTKEZŐ', R(8.00, 5.05, 10.75, 7.025)), ('03 ÉTKEZŐ', R(8.00, 7.025, 9.80, 8.05)),
          ('02 KONYHA', R(9.05, 1.35, 10.55, 2.35)), ('02 KONYHA', R(8.45, 2.35, 10.55, 4.05)),
          ('01 ELŐTÉR', R(5.60, 0.00, 6.70, 2.00)), ('01 ELŐTÉR', R(6.70, 0.85, 8.35, 2.00)), ('01 ELŐTÉR', R(8.35, 1.35, 8.95, 2.25)), ('01 ELŐTÉR', R(7.30, 2.00, 8.35, 4.05)),
          ('08 WC', R(5.60, 2.10, 6.60, 2.75)), ('08 WC', R(5.30, 2.75, 6.60, 3.25)), ('08 WC', R(5.30, 3.25, 6.45, 3.95)),
          ('06.1 FÜRDŐ', R(3.75, 0, 5.50, 2.65)),
          ('05.3 SZOBA', R(10.85, 4.10, 14.375, 7.025)), ('05.3 SZOBA', R(11.10, 7.025, 14.375, 8.05)), ('05.3 SZOBA', R(14.375, 4.10, 15.00, 5.10)),
          ('06.2 FÜRDŐ', R(14.475, 5.20, 16.40, 8.05)),
          ('13 ERKÉLY', R(-2.01, -0.20, -0.30, 5.69)), ('13 ERKÉLY', R(-1.12, 5.69, -0.30, 7.90)),
          ('09 TERASZ', R(3.02, 8.35, 10.34, 19.8)), ('10 TERASZ', R(10.34, 8.35, 16.72, 19.8))],
   specials=[('kaputelefon_belteri', 6.93, 1.00, '', 'videós kaputelefon beltéri egység (a fali × a bekötési pont)'),
             ('kezelo_billentyuzet', 7.15, 1.39, '', 'billentyűzetes kezelő a bejárati „a” kapcsoló fölött – valószínűleg riasztó-kezelő (jelmagyarázat nélkül NEM IGAZOLT)'),
             ('bejarati_ajto_eszkoz', 7.41, 0.70, '', 'a bejárati ajtótokon – elektromos zár vagy nyitásérzékelő (NEM IGAZOLT)'),
             ('EPH_csatlakozo', 4.12, 0.59, '', 'kád melletti kör (×|||) – valószínűleg EPH egyenpotenciál-csatlakozás (NEM IGAZOLT)'),
             ('jakuzzi_aramkiallas', 3.77, 9.29, '', 'kültéri jakuzzi-áramkiállás; fali bekötési pont x≈3,50 (a rajzi × helye)')]),
 'A811': dict(page=5, scale=50, X0=434.02, Y0=748.0, dosszie=150,
   verzio='M1 (érvényes; KORR-alaprajz nem készült)',
   origo='x=0: 04 nappali homlokzati (erkélyajtós, rajzon bal) belső falsíkja; y=0: 05.1 szoba rajzon alsó belső falsíkja. Helyi rendszer (Blender-modell még nincs).',
   kulso=[R(8.45, 6.20, 9.50, 7.60)],   # a bejárati ajtó lépcsőházi oldala (csengő, csengőnyomó doboza)
   rooms=[('05.1 SZOBA', R(-0.70, 0, 4.43, 2.69)), ('05.1 SZOBA', R(4.43, 1.60, 5.00, 2.69)),
          ('05.2-3 SZOBA', R(0, 2.81, 5.02, 3.85)), ('05.2-3 SZOBA', R(0, 3.85, 3.23, 6.56)), ('05.2-3 SZOBA (gardrób)', R(3.32, 3.85, 5.02, 6.56)),
          ('03-04 ÉTKEZŐ-NAPPALI', R(0, 6.65, 5.02, 7.85)), ('03-04 ÉTKEZŐ-NAPPALI', R(0, 7.85, 6.10, 11.54)), ('02 KONYHA', R(6.10, 8.54, 8.24, 11.54)),
          ('01 ELŐTÉR', R(6.17, 6.85, 8.24, 8.45)), ('07 KÖZLEKEDŐ', R(5.12, 1.49, 6.17, 7.85)),
          ('08 WC', R(7.31, 4.85, 8.24, 6.75)), ('06.2 FÜRDŐ', R(6.26, 2.43, 8.24, 4.76)), ('06.1 FÜRDŐ', R(6.26, 0, 8.24, 2.33)),
          ('09 HTH', R(4.52, 0, 6.17, 1.49)), ('10 ERKÉLY', R(-2.45, 0.40, -0.25, 11.30))],
   specials=[('kaputelefon_belteri', 5.95, 6.38, '', 'videós kaputelefon beltéri egység; fali bekötési pont (rajzi ×) x≈6,17, y≈6,40'),
             ('csengo_kulso', 8.61, 6.60, '', 'a bejárati ajtó külső oldalán (lépcsőház) – nem a lakásban'),
             ('kezelo_billentyuzet', 7.31, 7.50, '', 'billentyűzetes kezelő az „a” kapcsoló fölött – valószínűleg riasztó-kezelő (NEM IGAZOLT)'),
             ('bejarati_ajto_eszkoz', 8.40, 6.86, '', 'a bejárati ajtótokon – elektromos zár vagy nyitásérzékelő (NEM IGAZOLT)'),
             ('EPH_csatlakozo', 7.47, 0.37, '', 'kád melletti kör (×|||) – valószínűleg EPH (NEM IGAZOLT)')]),
 'A812': dict(page=12, scale=100, X0=539.36, Y0=600.95, dosszie=179,
   verzio='M1 KORR (2026.04.28.) – átnézeti lap 1:100, a teljes lakás (az 1:50-es 11. oldal csak részlet)',
   origo='x=0: 04 nappali homlokzati (erkélyajtós, rajzon bal) belső falsíkja; y=0: 04 nappali rajzon alsó belső falsíkja. Helyi rendszer (Blender-modell még nincs).',
   kulso=[R(8.45, 2.30, 9.50, 3.70)],   # a bejárati ajtó lépcsőházi oldala (csengő, csengőnyomó doboza)
   rooms=[('03-04 ÉTKEZŐ-NAPPALI', R(0, 0, 3.20, 5.60)), ('03-04 ÉTKEZŐ-NAPPALI', R(3.20, 0, 5.85, 4.70)),
          ('02 KONYHA', R(5.85, 0, 8.25, 2.85)), ('01 ELŐTÉR', R(5.85, 2.85, 8.35, 4.75)),
          ('07 KÖZLEKEDŐ', R(6.08, 4.75, 7.22, 12.74)), ('07 KÖZLEKEDŐ (gardrób rész)', R(7.31, 4.75, 8.72, 6.41)),
          ('05.1 SZOBA', R(3.15, 4.79, 6.08, 7.88)), ('05.2 SZOBA', R(3.15, 8.00, 6.08, 11.24)),
          ('10.2 GARDRÓB', R(3.15, 11.33, 5.48, 12.62)), ('05.3 SZOBA', R(3.15, 12.74, 6.30, 16.95)),
          ('10.3 GARDRÓB', R(6.30, 12.74, 8.72, 14.36)), ('06.2 FÜRDŐ', R(6.40, 14.45, 8.72, 16.95)),
          ('06.1 FÜRDŐ (HTH)', R(7.31, 9.80, 8.72, 12.62)), ('08/09 FÜRDŐ', R(7.31, 6.41, 8.72, 9.71)),
          ('11 ERKÉLY', R(-2.45, -0.35, -0.25, 6.40))],
   specials=[('kaputelefon_belteri', 7.35, 3.14, '', 'videós kaputelefon beltéri egység (a billentyűzetes kezelőtől balra)'),
             ('csengo_kulso', 8.61, 2.80, '', 'a bejárati ajtó külső oldalán (lépcsőház) – nem a lakásban'),
             ('kezelo_billentyuzet', 7.54, 3.45, '', 'billentyűzetes kezelő – valószínűleg riasztó-kezelő (NEM IGAZOLT)'),
             ('bejarati_ajto_eszkoz', 8.40, 3.06, '', 'a bejárati ajtótokon – elektromos zár vagy nyitásérzékelő (NEM IGAZOLT)')]),
}
# A rajzlapok „Elektromos módosítás (erős és gyengeáram)” és „Pincei tárolóval, gk.beállóval kapcsolatos módosítás”
# blokkja, tömörítve (a szöveg a rajzlapról; a hely a fenti kinyerésből). Tervezéshez fontos, mert megmondja, mire
# készült egy-egy kiállás (pl. szekrényvilágítás), és mi van a lakáson kívül (tároló, beálló).
MODOSITAS = {
 'A902': dict(forras='19. o. (átnézeti M1 KORR 2, dosszié 177) és 20. o. (parkoló, tároló, dosszié 170)', tetelek=[
   ('01 ELŐTÉR / 02 KONYHA', 'Az előtér és a konyha közötti pengefal megszűnik, a konyhai kapcsolóblokk követi a változást.'),
   ('02 KONYHA', 'Sütő m=1,10 m, mikró m=1,30 m (magasszekrény a folyosó felé eső falon). A mosogató feletti falikar-kiállás és a mosogatógép-dugalj követi az új helyet. A pultdugaljak helye megváltozik; +1 pultdugalj a meglévővel egy szerelvényben.'),
   ('02 KONYHA', 'KORR 2 (2025.12.15.): a „d” kapcsoló változik.'),
   ('03 ÉTKEZŐ', 'A „b” mennyezeti lámpakiállás eltolva.'),
   ('04 NAPPALI', '+1 falikar-kiállás a 05.1 szoba felé eső válaszfalon, m=2,85 m. Az „n,p” mennyezeti lámpakiállás eltolva.'),
   ('05.1 SZOBA', 'A válaszfal a szoba felé tolódik. Az ágy két oldalán 1-1 dugalj + 1-1 váltókapcsoló egy szerelvényben, m=65 cm. **+1 dugalj szekrényvilágításhoz.**'),
   ('05.2 SZOBA', '+1 dugalj a TV-blokk részeként.'),
   ('05.3 SZOBA', 'Az ágy két oldalán 1-1 dugalj + 1-1 váltókapcsoló egy szerelvényben, m=65 cm. **+2 dugalj szekrényvilágításhoz.**'),
   ('06.2 FÜRDŐ', 'A törölközőszárító (TSZ) a szoba felé eső válaszfalra kerül, a kiállása követi.')],
   lakason_kivul=['AT8-01 szinti tároló: 2 dugalj.', 'P-0-65 beálló: autótöltő.', 'T-0-26 tároló és P-0-64 beálló: nincs módosítás.']),
 'A811': dict(forras='5. o. (alaprajz M1, dosszié 150) és 6. o. (parkoló, tároló, dosszié 151)', tetelek=[
   ('02 KONYHA', 'A konyhatechnológia sorrendje megváltozik, az elektromos kiállások követik. +1 pultdugalj. Mikró m=1,30 m.'),
   ('03 ÉTKEZŐ', '+1 „g” váltókapcsoló (a váltópárja a nappaliban). A „g” mennyezeti lámpakiállás helye módosul.'),
   ('04 NAPPALI', '+1 oldalfali kiállás m=2,65 m. A konyhai pengefal megszűnése miatt a kapcsolók („g” és „c,d”), a termosztát és a **mozgásérzékelő** a nappali válaszfalának sarkára kerül.'),
   ('05.1 SZOBA', 'Az ágy két oldalán 1-1 többlet dugalj a meglévők mellé, m=65 cm. TV-blokk m=1,20 m. +2 dugalj.'),
   ('05.2-3 SZOBA', 'A két szoba összevonva. Az ágy két oldalán 1-1 többlet „m” váltókapcsoló a dugaljak mellé, m=65 cm. +2 mennyezeti lámpakiállás („m” és „l”); az „m” 3 helyről kapcsolható. A **biztonsági központ** áthelyezésre kerül.'),
   ('06.1 FÜRDŐ', 'A mosdó és a WC helycseréjét az elektromos kiállások követik; az elszívó ventilátor az ajtó mögül a mosdó fölé kerül.'),
   ('06.2 FÜRDŐ', 'Az elrendezés módosul, az elektromos kiállások követik.'),
   ('07 KÖZLEKEDŐ', 'A „h” mennyezeti lámpakiállás 3 helyről kapcsolható.'),
   ('09 HTH', '+1 dugalj a szárítógépnek a mosógép-dugalj fölött; +1 dugalj a kapcsoló alatt.')],
   lakason_kivul=['AT8-03 szinti tároló: 2 dugalj.', 'P-0-33 beálló: autótöltő.', 'T-0-06 tároló és P-0-34 beálló: nincs módosítás.']),
 'A812': dict(forras='11. o. (alaprajz M1 KORR 2026.04.28., dosszié 178) és 13. o. (parkoló, tároló, dosszié 160)', tetelek=[
   ('02 KONYHA', '+2 pultdugalj.'),
   ('05.2 SZOBA', 'Az ágy két oldalán 1-1 többlet dugalj a meglévők mellé, m=65 cm. TV-blokk m=1,20 m.'),
   ('05.3 SZOBA', 'Az ágy melletti dugaljak m=65 cm-re kerülnek; +2 dugalj m=65 cm.'),
   ('06.1 HTH', '+1 dugalj a szárítógépnek a mosógép-dugalj fölött.'),
   ('08/09 FÜRDŐ', 'A WC és a HTH fürdővé vonva össze. Az „m” és „l” lámpák egy csillárkapcsolóra kerülnek. Az elszívó ventilátor páraérzékelős típus lesz.'),
   ('07 KÖZLEKEDŐ', 'KORREKCIÓ 2026.04.28.: a közlekedői gardróbrészben nem kell gipszkarton álmennyezet.')],
   lakason_kivul=['AT8-02 szinti tároló: 2 dugalj.', 'P-0-32 beálló: autótöltő.', 'T-0-03 tároló és P-0-31 beálló: nincs módosítás.']),
}
ALMENNYEZET = ('Péter átvételi összesítője szerint gipszkarton álmennyezet csak az előtérben, a WC-ben és a fürdőben van, min. 2,40 m. '
               'A rajzon zöld „gk. álm.” felirat jelöli (imp. = impregnált, nor. = normál); a pontos kiterjedés helyszínen ellenőrizendő.')

RE_CIRCUIT = re.compile(r'^[a-z](\s*,\s*[a-z])*$')
RE_HEIGHT = re.compile(r'm\s*[=:]\s*([\d]+(?:[.,]\d+)?)\s*(cm|m)\b')
DEVICE_CODES = {'P', 'H', 'MG', 'Mi', 'S', 'S/F', 'EL', 'M', 'SZ', 'TSZ', 'B', 'K'}
KOD_JELENTES = {'P': 'pultdugalj', 'H': 'hűtő', 'MG': 'mosogatógép', 'Mi': 'mikró', 'S': 'sütő', 'EL': 'elszívó',
                'M': 'mosógép', 'SZ': 'szárítógép', 'TSZ': 'törölközőszárító', 'B': 'fürdőszobai (tükör melletti) dugalj – „B” jelentése nem igazolt', 'K': '?'}
TIPUS = [  # (belső kulcs, előtag, kimeneti típus, magyar leírás)
    ('LAMPA', 'ML', 'mennyezeti_lampakiallas', 'mennyezeti lámpakiállás (⊗)'),
    ('LAMPA_FAL', 'FL', 'fali_lampakiallas', 'lámpakiállás falon (⊗ dobozzal)'),
    ('FALI_LAMPA', 'FL', 'fali_lampakiallas', 'fali lámpakiállás (félkör ⊗ a falon)'),
    ('KAPCSOLO', 'K', 'kapcsolo', 'kapcsoló'),
    ('DUGALJ', 'D', 'dugalj', 'dugalj'),
    ('FIX', 'X', 'fix_bekotes', 'fix bekötés'),
    ('VENT', 'V', 'ventilator_kiallas', 'elszívó ventilátor (M körben)'),
    ('GYENGE', 'G', 'gyengearamu_aljzat', 'gyengeáramú aljzat (TV-blokk)'),
    ('ANTENNA', 'G', 'antenna_tv_aljzat', 'TV/antenna aljzat'),
    ('BK', 'G', 'BK_doboz', 'BK jelű doboz'),
    ('KUPOLA', 'S', 'hangjelzo_vagy_erzekelo', 'kupola hullámokkal'),
    ('R', 'R', 'R_jelu_kiallas', 'R jelű kör ablaknál'),
    ('TERMOSZTAT', 'T', 'termosztat', 'termosztát (kék T)'),
    ('ELOSZTO', 'E', 'lakaselosztó', 'lakáselosztó (EL4)'),
    ('SPEC', 'S', '', ''),
    ('DOBOZ', 'Z', 'doboz_jel_nelkul', 'doboz jel nélkül'),
]
TMAP = {t[0]: t for t in TIPUS}

def isred(c): return c is not None and c[0] > 0.9 and c[1] < 0.2 and c[2] < 0.2
def isblue(c): return c is not None and c[2] > 0.9 and c[0] < 0.5 and c[1] < 0.5
def rgb_int(c): return ((c >> 16) & 255, (c >> 8) & 255, c & 255)

def load(page):
    paths = []
    for x in page.get_drawings():
        items = []
        for it in x['items']:
            t = it[0]
            if t == 'l': items.append(('l', (it[1].x, it[1].y), (it[2].x, it[2].y)))
            elif t == 'c': items.append(('c', (it[1].x, it[1].y), (it[2].x, it[2].y), (it[3].x, it[3].y), (it[4].x, it[4].y)))
            elif t == 're':
                r = it[1]; items.append(('re', (r.x0, r.y0), (r.x1, r.y1)))
        r = x['rect']
        paths.append(dict(bbox=(r.x0, r.y0, r.x1, r.y1), items=items, col=x.get('color'), fill=x.get('fill'), w=round(x.get('width') or 0, 2)))
    spans = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            for s in l['spans']:
                t = s['text'].strip()
                if t:
                    bb = s['bbox']
                    spans.append(dict(text=t, rgb=rgb_int(s['color']), size=s['size'], bbox=bb, c=((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2)))
    return paths, spans

def clusters(idx, paths, tol):
    parent = {i: i for i in idx}
    def f(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    order = sorted(idx, key=lambda i: paths[i]['bbox'][0])
    for a, i in enumerate(order):
        x0, y0, x1, y1 = paths[i]['bbox']
        for j in order[a + 1:]:
            X0, Y0, X1, Y1 = paths[j]['bbox']
            if X0 > x1 + tol: break
            if Y0 <= y1 + tol and Y1 >= y0 - tol:
                parent[f(i)] = f(j)
    g = collections.defaultdict(list)
    for i in idx: g[f(i)].append(i)
    out = []
    for m in g.values():
        bb = [paths[i]['bbox'] for i in m]
        out.append(dict(idx=m, bbox=(min(b[0] for b in bb), min(b[1] for b in bb), max(b[2] for b in bb), max(b[3] for b in bb)),
                        cnt=collections.Counter(it[0] for i in m for it in paths[i]['items'])))
    return out

def seg_d(p, a, b):
    ax, ay = a; bx, by = b; px, py = p
    dx, dy = bx - ax, by - ay; L2 = dx * dx + dy * dy
    t = 0 if L2 == 0 else max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L2))
    return math.hypot(px - ax - t * dx, py - ay - t * dy)

def main():
    doc = pymupdf.open(PDF)
    sha = hashlib.sha256(open(PDF, 'rb').read()).hexdigest()
    F = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 15)
    FS = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 13)
    summary = {}
    for flat, P in FLATS.items():
        page = doc[P['page'] - 1]
        k = 50.0 / P['scale']; M = 72 / 25.4 * 1000 / P['scale']; X0, Y0 = P['X0'], P['Y0']
        tm = lambda pt: (round((pt[0] - X0) / M, 3), round((Y0 - pt[1]) / M, 3))
        tp = lambda xm, ym: (X0 + xm * M, Y0 - ym * M)
        paths, spans = load(page)
        red_idx = [i for i, p in enumerate(paths) if isred(p['col']) or isred(p['fill'])]
        reds = [s for s in spans if s['rgb'][0] > 200 and s['rgb'][1] < 60 and s['rgb'][2] < 60]
        blues = [s for s in spans if s['rgb'][2] > 200 and s['rgb'][0] < 120]
        def room_of(pt_m, tol=0.0):
            x, y = pt_m
            for name, (a, b, c, d) in P['rooms']:
                if a - tol <= x <= c + tol and b - tol <= y <= d + tol: return name
            return None
        def room_near(pt_m, maxd=0.6):
            r = room_of(pt_m)
            if r: return r, 0.0
            best = None
            for name, (a, b, c, d) in P['rooms']:
                dx = max(a - pt_m[0], 0, pt_m[0] - c); dy = max(b - pt_m[1], 0, pt_m[1] - d)
                dd = math.hypot(dx, dy)
                if best is None or dd < best[1]: best = (name, dd)
            return (best if best and best[1] <= maxd else (None, best[1] if best else 99))
        # --- primitívek
        circles, arcs, rlines = [], [], []
        for i in red_idx:
            p = paths[i]; cs = [it for it in p['items'] if it[0] == 'c']; b = p['bbox']; w = b[2] - b[0]; h = b[3] - b[1]
            if len(cs) >= 4 and abs(w - h) < 0.3 * k + 0.05:
                circles.append(dict(c=((b[0] + b[2]) / 2, (b[1] + b[3]) / 2), r=w / 2, pi=i))
            elif len(cs) == 2:
                p0 = cs[0][1]; pm = cs[0][4]; p1 = cs[1][4]
                arcs.append(dict(c=((p0[0] + p1[0]) / 2, (p0[1] + p1[1]) / 2), apex=pm, r=math.dist(p0, p1) / 2, pi=i))
            for it in p['items']:
                if it[0] == 'l': rlines.append((it[1], it[2]))
        # dobozok
        V, H = set(), set()
        for a, b in rlines:
            if abs(a[0] - b[0]) < 0.05 and abs(a[1] - b[1]) > 0.2: V.add((round(a[0], 2), round(min(a[1], b[1]), 1), round(max(a[1], b[1]), 1)))
            elif abs(a[1] - b[1]) < 0.05 and abs(a[0] - b[0]) > 0.2: H.add((round(a[1], 2), round(min(a[0], b[0]), 1), round(max(a[0], b[0]), 1)))
        boxes = []
        for S_, o in ((V, 'V'), (H, 'H')):
            by = collections.defaultdict(list)
            for c, a0, a1 in S_: by[(a0, a1)].append(c)
            for (a0, a1), cs in by.items():
                cs = sorted(set(cs))
                for i in range(len(cs)):
                    for j in range(i + 1, len(cs)):
                        t = cs[j] - cs[i]
                        if 0.6 * k <= t <= 1.7 * k and 3.4 * k <= a1 - a0 <= 6.5 * k:
                            bb = (cs[i], a0, cs[j], a1) if o == 'V' else (a0, cs[i], a1, cs[j])
                            c = ((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2)
                            if not any(math.dist(c, q['c']) < 0.8 * k for q in boxes):
                                boxes.append(dict(o=o, bbox=bb, c=c))
        def has_x(c, r):
            n = 0
            for a, b in rlines:
                if math.dist(a, c) <= r + 0.3 and math.dist(b, c) <= r + 0.3:
                    dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy)
                    if L > 0.5 * r and abs(abs(dx) - abs(dy)) < 0.35 * L: n += 1
            return n
        syms = []
        used_paths = set()
        for c in circles:
            r = c['r'] / k
            if 4.85 < r < 5.35: syms.append(dict(t='LAMPA', c=c['c'], x=has_x(c['c'], c['r']))); used_paths.add(c['pi'])
            elif 5.45 < r < 5.95: syms.append(dict(t='R', c=c['c'])); used_paths.add(c['pi'])
            elif 1.85 < r < 2.35: syms.append(dict(t='KAPCSOLO', c=c['c'])); used_paths.add(c['pi'])
        for a in arcs:
            r = a['r'] / k
            if 3.9 < r < 4.6: syms.append(dict(t='DUGALJ', c=a['c'], apex=a['apex'])); used_paths.add(a['pi'])
            elif 4.85 < r < 5.4: syms.append(dict(t='FALI_LAMPA', c=a['c'], apex=a['apex'])); used_paths.add(a['pi'])
        # --- doboz-párosítás: globális mohó, típusonkénti távolsággal
        maxd = {'FALI_LAMPA': 5 * k, 'DUGALJ': 7.5 * k, 'LAMPA': 7.5 * k, 'KAPCSOLO': 14 * k}
        pairs = []
        for si, s in enumerate(syms):
            if s['t'] not in maxd: continue
            ref = s.get('apex', s['c']) if s['t'] == 'DUGALJ' else s['c']
            for bi, b in enumerate(boxes):
                d = math.dist(ref, b['c'])
                if d <= maxd[s['t']]: pairs.append((d, si, bi))
        sused, bused = set(), set()
        for d, si, bi in sorted(pairs):
            if si in sused or bi in bused: continue
            syms[si]['box'] = bi; sused.add(si); bused.add(bi)
        for s in syms:
            if s['t'] == 'LAMPA' and 'box' in s: s['t'] = 'LAMPA_FAL'
            if s['t'] in ('KAPCSOLO', 'DUGALJ') and 'box' not in s:
                ref = s.get('apex', s['c']) if s['t'] == 'DUGALJ' else s['c']
                c = [(math.dist(ref, b['c']), bi) for bi, b in enumerate(boxes)]
                c = [x for x in c if x[0] <= (40 * k if s['t'] == 'KAPCSOLO' else 10 * k)]
                if c:
                    s['box'] = min(c)[1]; s['kozos'] = True
        # --- feliratok: áramkör-betűk globális mohó párosítása
        circ = [i for i, t in enumerate(reds) if RE_CIRCUIT.match(t['text'])]
        cand = []
        for si, s in enumerate(syms):
            if s['t'] in ('LAMPA', 'LAMPA_FAL', 'FALI_LAMPA', 'KAPCSOLO'):
                lim = 20 * k
                for ti in circ:
                    d = math.dist(s['c'], reds[ti]['c'])
                    if d <= lim: cand.append((d, si, ti))
        su, tu = set(), set()
        for d, si, ti in sorted(cand):
            if si in su or ti in tu: continue
            syms[si]['aramkor'] = reds[ti]['text'].replace(' ', ''); su.add(si); tu.add(ti)
        codes = [i for i, t in enumerate(reds) if t['text'] in DEVICE_CODES]
        cand = []
        for si, s in enumerate(syms):
            if s['t'] in ('DUGALJ', 'FALI_LAMPA', 'LAMPA_FAL'):
                for ti in codes:
                    d = math.dist(s['c'], reds[ti]['c'])
                    if d <= 7 * k: cand.append((d, si, ti))
        su, tu2 = set(), set()
        for d, si, ti in sorted(cand):
            if si in su or ti in tu2: continue
            syms[si]['kod'] = reds[ti]['text']; su.add(si); tu2.add(ti)
        # --- speciális jelek a maradék piros csoportokból
        rest = [i for i in red_idx if i not in used_paths]
        cl = clusters(red_idx, paths, 0.6 * k)
        def texts_near(c, rad):
            return [t for t in reds if math.dist(t['c'], c) <= rad]
        for g in cl:
            if any(i in used_paths for i in g['idx']): continue
            b = g['bbox']; w = (b[2] - b[0]) / k; h = (b[3] - b[1]) / k; c = ((b[0] + b[2]) / 2, (b[1] + b[3]) / 2)
            inside = [t for t in reds if b[0] - 1 <= t['c'][0] <= b[2] + 1 and b[1] - 1 <= t['c'][1] <= b[3] + 1]
            tx = [t['text'] for t in inside]
            if g['cnt']['c'] >= 6 and max(w, h) < 6.5 and min(w, h) < 3:
                syms.append(dict(t='KUPOLA', c=c))
            elif 'M' in tx and g['cnt']['l'] >= 15:
                mt = [t for t in inside if t['text'] == 'M'][0]
                low = [t for t in texts_near(mt['c'], 14 * k) if RE_CIRCUIT.match(t['text'])]
                low.sort(key=lambda t: math.dist(t['c'], mt['c']))
                syms.append(dict(t='VENT', c=mt['c'], aramkor=low[0]['text'] if low else ''))
            elif 'BK' in tx and not any(t in tx for t in ('1', '2', '3')) and max(w, h) > 12:
                if not any(q['t'] == 'BK' and math.dist(q['c'], c) < 8 * k for q in syms):
                    syms.append(dict(t='BK', c=c, kod='BK'))
        # ventilátor: minden piros „M”, amelyet ~5,7k sugarú gyűrű vesz körül (a fenti csoportos keresés kihagyja,
        # ha a jel egy szomszédos szerelvénnyel egy csoportba olvad – pl. A-811 06.1, független ellenőrzés 2026-10-24)
        for t in reds:
            if t['text'] != 'M' or any(q['t'] == 'VENT' and math.dist(q['c'], t['c']) < 3 * k for q in syms): continue
            ring = sum(1 for a, b in rlines if 4.6 * k <= math.dist(a, t['c']) <= 7.0 * k and 4.6 * k <= math.dist(b, t['c']) <= 7.0 * k)
            if ring >= 10:
                syms.append(dict(t='VENT', c=t['c'], aramkor=''))
        # ventilátor betű nélkül: a legközelebbi, más jelhez nem rendelt áramkör-betű 20k-n belül (pl. A-811 08 WC „b”)
        for s in syms:
            if s['t'] != 'VENT' or s.get('aramkor'): continue
            c = sorted((math.dist(reds[ti]['c'], s['c']), ti) for ti in circ if ti not in tu and math.dist(reds[ti]['c'], s['c']) <= 20 * k)
            if c:
                s['aramkor'] = reds[c[0][1]]['text'].replace(' ', ''); tu.add(c[0][1])
        # gyengeáramú aljzatok: minden piros '1','2','3' felirat (⊓ jel), a TV-blokkban a 'BK' is
        tvblocks = []
        for g in cl:
            b = g['bbox']
            inside = [t for t in reds if b[0] - 1 <= t['c'][0] <= b[2] + 1 and b[1] - 1 <= t['c'][1] <= b[3] + 1]
            tx = [t['text'] for t in inside]
            if '1' in tx and '2' in tx:
                tvblocks.append(b)
                for t in inside:
                    if t['text'] == 'BK':
                        syms.append(dict(t='GYENGE', c=t['c'], kod='BK', tv=True))
        for t in reds:
            if t['text'] in ('1', '2', '3'):
                tv = any(b[0] - 1 <= t['c'][0] <= b[2] + 1 and b[1] - 1 <= t['c'][1] <= b[3] + 1 for b in tvblocks)
                syms.append(dict(t='GYENGE', c=t['c'], kod=t['text'], tv=tv))
        for c in circles:
            r = c['r'] / k
            if 2.45 < r < 2.75:
                syms.append(dict(t='ANTENNA', c=c['c']))
        for t in reds:
            if t['text'] == 'S/F': syms.append(dict(t='FIX', c=t['c'], kod='S/F'))
            if t['text'] == 'EL4': syms.append(dict(t='ELOSZTO', c=t['c'], kod='EL4'))
        for t in blues:
            if t['text'] == 'T': syms.append(dict(t='TERMOSZTAT', c=t['c']))
        for (typ, x, y, kod, megj) in P.get('specials', []):
            syms.append(dict(t='SPEC', c=tp(x, y), spec=typ, megj=megj, kod=kod))
        # vezetővonal-láncok: tengelyirányú piros vonalak, amelyeken több fali jel ül -> közös fali hely
        segs = []
        for a, b in rlines:
            L = math.dist(a, b)
            if L < 6 * k or L > 90 * k: continue
            if abs(a[0] - b[0]) < 0.06: segs.append(('V', round((a[0] + b[0]) / 2, 1), min(a[1], b[1]), max(a[1], b[1])))
            elif abs(a[1] - b[1]) < 0.06: segs.append(('H', round((a[1] + b[1]) / 2, 1), min(a[0], b[0]), max(a[0], b[0])))
        merged = collections.defaultdict(list)
        for o, c0, a0, a1 in segs: merged[(o, c0)].append((a0, a1))
        lines_ = []
        for (o, c0), iv in merged.items():
            iv.sort(); cur = list(iv[0])
            for a0, a1 in iv[1:]:
                if a0 <= cur[1] + 0.8 * k: cur[1] = max(cur[1], a1)
                else: lines_.append((o, c0, cur[0], cur[1])); cur = [a0, a1]
            lines_.append((o, c0, cur[0], cur[1]))
        wl = []
        for p in paths:
            if p['col'] == (0.0, 0.0, 0.0) and p['w'] in (0.71, 0.99):
                for it in p['items']:
                    if it[0] == 'l': wl.append((it[1], it[2]))
        def near_wall(pt, tol):
            return any(seg_d(pt, a, b) <= tol for a, b in wl)
        chain_types = ('KAPCSOLO', 'DUGALJ', 'KUPOLA')
        for o, c0, a0, a1 in lines_:
            if a1 - a0 < 10 * k: continue
            on = []
            for s in syms:
                if s['t'] not in chain_types: continue
                x, y = s['c']
                if o == 'V' and abs(x - c0) <= 1.6 * k and a0 - 2 * k <= y <= a1 + 2 * k: on.append(s)
                elif o == 'H' and abs(y - c0) <= 1.6 * k and a0 - 2 * k <= x <= a1 + 2 * k: on.append(s)
            if len(on) < 2: continue
            ends = [(c0, a0), (c0, a1)] if o == 'V' else [(a0, c0), (a1, c0)]
            wall_end = [e for e in ends if near_wall(e, 2.5 * k)]
            if len(wall_end) != 1: continue
            e = wall_end[0]
            for s in on:
                s['lanc'] = e
                s.pop('kozos', None)
        # mozgásérzékelő bármilyen irányban: ≥3 koncentrikus hullám-ív (növekvő húr). A ferdén rajzoltak a fenti csoportos
        # keresésből kimaradtak (A-811: 2, A-902: 2 – független ellenőrzés, 2026-10-24). Fali hely: a vezetővonal falnál lévő vége.
        hullam = []
        for i in red_idx:
            its = paths[i]['items']
            if its and len(its) <= 2 and all(it[0] == 'c' for it in its):
                ch = math.dist(its[0][1], its[-1][4]) / k
                if 1.0 <= ch <= 7.0:
                    b = paths[i]['bbox']; hullam.append(((b[0] + b[2]) / 2, (b[1] + b[3]) / 2, ch))
        for h0 in hullam:
            grp = [h for h in hullam if math.dist(h[:2], h0[:2]) <= 2.5 * k]
            chs = sorted(h[2] for h in grp); dist_ = [chs[0]]
            for v in chs[1:]:
                if v > dist_[-1] * 1.08: dist_.append(v)
            if len(dist_) < 3: continue
            c = (sum(h[0] for h in grp) / len(grp), sum(h[1] for h in grp) / len(grp))
            if any(q['t'] == 'KUPOLA' and math.dist(q['c'], c) < 8 * k for q in syms): continue
            vege = None
            for a, b in rlines:
                for p0, p1 in ((a, b), (b, a)):
                    d0, d1 = math.dist(p0, c), math.dist(p1, c)
                    if d0 <= 12 * k and d1 - d0 >= 5 * k and math.dist(p0, p1) >= 6 * k and near_wall(p1, 3 * k):
                        if vege is None or d1 > vege[0]: vege = (d1, p1)
            s = dict(t='KUPOLA', c=c, ferde=True)
            if vege: s['lanc'] = vege[1]
            syms.append(s)
        # termosztát és kupola a lánc fali helyére
        for s in syms:
            if s['t'] == 'TERMOSZTAT' or (s['t'] == 'KUPOLA' and 'lanc' not in s):
                best = None
                lim = 12 * k if s['t'] == 'TERMOSZTAT' else 30 * k
                for q in syms:
                    if 'lanc' in q and math.dist(q['c'], s['c']) <= lim and (best is None or math.dist(q['c'], s['c']) < best[0]):
                        best = (math.dist(q['c'], s['c']), q['lanc'])
                if best: s['lanc'] = best[1]
        # árva dobozok a TV-blokknál -> a gyengeáramú feliratokhoz
        assigned_boxes = {s['box'] for s in syms if 'box' in s}
        for s in syms:
            if s['t'] in ('GYENGE', 'ANTENNA'):
                c = [(math.dist(s['c'], b['c']), bi) for bi, b in enumerate(boxes) if bi not in assigned_boxes]
                c = [x for x in c if x[0] <= 10 * k]
                if c:
                    s['box'] = min(c)[1]; assigned_boxes.add(s['box'])
        for s in syms:
            if s['t'] == 'KUPOLA' and not s.get('ferde'):
                c = [(math.dist(s['c'], b['c']), bi) for bi, b in enumerate(boxes) if bi not in assigned_boxes]
                c = [x for x in c if x[0] <= 10 * k]
                if c: assigned_boxes.add(min(c)[1]); s['sajat_talp'] = True
            if s['t'] == 'GYENGE' and s.get('tv'):
                for bi, b in enumerate(boxes):
                    if bi not in assigned_boxes and math.dist(s['c'], b['c']) <= 12 * k:
                        assigned_boxes.add(bi); s['tv_dobozok'] = s.get('tv_dobozok', 0) + 1
        # --- magasságok
        wall = [s for s in syms if s['t'] in ('DUGALJ', 'KAPCSOLO', 'FALI_LAMPA', 'LAMPA_FAL', 'GYENGE', 'ANTENNA')]
        anc = lambda s: boxes[s['box']]['c'] if 'box' in s else s['c']
        hl = []
        for t in reds:
            m = RE_HEIGHT.search(t['text'])
            if m:
                v = float(m.group(1).replace(',', '.')); v = round(v / 100, 3) if m.group(2) == 'cm' else v
                hl.append((t, v))
        cand = []
        for li, (t, v) in enumerate(hl):
            for si, s in enumerate(wall):
                d = math.dist(t['c'], s['c'])
                if d <= 32 * k: cand.append((d, li, si))
        lu = set()
        for d, li, si in sorted(cand):
            if li in lu or 'magassag' in wall[si]: continue
            t, v = hl[li]; lu.add(li)
            s0 = wall[si]; a0 = anc(s0)
            o0 = boxes[s0['box']]['o'] if 'box' in s0 else None
            for s in wall:
                if 'magassag' in s: continue
                a = anc(s)
                if s is s0 or (math.dist(a, a0) <= 14 * k and o0 and 'box' in s and boxes[s['box']]['o'] == o0 and
                               ((o0 == 'V' and abs(a[0] - a0[0]) < 1.5 * k) or (o0 == 'H' and abs(a[1] - a0[1]) < 1.5 * k))):
                    s['magassag'] = v; s['magassag_felirat'] = t['text']
        # --- lakáson kívüli terület (a bejárati ajtó lépcsőházi oldala): itt nincs lakás-kiállás
        kulso = lambda pm: any(a <= pm[0] <= c and b <= pm[1] <= e for (a, b, c, e) in P.get('kulso', []))
        # --- árva fali doboz -> a legközelebbi doboz nélküli fali jel (≤16k), pl. S/F fix bekötés, TSZ-dugalj
        #     (a független ellenőrzés szerint ezek „jel nélküli dobozként” duplikáltan szerepeltek)
        for bi, b in enumerate(boxes):
            if bi in assigned_boxes or kulso(tm(b['c'])): continue
            c = [(math.dist(s.get('apex', s['c']) if s['t'] == 'DUGALJ' else s['c'], b['c']), si) for si, s in enumerate(syms)
                 if s['t'] in ('DUGALJ', 'FIX', 'KAPCSOLO', 'FALI_LAMPA') and 'box' not in s and 'lanc' not in s]
            c = [x for x in c if x[0] <= 16 * k]
            if c:
                s = syms[min(c)[1]]; s['box'] = bi; s['utolag_doboz'] = round(min(c)[0] / M * 100); assigned_boxes.add(bi)
        # --- rekordok
        recs, kizart = [], []
        for s in syms:
            pm = tm(s['c'])
            probe = pm
            if s['t'] == 'FALI_LAMPA':
                probe = tm(s['apex'])          # a félkör domború oldala a helyiség felé néz
            elif s['t'] == 'DUGALJ':
                probe = tm(s['c'])             # a dugalj-félkör nyitott oldala néz a helyiség felé
            room, dist = room_near(probe, 0.35)
            if s.get('spec') == 'csengo_kulso' or kulso(pm): room = None
            if s['t'] in ('R', 'SPEC', 'GYENGE', 'BK', 'VENT') and room and ('ERKÉLY' in room or 'TERASZ' in room) and s.get('spec') != 'jakuzzi_aramkiallas':
                inner = [(n, rc) for n, rc in P['rooms'] if 'ERKÉLY' not in n and 'TERASZ' not in n]
                bestr = None
                for n, (a, b, c, e) in inner:
                    dd = math.hypot(max(a - probe[0], 0, probe[0] - c), max(b - probe[1], 0, probe[1] - e))
                    if dd <= 0.35 and (bestr is None or dd < bestr[1]): bestr = (n, dd)
                if bestr: room = bestr[0]
            if room is None:
                kizart.append(dict(tipus=TMAP[s['t']][2] or s.get('spec', ''), x_m=pm[0], y_m=pm[1], ok='a lakás helyiségein kívül (szomszéd vagy rajzrészlet)'))
                continue
            s['room'] = room; s['pm'] = pm
            recs.append(s)
        order = [t[0] for t in TIPUS]
        def key(s): return (order.index(s['t']), s['room'], -round(s['pm'][1], 1), s['pm'][0])
        recs.sort(key=key)
        out = []
        cnt = collections.Counter()
        for s in recs:
            T = TMAP[s['t']]
            cnt[T[1]] += 1
            typ = T[2] if s['t'] != 'SPEC' else s['spec']
            r = dict(azonosito=f"{flat}-{T[1]}{cnt[T[1]]:02d}", tipus=typ, helyiseg=s['room'], aramkor=s.get('aramkor', ''),
                     kod=s.get('kod', ''), x_m=s['pm'][0], y_m=s['pm'][1])
            if 'lanc' in s:
                bx, by = tm(s['lanc']); r.update(doboz_x_m=bx, doboz_y_m=by)
            elif 'box' in s:
                bx, by = tm(boxes[s['box']]['c']); r.update(doboz_x_m=bx, doboz_y_m=by)
            else:
                r.update(doboz_x_m='', doboz_y_m='')
            if s['t'] in ('LAMPA',):
                r['magassag_m'] = 'mennyezet'
            else:
                r['magassag_m'] = s.get('magassag', '')
            mj = []
            if 'magassag' in s: mj.append('magasság a rajzról: ' + s['magassag_felirat'])
            elif s['t'] in ('DUGALJ', 'KAPCSOLO'): mj.append('szerelési magasság nincs a rajzon')
            if s.get('ferde') and 'lanc' in s: mj.append('ferdén rajzolt jel: a fali hely a vezetővonal falnál lévő vége (az ajtósarok)')
            elif 'lanc' in s: mj.append('vezetővonalas csoport: a fali hely a vezetővonal falnál lévő vége (közös szerelvényhely)')
            elif s.get('kozos'): mj.append('a doboz-hozzárendelés bizonytalan (közös keret?)')
            if s.get('utolag_doboz') is not None: mj.append(f"a fali doboz a jeltől {s['utolag_doboz']} cm-re van (a legközelebbi doboz nélküli jelhez rendelve)")
            if s['t'] == 'LAMPA' and s.get('x', 2) < 2: mj.append('kör X nélkül – ellenőrizendő')
            if s.get('kod') in KOD_JELENTES and s['t'] in ('DUGALJ', 'FALI_LAMPA', 'LAMPA_FAL'): mj.append('kód: ' + KOD_JELENTES[s['kod']])
            if s['t'] == 'R': mj.append('ablakonként; jelentése a jelmagyarázatban – valószínűleg redőny/árnyékoló-kiállás, NEM IGAZOLT')
            if s['t'] == 'KUPOLA': mj.append('kupola + hullám jel – VALÓSZÍNŰLEG MOZGÁSÉRZÉKELŐ (riasztó): az A-811 módosítási szövege a „g”, „c,d” kapcsolókkal és a termosztáttal együtt mozgásérzékelőt tesz a nappali válaszfal sarkára, és ott pontosan ez a jel áll')
            if s['t'] == 'BK': mj.append('önálló BK doboz – VALÓSZÍNŰLEG A RIASZTÓ (BIZTONSÁGI) KÖZPONT: az A-811 módosítási szövege szerint a 05.2-3 összevonásakor „a biztonsági központ áthelyezésre kerül”, és az A-811 egyetlen önálló BK doboza a 05.2-3 gardróbjában van; nem takarható, hozzáférhető marad')
            if s['t'] == 'GYENGE': mj.append(('TV-blokk ' if s.get('tv') else '') + 'gyengeáramú aljzat (⊓ jel), kód: ' + s.get('kod', '') + ' – a kódok (1/2/3/BK) jelentése a jelmagyarázatban, NEM IGAZOLT (valószínűleg TV/adat/telefon)')
            if s['t'] == 'ANTENNA': mj.append('négyzet + kör: TV/antenna aljzat (valószínű)')
            if s['t'] == 'VENT': mj.append('elszívó ventilátor kiállása; a betű a kapcsoló áramkör')
            if s['t'] == 'FIX': mj.append('főzőlap/sütő fix bekötés (S/F)')
            if s['t'] == 'TERMOSZTAT': mj.append('mennyezeti hűtés-fűtés termosztátja (gépészeti kék jel)')
            if s['t'] == 'SPEC': mj.append(s['megj'])
            r['megjegyzes'] = '; '.join(mj)
            r['statusz'] = 'TERV SZERINT'
            r['forras'] = f"{P['page']}. o. (dosszié {P['dosszie']})"
            r['_c'] = s['c']; r['_box'] = boxes[s['box']]['bbox'] if 'box' in s else None; r['_t'] = s['t']
            out.append(r)
        # árva dobozok (a fenti, már elnyelt dobozokat – kupola talpa, TV-blokk keret – nem listázzuk)
        nz = 0
        for bi, b in enumerate(boxes):
            if bi in assigned_boxes: continue
            pm = tm(b['c']); room, dist = room_near(pm, 0.35)
            if kulso(pm):
                kizart.append(dict(tipus='doboz_jel_nelkul', x_m=pm[0], y_m=pm[1], ok='a bejárati ajtó lépcsőházi oldalán (csengőnyomó doboza) – nem a lakásban'))
                continue
            if room is None: continue
            nz += 1
            out.append(dict(azonosito=f"{flat}-Z{nz:02d}", tipus='doboz_jel_nelkul', helyiseg=room, aramkor='', kod='', x_m=pm[0], y_m=pm[1],
                            doboz_x_m=pm[0], doboz_y_m=pm[1], magassag_m='', megjegyzes='fali doboz, amelyhez a szkript nem rendelt jelet – kézi ellenőrzés',
                            statusz='TERV SZERINT', forras=f"{P['page']}. o.", _c=b['c'], _box=b['bbox'], _t='DOBOZ'))
        # --- hűtő-fűtő zónák
        zsegs = []
        for p in paths:
            if not isblue(p['col']): continue
            for it in p['items']:
                if it[0] != 'l': continue
                a, b = it[1], it[2]; dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy)
                if L < 0.3 or abs(dx) < 0.05 * L or abs(dy) < 0.05 * L: continue
                zsegs.append((a, b, p['w']))
        groups = collections.defaultdict(list)
        for a, b, w in zsegs:
            ang = math.atan2(b[1] - a[1], b[0] - a[0]) % math.pi
            off = a[0] * -math.sin(ang) + a[1] * math.cos(ang)
            groups[(round(ang, 2), round(off), w)].append((a, b))
        zones = []
        for (ang, off, w), ss in groups.items():
            if len(ss) < 8: continue
            ux, uy = math.cos(ang), math.sin(ang)
            pts = [p for s in ss for p in s]; ts = [p[0] * ux + p[1] * uy for p in pts]
            p0 = pts[ts.index(min(ts))]; p1 = pts[ts.index(max(ts))]
            if math.dist(p0, p1) < 25 * k: continue
            a, b = tm(p0), tm(p1)
            cpt = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
            room, dist = room_near(cpt, 0.6)
            if room is None: continue
            zones.append(dict(helyiseg=room, x_min=min(a[0], b[0]), y_min=min(a[1], b[1]), x_max=max(a[0], b[0]), y_max=max(a[1], b[1]),
                              statusz='TERV SZERINT', megjegyzes='a rajz szaggatott kék átlója jelöli a mennyezeti hűtő-fűtő mezőt; téglalap az átló végpontjaiból, panelszél ±10 cm'))
        zones.sort(key=lambda z: (z['x_min'], z['y_min']))
        for i, z in enumerate(zones, 1): z['azonosito'] = f"{flat}-HF{i:02d}"
        # --- álmennyezet: a zöld „gk. álm.” feliratok (imp. = impregnált, nor. = normál gipszkarton)
        alm = []
        for blk in page.get_text('dict')['blocks']:
            for ln in blk.get('lines', []):
                t = ''.join(sp['text'] for sp in ln['spans']).strip()
                if 'álm' in t and ln['spans'] and ln['spans'][0]['color'] == 0x1bb816:
                    bb = ln['bbox']; pm = tm(((bb[0] + bb[2]) / 2, (bb[1] + bb[3]) / 2))
                    room, _ = room_near(pm, 0.6)
                    alm.append(dict(felirat=t, x_m=pm[0], y_m=pm[1], helyiseg=room or 'a lakás körvonalán kívül – kézi ellenőrzés'))
        # --- azonosító-stabilitás: a korábbi kimenet azonosítója megmarad, ha a típus egyezik és a hely ≤3 cm-en belül van;
        #     új tétel az előtag következő szabad sorszámát kapja, megszűnt tétel száma nem kerül újra kiosztásra.
        #     Teljes újraszámozás csak WSG_UJRASZAMOZAS=1 mellett.
        pj = os.path.join(OUT, f'{flat}_villamos.json')
        prev = []
        if os.path.exists(pj) and not os.environ.get('WSG_UJRASZAMOZAS'):
            prev = json.load(open(pj, encoding='utf-8'))['kiallasok']
        pfx = lambda i: re.match(r'^[A-Z0-9]+-([A-Z]+)\d+$', i).group(1)
        used_ids, maxn = set(), collections.Counter()
        for q in prev:
            p_ = pfx(q['azonosito']); maxn[p_] = max(maxn[p_], int(re.search(r'(\d+)$', q['azonosito']).group(1)))
        for r in out:
            p_ = pfx(r['azonosito']); best = None
            for q in prev:
                if q['tipus'] != r['tipus'] or q['azonosito'] in used_ids or pfx(q['azonosito']) != p_: continue
                dq = math.hypot(float(q['x_m']) - r['x_m'], float(q['y_m']) - r['y_m'])
                if dq <= 0.03 and (best is None or dq < best[0]): best = (dq, q['azonosito'])
            if best: r['_id'] = best[1]; used_ids.add(best[1])
        for r in out:
            if '_id' not in r and prev:
                p_ = pfx(r['azonosito']); maxn[p_] += 1; r['_id'] = f"{flat}-{p_}{maxn[p_]:02d}"
            if '_id' in r: r['azonosito'] = r['_id']
        # --- mentés
        public = [{k2: v for k2, v in r.items() if not k2.startswith('_')} for r in out]
        cols = ['azonosito', 'tipus', 'helyiseg', 'aramkor', 'kod', 'x_m', 'y_m', 'doboz_x_m', 'doboz_y_m', 'magassag_m', 'statusz', 'forras', 'megjegyzes']
        meta = dict(lakas=flat[0] + '-' + flat[1:], forras_pdf='WGR1_meretezett_alaprajzok.pdf (vevői adat, nincs a repóban)', forras_pdf_sha256=sha,
                    oldal=P['page'], dosszie=P['dosszie'], lepték=f"1:{P['scale']}", verzio=P['verzio'],
                    koordinatak=dict(egyseg='m', x='rajzon jobbra', y='rajzon felfelé', origo=P['origo'], pt_per_m=round(M, 4), X0_pt=X0, Y0_pt=Y0),
                    pontossag='rajzi pontosság ±1 cm (1:50) / ±2 cm (1:100); a megvalósult kiállás eltérhet – a helyszíni ellenőrzésig TERV SZERINT',
                    mezok=dict(x_m_y_m='a rajzi jel középpontja (mennyezeti lámpánál ez a kiállás helye)',
                               doboz_x_m_doboz_y_m='a fali szerelvénydoboz helye a falsíkon – fali eszköznél ez a fizikai hely',
                               magassag_m='szerelési magasság a padlótól, ha a rajzon szerepel'),
                    modositasok_villamos=dict(forras=MODOSITAS[flat]['forras'],
                                              tetelek=[dict(terulet=a, szoveg=b) for a, b in MODOSITAS[flat]['tetelek']]),
                    lakason_kivul=MODOSITAS[flat]['lakason_kivul'], almennyezet=dict(megjegyzes=ALMENNYEZET, feliratok=alm),
                    kinyerve='2026-10-24, kinyeres/villamos_kinyeres.py v2 (Claude)')
        json.dump(dict(meta=meta, kiallasok=public, hutes_futes_zonak=zones, kizart_jelek=kizart),
                  open(os.path.join(OUT, f'{flat}_villamos.json'), 'w'), ensure_ascii=False, indent=1)
        with open(os.path.join(OUT, f'{flat}_villamos.csv'), 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=cols, extrasaction='ignore'); w.writeheader(); [w.writerow(r) for r in public]
        with open(os.path.join(OUT, f'{flat}_hutes_futes_zonak.csv'), 'w', newline='', encoding='utf-8') as f:
            zc = ['azonosito', 'helyiseg', 'x_min', 'y_min', 'x_max', 'y_max', 'statusz', 'megjegyzes']
            w = csv.DictWriter(f, fieldnames=zc, extrasaction='ignore'); w.writeheader(); [w.writerow(z) for z in zones]
        # --- átfedéskép
        dpi = 200 if P['scale'] == 50 else 330
        s_ = dpi / 72
        pix = page.get_pixmap(dpi=dpi)
        im = Image.frombytes('RGB', (pix.width, pix.height), pix.samples)
        im = Image.blend(im, Image.new('RGB', im.size, 'white'), 0.5)
        d = ImageDraw.Draw(im)
        COL = {'LAMPA': (0, 60, 255), 'LAMPA_FAL': (170, 0, 190), 'FALI_LAMPA': (170, 0, 190), 'KAPCSOLO': (0, 140, 0), 'DUGALJ': (230, 100, 0),
               'R': (0, 150, 180), 'TERMOSZTAT': (110, 110, 110), 'ELOSZTO': (0, 0, 0), 'DOBOZ': (255, 0, 0), 'VENT': (0, 120, 120),
               'GYENGE': (120, 60, 0), 'ANTENNA': (120, 60, 0), 'BK': (120, 60, 0), 'KUPOLA': (200, 0, 80), 'FIX': (150, 80, 0), 'SPEC': (200, 0, 80)}
        P2 = lambda xm, ym: ((X0 + xm * M) * s_, (Y0 - ym * M) * s_)
        for name, (a, b, c, e) in P['rooms']:
            d.rectangle([P2(a, e), P2(c, b)], outline=(200, 200, 200), width=1)
        for z in zones:
            d.rectangle([P2(z['x_min'], z['y_max']), P2(z['x_max'], z['y_min'])], outline=(70, 70, 255), width=3)
            q = P2(z['x_min'], z['y_max']); d.text((q[0] + 4, q[1] + 3), z['azonosito'] + ' hűtő-fűtő mező', fill=(50, 50, 220), font=FS)
        rr = 9 if P['scale'] == 50 else 7
        for r in out:
            x, y = r['_c']; c = COL.get(r['_t'], (0, 0, 0))
            d.ellipse([x * s_ - rr, y * s_ - rr, x * s_ + rr, y * s_ + rr], outline=c, width=3)
            if r['_box']:
                b0, b1, b2, b3 = r['_box']; d.rectangle([b0 * s_ - 2, b1 * s_ - 2, b2 * s_ + 2, b3 * s_ + 2], outline=c, width=2)
            lbl = r['azonosito'].split('-')[1] + ((' ' + r['aramkor']) if r['aramkor'] else '') + ((' ' + r['kod']) if r['kod'] else '')
            d.text((x * s_ + rr + 2, y * s_ - rr - 3), lbl, fill=c, font=F)
        xs = [a for _, (a, b, c, e) in P['rooms']] + [c for _, (a, b, c, e) in P['rooms']]
        ys = [b for _, (a, b, c, e) in P['rooms']] + [e for _, (a, b, c, e) in P['rooms']]
        gx0, gx1 = math.floor(min(xs)) - 1, math.ceil(max(xs)) + 1
        gy0, gy1 = math.floor(min(ys)) - 1, math.ceil(min(max(ys), 12.6 if flat == 'A902' else max(ys))) + 1
        for gx in range(gx0, gx1 + 1):
            d.line([P2(gx, gy1), P2(gx, gy0)], fill=(160, 205, 255), width=1)
            q = P2(gx, gy1); d.text((q[0] + 2, q[1] + 2), f'x={gx}', fill=(60, 120, 220), font=FS)
        for gy in range(gy0, gy1 + 1):
            d.line([P2(gx0, gy), P2(gx1, gy)], fill=(160, 205, 255), width=1)
            q = P2(gx0, gy); d.text((q[0] + 2, q[1] + 2), f'y={gy}', fill=(60, 120, 220), font=FS)
        a_, b_ = P2(gx0, gy1), P2(gx1, gy0)
        crop = (max(0, int(a_[0]) - 10), max(0, int(a_[1]) - 10), min(im.width, int(b_[0]) + 10), min(im.height, int(b_[1]) + 10))
        im = im.crop(crop)
        d = ImageDraw.Draw(im)
        leg = [('ML mennyezeti lámpa', COL['LAMPA']), ('FL fali lámpa', COL['FALI_LAMPA']), ('K kapcsoló', COL['KAPCSOLO']), ('D dugalj', COL['DUGALJ']),
               ('V ventilátor', COL['VENT']), ('G gyengeáram/TV', COL['GYENGE']), ('S/X egyéb', COL['SPEC']), ('R ablak-R', COL['R']), ('T termosztát', COL['TERMOSZTAT']),
               ('Z doboz jel nélkül', COL['DOBOZ']), ('HF hűtő-fűtő mező', (70, 70, 255))]
        y0 = 8
        d.rectangle([6, 4, 250, 8 + 18 * len(leg)], fill=(255, 255, 255), outline=(180, 180, 180))
        for t, c in leg:
            d.text((12, y0), t, fill=c, font=FS); y0 += 18
        d.text((260, 8), f"{meta['lakas']} – villamos kiállások, TERV SZERINT ({P['verzio'].split('(')[0].strip()}); rács: 1 m", fill=(0, 0, 0), font=F)
        im.save(os.path.join(OUT, f'{flat}_villamos_atfedes.png'), optimize=True)
        summary[flat] = dict(collections.Counter(r['tipus'] for r in public), hutes_futes_mezo=len(zones), kizart=len(kizart))
    print(json.dumps(summary, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main()
