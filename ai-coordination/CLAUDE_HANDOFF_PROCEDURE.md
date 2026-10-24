# Claude átadási eljárás – hogyan indítok és hogyan veszem vissza (v1, 2026-10-24)

Ez a `ROUTER.md` Claude-oldali végrehajtása. Csak igazolt képességek szerepelnek benne; ami nincs tesztelve, az annak van jelölve.

## 0. Igazolt hozzáférések (2026-10-24 04:05)
- **Claude GitHub-app telepítve** a `peterkapusi88-hub` fiókra, a `wsg-berendezes` repóval. Igazolás: `git clone` sikeres (HEAD `f10778b`), `gh api repos/peterkapusi88-hub/wsg-berendezes/pulls/1` olvasható, ágak listázhatók, `gh pr diff 1` működik.
- **Claude Project „WSG – Luxus lakberendezés és stíluslabor"**: a repo szöveges része (GOAL, AI_START_HERE, CLAUDE, MUNKAMENET, OPENAI/GEMINI/AGENTS, 03_blender szkriptek, 05–07 mappák, ai-coordination) GitHub-forrásként bekötve. **Ez pillanatkép**: a projekt tudásbázisát frissíteni kell változás után (Context → sync), de a munkamenetben mindig a friss klón/raw olvasás az irányadó.
- Képek, renderek, `.blend`: nem a projekt-tudásbázisból, hanem a klónból (`/home/claude/wsg-berendezes`) vagy a Macről (`~/Downloads/wsg-berendezes`, élő Blender: `~/Downloads/WSG_A902_stilusok.blend`).

## 1. Munkamenet eleje (minden alkalommal)
1. `git -C /home/claude/wsg-berendezes fetch origin && git status` → ha a klón elmaradt: `git pull --ff-only`. Ha a helyi munka nem tiszta: **nem írok felül**, külön ágra commitolok.
2. `GOAL.md` → `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` → `CLAUDE.md` → `ai-coordination/ROUTER.md` olvasása.
3. Nyitott PR-ek és friss commitok: `gh api repos/peterkapusi88-hub/wsg-berendezes/pulls`, `gh api .../commits?per_page=10`.
4. Blender állapot: `is_dirty`/mentés ellenőrzése az MCP-n át, mielőtt bármit módosítok.

## 2. Átadás Astrának (egy PR = egy brief)
1. Brief a `REQUEST_TEMPLATE.md` szerint → `ai-coordination/requests/<ID>.md`; a hivatkozott képek **előbb** a repóba (`04_renderek/...`).
2. Ág: `handoff/astra-<lakás>-<helyiség>-<nn>`; commit magyarul, egy sor; push.
3. Draft PR: `gh pr create --draft --title "[ASTRA-REVIEW] <ID> – <rövid cím>" --body-file ai-coordination/requests/<ID>.md`.
4. **Élesítés csak Péter kifejezett jóváhagyásával** és csak ha a webes Work-trigger igazoltan létezik: `gh api -X POST repos/peterkapusi88-hub/wsg-berendezes/pulls/<n>/ccr/ready_for_review`. Egyetlen alkalommal. (A Codex-munkamenetben a GraphQL nem elérhető, ezért ez a REST/CCR út.)
5. Státusz a PR-ben és a `PILOT.md`-ben: `tervezet` → `átadásra kész` → `Work indítva` (csak ha Péter vagy a Work-feladat naplója igazolja).

## 3. Visszavétel – három út, erősorrendben
- **A) GitHub PR-komment** (`WSG-ASTRA-RESULT: <ID>` fejléccel): `gh api repos/peterkapusi88-hub/wsg-berendezes/issues/<n>/comments --jq '.[] | select(.body|startswith("WSG-ASTRA-RESULT"))'`. Mechanizmus igazolt (a lekérdezés működik, PR #1-en jelenleg 0 komment). **Hogy a Work tud-e GitHubra írni, nem igazolt** – a ChatGPT GitHub-csatlakozó alapból olvasó.
- **B) Eredményfájl külön ágon**: `git fetch origin` → `ai-coordination/results/<ID>.md` olvasása az ágról. Mechanizmus igazolt; Work-oldali írás nem igazolt.
- **C) Chrome-relay (az, ami biztosan megy):** ha a Work eredménye csak a ChatGPT-feladatban jelenik meg, Claude a saját Chrome-fülén megnyitja a Work-feladat eredményét, kimásolja a `WSG-ASTRA-RESULT` blokkot, és **ő commitolja** `ai-coordination/results/<ID>.md`-be a `RESULT_TEMPLATE.md` szerint, megjelölve: `visszaadás: Chrome-relay, nem automatikus`. Ehhez Péter ChatGPT-je be legyen jelentkezve a Chrome-ban; Péter saját füleit nem használom.
- Utolsó tartalék: Péter bemásolja az eredményt a Claude-chatbe → Claude commitolja.
A visszavétel akkor „működő", ha a `results/<ID>.md` ténylegesen a repóban van és Claude abból dolgozott tovább.

## 4. Claude utómunka minden eredmény után
Független árellenőrzés külön forrásból (vizsgálati tábla: tétel · Astra ár/link/dátum · Claude ár/forrás · delta · állapot) → Blender-illesztés és Validator → `GOAL.md` 6–7. pont frissítése → Péter döntésére váró kérdések listája. Rendelés, ajánlatkérés, külső levél nincs.

## 5. Amit nem csinálok automatikusan
Nem váltok Ultra/Max-ra, nem indítok Codex- vagy Gemini-futtatást PR-ből (nincs híd), nem élesítek PR-t jóváhagyás nélkül, nem állítom, hogy Astra futott, amíg nincs igazolt output.
