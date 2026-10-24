# Geometry Validator v2 – A-811 és A-812 alapmodell, geometria v2 (2026-10-24)

A geometria v2 a független tervhűségi ellenőrzés javításait tartalmazza (5 HIBA, 11 FIGYELEM; lista: `geometry_A811_A812/README.md`, „v2”). Az alábbi számok a v2 modellre vonatkoznak.

| | A-811 | A-812 |
|---|---|---|
| Fájl | `WSG_A811_alaprajz_ELOZETES_20261024.blend` | `WSG_A812_alaprajz_ELOZETES_20261024.blend` |
| Lock | `geometry_lock_A811.json` | `geometry_lock_A812.json` |
| Kiállás-adat | `A811_villamos.json` (115 tétel) | `A812_villamos.json` (121 tétel) |
| **Eredmény** | **PASS – 0 hiba, 0 figyelmeztetés** | **PASS – 0 hiba, 0 figyelmeztetés** |
| LOCK falak / nyílászárók / padló | 60 / 50 / 31 elem, 0 eltérés (v1: 56 / 50 / 27) | 69 / 63 / 36 elem, 0 eltérés (v1: 64 / 62 / 35) |
| ERKÉLY (ELŐZETES) | 8 elem, 0 változás | 13 elem (+6 francia erkély korlát), 0 változás |
| KAMERA | 6 kamera, teljes paraméterlap; aktív: Cam_02_Nappali_erkely | ua. |
| AJTÓ | 12 nyílás (7 ajtó + 5 erkélyajtó-szárny) | 17 nyílás (7 ajtó + 2 erkélyajtó-szárny + 8 ablakszárny) |
| VILLAMOS | 115 kiállás; bútor nincs → takarás 0 | 121 kiállás; takarás 0 |

**A PASS csak annyit jelent, hogy a modell egyezik a saját lockjával, és üres. A tervhűséget nem igazolja:** a v1 is PASS volt, pedig 5 tervi hiba volt benne. Bútor nincs a modellben, ezért az ütközés-, ajtóforgás- és takarásvizsgálat a stílusrétegekkel lesz érdemi.

**Tervhűség (v2):**
- a független ellenőrzés minden HIBA- és FIGYELEM-tételét a PDF CAD-rétegein újraellenőriztem és javítottam;
- a geometria-szkript réskeresése (6 cm alatti rés vagy lyuk az alaprajzi unióban): 0 / 0;
- réskeresés a kész lockon 5 magasságban (0,30 · 1,20 · 2,20 · 2,45 · 2,65 m): 0 rés mindkét lakásban;
- mind a 12 beltéri ajtó falnyílásának két végén a terven ott a lezáró falvonal.

**Önteszt** (memóriában, nem mentve; a .blend md5-je változatlan): próbatömb minden nyitási negyedkör belsejében. A validátor mind a 12 (A-811) és mind a 17 (A-812) nyílásnál jelzett; a szabad helyen lévő tömbre nem.

## A validátor v2 bővítése (`geometry_validator_v2.py`)
- **Lakásválasztás:** a lock `gyujtemeny_elotag` kulcsa (A811/A812) választja a gyűjteményeket. Hiányában A902, így a régi lockok változatlanul működnek.
- **ERKÉLY:** az A-811 és az A-812 lockjában a tetőkert (`terrace_v2`) helyett `erkely_targyak` van; a validátor ezt vizsgálja.
- **Zsanérirány:** a nyitás iránya a zsanérhoz közelebbi nyílásvégből számolódik. Korábban pontos egyezést várt, ami az új ajtóknál 1 mm-en múlt.
- **Ablakszárny:** a nyíló ablakszárnynál (`tipus: ablak`) csak a negyedkör számít, megközelítési sáv nincs.
- **Csak A-902:** a konyhai pultköz- és a 05.2-ágyvizsgálat.
- **A-902 regresszió:** a régi és az új validátor a v2b fájlon azonos eredményt ad. FAIL – 89 hiba, 82 figyelmeztetés, Stil_LakeForest; a hiba-, figyelmeztetés-, info- és mérési lista tételesen azonos.

Részletes kimenet: `geometry_A811_A812/validator_A811.json`, `validator_A812.json`.
