# Validator-riport: A-902 lock-javítás v2b-1 – homlokzati rések, tetőkert-mellvéd (2026-10-24 17:20)

**Eredmény:**
- **Validator v2** (lock v2b-1 + javított .blend, bútorrétegek rejtve, mint a semleges referenciánál): **PASS – 0 hiba, 0 figyelmeztetés**. Javítás előtt is PASS 0/0.
- **Burokzártság: ZÁRT.** Előtte 2 rés (7 cm és 10 cm), mindhárom vizsgált magasságban.
- **Terasz ↔ belső tér: nincs átfedés.** Előtte a `v2_Mellved_Ny` 3 átfedése.
- **Regresszió:** a teljes, bútoros fájlon a Validator kimenete a javítás előtt és után azonos: FAIL 89/82. Ezek a régi Lake Forest-réteg ismert hibái, nem e javítás tárgyai.

**Jóváhagyás:** Péter, 2026-10-24 17:06 („igen, ha nem túl sok idő”). Geometria-változás, ezért draft PR; a `main`-be csak Péter „mehet”-je után.

**Bemenet és kimenet:**
- Bemenet: a repóbeli `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` (a PR #7 utáni `main`-változat a kiállás-réteggel), sha256 `febb285e…75e1`.
- Kimenet: ugyanez a fájl javítva, sha256 `399e5209…a0df`.
- Az élő Mac-fájlhoz (`~/Downloads/WSG_A902_stilusok.blend`) nem nyúltam.
- Szkript: `03_blender/geometry_v2/lockjavitas_v2b_burok.py`. Idempotens: a második futás 0 változást ad.

## Változások

| # | Elem | Régi | Új | Miért |
|---|---|---|---|---|
| 1 | `Kulso_E_05_1_0` x1 | 2,95 | 3,02 | A v2b a `Pillér_05_1_EK`-t x 3,02-re tolta, a fülke északi fala nem követte: 7 cm-es rés a homlokzaton (y 8,95–9,25). |
| 2 | `Kulso_D_05_2_furdo_0` x1 | 6,60 | 6,70 | A v2b a `Kulso_D_eloter_sarok_0`-t x 6,70-re tolta: 10 cm-es rés a déli homlokzaton (y −0,30–0,00). |
| 3 | `v2_Mellved_Ny` y0 (tetőkert, ELŐZETES) | 8,50 | 9,25 | A mellvéd 47 cm magasan belelógott a 05.1 fülkébe (x 2,83–3,02, y 8,50–8,95), a pillérbe és a fülke északi falába. Most a szerkezeti fal külső síkjánál kezdődik. |
| 4 | Anyag: `Fal_05_1_nappali_0`, `Kulso_E_05_1_0` (csak a .blend-ben) | `Z_tapeta_greige` | `Fal_feher` | A falon maradt Zenit-tapéta a Gate szerint falszínhiba; ez okozta a PR #7-képek bézs falát. Az anyag a fájlban marad (fake user), egy későbbi, árazott tapétafelülethez. |

A lockban a `javitasok` mező rögzíti a fentieket. A `statusz.terasz_v2` szövege frissült.

## Ellenőrzés

| Ellenőrzés | Előtte | Utána |
|---|---|---|
| Validator v2, bútorrétegek rejtve | PASS 0/0 | PASS 0/0 |
| Validator v2, teljes fájl (régi LF-réteg látható) | FAIL 89/82 | FAIL 89/82, a hiba- és figyelmeztetéslista azonos |
| Burokzártság (1 cm-es rács, z = 0,3 / 1,5 / 2,6 m, 4 cm alatti rés zártnak számít) | 2 rés | ZÁRT |
| Terasz ↔ helyiség, fal, nyílászáró (átfedés > 1 cm mindhárom irányban) | 3 átfedés | nincs |
| .blend, mind a 967 objektum: befoglaló doboz, anyag, gyűjtemény, láthatóság, kamera | – | csak a fenti 3 doboz és 2 anyag változott |
| Cam_04 ellenőrző render (közepes minőség) a javított fájlból, renderhez szóló trükkök nélkül | a referenciához rejtés és hézagzárás kellett | nincs doboz a fülkében, nincs fényrés; a hézagzárás és a rejtés nem futott (`v2b1_ellenorzo_Cam04_mid.png`) |

Az átfedés-ellenőrzés új: `03_blender/geometry_v2/burok_zartsag_ellenorzes.py` 2. része. Kilépési kód 0, ha zárt és nincs átfedés.

## Ami nem változott, és ami nyitott
- Minden más fal, nyílászáró, padló, teraszelem és kamera változatlan; a kiállás-réteg (PR #7) is.
- A `Pillér_05_1_EK` 1 cm-es síkeltérése (y 8,04 vs. a fal 8,05) a hétfői mérésig marad.
- A mellvéd x 3,32–3,39 közti, 7 cm-es csíkja most y 9,25-nél kezdődik. Ott a ház fala y 8,35-nél van, így a pillér keleti oldala mellett egy 7 cm széles, kb. 75 cm hosszú sáv üres maradt. A tényleges csatlakozást a hétfői bejáráson kell megnézni.
- A régi tetőkert-forrásfájl (`WSG_A902_v2_terasz_ELOZETES_20261024.blend`) ugyanezt a hibás mellvédet tartalmazza. Elavult alap, nem javítottam.

## Hatás a meglévő képekre
- **`04_renderek/semleges_v2b/`** (az összehasonlító alap): érvényes marad. A Cam_04 ott renderhez szóló rejtéssel és hézagzárással készült; ez ugyanazt adja, mint a javított geometria. A render-szkript ezeket a lépéseket mostantól csak a javítás előtti lockkal futtatja.
- **`04_renderek/A902_alap_v2b/`** (PR #7): a Cam_04 képen a mellvéd 47 cm-es doboza látszik a fülke sarkában. Péter döntése szerint ez a készlet nem alap. Ha újrarenderelik (PR #10), a javított fájlból a doboz eltűnik.

## Viszony a nyitott PR-ekhez
- **PR #9** (A-811/A-812) a `geometry_validator_v2.py`-t módosítja. Ez a PR a validátorhoz nem nyúl, ezért nem ütköznek.
- **PR #10** (A902_alap_v2b falanyag, csak renderben): a .blend-ben most javított anyag mellett a PR #10 cseréje hatástalan, de nem ütközik.
