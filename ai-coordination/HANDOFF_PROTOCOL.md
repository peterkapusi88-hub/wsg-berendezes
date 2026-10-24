# WSG – tartós GitHub-átadás („postafiók”), v2 · 2026-10-24

**Cél:** Péternek ne kelljen fájlt másolnia ChatGPT és Claude között. A GitHub-repó a postafiók. Minden AI innen olvas és ide ír. A chat csak egy rövid indító mondat.

**Mi igazolt (2026-10-24):**
- A ChatGPT GitHub-kapcsolata **tud fájlt létrehozni a `main` ágon** (commit `f307765`, szerző `peterkapusi88-hub`, `ai-coordination/results/WSG-20261024-PILOT-001.md`).
- Claude felhőből `add_repo` + klónnal olvas és pushol. Ugyanez megy a Mac-tükörből is: `~/Downloads/wsg-berendezes`.

**Mi nem igazolt:**
- a Work automatikus indítása PR-eseményre (`WORK_TRIGGER_SETUP.md`);
- a ChatGPT ütemezett feladata;
- a Codex és a Gemini repó-írása.

Ezek opcionálisak. A protokoll nélkülük is működik.

---

## 1. Az állapot a fájlokból olvasható, nincs közös státuszfájl

Egy feladat = egy azonosító (`WSG-ÉÉÉÉHHNN-<rövid>-NNN`). Az állapotot az dönti el, **mely fájlok léteznek**. Így két AI soha nem szerkeszti ugyanazt a fájlt, és nincs ütközés.

| Fájl | Ki írja | Jelentés |
|---|---|---|
| `ai-coordination/requests/<ID>.md` | **csak Claude** | brief; a fejlécben `Indítás:` és `Cél AI:` mező |
| `ai-coordination/results/<ID>.md` | **csak a cél-AI** (vagy Péter kérésére a ChatGPT GitHub-kapcsolata) | eredmény, **változatlanul**; létezése = „eredmény kész” |
| `ai-coordination/results/<ID>_r2.md`, `_r3` … | cél-AI | javított vagy folytatott eredmény; a korábbit **senki nem írja felül** |
| `ai-coordination/audits/<ID>_CLAUDE_AUDIT.md` | **csak Claude** | független audit; létezése = „Claude validálta” |
| `GOAL.md` 7. pont | Claude, Péter döntése után | döntés |

**Állapotok:**
- **NYITOTT:** van request, `Indítás: PÉTER INDÍTJA`, és nincs result.
- **AUDITRA VÁR:** van result, nincs audit.
- **KÉSZ:** van audit.
- **DÖNTÉSRE VÁR:** az audit 9. pontjában van nyitott kérdés.

## 2. Péter két mondata (ennyi a kézi munka)

**ChatGPT-ben** (WSG projekt, Work):
> **WSG: dolgozd fel a `<ID>` feladatot a GitHubról, és mentsd az eredményt a repóba.**

Ez a mondat Péter „mehet”-je erre az egy feladatra. Astra innen mindent maga csinál (3. pont).

**Claude-ban:**
> **WSG: `<ID>` kész.**

Vagy semmi, ha a Claude-oldali ütemezett ellenőrzés be van kapcsolva (6. pont). Claude ilyenkor maga húzza le a repót, auditál, és visszaír.

## 3. Astra/Work kötelező lépései (az `OPENAI_instructions.md`-ben is)
1. Olvasd a **legfrissebb** `main`-t: `GOAL.md`, `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`, `ai-coordination/RENDER_REALITY_GATE.md`, a brief, és a briefben felsorolt inputok. Jegyezd fel a commit-azonosítót, amiből dolgozol.
2. Csak a briefben kért munkát végezd.
3. Az eredményt **egyetlen új fájlba** írd: `ai-coordination/results/<ID>.md`.
   - Ha túl hosszú: `<ID>_A.md`, `<ID>_B.md`.
   - Commit-üzenet: `WSG-RESULT <ID>: <egy sor>`, közvetlenül a `main`-re.
4. Az eredmény **első sorai** kötelezően:
   ```
   WSG-RESULT: <ID>
   Szerző-AI: ChatGPT Work/Astra (vagy amit a felület ténylegesen mutat)
   Modell: <ha igazolt> | nem igazolt
   Bázis-commit: <sha>
   Státusz: TELJES | RÉSZLEGES | BLOKKOLT
   ```
5. **Írhatsz:** `ai-coordination/results/`. Képek: `04_renderek/ai_chatgpt/<ID>_*` (csak ha a brief képet kér).
   **Nem írhatsz és nem módosíthatsz:** `GOAL.md`, `requests/`, `audits/`, `03_blender/`, `07_skill/`, létező eredményfájl, PR-ek.
6. Ha nem tudsz a repóba írni, válaszold a chatben: `WSG-RESULT BLOKKOLT: <ID> – <ok>`. Ilyenkor a tartalék: Claude Chrome-relay (`CLAUDE_HANDOFF_PROCEDURE.md` 3/C), vagy Péter egy mondattal szól Claude-nak.
7. A chatben csak ennyit válaszolj: a commit-azonosító és 3–5 soros összefoglaló.

## 4. Claude kötelező lépései
1. **Munkamenet-indítás:** felhőben `add_repo` → friss klón. Macen a `~/Downloads/wsg-berendezes`, `git fetch` + `git status`. Nem commitolt helyi munkát nem írok felül, ilyenkor külön ágra dolgozom.
2. Brief: `requests/<ID>.md` a `REQUEST_TEMPLATE.md` szerint, `Indítás: NEM INDÍTOTT` vagy `Indítás: PÉTER INDÍTJA`. Az inputképek előbb kerülnek a repóba.
3. Átvétel: AUDITRA VÁR állapotú eredmények keresése. Az eredmény sha256-ját rögzítem az auditban. **Az eredményfájlt nem szerkesztem.**
4. Audit: `audits/<ID>_CLAUDE_AUDIT.md`. Benne: független árellenőrzés, geometria/Validator, Gate-státusz, tanulságok, Péter kérdései.
5. Ha a brief vagy a szabály hibás volt: javítás a következő briefben vagy a szabályfájlban, külön commitban.

## 5. Biztonsági szabályok (változatlanok)
- Rendelés, ajánlatkérés, külső levél, publikálás, fizetés: csak Péter „mehet”-je után.
- Személyes adat, szerződés, átvételi dokumentum nem kerül a repóba.
- Az élő Blender-fájlt csak Claude kezeli. Más AI a .blend-et csak olvassa.
- Egy azonosító = egy futás. Ismétlés csak `_r2` néven, Péter kérésére.
- Ultra/Max és extra kredit csak Péter külön engedélyével.

## 6. Opcionális automatizálás (bekapcsolás Péter jóváhagyásával)
- **Claude-oldali ütemezett ellenőrzés (javasolt):** a Claude felhős ütemezett feladata naponta 2× (pl. 8:40 és 18:40 budapesti idő):
  - friss klón;
  - AUDITRA VÁR eredmények keresése;
  - audit megírása és pusholása;
  - push-értesítés Péternek.

  Nem rendel, nem indít más AI-t, a Blendert nem érinti. Ha nincs új eredmény, nem csinál semmit.
- **ChatGPT-oldali ütemezett feladat:** a ChatGPT-ben Péter beállíthatja, hogy naponta nézze a NYITOTT, `Indítás: AUTOMATIKUS ENGEDÉLYEZVE` jelölésű briefeket. **Nem tesztelt.** Kreditet fogyaszt, és csak ilyen jelölésű briefre futhat.
- **PR-eseményes Work-trigger** (`WORK_TRIGGER_SETUP.md`): marad tartalék. A PR #1 inaktív, nem módosítjuk.

## 7. Codex és Gemini ugyanebben a postafiókban
- **Codex:** brief `Cél AI: CODEX`; eredmény `results/<ID>.md` a Codex saját commitjával a helyi klónból. **Nem igazolt.** Első próbája külön feladat.
- **Gemini/Flow:** nem ír GitHubra. A videó letöltése után Péter vagy Claude (Chrome) teszi a `04_renderek/ai_video_tests/<ID>_*` alá, és Claude írja a result-fájlt `Szerző-AI: Gemini (Claude/Péter relay)` jelöléssel.

## 8. Igazolási napló
| Dátum | Lépés | Eredmény |
|---|---|---|
| 2026-10-24 | ChatGPT GitHub-kapcsolat ír a `main`-re | **igen** (`f307765`) |
| 2026-10-24 | Claude felhőből átveszi és auditálja | **igen** (`audits/WSG-20261024-PILOT-001_CLAUDE_AUDIT.md`) |
| – | Astra a 2. pont mondatára maga írja a result-fájlt (Péter másolása nélkül) | **következő feladatnál igazolandó** |
| – | Claude ütemezett ellenőrzés | nincs bekapcsolva |
