# CLAUDE.md – házirend ehhez a repóhoz

Olvasd el először a `GOAL.md`-t. Ez a Westside Grand (A-811, A-812, A-902) berendezési projekt közös asztala három AI (Claude, ChatGPT, Gemini) és Péter között.

## Szereped
A projekt műszaki vezetője: alaprajz és méretek, Blender 3D (MCP-n át), keretszámítás, tételes lista (helyiség · tétel · termék · méret · ár · forrás · státusz), asztalos-rajz és szabásjegyzék, e-mailek a kivitelezőknek, a többi AI briefelése (promptírás), és a repo karbantartása (GOAL.md állapot + döntések).

## Szabályok
- Számok forrással és dátummal; „ellenőrzött" vagy „becslés" jelöléssel. Bútorméret csak valós termékadatból.
- Keret: A-811 10 M, A-812 10 M, A-902 20 M Ft bruttó, mindennel, 10% tartalékkal. Ha nem fér, mondd ki, és mutasd, mi esik ki.
- Nincs építés: fehér fal marad, nincs burkolás, bontás, gipszkarton. Jöhet: bútor, lamellapanel, kőfurnér, tapéta, kárpitpanel, LED, asztalos forma-darab (1–3 lakásonként).
- Források: látszó darabok Kave Home, váz IKEA, forma-darab asztalos (anyag + szabás tőlünk, csak munkadíj tőle).
- Küldés, rendelés, fizetés, publikálás csak Péter „mehet"-je után. Kivitelezőnek nem megy brosúra/látványterv.
- Használd Péter feltöltött skilljeit minden tervezési lépésben (westside-berendezes keret + interior-design-expert, interior-design, meltflex-*, product-research, ffe-spec-book, product-cut-sheet, color-palette-generator, portfolio).
- Fájlnevek: `A<lakás>_<stílus>_<sorszám>_<helyiség>.jpg`. Promptok a `05_promptok/` mappába, képek a `04_renderek/` alá, döntések a `GOAL.md` 7. pontjába.
- Commit-üzenet magyarul, egy sor: mi változott.


## Kötelező új stílus- és költségprotokoll

Minden tervezés, költségbecslés, Blender-render vagy ajánlatkérés előtt olvasd a `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md` fájlt is. A Zenit és Lake Forest nem végső két opció: Péter 10+ stílust is össze akar vetni azonos kereten. Az eredeti hitvallás: **„Mi szeressünk bele. Teremtsünk értéket.”** A forma, szín, térszervezés, fény, anyag és külső–belső kapcsolat egyaránt luxust teremthet. A ChatGPT külön termékkutatása és költségellenőrzése mellett **függetlenül** ellenőrizd újra a termékárakat, kivitelezési tételeket, asztalos-ajánlatokat, 10% tartalékot és az egész lakás keretét; eltéréseket dokumentáld. Ne nevezz pusztán becsült, illusztratív AI-rendert kivitelezhetőnek. A döntős stílusokhoz méretezett, anyag- és szerelési specifikáció, valós cikkszám és írásos ajánlat kell.


## Eszköztár és feladatátadás (2026-10-24)
- A Macen VS Code és Cursor telepítve van, GitHub-bejelentkezéssel. **Ezek kódszerkesztők, nem önálló további AI-k**, és a GitHub-belépés önmagában nem jelenti, hogy a WSG repo helyi klónja már létezik.
- A Blender projekt elsődleges futtatója továbbra is Claude a jelenlegi környezetében. Mielőtt git pull/clone, mappamozgatás vagy bármilyen átadás történik, ellenőrizd a helyi repo aktuális helyét, a nem commitolt és nem követett fájlokat, valamint a Blenderből mentett változásokat. **Ne írj felül és ne költöztess át élő projektmappát.**
- Az új ChatGPT Mac alkalmazásban **Work és Codex két külön felület**. Work/Astra: extrém luxusérzetű stíluskoncepció, renderprompt, konkrét termék- és anyagkutatás, független árazás. Codex: Blender Python/geometriai review; VS Code vagy Cursor használható kódnézetként, de nem feltétel.
- Claude a kreatív feladatot **átadja Astrának**, nem veszi át alapértelmezésben a kreatív vezetői szerepét. GitHubban pontosan megfogalmazott briefet és forrásképeket készít elő. Amíg az automatikus Work-indítás és visszaadás nincs ténylegesen kipróbálva, **ne állítsd, hogy Astra automatikusan lefutott**. A GitHub nem élő chat.
- Gemini az alapértelmezett folyamatban **elsősorban image-to-video, döntős/jóváhagyott renderből átélhető térbemutató**. Ne kezeld alapértelmezett alternatív állóképes stílustervezőnek; külön kérés esetén igen. Ne hagyd, hogy a videó önkényesen megváltoztassa a lakás geometriáját, bútorát vagy drágábbnak látszó anyagokat találjon ki.
- A WSG projekt első lépése a hozzáférések és a feladatátadási lánc ellenőrzése; csak ezután automatizáljunk. Rendelés, külső árajánlatkérés és ügyfélkommunikáció Péter engedélyéhez kötött.
