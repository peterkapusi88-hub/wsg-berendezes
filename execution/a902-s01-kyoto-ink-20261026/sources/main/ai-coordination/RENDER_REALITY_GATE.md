# WSG – Render Reality Gate (kötelező vizuális és költséghűségi kapu)

**Hatály:** A-811, A-812, A-902; Claude, ChatGPT Work/Astra, Codex, Gemini/Flow. Közös szabály: `GOAL.md` + `07_skill/wsg-ertekalapu-stiluslabor/SKILL.md`. A szabad stíluskísérleteket nem tiltja, de különválasztja a fantáziaképet a megvalósítható tervtől.

## A. Meglévő állapot – kötelező zárolás
- **Meglévő padló:** Egger szürke tölgy parketta, megtartandó. **Pontos dekor/SKU, szín, szemcse és deszkaméret: a helyszíni fotó és termékazonosítás előtt NEM IGAZOLT.** A „light oak”, „grey oak” AI-interpretáció nem termékazonosítás. A padló csere vagy átszínezés nélkül jelenjen meg a megvalósítást állító renderben. Ha szőnyeg takarja: státusz „nem látható/nem ellenőrizhető”, ne „megfelelt”.
- **Falak:** meglévő fehér, alapból fehérek maradnak. Krém/greige tónus lehet fényhatás; tényleges festés, vakolat, tapéta, dekorpanel csak kijelölt felületen, külön tétellel, mérettel és bruttó kivitelezési költséggel. Képről a fényhatás és felületcsere bizonytalansága jelezendő.
- **Fix építészet:** falak, padló, mennyezet, belmagasság, ajtók (világosszürke), ablakok és kereteik (**belül fehér, kívül antracit** – IGAZOLT-F 2026-10-21), gépészet, hűtő-fűtő mennyezeti panelek és panoráma/terasz valós forrásból. Nincs kitalált új helyiség, ablak, fülke, süllyesztett mennyezet, új kilátás.
- **Forrásbizonytalanság:** brosúraméret / Blender-becslés / helyszínen lemért / termékkóddal igazolt – egymástól elkülönítve. Fotó hiányában a meglévő felület nem válik automatikusan hitelessé.

## B. Render előtti anyag- és tételkiosztás (preflight)
Minden helyiség / kamera esetén hozz létre rövid, verziózott `RENDER_REALITY_CARD`-ot vagy táblát:
1. forráslakás, kameraazonosító, bemeneti Blender-kép/fotó, készültségi szint;
2. **felületenként:** padló, bal/jobb/hátsó fal, TV-fal, mennyezet, nyílászáró, konyha; `MEGLÉVŐ / MEGTARTOTT`, `ÚJ / ÁRAZOTT`, `JAVASOLT / BECSLÉS` vagy `ISMERETLEN`;
3. új látható elem azonosító, gyártó/SKU vagy egyedi gyártási specifikáció, pontos/tervezett méret, **képen megjelenítendő tényleges felület**, bruttó ár és forrás/dátum, beépítés/szállítás/LED/szerelés, bizonytalansági sáv;
4. drága látványelemnél (kő, márvány, TV-fal, íves asztalos, csillár) valós anyag **vs.** kőhatású panel/laminátum külön néven; az illusztráció nem mutathat lényegesen nem megvásárolt prémium anyagminőséget jóváhagyott valóságként;
5. teljes **lakás** bruttó keretellenőrzés A-811/A-812 10 M, A-902 20 M Ft, tartalék minimum 10%, minden lakásrész/terasz/szállítás/szerelés/tervezés figyelembevéve; becslés nem ajánlat;
6. **renderprompt** külön rögzítse: megőrzendő felületek/nyílások + csak engedélyezett új elemek + pontos anyagmegjelenés. A „luxury travertine” nem írhatja felül a ténylegesen tervezett travertin-hatású panelt.

**Kreatív gyors kör kivétele:** 10+ stílus első szabad képalkotó körében elég egy minimalista kártya, becsült költségsáv és egy látható `KONCEPCIÓ – NEM VALIDÁLT` jelölés; csak utána lehet preflighttal megvalósítható jelöltként továbbvinni.

## C. Kép/videó utáni kötelező audit
Hasonlítsd össze (1) rögzített eredeti fotó/Blender-nézet, (2) render/videó kezdő- és záróképkocka, (3) reality card, (4) terméklista/költségterv. Minden lényeges látható elemhez sor:
`elem | forrás/azonosító | tervezett valós felület | képen látott | eltérés | Ft-kockázat | bizonyíték | döntés`.
Kötelező részellenőrzések:
- **Padló**: szín, mintázat, deszkairány és láthatóság; nem igazolható, ha takart vagy nincs hiteles referenciakép.
- **Falak**: ténylegesen fehérek-e, vagy megjelenő krém/greige falszínhez festési/tapétázási tétel kell; a megvilágításból eredő elszíneződést külön jelöld.
- **Geometria**: fix fal/ablak/ajtó/mennyezet, terasz, perspektíva, bútorpozíció, méret és közlekedő.
- **Anyagok**: valódi kőnek néző olcsó panel, márványnak néző laminált lap, hibás front és asztalos részlet, rejtett szerelési költség.
- **Termékek**: AI által kitalált kanapé, lámpa, plusz bútor; valós termék konfigurációja és mennyisége.
- **Videó**: külön objektummorfing, változó ablakok, kitalált kilátás, fizikailag lehetetlen kameramozgás; a kép/videó nem geometriai mérés.

## D. Döntési kapu és státusz
- `KONCEPCIÓ – NEM VALIDÁLT`: vizuális ötlet; még nem állítható megépíthetőnek, pontos padlónak vagy árra igazoltnak.
- `ELŐSZŰRT – FELTÉTELES`: fő látványelemek és költségsávok szerepelnek; még nem termékhű.
- `RENDER REALITY PASS – TÉTELES`: minden lényeges látható elem megfelel a rögzített anyag- és termékspecifikációnak, elfogadható geometriával, teljes bruttó lakáskerettel és minimum 10% tartalékkal. A bizonyíték nélküli anyagok `nem igazolt` státuszúak, ezért nem PASS.
- `AJÁNLATTAL VALIDÁLT`: a fenti megfelelés mellett a szükséges tényleges asztalos/kivitelezői ajánlatok és friss beszerzési árak is igazoltak.
- `FAIL / ÚJRATERVEZÉS`: kicserélt parketta, nem engedélyezett/árazatlan új festés vagy burkolat, drágábbnak megjelenített anyag, kitalált geometria, nem létező termék vagy a teljes keret túllépése. Javítás, tételes beárazás + Péter jóváhagyása, vagy visszasorolás `KONCEPCIÓ`-ba.

**Tiltás:** `PASS` vagy `AJÁNLATTAL VALIDÁLT` megnevezés nélküli ellenőrzést nem lehet „kész, kivitelezhető látványtervként” prezentálni. A kreatív munka legyen bátran luxus, de a valós kivitelezhetőség státuszát soha ne találjuk ki.

## E. Szerepek és átadás
- **Claude:** összegyűjti a valós állapotot, készíti a reality cardot, kezeli a Blender-geometriát, külön árauditot végez, vezeti a státuszt.
- **Work/Astra:** kreatív irányok és renderprompt a reality card szerint; független termék-/anyag- és keretvizsgálat, render vs. specifikáció eltéréslista.
- **Codex:** automatizálható geometria-/kamera-/objektumellenőrzések; élő Blender MCP-t nem veszi át.
- **Gemini/Flow:** csak a megadott forrás és specifikáció alapján animál; benchmark célból nem validált korábbi kép is használható, de `KONCEPCIÓ ALAPÚ VIDEÓTESZT – NEM KIVITELEZÉSI BIZONYÍTÉK` címkével.
- **Péter:** stílusjóváhagyás, módosítás, külső kötelezettségvállalás.

Alapértelmezett kimeneti szerkezet: `REALITY CARD → KREATÍV KÉP/VIDEÓ → VIZUÁLIS ELTÉRÉSLISTA → STÁTUSZ → KÖLTSÉGKOCKÁZAT → DÖNTÉSI KÉRDÉSEK`. Minden mesterségesen generált kép saját azonosítót és visszakövethető inputverziót kap.

