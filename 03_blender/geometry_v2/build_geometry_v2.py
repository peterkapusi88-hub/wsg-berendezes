"""A-902 geometria v2 – ELŐZETES (tervdokumentumból, nem helyszíni mérés).
Forrás: WGR1_meretezett_alaprajzok.pdf (műszaki átadás-átvételi dosszié kivonat, Péter, 2026-10-24)
  - 18. old.: A-902 méretezett alaprajz, 1:50 A3, vektoros (vakolatlan falméretek!)
  - 3. old.: 9. emelet MEGVALÓSULÁSI TERV 1:125, 2026-07-08 (terasz, zöldtető, szintek, m²)
  - 21. old.: A-902 burkolatkiosztási terv (parketta dekor)
Koordináta: mint geometry_lock_A902.json (origó 05.2 DNy belső sarok; x kelet, y észak; z: belső kész padló = 0).
A nyers PDF vevői adatot tartalmaz → NEM kerül a repóba; a kinyerő szkript helyi útvonalról olvas.
"""
import json
SRC18="PDF p18 vektor 1:50 (vakolatlan)"; SRC3="PDF p3 megvalósulási terv 1:125 (2026-07-08)"
rooms = {  # [x0,y0,x1,y1], terv m², megjegyzés
 "05_2":            ([0.00,0.00,3.65,2.65], 11.66, "3.65 × 3.35 a fülkével"),
 "05_2_gardrob":    ([0.00,2.65,2.42,3.35], None,  "fülke 2.42 széles"),
 "05_1":            ([0.00,3.45,3.57,8.05], 19.58, "5.50 a fülkével; K-i rész 4.00 (4.05–8.05); D-i fal x 2.42–3.57 között y 4.05-nél"),
 "05_1_eszaki":     ([0.00,8.05,3.02,8.95], None,  "északi fülke (pillér mögött)"),
 "kozlekedo":       ([2.52,2.65,5.30,4.05], 3.23,  "2.48 × 1.20 (+ ajtózsebek)"),
 "nappali_etkezo":  ([3.67,4.05,10.75,8.05], 27.87, "7.08 hossz; É-i falsík 8.05, üvegfal belső síkja ~7.93–8.27 tok"),
 "konyha":          ([8.45,1.35,10.55,4.05], 5.24, "konyhafal (K) 3.90: y 1.35–5.25; 10.55–10.75 szerelt gk. technikai fal y 4.1–4.55 (elszívó)"),
 "eloter":          ([5.60,0.00,8.35,2.00], 6.98, "bejárati fülke x 6.70–8.30, y 0.00–0.85; ajtó 1.05×2.10"),
 "eloter_atjaro":   ([7.30,2.00,8.35,4.05], None,  "előtér → nappali átjáró"),
 "wc":              ([5.60,2.10,6.60,3.95], 1.88, "1.30 × 1.85 (bidés ülőke); pontos kontúr L-alakú – helyszínen mérendő"),
 "furdo_06_1":      ([3.75,0.00,5.50,2.65], 4.46, "1.75 × 2.65, kád 170×70"),
 "05_3":            ([10.85,4.10,14.37,8.05], 14.65, "3.525 × 3.95"),
 "furdo_06_2":      ([14.47,5.20,16.40,8.05], 4.39, "1.925 × 2.85; épített zuhany 1.825 × 0.85 (y 7.20–8.05), 5/5 padka"),
}
lock_v1 = json.load(open('../geometry_lock_A902.json'))['rooms']
name_map={"kozlekedo":"eloszoba_kozlekedo"}
diff=[]
for k,(r,a,n) in rooms.items():
    old=lock_v1.get(name_map.get(k,k))
    d=None if old is None else [round((r[i]-old[i])*100) for i in range(4)]
    diff.append({"room":k,"v1":old,"v2":r,"delta_cm_W_S_E_N":d,"terv_m2":a,"megj":n})
terrace = {  # x0,y0,x1,y1, z (belső kész padlóhoz képest), anyag, forrás, státusz
 "T09_greslap_Ny":   dict(box=[3.44,8.50,9.29,12.40], z=-0.15, anyag="világos szürke greslap (nagyformátum, ~60×60 – videó)", m2_terv=23.62, abs_szint="+28,40", status="DOKUMENTUM + VIDEÓ", src=SRC3),
 "T10_greslap_K":    dict(box=[11.39,8.50,16.27,12.40], z=-0.15, anyag="világos szürke greslap", m2_terv=19.34, abs_szint="+28,40", status="DOKUMENTUM + VIDEÓ", src=SRC3),
 "T11_WPC_kozepso":  dict(box=[9.29,8.50,11.39,12.40], z=+0.47, anyag="sötét szürkésbarna bordázott WPC (»11 TERASZ kültéri fa burkolat«)", m2_terv="25.00 (a T11 összesen)", abs_szint="+29,02", status="DOKUMENTUM + VIDEÓ", src=SRC3),
 "T11_WPC_harant":   dict(box=[3.44,12.40,16.27,13.41], z=+0.47, anyag="WPC", abs_szint="+29,02", status="DOKUMENTUM + VIDEÓ", src=SRC3),
 "T11_WPC_eszaki_nyelv": dict(box=[9.29,13.41,11.39,14.46], z=+0.47, anyag="WPC", status="ELŐZETES – vonalból értelmezve", src=SRC3),
 "T11_WPC_jarosav_megjegyzes": dict(note="A videón (t=4–12 s, 36–46 s, panoráma) WPC járósáv fut a zöldtető szélén, a korlát mentén; a terven nem szerepel → helye, szélessége, szintje HIÁNYZIK. Blenderben NINCS modellezve, amíg nincs mérés.", src="videó IMG_2481"),
 "T11_WPC_panorama_pont": dict(box=[7.62,18.95,11.42,19.79], z=+0.47, anyag="WPC pihenő a É-i korlátnál", status="ELŐZETES – terv-kontúr + videó", src=SRC3),
 "Zoldtető":         dict(box=[3.71,13.41,16.04,19.80], z=+0.77, anyag="extenzív zöldtető: fű/szukkulens, kavicssáv, csepegtető cső, aknafedlapok", m2_terv=71.18, status="terület DOKUMENTUM; felszínmagasság ELŐZETES (videóbecslés), terhelhetőség HIÁNYZIK; NEM bútorozható/járható alapból", src=SRC3),
 "Zoldtető_tagolas": dict(fu_Ny=[3.71,13.41,7.62,19.80], domb_agyas=[7.62,14.58,12.00,18.83], fu_K=[12.00,13.41,16.04,19.80], domb_magassag=0.25, note="két szélen sík fű pop-up esőztetővel, középen enyhén dombos évelő-ágyás (mulcs, kavics, csepegtető) – Péter megfigyelése + IMG_2498; zónahatár ELŐZETES (videóbecslés)"),
 "Ontozoszelep_akna": dict(box=[9.17,13.30,9.45,13.41], note="zöld fedlapos szelepakna a WPC sarkánál (IMG_2498 t05–07); hely ELŐZETES"),
 "Zoldtető_szegely": dict(note="világos előregyártott beton szegély a WPC és a zöldtető között, ~35–45 cm a WPC fölött, kb. térdmagas (IMG_2498) – ülőperem-adottság, terhelhetőség HIÁNYZIK – ELŐZETES"),
 "Lepcso_Ny":        dict(box=[6.48,12.10,7.68,12.40], z_from=-0.15, z_to=+0.47, fokok="3–4 fok (videó: 3 WPC fok)", status="DOKUMENTUM (nyíl) + VIDEÓ", src=SRC3),
 "Lepcso_K":         dict(box=[11.39,12.10,12.59,12.40], z_from=-0.15, z_to=+0.47, status="DOKUMENTUM (nyíl) + VIDEÓ", src=SRC3),
 "Jakuzzi_elokeszites": dict(box=[4.10,9.74,6.10,11.74], z=-0.15, note="2.00 m széles szaggatott keret a 18. oldalon (É-i éle a rajz szélén kívül → mélység HIÁNYZIK, 2.00 feltételezve); áramkiállás (3.82, 9.69); fagymentes kültéri csap (4.14, 9.0). Terhelhetőség: HIÁNYZIK (statikus nyilatkozat)", src=SRC18),
 "Korlat":           dict(vonal={"Ny":3.39,"K":16.32,"É":20.11}, magassag=1.10, anyag="antracit fém, függőleges pálcás, mellvéden (videó)", status="nyomvonal DOKUMENTUM, magasság ELŐZETES", src=SRC3),
 "Mellved_kulso":    dict(vonal={"Ny":2.83,"K":16.86,"É":20.61}, src=SRC3),
 "Erkely_13":        dict(poly=[[-0.30,-0.20],[-2.01,-0.20],[-2.01,5.69],[-1.12,5.69],[-1.12,7.90],[-0.30,7.90]], m2_terv=11.26, anyag="greslap", note="Ny-i oldal, 05.1/05.2 előtt, L-alak (külső kontúr a megvalósulási terv vonalaiból; a v1 lock téglalapja [-2.3,0,-0.3,6.05] volt); nincs a videóban – ELŐZETES", src=SRC3),
 "Homlokzat":        dict(anyag="világos szürke/fehér foltos klinker tégla, fekete nyílászárók, felette sötét álló fémburkolat (videó)", status="VIDEÓ"),
 "Ajtok_terasz":     dict(note="4.50 × 2.53 tolóajtós üvegfal (nappali) és 1.80 × 2.53 (05.3); fellépés 15 cm, 2025-10-13-i korrekció szerint módosult → helyszínen mérendő", src=SRC18),
}
facts = {
 "belmagassag": {"ertek":2.90,"status":"IGAZOLT – Péter közlése 2026-10-24 (+ brosúra)","megj":"a 18. oldalon 'm=2.85' egy szerelési/nyílásmagasság-jelölés, nem belmagasság"},
 "parketta_A902": {"ertek":"Egger Grey Treviso Oak EL2184, Classic 8/32 4V Aqua+ (591760), szegőléc 6 cm (1818766), burkolatváltó szálcsiszolt titán T-profil","status":"IGAZOLT – dokumentum (burkolatkiosztási terv, 21. old.); helyszíni fotóval megerősítendő"},
 "parketta_A811_A812": {"ertek":"Egger Grey Soria Oak EL2065, Classic 8/32 4V Aqua (593610)","status":"IGAZOLT – dokumentum (7. és 14. old.)"},
 "konyha_padlo_A902": {"ertek":"ELLENTMONDÁS: 18. old. 'kerámia' vs. 21. old. 'lam.parketta'","status":"HIÁNYZIK – hétfőn fotó"},
 "meretek_jellege": "a terven szereplő méretek vakolatlan falfelületre vonatkoznak (−1…−3 cm/oldal vakolat), tájékoztató jellegűek",
 "terulet_A902": {"belso_m2":99.94,"terasz_m2":79.22,"bontas":"T09 23.62 + T11 25.00 + T10 19.34 + erkély 11.26","zoldtető_m2":71.18,"osszes_kulter":150.40,"src":SRC3},
 "mennyezeti_hutes_futes": "a 18. oldalon zónák jelölve; fúrás/rögzítés csak panelmentes sávban – pontos panelkiosztás HIÁNYZIK",
}
out = {"verzio":"A902 geometria v2 – ELŐZETES","datum":"2026-10-24","coord":"lock v1-gyel azonos","rooms":{k:v[0] for k,v in rooms.items()},"room_notes":{k:{"terv_m2":v[1],"megj":v[2]} for k,v in rooms.items()},"terrace":terrace,"facts":facts,"diff_vs_v1":diff,
       "status":"ELŐZETES – tervdokumentumból; a lock v1-et NEM írja felül. Véglegesítés: hétfői helyszíni mérés/fotó után, Péter jóváhagyásával."}
json.dump(out,open('A902_geometria_v2_ELOZETES.json','w'),ensure_ascii=False,indent=1)
for d in diff: print(d['room'].ljust(16), d['delta_cm_W_S_E_N'])
