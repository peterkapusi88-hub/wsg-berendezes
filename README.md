# wsg-berendezes

Westside Grand A-811 / A-812 / A-902 berendezési projekt – a közös „igazság-mappa" Claude, ChatGPT és Gemini számára.

**Kezdd a `GOAL.md`-vel** – ez a projekt memóriája (lakásadatok, keret, elvek, állapot, nyitott döntések, következő lépések).

## Hogyan használd

- **Claude** (Cowork/Desktop): a repo csatlakoztatva; a `07_skill/` skilljei ugyanez a tudás skill-formában, feltöltve a Claude-fiókba. Házirend: `CLAUDE.md`.
- **ChatGPT Work** (lakberendező/projektvezető) és **Codex** (Blender-technikus): házirend `OPENAI_instructions.md` és `AGENTS.md`. Work: GitHub-connector vagy Project „WSG berendezés" a `GOAL.md` + `06_koncepcio/*.md` + képek feltöltésével. Képgeneráláshoz a `05_promptok/gemini_prompts.md` promptjai ugyanúgy működnek (bemenet: Blender-nézet + referencia + termékfotó).
- **Gemini**: ugyanez (`GEMINI_instructions.md`); a Nano Banana képszerkesztő a Blender-nézetet tartja geometriának.
- A teljes szereposztás és egy kör menete, „8 évesnek elmagyarázva" is: `MUNKAMENET.md`.

## Mappák

| Mappa | Tartalom |
|---|---|
| `01_alaprajzok/` | Westside Grand brosúra (PDF) + lakásonkénti alaprajz-képek |
| `02_referenciak/` | Zenit Residence és Lake Forest látványtervek kontaktlapjai (a stílus-DNS forrása) |
| `03_blender/` | `WSG_A902_base.blend` (alap), `WSG_A902_stilusok.blend` (Zenit- és Lake Forest-réteg beépítve), `wsg_helpers.py` (box/cyl/sphere/tube/disc/mat/coll/set_style), `stil_lakeforest_layer.py` (a Lake Forest-réteg forrása) |
| `04_renderek/alap/` | Blender-renderek (EEVEE): alaprajz felülnézet, nappali, étkező-konyha, master, terasz |
| `04_renderek/blender_stilusok/` | 3+3 EEVEE-nézet a két stílusréteggel (geometria-alap az AI-képekhez) + kontaktlap |
| `04_renderek/ai_gemini/` | 6 fotorealisztikus AI-kép (Gemini) az A-902-ről (3 Zenit, 3 Lake Forest) + összehasonlító lap |
| `04_renderek/ai_chatgpt/` | ugyanaz a 6 kép ChatGPT-vel + Gemini-vs-ChatGPT lap |
| `05_promptok/` | Képgeneráló promptok mindkét stílushoz, helyiségenként |
| `06_koncepcio/` | A koncepció-doksi: két referencia DNS-e, fordítótábla, asztalos vs IKEA, verziók lakásonként, keretszámítás |
| `07_skill/` | A `westside-berendezes` Claude-skill forrása |

## Szabály
Ami ide kerül, az a hivatalos állapot. Ha egy AI más számmal dolgozik, a `GOAL.md` és a `06_koncepcio/` az irányadó. Személyes adat (leadek, szerződések, e-mailek) nem kerül ide.
