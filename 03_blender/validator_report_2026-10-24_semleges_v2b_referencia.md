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

**Korlát:**
- A PASS a **terv szerinti** lockhoz való egyezés, nem helyszíni igazolás.
- A bútoros stílusrétegek a v2b-n továbbra is FAIL-esek (`validator_report_2026-10-24_v2b.md`, 89 hiba): a régi LF-réteg nem használható. Új elrendezés csak tömegmodellel és új Validator-futással mehet.
