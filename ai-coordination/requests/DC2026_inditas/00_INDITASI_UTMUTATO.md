# WSG Design Challenge 2026 – indítási útmutató (végleges, 2026-10-25)

**Mi ez:** a három versenyző teljes, önálló indítóüzenete és a hozzá tartozó rövid teendőlista. Az indítóüzenetek ezen az előkészítő ágon vannak: `competition/inditas-20261025` (a baseline-commitból ágazik, a baseline-ágat nem módosítja).

**Közös forrásállapot mindhárom futáshoz:** ág `competition/baseline-20261025-v3`, commit **`45632b5ad5586e1f3f884a8f723c1cc13cda6da3`**.

## 1. A három indítóüzenet
| | Versenyző | Hol fut | Bemásolandó fájl (ezen az ágon) | Saját ág (a baseline-commitból) | Saját mappa | PR-jelölő | Költség-keresztellenőrző |
|---|---|---|---|---|---|---|---|
| A | GPT-6 Astra, **Medium** | ChatGPT Work, új feladat | `ai-coordination/requests/DC2026_inditas/A_GPT6_Astra_Medium_ChatGPT_Work.md` | `competition/gpt6astra-v3-1-20261025` | `05_promptok/KEP004_GPT6ASTRA_V3_1_r1/` | `WSG-COMPETITION-RESULT: GPT6ASTRA-V3_1` | Claude |
| B | Claude Fable 5.1, **High** | új Claude-munkamenet, a repóval | `ai-coordination/requests/DC2026_inditas/B_Claude_Fable51_High.md` | `competition/fable51-v3-1-20261025` | `05_promptok/KEP004_FABLE51_V3_1_r1/` | `WSG-COMPETITION-RESULT: FABLE51-V3_1` | GPT-6 Chat |
| C | Claude Opus 5.5, **High** | új Claude-munkamenet, a repóval | `ai-coordination/requests/DC2026_inditas/C_Claude_Opus55_High.md` | `competition/opus55-v3-1-20261025` | `05_promptok/KEP004_OPUS55_V3_1_r1/` | `WSG-COMPETITION-RESULT: OPUS55-V3_1` | Astra vagy GPT-6 |

Mindhárom draft PR célága: `competition/baseline-20261025-v3`. Terjedelem: A 42 699, B 40 746, C 41 343 karakter.

## 2. Indítás előtt (Péter, kb. 2 perc)
1. **ChatGPT Work:** nézd meg, fut-e még a 02:52-kor indított Astra V3.1 (nem verseny) feladat. Ha fut, állítsd le vagy hagyd lefutni – a versenyző A **új** Work-feladatban induljon, ne abban a beszélgetésben.
2. **Work:** ellenőrizd a felületen, hogy **Medium** a gondolkodási szint.
3. **Claude:** két új munkamenet a WSG projektben, a `wsg-berendezes` repóval: Fable 5.1 High és Opus 5.5 High. Ne ebben a beszélgetésben, és ne a kameracsomagos munkamenetben.

## 3. Bemásolás
- A GitHubon nyisd meg a fájlt az `competition/inditas-20261025` ágon → „Copy raw file” → első üzenetként szó szerint beilleszted. Mást ne írj mellé.
- **Ha a Work beviteli mezője túl hosszúnak találja**, ezt az egy mondatot küldd helyette:
  > Olvasd el és hajtsd végre szó szerint a `peterkapusi88-hub/wsg-berendezes` repó `competition/inditas-20261025` ágán lévő `ai-coordination/requests/DC2026_inditas/A_GPT6_Astra_Medium_ChatGPT_Work.md` fájlt; a munkát a fájlban megadott baseline-commitból (`45632b5…`) végezd, ne az előkészítő ágból.

## 4. Az első jel: CP0 (mindhárom versenyzőnél ugyanaz)
A GitHubon megjelenik: a saját ág, benne `00_README.md`, `00_CHECKPOINT_NAPLO.md` és a 66 soros `01_MANIFEST_66.csv` (60 PENDING + 6 KOZOS), valamint egy draft PR a `competition/baseline-20261025-v3` ágra, a PR-jelölővel. Ha 30–60 percen belül nincs CP0, a versenyző valószínűleg a GitHub-írásnál akadt el – kérdezz rá (a promptok szerint ezt azonnal jelezniük kell).

## 5. Folytató üzenet megszakadt futás után (csak új munkamenetben)
> WSG DC2026 – **<A | B | C>** folytatás. A `<saját ág>` legutóbbi commitja, a `<saját mappa>/00_CHECKPOINT_NAPLO.md` és `01_MANIFEST_66.csv` alapján készítsd el a PENDING és DRAFT tételeket ugyanazzal az indítóüzenettel (`ai-coordination/requests/DC2026_inditas/<saját fájl>`, ág `competition/inditas-20261025`) és checkpointolással. A COMPLETE tételeket ne írd újra; az ágat ne hozd létre újra, és ne rebase-eld.

(Az r2 brief C részének régi folytató üzenete nem használható: az a nem verseny Astra-feladat ágára mutat.)

## 6. Mi változott az eredeti (ChatGPT által összeállított) promptokhoz képest
- A kreatív tartalom megmaradt; az elejükre került a közös **VB blokk** (§0 v3.1), mindháromban bájtra azonosan (sha256 `64a7bb93…8bb9b6`; a `WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` 1. pontja ugyanez). Számozása VB.1–VB.10, mert az r2 briefnek saját 0. fejezete van.
- A 11 célzott szövegcsere a törzsszövegben is végrehajtva – nyomkövetés fejezetenként: `WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md` 2. pont.
- **A versenyző A ágneve megváltozott:** `astra/creative-upgrade-v3-1-r1-20261025` helyett `competition/gpt6astra-v3-1-20261025` (mappa és jelölő ugyanígy), mert az eredeti nevek a 02:52-es nem verseny Astra-feladatéval azonosak.
- Mindhárom prompt kimondja, hogy a saját házirend erre a feladatra nem érvényes, ahol ütközik (Astra: „friss main, main-re írás, PR nélkül, P902_24A”; Fable/Opus: „operatív vezető, Blender, main-re írás”).
- Új, mindháromban azonos elemek: a kanapé L/U-szabály, a források és az anyagszabály, az elavult anyagok listája, az r2 felülírt fejezetei, a validátor-státusz, az összefoglaló kötelező fejléce, a stílusonkénti asztal-/teraszajtó-eset.

## 7. Gépi ellenőrzés (2026-10-25)
- A VB blokk a három promptban és a közös fájlban azonos (sha256 egyezik).
- Mindhárom promptban szerepel a teljes baseline-SHA, a saját ág, mappa, összefoglaló és PR-jelölő; a másik két versenyzőé egyikben sem.
- Nincs elavult kifejezés: a `45d1e4d` csak az elavult-listában; nincs „66 prompt” mint saját kimenet, „a többi 62”, „36–38 cm”, „2–3 alternatíva”, „a kamera még készül”, „hiányzó tétel = nem igazolt”, `WSG-ASTRA-RESULT`; az Anouk 180 csak „nem elfogadott” összefüggésben.
- Fény: egyetlen Cam_02-sor sem nappali, egyetlen Cam_12-sor sem esti.
- A hat közös kalibrációs prompt jelölői rendben; a nem igazolt méretek és a nem igazolt krém „FORSAND” front ezen az ágon kivéve (`05_promptok/KEP004_KALIBRACIO_C1_C2_V3_1/00_README.md` – változásnapló). A képgeneráláskor ezt a tisztított változatot használjuk.

## 8. Tilos (változatlanul)
Képgenerálás, PR-merge, Blender-módosítás, rendelés – külön engedély nélkül. Ez az ág, a baseline-ág és a main nincs összefésülve; a különbség itt nézhető meg: `https://github.com/peterkapusi88-hub/wsg-berendezes/compare/competition/baseline-20261025-v3...competition/inditas-20261025`.

**Összeférhetetlenség:** a végleges csomagot Claude Opus 5.5 állította össze – ez a C versenyző modellje. Ezért a változtatások mindhárom promptban szimmetrikusak, a C-terv költségét nem Claude ellenőrzi, a bírálat kódneves, és a döntés Péteré.
