# =====================================================================================
# A-902 geometria v2b – ALAPRAJZ SZERINTI CÉLZOTT JAVÍTÁS (2026-10-24)
# STÁTUSZ: ELŐZETES – tervből igazolt, helyszínen még NEM mért. Csak KÉZI futtatásra.
#
# Bemenet : 03_blender/WSG_A902_v2_terasz_ELOZETES_20261024.blend (MÁSOLAT; a bemenetet nem írja felül)
# Kimenet : 03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend  (új fájl)
#           03_blender/geometry_lock_A902_v2b.json                     (új lock, a v1 lock érintetlen)
#           03_blender/geometry_v2/v2b_valtozasok.json                 (minden módosítás: régi → új, bizonyíték, státusz)
# Élő fájl (~/Downloads/WSG_A902_stilusok.blend): NEM érinti.
#
# Elv (Péter, 2026-10-24): a meglévő modellt megtartjuk; csak a méretezett terv (18. old., 1:50, vektoros
# falvonalak: pdf_kinyeres/p18_falvonalak_m.json) által bizonyított eltéréseket javítjuk. A terasz/kert (v2),
# a bútorok és a stílusrétegek NEM változnak. Fotóból falméretet nem módosítunk.
# A terv méretei VAKOLATLAN falsíkra vonatkoznak; a kész falsík oldalanként ~1–2 cm-rel beljebb lehet (Kémeri: 05.1 3,548 vs 3,57).
#
# Futtatás (bpy 5.2.3, NEM a szkript mappájából):
#   WSG_KEZI_FUTTATAS=1 python3 -c "import sys,bpy; sys.argv=['x','<repo>/03_blender']; exec(open('<ez a fájl>').read())"
# =====================================================================================
import os as _os
if _os.environ.get("WSG_KEZI_FUTTATAS") != "1":
    raise SystemExit("v2b alaprajz-javító szkript – futtatás csak WSG_KEZI_FUTTATAS=1 mellett, Péter kérésére.")

import bpy, sys, os, json, datetime
from mathutils import Vector

B = sys.argv[-1]                                  # <repo>/03_blender
SRC = os.path.join(B, 'WSG_A902_v2_terasz_ELOZETES_20261024.blend')
OUT = os.path.join(B, 'WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend')
LOCK = os.path.join(B, 'geometry_lock_A902_v2b.json')
CHG = os.path.join(B, 'geometry_v2', 'v2b_valtozasok.json')
assert os.path.abspath(OUT) != os.path.abspath(SRC)
bpy.ops.wm.open_mainfile(filepath=SRC)

T = 'TERV SZERINT IGAZOLT'          # 18. old. vektoros falvonal + méretszám
TM = 'TERV SZERINT IGAZOLT + HELYSZÍNEN MÉRT'
F = 'FOTÓVAL ALÁTÁMASZTOTT'
E = 'ELŐZETES / MÉRENDŐ'
H = 2.90

# ---------------------------------------------------------------- falak: régi név → új befoglaló [x0,y0,z0,x1,y1,z1]
WALLS = {
 # nyugati homlokzat: falsík (x 0 / −0,30) egyezik; csak a nyílásokhoz igazodó végek és a 2,57-es nyílásmagasság
 'Kulso_Ny_szemoldok1': ([-0.30, 0.06, 2.57, 0.00, 1.94, H], T, '05.2 erkélyajtó 1,88/2,57; tok y 0,059–1,939'),
 'Kulso_Ny_1':          ([-0.30, 1.94, 0.00, 0.00, 4.28, H], T, 'nyílásvégek a tokvonalakhoz (1,939 / 4,274)'),
 'Kulso_Ny_szemoldok2': ([-0.30, 4.28, 2.57, 0.00, 7.92, H], T, '05.1 üvegfal 3,65/2,57; tok y 4,274–7,924'),
 'Kulso_Ny_2':          ([-0.30, 7.92, 0.00, 0.00, 8.95, H], T, 'tok y 7,924'),
 # bejárat: a bejárati fal y 0,60–0,85 (terv), a modellben y 0,35–0,65 volt
 'Kulso_D_eloter_sarok_0':    ([6.70, -0.30, 0.0, 6.95, 0.60, H], T, 'V 6,699 / 6,949 (y −0,31…0,60)'),
 'Kulso_D_eloter_0':          ([6.70, 0.60, 0.0, 7.30, 0.85, H], T, 'V 6,699 (…0,849); ajtótok 7,299 (y 0,599–0,849)'),
 'Kulso_D_eloter_szemoldok1': ([7.30, 0.60, 2.10, 8.35, 0.85, H], T, 'bejárati ajtó 1,05/2,10, tok 7,299–8,349'),
 'Kulso_D_eloter_1':          ([8.35, 0.60, 0.0, 8.60, 1.35, H], T, 'V 8,349 / 8,599 (y 0,60–1,35)'),
 # konyha
 'Kulso_tomb_eloter_konyha':  ([8.60, 1.10, 0.0, 9.10, 1.35, H], T, 'a 65 cm-es „tömb” helyett a konyha D-i fala: H 1,099 / 1,349'),
 'Kulso_D_konyha_0':          ([9.10, 1.10, 0.0, 10.85, 1.35, H], T, 'H 1,099 / 1,349 (x 8,60–10,55)'),
 'Beepitett_szekreny_eloter': ([8.95, 1.35, 0.0, 9.05, 2.35, H], T, 'a tömör „szekrénytömb” helyett a fülke K-i fala: V 8,949 / 9,049; a fülke az előtér felé nyitott'),
 'Fal_konyha_Ny_0':           ([8.35, 2.35, 0.0, 8.45, 4.05, 0.85], T, 'V 8,348 / 8,448 (y 2,35–4,05); −10 cm; MAGASSÁG 0,85 m: a terven „pm.:85.0 cm”, a módosítás szerint „pengefal helyett 85 cm magas, erősített gipszkarton fal” (M1 KORR 2)'),
 'Kulso_K_konyha_05_3_0':     ([10.55, 1.10, 0.0, 10.85, 4.10, H], T, 'konyha K-i fala: V 10,549 / 10,849; −9 cm a belső síkon'),
 'Kulso_K_konyha_05_3_szemoldok1': ([10.75, 6.05, 2.10, 10.85, 6.95, H], T, '05.3 ajtó 90/2,10, tok y 6,049–6,949'),
 'Kulso_K_konyha_05_3_1':     ([10.75, 6.95, 0.0, 10.85, 7.025, H], T, 'nappali|05.3 válaszfal 10 cm: V 10,749 / 10,849'),
 'Akna_etkezo_05_3':          ([9.80, 7.025, 0.0, 11.10, 8.05, H], T, 'akna: V 9,799 / 11,099, H 7,024; pillér 10,80–11,10 a 05.3 ÉNy-i sarkában'),
 # 05.3 / 06.2
 'Kulso_D_05_3_06_2_0':       ([10.85, 3.85, 0.0, 16.70, 4.10, H], T, 'H 3,849 / 4,099 (05.3 D-i belső sík +6 cm)'),
 'Akna_06_2':                 ([15.00, 4.10, 0.0, 16.40, 5.20, H], T, 'gépészeti tömb: V 14,999…16,399, H 4,099 / 5,199; a 14,37–15,00 sáv a 05.3 fülkéje'),
 'Kulso_K_06_2_0':            ([16.40, 4.10, 0.0, 16.70, 8.35, H], T, 'V 16,399 / 16,699; −10 cm'),
 'Fal_05_3_06_2_0':           ([14.375, 5.10, 0.0, 14.475, 6.30, H], T, 'V 14,374 / 14,474; −12,6 cm'),
 'Fal_05_3_06_2_szemoldok1':  ([14.375, 6.30, 2.10, 14.475, 7.05, H], T, '06.2 ajtó 75/2,10, tok y 6,299–7,049'),
 'Fal_05_3_06_2_1':           ([14.375, 7.05, 0.0, 14.475, 8.05, H], T, 'V 14,374 / 14,474'),
 # északi (terasz) homlokzat: belső sík 7,97 → 8,05 (+8 cm), nyílásmagasság 2,53
 'Kulso_E_terasz_0':          ([3.32, 8.05, 0.0, 4.38, 8.35, H], T, 'H 8,049 / 8,349; nyílás falazott kávája 4,379'),
 'Kulso_E_terasz_szemoldok1': ([4.38, 8.05, 2.53, 9.00, 8.35, H], T, 'nappali üvegfal 4,50/2,53; káva 4,379–8,999'),
 'Kulso_E_terasz_1':          ([9.00, 8.05, 0.0, 12.00, 8.35, H], T, 'H 8,049 / 8,349; káva 8,999 / 11,999'),
 'Kulso_E_terasz_szemoldok2': ([12.00, 8.05, 2.53, 13.92, 8.35, H], T, '05.3 teraszajtó 1,80/2,53; káva 11,999–13,919'),
 'Kulso_E_terasz_2':          ([13.92, 8.05, 0.0, 16.70, 8.35, H], T, 'H 8,049 / 8,349'),
 'Pillér_05_1_EK':            ([3.02, 8.04, 0.0, 3.32, 9.25, H], T, 'V 3,019 / 3,319, H 8,039'),
 # 05.1 / közlekedő / 05.2 / 06.1
 'Fal_05_1_nappali_0':        ([3.57, 4.05, 0.0, 3.67, 8.05, H], TM, 'V 3,569 / 3,669; méretszám 3,57 és 7,08; Kémeri 05.1 = 3,548 (vakolt)'),
 'Fal_eloszoba_E_05_1ajto_0': ([2.42, 3.95, 0.0, 2.594, 4.05, H], T, '05.1 ajtótok 2,594'),
 'Fal_eloszoba_E_05_1ajto_szemoldok1': ([2.594, 3.95, 2.10, 3.494, 4.05, H], T, '05.1 ajtó 90/2,10, tok x 2,594–3,494'),
 'Fal_eloszoba_E_05_1ajto_1': ([3.494, 3.95, 0.0, 3.67, 4.05, H], T, 'tok 3,494 → válaszfal 3,669'),
 'Fal_eloszoba_Ny_0':         ([2.42, 2.65, 0.0, 2.52, 3.95, H], T, 'V 2,419 / 2,519'),
 'Fal_eloszoba_D_05_2ajto_0': ([2.42, 2.65, 0.0, 2.674, 2.75, H], T, 'H 2,649 / 2,749 (+10 cm); 05.2 ajtótok 2,674'),
 'Fal_eloszoba_D_05_2ajto_szemoldok1': ([2.674, 2.65, 2.10, 3.574, 2.75, H], T, '05.2 ajtó 90/2,10, tok x 2,674–3,574'),
 'Fal_eloszoba_D_05_2ajto_1': ([3.574, 2.65, 0.0, 3.75, 2.75, H], T, 'tok 3,574'),
 'Fal_05_2_furdo_0':          ([3.65, 0.00, 0.0, 3.75, 2.65, H], T, 'V 3,649 / 3,749; méretszám 3,65 és 1,75'),
 'Fal_furdo_E_0':             ([3.75, 2.65, 0.0, 3.824, 2.75, H], T, '06.1 ajtótok 3,824'),
 'Fal_furdo_E_szemoldok1':    ([3.824, 2.65, 2.10, 4.574, 2.75, H], T, '06.1 ajtó 75/2,10, tok x 3,824–4,574'),
 'Fal_furdo_E_1':             ([4.574, 2.65, 0.0, 5.60, 2.75, H], T, 'H 2,649 / 2,749 (x 4,574–5,599)'),
 'Fal_furdo_wc_K_0':          ([5.50, 0.00, 0.0, 5.60, 2.75, H], T, 'V 5,499 / 5,599 (y 0–2,75); +5 cm; északon nem folytatódik'),
 'Pillér_kozlekedo':          ([5.00, 2.95, 0.0, 5.20, 3.45, H], T, 'H 2,949 / 3,449, V 4,999; a 30-as méretszám a pillér + fal'),
 'Fal_wc_D_0':                ([5.60, 2.00, 0.0, 5.774, 2.10, H], T, 'H 1,999 / 2,099 (+5 cm); WC-ajtótok 5,774'),
 'Fal_wc_D_szemoldok1':       ([5.774, 2.00, 2.10, 6.524, 2.10, H], T, 'WC-ajtó 75/2,10, tok x 5,774–6,524'),
 'Fal_wc_D_1':                ([6.524, 2.00, 0.0, 6.60, 2.10, H], T, 'tok 6,524 → akna 6,599'),
 'Akna_WC_gepeszet':          ([6.60, 2.00, 0.0, 7.30, 3.95, H], T, 'V 6,599 / 7,299, H 1,999 / 3,949; K-i sík −10 cm (az átjáró 1,05 marad)'),
 'Fal_wc_E_nappali_0':        ([5.20, 3.95, 0.0, 7.30, 4.05, H], T, 'H 3,949 / 4,049 (x 5,20–7,30)'),
 'Szemoldok_atjaro_eloter_nappali': ([7.30, 3.95, 2.10, 8.45, 4.05, H], E, 'átjáró x 7,30–8,35 a terv szerint; a 2,10-es szemöldök a v1 brosúrából – NEM igazolt'),
}
NEW_WALLS = {  # új név: (sablon, bbox, státusz, bizonyíték)
 'Fal_kozlekedo_wc_v2b':      ('Fal_furdo_wc_K_0', [5.20, 2.75, 0.0, 5.30, 4.05, H], T, 'V 5,199 / 5,299 (y 2,75–4,05) – közlekedő|WC fal; a WC É-i része 1,30 széles (méretszám)'),
 'Akna_WC_gepeszet_b_v2b':    ('Akna_WC_gepeszet', [6.45, 3.25, 0.0, 6.60, 3.95, H], T, 'V 6,449, H 3,249 – a WC L-alakja (ÉK-i sarok)'),
 'Fal_szekrenyfulke_E_v2b':   ('Beepitett_szekreny_eloter', [8.35, 2.25, 0.0, 9.05, 2.35, H], T, 'H 2,249 / 2,349 (x 8,35–9,05) – az előtéri fülke É-i fala'),
 'Fal_konyha_K_csonk_v2b':    ('Kulso_K_konyha_05_3_0', [10.55, 4.10, 0.0, 10.85, 5.05, H], T, 'V 10,549 / 10,849, H 4,099 / 5,049 – gépészeti csonk + szerelt GK technikai fal (elszívó)'),
 'Fal_nappali_05_3_v2b_0':    ('Kulso_K_konyha_05_3_1', [10.75, 5.05, 0.0, 10.85, 6.05, H], T, 'V 10,749 / 10,849 (y 5,06–6,05)'),
 'Fal_06_2_D_v2b':            ('Fal_05_3_06_2_0', [14.375, 5.10, 0.0, 15.00, 5.20, H], T, 'H 5,099 / 5,199 – 06.2 D-i fala = a 05.3 DK-i fülke É-i fala'),
}

# ---------------------------------------------------------------- nyílászárók
def door_boxes(axis, a0, a1, w0, w1):
    """axis='x': a fal x mentén fut (az ajtó x-ben a0..a1, a fal y-vastagsága w0..w1); 'y': fordítva."""
    wc = (w0 + w1) / 2
    if axis == 'x':
        return {'tok_b': [a0, w0, 0, a0 + .03, w1, 2.10], 'tok_j': [a1 - .03, w0, 0, a1, w1, 2.10],
                'tok_f': [a0, w0, 2.07, a1, w1, 2.10], 'lap': [a0 + .03, wc - .02, 0, a1 - .03, wc + .02, 2.08]}
    return {'tok_b': [w0, a0, 0, w1, a0 + .03, 2.10], 'tok_j': [w0, a1 - .03, 0, w1, a1, 2.10],
            'tok_f': [w0, a0, 2.07, w1, a1, 2.10], 'lap': [wc - .02, a0 + .03, 0, wc + .02, a1 - .03, 2.08]}
DOORS = {  # ajtó: (tengely, nyílás a0..a1, fal w0..w1, bizonyíték)
 'Ajto_05_1':       ('x', 2.594, 3.494, 3.95, 4.05, 'tok x 2,594–3,494 (−3,6 cm)'),
 'Ajto_05_2':       ('x', 2.674, 3.574, 2.65, 2.75, 'tok x 2,674–3,574 (+4,4 cm), fal +10 cm'),
 'Ajto_furdo_06_1': ('x', 3.824, 4.574, 2.65, 2.75, 'tok x 3,824–4,574 (−12,6 cm)'),
 'Ajto_WC':         ('x', 5.774, 6.524, 2.00, 2.10, 'tok x 5,774–6,524 (+7,4 cm)'),
 'Ajto_bejarat':    ('x', 7.30, 8.35, 0.60, 0.85, 'tok x 7,299–8,349 (egyezik), fal y 0,60–0,85 (+25 cm)'),
 'Ajto_05_3':       ('y', 6.05, 6.95, 10.75, 10.85, 'tok y 6,049–6,949 (−5 cm), fal 10,75–10,85'),
 'Ajto_06_2':       ('y', 6.30, 7.05, 14.375, 14.475, 'tok y 6,299–7,049 (+25 cm)'),
}
def win_boxes(axis, f0, f1, b0, b1, Hn, mull):
    """Homlokzati üvegfal: tok f0..f1, tokszalag (fal-vastagság irányban) b0..b1, magasság Hn; mull = osztók középvonala."""
    g0, g1 = b0 + (b1 - b0) * 0.33, b0 + (b1 - b0) * 0.67
    def bx(a0, a1, c0, c1, z0, z1):
        return [a0, c0, z0, a1, c1, z1] if axis == 'x' else [c0, a0, z0, c1, a1, z1]
    d = {'also': bx(f0, f1, b0, b1, 0, .05), 'felso': bx(f0, f1, b0, b1, Hn - .05, Hn),
         'uveg': bx(f0, f1, g0, g1, .02, Hn - .03)}
    d['profil_szelek'] = [bx(f0 - .03, f0 + .03, b0, b1, 0, Hn), bx(f1 - .03, f1 + .03, b0, b1, 0, Hn)]
    d['osztok'] = [bx(m - .03, m + .03, b0, b1, 0, Hn) for m in mull]
    return d
WINDOWS = {  # (tengely, tok f0..f1, tokszalag b0..b1, magasság, osztók, meglévő profilnevek sorrendben, új osztók nevei, bizonyíték)
 'Uvegfal_nappali_terasz': ('x', 4.44, 8.94, 8.21, 8.33, 2.53, [6.257, 7.949],
     ['profil0', 'profil3'], ['profil1', 'profil2'], [], 'tok 4,44–8,939 (4,50 ✓), osztók 6,217–6,297 és 7,909–7,989, tolóajtó (nyíl); 2,53'),
 'Uvegfal_05_3_terasz':    ('x', 12.06, 13.86, 8.21, 8.33, 2.53, [12.935],
     ['profil0', 'profil2'], ['profil1'], [], 'tok 12,06–13,859 (1,80 ✓), osztó ~12,86–13,03, nyíló szárny (nyitásív); 2,53'),
 'Uvegfal_05_1_erkely':    ('y', 4.28, 7.92, -0.28, -0.20, 2.57, [5.184, 6.084],
     ['profil0', 'profil2'], ['profil1'], ['profil_v2b_5184'], 'tok 4,274–7,924 (3,65 ✓), osztók 5,124–5,244 és 6,024–6,144, nyíló szárny D-en; 2,57'),
 'Erkelyajto_05_2':        ('y', 0.06, 1.94, -0.28, -0.20, 2.57, [1.029],
     ['profil0', 'profil1'], [], ['profil_v2b_1029'], 'tok 0,059–1,939 (1,88 ✓), osztó 0,969–1,089, nyíló szárny É-on; 2,57'),
}
OPENINGS_META = {  # nyílástípus, nyitás (a validátor nyitási negyedköre), forrás: 18. old. nyitásívek
 'Ajto_05_1':       dict(tipus='nyilo', fal='x', nyilas=[2.594, 3.494], fal_sik=[3.95, 4.05], irany='+y', zsaner=[3.494, 4.05], r=0.90),
 'Ajto_05_2':       dict(tipus='nyilo', fal='x', nyilas=[2.674, 3.574], fal_sik=[2.65, 2.75], irany='-y', zsaner=[3.574, 2.65], r=0.90),
 'Ajto_furdo_06_1': dict(tipus='nyilo', fal='x', nyilas=[3.824, 4.574], fal_sik=[2.65, 2.75], irany='-y', zsaner=[3.824, 2.65], r=0.75),
 'Ajto_WC':         dict(tipus='nyilo', fal='x', nyilas=[5.774, 6.524], fal_sik=[2.00, 2.10], irany='-y', zsaner=[5.774, 2.00], r=0.75),
 'Ajto_bejarat':    dict(tipus='nyilo', fal='x', nyilas=[7.30, 8.35], fal_sik=[0.60, 0.85], irany='+y', zsaner=[8.35, 0.85], r=1.05),
 'Ajto_05_3':       dict(tipus='nyilo', fal='y', nyilas=[6.05, 6.95], fal_sik=[10.75, 10.85], irany='+x', zsaner=[10.85, 6.95], r=0.90),
 'Ajto_06_2':       dict(tipus='nyilo', fal='y', nyilas=[6.30, 7.05], fal_sik=[14.375, 14.475], irany='-x', zsaner=[14.375, 7.05], r=0.75),
 'Erkelyajto_05_2': dict(tipus='nyilo+fix', fal='y', nyilas=[1.03, 1.94], fal_sik=[-0.30, 0.0], irany='+x', zsaner=[0.0, 1.03], r=0.91, megj='nyíló szárny az É-i fél; zsanér D-en (nyitásív)'),
 'Uvegfal_05_1_erkely': dict(tipus='nyilo+fix', fal='y', nyilas=[4.28, 5.18], fal_sik=[-0.30, 0.0], irany='+x', zsaner=[0.0, 4.28], r=0.90, megj='nyíló szárny a D-i vég; zsanér D-en (nyitásív)'),
 'Uvegfal_05_3_terasz': dict(tipus='nyilo+fix', fal='x', nyilas=[12.06, 12.90], fal_sik=[8.05, 8.35], irany='-y', zsaner=[12.06, 8.05], r=0.84, megj='nyíló szárny Ny-on (nyitásív); a „mind tolóajtó” leírás téves'),
 'Uvegfal_nappali_terasz': dict(tipus='tolo', fal='x', nyilas=[4.44, 8.94], fal_sik=[8.05, 8.35], irany='-y', zsaner=None, r=0.0, megj='tolóajtó (nyíl); osztás a terv szerint, a ME-BAL-045 fotó eltérőnek tűnhet → helyszínen ellenőrizendő'),
}

# ---------------------------------------------------------------- padlók és helyiségek
FLOORS = {
 'P_05_1':               [0.00, 3.45, 3.57, 8.05], 'P_05_1_eszaki': [0.00, 8.05, 3.02, 8.95],
 'P_05_2':               [0.00, 0.00, 3.65, 2.65], 'P_05_2_gardrob': [0.00, 2.65, 2.42, 3.35],
 'P_05_3':               [10.85, 4.10, 14.375, 8.05],
 'P_eloszoba_kozlekedo': [2.52, 2.75, 5.20, 4.05],
 'P_eloter':             [5.60, 0.00, 6.70, 2.00], 'P_eloter_atjaro': [7.30, 2.00, 8.35, 4.05],
 'P_furdo_06_1':         [3.75, 0.00, 5.50, 2.65], 'P_furdo_06_2': [14.475, 5.20, 16.40, 8.05],
 'P_konyha':             [8.45, 1.35, 10.55, 4.05], 'P_nappali_etkezo': [3.67, 4.05, 10.75, 8.05],
 'P_wc':                 [5.60, 2.10, 6.60, 3.95],
}
NEW_FLOORS = {
 'P_eloter_b_v2b':      ('P_eloter', [6.70, 0.85, 8.35, 2.00], 'előtér K-i része (a bejárati fal mögött)'),
 'P_eloter_fulke_v2b':  ('P_eloter', [8.35, 1.35, 8.95, 2.25], 'előtéri fülke (a tömör „szekrénytömb” helyén; funkció ELŐZETES)'),
 'P_05_3_fulke_v2b':    ('P_05_3', [14.375, 4.10, 15.00, 5.10], '05.3 DK-i fülke'),
 'P_wc_b_v2b':          ('P_wc', [5.30, 2.75, 5.60, 3.95], 'WC É-i része 1,30 széles (L-alak)'),
}
ROOMS = {  # téglalap-unió, vakolatlan tervsíkok
 '05_2': [[0, 0, 3.65, 2.65]], '05_2_gardrob': [[0, 2.65, 2.42, 3.35]],
 '05_1': [[0, 3.45, 2.42, 3.95], [0, 3.95, 3.57, 8.05]], '05_1_eszaki': [[0, 8.05, 3.02, 8.95]],
 'kozlekedo': [[2.52, 2.75, 5.00, 3.95], [5.00, 2.75, 5.20, 2.95], [5.00, 3.45, 5.20, 3.95]],
 'nappali_etkezo': [[3.67, 4.05, 10.55, 5.05], [3.67, 5.05, 10.75, 7.025], [3.67, 7.025, 9.80, 8.05], [3.67, 3.95, 5.20, 4.05]],
 'konyha': [[9.05, 1.35, 10.55, 2.35], [8.45, 2.35, 10.55, 4.05]],
 'eloter': [[5.60, 0.00, 6.70, 2.00], [6.70, 0.85, 8.35, 2.00], [8.35, 1.35, 8.95, 2.25]],
 'eloter_atjaro': [[7.30, 2.00, 8.35, 4.05]],
 'wc': [[5.60, 2.10, 6.60, 2.75], [5.30, 2.75, 6.60, 3.25], [5.30, 3.25, 6.45, 3.95]],
 'furdo_06_1': [[3.75, 0, 5.50, 2.65]],
 '05_3': [[10.85, 4.10, 14.375, 7.025], [11.10, 7.025, 14.375, 8.05], [14.375, 4.10, 15.00, 5.10]],
 'furdo_06_2': [[14.475, 5.20, 16.40, 8.05]],
}
ROOM_TERV_M2 = {'05_2': 11.66, '05_1': 19.58, 'kozlekedo': 3.23, 'nappali_etkezo': 27.87, 'konyha': 5.24, 'eloter': 6.98,
                'wc': 1.88, 'furdo_06_1': 4.46, '05_3': 14.65, 'furdo_06_2': 4.39}
TERRACE_ZONES = {  # a v2 kertből (változatlan) – bútor csak gresen/WPC-n
 'gres_Ny': dict(r=[3.44, 8.5, 9.29, 12.4], z=-0.15, butorozhato=True), 'gres_K': dict(r=[11.39, 8.5, 16.27, 12.4], z=-0.15, butorozhato=True),
 'WPC_kozepso': dict(r=[9.29, 8.5, 11.39, 12.4], z=0.47, butorozhato=True), 'WPC_harant': dict(r=[3.44, 12.4, 16.27, 13.41], z=0.47, butorozhato=True),
 'WPC_nyelv': dict(r=[9.29, 13.41, 11.39, 14.46], z=0.47, butorozhato=True, megj='bejárata a modellben szegéllyel zárt – MÉRENDŐ'),
 'WPC_panorama': dict(r=[7.62, 18.95, 11.42, 19.79], z=0.47, butorozhato=True, megj='megközelítése nincs modellezve – MÉRENDŐ'),
 'zoldteto': dict(r=[3.71, 13.41, 16.04, 19.80], z=0.77, butorozhato=False, megj='terhelhetőség HIÁNYZIK'),
 'erkely_13': dict(r=[-2.01, -0.20, -0.30, 5.69], z=-0.15, butorozhato=True), 'erkely_13_nyulvany': dict(r=[-1.12, 5.69, -0.30, 7.90], z=-0.15, butorozhato=True),
}

# ---------------------------------------------------------------- segédfüggvények
def wb(o):
    M = o.matrix_world
    pts = [M @ v.co for v in o.data.vertices]
    return [min(p[i] for p in pts) for i in range(3)] + [max(p[i] for p in pts) for i in range(3)]
def r3(b): return [round(v, 3) for v in b]
def set_bbox(o, nb):
    M = o.matrix_world; Mi = M.inverted()
    pts = [M @ v.co for v in o.data.vertices]
    ob = wb(o)
    for v, p in zip(o.data.vertices, pts):
        q = []
        for i in range(3):
            span = ob[i + 3] - ob[i]
            t = (p[i] - ob[i]) / span if span > 1e-9 else 0.0
            q.append(nb[i] + t * (nb[i + 3] - nb[i]))
        v.co = Mi @ Vector(q)
    o.data.update()
def new_like(src, name, nb, coll=None):
    s = bpy.data.objects[src]
    o = s.copy(); o.data = s.data.copy(); o.name = name; o.data.name = name
    (coll or s.users_collection[0]).objects.link(o)
    set_bbox(o, nb); return o

log = []
def rec(kind, name, old, new, status, ev):
    log.append(dict(tipus=kind, nev=name, regi=r3(old) if old else None, uj=r3(new), statusz=status, bizonyitek=ev))

# ---------------------------------------------------------------- 1) falak
for n, (nb, st, ev) in WALLS.items():
    o = bpy.data.objects[n]; old = wb(o); set_bbox(o, nb); rec('fal', n, old, nb, st, ev)
for n, (src, nb, st, ev) in NEW_WALLS.items():
    new_like(src, n, nb); rec('új fal', n, None, nb, st, ev)

# ---------------------------------------------------------------- 2) ajtók (tok + lap a falvastagsághoz)
for d, (ax, a0, a1, w0, w1, ev) in DOORS.items():
    for part, nb in door_boxes(ax, a0, a1, w0, w1).items():
        o = bpy.data.objects[f'{d}_{part}']; old = wb(o); set_bbox(o, nb); rec('ajtó', o.name, old, nb, T, ev)

# ---------------------------------------------------------------- 3) homlokzati üvegfalak
for w, (ax, f0, f1, b0, b1, Hn, mull, edge_names, mull_names, new_mull_names, ev) in WINDOWS.items():
    bx = win_boxes(ax, f0, f1, b0, b1, Hn, mull)
    for part in ('also', 'felso', 'uveg'):
        o = bpy.data.objects[f'{w}_{part}']; old = wb(o); set_bbox(o, bx[part]); rec('üvegfal', o.name, old, bx[part], T, ev)
    for pn, nb in zip(edge_names, bx['profil_szelek']):
        o = bpy.data.objects[f'{w}_{pn}']; old = wb(o); set_bbox(o, nb); rec('üvegfal', o.name, old, nb, T, ev)
    osztok = list(bx['osztok'])
    for pn in mull_names:
        nb = osztok.pop(0); o = bpy.data.objects[f'{w}_{pn}']; old = wb(o); set_bbox(o, nb); rec('üvegfal', o.name, old, nb, T, ev)
    for pn in new_mull_names:
        nb = osztok.pop(0); new_like(f'{w}_{edge_names[0]}', f'{w}_{pn}', nb); rec('új osztó', f'{w}_{pn}', None, nb, T, ev)
    assert not osztok, w

# ---------------------------------------------------------------- 4) padlók
for n, r in FLOORS.items():
    o = bpy.data.objects[n]; old = wb(o); nb = [r[0], r[1], -0.02, r[2], r[3], 0.0]; set_bbox(o, nb); rec('padló', n, old, nb, T, 'helyiség a tervi falsíkok között')
for n, (src, r, ev) in NEW_FLOORS.items():
    nb = [r[0], r[1], -0.02, r[2], r[3], 0.0]; new_like(src, n, nb); rec('új padló', n, None, nb, T, ev)

# ---------------------------------------------------------------- 5) anyagok (fotóval alátámasztott meglévő felületek)
def mat(name, rgb, rough):
    m = bpy.data.materials.get(name) or bpy.data.materials.new(name)
    m.use_nodes = True
    b = m.node_tree.nodes.get('Principled BSDF')
    b.inputs['Base Color'].default_value = (*rgb, 1); b.inputs['Roughness'].default_value = rough
    return m
m_profil = mat('v2b_nyilaszaro_profil_belul_feher', (0.80, 0.80, 0.79), 0.45)
m_lap = mat('v2b_belteri_ajtolap_vilagosszurke', (0.50, 0.51, 0.52), 0.5)
m_tok = mat('v2b_belteri_ajtotok_szurke', (0.42, 0.43, 0.44), 0.5)
m_bej = mat('v2b_bejarati_ajto_belul_feher', (0.80, 0.80, 0.79), 0.5)
mat_log = []
for o in bpy.data.collections['A902_Nyilaszarok'].objects:
    for s in o.material_slots:
        if not s.material: continue
        n = o.name
        if (n.startswith('Uvegfal_') or n.startswith('Erkelyajto_')) and s.material.name == 'Fekete_fem':
            s.material = m_profil; mat_log.append((n, 'belül fehér profil'))
        elif n.startswith('Ajto_bejarat'):
            s.material = m_bej; mat_log.append((n, 'bejárati ajtó belül fehér'))
        elif n.startswith('Ajto_') and n.endswith('_lap'):
            s.material = m_lap; mat_log.append((n, 'világosszürke ajtólap'))
        elif n.startswith('Ajto_') and '_tok_' in n:
            s.material = m_tok; mat_log.append((n, 'szürke tok'))
for mn in ('Fal_feher', 'Plafon_feher'):
    m = bpy.data.materials.get(mn)
    if m and m.use_nodes:
        b = m.node_tree.nodes.get('Principled BSDF')
        old = tuple(round(c, 3) for c in b.inputs['Base Color'].default_value[:3])
        b.inputs['Base Color'].default_value = (0.80, 0.80, 0.80, 1); mat_log.append((mn, f'semleges fehér (régi {old})'))
pm = bpy.data.materials.get('v2_parketta_GreyTreviso_EL2184_foto')
for n in pm.node_tree.nodes:
    if n.type == 'VALTORGB':
        e = n.color_ramp.elements
        e[0].color = (0.140, 0.128, 0.116, 1); e[-1].color = (0.215, 0.198, 0.180, 1)
        mat_log.append(('v2_parketta_GreyTreviso_EL2184_foto', 'szürkésbarna tónus a ME-BAL-080 fotóhoz (deszkaminta NINCS modellezve)'))

# ---------------------------------------------------------------- 6) kamerák (változatlanok) – teljes paraméterlap a lockba
sc = bpy.context.scene
def cam_params(o):
    c = o.data
    return dict(tipus=c.type, lens_mm=round(c.lens, 3), sensor_width=round(c.sensor_width, 3), sensor_height=round(c.sensor_height, 3),
                sensor_fit=c.sensor_fit, shift_x=round(c.shift_x, 4), shift_y=round(c.shift_y, 4), clip_start=round(c.clip_start, 4),
                clip_end=round(c.clip_end, 2), ortho_scale=round(c.ortho_scale, 3), dof=bool(c.dof.use_dof),
                loc=[round(v, 4) for v in o.location], rot=[round(v, 4) for v in o.rotation_euler], rot_mode=o.rotation_mode,
                scale=[round(v, 4) for v in o.scale], parent=o.parent.name if o.parent else None)
CAM_STATUS = {
 'Cam_01_Felulnezet': 'ellenőrző felülnézet', 'Cam_02_Nappali_terasz': 'ÖSSZEHASONLÍTÓ – B fázis', 'Cam_03_Etkezo_konyha': 'ÖSSZEHASONLÍTÓ – B fázis',
 'Cam_04_Master': 'ÖSSZEHASONLÍTÓ – B fázis', 'Cam_05_Terasz': 'ELAVULT (régi sík teraszra; évelőágyás fölé esik) – nem használandó',
 'Cam_06_Alaprajz_lakas': 'ellenőrző alaprajz', 'Cam_07_Terasz_v2_greslaprol': 'ELŐZETES terasznézet (16 mm, z 1,45 = 1,60 a gres fölött)',
 'Cam_08_Terasz_v2_madarnezet': 'ellenőrző madártávlat', 'Cam_09_Terasz_v2_felulnezet': 'ellenőrző felülnézet'}
cams = {o.name: dict(cam_params(o), statusz=CAM_STATUS.get(o.name, 'nincs besorolva')) for o in bpy.data.objects if o.type == 'CAMERA'}
render = dict(resolution_x=sc.render.resolution_x, resolution_y=sc.render.resolution_y, percentage=sc.render.resolution_percentage,
              pixel_aspect=[sc.render.pixel_aspect_x, sc.render.pixel_aspect_y], scene_camera=sc.camera.name if sc.camera else None,
              engine=sc.render.engine, view_transform=sc.view_settings.view_transform, look=sc.view_settings.look,
              exposure=round(sc.view_settings.exposure, 3), gamma=round(sc.view_settings.gamma, 3))

# ---------------------------------------------------------------- 7) mentés + lock + változásnapló
bpy.ops.wm.save_as_mainfile(filepath=OUT, copy=False)
def coll_boxes(cn, only_visible=False):
    return {o.name: r3(wb(o)) for o in bpy.data.collections[cn].objects if o.type == 'MESH' and not (only_visible and o.hide_render)}
lock = dict(
    verzio='A902 geometria v2b – alaprajz szerinti, ELŐZETES (helyszínen nem mért)', datum=datetime.date.today().isoformat(),
    forras=dict(blend=os.path.basename(OUT), alap=os.path.basename(SRC), terv='WGR1 méretezett alaprajz 18. old. 1:50 (p18_falvonalak_m.json) + megvalósulási terv 3. old.',
                megj='Vakolatlan tervsíkok; kész falsík oldalanként ~1–2 cm-rel beljebb lehet.'),
    origin='05.2 DNy-i belső sarka (x kelet, y észak, m)', H=H, tolerance_m=0.01,
    rooms=ROOMS, room_terv_m2=ROOM_TERV_M2, walls=coll_boxes('A902_Falak'), openings=coll_boxes('A902_Nyilaszarok'),
    openings_meta=OPENINGS_META, floors=coll_boxes('A902_Padlo', only_visible=True),
    floors_rejtett_elavult=sorted(o.name for o in bpy.data.collections['A902_Padlo'].objects if o.hide_render),
    terrace_v2={o.name: r3(wb(o)) for o in bpy.data.collections['A902_Terasz_v2_ELOZETES'].objects if o.type == 'MESH'},
    terrace_zones=TERRACE_ZONES, cameras=cams, render=render,
    statusz=dict(falak_nyilasok=T, belmagassag='HELYSZÍNEN MÉRT 2,90–2,93 (Kémeri)', anyagok=F, terasz_v2='változatlan (v2, ELŐZETES)'))
json.dump(lock, open(LOCK, 'w'), ensure_ascii=False, indent=1)
json.dump(dict(datum=lock['datum'], alap=os.path.basename(SRC), kimenet=os.path.basename(OUT), valtozasok=log,
               anyagok=[dict(objektum=a, valtozas=b) for a, b in mat_log]), open(CHG, 'w'), ensure_ascii=False, indent=1)
print('KESZ', OUT, 'valtozas:', len(log), 'anyag:', len(mat_log))
