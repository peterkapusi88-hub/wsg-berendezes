# wsg-berendezes

Westside Grand A-811 / A-812 / A-902 berendezési projekt – a közös „igazság-mappa" Claude, ChatGPT és Gemini számára.

**Kezdd a `GOAL.md`-vel** – ez a projekt memóriája (lakásadatok, keret, elvek, állapot, nyitott döntések, következő lépések).

## Hogyan használd

- **Claude** (Cowork/Desktop): a repo csatlakoztatva; a `07_skill/westside-berendezes_SKILL.md` ugyanez a tudás skill-formában, feltöltve a Claude-fiókba.
- **ChatGPT**: hozz létre egy Projectet „WSG berendezés" néven, töltsd fel a `GOAL.md`-t és a `06_koncepcio/*.md`-t, a képeket a `04_renderek/` mappából. Képgeneráláshoz a `05_promptok/gemini_prompts.md` promptjai ugyanúgy működnek (bemenet: Blender-nézet + referencia + termékfotó).
- **Gemini**: ugyanez; a Nano Banana képszerkesztő a Blender-nézetet tartja geometriának.

## Mappák

| Mappa | Tartalom |
|---|---|
| `01_alaprajzok/` | Westside Grand brosúra (PDF) + lakásonkénti alaprajz-képek |
| `02_referenciak/` | Zenit Residence és Lake Forest látványtervek kontaktlapjai (a stílus-DNS forrása) |
| `03_blender/` | `WSG_A902_base.blend` (alap), `WSG_A902_stilusok.blend` (Zenit-réteg beépítve), `stil_lakeforest_layer.py` (Lake Forest-réteg, a Blender MCP-n át futtatva) |
| `04_renderek/alap/` | Blender-renderek (EEVEE): alaprajz felülnézet, nappali, étkező-konyha, master, terasz |
| `04_renderek/ai_gemini/` | 6 fotorealisztikus AI-kép az A-902-ről (3 Zenit, 3 Lake Forest) + összehasonlító lap |
| `05_promptok/` | Képgeneráló promptok mindkét stílushoz, helyiségenként |
| `06_koncepcio/` | A koncepció-doksi: két referencia DNS-e, fordítótábla, asztalos vs IKEA, verziók lakásonként, keretszámítás |
| `07_skill/` | A `westside-berendezes` Claude-skill forrása |

## Szabály
Ami ide kerül, az a hivatalos állapot. Ha egy AI más számmal dolgozik, a `GOAL.md` és a `06_koncepcio/` az irányadó. Személyes adat (leadek, szerződések, e-mailek) nem kerül ide.
