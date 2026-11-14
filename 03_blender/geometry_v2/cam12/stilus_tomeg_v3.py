# KEP-004 – Astra Creative Upgrade V3 r1 (PR #16, be6b1f3) S01/S02 nappali tömegei, a blender_cam12_v1/03_ellenorzes_tomegek.py-val azonos méretekkel.
# Claude, 2026-10-25. A betöltött .blend-et NEM menti.
import bpy
def stilus_tomeg(kod, sc, T):
    col = bpy.data.collections.new('Stil_TOMEG_' + kod); sc.collection.children.link(col); rec = {}
    def blokk(nev, a, b, fajta): return T.doboz(col, nev, a, b, fajta, rec)
    if kod == 'S01':
        blokk('S01_KI3L_also_tarolo', (3.67, 5.15, 0), (4.07, 7.55, 0.48), 'tarolo')          # 240×48×40
        blokk('S01_KI3V_torony', (3.67, 4.35, 0), (3.97, 4.95, 2.20), 'tarolo')               # 60×220×30
        blokk('S01_KI3P_panel_a', (3.67, 5.05, 0.55), (3.69, 6.35, 2.45), 'panel')            # 260×190, két sík, 15 mm eltolás
        blokk('S01_KI3P_panel_b', (3.67, 6.35, 0.55), (3.705, 7.65, 2.45), 'panel')
        blokk('S01_TV_kepernyo', (3.71, 6.35 - 0.725, 0.85), (3.76, 6.35 + 0.725, 1.68), 'kepernyo')
        blokk('S01_KI3A_mu_W02', (5.95, 4.05, 0.80), (6.95, 4.08, 2.60), 'mu')                 # 100×180, javasolt hely
        XB, YS, YN, D, CH, CW = 7.17, 5.21, 7.59, 0.95, 1.80, 0.95                             # Lennon jobbos L 238×180×68
        blokk('S01_kanape_L_fo', (XB - D, YS + CW, 0), (XB, YN, 0.42), 'kanape')
        blokk('S01_kanape_L_chaise', (XB - CH, YS, 0), (XB, YS + CW, 0.42), 'kanape')
        blokk('S01_kanape_L_hattamla', (XB - 0.22, YS, 0.42), (XB, YN, 0.68), 'kanape')
        blokk('S01_kanape_L_kar', (XB - D, YN - 0.20, 0.42), (XB - 0.22, YN, 0.60), 'kanape')
        AX0, AY0, AX1, AY1, SZ, MEL, YK = 7.90, 5.27, 8.80, 7.27, 0.55, 0.53, (5.60, 6.27, 6.94)  # Toni 200×90, 6 Eamy 55×53
    else:
        blokk('S02_BN3L_also_tarolo', (3.67, 5.25, 0), (4.07, 7.65, 0.50), 'tarolo')          # 240×50×40
        blokk('S02_BN3V_kabinet', (3.67, 4.25, 0), (3.99, 5.15, 2.20), 'tarolo')              # 90×220×32
        blokk('S02_BN3P_panel', (3.67, 5.25, 0.55), (3.71, 7.65, 2.45), 'panel')              # 240×190
        blokk('S02_TV_kepernyo', (3.71, 6.35 - 0.725, 0.85), (3.76, 6.35 + 0.725, 1.68), 'kepernyo')
        blokk('S02_BN3A_grafika_W02', (5.85, 4.05, 0.85), (7.05 - 0.05, 4.07, 2.45), 'mu')     # 120×160
        X1, Y0, Y1, D, AR = 7.17, 4.975, 7.825, 0.95, 1.60                                     # JÄTTEBO U 285×160×71
        blokk('S02_kanape_U_hat', (X1 - D, Y0, 0), (X1, Y1, 0.42), 'kanape')
        blokk('S02_kanape_U_del', (X1 - AR, Y0, 0), (X1 - D, Y0 + D, 0.42), 'kanape')
        blokk('S02_kanape_U_eszak', (X1 - AR, Y1 - D, 0), (X1 - D, Y1, 0.42), 'kanape')
        blokk('S02_kanape_U_hattamla', (X1 - 0.22, Y0, 0.42), (X1, Y1, 0.71), 'kanape')
        blokk('S02_kanape_U_hattamla_d', (X1 - AR, Y0, 0.42), (X1 - 0.22, Y0 + 0.22, 0.71), 'kanape')
        blokk('S02_kanape_U_hattamla_e', (X1 - AR, Y1 - 0.22, 0.42), (X1 - 0.22, Y1, 0.71), 'kanape')
        AX0, AY0, AX1, AY1, SZ, MEL, YK = 7.90, 5.37, 8.80, 7.17, 0.525, 0.55, (5.67, 6.27, 6.87)  # Anouk 180×90, 6 Ciselia 52,5×55
    blokk(f'{kod}_etkezo_asztal_lap', (AX0, AY0, 0.72), (AX1, AY1, 0.75), 'etkezo')
    blokk(f'{kod}_etkezo_asztal_labd', (AX0 + 0.20, AY0 + 0.25, 0), (AX1 - 0.20, AY0 + 0.33, 0.72), 'etkezo')
    blokk(f'{kod}_etkezo_asztal_labe', (AX0 + 0.20, AY1 - 0.33, 0), (AX1 - 0.20, AY1 - 0.25, 0.72), 'etkezo')
    for i, yc in enumerate(YK):
        x1 = AX0 + 0.18; x0 = x1 - MEL
        blokk(f'{kod}_etkezo_szekny{i}_ules', (x0, yc - SZ / 2, 0), (x1, yc + SZ / 2, 0.46), 'etkezo')
        blokk(f'{kod}_etkezo_szekny{i}_hat', (x0, yc - SZ / 2, 0.46), (x0 + 0.06, yc + SZ / 2, 0.78), 'etkezo')
        x0 = AX1 - 0.18; x1 = x0 + MEL
        blokk(f'{kod}_etkezo_szekk{i}_ules', (x0, yc - SZ / 2, 0), (x1, yc + SZ / 2, 0.46), 'etkezo')
        blokk(f'{kod}_etkezo_szekk{i}_hat', (x1 - 0.06, yc - SZ / 2, 0.46), (x1, yc + SZ / 2, 0.78), 'etkezo')
    col.hide_render = True
    return col, rec
