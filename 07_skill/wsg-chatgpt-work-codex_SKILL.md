---
name: wsg-chatgpt-work-codex
description: Hogyan használjuk a ChatGPT-t (Work = lakberendező/projektvezető, Codex = Blender-technikus, GPT-6 Astra / GPT-5.6 Sol) a Westside Grand berendezési projektben Claude és Gemini mellett. Használd, ha a WSG-projektben ChatGPT-t, Workot, Codexet, Astrát, Solt briefelünk, promptot írunk neki, feladatot osztunk, vagy a keretét kíméljük.
---

> **ELAVULT (2026-10-24):** a szereposztást a `wsg-ai-munkamenet_SKILL.md` váltotta fel (Work = kreatív + független költségellenőr, Codex = geometriai auditor, Claude = Blender + független költségellenőr, Gemini = kép/videó). Ez a fájl csak előzményként marad.

# ChatGPT a WSG-projektben: Work tervez, Codex szerel, Claude vezet

## 1. Mi micsoda
- **Work** és **Codex** ugyanaz az intelligencia (GPT-6 Astra, illetve GPT-5.6 Sol), két felületen, más munkára optimalizálva. **Ugyanazt az előfizetéses keretet fogyasztják.**
- **Work** = lakberendező és projektvezető: alaprajz-elemzés, bútor/anyag/világítás a referenciák alapján, fotoreál képek előkészítése és generálása, renderek összevetése a referenciákkal, több fájl/alkalmazás koordinálása.
- **Codex** = Blender-technikus: Python-szkriptek írása/javítása a `03_blender/` mappában, jelenet programozott felépítése, renderhibák, automatizálás. Helyi projektmappával és terminállal dolgozik; az `AGENTS.md`-t olvassa.
- **Claude** marad a műszaki vezető: a Blender MCP-kapcsolat (localhost:9876) futtatója, a GOAL.md gazdája, a többi AI briefelője. A Codex szkriptjét Claude futtatja (vagy Péter kézzel a Blender Text Editorban).
- **Gemini** a fotós (Nano Banana a Blender-nézetből) – lásd `GEMINI_instructions.md`.

## 2. Feladat → felület
| Feladat | Work | Codex |
|---|---|---|
| Alaprajz elemzése, helyiségek berendezése | ✔ | |
| Referenciaképek alapján stílus és anyagok | ✔ | |
| Fotorealisztikus látványtervek előkészítése, generálása | ✔ | |
| Bútor, burkolat, világítás megtervezése | ✔ | |
| Renderek összevetése a referenciával, eltéréslista, következő javítások | ✔ | |
| Projektkoordináció több fájl és alkalmazás között | ✔ | |
| Blender-fájlok, objektumok módosítása Python-szkripttel | | ✔ |
| Komplett Blender-jelenet programozott felépítése | | ✔ |
| Renderelési hibák keresése, automatizálás | | ✔ |

## 3. A három lépés egy körben
1. **Work tervez** – bemenet: `GOAL.md` + alaprajz (`01_alaprajzok/`) + referenciák (`02_referenciak/`). Kimenet: bútorozás, anyagok, világítás, helyiségenként megvalósítási terv; vagy fotoreál kép a prompt + Blender-nézet + referencia alapján.
2. **Codex szerel** – ha a jelenethez új/módosított geometria, anyag, kamera, fény kell: szkript a `03_blender/` mappába a `wsg_helpers.py` függvényeivel (box, cyl, sphere, tube, disc, mat, coll, set_style). Futtatás: Claude MCP-n át → render `04_renderek/blender_stilusok/`.
3. **Work ellenőriz** – a render/AI-kép összevetése a referenciával: eltéréslista fontossági sorrendben, javítási javaslatok. Péter dönt → Claude frissíti a GOAL.md 7. pontját.

## 4. Modellválasztás – a keret kímélése
- **GPT-5.6 Sol**: normál tervezés, rutin Blender-szkript, szövegek.
- **GPT-6 Astra**: bonyolult geometria, összeomló szkript, nehéz automatizálás, többlépéses feladat, nagy bemenet.
- **Erős gondolkodási fokozat**: csak ha a közepes nem boldogul.
- Nem használunk Astrát apró módosításra. Nagy bemenet (sok kép, hosszú fájl) gyorsabban fogyasztja a keretet – előbb szűrjük, mit töltünk fel.
- A Revolut Ultra-s **Go** csomagban van képgenerálás, de nincs Astra, agent-mód és connector; ehhez Plus (vagy magasabb) kell.

## 5. Hozzáférés és Blender
- A böngészős Work **nem látja** a Macen futó Blendert. Blenderhez: **ChatGPT Mac-alkalmazás** (helyi fájlok, támogatott asztali appok) vagy **Codex** (helyi projektmappa + terminál). Hogy mit tud ténylegesen vezérelni, az az alkalmazás támogatásától és az engedélyektől függ – nem garantált.
- **Egy jeleneten egyszerre egy vezérlő**: vagy Claude MCP, vagy ChatGPT Mac-app/Codex. Soha ne fusson a kettő ugyanazon a .blend-en párhuzamosan.
- A Codex projektmappája a repo helyi klónja (`~/Projects/wsg-berendezes`); a GitHub-connector a Workben a `wsg-berendezes` repót olvassa.

## 6. Briefelés – így adunk feladatot a ChatGPT-nek
- Minden briefben: a `GOAL.md` releváns része (lakás, helyiség méretei, keret), a kért kimenet és a fájlnév-szabály. Ha Project/connector van, elég hivatkozni a fájlra.
- Képgenerálásnál a bemenet sorrendje: [1] Blender-nézet (geometria – pontosan tartandó), [2] stílus-referencia (Zenit vagy Lake Forest), [3] termékfotó, ha van. Prompt a `05_promptok/`-ból; új promptot oda is beírunk.
- Kimenet: képek `04_renderek/ai_chatgpt/A<lakás>_<stílus>_<n>_<helyiség>_chatgpt.png`; eltéréslista `06_koncepcio/`; szkript `03_blender/`.
- Chrome-on át Claude külön fülön dolgozik, Péter saját fülét nem használja.

## 7. Amit a ChatGPT mond, az nem automatikusan igaz
- Termék, méret, ár: csak forrással és dátummal fogadjuk el, „ellenőrzött"/„becslés" jelöléssel; Kave Home ár csak a webshopból, IKEA méret csak termékadatból.
- Ha a ChatGPT és a GOAL.md ellentmond, a GOAL.md nyer, és Claude javít.
- Küldés, rendelés, fizetés: soha nem a ChatGPT dönti el – Péter „mehet"-je kell.
- Személyes adat (leadek, szerződések, e-mailek) nem kerül a repóba és nem megy a ChatGPT-nek.

## 8. Fájlok a repóban
`OPENAI_instructions.md` (Work házirend + a fenti szereposztás, a Project Instructions mezőjébe), `AGENTS.md` (Codex házirend), `GOAL.md` (igazság), `MUNKAMENET.md` (a teljes három-AI munkamenet, 8 évesnek is elmagyarázva), `03_blender/wsg_helpers.py` és `stil_lakeforest_layer.py` (minta a Codexnek).
