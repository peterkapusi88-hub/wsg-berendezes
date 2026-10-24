# Validator-riport: A-902 v2b semleges referencia (Cam_02, Cam_03, Cam_04) – 2026-10-24 13:36

**Eredmény: PASS – 0 hiba, 0 figyelmeztetés.** A teljes kimenet: `04_renderek/semleges_v2b/validator_v2b_referencia.json`.

**Bemenet:**
- `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` **másolata** a felhős munkaterületen, sha256 `c27931e053b0b04e79c41609b8ae0f82c5c05402850809a30996d2551221d9c2`.
- Az élő `~/Downloads/WSG_A902_stilusok.blend`-hez és a repóbeli .blend-ekhez nem nyúltam; a módosított másolatot nem mentettem vissza.

**Futtatás:**
- `03_blender/geometry_validator_v2.py`, lock: `geometry_lock_A902_v2b.json`, kiállások: `01_alaprajzok/villamos_kiallasok/A902_villamos.json`.
- A `03_blender/geometry_v2/render_semleges_v2b_referencia.py` hívja, a megjelenési módosítások után és a render előtt, ugyanazon a másolaton.

| Ellenőrzés | Eredmény |
|---|---|
| LOCK – falak | 60 elem, 0 eltérés |
| LOCK – nyílászárók | 54 elem, 0 eltérés |
| LOCK – látható padlók | 17 elem, 0 eltérés |
| TERASZ v2 (tetőkert) | 43 elem, 0 változás |
| KAMERA | 9 kamera teljes paraméterlappal egyezik; aktív: Cam_02 |
| BURKOLÓ / ÜTKÖZÉS / AJTÓ | 0 látható bútor (szándékosan üres); 11 ajtónyílás szabad |
| VILLAMOS | 130 terv szerinti kiállás; takarás 0 |
| KONYHA | nincs pultsor a látható rétegben → a 85 cm-es köz itt nem mérhető (K1 nyitott) |

**Mit változtat a szkript a másolaton (csak megjelenés, geometria nem):**
- Rejtve: régi bútor (`A902_Butor`), `Stil_LakeForest`, `Stil_Zenit`, régi sík terasz (`A902_Terasz`), narancs JELÖLŐ-k, mesterséges fények, nap.
- Fal és mennyezet semleges fehér (0,82). A `Fal_05_1_nappali_0` (a nappali nyugati válaszfala) és a `Kulso_E_05_1_0` falon maradt `Z_tapeta_greige` anyag fehérre cserélve.
- Padló: procedurális EL2184-közelítés (1292×193 mm, É–D, 4V horony).
- Üveg: átlátszó + Fresnel; a hátoldali lapon csak átengedés.
- Ég: egyenletes, semleges, nap nélkül; portálfények a 4 külső üvegezésben.
- Új, lockon kívüli gyűjtemények: `Ref_v2b_szegelyleces` (6 cm-es szegőléc, 66 szakasz) és `Ref_v2b_portalok`.
- A régi bútorral együtt a beépített szaniterek is rejtve vannak; a három nézetből nem látszanak.
- **Csak a renderhez, a Validator futása után:** a vízszintes nyílászáró-profilok (`_also`, `_felso`, 8 objektum) mélysége +2 mm (oldalanként 1 mm). Az egymásba érő, egysíkú profildobozok különben fekete foltot adnak a Cyclesben. Ez kisebb a lock 1 cm-es tűrésénél, és a lockolt geometriát nem érinti.
- **Ugyanígy a falaknál** (szintén csak a renderhez, a Validator után): ahol két falhasáb átfed, és lapjuk egy síkban van, a kisebb hasáb azon lapja vízszintesen 1 mm-rel befelé kerül.
  - Ok: a konyhai szekrényfülke sarkánál (`Fal_szekrenyfulke_E_v2b` / `Beepitett_szekreny_eloter`) a Cam_03-on keskeny fekete rés jelent meg.
  - Érintett falak: 9.
  - A Cam_02 nézetben egyik sem látszik, ezért a Cam_02 a javítás előtti futásból maradt; a Cam_03 és a Cam_04 a javítással készült.

**Modellhiba – a Validator nem jelzi:** a v2 tetőkert nyugati mellvédje (`v2_Mellved_Ny`, x 2,83–3,39, y 8,50–20,61, z −0,45…0,47) belelóg a 05.1 északi fülkéjébe.
- Átfedés: x 2,83–3,02, y 8,50–8,95, a padló fölött 47 cm.
- A `Pillér_05_1_EK` és a `Kulso_E_05_1_0` falhasábbal is átfed.
- A Cam_04 referencia-renderen erre az egy kamerára rejtve van. Javítás a tetőkert-modellben kell: a mellvéd ennél az x-nél legfeljebb y ≈ 9,25-ig tarthat.
- Javasolt új Validator-ellenőrzés: „terasz ↔ helyiség- és falátfedés”.

**Két rés a homlokzaton a v2b-javítás után – a Validator nem jelzi.**

Új, csak olvasó ellenőrzés: `03_blender/geometry_v2/burok_zartsag_ellenorzes.py`. 1 cm-es rácson, 0,3 / 1,5 / 2,6 m magasságban elárasztja a falakon és nyílászárókon kívüli teret; a 4 cm alatti rés zártnak számít.

| Hol | Rés | Ok | Javasolt lockjavítás |
|---|---|---|---|
| 05.1 északi fülke ÉK-i sarka (x 2,95–3,02, y 8,95–9,25) | 7 cm | a v2b a `Pillér_05_1_EK`-t x 3,02-re tolta, a `Kulso_E_05_1_0` fal maradt x 2,95-ig | `Kulso_E_05_1_0` x1: 2,95 → 3,02 |
| előtér déli homlokzata (x 6,60–6,70, y −0,30–0,00) | 10 cm | a v2b a `Kulso_D_eloter_sarok_0`-t x 6,70-re tolta, a `Kulso_D_05_2_furdo_0` maradt x 6,60-ig | `Kulso_D_05_2_furdo_0` x1: 6,60 → 6,70 |

- A Cam_04 referencián az első rés fényrést adna. Ezért **csak a renderhez** egy fehér hézagzáró hasáb zárja (`Ref_v2b_hezagzaras`).
- A második rés a három referencianézetből nem látszik.
- A teraszüvegek tokja és a falkáva között modell-egyszerűsítésként kb. 3 cm-es rés van (tűrésen belül); ez a képen nem látszik.

**Korlát:**
- A PASS a **terv szerinti** lockhoz való egyezés, nem helyszíni igazolás.
- A bútoros stílusrétegek a v2b-n továbbra is FAIL-esek (`validator_report_2026-10-24_v2b.md`, 89 hiba): a régi LF-réteg nem használható. Új elrendezés csak tömegmodellel és új Validator-futással mehet.
