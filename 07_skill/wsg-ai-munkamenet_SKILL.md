---
name: "wsg-ai-munkamenet"
description: "A Westside Grand berendezési projekt négy-AI munkarendje: Claude (fő műszaki kivitelező, Blender egyetlen vezérlője, független költségellenőr), ChatGPT Work/Astra (kreatív tervező + független termék- és költségellenőr), Codex (geometriai és programozási auditor), Gemini (kép és videó), GitHub (közös memória). Használd, ha a WSG-projektben ChatGPT-t, Codexet, Geminit briefelünk, átadunk, auditálunk, a repót szinkronizáljuk vagy a keretet kíméljük."
---

# WSG – AI-munkamenet: ki mit csinál, hogyan adunk át, mit ellenőrzünk

A repo (`peterkapusi88-hub/wsg-berendezes`, main) a közös asztal; `AI_START_HERE.md` a belépési útmutató. **A GitHub nem közös memória vagy üzenetbusz: a repóba mentett munkatermék az átadás, nem a chat-előzmény.** Minden munkamenet elején a friss `GOAL.md` → `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` → szerep szerinti házirend (`CLAUDE.md` / `OPENAI_instructions.md` / `AGENTS.md`).

## 1. Szereposztás (érvényes 2026-10-24-től)
| Szereplő | Feladat | Nem csinálja |
|---|---|---|
| **Péter** | dönt, „mehet”-et mond, fotóz, fizet; stílusok közül választ | – |
| **Claude** (Cowork/Desktop) | fő műszaki kivitelező: alaprajz, méretek, **Blender MCP egyetlen vezérlője**, Geometry Validator, renderek, keretszámítás, tételes lista, **a ChatGPT termék- és árválasztásának független újraellenőrzése** (saját forrásból, nem átmásolva), asztalos-rajz, e-mailek, repo-karbantartás (GOAL.md állapot/döntések) | nem írja felül automatikusan a ChatGPT tervezői szempontjait; nem nevez koncepció-rendert kivitelezhetőnek |
| **ChatGPT Work / Astra** | kreatív tervező: stíluskártyák, koncepció, forma–szín–tér–fény alternatívák, képi/videós promptok, esztétikai kritika; **független termékkutatás és árellenőrzés** (konkrét termék, link, ár, dátum); render-vs-tétellista eltéréslista | nem vezérli a Blendert; nem kattintgat Claude helyett |
| **Codex** (ChatGPT Mac-app, helyi klón) | geometriai és programozási auditor: mérhető Blender/Python-tesztek, bútorméret, közlekedő, mennyezeti panel kockázat, kódreview; olvas és tesztel, lehetőleg külön ágon/PR-ben | nem módosítja Claude élő Blender-jelenetét; árat nem talál ki |
| **Gemini** (peter.kapusi88 fiók) | fotorealisztikus képek a Blender-nézetből (Nano Banana) és videó (Flow/Veo) a jóváhagyott briefből | nem változtat geometriát; a GitHub-importja pillanatkép – ellenőrzés előtt újra kell tölteni |
| **GitHub** | verziózott közös tudástár; minden átadás fájlban/PR-ben | nem indít automatikusan másik AI-feladatot |

## 2. Egy kör (átadási lánc)
1. **Work** stíluskártya + brief (forma, szín, tér, fény, anyag, WOW-gesztusok) és termékjavaslatok árral → repo (`06_koncepcio/`, `05_promptok/`).
2. **Claude** Blender-réteg + Validator + renderek a három rögzített kamerából → `03_blender/`, `04_renderek/`, validator-jelentés; **külön** árellenőrzés a Work terméktáblájára → vizsgálati tábla (tétel, ChatGPT ár/link/dátum, Claude ár/forrás, delta, állapot).
3. **Codex** (ha kell) geometriai teszt / review → eltéréslista, PR.
4. **Gemini / ChatGPT képgenerálás** a Blender-nézet + referencia + termékfotó alapján → `04_renderek/ai_*`; státusz-címke (koncepció / keretre előszűrt / tételesen költségelt / ajánlattal validált).
5. **Péter** választ; Claude a döntést a `GOAL.md` 7. pontjába írja. Rendelés, küldés, fizetés csak „mehet” után.
Egyszerű hibát (rossz anyagbeállítás, elmozdult bútor) Claude önállóan javít; Astrához csak új kreatív döntésnél fordulunk.

## 3. Keretkímélés
- ChatGPT: rutin → **Sol**; bonyolult geometria, összeomló szkript, többlépéses feladat → **Astra**, előbb alacsony/közepes, erős csak ha kell; Work és Codex ugyanazt a keretet fogyasztja. Astrát nem apró módosításra. Nagy bemenet (sok kép) gyorsabban fogyaszt – szűrni.
- Claude: a hosszú Blender-javítási ciklusokat ne a legdrágább modell/legmagasabb erőfeszítés vigye; mérés (Validator) helyettesíti az AI-véleményt, ahol lehet.
- Nem építünk egymást hívogató automata AI-rendszert: néhány jól elhelyezett ellenőrzési pont, kézi átadás; automatizálás csak a bevált lépésekre.

## 4. Hozzáférés és mechanika
- **Claude GitHub-app**: amíg nincs jogosultsága a repóra (GitHub → Settings → Applications → Claude → Configure → Repository access), Claude a Chrome-on át olvassa a `/raw/main/...` fájlokat és a webes feltöltővel (`/upload/main/<mappa>`, ≤10 MB/hívás) tölt fel; a helyi tükör `/home/claude/wsg-berendezes` (konténer) és `~/Downloads/wsg-berendezes` (Mac, Cowork-projekt mappája, Codex klónja).
- **Egy jeleneten egyszerre egy vezérlő** (Claude MCP, localhost:9876). A Blender Lab MCP add-on újraindítás után a Preferences-ben mentve kell legyen.
- Chrome-on Claude saját fülön dolgozik, Péter füleit nem használja; ChatGPT/Gemini képcsatolás rejtett file-input + paste-esemény, prompt `insertText`.
- Fájlnevek: `A<lakás>_<stílus>_<n>_<helyiség>.jpg` (AI-kép), `A<lakás>_<stílus>_blender_<n>_<helyiség>.png` (Blender), `_chatgpt` utótag a ChatGPT-képeknél. Promptot mindig a repóba is.
- Személyes adat (leadek, szerződések, e-mailek) nem kerül a repóba és nem megy más AI-nak.

## 5. Amit nem fogadunk el bizonyítás nélkül
- ChatGPT (és bármely AI) termék-, méret- és áradatai: csak forrással és dátummal, „ellenőrzött”/„becslés” címkével; Claude külön forrásból ellenőriz, eltérést dokumentál, nem átlagol.
- A render nem költségvetés; két eltérő AI-kép nem ugyanaz a költség. A GOAL.md nyer minden ellentmondásban, Claude javít.
- Gyártói benchmark-állítások (melyik modell „jobb geometriában”) nem döntenek: egy valós szobán mért összehasonlítás (pontosság, idő, keret) dönt, ha egyáltalán kell.
