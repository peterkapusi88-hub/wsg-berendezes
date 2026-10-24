# WSG AI-indítás – ugyanaz a friss tudás Claude, ChatGPT Work és Codex számára

## 1. Hiteles projektforrás
Repo: `peterkapusi88-hub/wsg-berendezes` (`main`). GitHub a közös verziózott tudástár, nem közös AI-memória vagy folyamatos üzenetbusz. **Minden új munkamenet elején olvassátok be a legfrissebb változatot, ne régi feltöltött másolatból dolgozzatok.**

Kötelező sorrend:
1. `GOAL.md` – aktuális projektállapot, keret, méretek, döntések.
2. `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` – közös tervezési filozófia, sok stílus, drágának ható megvalósítható luxus, költséghűség.
3. Szerep szerint `CLAUDE.md`, `OPENAI_instructions.md` vagy `AGENTS.md`.
4. A feladathoz szükséges `06_koncepcio/`, `03_blender/`, `02_referenciak/`, `04_renderek/`, `05_promptok/`.

## 2. ChatGPT Projekt beállítása (felhasználói lépés)
ChatGPT oldalsáv → Új projekt → `WSG – stíluslabor` → hárompontos menü → Projektbeállítások → Projektutasítások:

> A `peterkapusi88-hub/wsg-berendezes` privát GitHub-repóhoz tartozó Westside Grand projekten dolgozol. Minden Work-feladat elején keresd le az aktuális `GOAL.md`, `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` és `OPENAI_instructions.md` fájlokat a csatlakoztatott GitHubról; ha nem sikerül, ezt jelezd és ne találj ki projektadatokat. Zenit és Lake Forest csak két lehetséges stílus; akár 10+ stílust hasonlíts össze azonos valós geometriával és 10/10/20 M Ft-os bruttó teljes kerettel, 10% tartalékot figyelembe véve. Elsődleges cél: elképesztően drágának és egyedinek ható, nem giccses, mégis valóságosan megépíthető lakás. A forma, szín, térszervezés, fény, anyag és panoráma együtt teremtik a luxust. A végleges render minden jelentős eleme valós termékhez vagy specifikált, beárazott egyedi bútordarabhoz kötődjön; az eltéréseket jelezd. Work: kreatív koncepció + független termékkutatás és árellenőrzés. Claude: Blender-kivitelezés + ettől független költségellenőrzés. Codex: műszaki-geometriai audit. Külső küldés, rendelés, fizetés csak Péter „mehet” jóváhagyása után.

Indíts Work-feladatot **ezen a ChatGPT Projekten belül**. A GitHub-connector engedélyezése szükséges az adott repóra. A ChatGPT Projectbe manuálisan feltöltött fájlok pillanatképek, ezért változás után újra kell őket tölteni; a GitHub élő lekérését kérd.

## 3. Claude Cowork / Desktop kezdés
> Folytasd a `peterkapusi88-hub/wsg-berendezes` projektet. Mielőtt bármihez nyúlsz, olvasd a friss `GOAL.md`, `CLAUDE.md` és `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` tartalmát. Te vagy a Blender és a műszaki kivitelezés fő gazdája; a ChatGPT független tervezési és költségellenőrzési szempontjait ne írd felül automatikusan. A valódi méret és teljes bruttó keret elsőbbséget élvez. Ne módosítsd a renderben a kiválasztott termékek alapgeometriáját. A munka eredményét verziózott fájlban vagy PR-ben add át.

Ha a Claude GitHub-alkalmazásnak nincs jogosultsága a repóhoz, azt külön engedélyezni kell, vagy a helyi git-klónt használni.

## 4. Codex (repo-local)
Mac ChatGPT alkalmazás → Codex → nyisd meg a helyi `wsg-berendezes` klónt. A gyökérben lévő `AGENTS.md` a belépési útmutató; repo-skill: `.agents/skills/wsg-stiluslabor/SKILL.md`. Indító utasítás: „Végezz kizárólag olvasási és tesztelési geometriai auditot, és írd le a hibákat; Claude élő Blender-jelenetét ne módosítsd.”

## 5. AI-k együttműködése: átadás és audit
1. Claude új Blender-geometriát vagy rendercsomagot készít; frissíti a műszaki naplót, commit/PR.
2. ChatGPT Work önállóan készít/ellenőriz stílust, termékeket, árat, hiányzó tételeket, eltéréseket.
3. Codex szükség esetén geometriai teszteket készít és review-t ad, lehetőleg külön ágon/PR-en.
4. Claude külön forrásból árellenőrzi ChatGPT terméktábláját; eltérést és hiányzó asztalos-ajánlatot rögzít.
5. Gemini jóváhagyott képi briefből videót készít. Péter választ és hagy jóvá.

Nem szükséges, hogy egyik AI a másik weboldalán kattintgasson. A GitHubon történt átadás **nem indít automatikusan** másik AI-feladatot. Ha automatikus értesítés kell, ChatGPT Workben jogosult fióknál GitHub pull request eseményre külön triggeres feladat állítható be. Az automatikus írás, rendelés vagy küldés jogosultságát ne add meg alapértelmezésben.

## 6. Fontos
A jelen konfiguráció használja a meglévő ChatGPT/Claude előfizetéseket az interaktív felületeken. Későbbi teljes API-alapú orkesztráció külön feladat és külön API-költséggel járhat. Ha a modellek saját beszélgetése nem olvasható egymás számára, **a GitHubra mentett munkatermék az átadás**, nem a chat-előzmény.


## Új: Claude mint AI-karmester (2026-10-24)
Elsőként olvasd el az `ai-coordination/ROUTER.md` fájlt. Péternek **Claude-ban kell csak a célt megfogalmaznia**; Claude választja ki, kell-e Astra/Work kreatív, Codex geometriai, Gemini videós feladat. A GitHub PR → Work trigger használatához **egyszeri, kézi webes beállítás** szükséges: `ai-coordination/WORK_TRIGGER_SETUP.md`. Pilot: `ai-coordination/PILOT.md`. A Codex/Gemini autonóm indítása nincs beállítva. Astra Ultra indítása, fizetős extra kreditek, külső beszerzés kizárólag Péter külön engedélyével.
