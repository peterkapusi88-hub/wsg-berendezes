# Munkamenet – három AI + GitHub egy projekten

Egyszerűen: a **repo a közös asztal**, ahol a projekt minden ténye és fájlja van. Minden AI ugyanarról az asztalról dolgozik, és ami kész, azt visszateszi az asztalra. Így nem kell semmit kétszer elmagyarázni, és nem keverednek a számok.

## Ki mit csinál (szereposztás)

| Szereplő | Feladat | Honnan olvas | Hova ír |
|---|---|---|---|
| **Péter** | dönt, „mehet"-et mond, fotóz, fizet | a repo + a chat | GOAL.md (döntések), fotók |
| **Claude** (Cowork/Desktop) | a projekt „műszaki vezetője": alaprajz, méretek, Blender 3D, keretszámítás, tételes lista, e-mailek, asztalos-rajz, a repo karbantartása, a többi AI briefelése | `GOAL.md`, `CLAUDE.md`, az egész repo | minden mappa; commitol a repóba |
| **ChatGPT** (Go/Plus) | kreatív képek (GPT Image), második vélemény a koncepcióra, szöveges variációk | `GOAL.md`, `OPENAI_instructions.md`, a `05_promptok/` és a `04_renderek/` képei (Projectbe feltöltve) | képek → Péter lementi a `04_renderek/ai_chatgpt/` mappába (vagy Claude teszi be) |
| **Gemini** (AI Pro) | fotorealisztikus képek a Blender-nézetből (Nano Banana), keresés, Google-ökoszisztéma (Drive, Gmail) | `GOAL.md`, `GEMINI_instructions.md`, promptok, képek | képek → `04_renderek/ai_gemini/` |
| **GitHub** | az asztal: verziózott, visszakereshető, mindhárom AI eléri | – | – |

## Hogyan megy egy kör (példa: „kérek egy Zenit-stílusú képet a 811 nappalijáról")

1. Péter a Claude-nak mondja, mit akar (egy mondat elég).
2. Claude a repóból kiolvassa a lakás adatait, elkészíti a geometriát (Blender-nézet) és **megírja a részletes promptot** → beteszi a `05_promptok/` mappába.
3. Claude a Chrome-on át **beadja a promptot + a képeket** a Gemininek (és/vagy a ChatGPT-nek), letölti az eredményt, beteszi a `04_renderek/` mappába, commitol.
4. Péter ránéz, mond egy „jó" / „ne így" → Claude frissíti a GOAL.md-t (döntés rögzítve) és megy a következő kör.

Ha Péter közvetlenül a ChatGPT-vel vagy Geminivel beszél: ott a Project/Gem már ismeri a `GOAL.md`-t, tehát ugyanazt tudja; az eredményt Péter lementi a repo megfelelő mappájába (vagy bemásolja a Claude-chatbe, és Claude teszi be).

## A fájlok, amiket minden AI először elolvas

- `GOAL.md` – a projekt memóriája (adatok, keret, elvek, állapot, döntések, következő lépések). **Ez az igazság.**
- `CLAUDE.md` – Claude házirendje (mit csinál, mit kérdez meg, hova ír).
- `OPENAI_instructions.md` – ChatGPT házirendje (Project „Instructions" mezőjébe bemásolható).
- `GEMINI_instructions.md` – Gemini házirendje (Gem „Instructions" mezőjébe bemásolható).
- `07_skill/westside-berendezes_SKILL.md` – ugyanez a tudás Claude-skill formában.

## Beállítás (egyszer)

1. **Claude**: a repo csatlakoztatva (Settings → Connectors → GitHub → a `wsg-berendezes` engedélyezve). Claude olvas-ír.
2. **ChatGPT**: új Project „WSG berendezés" → Instructions: az `OPENAI_instructions.md` tartalma → Files: `GOAL.md`, `06_koncepcio/*.md`, a `04_renderek/` képei. (Plus-tól a GitHub-connector is ráköthető olvasásra, akkor nem kell kézzel feltölteni.)
3. **Gemini**: új Gem „WSG berendezés" → Instructions: `GEMINI_instructions.md` → Knowledge: `GOAL.md`, koncepció-doksi. Képgenerálás: a Blender-nézet + referencia + termékfotó feltöltése a promptokkal.
4. **Frissítés**: ha a GOAL.md változik, a ChatGPT Projectben és a Gemben is cseréld (vagy Claude teszi, Chrome-on át).

## Szabályok, hogy ne legyen káosz

- Egy igazság: a GOAL.md. Ha egy AI mást mond, a GOAL.md nyer, és Claude javítja.
- Minden kép fájlneve: `A<lakás>_<stílus>_<sorszám>_<helyiség>.jpg` (pl. `A902_Zenit_1_nappali.jpg`).
- Promptot mindig a repóba is beírjuk, hogy a kép reprodukálható legyen.
- Személyes adat (leadek, szerződések, e-mailek) nem kerül a repóba.
- Küldés, rendelés, fizetés csak Péter „mehet"-je után – ezt minden AI házirendje tartalmazza.
