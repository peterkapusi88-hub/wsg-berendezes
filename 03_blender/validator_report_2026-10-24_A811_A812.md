# Geometry Validator v2 – A-811 és A-812 alapmodell (2026-10-24)

| | A-811 | A-812 |
|---|---|---|
| Fájl | `WSG_A811_alaprajz_ELOZETES_20261024.blend` | `WSG_A812_alaprajz_ELOZETES_20261024.blend` |
| Lock | `geometry_lock_A811.json` | `geometry_lock_A812.json` |
| Kiállás-adat | `A811_villamos.json` (115 tétel) | `A812_villamos.json` (121 tétel) |
| **Eredmény** | **PASS – 0 hiba, 0 figyelmeztetés** | **PASS – 0 hiba, 0 figyelmeztetés** |
| LOCK falak / nyílászárók / padló | 56 / 50 / 27 elem, 0 eltérés | 64 / 62 / 35 elem, 0 eltérés |
| ERKÉLY (ELŐZETES) | 8 elem, 0 változás | 7 elem, 0 változás |
| KAMERA | 6 kamera, teljes paraméterlap; aktív: Cam_02_Nappali_erkely | ua. |
| AJTÓ | 12 nyílás (7 ajtó + 5 erkélyajtó-szárny) | 17 nyílás (7 ajtó + 2 erkélyajtó-szárny + 8 ablakszárny) |
| VILLAMOS | 115 kiállás; bútor nincs → takarás 0 | 121 kiállás; takarás 0 |

A PASS ebben az állapotban csak annyit jelent, hogy a modell egyezik a saját lockjával, és üres. Bútor nincs benne, ezért az ütközés-, ajtóforgás- és takarásvizsgálat a stílusrétegekkel lesz érdemi.

**Önteszt** (memóriában, nem mentve): próbatömbök a nyitási negyedkörökben. A validátor jelezte a 05.1-es, a 05.2-3-as, a HTH- és a nappali erkélyajtót (A-811), valamint az 05.3-as ajtót és a 05.2-es ablakszárnyat (A-812). A szabad helyen lévő tömbre nem jelzett.

## A validátor v2 bővítése (`geometry_validator_v2.py`)
- **Lakásválasztás:** a lock `gyujtemeny_elotag` kulcsa (A811/A812) választja a gyűjteményeket. Hiányában A902, így a régi lockok változatlanul működnek.
- **ERKÉLY:** az A-811 és az A-812 lockjában a tetőkert (`terrace_v2`) helyett `erkely_targyak` van; a validátor ezt vizsgálja.
- **Zsanérirány:** a nyitás iránya a zsanérhoz közelebbi nyílásvégből számolódik. Korábban pontos egyezést várt, ami az új ajtóknál 1 mm-en múlt.
- **Ablakszárny:** a nyíló ablakszárnynál (`tipus: ablak`) csak a negyedkör számít, megközelítési sáv nincs.
- **Csak A-902:** a konyhai pultköz- és a 05.2-ágyvizsgálat.
- **A-902 regresszió:** a régi és az új validátor a v2b fájlon azonos eredményt ad. FAIL – 89 hiba, 82 figyelmeztetés, Stil_LakeForest; a hiba-, figyelmeztetés-, info- és mérési lista tételesen azonos.

Részletes kimenet: `geometry_A811_A812/validator_A811.json`, `validator_A812.json`.
