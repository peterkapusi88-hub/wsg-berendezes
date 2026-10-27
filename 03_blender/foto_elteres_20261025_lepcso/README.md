# A-902 · nappali–étkező teraszüvegfal előtti belső lépcső – FOTO_ELTERES (JAVASLAT, draft)

**Forrás:** profi helyszíni fotók 2026-10-25 – KZS_3659, KZS_3708, KZS_3726 (`08_allapotfelmeres/fotok_profi_20261025/A902/`). A lépcső a méretezett tervben és a v2b-1-k13 modellben/lockban nem szerepel (ott csak vékony fehér alsó keret van, z 0–0,05).

## Becslés (a fotóból, nem mért)
- **Magasság: kb. 15 cm (13–17 cm).**
  - KZS_3726, a nyílás keleti végén, a falsíkban: lépcső ~35 px a padló–szemöldök távolság (2,53 m) ~650 px-éhez képest → 0,136 m;
  - KZS_3659, nyugati vég: 15/270 × 2,53 = 0,14 m;
  - közeli végeken a perspektíva-korrekció után kb. 0,16–0,17 m.
- Mélység: kb. 25 cm (y 7,95–8,21; kb. 10 cm-rel a belső falsík elé nyúlik). Gyenge becslés.
- Hossz: x ≈ 3,67 (Ny-i falsarok) → ≈ 9,25 (a nyílás K-i végén ~0,3 m-rel túl).
- Burkolat: ugyanaz a laminált padló, mint a szoba (Egger Grey Treviso EL2184, terv szerint). A keret erre ül.

## Mi készült (az élő Blender és a lock érintetlen)
- `00_lepcso_wrapper.py`: a k13 blend **másolatán** egy `FOTO_ELTERES_lepcso_nappali_uvegfal` doboz (H 0,15, `v2_parketta_GreyTreviso_EL2184_foto` anyaggal); ezután a változatlan `01_render_cam02_korr.py` renderel (mentés nélkül).
- Alapkép: `A902_Alap-v2b1k13_blender_02_nappali-terasz_KORR_LEPCSO15_semleges.png`. Ez a holnapi S06–S10 és a padlójavított S01–S05 Cam_02 image 1-e.
- Validátor: üres PASS 0/0; referencia FAIL 6/3 – **azonos a lépcső nélküli KORR-futással** (régi, ismert eltérések, nem a lépcső okozza). sha a blend-másolaton előtte = utána.

## Döntés kell (Péter)
1. Elég-e a fotós becslés, vagy helyszíni mérés (mérőszalag: magasság, mélység, hossz).
2. „mehet” esetén: a lépcső felvétele a v2b-1 modellbe és a `geometry_lock_A902_v2b.json`-ba (új elem `Lepcso_nappali_uvegfal`), validátorfrissítés, majd a többi érintett kamera (Cam_05/07 terasz felől, Cam_F_3726) újrarenderelése.
3. Bútorhatás: a kanapé/szőnyeg az üvegsávnál ne a lépcsőre kerüljön; a terasz felé a küszöb kb. 15 cm.
