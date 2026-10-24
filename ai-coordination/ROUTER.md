# WSG AI-feladatirányítás – v1 (2026-10-24)

## Alapcél
Péter **Claude-ban fogalmazza meg a feladatot**. Claude dönti el, kell-e másik szakértő, és ha igen, kinek mit kell átadni. A döntést a `GOAL.md`, `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` és az érvényes költségkeret határozza meg. Ne legyen szükség arra, hogy Péter kézzel válasszon AI-t minden részfeladathoz.

**Státusz:** a GitHub-közvetített **Astra/Work indítás támogatott, de a fiókszintű eseményvezérelt feladat külön beállítandó és tesztelendő**. Codex/Gemini automatikus indítás **még nincs élesítve**. Ez a dokumentum routing-szabály és átadási szerződés, nem működő API-integráció.

## Kötelező szerepek
- **CLAUDE / saját feladat:** helyi Blender MCP, alaprajz, geometria, kivitelezési terv, technikai szerkesztés, költségösszesítés, projektállapot és munkafolyamat-koordináció.
- **ASTRA / ChatGPT Work:** *elsődleges kreatív tervező*: 10+ lehetséges, egymástól karakteresen eltérő, elképesztően drágának ható, de valósághűen kivitelezhető stílus, tervezési arányok, anyagok, forma, fény, térhasználat, render-/image prompt; valódi termékek és **független** költségellenőrzés. Nem a Blender fő kezelője.
- **CODEX / ChatGPT kódoló:** Blender Python és objektumgeometria audit, tesztek, review. Ne vezérelje párhuzamosan Claude aktív Blender-jelenetét. **A PR nem indít automatikusan Codex-feladatot a Work-triggerrel**; külön Codex Code Review/beállítás szükséges.
- **GEMINI / Flow-Veo:** főként jóváhagyott vagy döntős renderből **image-to-video stílus-/térélmény**, lehetőleg ugyanazzal a kameramozgással az összehasonlíthatóságért. **A GitHub Work-trigger nem indítja automatikusan a Geminit**; a videófeladat átadása külön megoldandó.
- **Kettős költségkontroll:** ChatGPT Astra és Claude külön forrásokból ellenőrizzen; eltérést dokumentáljanak, ne másolják egymás számait.

## Feladatosztályozás Claude számára
1. Kérdés vagy egyszerű adminisztráció, állapotellenőrzés → **Claude maga**, másik modell nélkül.
2. Új stílus, luxus „wow”, renderkoncepció, prompt, termék- vagy anyagkutatás, független költségellenőrzés → **ASTRA**. Ha műszaki Blender-változtatás kell, előbb Claude készítsen megbízható geometriai alapot.
3. Nehéz Blender/Python hiba vagy független geometriai teszt → **CODEX**. Az önálló futtatási híd még külön setup; addig külön feladat/PR review.
4. Döntős renderből élethű bejárófilm vagy stílusvideo → **GEMINI**; automatikus híd még nincs.
5. Egyszerre kreatív + műszaki + ár → Claude szervezi a sorrendet: **Claude geometria → Astra kreatív/költség → Claude árellenőrzés → Codex audit → jóváhagyás → Gemini videó**.
6. Ha a másik szolgáltatás kerete elfogyott, **ne lépj át észrevétlenül másik modellre** és ne ismételd a kérést. Írd le a feladatot mint FÜGGŐ, hogy később ugyanazzal a brief-feladattal folytatható legyen.

## Kerettakarékosság és kézi jóváhagyások
- Az Astra előkészítetlen projektbeolvasásra/egyszerű adminra nem indul.
- **Alapmodell-ajánlás:** Work/Astra közepes gondolkodási fokozat a kreatív munkához. Magas/Ultra csak igazoltan indokolt, és **Péter kifejezett jóváhagyásával**. A modellválasztás az eseményvezérelt Work-feladat beállításának függvénye; Claude egy PR-címkével **nem tudja garantáltan átkapcsolni** a modellt.
- **Egy PR = egy szakértői brief = egy Work-indítás**; ne küldj minden commitra új hívást. A Work-trigger célja első körben **ready for review** esemény, és `[ASTRA-REVIEW]` feltétel, ha támogatott.
- Fizetős API kulcsok, extra kreditek, új előfizetések nem szükségesek a PR-trigger kísérlethez; **semmilyen külön számlázható új integrációt ne aktiválj automatikusan**.
- Fizikai termékrendelés, kivitelezői ajánlatkérés, külső e-mail, publikálás, végleges jóváhagyás csak Péter explicit „mehet”-je után.

## Átadás Astra felé (egyirányú indítás)
1. Claude a közös repóból olvas, elkészíti a lehető legrövidebb, elégséges input-briefet az `ai-coordination/REQUEST_TEMPLATE.md` alapján.
2. Új ág, pl. `handoff/astra-A902-living-style-01`; brief a `ai-coordination/requests/<ID>.md` alatt. Ha a meglévő helyi Git-munka nem tiszta, ne írj felül semmit; külön, biztonságos ágat/klónt használj.
3. Claude **draft pull requestet** készít `[ASTRA-REVIEW]` címmel. Csak akkor jelöli **ready for review** állapotúra, ha minden bemenet létezik, nincs duplikált feladat, és a felhasználói limit/engedély ezt megengedi.
4. A ChatGPT Work weben külön létrehozott, GitHub PR-eseményre figyelő feladata elindulhat, és az aktuális `GOAL.md`, stíluslabor-skill, brief, releváns képek/fájlok alapján végzi a kreatív vagy független költségellenőrzést.
5. Kimenet: lehetőség szerint **PR-hozzászólás** a `WSG-ASTRA-RESULT` fejlécével, vagy a repo `ai-coordination/results/<ID>.md` fájlja külön ágon. Ha a Work jogosultsága miatt nem tud visszaírni, a Work feladatban adott eredményhez kézi átadás szükséges. **Ne állítsd, hogy visszajutott Claude-hoz, amíg tényleg nincs GitHubon.**
6. Claude olvassa az eredményt, **külön** ellenőrzi az árakat, dokumentálja az eltéréseket és javítási tervet készít. Külső beszerzés továbbra sem indul.

## Méretek és pénz
A-811/A-812/A-902: 10/10/20 M Ft **bruttó teljes költségplafon**, 10% tartalék. A nagyobb képzelt márvány/egyedi bútor nem válhat jóváhagyott valósággá anélkül, hogy konkrét anyag, méret, ár és asztalos árajánlat igazolná. Stílus-előszűrésnél óvatos sávbecslés; döntősöknél valós termék és kivitelezői ajánlat.

## Elkülönítendő státuszok
`tervezet` → `átadásra kész` → `Work indítva` → `eredmény látható` → `Claude függetlenül validálta` → `Péter jóváhagyta`. **Egy PR létrejötte nem jelenti, hogy Work futott, vagy hogy Astra eredményt küldött.**

További részletek: `ai-coordination/WORK_TRIGGER_SETUP.md`, `ai-coordination/REQUEST_TEMPLATE.md`, `ai-coordination/RESULT_TEMPLATE.md`.
