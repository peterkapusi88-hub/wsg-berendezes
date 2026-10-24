# ChatGPT Work GitHub automatikus Astra-átadás – egyszeri beállítás

**Fontos:** a beállítás **nem történik meg pusztán e fájl feltöltésétől**. A Plus fiók jogosultsága támogatja az eseményvezérelt Work-feladatot, de a feladatot a felhasználónak létre kell hoznia a **ChatGPT weboldal Work felületén**. A Mac desktop alkalmazás nem tudja létrehozni/szerkeszteni az eseményfeltételeket. Az elérhető trigger-/condition-/model választók a tényleges fiók UI-jától függenek.

## Egyszeri lépések Péternek
1. A böngészőben nyisd meg a ChatGPT-t → **Settings / Plugins (Apps)** → GitHub-kapcsolat, győződj meg arról, hogy a **privát** `peterkapusi88-hub/wsg-berendezes` repo engedélyezett. A korábbi ChatGPT-beszélgetésből olvasási jogosultság igazolt.
2. Nyisd meg a `WSG – Stíluslabor` projektet → **Work** mód (NEM Codex).
3. Kérd **eseményvezérelt Work-feladat létrehozását** a repo `pull request marked ready for review` eseményére. Szűrés/feltétel: a PR címe tartalmazza **`[ASTRA-REVIEW]`**. Ha az adott UI nem tud címszűrést, ne aktiválj minden PR-re futó feladatot: jelezd, és állítsuk át a pilotot másik támogatott feltételre.
4. A feladat utasítása az alábbi rész, modelleffektus: **GPT-6 Astra**, alapból **Medium/közepes**, ha van modellválasztó. Ha a Work-trigger nem engedi modell rögzítését, **ne állítsuk be, hogy garantáltan Astra fut**. Ultra/Max választása minden esetben kézi jóváhagyást igényel.
5. Ellenőrizd **Trigger / Condition / Prompt**, jogosultságokat és felhasználási keretet, csak utána hozz létre feladatot.
6. Az első tesztet csak akkor indítsuk, amikor van rendelkezésre álló Work/Codex-keret. Pilot egyetlen kis kreatív brief, **egy PR → egy feladat**. Ne állítsunk be commitra, kommentre és nyitásra is több párhuzamos triggert.

## A Work-trigger utasítása (másolható)

> A `peterkapusi88-hub/wsg-berendezes` privát repository egyik `[ASTRA-REVIEW]` című pull requestje „ready for review” állapotba került. Ez egy Claude által előkészített, jóváhagyott kreatív vagy független költségellenőrzési átadás. Azonosítsd az éppen kiváltó PR-t; ne dolgozz régi vagy másik PR-n. Először olvasd el a repo `GOAL.md`, `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`, `OPENAI_instructions.md` fájljait, valamint a PR-ben hivatkozott `ai-coordination/requests/<ID>.md` briefet. Csak a briefben megadott helyiséget, stílust és kért eredményeket dolgozd fel. A te szereped a **kreatív tervezés, drágának ható luxusstílusok, belsőépítészeti forma/szín/tér/fény, renderpromptok, konkrét magyarországi termék- és anyagkutatás, független költségellenőrzés**. A Blender fő jelenetét és szkriptjeit ne módosítsd. Nem válthatsz kétes méretre vagy olcsó anyagra úgy, hogy a kép hamisan drágábbat mutasson. Minden árnál termékazonosító, dátum, link, szállítási/szerelési feltétel és bizonytalanság szükséges. Különítsd el az illusztratív koncepciót, az előzetes becslést és az ajánlattal validált megoldást. A válasz első sora legyen **`WSG-ASTRA-RESULT: <ID>`**; tartalmazzon rövid kreatív koncepciót, WOW-gesztusokat, tényleges termék/anyag opciókat, költségkockázatot, geometriára vonatkozó kérdéseket, a Claude-nak átadandó teendőket. Ha a GitHubhoz van hozzászólási jogosultságod, ezt a visszajelzést a PR **Conversation** részére írd kommentként; más esetben a feladat eredményében add vissza, és mondd ki, hogy nem sikerült a GitHub-visszaadás. Ne indíts másik PR-t, új AI-feladatot, rendelést vagy külső megkeresést; ne ismételd automatikusan a futást. Ha a kért modell nem elérhető vagy a kreditek elfogytak, ezt jelezd, ne használj titokban másik modellt.

## Korlátok
- A GitHub PR-aktivitás indíthat Worköt, **de egy PR nem tudja közvetlenül előírni a Work modelljét**.
- Ezt az útvonalat használjuk **Astra/Work** feladatátadásra. Codex kód-review külön engedélyezhető, Gemini video pedig külön integráció.
- Claude nem látja garantáltan a ChatGPT Plus felhasználási limitjét; szükség esetén Péter egyszer kézzel jelzi, hogy a pilot indítható.
- Visszaadás és automatikus újrafelvétel akkor tekinthető megoldottnak, ha a PR-komment vagy fájl ténylegesen látható és Claude azt elolvasta.

OpenAI hivatalos leírások:
- https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt
- https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
- https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
