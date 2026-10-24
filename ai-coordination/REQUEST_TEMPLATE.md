# WSG AI-feladatátadás – kitöltendő sablon

> Claude egyetlen, önmagában érthető és visszakereshető briefet készít. Ez nem instrukció arra, hogy minden PR automatikusan kreditet fogyasszon. A `[ASTRA-REVIEW]` jelölést csak az Astra/Work-nek szánt átadás kapja, az aktiválás **ready for review** állapotváltással történik.

- **Task ID:** WSG-YYYYMMDD-001
- **Cél AI:** ASTRA_WORK | CODEX | GEMINI
- **Típus:** STYLE_CONCEPT | PRODUCT_RESEARCH | INDEPENDENT_COST_AUDIT | RENDER_PROMPT | BLENDER_AUDIT | VIDEO
- **Lakás:** A-811 | A-812 | A-902
- **Helyiségek:** pontos megnevezés
- **Stílus:** azonosító vagy `ÚJ STÍLUS – NINCS MÉG KIVÁLASZTVA`
- **Prioritás:** normal | high
- **Javasolt gondolkodás:** medium (Ultra csak Péter jóváhagyásával)
- **Engedély a Work automatikus indításához:** yes | no
- **Keret:** bruttó teljes lakáskeret, fel nem osztott rész és 10% tartalék
- **Bemenet:** konkrét repo-fájlok elérési útja és a helyi Blender-renderek GitHubra mentett változata
- **Rögzített geometria:** falak, ablakok, belmagasság, kamera, bútorpozíciók, bizonytalan méretek
- **Korábbi döntések:** mi fix; mi csak kísérleti elképzelés
- **Kért eredmény:** pl. 3 stíluskártya + hozzájuk prompt + előzetes árkockázat + 1–3 WOW-gesztus
- **Vizuális sikerfeltétel:** nem csak szép, hanem kivételesen drágának ható, ízléses, ténylegesen kivitelezhető luxus
- **Költségsikerfeltétel:** valós termék/anyag/opció vagy külön becslés; semmi nem szerepelhet bizonyítottként ellenőrzés nélkül
- **Mi NEM feladat:** ne írja felül Claude Blender fájljait, ne rendeljen, ne küldjön ajánlatkérést, ne válassza ki Péter helyett a végleges stílust
- **Visszaadás:** PR Conversation comment `WSG-ASTRA-RESULT: <ID>` formában; ha nincs joga, Work eredmény és `handoff blocked` jelzés

## Rövid összefoglaló

**Feladat (2–5 mondat):** …

**Függőségek / kockázatok:** …

**Kész definíciója:** …

**Ellenőrző lista Claude-nak:** ugyanazt a briefet küldted? biztosan csak egyszer indítod? elérhetők a hivatkozott fájlok? a képek ténylegesen a repóban vannak? a feladat része-e a keret és a 10% tartalék?

## Kötelező Render Reality Gate mezők

- **Reality card / preflight:** repoelérési út vagy tartalom; verzió, kamera, forrás-Blender/fotó és bizonytalanság.
- **Meglévő/megtartott felületek:** WSG szürke tölgy padló; fehér falak; mennyezet, fekete nyílászárók, fix geometria. Padló pontos dekor/SKU helyszíni bizonyításig `NEM IGAZOLT`.
- **Tervezett új felületek:** hol, hány m², konkrét panel/tapéta/festés, valós vizuális megjelenés, bruttó anyag- és szerelési ár/státusz.
- **Render-szint:** `KONCEPCIÓ – NEM VALIDÁLT` | `ELŐSZŰRT – FELTÉTELES` | részletes termékhűség-vizsgálatra kért.
- **Preflight gate:** `ai-coordination/RENDER_REALITY_GATE.md` szerinti anyag-/geometrialezárás és vizuális PASS/FAIL elvárások; takart padló `nem ellenőrizhető`.
