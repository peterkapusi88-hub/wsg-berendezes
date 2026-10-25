# A-902 S02 BiBo Nocturne konyha (Cam_03 K1) – megépíthetőségi tömbök (Claude, 2026-10-25, Péter 08:21 „mehet”, 08:26 döntés:
# „kb. úgy legyen, ahogy a BiBo-konyha” – a hűtőoszlop a W03-a előtt, a 05.3 ajtótól jobbra marad).
# Koordináták: lock v2b-1-k13 (x kelet, y észak, m). A konyha a lock szerint: déli rész x 9,05–10,55 × y 1,35–2,35 (1,50 m széles),
# északi rész x 8,45–10,55 × y 2,35–4,05 (2,10 m); pillér/szekrényfülke-fal x 8,35–9,05 × y 2,25–2,35 és x 8,95–9,05 × y 1,35–2,35 (szerkezet, nem bontható).
# Modulméretek: IKEA METOD alsó 60 mély korpusz + front ≈ 62, lábazat 0,10, alsó front 0,80, munkalap 0,04 (Fable S02 §2.4);
# magas szekrény 60 × 62 × 228 + felső doboz 2,75-ig (Fable S02 ET-01); felső elem 0,80 magas front (Fable), alsó éle 1,45 és mélysége 0,37 BECS.
# allapot: ELL / LEV / BECS / FELT, mint a cam12 korrekcióban.
NAVY, SILVER, STONE, BLACK, BRONZE, BEIGE, BRASS = (0.05, 0.08, 0.18), (0.66, 0.67, 0.68), (0.60, 0.57, 0.52), (0.03, 0.03, 0.03), (0.30, 0.25, 0.20), (0.66, 0.60, 0.50), (0.72, 0.55, 0.32)
def K(v):
    L = []
    def add(id_, nev, tipus, g, szin, allapot, forras, rough=0.8): L.append(dict(v=v, id=id_, nev=nev, tipus=tipus, g=g, szin=szin, allapot=allapot, forras=forras, rough=rough))
    # --- közös: keleti sor, hűtőoszlop (tulajdonosi döntés), tükörsáv, étkező
    add('KO-K1', 'keleti sor alsó elemek navy (METOD, 62 mély)', 'box', (9.93, 1.35, 0, 10.55, 4.10, 0.90), NAVY, 'ELL 62 / 0,10+0,80; hossz LEV (K-pultfal y 1,35–4,10)', 'Fable S02 §2.4; BiBo-kép')
    add('KO-K1_munkalap', 'keleti sor munkalap 4 cm kőhatású laminált', 'box', (9.93, 1.35, 0.90, 10.55, 4.10, 0.94), STONE, 'ELL 4 cm', 'Fable S02 §2.4 (EKBACKEN)')
    add('KO-K1_mosogato', 'mosogató (jelölés) – a fotók szerinti vízkiállás közelében', 'box', (10.02, 3.30, 0.935, 10.46, 3.80, 0.942), BLACK, 'hely BECS (vízkiállás a 045/056 fotón a sor északi felén, nem mért)', '056/045 fotó; D04 MG y 3,31')
    add('ET-01', 'hűtőoszlop METOD 60×62×228 + doboz 2,75-ig, navy, a W03-a előtt', 'box', (10.13, 5.05, 0, 10.75, 5.65, 2.75), NAVY, 'ELL; hely: Péter 08:26 döntése', 'Fable S02 ET-01; BiBo-kép')
    add('ET-02', 'füstbronz tükörsáv 0,40×2,60 (y 5,65–6,05)', 'box', (10.74, 5.65, 0.15, 10.75, 6.05, 2.75), BRONZE, 'ELL', 'Fable S02 ET-02', rough=0.05)
    add('DI-01', 'Westwing Toni ovális 160×90 fekete – lap', 'ell', (8.45, 6.20, 0.72, 0.45, 0.80, 0.75), BLACK, 'ELL (C alap)', 'Fable S02 §2.5; GEOM v2 §2')
    add('DI-01b', 'Toni – láb (jelképes)', 'box', (8.25, 6.00, 0, 8.65, 6.40, 0.72), BLACK, 'BECS', '')
    for i, (cx, cy, nx, ny) in enumerate([(8.00, 6.10, -1, 0), (8.00, 6.70, -1, 0), (8.90, 6.10, 1, 0), (8.90, 6.70, 1, 0), (8.45, 5.40, 0, -1), (8.45, 7.00, 0, 1)]):
        add(f'DI-02{"abcdef"[i]}', f'Kave Home Ciselia 52,5×55×75 #{i + 1}', 'chair', (cx, cy, nx, ny, 0.525, 0.55, 0.45, 0.75), BEIGE, 'ELL; C alap', 'Fable S02 §2.5')
    add('DI-03', 'Kave Home Brisia Ø72,5×27 az ML04-en', 'ell', (8.549, 6.274, 1.60, 0.3625, 0.3625, 1.87), BRASS, 'ELL méret; mag. BECS', 'Fable S02 §2.5')
    add('DI-03k', 'Brisia kábel', 'box', (8.544, 6.269, 1.87, 8.554, 6.279, 2.90), BLACK, 'LEV', '')
    if v == 'U':
        # BiBo-kép fizikailag illesztve: déli pultvisszafordulás főzőlappal a teljes 0,88 m-en, magas sütő/mikró oszlop a pillér ELŐTT
        add('KO-S1', 'déli pultvisszafordulás alsó navy (x 9,05–9,93, 0,88 m)', 'box', (9.05, 1.35, 0, 9.93, 1.97, 0.90), NAVY, 'hossz LEV (a déli fal 1,50 m – 0,62 keleti sor); a sarok vakkarkas BECS', 'BiBo-kép; lock')
        add('KO-S1_fedlap', 'déli pultvisszafordulás munkalap', 'box', (9.05, 1.35, 0.90, 9.93, 1.97, 0.94), STONE, 'ELL 4 cm', 'BiBo-kép')
        add('KO-S1_fozolap', 'főzőlap 58×51 (jelölés)', 'box', (9.20, 1.42, 0.94, 9.78, 1.93, 0.946), BLACK, 'termékméret BECS (szokásos 60-as indukciós)', 'BiBo-kép')
        add('KO-K2', 'keleti felső elemek ezüstszürke + navy doboz 2,75-ig', 'box', (10.18, 1.35, 1.45, 10.55, 4.10, 2.75), SILVER, 'teteje ELL; alsó él 1,45 és 0,37 mély BECS', 'Fable S02 §2.4; BiBo-kép')
        add('KO-S2', 'déli felső elemek + doboz 2,75-ig (benne beépített elszívó BECS)', 'box', (9.05, 1.35, 1.45, 10.18, 1.72, 2.75), SILVER, 'BECS', 'BiBo-kép')
        add('KO-T1', 'magas sütő/mikró oszlop navy 60×62, a pillér északi lapja előtt, front kelet felé', 'box', (8.45, 2.35, 0, 9.07, 2.95, 2.75), NAVY, 'ELL modul; hely LEV (az egyetlen hely „a pillérnél”, a pillér nem bontható)', 'BiBo-kép; Fable S02 §2.4')
        add('KO-T1_suto', 'sütő + mikró (jelölés a keleti lapon)', 'box', (9.07, 2.42, 0.82, 9.075, 2.88, 1.88), BLACK, 'BECS', '')
        add('KO-NY', 'nyugati alacsony sor navy a mellvéd mentén (y 2,95–4,05)', 'box', (8.45, 2.95, 0, 9.07, 4.05, 0.90), NAVY, 'mély ELL; hossz LEV', 'BiBo-kép')
        add('KO-NY_munkalap', 'nyugati munkalap a mellvéden átnyúlva (72 cm mély, x 8,35–9,07)', 'box', (8.35, 2.95, 0.90, 9.07, 4.05, 0.94), STONE, 'BECS – egyedi 72 cm-es lap (a szabvány 63,5)', 'BiBo-kép (a kő a mellvéd külső síkjáig)')
    else:
        # kiállás-hű alternatíva: a déli falon magas géposzlop a D08/D09 előtt (Fable/fejlesztői terv), főzőlap a nyugati soron az X01-nél
        add('KO-T1', 'magas sütő/mikró oszlop navy 60×62 a déli falon (D08/D09 előtt), front észak felé', 'box', (9.05, 1.35, 0, 9.65, 1.97, 2.75), NAVY, 'ELL modul; hely LEV (D08 Mi 1,30 / D09 S 1,10 x 9,349)', 'Fable S02 §2.4; A902_villamos.csv')
        add('KO-T1_suto', 'sütő + mikró (jelölés az északi lapon)', 'box', (9.12, 1.97, 0.80, 9.58, 1.975, 1.86), BLACK, 'BECS', '')
        add('KO-S1', 'töltőelem 28 cm (20 cm-es kihúzható + takaró) a géposzlop és a keleti sor között', 'box', (9.65, 1.35, 0, 9.93, 1.97, 0.90), NAVY, 'BECS', 'METOD 20-as alsó (ellenőrzendő)')
        add('KO-S1_fedlap', 'töltőelem fedlap', 'box', (9.65, 1.35, 0.90, 9.93, 1.97, 0.94), STONE, 'ELL 4 cm', '')
        add('KO-K2', 'keleti felső elemek ezüstszürke + navy doboz 2,75-ig', 'box', (10.18, 1.97, 1.45, 10.55, 4.10, 2.75), SILVER, 'teteje ELL; alsó él és mélység BECS', 'Fable S02 §2.4')
        add('KO-NY', 'nyugati alacsony sor navy a mellvéd mentén (y 2,35–4,05), benne főzőlap', 'box', (8.45, 2.35, 0, 9.07, 4.05, 0.90), NAVY, 'mély ELL; hossz LEV', 'Fable S02 §2.4; fejlesztői terv')
        add('KO-NY_munkalap', 'nyugati munkalap a mellvéden átnyúlva (72 cm mély)', 'box', (8.35, 2.35, 0.90, 9.07, 4.05, 0.94), STONE, 'BECS – egyedi 72 cm-es lap', 'BiBo-kép')
        add('KO-NY_fozolap', 'főzőlap 58×51 az X01 fix bekötésnél (8,776; 3,224)', 'box', (8.52, 2.93, 0.94, 9.03, 3.51, 0.946), BLACK, 'hely LEV (X01); méret BECS', 'A902_villamos.csv X01')
        add('KO-ELSZ', 'mennyezeti/szigetelszívó befoglaló 0,90×0,50×0,30 a csőcsonk/D05 alatt (HF04 mezőn kívül, x < 9,05)', 'box', (8.53, 2.77, 2.60, 9.03, 3.67, 2.90), (0.55, 0.56, 0.58), 'ISMERETLEN termék; hely: a D05/X01 és a fotón látott csőcsonk szerint, nem mért', 'A902_villamos.csv D05; 045/046/056 fotó')
    return L
VALTOZATOK = {'U': 'BiBo-kép szerinti U (fizikailag illesztve)', 'A': 'kiállás-hű alternatíva (déli géposzlop, nyugati főzőlap)'}
