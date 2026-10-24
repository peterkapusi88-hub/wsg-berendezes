# Lake Forest-réteg az A-902-höz (Stil_LakeForest gyűjtemény). Előfeltétel: wsg_helpers.py lefuttatva.
import bpy, math, random
W = bpy.app.driver_namespace['wsg']
box, cyl, sphere, tube, disc, mat, coll = W['box'], W['cyl'], W['sphere'], W['tube'], W['disc'], W['mat'], W['coll']

# ha már létezik, töröljük és újraépítjük
old = bpy.data.collections.get("Stil_LakeForest")
if old:
    for o in list(old.objects):
        bpy.data.objects.remove(o, do_unlink=True)
C = coll("Stil_LakeForest")

# ---- anyagok (Lake Forest) ----
TRAV  = mat("L_travertin", (0.80,0.72,0.60), 0.35, noise=(14.0,(0.90,0.84,0.74),0.12))
TOLGY = mat("L_vilagos_tolgy", (0.76,0.64,0.46), 0.45)
BRONZ = mat("L_bronz", (0.62,0.46,0.28), 0.25, metal=1.0)
ARANY = mat("L_pezsgo_arany", (0.85,0.70,0.42), 0.2, metal=1.0)
KREM  = mat("L_boucle_krem", (0.92,0.89,0.83), 1.0)
LEN2  = mat("L_len_feher", (0.95,0.93,0.89), 0.9)
MARV  = mat("L_feher_marvany", (0.92,0.91,0.89), 0.15, noise=(9.0,(0.70,0.70,0.70),0.0))
SHAG  = mat("L_shaggy_krem", (0.90,0.86,0.78), 1.0)
LEDW  = mat("L_LED_3000K", (1.0,0.85,0.62), 0.5, emit=20.0)
FUSTT = mat("L_fustos_tukor", (0.35,0.30,0.25), 0.03, metal=1.0)
TUKOR = mat("L_tukor", (0.9,0.9,0.9), 0.0, metal=1.0)
TVM   = mat("L_tv_fekete", (0.01,0.01,0.01), 0.15)
FUGG  = mat("L_fuggony_feher", (0.96,0.95,0.93), 1.0)
GOMB  = mat("L_gomb_uveg", (0.98,0.95,0.88), 0.05, emit=6.0)
KREMFRONT = mat("L_konyhafront_krem", (0.90,0.87,0.80), 0.6)
LABKREM = mat("L_lab_krem", (0.85,0.82,0.76), 0.6)
RELIEF = mat("L_relief_krem", (0.88,0.84,0.76), 0.8, noise=(5.0,(0.78,0.72,0.62),0.6))
BARSONY = mat("L_barsony_bezs", (0.80,0.72,0.60), 0.8)

# ---- NAPPALI: travertin TV-fal bronz keretben + világos tölgy lamella + lebegő tölgy pad ----
box("L_TVfal_travertin", 5.45,4.04,0, 7.40,4.075,2.88, TRAV, C)
box("L_TVfal_bronzkeret_a", 5.45,4.075,0, 5.49,4.10,2.88, BRONZ, C); box("L_TVfal_bronzkeret_b", 7.36,4.075,0, 7.40,4.10,2.88, BRONZ, C)
box("L_TVfal_bronzkeret_top", 5.45,4.075,2.84, 7.40,4.10,2.88, BRONZ, C)
for x in [x/1000 for x in range(5520, 5760, 45)] + [x/1000 for x in range(7090, 7340, 45)]:
    box(f"L_lamella_{int(x*1000)}", x,4.075,0.0, x+0.028,4.097,2.84, TOLGY, C)
box("L_TVfal_pad", 5.52,4.075,0.40, 7.33,4.50,0.72, TOLGY, C, bevel=0.01)
box("L_TVfal_pad_LED", 5.56,4.10,0.39, 7.29,4.16,0.40, LEDW, C)
box("L_TV55", 5.81,4.095,1.00, 7.04,4.11,1.71, TVM, C)
# krém bouclé modulkanapé (Neom-arány) + chaise + puff
mods = [(4.55,5.75,5.45,6.75),(5.45,5.75,6.35,6.75),(6.35,5.75,7.25,6.75),(7.25,5.0,8.15,6.75)]
for i,(x0,y0,x1,y1) in enumerate(mods):
    box(f"L_kanape_ules_{i}", x0,y0,0.12, x1,y1,0.44, KREM, C, bevel=0.07)
    if i < 3: box(f"L_kanape_hat_{i}", x0,y1-0.22,0.44, x1,y1,0.82, KREM, C, bevel=0.07)
    else: box(f"L_kanape_hat_{i}", x1-0.22,y0,0.44, x1,y1,0.82, KREM, C, bevel=0.07)
box("L_kanape_kar", 4.40,5.75,0.12, 4.55,6.75,0.64, KREM, C, bevel=0.05)
box("L_kanape_lab", 4.5,5.8,0.0, 8.1,6.7,0.12, LABKREM, C)
for i,(x,y) in enumerate([(4.9,6.35),(5.6,6.3),(6.4,6.35),(7.0,6.3),(7.8,5.6),(7.85,6.3)]):
    p = box(f"L_parna_{i}", -0.26,-0.1,0.44, 0.26,0.1,0.92, LEN2 if i%2 else KREM, C, bevel=0.05)
    p.location=(x,y,0); p.rotation_euler=(0,0,math.radians(-8+6*i))
box("L_puff", 4.4,4.65,0.0, 5.3,5.35,0.44, KREM, C, bevel=0.12)
box("L_szonyeg_shaggy", 4.25,4.45,0.0, 8.35,6.65,0.03, SHAG, C, bevel=0.01)
cyl("L_dohanyzo_lap", 6.1,5.4,0.33, 0.42, 0.36, MARV, C); cyl("L_dohanyzo_lab", 6.1,5.4,0.0, 0.16, 0.33, ARANY, C, 24)
cyl("L_kisasztal_lap", 7.9,4.9,0.45, 0.25, 0.47, MARV, C); cyl("L_kisasztal_lab", 7.9,4.9,0.0, 0.03, 0.45, ARANY, C, 12)
# bouclé fotel fa karfával
f1 = box("L_fotel_ules", -0.40,-0.40,0.10, 0.40,0.40,0.44, KREM, C, bevel=0.08); f2 = box("L_fotel_hat", -0.40,0.22,0.44, 0.40,0.40,0.90, KREM, C, bevel=0.08)
f3 = box("L_fotel_karfa_a", -0.44,-0.40,0.44, -0.36,0.40,0.62, TOLGY, C); f4 = box("L_fotel_karfa_b", 0.36,-0.40,0.44, 0.44,0.40,0.62, TOLGY, C)
for o in (f1,f2,f3,f4): o.rotation_euler=(0,0,math.radians(35)); o.location=(4.3,7.3,0)
# bubble-csillár a nappali közepén + az étkező fölött
random.seed(7)
def bubble(prefix, cx, cy, zc, n=14, spread=0.45):
    tube(prefix+"_szar", (cx,cy,2.89), (cx,cy,zc+0.3), 0.01, ARANY, C)
    for i in range(n):
        a = random.uniform(0, 2*math.pi); r = random.uniform(0.05, spread); z = zc + random.uniform(-0.35, 0.35)
        sphere(f"{prefix}_gomb_{i}", cx+r*math.cos(a), cy+r*math.sin(a), z, random.uniform(0.07,0.14), GOMB, C)
bubble("L_csillar_nappali", 6.0,5.6, 2.25, 16, 0.5)
bubble("L_csillar_etkezo", 9.6,6.35, 1.95, 10, 0.3)
# függöny: áttetsző fehér, a terasz üvegnél
box("L_fuggony_a", 3.75,7.80,0.02, 4.45,7.90,2.88, FUGG, C); box("L_fuggony_b", 9.05,7.80,0.02, 9.75,7.90,2.88, FUGG, C)
box("L_fuggonysin", 3.72,7.78,2.86, 9.9,7.82,2.89, ARANY, C)
# nagy kép a 05.1 falon (x=3.72): relief-hatás
box("L_kep_keret", 3.72,5.0,1.1, 3.745,6.6,2.3, ARANY, C); box("L_kep", 3.745,5.03,1.13, 3.75,6.57,2.27, RELIEF, C)

# ---- ÉTKEZŐ: tölgy asztal arany lábbal + arany drótvázas bársony székek + tálaló ----
box("L_etkezo_lap", 8.65,5.45,0.73, 9.55,7.25,0.76, TOLGY, C, bevel=0.01)
for i,(x,y) in enumerate([(8.72,5.52),(9.48,5.52),(8.72,7.18),(9.48,7.18)]): box(f"L_etkezo_lab{i}", x-0.025,y-0.025,0, x+0.025,y+0.025,0.73, ARANY, C)
for i,y in enumerate((5.75,6.35,6.95)):
    for j,(x,facing) in enumerate([(8.25,'E'),(9.95,'W')]):
        box(f"L_szek_ules_{i}{j}", x-0.23,y-0.23,0.43, x+0.23,y+0.23,0.49, BARSONY, C, bevel=0.03)
        bk = (x-0.23,y-0.23,x-0.19,y+0.23) if facing=='E' else (x+0.19,y-0.23,x+0.23,y+0.23)
        box(f"L_szek_hat_{i}{j}", bk[0],bk[1],0.49, bk[2],bk[3],0.88, ARANY, C)
        for dx,dy in ((-0.2,-0.2),(0.2,-0.2),(-0.2,0.2),(0.2,0.2)):
            box(f"L_szek_lab_{i}{j}_{dx}{dy}", x+dx-0.008,y+dy-0.008,0, x+dx+0.008,y+dy+0.008,0.43, ARANY, C)
box("L_talalo", 10.20,5.40,0.0, 10.64,7.00,0.74, TOLGY, C); box("L_talalo_lap", 10.18,5.38,0.74, 10.64,7.02,0.77, MARV, C); box("L_talalo_LED", 10.22,5.45,0.77, 10.62,6.95,0.78, LEDW, C)

# ---- KONYHA: krém front + fehér márvány munkalap + sárgaréz fogantyú + tölgy magas elemek ----
box("L_konyha_also_K", 10.04,1.30,0.10, 10.64,4.50,0.86, KREMFRONT, C); box("L_konyha_munkalap_K", 10.02,1.30,0.86, 10.64,4.50,0.90, MARV, C)
box("L_konyha_huto", 10.04,4.50,0.10, 10.64,5.15,2.30, TOLGY, C); box("L_konyha_felso_K", 10.29,1.30,1.45, 10.64,4.50,2.30, KREMFRONT, C)
box("L_konyha_hatfal_marvany", 10.30,1.30,0.90, 10.64,4.50,1.45, MARV, C)
box("L_konyha_felso_LED", 10.30,1.35,1.44, 10.62,4.45,1.45, LEDW, C); box("L_konyha_top_LED", 10.30,1.30,2.30, 10.62,5.15,2.32, LEDW, C)
box("L_konyha_also_Ny", 8.55,2.40,0.10, 9.15,4.04,0.86, KREMFRONT, C); box("L_konyha_munkalap_Ny", 8.55,2.40,0.86, 9.17,4.04,0.90, MARV, C)
box("L_konyha_magas", 9.10,1.30,0.10, 9.70,1.90,2.30, TOLGY, C)
for y in (1.6,2.2,2.8,3.4,4.0): box(f"L_fogantyu_{int(y*10)}", 10.03,y,0.78, 10.04,y+0.16,0.80, ARANY, C)

# ---- MASTER: travertin ágyfal bronz sávval, krém ágy, kerek LED-tükör, krém gardrób füstös tükörbetéttel ----
box("L_agyfal_travertin", 3.56,4.08,0.0, 3.62,7.86,2.88, TRAV, C)
box("L_agyfal_bronz", 3.55,5.95,0.0, 3.56,6.05,2.88, BRONZ, C); box("L_agyfal_LED", 3.54,4.10,2.84, 3.56,7.84,2.86, LEDW, C)
box("L_agy_keret", 1.56,5.10,0.0, 3.54,6.90,0.30, KREM, C, bevel=0.06); box("L_agy_matrac", 1.60,5.14,0.30, 3.52,6.86,0.54, LEN2, C, bevel=0.03)
box("L_agy_takaro", 1.62,5.20,0.54, 3.30,6.82,0.62, LEN2, C, bevel=0.03)
for i,y in enumerate((4.55,7.15)):
    cyl(f"L_ejjeli_{i}", 3.25,y+0.2,0.0, 0.22, 0.52, ARANY, C, 32); cyl(f"L_ejjeli_lap_{i}", 3.25,y+0.2,0.52, 0.24, 0.54, MARV, C, 32)
    box(f"L_olvasolampa_{i}", 3.50,y+0.1,1.45, 3.56,y+0.3,1.52, ARANY, C); box(f"L_olvasolampa_feny_{i}", 3.49,y+0.12,1.44, 3.50,y+0.28,1.45, LEDW, C)
box("L_gardrob_krem", 0.0,3.45,0.0, 2.42,4.02,2.36, KREMFRONT, C)
for i in range(1,4): box(f"L_gardrob_fuga_{i}", i*0.605-0.003,4.0,0.05, i*0.605+0.003,4.03,2.31, BRONZ, C)
box("L_gardrob_fustos_betet", 0.70,4.02,0.3, 1.70,4.03,2.1, FUSTT, C)
box("L_gardrob_LED", 0.05,3.50,2.36, 2.37,3.97,2.38, LEDW, C)
box("L_master_szonyeg", 0.9,4.5,0.0, 3.3,7.5,0.03, SHAG, C, bevel=0.01)
disc("L_tukor_kerek", 1.35,8.94,1.6, 0.45, 0.02, TUKOR, C, axis='Y')
disc("L_tukor_LED", 1.35,8.945,1.6, 0.49, 0.01, LEDW, C, axis='Y')
box("L_fesulkodo", 0.6,8.5,0.0, 2.1,8.93,0.75, TOLGY, C); box("L_fesulkodo_lap", 0.58,8.48,0.75, 2.12,8.95,0.78, MARV, C)
box("L_master_fuggony_a", 0.03,4.25,0.02, 0.10,4.95,2.88, FUGG, C); box("L_master_fuggony_b", 0.03,7.25,0.02, 0.10,7.90,2.88, FUGG, C)

result = {"lf_objects": len(C.objects)}
