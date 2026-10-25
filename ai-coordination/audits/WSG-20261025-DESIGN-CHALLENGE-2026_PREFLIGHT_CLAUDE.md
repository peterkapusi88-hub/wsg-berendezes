# WSG DESIGN CHALLENGE 2026 – FINAL PREFLIGHT AUDIT (Claude, írásvédett, végleges 2026-10-25)

**Tárgy:** a három végleges indítóprompt (A GPT-6 Astra Medium · B Claude Fable 5.1 High · C Claude Opus 5.5 High), a végleges r2 brief és a közös verseny-baseline.
- Indítóprompt-fájlok: `ai-coordination/requests/DC2026_inditas/` (A, B, C + `00_INDITASI_UTMUTATO.md`), az előkészítő ágon `competition/inditas-20261025`.
- Közös forrásállapot: ág `competition/baseline-20261025-v3`, commit `45632b5ad5586e1f3f884a8f723c1cc13cda6da3` = main `5ebc7d7` + PR #20 r2 (`f190e5f`) + PR #19 (`cf3b523`).

**Hatókör:** csak audit és előkészítés. Nem indult versenyzői futás, nem készült versenyzői ág vagy PR, nem készült kép, nem volt merge; a baseline-commit nem változott.

**Összeférhetetlenség kimondva:** az audit első részét Claude Fable 5.1 (a B versenyző modellje), a végleges indítócsomagot Claude Opus 5.5 (a C versenyző modellje) állította össze. Ezért: a három prompt kreatív tartalma az eredeti (Péter 03:13-as csatolmánya), a változtatások mindháromban szimmetrikusak; a geometriai kapu szkriptes és kódneves; a költségkaput keresztellenőrzés végzi (B-t GPT-6, C-t Astra vagy GPT-6 – egyiket sem Claude); a döntőbíró Péter.

## Verdikt: **INDÍTHATÓ** – a három végleges indítóprompttal, a `45632b5…` baseline-commitból, Péter külön „mehet”-jével.
A futásokat Péter indítja; az indítás előtti két ellenőrzést az útmutató 2. pontja tartalmazza (a 02:52-es Astra-feladat állapota, a Work Medium-beállítása).

## A 15 ellenőrzés
| # | Kérdés | Eredmény | Megjegyzés |
|---|---|---|---|
| 1 | Azonos forráscommit és r2 brief | **IGEN** | mindhárom prompt: `45632b5ad5586e1f3f884a8f723c1cc13cda6da3` (ág `competition/baseline-20261025-v3`) + r2 brief; a korábbi `45d1e4d` és a `32ba7bd`, `a8ab8d3`, `ce06496` baseline-SHA-k elavultként jelölve (VB.1). Egyetlen, csak olvasható kivétel: a hat közös kalibráció hivatalos forrása `competition/inditas-20261025` @ `2452dfc54f26467791dccbd9ce620cd7af0435bb` (Péter 05:38). A B és C saját klónban vagy worktree-ben dolgozik. |
| 2 | 10 stílus, 3+3 TV-fal, képszám | **IGEN** | versenyzőnként 60 saját + 6 közös kalibráció = 66 képes készlet; összesen 180 saját prompt; S06/S07 teljes stílus; S03–S10 egy-egy TV-fal (r2 §11.2). |
| 3 | kep_id betű szerint | **IGEN** | regiszter 1–60 saját, 61–66 közös; a hat közös kalibráció jelölői gépileg ellenőrizve. |
| 4 | Azonos kreatív, fal-, berendezési és Hue-követelmény | **IGEN** | a VB blokk bájtra azonos (sha256 mindháromban egyezik); a fény Péter 04:40/04:49-es döntése szerint (Cam_02 kék óra / Hue TV-fal, Cam_12 nappal), a két Cam_02 kalibráció is kékórás. |
| 5 | Azonos építészeti korlátok és bútorszabadság | **IGEN** | C alapelrendezés (GEOMETRIA v2); kanapé L/U; források és anyagszabály (VB.4); étkező: 160 × 90 alap (Toni 160 igazolt, Anouk 180 nem elfogadott), kerek/ovális/bővíthető külön Blender-méretpróbával a PR #20 kerek-próbája szerint (Ø150 csak sík TV-fallal; Ø130 40 cm-es TV-bútorral U-val). |
| 6 | Kötelező utólagos Blender/Gate | **IGEN** | A 6., B 5., C 5. – azonos tartalommal; a koncepcióképek és a végső összehasonlító képek különválasztva (VB.9). |
| 7 | Integrátor nem egyszerűsít vissza V3-ra | **IGEN** | mindháromban; kiegészítve: ha az ötletet a kamera nem mutatja, a kamerát vizsgáljuk újra (VB.3). |
| 8 | Teljes 18 M, 2 M érintetlen | **IGEN** | 8,40 M közös fix (versenyfeltételezés, a végső kapun ellenőrzött) + 9,60 M stílusfüggő; teljes ≤ 18,00 M. |
| 9 | Ellenőrizetlen ár nem jogosít győzelemre | **IGEN** | a saját becslés tájékoztató; a hiányzó tételt a keresztellenőrző konzervatív benchmarkkal pótolja; a kapu a keresztellenőrzött végösszegen. |
| 10 | Végső kép csak auditált tervből | **IGEN** | koncepcióképek a kész promptokból (hero először: Cam_12 nappal, majd Cam_02 kék óra), „KONCEPCIÓ – NEM VALIDÁLT”; végső összehasonlító képek csak a kapuk után. |
| 11 | Külön ág, gyökér, PR | **IGEN** | A `competition/gpt6astra-v3-1-20261025` · `KEP004_GPT6ASTRA_V3_1_r1`; B `competition/fable51-v3-1-20261025` · `KEP004_FABLE51_V3_1_r1`; C `competition/opus55-v3-1-20261025` · `KEP004_OPUS55_V3_1_r1`; mindhárom draft PR célága a baseline-ág. Az A eredeti ágneve a 02:52-es nem verseny Astra-feladattal ütközött – átnevezve. |
| 12 | Távoli GitHub-mentés a checkpointokon | **IGEN** | CP0–záró CP, legfeljebb 6–10 promptonként; csak távolról visszaolvasott commit számít (VB.10); Astra-tartalék: csomagátadás a chatben. |
| 13 | Kreatív függetlenség | **RÉSZBEN** | a draft PR-ek láthatók – önkéntes fegyelem, kódneves bírálat; Astra a V2/V3 szerzője (strukturális előny, nem javítható); a Claude-versenyzők szöveges skilleket használhatnak (platformadottság). |
| 14 | Indokolatlan előny/hátrány | **VAN, elfogadva** | Astra Medium + kb. 26 % heti Work-keret vs. Claude High – Péter 04:03: „nekem jó így”. |
| 15 | Technikai akadály | **KEZELVE** | (a) a házirendek ütközése (Astra: friss main, main-re írás; Claude: operatív vezető, Blender) → mindhárom promptban felülírva; (b) Claude-környezetben a GraphQL nem érhető el → REST-es PR-nyitás a B/C promptban; (c) ág már létezik / megszakadt futás → VB.10; (d) a prompt kb. 41 ezer karakter – ha a Work beviteli mezője nem fogadja, az útmutató 3. pontja szerint fájlból olvastatható. |

## Bírói protokoll (változatlan elvek)
1. **Átvétel:** a három draft PR gépi teljességi ellenőrzése (60/60 + 6 KOZOS, 10 spec, BEGIN/END, helykitöltő, közel azonos szövegpárok); kódnév X/Y/Z, a hozzárendelés zárt fájlban Péternél.
2. **Koncepcióképek:** a 180 saját + 6 közös prompt képei egyesével, Claude Chrome-ból, ChatGPT Images, azonos referenciákkal; előbb minden stílus Cam_12, majd Cam_02; „KONCEPCIÓ – NEM VALIDÁLT”.
3. **Előszűrés:** Péter a 30 koncepcióból kiválasztja a továbbjutókat (javasolt 3–5).
4. **1. kapu – geometria:** mérethű Blender-tömbök, validátor, utak, székkihúzás, ajtók, TV-mélység, kamerakivágás; szükség esetén azonos látványértékű módosítás vagy második hero kamera.
5. **2. kapu – kivitelezhetőség:** kiállások, Hue-betáplálás, hűtő-fűtő mezők, asztalos-anyagszabály, rögzítés.
6. **3. kapu – költség:** keresztellenőrzés, dátumozott árak, benchmark-pótlás; a 8,40 M fix alap tételei is ellenőrzött árat kapnak; teljes ≤ 18,00 M.
7. **4. kapu – renderhűség:** a kapukon átment, szükség szerint módosított terv végső képei azonos kamerákkal és referenciákkal; eltéréslista a Gate szerint.
8. **Döntés:** Péter, a 4. kapu képei alapján; utána a kódnevek feloldása; rögzítés a GOAL §7-ben.

## Ami még nyitott (nem akadály az indításhoz)
- Hue-fajlagos árak dátumozott webshop-ellenőrzése (Chrome-ról, a költségkapu előtt).
- A 0,40 M-os tervezési fix sor tartalma.
- Hétfői (2026-10-26) helyszíni pontok: teraszajtó-szárny, káva, TV-csatlakozók, parketta dekorja, fürdő szaniterei.
- A main GOAL.md 7. pontjában a baseline v3 SHA-ja még `ce06496` (köztes állapot) – a helyes `45632b5…`; javítás a mainen Péter engedélyével.
