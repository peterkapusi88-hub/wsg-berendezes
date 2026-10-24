# Validator-riport: A-902 v2b-1-k10 – Cam_10 fürdőkamera + 06.2 akna/falblokk (2026-10-24 21:55)

**Eredmény (Validator v2, lock v2b-1-k10 + `A902_villamos.json`):**
- **Üres állapot** (stílusrétegek és minden bútor/szaniter rejtve): **PASS – 0 hiba, 0 figyelmeztetés** (`validator_v2b1_kam10_ures.json`).
- **Referencia-állapot** (beépített szaniterek láthatók): FAIL 6 / 3 – kizárólag a modell régi, egyszerűsített szaniter-tömbjei (06.2 mosdó 10 cm-rel a külső falban, zuhanytálca/üveg 2–3 cm, WC-tartály 2 cm, 06.1 törölközőszárító 3 cm). Nem lock-elemek; a 06.2 renderen terv szerinti render-réteg váltja őket (`geometry_v2/furdo06_2_beallitas.py`). Javításuk külön feladat.
- LOCK: 61 fal / 54 nyílás / 17 padló – 0 eltérés; TERASZ 43 elem – 0 változás; KAMERA 10 – teljes paraméterlap egyezik; VILLAMOS 130 kiállás – takarás 0.

**Változások (`javitasok` → `v2b-1-k10`):**
1. `cameras.Cam_10_Furdo_06_2` ÚJ – [14,50; 6,62; 1,50], [1,38; 0; −1,5708], 16 mm.
2. `walls.Akna_06_2_EK_v2b1k10` ÚJ – [15,45; 5,20; 0; 16,40; 5,81; 2,90] (KORR 2, 18. o.; burkolatkiosztás 23. o.; Kémeri-fotó 2026-10-21 14:51).
3. `rooms.furdo_06_2` → L alak.

**Bemenet / kimenet:** bemenet a `main` v2b-1 .blend (sha256 `399e5209…a0df`); kimenet ugyanazon útvonalon, sha256 `02869543…c6a1`. Szkript: `geometry_v2/kam10_rogzites_v2b1k10.py` (munkamásolaton, háttér-Blender 5.2.3). Az élő Mac-fájlhoz nem nyúltam.
**Jóváhagyás:** Péter, 2026-10-24 21:33 (KEP-004 Blender-előkészítés). Geometria-változás → draft PR; a `main`-be csak „mehet” után.
