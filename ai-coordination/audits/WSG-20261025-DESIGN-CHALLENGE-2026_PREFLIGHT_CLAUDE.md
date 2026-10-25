# WSG DESIGN CHALLENGE 2026 – FINAL PREFLIGHT AUDIT (Claude Fable 5.1, írásvédett, 2026-10-25 05:05 CET)

**Tárgy:** a három indítóprompt (A GPT-6 Astra Medium · B Claude Fable 5.1 High · C Claude Opus 5.5 High), a végleges r2 brief (`ai-coordination/requests/WSG-20261025-ASTRA-CREATIVE-UPGRADE-V3_1_r2.md`, commit `978df16`) és a közös forráscommit `45d1e4d` ellen.
**Hatókör:** csak audit. Nem indult versenymunka, nem készült versenyzői ág vagy PR, nem módosult közös forrásfájl, nem készült kép. A közös bemeneteket (fix-alap, Hue-alap, kalibráció, §0 blokk) külön draft PR-ben adom át.
**Összeférhetetlenség kimondva:** az auditor (Fable) a B versenyző modellje. Ezért a geometriai kapu szkriptes és kódneves, a költségkaput keresztellenőrzés végzi (Fable tervét GPT-6), a döntőbíró Péter.

## Verdikt: **INDÍTHATÓ – a közös §0 blokk beillesztése és a 2. pont nyolc szövegcseréje után.**
Enélkül a három modell a 36–38 cm-es, már elvetett elrendezésre, egy nem létező Cam_03-ra és egymástól eltérő költségalapra tervezne; a kanapé L/U követelménye egyik promptban sincs.

## A 15 ellenőrzés
| # | Kérdés | Eredmény | Megjegyzés / javítás |
|---|---|---|---|
| 1 | Azonos forráscommit és r2 brief | **IGEN** | mindhárom `45d1e4d` + r2. A `45d1e4d` létezik a mainen (02:53, GOAL-frissítés), a brief `978df16`-ban. Megjegyzés: a `45d1e4d` **nem** tartalmazza a PR #18 elrendezést és a közös bemeneteket → a §0 blokk hivatkozza őket útvonallal; a rögzített commit marad a kreatív forrásbázis. |
| 2 | 10 stílus, 3+3 TV-fal, 66 prompt | **IGEN, módosítva** | Péter 04:03: a 6 kalibrációt egyszer Claude írja → versenyzőnként 60 prompt + 10 spec; a manifest 66 soros marad (§0.4). |
| 3 | kep_id betű szerint | **IGEN** | mindhárom a regisztert hivatkozza; a kalibrációs 6 ID-t gépi ellenőrzéssel igazoltam a közös promptokon. |
| 4 | Azonos kreatív/fal/Hue-követelmény | **IGEN** | a három szöveg tartalmilag azonos; a Hue az r2 §2–4-re támaszkodik → közös fajlagos árak a HUE_ALAPCSOMAG_v1-ben. |
| 5 | Azonos építészeti korlátok és bútorszabadság | **IGEN, hiányos** | kanapé L/U szabály hiányzik mindháromból (GOAL §4.7) → §0.2. A beszerzési források (Kave Home/Westwing/IKEA/asztalos, Egger-anyagszabály) sincsenek nevesítve → §0.3. |
| 6 | Kötelező utólagos Blender/Gate | **IGEN** | A §6, B §5, C §5 azonos tartalmú. |
| 7 | Integrátor nem egyszerűsít vissza V3-ra | **IGEN** | mindháromban kimondva. |
| 8 | Teljes 18 M, 2 M érintetlen | **IGEN, pontosítva** | „teljes lakásszintű” költségvetés versenyzőnként 10× → közös fix-alap 8,40 M + stílusfüggő 9,60 M (`KOZOS_FIX_ALAP_v1`), így a három modell azonos alapon és feleslegesen nem árazza a konyhagépet tízszer. |
| 9 | Ellenőrizetlen ár nem jogosít győzelemre | **IGEN, enyhítve** | a „hiányzó tétel = nem igazolt” formai kizárás helyett benchmark-pótlás (§0.5); a saját becslés tájékoztató → nincs lowball-ösztönző. |
| 10 | Végső kép csak auditált tervből | **IGEN, kiegészítve** | Péter: a 66 prompt képei koncepció státuszban azonnal készülnek (hero először); a végső összehasonlító képek a kapuk után (§0.6). Ez nem mond ellent a brief B részének. |
| 11 | Külön ág/gyökér/PR | **IGEN** | A `astra/creative-upgrade-v3-1-r1-20261025`, B `competition/fable51-v3-1-20261025`, C `competition/opus55-v3-1-20261025`; gyökerek `KEP004_ASTRA/FABLE51/OPUS55_V3_1_r1`. |
| 12 | Távoli GitHub-mentés a checkpointokon | **IGEN** | mindháromnál; Astra GitHub-írása a projektben korábban akadozott (STYLE10-002 mentés elmaradt) → fallback §0.8. |
| 13 | Kreatív függetlenség | **RÉSZBEN** | a draft PR-ek a repóban láthatók, a tilalom önkéntes fegyelem; Astra a V2/V3 szerzője (strukturális előny, nem javítható). Kódneves bírálat (§0.7) csökkenti a hatást. |
| 14 | Indokolatlan előny/hátrány | **VAN, elfogadva** | Astra Medium + ~26 % heti keret vs. Claude High – Péter 04:03: „5 nekem jó így”. Dokumentálva; az eredmény értékelésekor tudni kell. |
| 15 | Technikai akadály | **KEZELVE** | (a) Cam_03 nem létezett → K1 (Péter 04:09); (b) elrendezés nem volt rögzítve → C (Péter 04:09); (c) 66 prompt egy futásban a kontextuskorlát miatt megszakadhat → §0.8 folytatási protokoll; (d) Astra V3.1 03:58-kor még CP0 nélkül – indítás előtt Workben ellenőrizendő, nem akadt-e el; (e) a PR #17/#18 kameracsomag (Cam_03 K1 + Cam_12 újrakivágás) még fut a másik Claude-munkamenetben – a versenyzők a §0.1 szöveges leírásából dolgoznak, a FRAME LAYOUT-ot utólag Claude adja. |

## Bírói protokoll (javasolt végső eljárás)
1. **Átvétel:** mindhárom draft PR gépi teljességi ellenőrzése (60/60 + 10 spec, BEGIN/END, helykitöltő-keresés, közel azonos szövegpárok). Kódnév X/Y/Z kiosztása, a hozzárendelés zárt fájlban Péternél.
2. **Koncepcióképek:** a 66 (60 + 6 közös) prompt képei stílusonként, hero először (Cam_12, Cam_02 → 60 kép; utána a többi 120 + 6), Claude Chrome-ból, azonos generátor és referencia, „KONCEPCIÓ – NEM VALIDÁLT” státusz. Átvétel a 66-os keret archiválási rendje szerint.
3. **Előszűrés:** Péter a 30 koncepcióból kiválasztja a továbbjutókat a hero képek alapján (javasolt 3–5).
4. **1. kapu – geometria:** a továbbjutók elemlistájából mérethű Blender-tömbök, validator, utak/székkihúzás/ajtók/TV-mélység (`tv_melyseg.py`), Cam-ok kivágása; eredmény fájlban. Ha nem fér: azonos látványértékű módosítás, dokumentálva; jelentős kompromisszum → Péter.
5. **2. kapu – kivitelezhetőség:** kiállások, Hue-betáplálás, hűtő-fűtő mezők, asztalos-anyagszabály, rögzítés.
6. **3. kapu – költség:** keresztellenőrzés a 3. pont beosztásával, azonos fix-alap, dátumozott árak, benchmark-pótlás; ≤ 18,00 M, tartalék érintetlen.
7. **4. kapu – renderhűség:** a kapukon átment, szükség szerint módosított terv végső képei azonos Blender-kamerákkal és referenciákkal; geometriai eltéréslista a Gate szerint; PASS/FAIL.
8. **Döntés:** Péter, a 4. kapu képei alapján (Cam_02 + Cam_12 + Cam_04/11 kötelező, Cam_03 és Cam_10 kiegészítő), kódnevek feloldása utána. Dokumentálás a GOAL §7-ben.

## Ami még nyitott (nem akadály az indításhoz)
- Hue-fajlagos árak dátumozott webshop-ellenőrzése (a Claude-munkamenetből nem volt elérhető; Chrome-ról a kapu előtt).
- A 0,40 M-os tervezési fix sor tartalma (külső tervező nincs, IKEA-konyhatervezés és asztalos-rajz igen).
- A kameracsomag (Cam_03 K1 + Cam_12) validálása és Péter merge-engedélye (másik munkamenet, PR #17/#18).
