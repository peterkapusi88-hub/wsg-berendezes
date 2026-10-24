# Munkamenet – három AI + GitHub egy projekten

## Ha 8 éves lennél: így működik

Képzeld el, hogy a lakásberendezés egy nagy legóépítés, és három barátod segít. Mind a hárman ugyanabból a **dobozból** dolgoznak – ez a doboz a GitHub-repo. A dobozban van egy **füzet** (`GOAL.md`), amibe le van írva minden, amit tudni kell: mekkorák a szobák, mennyi pénz van, mit szeret Péter, mit döntöttünk eddig. Aki segíteni akar, először elolvassa a füzetet, ezért nem kell neki semmit újra elmagyarázni, és nem is kever össze semmit.

- **Claude** a *csapatkapitány és mérnök*: ő méri le a szobákat, ő építi a 3D-makettet (Blender), ő számolja a pénzt, ő ír a mestereknek, és ő írja be a füzetbe, ha valami eldőlt.
- **ChatGPT** két ruhában jár: **Work**-ruhában ő a *lakberendező* (nézi a referenciaképeket, kitalálja a bútort és a színeket, rajzol szép képeket, ellenőrzi, hogy a kész kép hasonlít-e a mintára); **Codex**-ruhában ő a *Blender-szerelő* (megírja vagy megjavítja a programocskákat, amik a makettet építik).
- **Gemini** a *fotós*: a makett képéből és a mintaképből csinál olyan fotót, mintha a lakás már kész lenne.

Egy kör így megy: Péter mond egy kívánságot → Claude kikeresi a füzetből az adatokat és elkészíti a makett-képet → a lakberendező vagy a fotós kiszínezi → Péter ránéz és azt mondja „jó" vagy „ne így" → Claude beírja a füzetbe, és a kész képet beteszi a dobozba. Senki nem rendel és nem fizet semmit, amíg Péter nem mondja: **„mehet"**.

## Ki mit csinál (szereposztás)

| Szereplő | Feladat | Honnan olvas | Hova ír |
|---|---|---|---|
| **Péter** | dönt, „mehet"-et mond, fotóz, fizet | a repo + a chat | GOAL.md (döntések), fotók |
| **Claude** (Cowork/Desktop) | a projekt „műszaki vezetője": alaprajz, méretek, Blender 3D az MCP-n át, keretszámítás, tételes lista, e-mailek, asztalos-rajz, a repo karbantartása, a többi AI briefelése | `GOAL.md`, `CLAUDE.md`, az egész repo | minden mappa; commitol a repóba |
| **ChatGPT Work** (Plus-tól, GPT-5.6 Sol / GPT-6 Astra) | lakberendező + projektvezető: alaprajz-elemzés, bútor/anyag/világítás a referenciák alapján, fotoreál képek előkészítése és generálása, renderek összevetése a referenciákkal, eltéréslista | `GOAL.md`, `OPENAI_instructions.md`, `02_referenciak/`, `04_renderek/`, `05_promptok/` (Projectbe töltve vagy GitHub-connectoron át) | képek → `04_renderek/ai_chatgpt/`; eltéréslisták → `06_koncepcio/` |
| **ChatGPT Codex** (ugyanaz a keret) | Blender-technikus: a `03_blender/*.py` szkriptek írása/javítása, jelenet-építés kódból, renderhibák, automatizálás | `AGENTS.md`, `GOAL.md`, `03_blender/` | `03_blender/` (futtatás Claude-on vagy kézzel Blenderben) |
| **Gemini** (AI Pro, peter.kapusi88 fiók) | fotorealisztikus képek a Blender-nézetből (Nano Banana), keresés, Google-ökoszisztéma | `GOAL.md`, `GEMINI_instructions.md`, promptok, képek | képek → `04_renderek/ai_gemini/` |
| **GitHub** | az asztal/doboz: verziózott, visszakereshető, mindhárom AI eléri | – | – |

Keretkímélés ChatGPT-ben: rutin tervezés és egyszerű szkript → Sol; bonyolult geometria, összeomló szkript, többlépéses automatizálás → Astra; erős gondolkodás csak ha a közepes nem boldogul. Work és Codex ugyanazt a keretet fogyasztja.

## Hogyan megy egy kör (példa: „kérek egy Zenit-stílusú képet a 811 nappalijáról")

1. Péter a Claude-nak mondja, mit akar (egy mondat elég).
2. Claude a repóból kiolvassa a lakás adatait, elkészíti a geometriát (Blender-nézet) és **megírja a részletes promptot** → `05_promptok/`.
3. Ha a jelenethez új szkript kell, azt Codex is megírhatja a `03_blender/` mappába; Claude futtatja az MCP-n át.
4. Claude a Chrome-on át **beadja a promptot + a képeket** a Gemininek és/vagy a ChatGPT Worknek, letölti az eredményt → `04_renderek/`, commit.
5. Work összeveti a képet a referenciával (eltéréslista) → Péter ránéz, „jó" / „ne így" → Claude frissíti a GOAL.md-t (döntés rögzítve), és megy a következő kör.

Ha Péter közvetlenül a ChatGPT-vel vagy Geminivel beszél: ott a Project/Gem már ismeri a `GOAL.md`-t, tehát ugyanazt tudja; az eredményt Péter lementi a repo megfelelő mappájába (vagy bemásolja a Claude-chatbe, és Claude teszi be).

## A fájlok, amiket minden AI először elolvas

- `GOAL.md` – a projekt memóriája (adatok, keret, elvek, állapot, döntések, következő lépések). **Ez az igazság.**
- `CLAUDE.md` – Claude házirendje.
- `OPENAI_instructions.md` – ChatGPT Work házirendje (Project „Instructions" mezőjébe) + a Work/Codex szereposztás.
- `AGENTS.md` – ChatGPT Codex házirendje (a Codex ezt a fájlnevet keresi).
- `GEMINI_instructions.md` – Gemini házirendje (Gem „Instructions" mezőjébe).
- `07_skill/` – ugyanez a tudás Claude-skill formában (`westside-berendezes`, `wsg-chatgpt-work-codex`).

## Beállítás (egyszer)

1. **Claude**: GitHub → Settings → Applications → Installed GitHub Apps → *Claude* → Configure → Repository access → `wsg-berendezes` hozzáadása (sudo e-mail-megerősítés kell, ezt Péter csinálja). Utána Claude közvetlenül pushol.
2. **ChatGPT Work**: Settings → Connectors → GitHub → a `wsg-berendezes` engedélyezése (Plus-tól), vagy új Project „WSG berendezés" → Instructions: `OPENAI_instructions.md` vonal alatti része → Files: `GOAL.md`, `06_koncepcio/*.md`, a `04_renderek/` és `02_referenciak/` képei.
3. **ChatGPT Codex**: a Mac-alkalmazásban a repo helyi klónja (`~/Projects/wsg-berendezes`) a projektmappa; a Codex az `AGENTS.md`-t olvassa.
4. **ChatGPT Mac-app Blenderhez**: a böngészős Work nem látja a Blendert; ha Blender-műveletet kérsz tőle, a Mac-appot használd – de egyszerre csak egy vezérlő (Claude MCP vagy ChatGPT) dolgozzon a jeleneten.
5. **Gemini**: új Gem „WSG berendezés" → Instructions: `GEMINI_instructions.md` → Knowledge: `GOAL.md`, koncepció-doksi. Képgenerálás: Blender-nézet + referencia + termékfotó a promptokkal.
6. **Frissítés**: ha a GOAL.md változik, a ChatGPT Projectben és a Gemben is cseréld (vagy Claude teszi, Chrome-on át); GitHub-connectorral ez automatikus.

## Szabályok, hogy ne legyen káosz

- Egy igazság: a GOAL.md. Ha egy AI mást mond, a GOAL.md nyer, és Claude javítja.
- Minden kép fájlneve: `A<lakás>_<stílus>_<sorszám>_<helyiség>.jpg` (AI-kép) vagy `A<lakás>_<stílus>_blender_<sorszám>_<helyiség>.png` (Blender-nézet).
- Promptot mindig a repóba is beírjuk, hogy a kép reprodukálható legyen.
- Egy jeleneten egyszerre egy vezérlő (Claude MCP **vagy** ChatGPT Mac-app/Codex).
- Személyes adat (leadek, szerződések, e-mailek) nem kerül a repóba.
- Küldés, rendelés, fizetés csak Péter „mehet"-je után – ezt minden AI házirendje tartalmazza.


## Kiemelt munkarend – stíluslabor

Olvasd el a `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` fájlt. A Zenit és Lake Forest csak két példa, akár tíz vagy több stílus összevetése lehetséges. A közös mérce: azonos geometria, azonos lakásonkénti bruttó keret, 10% tartalék, jó használhatóság. Luxusérzetet forma, szín, térhasználat, fény, anyag és természetkapcsolat együtt teremtenek. A koncepciók költségelőszűrést kapnak, a döntősök részletes termék- és asztaloslistát, a ChatGPT és Claude független árvizsgálatát. A render státusza koncepció, keretre előszűrt, tételesen költségelt vagy ajánlattal validált; a valódi termék és a képen megjelenő elem eltérését jelezni kell. Geminivel készülhet videó is, változatlan geometriával.
