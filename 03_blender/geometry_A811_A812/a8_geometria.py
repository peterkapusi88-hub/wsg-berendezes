# =====================================================================================
# A-811 és A-812 – Blender-alapmodell geometriája a méretezett alaprajzokból (ELŐZETES, 2026-10-24, Claude)
#
# Forrás: WGR1_meretezett_alaprajzok.pdf (vevői adat, NINCS a repóban; helyi útvonal az 1. argumentum)
#   - 5. old.  A-811 méretezett alaprajz 1:50, M1 (KORR nem készült)        1 m = 56,693 pt, origó X0 434,02 / Y0 748,0 pt
#   - 12. old. A-812 átnézeti alaprajz 1:100, M1 KORR (2026.04.28.)          1 m = 28,346 pt, origó X0 539,36 / Y0 600,95 pt
#   - 2. old.  8. emelet megvalósulási terv 1:125 (2026.05.20.) – helyiség-m², erkély-m² (eltolással illesztve)
#   - 7. és 14. old. burkolatkiosztási terv – padlóanyag helyiségenként
# Koordináta: azonos a 01_alaprajzok/villamos_kiallasok/A811_/A812_villamos.json rendszerével (x rajzon jobbra, y rajzon
#   felfelé, m; x=0 a nappali homlokzati belső falsíkja). A 2. oldali illesztés szerint a két lakás x-e közös, és
#   y_A812 = y_A811 − 11,85 (az A-811 felső fala = az A-812 alsó fala).
# Módszer (reprodukálható): 0,71/0,99 pt fekete falvonal-párok, köztük sraffozással → falsávok; kézi javítás (törlés,
#   kiegészítés: beton pillérek kereszt-sraffal, aknák); ajtó- és ablaknyílások kivonása; téglalap-felbontás.
#   Nyílászárók: nyitásívek (Bézier-ív középpontja = zsanér, sugár = szárny), ablakprofilok a tokvonalakból.
# Kimenet: <lakás>_geometria_ELOZETES.json és <lakás>_falak_ellenorzes.png ebben a mappában. Blender-fájlhoz nem nyúl.
# Futtatás: python3 a8_geometria.py /helyi/útvonal/WGR1_meretezett_alaprajzok.pdf
# =====================================================================================
import sys, os, json, math, hashlib
import pymupdf
from shapely.geometry import box, Polygon
from shapely.ops import unary_union

PDF = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
SHA = hashlib.sha256(open(PDF, 'rb').read()).hexdigest()

# ------------------------------------------------------------------ közös adatok
FAL_ANYAG = 'fehér festett fal (MEGLÉVŐ, megtartandó)'
PARKETTA = 'Egger Grey Soria Oak EL2065, Classic 8/32 4V Aqua (593610) – burkolatkiosztási terv'
KERAMIA = 'Glitch Salt matt 60×60 (03285A), fuga Holdfény 103 – burkolatkiosztási terv'


def ajto(nev, fal, nyilas, fal_sik, zsaner, irany, r, nevleges, szobak, megj=''):
    return nev, dict(tipus='nyilo', fal=fal, nyilas=nyilas, fal_sik=fal_sik, zsaner=zsaner, irany=irany, r=r,
                     magassag=2.10, nevleges=nevleges, szobak=szobak, megj=megj)


FL = {
 'A811': dict(
  lakas='A-811', page=5, scale=50, X0=434.02, Y0=748.0, box=(-2.8, -0.9, 9.0, 12.3),
  verzio='M1 (érvényes; KORR-alaprajz nem készült), 5. old., dosszié 150',
  H=2.70, H_forras='Kémeri műszaki ellenőr mérése 2,69–2,72 m (2026-10-21, GOAL.md); a műszaki melléklet: 8. em. 2,70 m',
  # --- falsávok kézi javítása
  torol=[[-0.48, 10.99, -0.29, 11.15],   # hőszigetelés-részlet
         [-0.29, 7.60, -0.19, 7.95], [-0.29, 2.64, -0.19, 2.92],   # ablakprofil (a nyílászáróhoz tartozik)
         [-0.47, 5.69, -0.29, 5.78],     # szigetelés-szilánk
         [-1.14, 0.41, -0.97, 0.50], [-1.14, -0.31, -0.96, -0.14],   # erkélyvég szigetelés-részletei
         [0.88, -0.47, 0.98, -0.30], [3.01, -0.49, 3.03, 0.002],   # alsó szigetelés-szilánkok
         [5.30, 1.48, 5.99, 1.62], [5.22, 1.48, 5.32, 1.51],       # a HTH-ajtó nyílása (méretvonal-jel miatt téves sáv)
         [5.0, 3.73, 5.14, 3.82]],       # a 05.2-3 ajtó tokvonalai közti téves sáv (a falcsonkot a hozzaad pótolja)
  hozzaad=[[-0.465, 4.65, 0.0, 6.815],     # homlokzati pillér (beton, kereszt-sraff) + hőszigetelés az erkély felé
           [-0.465, 10.415, -0.305, 11.857],   # sarokpillér hőszigetelése
           [-0.975, 0.6, -0.3, 0.9],       # a 05.1 fülke feletti fal/gerenda (sraffozott)
           [-0.975, 0.9, -0.305, 1.08],    # v2: a fülke-fal hőszigetelése az erkélylemezig (Homlokzati fal réteg; a v1-ben rés volt)
           [3.015, -0.489, 3.32, 0.001],   # pillér az alsó falban (kereszt-sraff); v2: 3,015-től, a v1-ben 5 mm-es rés volt
           [5.02, 3.775, 5.12, 3.82],      # v2: a 05.2-3 ajtó felső falcsonkja (a v1-ben 4 cm-es lyuk volt)
           [8.25, -0.307, 8.5, 6.651],     # jobb oldali külső fal egyben
           [3.22, 6.551, 3.32, 6.651], [5.02, 6.551, 5.12, 6.651], [4.42, 1.5, 4.52, 1.601], [6.17, 2.501, 6.27, 2.6]],  # csomópontok
  hozzaad_utana=[[-0.2, 7.69, 0.0, 7.85],    # beton oszlop a nappali üvegfal síkjában (kereszt-sraff)
                 [-0.2, 2.7, 0.01, 2.861]],  # a 05.1 | 05.2-3 válaszfal csatlakozása az üvegfalhoz (v2: 0,01-ig, a v1-ben 1 cm-es rés volt)
  kivon=[[5.12, 1.60, 5.27, 1.70], [5.0, 1.60, 5.02, 1.70]],   # v2: a 05.1 ajtótok takaróvonalaiból képzett fölösleges falrész (a terven ott padló van)
  elotetfal={'Elotetfal_GK_EL4': [7.25, 8.325, 8.25, 8.45]},  # v2: „Előtétfal (GK)” réteg, 12,5 cm; az EL4 lakáselosztó előtétfala (méretszám 1,62⁵)
  almennyezet={'Almennyezet_WC_08': dict(r=[[7.30, 4.85, 8.25, 6.60]], z=2.40, felirat='imp.gk. álm. as.:+2,40 m')},
  aknak={'Akna_konyha': [6.6, 10.95, 7.3, 11.55], 'Akna_gepeszet_WC': [6.17, 4.75, 7.3, 6.25]},
  ajtok=dict([   # v2: a nyilas a terv falnyílása; a tok 4 cm (a tok és a tiszta nyílás a tervvel egyezik, lásd README)
   ajto('Ajto_05_1', 'y', [1.70, 2.60], [5.005, 5.135], [5.005, 2.56], '-x', 0.82, '90/2,10', ['05.1', '07']),
   ajto('Ajto_05_2_3', 'y', [2.875, 3.775], [5.005, 5.135], [5.005, 2.915], '-x', 0.82, '90/2,10', ['05.2-3', '07']),
   ajto('Ajto_HTH_09', 'x', [5.27, 6.02], [1.486, 1.615], [5.31, 1.615], '+y', 0.67, '75/2,10', ['09', '07'], 'kifelé, a közlekedőbe nyílik'),
   ajto('Ajto_furdo_06_1', 'y', [1.675, 2.425], [6.17, 6.27], [6.28, 2.385], '+x', 0.67, '75/2,10', ['06.1', '07']),
   ajto('Ajto_furdo_06_2', 'y', [3.527, 4.277], [6.17, 6.28], [6.155, 4.237], '-x', 0.67, '75/2,10', ['06.2', '07'], 'kifelé, a közlekedőbe nyílik'),
   ajto('Ajto_WC_08', 'x', [7.425, 8.175], [6.59, 6.715], [8.135, 6.715], '+y', 0.67, '75/2,10', ['08', '01'], 'kifelé, az előtérbe nyílik; forgása a bejárati ajtóéval átfed'),
   ajto('Ajto_bejarat', 'y', [6.75, 7.801], [8.25, 8.5], [8.35, 7.772], '-x', 0.994, '1,05/2,10', ['01', 'lépcsőház']),
  ]),
  # homlokzati üvegfalak: tok f0..f1, toksáv b0..b1 (x), fal x0..x1, magasság 2,57; üvegtáblák; nyíló szárnyak (nyitásív)
  ablakok={
   'Uvegfal_05_1_05_2_3': dict(tengely='y', f=[1.026, 4.675], b=[-0.28, -0.20], fal=[-0.305, 0.0], Hn=2.57, nevleges='3,65/2,57',
       uvegek=[[1.161, 1.931], [2.10, 2.646], [2.916, 3.705], [3.876, 4.54]],
       nyilo=[dict(nev='Erkelyajto_05_1', nyilas=[1.08, 2.01], zsaner=[-0.18, 1.08], irany='+x', r=0.93),
              dict(nev='Erkelyajto_05_2_3', nyilas=[3.795, 4.62], zsaner=[-0.18, 4.62], irany='+x', r=0.825)],
       szobak=['05.1', '05.2-3'], megj='egy 3,65 m-es elem; a 2,646–2,916 közti profilhoz csatlakozik a két szoba közti válaszfal'),
   'Uvegfal_nappali': dict(tengely='y', f=[6.79, 10.44], b=[-0.28, -0.20], fal=[-0.305, 0.0], Hn=2.57, nevleges='3,65/2,57',
       uvegek=[[6.926, 7.556], [7.936, 8.57], [8.741, 9.443], [9.603, 10.306]],
       nyilo=[dict(nev='Erkelyajto_nappali_1', nyilas=[6.846, 7.636], zsaner=[-0.18, 7.635], irany='+x', r=0.79),
              dict(nev='Erkelyajto_nappali_2a', nyilas=[8.66, 9.523], zsaner=[-0.18, 8.66], irany='+x', r=0.863),
              dict(nev='Erkelyajto_nappali_2b', nyilas=[9.523, 10.386], zsaner=[-0.18, 10.385], irany='+x', r=0.863)],
       szobak=['03-04'], megj='a 7,69–7,85 közti beton oszlop az üvegfal síkjában marad (kereszt-sraff)'),
  },
  szobak={  # téglalap-unió a tervi (vakolatlan) falsíkok között; kulcs: (rövid név, rajzi név, padló)
   'nappali_etkezo': ('03-04 ÉTKEZŐ-NAPPALI', 'parketta', [[0, 6.651, 6.17, 11.55]]),
   'konyha': ('02 KONYHA', 'parketta', [[6.17, 8.55, 8.25, 10.95], [6.17, 10.95, 6.6, 11.55], [7.3, 10.95, 8.25, 11.55]]),
   'eloter': ('01 ELŐTÉR', 'parketta', [[6.17, 6.7, 8.25, 8.325], [6.17, 8.325, 7.25, 8.45], [6.27, 6.25, 7.2, 6.7]]),   # v2: az EL4 előtétfal nélkül
   'kozlekedo': ('07 KÖZLEKEDŐ', 'parketta', [[5.12, 1.615, 6.17, 6.651], [5.12, 1.60, 5.27, 1.615]]),   # v2: a HTH-fal síkjáig
   '05_1': ('05.1 SZOBA', 'parketta', [[0, 0, 4.42, 2.7], [4.42, 1.601, 5.005, 2.7], [5.005, 1.601, 5.02, 1.70], [-0.67, 0, 0, 0.6]]),   # v2: a falsíkig az ajtó mellett
   '05_2_3': ('05.2-3 SZOBA', 'parketta', [[0, 2.8, 5.02, 3.85], [0, 3.85, 3.22, 6.551]]),
   '05_2_3_gardrob': ('05.2-3 SZOBA (gardrób)', 'parketta', [[3.32, 3.85, 5.02, 5.351], [3.92, 5.351, 5.02, 5.651], [3.32, 5.651, 5.02, 6.551]]),
   'hth_09': ('09 HTH', 'keramia', [[4.52, 0, 6.17, 1.486], [4.52, 1.486, 5.27, 1.50]]),   # v2: a falsíkig (a v1-ben 1,4 cm-es padlórés)
   'furdo_06_1': ('06.1 FÜRDŐ', 'keramia', [[6.27, 0, 8.25, 2.501]]),
   'furdo_06_2': ('06.2 FÜRDŐ', 'keramia', [[6.27, 2.6, 8.25, 4.75]]),
   'wc_08': ('08 WC', 'keramia', [[7.3, 4.851, 8.25, 6.59]]),
  },
  # a megvalósulási terv (2. old.) helyiség-m²-e: melyik szobakulcs(ok) összegével vethető össze. A terv a homlokzati
  # szobák területébe az üvegfal tokjáig (~0,2 m mély ablakmélyedés) beszámít, a fürdők területéből az előtétfalat levonja.
  terv_m2={'Nappali+étkező': (30.93, ['nappali_etkezo']), 'Konyha': (5.80, ['konyha']), 'Előtér': (4.04, ['eloter']),
           'Közlekedő': (5.30, ['kozlekedo']), 'Szoba (05.2-3, gardróbbal)': (18.74, ['05_2_3', '05_2_3_gardrob']),
           'Szoba (05.1)': (13.33, ['05_1']), 'Fürdő (06.2)': (3.82, ['furdo_06_2']), 'Fürdő (06.1)': (4.77, ['furdo_06_1']),
           'Ht.hg (09)': (2.48, ['hth_09']), 'WC (08)': (1.47, ['wc_08'])},
  terv_ossz=90.68, erkely_m2=14.30,
  erkely=dict(lapok=[[-2.035, 3.26, -0.465, 10.905], [-1.15, 1.08, -0.465, 3.26]], z=-0.15,
              korlat=[['x', -2.03, 3.29, 10.825], ['y', 3.29, -2.035, -1.105], ['x', -1.105, 1.08, 3.29]],   # a korlát tengelyvonala (v2: a terv x −2,055…−2,005 sávjának közepe)
              korlat_oszto=0.11,   # v2: pálcatávolság a terv szerint ≈ 11 cm
              valaszfal=[[-1.955, 10.825, -0.51, 10.905]],   # v2: a terven fém osztó („Lakatos Külső” réteg), 1,445 × 0,08 m
              megj='a kontúr a rajz 0,51 pt erkélyvonalaiból; a korlát pálcás (terv, ≈ 11 cm osztás), helye a tervvel egyezik; padlószint (−0,15 m) és '
                   'korlátmagasság (1,10 m) a terven nincs, NEM IGAZOLT; a felső végén fém osztó az A-812 erkélye felé, magassága a terven nincs (1,10 m feltételezve)'),
  plafon=[[-0.975, -0.307, 8.5, 1.08], [-0.465, 1.08, 8.5, 11.857]],
  kamerak={
   'Cam_02_Nappali_erkely': dict(loc=[5.75, 7.15, 1.5], cel=[0.0, 10.2, 1.25], statusz='ÖSSZEHASONLÍTÓ – B fázis (nappali → erkélyüveg)'),
   'Cam_03_Etkezo_konyha': dict(loc=[0.55, 7.05, 1.5], cel=[7.6, 10.6, 1.2], statusz='ÖSSZEHASONLÍTÓ – B fázis (ablak felől → étkező, konyha)'),
   'Cam_04_Haloszoba': dict(loc=[3.0, 3.0, 1.5], cel=[0.2, 6.2, 1.2], statusz='ÖSSZEHASONLÍTÓ – B fázis (05.2-3 háló: ágyfal + üvegfal)'),
   'Cam_05_Haloszoba_05_1': dict(loc=[4.75, 2.45, 1.5], cel=[0.0, 0.9, 1.2], statusz='kiegészítő nézet (05.1)'),
  },
 ),
 'A812': dict(
  lakas='A-812', page=12, scale=100, X0=539.36, Y0=600.95, box=(-2.8, -1.2, 9.4, 17.6),
  verzio='M1 KORR (2026.04.28.), 12. old. átnézeti lap 1:100, dosszié 179 (a 11. old. 1:50-es lap csak részlet)',
  H=2.70, H_forras='Kémeri műszaki ellenőr mérése 2,69–2,73 m (2026-10-21, GOAL.md); a műszaki melléklet: 8. em. 2,70 m',
  torol=[[2.84, 5.89, 3.021, 17.22],      # hálószobai homlokzat: hőszigetelés-szilánkok (nincs erkély előtte)
         [0.88, 5.59, 0.98, 6.07], [-1.14, 4.99, -0.969, 5.91],
         [8.54, 4.14, 8.56, 4.41], [-0.31, -0.56, -0.279, 0.87],
         [7.20, 10.83, 7.34, 11.68],      # a 06.1 ajtónyílás téves sávja + toksávok
         [3.05, 7.83, 3.15, 8.11]],       # v2: a két ablak közti tok-kontúr téves sávja (a kapcsolóprofil külön elem)
  hozzaad=[[3.02, 16.82, 9.02, 17.12],    # felső külső fal (kereszt-sraff; belső sík a 4,09-es méretből: 12,73 + 4,09)
           [8.25, -0.308, 8.5, 2.95],      # jobb oldali külső fal egyben
           [8.25, 6.1, 9.02, 6.4],         # pillér + falcsatlakozás a jobb oldalon
           [3.015, 5.6, 3.32, 5.905], [3.22, 4.7, 3.32, 4.8], [5.47, 4.7, 5.57, 4.8], [6.07, 7.89, 6.17, 7.99],
           [6.07, 11.23, 6.17, 11.33], [7.22, 9.7, 7.32, 9.8], [7.185, 12.63, 7.32, 12.73], [7.22, 6.3, 7.32, 6.4],
           [-0.465, -1.031, -0.305, 0.925],   # v2: homlokzati hőszigetelés a nappali pillére előtt (Homlokzati fal réteg; a v1-ben hiányzott)
           [-0.975, 4.52, -0.305, 4.695],     # v2: hőszigetelés a fülke-fal alatt, az erkélylemezig (a v1-ben rés volt)
           [-0.975, 4.695, -0.67, 5.0]],      # v2: a fülke külső falsarka (a v1-ben hiányzott)
  hozzaad_utana=[[3.12, 7.89, 3.32, 8.05],      # v2: vasbeton oszlop a 05.1 és a 05.2 ablaka között (T_Oszlop réteg); a v1 teljes 27 cm-es pillére túl széles volt
                 [3.015, 16.80, 3.32, 16.82]],  # v2: a 05.3 sarka (a terv felső fala 0,275°-kal ferde; a v1-ben 1,2 cm-es rés volt)
  kivon=[],
  elotetfal={'Elotetfal_GK_EL4': [7.32, 4.575, 8.25, 4.70]},   # v2: „Előtétfal (GK)” réteg, 12,5 cm; az EL4 lakáselosztó előtétfala (méretszám 1,67⁵)
  almennyezet={'Almennyezet_eloter': dict(r=[[7.22, 2.90, 7.32, 4.10], [7.32, 2.90, 8.25, 4.575]], z=2.50, felirat='gk. álm. as.: + 2,50 m'),
               'Almennyezet_konyhasarok': dict(r=[[7.30, 0.0, 8.25, 0.30]], z=2.45, felirat='nor. gk. álm. as.: + 2,45 m (a felsőszekrény magasságát korlátozza)')},
  kapcsolo_profil={'Ablak_05_1_05_2_kapcsoloprofil': dict(r=[3.04, 7.835, 3.12, 8.105], Hn=2.57,
                                                          megj='v2: a két ablak közti kapcsoló-/tokprofil a tok síkjában (Homlokzati fal réteg)')},
  szemoldok_extra={'Ablak_05_1_05_2_szemoldok': [3.02, 7.835, 2.57, 3.32, 8.105]},   # v2: az oszlop melletti mélyedések fölött
  aknak={'Akna_konyha': [6.45, -0.3, 7.3, 0.6], 'Akna_gardrob_10_2': [5.47, 11.9, 6.17, 12.63], 'Akna_05_1': [5.47, 5.3, 6.17, 5.7],
         'Akna_furdo_06_1': [8.15, 9.7, 8.72, 10.4], 'Akna_furdo_06_2': [8.01, 16.205, 8.72, 16.82]},
  ajtok=dict([   # v2: a nyilas a terv falnyílása; a tok 4 cm (lásd README)
   ajto('Ajto_05_1', 'y', [6.915, 7.815], [6.055, 6.185], [6.055, 7.775], '-x', 0.82, '90/2,10', ['05.1', '07']),
   ajto('Ajto_05_2', 'y', [10.03, 10.93], [6.055, 6.185], [6.055, 10.89], '-x', 0.82, '90/2,10', ['05.2', '07']),
   ajto('Ajto_05_3', 'x', [6.245, 7.145], [12.63, 12.73], [7.105, 12.745], '+y', 0.82, '90/2,10', ['05.3 / 10.3', '07']),
   ajto('Ajto_furdo_06_2', 'x', [6.595, 7.345], [14.355, 14.455], [6.635, 14.465], '+y', 0.67, '75/2,10', ['06.2', '10.3']),
   ajto('Ajto_hth_06_1', 'y', [10.88, 11.63], [7.22, 7.32], [7.205, 11.59], '-x', 0.67, '75/2,10', ['06.1 (HTH)', '07'], 'kifelé, a közlekedőbe nyílik'),
   ajto('Ajto_furdo_08_09', 'y', [7.7, 8.45], [7.22, 7.32], [7.205, 8.41], '-x', 0.67, '75/2,10', ['08/09', '07'], 'kifelé, a közlekedőbe nyílik'),
   ajto('Ajto_bejarat', 'y', [2.95, 4.0], [8.25, 8.5], [8.35, 3.972], '-x', 0.994, '1,05/2,10', ['01', 'lépcsőház']),
  ]),
  ablakok={
   'Uvegfal_nappali': dict(tengely='y', f=[0.925, 4.575], b=[-0.28, -0.20], fal=[-0.30, 0.0], Hn=2.57, nevleges='3,65/2,57',
       uvegek=[[1.06, 1.762], [1.923, 2.625], [2.795, 4.45]],
       nyilo=[dict(nev='Erkelyajto_nappali_a', nyilas=[0.98, 1.843], zsaner=[-0.18, 0.98], irany='+x', r=0.863),
              dict(nev='Erkelyajto_nappali_b', nyilas=[1.843, 2.705], zsaner=[-0.18, 2.705], irany='+x', r=0.863)],
       szobak=['03-04'], megj='kétszárnyú erkélyajtó + fix mező'),
   'Ablak_05_1': dict(tengely='y', f=[6.93, 7.835], b=[3.04, 3.12], fal=[3.02, 3.32], Hn=2.57, nevleges='0,90/2,57',
       uvegek=[[7.065, 7.755]],
       nyilo=[dict(nev='Ablakszarny_05_1', nyilas=[6.985, 7.835], zsaner=[3.14, 7.835], irany='+x', r=0.85, tipus='ablak')],
       melyedes=[6.93, 7.89],   # v2: a belső mélyedés az oszlopig tart (az ablak és az oszlop között a tok síkjában kapcsolóprofil)
       szobak=['05.1'], megj='padlóig érő nyíló ablak (45°-os nyitásjel); előtte francia erkély korlát (terv: Lakatos Külső réteg; típus, magasság a terven nincs)'),
   'Ablak_05_2': dict(tengely='y', f=[8.105, 10.98], b=[3.04, 3.12], fal=[3.02, 3.32], Hn=2.57, nevleges='2,87/2,57',
       uvegek=[[8.185, 8.715], [8.875, 9.405], [9.625, 10.155], [10.315, 10.845]],
       nyilo=[dict(nev='Ablakszarny_05_2_a', nyilas=[8.105, 8.795], zsaner=[3.14, 8.105], irany='+x', r=0.69, tipus='ablak'),
              dict(nev='Ablakszarny_05_2_b', nyilas=[8.795, 9.485], zsaner=[3.14, 9.485], irany='+x', r=0.69, tipus='ablak'),
              dict(nev='Ablakszarny_05_2_c', nyilas=[9.545, 10.235], zsaner=[3.14, 9.545], irany='+x', r=0.69, tipus='ablak'),
              dict(nev='Ablakszarny_05_2_d', nyilas=[10.235, 10.925], zsaner=[3.14, 10.925], irany='+x', r=0.69, tipus='ablak')],
       melyedes=[8.05, 10.98],
       szobak=['05.2'], megj='két kétszárnyú, padlóig érő nyíló ablak; előtte francia erkély korlát (terv)'),
   'Ablak_05_3': dict(tengely='y', f=[13.01, 15.81], b=[3.04, 3.12], fal=[3.02, 3.32], Hn=2.57, nevleges='2,80/2,57',
       uvegek=[[13.145, 13.847], [14.007, 14.71], [14.93, 15.675]],
       nyilo=[dict(nev='Ablakszarny_05_3_a', nyilas=[13.065, 13.927], zsaner=[3.14, 13.065], irany='+x', r=0.862, tipus='ablak'),
              dict(nev='Ablakszarny_05_3_b', nyilas=[13.927, 14.79], zsaner=[3.14, 14.79], irany='+x', r=0.862, tipus='ablak'),
              dict(nev='Ablakszarny_05_3_c', nyilas=[14.85, 15.755], zsaner=[3.14, 15.755], irany='+x', r=0.905, tipus='ablak')],
       szobak=['05.3'], megj='kétszárnyú + egyszárnyú, padlóig érő nyíló ablak; előtte francia erkély korlát (terv)'),
  },
  szobak={
   'nappali_etkezo': ('03-04 ÉTKEZŐ-NAPPALI', 'parketta', [[0, 0, 5.80, 4.7], [5.80, 2.9, 7.22, 4.7], [0, 4.7, 3.22, 5.6], [-0.67, 5.0, 0, 5.6]]),
   'konyha': ('02 KONYHA', 'parketta', [[5.80, 0, 6.45, 2.8], [6.45, 0.6, 7.3, 2.8], [7.3, 0, 8.25, 2.8]]),   # 5,80 + 2,45 (méretszám)
   'eloter': ('01 ELŐTÉR', 'parketta', [[7.32, 2.9, 8.25, 4.575], [7.22, 2.9, 7.32, 4.1]]),   # v2: az EL4 előtétfal nélkül
   'kozlekedo': ('07 KÖZLEKEDŐ', 'parketta', [[6.17, 4.7, 7.22, 12.63]]),
   'kozlekedo_gardrob': ('07 KÖZLEKEDŐ (gardrób rész)', 'parketta', [[7.32, 4.8, 8.25, 6.3], [7.22, 4.8, 7.32, 5.6]]),   # v2: az átjáró padlója (a v1-ben hiányzott)
   '05_1': ('05.1 SZOBA', 'parketta', [[3.32, 4.8, 5.47, 7.89], [5.47, 5.7, 6.07, 7.89]]),
   '05_1_fulke': ('05.1 SZOBA (fülke a közlekedő felé)', 'parketta', [[5.57, 4.8, 6.17, 5.3]]),
   '05_2': ('05.2 SZOBA', 'parketta', [[3.32, 7.99, 6.07, 11.23]]),
   'gardrob_10_2': ('10.2 GARDRÓB', 'parketta', [[3.32, 11.23, 4.07, 11.33], [3.32, 11.33, 5.47, 12.63], [5.47, 11.33, 6.07, 11.9]]),   # v2: az átjáró a gardróbhoz (a terv m²-e így egyezik)
   '05_3': ('05.3 SZOBA', 'parketta', [[3.32, 12.73, 6.42, 16.82]]),
   'gardrob_10_3': ('10.3 GARDRÓB', 'parketta', [[6.42, 12.73, 8.72, 14.355]]),
   'furdo_06_2': ('06.2 FÜRDŐ', 'keramia', [[6.52, 14.455, 8.72, 16.205], [6.52, 16.205, 8.01, 16.82]]),
   'hth_06_1': ('06.1 FÜRDŐ (HTH)', 'keramia', [[7.32, 10.4, 8.72, 12.63], [7.32, 9.8, 8.15, 10.4]]),
   'furdo_08_09': ('08/09 FÜRDŐ', 'keramia', [[7.32, 6.4, 8.72, 9.7]]),
  },
  terv_m2={'Nappali+étkező': (33.85, ['nappali_etkezo']), 'Konyha': (6.35, ['konyha']), 'Előtér': (1.78, ['eloter']),
           'Közlekedő': (8.63, ['kozlekedo', '05_1_fulke']), 'Gardrób (közlekedő)': (1.48, ['kozlekedo_gardrob']),
           'Szoba (05.1)': (8.15, ['05_1']), 'Szoba (05.2)': (9.50, ['05_2']), 'Gardrób (10.2)': (3.21, ['gardrob_10_2']),
           'Szoba (05.3, gardróbbal)': (16.97, ['05_3', 'gardrob_10_3']), 'Fürdő (06.2)': (4.31, ['furdo_06_2']),
           'Ht.hg. (06.1)': (3.45, ['hth_06_1']), 'Fürdő (08/09)': (4.37, ['furdo_08_09'])},
  terv_ossz=102.05, erkely_m2=7.04,
  erkely=dict(lapok=[[-2.035, -1.025, -0.465, 2.34], [-1.15, 2.34, -0.465, 4.52]], z=-0.15,
              korlat=[['x', -2.03, -0.945, 2.31], ['y', 2.31, -2.035, -1.105], ['x', -1.105, 2.31, 4.52]],
              korlat_oszto=0.11,
              valaszfal=[[-1.955, -1.025, -0.51, -0.945]],   # v2: fém osztó (Lakatos Külső réteg), 1,445 × 0,08 m – közös az A-811-gyel
              megj='a kontúr a rajz erkélyvonalaiból (v2: a bal szél x −2,035 a 11. és a 12. oldalon is ki van rajzolva – igazolt); a korlát pálcás (terv, ≈ 11 cm osztás); '
                   'padlószint (−0,15 m) és korlátmagasság (1,10 m) a terven nincs, NEM IGAZOLT; fém osztó az A-811 erkélye felé, magassága a terven nincs'),
  francia_korlat=dict(x=[2.915, 2.935], hk=1.00, szakaszok=[[6.98, 7.955], [7.985, 9.50], [9.53, 10.93], [13.06, 13.91], [13.94, 14.805], [14.835, 15.76]],
                      megj='v2: francia erkély korlát a hálók padlóig érő ablakai előtt – a terven szerepel (Lakatos Külső réteg, 12. old.; a 11. old. 1:50-es lapja 10,29-nél levágva); '
                           'típus és magasság a terven nincs: semleges pálcás korlát, 1,00 m (NEM IGAZOLT)'),
  plafon=[[-0.97, -0.3, 8.5, 5.905], [3.02, 5.905, 9.02, 17.12], [8.5, 4.0, 9.02, 5.905]],
  kamerak={
   'Cam_02_Nappali_erkely': dict(loc=[5.5, 0.55, 1.5], cel=[0.0, 3.9, 1.25], statusz='ÖSSZEHASONLÍTÓ – B fázis (nappali → erkélyüveg)'),
   'Cam_03_Etkezo_konyha': dict(loc=[0.55, 4.5, 1.5], cel=[7.2, 0.9, 1.2], statusz='ÖSSZEHASONLÍTÓ – B fázis (ablak felől → étkező, konyha)'),
   'Cam_04_Haloszoba': dict(loc=[6.15, 13.05, 1.5], cel=[3.3, 15.9, 1.2], statusz='ÖSSZEHASONLÍTÓ – B fázis (05.3 háló)'),
   'Cam_05_Haloszoba_05_2': dict(loc=[5.85, 8.25, 1.5], cel=[3.3, 10.6, 1.2], statusz='kiegészítő nézet (05.2)'),
  },
 ),
}


# ------------------------------------------------------------------ PDF → falsávok
def falsavok(P):
    d = pymupdf.open(PDF); pg = d[P['page'] - 1]
    M = 72 / 25.4 * 1000 / P['scale']; X0, Y0 = P['X0'], P['Y0']
    tm = lambda p: ((p.x - X0) / M, (Y0 - p.y) / M)
    bx = P['box']; inb = lambda p: bx[0] <= p[0] <= bx[2] and bx[1] <= p[1] <= bx[3]
    V, Hh, hatch, dim = [], [], [], []
    for D in pg.get_drawings():
        c = D.get('color'); f = D.get('fill'); w = round(D.get('width') or 0, 2)
        if D['type'] == 's' and c is not None and tuple(round(v, 3) for v in c) == (0, 0, 0):
            for it in D['items']:
                if it[0] != 'l': continue
                a, b = tm(it[1]), tm(it[2])
                if not (inb(a) and inb(b)): continue
                if w in (0.71, 0.99):
                    if abs(a[0] - b[0]) < 0.003: V.append([round((a[0] + b[0]) / 2, 4), min(a[1], b[1]), max(a[1], b[1])])
                    elif abs(a[1] - b[1]) < 0.003: Hh.append([round((a[1] + b[1]) / 2, 4), min(a[0], b[0]), max(a[0], b[0])])
                elif w == 0.28:
                    dx, dy = abs(a[0] - b[0]), abs(a[1] - b[1])
                    if dx > 0.004 and dy > 0.004 and math.hypot(dx, dy) < 1.3:
                        hatch.append((min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])))
                    elif (dx < 0.002 or dy < 0.002) and dx + dy > 0.3: dim.append((a, b))
        elif D['type'] == 'f' and f is not None and tuple(round(v, 3) for v in f) == (0, 0, 0):
            r = D['rect']; a = tm(pymupdf.Point(r.x0, r.y1)); b = tm(pymupdf.Point(r.x1, r.y0))
            if inb(a) and inb(b) and (b[0] - a[0]) < 0.5 and (b[1] - a[1]) < 0.5: hatch.append((a[0], a[1], b[0], b[1]))

    def on_dim(h):  # méretvonal-jel: a méretvonalon ülő rövid ferde vonal – nem sraffozás
        mx, my = (h[0] + h[2]) / 2, (h[1] + h[3]) / 2
        for a, b in dim:
            if abs(a[1] - b[1]) < 0.002 and abs(my - a[1]) < 0.003 and min(a[0], b[0]) - 0.01 <= mx <= max(a[0], b[0]) + 0.01: return True
            if abs(a[0] - b[0]) < 0.002 and abs(mx - a[0]) < 0.003 and min(a[1], b[1]) - 0.01 <= my <= max(a[1], b[1]) + 0.01: return True
        return False
    hatch = [h for h in hatch if not on_dim(h)]

    def merge(L):
        L = sorted(L); out = []
        for c, a, b in L:
            if out and abs(out[-1][0] - c) < 0.002 and a <= out[-1][2] + 0.005: out[-1][2] = max(out[-1][2], b)
            else: out.append([c, a, b])
        return out

    def bands(lines, vertical):
        lines = merge(lines); res = []
        for c1, a1, b1 in lines:
            for c2, a2, b2 in lines:
                if not (0.035 <= c2 - c1 <= 0.75): continue
                lo, hi = max(a1, a2), min(b1, b2)
                if hi - lo < 0.03: continue
                if [l for l in lines if c1 + 0.008 < l[0] < c2 - 0.008 and min(hi, l[2]) - max(lo, l[1]) > 0.5 * (hi - lo)]: continue
                iv = []
                for h in hatch:
                    hx0, hy0, hx1, hy1 = (h if vertical else (h[1], h[0], h[3], h[2]))
                    if hx0 >= c1 - 0.006 and hx1 <= c2 + 0.006 and hy1 >= lo - 0.01 and hy0 <= hi + 0.01:
                        iv.append((max(lo, hy0), min(hi, hy1)))
                if not iv: continue
                iv.sort(); mg = []
                for s, e in iv:
                    if mg and s <= mg[-1][1] + 0.16: mg[-1][1] = max(mg[-1][1], e)
                    else: mg.append([s, e])
                for s, e in mg:
                    if s - lo < 0.16: s = lo
                    if hi - e < 0.16: e = hi
                    if e - s >= 0.03: res.append((c1, c2, round(s, 4), round(e, 4)))
        return res
    vb = bands(V, True); hb = bands(Hh, False)
    return [[c1, s, c2, e] for c1, c2, s, e in vb] + [[s, c1, e, c2] for c1, c2, s, e in hb], len(hatch)


def teglalapok(U):
    """ortogonális sokszög(ek) → nem átfedő téglalapok (rácscellák mohó összevonása, a hosszabb irány előnyben)"""
    polys = [U] if isinstance(U, Polygon) else list(U.geoms)
    rects = []
    for P in polys:
        pts = list(P.exterior.coords) + [c for i in P.interiors for c in i.coords]
        xs = sorted(set(round(c[0], 4) for c in pts)); ys = sorted(set(round(c[1], 4) for c in pts))
        nx, ny = len(xs) - 1, len(ys) - 1
        Pi = P.buffer(-1e-5)
        fill = [[Pi.contains(box(xs[i], ys[j], xs[i + 1], ys[j + 1]).centroid) for i in range(nx)] for j in range(ny)]
        used = [[False] * nx for _ in range(ny)]
        free = lambda j, i: fill[j][i] and not used[j][i]
        for j in range(ny - 1, -1, -1):
            for i in range(nx):
                if not free(j, i): continue
                i2 = i
                while i2 + 1 < nx and free(j, i2 + 1): i2 += 1
                j2 = j
                while j2 - 1 >= 0 and all(free(j2 - 1, k) for k in range(i, i2 + 1)): j2 -= 1
                j3 = j
                while j3 - 1 >= 0 and free(j3 - 1, i): j3 -= 1
                i3 = i
                while i3 + 1 < nx and all(free(k, i3 + 1) for k in range(j3, j + 1)): i3 += 1
                if (ys[j + 1] - ys[j3]) * (xs[i3 + 1] - xs[i]) > (xs[i2 + 1] - xs[i]) * (ys[j + 1] - ys[j2]): i2, j2 = i3, j3
                for jj in range(j2, j + 1):
                    for ii in range(i, i2 + 1): used[jj][ii] = True
                rects.append([xs[i], ys[j2], xs[i2 + 1], ys[j + 1]])
    return rects


def r3(v): return [round(x, 3) for x in v]


for flat, P in FL.items():
    B, nh = falsavok(P)
    keep = [r for r in B if not any(r[0] >= R[0] - 0.004 and r[1] >= R[1] - 0.004 and r[2] <= R[2] + 0.004 and r[3] <= R[3] + 0.004 for R in P['torol'])]
    U = unary_union([box(*r) for r in keep] + [box(*r) for r in P['hozzaad']])
    # nyílások és aknák kivonása (az aknák külön tárgyak)
    nyil = []
    for n, a in P['ajtok'].items():
        (a0, a1), (w0, w1) = a['nyilas'], a['fal_sik']
        nyil.append(box(a0, w0 - 0.01, a1, w1 + 0.01) if a['fal'] == 'x' else box(w0 - 0.01, a0, w1 + 0.01, a1))
    for n, w in P['ablakok'].items():
        f0, f1 = w['f']; x0, x1 = w['fal']
        nyil.append(box(x0 - 0.17, f0, x1 + 0.01, f1))
    U = U.difference(unary_union(nyil + [box(*r) for r in P['aknak'].values()]))
    U = unary_union([U] + [box(*r) for r in P['hozzaad_utana']])
    if P.get('kivon'): U = U.difference(unary_union([box(*r) for r in P['kivon']]))
    U = U.buffer(0.0005, join_style=2).buffer(-0.0005, join_style=2)
    rects = [r for r in teglalapok(U) if min(r[2] - r[0], r[3] - r[1]) >= 0.019]   # 2 cm alatti szilánk nélkül
    rects.sort(key=lambda r: (round(-r[3], 2), r[0]))
    walls = {}
    for i, r in enumerate(rects, 1):
        vast = min(r[2] - r[0], r[3] - r[1])
        walls[f"{'Kulso' if vast >= 0.2 else 'Fal'}_{i:02d}"] = r3(r)
    H = P['H']
    # szemöldökök
    szem = {}
    for n, a in P['ajtok'].items():
        (a0, a1), (w0, w1) = a['nyilas'], a['fal_sik']
        szem[f'{n}_szemoldok'] = r3([a0, w0, a['magassag'], a1, w1, H] if a['fal'] == 'x' else [w0, a0, a['magassag'], w1, a1, H])
    for n, w in P['ablakok'].items():
        f0, f1 = w['f']; x0, x1 = w['fal']
        szem[f'{n}_szemoldok'] = r3([x0, f0, w['Hn'], x1, f1, H])
    for n, r in P.get('szemoldok_extra', {}).items():
        szem[n] = r3(r + [H])
    # küszöbök (padló a nyílásban)
    kuszob = {}
    for n, a in P['ajtok'].items():
        if a['szobak'][-1] == 'lépcsőház': continue
        (a0, a1), (w0, w1) = a['nyilas'], a['fal_sik']
        anyag = 'keramia' if any(k in n for k in ('furdo', 'WC', 'HTH', 'hth')) else 'parketta'
        kuszob[f'P_kuszob_{n}'] = dict(r=r3([a0, w0, a1, w1] if a['fal'] == 'x' else [w0, a0, w1, a1]), anyag=anyag)
    # m² összevetés
    def area(rs): return unary_union([box(*r) for r in rs]).area
    def melyedes(k):   # a szobához csatlakozó ablakmélyedés (a tok belső síkja és a belső falsík között)
        s_ = 0.0
        for w in P['ablakok'].values():
            (f0, f1), (b0, b1), (x0, x1) = w['f'], w['b'], w['fal']
            m0, m1 = w.get('melyedes', w['f'])
            for r in P['szobak'][k][2]:
                if abs(r[0] - x1) < 0.002: s_ += max(0.0, min(m1, r[3]) - max(m0, r[1])) * (x1 - b1)
        return s_
    m2 = []
    for nev, (t, keys) in P['terv_m2'].items():
        a = sum(area(P['szobak'][k][2]) for k in keys); am = a + sum(melyedes(k) for k in keys)
        m2.append(dict(helyiseg=nev, terv_m2=t, modell_m2=round(a, 2), modell_m2_ablakmelyedessel=round(am, 2),
                       elteres_m2=round(am - t, 2), elteres_szazalek=round((am - t) / t * 100, 1), szobak=keys))
    # ellenőrzés: szobák nem fedik a falakat (1 cm²-nél nagyobb átfedés)
    WU = unary_union([box(*r) for r in rects] + [box(*r) for r in P['aknak'].values()] + [box(*r) for r in P.get('elotetfal', {}).values()])
    atfedes = {}
    for k, (rn, mat, rs) in P['szobak'].items():
        o = unary_union([box(*r) for r in rs]).intersection(WU).area
        if o > 0.0001: atfedes[k] = round(o, 4)
    # v2 – réskeresés (a független ellenőrzés nyomán): a falak, aknák, előtétfalak, nyílászárók, helyiségek, küszöbök és
    # ablakmélyedések alaprajzi uniójában a 6 cm-nél keskenyebb rést vagy lyukat keressük (morfológiai zárás, ±3 cm).
    # Ami itt megjelenik, az a modellben teljes magasságú rés vagy padlóhiány; a kimenetben listázva, 0 a cél.
    elemek = [box(*r) for r in rects] + [box(*r) for r in P['aknak'].values()] + [box(*r) for r in P.get('elotetfal', {}).values()]
    for n, a in P['ajtok'].items():
        (a0, a1), (w0, w1) = a['nyilas'], a['fal_sik']
        elemek.append(box(a0, w0, a1, w1) if a['fal'] == 'x' else box(w0, a0, w1, a1))
    for n, w in P['ablakok'].items():
        (f0, f1), (b0, b1), (x0, x1) = w['f'], w['b'], w['fal']; m0, m1 = w.get('melyedes', w['f'])
        elemek += [box(x0, f0, x1, f1) if x1 <= 0.01 else box(b0, f0, b1, f1), box(b1, m0, x1, m1)]
    for q in P.get('kapcsolo_profil', {}).values(): elemek.append(box(*q['r']))
    elemek += [box(*r) for v in P['szobak'].values() for r in v[2]]
    UE = unary_union(elemek)
    zart = UE.buffer(0.03, join_style=2).buffer(-0.03, join_style=2)
    rest = zart.difference(UE)
    # a lebegőpontos (< 3 mm vastag) szilánkok nem rések: vastagság ≈ 2 · terület / kerület
    resek = [r3(g.bounds) + [round(g.area, 5), round(2 * g.area / g.length, 4)] for g in (list(rest.geoms) if hasattr(rest, 'geoms') else [rest])
             if not g.is_empty and g.area > 2e-5 and 2 * g.area / g.length >= 0.003]
    out = dict(
        lakas=P['lakas'], verzio='geometria v2 – ELŐZETES (tervből, helyszínen nem mért; a független tervhűségi ellenőrzés javításaival)', datum='2026-10-24',
        forras=dict(pdf='WGR1_meretezett_alaprajzok.pdf (vevői adat, nincs a repóban)', pdf_sha256=SHA, oldal=P['page'],
                    leptek=f"1:{P['scale']}", rajz=P['verzio'], m2='2. old. megvalósulási terv 1:125 (2026.05.20.), illesztve',
                    padlo='burkolatkiosztási terv (A-811: 7. old., A-812: 14. old.)'),
        koordinata=dict(egyseg='m', x='rajzon jobbra', y='rajzon felfelé', origo='x=0: a nappali homlokzati belső falsíkja; y=0: '
                        + ('a 05.1 szoba rajzon alsó belső falsíkja' if flat == 'A811' else 'a nappali rajzon alsó belső falsíkja')
                        + ' – azonos a villamos JSON rendszerével', pt_per_m=round(72 / 25.4 * 1000 / P['scale'], 4), X0_pt=P['X0'], Y0_pt=P['Y0'],
                        tajolas='a rajz É-jele szerint a +y irány ≈ 53° (ÉK), a −x irány (a homlokzati üvegfal) ≈ ÉNy – tájékoztató',
                        szomszed='A-812: x közös, y_A812 = y_A811 − 11,85 (2. old. illesztés)'),
        H=H, H_forras=P['H_forras'], meretek='vakolatlan tervsíkok; a kész falsík oldalanként ~1–2 cm-rel beljebb lehet',
        walls=walls, aknak={k: r3(v) for k, v in P['aknak'].items()}, elotetfal={k: r3(v) for k, v in P.get('elotetfal', {}).items()},
        almennyezet=P.get('almennyezet', {}), kapcsolo_profil=P.get('kapcsolo_profil', {}), francia_korlat=P.get('francia_korlat'),
        szemoldok=szem, ajtok=P['ajtok'], ablakok=P['ablakok'],
        szobak={k: dict(nev=v[0], padlo=v[1], r=v[2]) for k, v in P['szobak'].items()}, kuszob=kuszob,
        padloanyag=dict(parketta=PARKETTA, keramia=KERAMIA), erkely=P['erkely'], erkely_terv_m2=P['erkely_m2'], plafon=P['plafon'],
        kamerak=P['kamerak'], m2_osszevetes=m2, terv_ossz_m2=P['terv_ossz'],
        modell_ossz_m2=round(sum(area(v[2]) for v in P['szobak'].values()), 2),
        modell_ossz_m2_ablakmelyedessel=round(sum(area(v[2]) + melyedes(k) for k, v in P['szobak'].items()), 2), szoba_fal_atfedes=atfedes,
        resek_6cm_alatt=resek,
        statusz=dict(falak_nyilasok='TERV SZERINT (vektoros rajzból)', belmagassag='HELYSZÍNEN MÉRT tartomány (Kémeri), modell: 2,70 m',
                     erkely='ELŐZETES – kontúr a rajzból, szint és korlát nem igazolt', szaniter='NINCS MODELLEZVE'))
    json.dump(out, open(os.path.join(HERE, f'{flat}_geometria_ELOZETES.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(flat, 'sávok', len(B), 'sraff', nh, '→ falak', len(walls), '| aknák', len(P['aknak']), '| ajtók', len(P['ajtok']), '| ablakok', len(P['ablakok']),
          '| szoba–fal átfedés', atfedes, '| rések (<6 cm):', len(resek))
    for r in resek: print('    RÉS', r)
    for m in m2: print('   ', m['helyiseg'].ljust(28), m['terv_m2'], '→', m['modell_m2'], '+ mélyedés →', m['modell_m2_ablakmelyedessel'], f"({m['elteres_m2']:+.2f} m², {m['elteres_szazalek']:+.1f}%)")
    print('    összesen terv', P['terv_ossz'], 'modell', out['modell_ossz_m2'], '(ablakmélyedéssel', out['modell_ossz_m2_ablakmelyedessel'], ')')
