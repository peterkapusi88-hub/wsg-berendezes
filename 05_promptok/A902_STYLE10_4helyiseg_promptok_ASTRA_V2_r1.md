# A-902 · STYLE10 · négyhelyiséges renderpromptok · ASTRA V2 r1

WSG-RESULT: WSG-20261024-ASTRA-KREATIV-V2
Szerző-AI: ChatGPT / Codex, a felhasználó által Astra Mediumként indított kreatív munkamenet
Modell: Astra – felhasználói felületigazolás; pontos modellverzió technikailag nem igazolt
Szint: Medium – Péter chatbeli igazolása: „Astra, Medium beállítva”
Bázis-commit: 46e3c5cbe2607479d7eba8037b1fbbc164365fe6
Státusz: TELJES kreatív szövegcsomag (40/40) · KONCEPCIÓ – NEM VALIDÁLT · KÉPFÁZIS ZÁRVA
Dátum: 2026-10-24, Europe/Budapest

Ez új, önálló r1 fájl. A STYLE10-002 §10 v1 promptjai, a Cam_02 v2 sablon és a v3.1 fixed blokkok változatlanok. **Ebben a feladatban kép nem készült.** Az alábbi 40 angol blokk nem írja felül a valós termék- vagy geometriai hiányokat: a KEP-004 kapu után futtatható; jelenleg feltétel nélküli azonnali képfuttathatóság nem állítható.

## Összefűzés és forráselsőbbség

Minden végső képprompt sorrendje: **[v3.1 sablon](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md) §1 közös FIXED blokk szó szerint → ugyanott §2 megfelelő helyiség FIXED blokkja szó szerint → az alábbi egyetlen stílus/helyiség blokk**. A két fixed blokkot ez a fájl nem ismétli és nem fogalmazza át. A képfázis mentse az összefűzött szöveget a megadott .prompt.txt mellékletbe. A stílusblokk nem írhatja felül a fixed blokkot; hiány vagy ütközés esetén Claude tisztázása kell, nem az AI rögtönzése.

A termékrekordok a 2026-10-24-i kész forrásokból származnak: **nem új webkutatás, nem friss ár- vagy rendelési igazolás**. Az árkönyvtárban hiányzó méretet nem pótoljuk becsült termékmérettel. A custom méretek viszont tudatos **tervezett befoglalók**, nem megmért lakásadatok vagy igazolt gyártmánytervek. W × H × D = szélesség × magasság × mélység; a gyári termékméretnél a forrás sorrendje érvényes.

Az aktív promptokban a NORDLI ismert külső befoglalójú alap marad. A Kave Home Selven/Martina/Nahiri ágyjelöltek adata csak matracméretet ad; ezért nem rajzoljuk ezeket 180×200-as külső testnek. Választásuk az eredményfájl termékfüggelékében szerepel, nem automatikus rendercsere. A JÄTTEBO U-k a briefben és az auditban megőrzött kész horgonyok; Westwing és Kave Home az étkezőben, textilekben, világításban és alternatív főbútorokban egyenrangúan szerepel.

## Képbemenetek – a v3.1 §0/a változatlan átvétele

## 0/a. Képbemenetek helyiségenként – kötelező sorrend (Péter 21:18)

Minden prompthoz a bemeneti képek ebben a sorrendben, és a prompt szövege hivatkozik rájuk („image 1 = geometry…”). Ami még nincs meg, azt a képfázis kapuja előtt kell pótolni; Astra a V2-ben a listát változatlanul veszi át.

| Helyiség | 1. Hiteles Blender-kameraalap (geometria + kamera, kötelező) | 2. Valódi helyszíni anyag- és felületfotók (kötelező) | 3. Eredeti kreatív referencia (opcionális, csak hangulat/küszöb, nem geometria) | 4. Termékfotó (hős-darabok, termékoldalról) |
|---|---|---|---|---|
| Nappali–terasz (Cam_02) | `04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png` (v2b-1-ből újrarenderelve) + ellenőrző `04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png` | `08_allapotfelmeres/fotok/A902/04_nappali/…ME-BAL-080_parketta_szegely_kozel.jpg` (padló), `…ME-BAL-045_nappali_terasz_fele.jpg` (fal, profil, terasz), `…ME-BAL-046_nappali_eloter_fele.jpg`; terasz: `00_besorolando/…ME-BAL-042_greslap_lepcso_teglafal.jpg`, `…ME-BAL-044_greslap_kozel.jpg`, `…ME-BAL-053_teraszajto_sotet_tegla_kava.jpg`; panoráma `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg` | Zenit/LF: `04_renderek/ai_chatgpt/A902_Zenit_1_nappali_chatgpt.png`, `A902_LakeForest_1_nappali_chatgpt.png`; `ai_gemini/A902_Zenit_1_nappali.jpg`, `A902_LakeForest_1_nappali.jpg` (KONCEPCIÓ – NEM VALIDÁLT; kamerájuk eltér) | kanapé, étkezőasztal |
| Konyha–étkező (Cam_03) | `…A902_Alap-v2b_blender_03_etkezo-konyha.png` (v2b-1) + `04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png` | `08_allapotfelmeres/fotok/A902/02_konyha/…ME-BAL-056_konyhafal_kiallasok.jpg` (konyhafal, kiállások, mellvéd), ME-BAL-080 (padló), ME-BAL-045 (fal/profil) | `ai_chatgpt/A902_Zenit_2_etkezo_konyha_chatgpt.png`, `A902_LakeForest_2_etkezo_konyha_chatgpt.png`; `ai_gemini/…_2_etkezo_konyha.jpg`; `blender_stilusok/…_2_etkezo_konyha.png` | front/dekor minta (Egger kód), étkezőasztal, szék |
| Master 05.1 (Cam_04) | `…A902_Alap-v2b_blender_04_master.png` (**v2b-1-ből újrarenderelve** – a fülke-javítás érinti) + `04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png` | ME-BAL-080 (padló), `00_besorolando/…ME-BAL-060_szoba_teraszajto.jpg`, `…ME-BAL-069_szoba_teraszajto2.jpg`, `…ME-BAL-063_szoba_ajto.jpg` (szobaajtó, profil, redőny – besorolásuk 05.1/05.2/05.3 a hétfői fotókkal pontosítandó) | `ai_chatgpt/A902_Zenit_3_master_chatgpt.png`, `A902_LakeForest_3_master_chatgpt.png`; `ai_gemini/…_3_master.jpg`; `blender_stilusok/…_3_master.png` | ágy, fejvég-anyag |
| Fürdő 06.2 (Cam_10 – FELTÉTELES) | **még nincs** – Claude készíti a v2b-1 .blend-ből a Cam_10 rögzítése után (bútor nélkül, meglévő szaniterekkel) | `00_besorolando/…ME-BAL-064_furdo_zuhany.jpg` (kőhatású lap, walk-in zuhany, fekete esőztető), `…ME-BAL-066_furdo_torolkozoszarito.jpg` (fekete törölközőszárító) – **melyik fürdőt mutatják (06.1/06.2), még besorolandó**; a 06.2-ről célzott fotó a hétfői (2026-10-26) sorozatból pótlandó | nincs eredeti Zenit/LF fürdőreferencia → a kalibráció a nappali/master képekre épül | tükör, tároló, textil |

A fürdő 06.2 hiányzó alapképe és fotója **nem akadálya a V2 promptírásnak** (a prompt a lock adataira és a meglévő burkolat/szaniter leírására épül), de **a képfázis kapuja**.



### A rövidített fotóazonosítók tényleges repóútvonalai

- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-042_greslap_lepcso_teglafal.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-044_greslap_kozel.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-053_teraszajto_sotet_tegla_kava.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-060_szoba_teraszajto.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-063_szoba_ajto.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-064_furdo_zuhany.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-066_furdo_torolkozoszarito.jpg`
- `08_allapotfelmeres/fotok/A902/00_besorolando/A902_00_20261021_ME-BAL-069_szoba_teraszajto2.jpg`
- `08_allapotfelmeres/fotok/A902/02_konyha/A902_02_20261021_ME-BAL-056_konyhafal_kiallasok.jpg`
- `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg`
- `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-046_nappali_eloter_fele.jpg`
- `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg`
- `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg`

## Termék- és gyártási kapuk

- **K8:** Eamy/Ciselia teljes külső méretei hiányoznak az árkönyvtárból; a hat szék használati és szállítási méretét a képfázis előtt rögzíteni kell. Ne legyen generikus vagy kicsinyített helyettesítés.
- **S06:** Blok sarokirány a pontos termékfotóhoz kötendő. **S10:** Neom 263 teljes mélység/magasság és választott sarokirány nincs a forrásban. **S09:** Corvena 98 cm széles, nem a korábbi 80 cm célbefoglaló; további méretek és teljes ülőcsoport-próba kell.
- **Kerek étkezők:** Nealy Ø150, Argo Ø119 és Naanim Ø120 új teljes székkihúzási vizsgálatot igényelnek; hat helyet nem állítunk igazoltnak a puszta átmérőből. A termékmagasságok hiányoznak a forrásból.
- **Lámpák:** a dokumentált átmérő vagy gömbátmérő nem teljes lámpabefoglaló; függesztési hossz, rögzítés, terhelés és villamos megfelelés a meglévő pontokon igazolandó. A master kis olvasólámpái és a fürdő opál fénytestei típus-előírások, nem kitalált késztermékek.
- **Költség:** a drágább csomagok PREMIUM/átrendezendő jelölése az eredményfájlban; egyik prompt sem beszerzési engedély. A 07 sor két fürdőt és a WC-t együtt fedezi.
- **K4/H7:** v2b-1 kameraalapok és a 06.2 célzott fotója szükséges. Cam_10 még feltételes; ne kompenzáld szélesebb objektívvel vagy szaniter-áthelyezéssel.
- A 3D méretpróba nem bizonyítja a hat szék 90 cm-es kihúzását. A korábbi P902_24A 0,51 m nyugati székhézagát nem nevezzük 90 cm-nek. A fixed blokk és a tényleges használat közti eltérés képfázis előtti tisztázandó kapu.


## 40 angol stílusblokk

### S01 — Kyoto Ink · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Contemporary Japanese luxury through low graphite horizons, taupe woven upholstery, translucent natural textile and precisely proportioned white voids; each room interprets layering rather than repeating a beige palette.

Room composition: Place the exact right-hand Lennon L as one low seating island on the Nifelia rug, with the west-facing TV integrated into a long graphite cabinet. Offset one translucent textile panel beside, not over, the screen; let its real shadow and a narrow open lattice edge reveal the white wall behind it. Keep the upper wall mostly empty and the dining oval visually separate from the denser sofa. On the accessible tiled terrace, repeat only the low horizon with the specified removable bench; retain the threshold, steps and planting.

Products (verified records): P14: Westwing Lennon right-hand L, taupe woven polyester upholstery, DEQ21WES12329-168260; 238 × 180 × 68 cm; recorded price 800,000 HUF, 2026-10-24; https://www.westwing.hu/lennon-modularis-sarokkanape-hu-21wes12329.html?simple=DEQ21WES12329-168260; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

P09: Westwing Toni oval dining table, light oak veneer/MDF, 200 cm version, DEQ19WES60483-150724; 200 × 90 × 75 cm; recorded price 320,000 HUF (not the price of the 160 cm version), 2026-10-24; https://www.westwing.hu/toni-ovalis-alaku-fa-etkezoasztal-200-x-90-cm-hu-19wes60483.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-EAMY-LG: Kave Home Eamy chair, light-grey chenille, natural ash veneer and black metal; outer dimensions NOT RECORDED in the source; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-light-grey-chenille-and-ash-wood-veneer-with-a-natural-finish-and-black-metal; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-NIFELIA: Kave Home Nifelia beige wool jacquard rug; 200×300 cm; recorded price 439 EUR, 2026-10-24; https://kavehome.com/hu/en/p/nifelia-beige-wool-jacquard-rug-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-SOMAR76: Kave Home Somar pendant, synthetic fibres and steel rods; Ø76 cm; recorded price 579 EUR, 2026-10-24; https://kavehome.com/hu/en/p/somar-ceiling-lamp-made-with-synthetic-fibres-and-steel-rods-o76cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: KI-L: media cabinet W240 × H48 × D40 cm, white board carcass, matte graphite laminate (sample/code to be approved), 2 mm matching ABS edge, recessed floor-supported plinth, removable cable back at D16/D17. KI-T: W100 × H180 × D3 cm translucent linen frame, black open lattice strip W15 cm, wall cleat 2–3 cm off wall, no backlight. KI-O: terrace bench W160 × H42 × D60 cm, powder-coated aluminium frame and outdoor HPL seat, loose neutral outdoor cushion; freestanding on gres, no roof fixing. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,800 M HUF, 03b cap 0,800 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-SOMAR76 only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: fake shoji doors, bonsai styling, all-beige Japandi, a full slatted wall, dramatic amber lighting. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S01 — Kyoto Ink · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Contemporary Japanese luxury through low graphite horizons, taupe woven upholstery, translucent natural textile and precisely proportioned white voids; each room interprets layering rather than repeating a beige palette.

Room composition: Create a disciplined graphite lower kitchen band below quiet off-white upper fronts, with the thin light-grey concrete-effect laminate worktop clearly reading as laminate. Align the front seams with the actual METOD modules and keep the existing parapet visible. Let the Toni oak-veneer oval and six light-grey Eamy chairs form a softer social counterpoint without adding an island or open display shelves. Use one broad, light-looking pendant at the existing dining point; the white space between furniture remains part of the composition.

Products (verified records): P09: Westwing Toni oval dining table, light oak veneer/MDF, 200 cm version, DEQ19WES60483-150724; 200 × 90 × 75 cm; recorded price 320,000 HUF (not the price of the 160 cm version), 2026-10-24; https://www.westwing.hu/toni-ovalis-alaku-fa-etkezoasztal-200-x-90-cm-hu-19wes60483.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-EAMY-LG: Kave Home Eamy chair, light-grey chenille, natural ash veneer and black metal; outer dimensions NOT RECORDED in the source; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-light-grey-chenille-and-ash-wood-veneer-with-a-natural-finish-and-black-metal; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-SOMAR76: Kave Home Somar pendant, synthetic fibres and steel rods; Ø76 cm; recorded price 579 EUR, 2026-10-24; https://kavehome.com/hu/en/p/somar-ceiling-lamp-made-with-synthetic-fibres-and-steel-rods-o76cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-31: IKEA EKBACKEN light-grey concrete-effect laminate worktop, 40616275; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-vilagosszuerke-beton-hatasu-laminalt-40616275/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: KI-K: straight laminate fronts on plan-sized METOD carcasses; graphite lower sample and white upper sample, matching ABS edges, no painted fronts. Worktop AG-31, cut from its documented 246 × 2.8 cm stock length/thickness with joints and actual depth resolved in the kitchen drawing; service doors and FL01 remain accessible. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-SOMAR76 at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: tea-house scenery, black kitchen walls, new island, floating stone countertop. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S01_KyotoInk_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S01 — Kyoto Ink · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Contemporary Japanese luxury through low graphite horizons, taupe woven upholstery, translucent natural textile and precisely proportioned white voids; each room interprets layering rather than repeating a beige palette.

Room composition: Build the bedroom around a pale stone-coloured woven headboard composed of two broad overlapping planes, one only 3 cm forward of the other. Keep the NORDLI bed low and white, with a single muted olive folded throw and no repeated graphite feature wall. Two narrow grounded bedside blocks frame the bed without blocking drawers or sockets. The wardrobe niche stays quiet and flush-fronted; depth, seams and textile grain must carry the room in neutral daylight.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: KI-M: W260 × H85 × D8 cm overall upholstered headboard, two removable linen-faced padded plywood panels, concealed wall cleats and socket cut-outs; max 3 cm plane offset within the stated depth. Two simple bedside boxes W30 × H42 × D30 cm in graphite laminate; no cantilever illusion. PAX fronts in white laminate in the existing niche, exact carcass count per measured niche. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,300 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: a dark box bedroom, shoji wardrobe doors, ceiling coves, lantern collections. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S01_KyotoInk_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S01 — Kyoto Ink · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Contemporary Japanese luxury through low graphite horizons, taupe woven upholstery, translucent natural textile and precisely proportioned white voids; each room interprets layering rather than repeating a beige palette.

Room composition: Use one upright safety-backed mirror with a very thin black frame over the existing basin, balanced by a single low graphite storage box in the verified dry free zone. Leave generous visible warm-grey tile around the mirror; do not turn the wall into a Japanese screen. Fold porcelain-white towels into one calm horizontal stack and add one small clay vessel. The signature is the precise frame-to-tile relationship under neutral artificial light, with no luminous mirror perimeter.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: KI-B: mirror W55 × H90 cm, 10 mm black metal frame, safety backing and mechanical tile-wall fixings. One floor-standing storage box W30 × H60 × D25 cm, moisture-resistant compact laminate, sealed joints and adjustable feet, removable shelf; location subject to door/shower clearance. No wall covering. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: bamboo wallpaper, stone basin replacement, a daylight shaft, a second storage unit. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S01_KyotoInk_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S02 — BiBo Nocturne · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): An intimate sculptural residence contrasting a navy conversation mass with softly irregular real reflections, transparent glass and restrained pale fabric; plum in the bedroom and graphite in the bathroom reinterpret the same soft contour.

Room composition: Use the exact navy JÄTTEBO U, open towards the west TV, as a compact conversation basin with its central bay left clear rather than filled by an oversized coffee table. Integrate one softly irregular mirror beside a matte-blue floor-supported cabinet so reflection and opaque colour read as one composition. The clear Anouk dining rectangle and six beige Ciselia chairs must remain lighter than the U, with no extra lounge chair. Carry a small navy textile echo onto the removable terrace bench; reflect only real architecture and the actual view.

Products (verified records): P04: IKEA JÄTTEBO 3.5-seat modular U with two chaises and arms, Samsala dark blue, 496.076.48; 285 × 160 × 71 cm; recorded price 928,000 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/jaettebo-3-5-szemelyes-elemes-kanape-heverok-karfak-samsala-soetetkek-s49607648/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

P08: Westwing Anouk dining table, transparent clear glass, 23WES68910; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes68910.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-CISELIA-BK: Kave Home Ciselia chair, beige chenille and black steel legs; outer dimensions NOT RECORDED in the source; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-steel-legs-with-black-finish-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-MARELY-W: Kave Home Marely white wool rug; 200×300 cm; recorded price 499 EUR, 2026-10-24; https://kavehome.com/hu/en/p/marely-white-wool-rug-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-BRISIA: Kave Home Brisia pendant, brushed brass and four frosted glass balls; gömb Ø15 cm; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/brisia-metal-ceiling-lamp-with-brushed-brass-finish-and-4-frosted-glass-balls-o15cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: BN-L: W240 × H50 × D40 cm white carcass media unit, matte navy laminate fronts (sample/code pending), radiused applied end only, 2 mm ABS edges, plinth-supported. BN-R: W80 × H190 cm irregular mirror, safety-backed, separately mechanically fixed and floor supported where engineered; cable access to D16/D17 kept. BN-O: W150 × H42 × D60 cm aluminium/outdoor-HPL terrace bench with navy outdoor cushion. Narrow removable arm tray W25 × D35 cm is an accessory, not a new central table. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,900 M HUF, 03b cap 0,928 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-BRISIA only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: a giant marble coffee table inside the U, a blue Gala invented from a beige product, restaurant artworks, floral ceiling installations, gold overload. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S02 — BiBo Nocturne · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): An intimate sculptural residence contrasting a navy conversation mass with softly irregular real reflections, transparent glass and restrained pale fabric; plum in the bedroom and graphite in the bathroom reinterpret the same soft contour.

Room composition: Give the kitchen a matte navy lower band and quiet white upper fronts, with an honestly rendered grey-beige stone-effect laminate worktop. Centre the visual dining scene on the clear Anouk table and six identical beige Ciselia chairs, keeping their black legs legible through the glass. The four frosted Brisia globes form one restrained suspended object at ML04, not multiple new ceiling points. Avoid turning the entire kitchen blue; the white parapet and clear work surfaces provide the necessary pause.

Products (verified records): P08: Westwing Anouk dining table, transparent clear glass, 23WES68910; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes68910.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-CISELIA-BK: Kave Home Ciselia chair, beige chenille and black steel legs; outer dimensions NOT RECORDED in the source; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-steel-legs-with-black-finish-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-BRISIA: Kave Home Brisia pendant, brushed brass and four frosted glass balls; gömb Ø15 cm; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/brisia-metal-ceiling-lamp-with-brushed-brass-finish-and-4-frosted-glass-balls-o15cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-33: IKEA EKBACKEN grey-beige stone-effect laminate worktop, 20604320; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-szuerke-bezs-ko-hat-laminalt-20604320/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: BN-K: plan-sized METOD carcasses with matte navy lower laminate fronts, white upper fronts and AG-33 laminate worktop; straight joinery with moisture-sealed cut-outs, matching edge bands and removable appliance/service panels. No mirrored splashback and no added island. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-BRISIA at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: mirror-clad kitchen walls, blue marble, relocating the pendant to table centre, a restaurant bar. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S02_BiBoNocturne_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S02 — BiBo Nocturne · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): An intimate sculptural residence contrasting a navy conversation mass with softly irregular real reflections, transparent glass and restrained pale fabric; plum in the bedroom and graphite in the bathroom reinterpret the same soft contour.

Room composition: Create a quiet plum textile sanctuary using two broad headboard panels with softened upper corners, separated by a narrow white slit. Keep the white NORDLI platform honest and low; use pale bedding and only one small navy piping detail to connect back to the salon. Small grounded bedside blocks should be subordinate to the headboard and leave sockets, drawer travel and the terrace route free. The luxury comes from the rounded silhouette and fabric pile, not darkened walls or a mirror above the bed.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: BN-M: W260 × H100 × D6 cm padded plywood headboard, two plum textile panels, 8 cm upper corner radii, removable covers and wall cleats with D20–23 cut-outs. Bedside blocks W30 × H45 × D30 cm, matte graphite laminate, floor standing. PAX light laminate fronts within the existing niche. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,350 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: a navy copy of the living room, upholstered whole walls, floating bedside tables without brackets, mirrored ceiling. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S02_BiBoNocturne_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S02 — BiBo Nocturne · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): An intimate sculptural residence contrasting a navy conversation mass with softly irregular real reflections, transparent glass and restrained pale fabric; plum in the bedroom and graphite in the bathroom reinterpret the same soft contour.

Room composition: Place a softly asymmetrical safety-backed mirror over the built basin, with a thin silver-coloured metal edge and generous exposed tile around it. Use graphite towels against a pale, narrow storage piece; keep navy out of the major surfaces so this is a distinct bathroom within the same sculptural family. A single small real-metal tray supplies reflection at hand level. Use only the existing basin and ceiling light points with neutral artificial light, no backlit perimeter or invented daylight.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: BN-B: mirror W60 × H90 cm, shallow asymmetric outline with rounded corners, safety backing and mechanical wall fixing. One W30 × H65 × D25 cm moisture-resistant white compact-laminate storage unit with one graphite open shelf, floor supported, fully sealed edges; placement only in the verified dry free zone. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: a nightclub bathroom, blue retiling, full mirrored walls, gold sanitary fittings. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S02_BiBoNocturne_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S03 — Alelí Casa · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A cultivated Mediterranean-Italian home centred on a sculptural walnut dining circle, olive upholstery and genuine terracotta; raw linen and cocoa in the bedroom, clay and chalk-white in the bathroom.

Room composition: Let the dark walnut Nealy circle be the social focal point while the exact olive left-hand Melva L faces the south TV. Balance the circular table with a low wood-effect cabinet whose single curved end is deliberately quieter than the dining pedestal. Place one framed ceramic relief made from four broad clay forms on a restrained white wall area, with the remaining wall empty. Extend the convivial character onto a simple outdoor bench on the existing gres; do not alter the terrace levels or add a second dining set in this camera.

Products (verified records): P02: Westwing Melva, olive fine-woven upholstery, left-hand L, DEQ23WES08157-200447; 238 × 143 × 75 cm; recorded price 650,000 HUF product-page / 850,000 HUF search extract; unresolved discrepancy, inherited planning cap 850,000 HUF, 2026-10-24; https://www.westwing.hu/melva-sarokkanape-3-szemelyes-hu-23wes08157.html; status: SOURCE-VERIFIED PRODUCT, PRICE DISPUTED / CONDITIONAL K8.

KH-DT-NEALY-W150: Kave Home Nealy round dining table, dark walnut veneer; Ø150 cm; recorded price 1465 EUR, 2026-10-24; https://kavehome.com/hu/en/p/nealy-round-table-with-a-walnut-veneer-in-a-dark-finish-o-150-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-NIFELIA: Kave Home Nifelia beige wool jacquard rug; 200×300 cm; recorded price 439 EUR, 2026-10-24; https://kavehome.com/hu/en/p/nifelia-beige-wool-jacquard-rug-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-DRAVA: Kave Home Drava pendant, burgundy ceramic; outer dimensions NOT RECORDED in the source; recorded price 45.99 EUR, 2026-10-24; https://kavehome.com/hu/en/p/drava-ceiling-lamp-in-burgundy-ceramic; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: AC-L: cabinet W210 × H50 × D40 cm, white board carcass and H3710 walnut-effect laminate, one R20 cm end in formed MDF with compatible laminate skin, matching 2 mm edge; grounded, ending before the switch column. AC-R: W100 × H100 × D5 cm framed genuine fired-clay relief, four independently retained lightweight elements, wall anchoring engineered under K6. AC-O: W160 × H43 × D60 cm aluminium/outdoor-HPL bench with oatmeal outdoor cushion. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,750 M HUF, 03b cap 0,850 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-DRAVA only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D19 on the south wall, stopping the cabinet before the switch column.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: trattoria props, lemon patterns, faux brick, terracotta plaster, copying Alelí artworks. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S03_AleliCasa_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S03 — Alelí Casa · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A cultivated Mediterranean-Italian home centred on a sculptural walnut dining circle, olive upholstery and genuine terracotta; raw linen and cocoa in the bedroom, clay and chalk-white in the bathroom.

Room composition: Make the Nealy walnut pedestal and circular top the dominant dining sculpture, surrounded by six identical brown Eamy chairs. Hold the kitchen back with flat light upper fronts, walnut-effect lower fronts and one muted clay-coloured laminate insert; preserve the actual appliance layout and the low parapet. A single burgundy ceramic Drava pendant at ML04 adds tactile depth without copying a restaurant installation. The larger round table is conditional on a new chair-use check at the fixed P902_24A centre; never distort it to fit.

Products (verified records): KH-DT-NEALY-W150: Kave Home Nealy round dining table, dark walnut veneer; Ø150 cm; recorded price 1465 EUR, 2026-10-24; https://kavehome.com/hu/en/p/nealy-round-table-with-a-walnut-veneer-in-a-dark-finish-o-150-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-DRAVA: Kave Home Drava pendant, burgundy ceramic; outer dimensions NOT RECORDED in the source; recorded price 45.99 EUR, 2026-10-24; https://kavehome.com/hu/en/p/drava-ceiling-lamp-in-burgundy-ceramic; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-33: IKEA EKBACKEN grey-beige stone-effect laminate worktop, 20604320; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-szuerke-bezs-ko-hat-laminalt-20604320/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: AC-K: straight METOD front package, H3710 walnut-effect lower panels, light neutral upper laminate, one clay-tone sample panel within an existing door width; AG-33 stone-effect laminate worktop with sealed edges. No rounded kitchen extension, no added island and no third bespoke cabinet sculpture. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-DRAVA at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: a rustic kitchen, an oversized ceramic chandelier, stone counter misrepresentation, deleting two chairs to make the plan fit. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S03_AleliCasa_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S03 — Alelí Casa · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A cultivated Mediterranean-Italian home centred on a sculptural walnut dining circle, olive upholstery and genuine terracotta; raw linen and cocoa in the bedroom, clay and chalk-white in the bathroom.

Room composition: Compose the bedroom as a quiet linen alcove made entirely from furniture: two broad padded panels turn gently forward only at their outer edges. Pair the low white NORDLI bed with cocoa bedding accents and pale curtains, avoiding an olive or terracotta copy of the salon. Small wood-effect bedside blocks sit low enough to preserve the visual sweep of the headboard. Keep the wardrobe niche calm, with all electrical points and bed drawers accessible.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: AC-M: W260 × H100 × D8 cm overall linen-clad headboard, padded plywood sections with softly turned outer 20 cm wings contained within the stated depth, removable textile and concealed wall cleats. Two W30 × H42 × D30 cm H3710 laminate bedside boxes, grounded; white/light laminate PAX fronts in the existing niche. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,350 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: an upholstered arch built into the wall, terracotta room paint, matching rustic furniture sets. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S03_AleliCasa_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S03 — Alelí Casa · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A cultivated Mediterranean-Italian home centred on a sculptural walnut dining circle, olive upholstery and genuine terracotta; raw linen and cocoa in the bedroom, clay and chalk-white in the bathroom.

Room composition: Echo the dining circle with one round safety-backed mirror over the existing basin, using a narrow dark bronze-toned metal rim rather than a rustic timber frame. Place one genuine clay soap dish and chalk-white towels with a fine clay-coloured border against the existing grey tile. A single narrow dark storage box in the verified dry zone grounds the composition. Keep the shower, black fittings and all tiled surfaces exactly as built; the bathroom should feel collected and tactile, not themed.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: AC-B: mirror Ø65 cm, safety-backed glass and 12 mm bronze-tone metal rim, mechanical tile-wall fixing; one W30 × H60 × D25 cm moisture-resistant compact-laminate dark storage box, sealed joints, floor supported. Clay soap dish is a handmade accessory with no claimed brand or verified price. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: terracotta retiling, new niches, antique taps, a pottery collection covering every surface. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S03_AleliCasa_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S04 — LA Horizon · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Cinematic horizontal luxury through low taupe lounge seating, offset walnut-effect planes, tobacco glass and the actual Buda panorama; pearl-grey bedroom textiles and smoky silver bathroom details keep the family coherent without repeating colours.

Room composition: Keep the exact right-hand Lennon L low against the real glazing rhythm, facing the south TV. Build the media composition from two offset, genuinely floor-supported walnut-effect volumes with different heights; let their overhang-like reading come from alignment, not unsupported slabs. Use the brown Anouk table and six brown Eamy chairs to create depth through transparency, with visible existing flooring around the Malenka rug. A separate low terrace bench extends the visual horizon across the real threshold without pretending the indoor and outdoor floors are level.

Products (verified records): P14: Westwing Lennon right-hand L, taupe woven polyester upholstery, DEQ21WES12329-168260; 238 × 180 × 68 cm; recorded price 800,000 HUF, 2026-10-24; https://www.westwing.hu/lennon-modularis-sarokkanape-hu-21wes12329.html?simple=DEQ21WES12329-168260; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

P07: Westwing Anouk dining table, transparent brown glass, DEQ23WES69048-203420; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes69048.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-MALENKA: Kave Home Malenka brown wool rug; 200×300 cm; recorded price 499 EUR, 2026-10-24; https://kavehome.com/hu/en/p/malenka-brown-wool-carpet-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-ARDALI50: Kave Home Ardali pendant, smoked glass and brushed steel; Ø50 cm; recorded price 319 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ardali-ceiling-lamp-in-smoked-glass-and-steel-with-brushed-finish-o50cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: LH-L: combined W240 cm media composition, lower module H30 × D45 cm and offset module H55 × D35 cm, white board carcasses, H3710 walnut-effect laminate, 2 mm ABS edges and solid recessed plinths; terminate before the D19 switch column, removable cable panels. LH-O: W180 × H38 × D65 cm terrace bench, aluminium frame, outdoor HPL seat and taupe outdoor cushion, freestanding on verified gres. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,800 M HUF, 03b cap 0,928 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-ARDALI50 only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D19 on the south wall, stopping the cabinet before the switch column.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: a fictional Los Angeles skyline, continuous LED edge outlines, giant stone slabs, removing the actual glazing mullions. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S04_LAHorizon_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S04 — LA Horizon · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Cinematic horizontal luxury through low taupe lounge seating, offset walnut-effect planes, tobacco glass and the actual Buda panorama; pearl-grey bedroom textiles and smoky silver bathroom details keep the family coherent without repeating colours.

Room composition: Use quiet light laminate kitchen fronts behind a dark walnut-effect laminate worktop, preserving its real joins and the appliance layout. Make the brown Anouk tabletop the principal horizontal layer, paired with six brown polyurethane Eamy chairs rendered honestly as PU, not leather. One Ardali smoked-glass pendant at ML04 introduces a darker disc above the table without closing the view. Keep the existing parapet and all negative space between kitchen, dining and lounge legible.

Products (verified records): P07: Westwing Anouk dining table, transparent brown glass, DEQ23WES69048-203420; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes69048.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-ARDALI50: Kave Home Ardali pendant, smoked glass and brushed steel; Ø50 cm; recorded price 319 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ardali-ceiling-lamp-in-smoked-glass-and-steel-with-brushed-finish-o50cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-32: IKEA EKBACKEN brown walnut-effect laminate worktop, 10442984; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-barna-dio-hat-laminalt-10442984/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: LH-K: straight METOD fronts in light neutral laminate, AG-32 walnut-effect laminate countertop (documented stock 246 × 2.8 cm), matching end panels, sealed sink/appliance cut-outs, service access. No stone waterfall or extra worktop extension. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-ARDALI50 at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: black marble kitchen, fake leather chairs, moving the parapet, a dropped ceiling over the dining area. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S04_LAHorizon_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S04 — LA Horizon · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Cinematic horizontal luxury through low taupe lounge seating, offset walnut-effect planes, tobacco glass and the actual Buda panorama; pearl-grey bedroom textiles and smoky silver bathroom details keep the family coherent without repeating colours.

Room composition: Create a pearl-grey bedroom with one broad low headboard plane and a narrower upholstered strip slightly offset over it. Keep the upper wall completely calm so the real glazing height provides the vertical counterweight. The white NORDLI platform and pale bedding should read as a floating-looking but fully supported horizon, with only one graphite textile edge. Use two small grounded bedside blocks and quiet niche fronts, preserving drawer travel and socket access.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: LH-M: W280 × H85 × D6 cm laminate back panel in a light neutral sample, with a W220 × H55 cm pearl-grey textile panel within the same depth; wall cleats and removable access sections at D20–23. Bedside boxes W30 × H38 × D30 cm, H3710 laminate on supported plinths; PAX light fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,350 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: a full-width brown wall, ceiling light strips, glass bedside clutter, a larger imaginary bed. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S04_LAHorizon_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S04 — LA Horizon · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Cinematic horizontal luxury through low taupe lounge seating, offset walnut-effect planes, tobacco glass and the actual Buda panorama; pearl-grey bedroom textiles and smoky silver bathroom details keep the family coherent without repeating colours.

Room composition: Translate the horizon into one landscape-format safety-backed mirror above the existing basin, with a restrained brushed-silver edge. Pair silver-grey towels with a narrow dark storage unit, leaving the shower edge and large areas of the original tile visible. Keep every fitting in its built position and align the mirror to the verified basin rather than to the provisional camera. The room is lit only by the existing basin and ceiling points, with no suggestion of daylight.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: LH-B: mirror W75 × H55 cm, 10 mm brushed-metal frame and mechanical wall fixings; one W30 × H65 × D25 cm sealed compact-laminate charcoal storage unit on feet. Mirror width is a design envelope subject to the actual basin/tile-wall clearances, not a measured fit. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: a new window, floor-level strip lighting, replacing the basin with a stone trough. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S04_LAHorizon_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S05 — Miami Streamline · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Enduring Art Deco through rounded stepped furniture profiles, controlled ribbed rhythms, dusty-rose corduroy and graphite discipline; champagne upholstery in the bedroom and muted turquoise bathroom textiles reinterpret the same geometry.

Room composition: Use the exact dusty-rose left-hand Melva L as the only large coloured upholstery mass, opposite a stepped low cabinet with one rounded end. Two separated ribbed panels of unequal width create a deliberate vertical rhythm, while most of the white wall stays untouched. Balance the curves with the clear Anouk rectangle, black chair legs and a quiet jacquard rug, without adding a second graphic carpet. Repeat only a restrained striped outdoor cushion on the low terrace bench.

Products (verified records): P03: Westwing Melva, dusty-rose corduroy, left-hand L, DEQ21WES45069-169001; 238 × 143 × 75 cm; recorded price 750,000 / 850,000 / 1,000,000 HUF conflicting observations; inherited planning cap 1,000,000 HUF, 2026-10-24; https://www.westwing.hu/melva-kordbarsony-sarokkanape-3-szemelyes-hu-21wes45069.html; status: SOURCE-VERIFIED PRODUCT, PRICE DISPUTED / CONDITIONAL K8.

P08: Westwing Anouk dining table, transparent clear glass, 23WES68910; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes68910.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-CISELIA-BK: Kave Home Ciselia chair, beige chenille and black steel legs; outer dimensions NOT RECORDED in the source; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-steel-legs-with-black-finish-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-NIFELIA: Kave Home Nifelia beige wool jacquard rug; 200×300 cm; recorded price 439 EUR, 2026-10-24; https://kavehome.com/hu/en/p/nifelia-beige-wool-jacquard-rug-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-NOVAE40: Kave Home Novae pendant, light-grey brushed metal and frosted glass; Ø40 cm; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/novae-ceiling-lamp-in-light-grey-brushed-metal-and-frosted-glass-o-40-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: MS-L: W220 × H55 × D40 cm grounded cabinet, white carcass, light laminate fronts, one formed MDF end with compatible laminate skin; two ribbed factory-finished MDF inserts W40/W65 × H160 × D2 cm, independently wall-fixed after K6 check, no plaster work. MS-O: W160 × H42 × D60 cm aluminium/HPL terrace bench, pale outdoor cushion with narrow graphite stripe. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,800 M HUF, 03b cap 1,000 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-NOVAE40 only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: neon, palm wallpaper, gold-and-pink confectionery, ribbing on every surface, new architectural arches. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S05_MiamiStreamline_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S05 — Miami Streamline · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Enduring Art Deco through rounded stepped furniture profiles, controlled ribbed rhythms, dusty-rose corduroy and graphite discipline; champagne upholstery in the bedroom and muted turquoise bathroom textiles reinterpret the same geometry.

Room composition: Keep most kitchen fronts flat and light, reserving the ribbed rhythm for shallow applied details on the two already exposed end panels. Introduce one muted turquoise laminate door within the actual module grid, not a coloured wall. Pair the clear Anouk table and six beige Ciselia chairs with one light-grey Novae metal-and-frosted-glass pendant at ML04. Do not increase cabinet depth or narrow the already conditional kitchen aisle with decorative cladding.

Products (verified records): P08: Westwing Anouk dining table, transparent clear glass, 23WES68910; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes68910.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-CISELIA-BK: Kave Home Ciselia chair, beige chenille and black steel legs; outer dimensions NOT RECORDED in the source; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-steel-legs-with-black-finish-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-NOVAE40: Kave Home Novae pendant, light-grey brushed metal and frosted glass; Ø40 cm; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/novae-ceiling-lamp-in-light-grey-brushed-metal-and-frosted-glass-o-40-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-33: IKEA EKBACKEN grey-beige stone-effect laminate worktop, 20604320; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-szuerke-bezs-ko-hat-laminalt-20604320/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: MS-K: METOD flat light laminate fronts, one turquoise sample front; ribbed inserts confined within the existing finished end-panel envelope, never added into the aisle. AG-33 grey-beige stone-effect laminate worktop, sealed cut-outs, matching ABS edges and accessible appliance fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-NOVAE40 at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: a turquoise kitchen shell, deep applied flutes stealing aisle width, bar stools, mirrored splashbacks. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S05_MiamiStreamline_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S05 — Miami Streamline · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Enduring Art Deco through rounded stepped furniture profiles, controlled ribbed rhythms, dusty-rose corduroy and graphite discipline; champagne upholstery in the bedroom and muted turquoise bathroom textiles reinterpret the same geometry.

Room composition: Make the bedroom a restrained champagne textile composition with one wide headboard whose upper corners curve softly downward. Use a single graphite piping line to define its silhouette, leaving the central fabric unpatterned. Keep the white NORDLI platform, plain pale bedding and unfluted wardrobe fronts quiet; a small muted turquoise cushion is enough connection to the wider palette. Bedside lighting must be functional at the existing sockets, not a new pair of wall sconces.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: MS-M: W250 × H100 × D6 cm upholstered plywood headboard, R20 cm upper corners, champagne fabric and graphite piping, removable panels and wall cleats with point access. Two W30 × H42 × D30 cm light laminate bedside blocks with 2 mm dark edge; PAX flat light fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,300 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: shell-shaped novelty headboards, pink velvet everywhere, gold trim on all edges, plaster arches. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S05_MiamiStreamline_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S05 — Miami Streamline · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Enduring Art Deco through rounded stepped furniture profiles, controlled ribbed rhythms, dusty-rose corduroy and graphite discipline; champagne upholstery in the bedroom and muted turquoise bathroom textiles reinterpret the same geometry.

Room composition: Use one flat safety-backed mirror with a restrained stepped upper outline, its thin black frame relating to the existing black fittings. Introduce muted turquoise only in two neatly folded towels; keep the single storage piece smooth and pale so the small room does not become a Deco set. Leave the original stone-effect tiles fully legible around the composition. Illuminate from the existing basin point with a simple opal diffuser and from the existing ceiling point, identically to the other styles.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: MS-B: W60 × H85 cm mirror with two 5 cm upper-corner setbacks, rounded safe edges and a 10 mm black metal frame, mechanical fixing. One W30 × H65 × D25 cm moisture-resistant light compact-laminate storage box, sealed joints and floor feet. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: new arches, brass tap replacement, pink tiles, neon strips around the mirror. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S05_MiamiStreamline_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S06 — Zenit Atelier · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Develop Zenit through deep chenille seating, smoked walnut-effect mass and concentrated furniture-contained light; broad lighter bedroom textile panels and a precise black bathroom frame translate the same disciplined depth.

Room composition: Place the exact Blok corner L in the audited west-TV layout, preserving its large depth and genuine module silhouette. Pair a low smoked-walnut-effect media volume with one offset tall unit containing a single shallow illuminated reveal; the reveal's physical depth must remain visible in neutral daylight even when the light is subdued. The round Argo glass table and six brown Eamy chairs provide a light counterweight, with no extra lounge chair. Use one simple graphite outdoor bench and leave the real roof garden untouched.

Products (verified records): KH-SOF-BLOK-CORNER: Kave Home Blok 3-seat corner L, beige chenille; exact handedness to be bound to the product photo before rendering; 290 × 230 × 69 cm (height from Claude audit §4); handedness unresolved; recorded price 2625 EUR, 2026-10-24; https://kavehome.com/hu/en/p/blok-beige-chenille-3-seater-corner-sofa-290-x-230cm230cm-x-290cm-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-DT-ARGO: Kave Home Argo round glass dining table, black steel legs; Ø119 cm; recorded price 379 EUR, 2026-10-24; https://kavehome.com/hu/en/p/argo-round-glass-table-with-steel-legs-with-black-finish-o-119-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-MALENKA: Kave Home Malenka brown wool rug; 200×300 cm; recorded price 499 EUR, 2026-10-24; https://kavehome.com/hu/en/p/malenka-brown-wool-carpet-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-ARDALI50: Kave Home Ardali pendant, smoked glass and brushed steel; Ø50 cm; recorded price 319 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ardali-ceiling-lamp-in-smoked-glass-and-steel-with-brushed-finish-o50cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: ZA-L: lower cabinet W240 × H45 × D40 cm plus separate W45 × H190 × D35 cm tower, white carcasses with H3710 laminate, 2 mm ABS edges, grounded and anti-tip fixed; one W12 × H120 × D8 cm open reveal integrated in the tower, aluminium LED profile and serviceable driver powered only from D16/D17. ZA-O: W160 × H42 × D60 cm aluminium/HPL terrace bench, graphite outdoor textile. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,900 M HUF, 03b cap 0,800 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-ARDALI50 only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08. The single furniture reveal is fed from D16/D17, with a serviceable driver and no glowing perimeter.  No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: continuous glowing outlines, ceiling coves, a fake concrete wall, shrinking the Blok to fit, a tall tower across an electrical point. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S06_ZenitAtelier_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S06 — Zenit Atelier · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Develop Zenit through deep chenille seating, smoked walnut-effect mass and concentrated furniture-contained light; broad lighter bedroom textile panels and a precise black bathroom frame translate the same disciplined depth.

Room composition: Compose the kitchen as a darker walnut-effect lower volume below quiet light fronts, with a light-grey concrete-effect laminate worktop. The single task-light line at FL01 reveals the real work surface and joins rather than tracing every cabinet edge. Let the Argo round glass tabletop expose the disciplined front rhythm behind six identical brown Eamy chairs. One Ardali pendant at ML04 concentrates the dining focus; no new island, ceiling track or extra decorative shelf.

Products (verified records): KH-DT-ARGO: Kave Home Argo round glass dining table, black steel legs; Ø119 cm; recorded price 379 EUR, 2026-10-24; https://kavehome.com/hu/en/p/argo-round-glass-table-with-steel-legs-with-black-finish-o-119-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-ARDALI50: Kave Home Ardali pendant, smoked glass and brushed steel; Ø50 cm; recorded price 319 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ardali-ceiling-lamp-in-smoked-glass-and-steel-with-brushed-finish-o50cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-31: IKEA EKBACKEN light-grey concrete-effect laminate worktop, 40616275; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-vilagosszuerke-beton-hatasu-laminalt-40616275/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: ZA-K: straight METOD fronts in H3710 laminate below and light neutral laminate above, AG-31 countertop, sealed cuts and matching edges. Task-light profile sits within the existing cabinet envelope with an accessible driver; cabinet/module sizes remain those of the approved kitchen plan. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-ARDALI50 at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: full-height dark kitchen walls, real concrete substituted for laminate, continuous ceiling lighting, false leather. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S06_ZenitAtelier_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S06 — Zenit Atelier · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Develop Zenit through deep chenille seating, smoked walnut-effect mass and concentrated furniture-contained light; broad lighter bedroom textile panels and a precise black bathroom frame translate the same disciplined depth.

Room composition: Make the master a broad textile triptych with deliberately unequal panel widths, using pale greige woven fabric rather than the salon's darker upholstery. A single dark side return and the shadows of compact socket-fed reading lights create depth without a glowing perimeter. Keep the white NORDLI bed visibly separate from the wall composition and the PAX storage confined to its niche. Preserve the large white upper wall and unobstructed terrace glazing.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: ZA-M: W270 × H110 × D6 cm overall padded plywood headboard, three panels W60/120/90 cm before small join adjustments, greige textile, removable cleated sections and socket cut-outs; no new electrical cavity. Two W30 × H42 × D30 cm H3710 grounded bedside boxes; light PAX fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,400 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: a grid of small hotel panels, a dark wall behind every bed, concealed inaccessible drivers. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S06_ZenitAtelier_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S06 — Zenit Atelier · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Develop Zenit through deep chenille seating, smoked walnut-effect mass and concentrated furniture-contained light; broad lighter bedroom textile panels and a precise black bathroom frame translate the same disciplined depth.

Room composition: Create one deep-framed black mirror object above the existing basin, paired with a simple opal light bar at the actual basin-light point. The frame's real shadow, not a fake recessed wall, provides the architectural depth. Use a pale narrow storage unit and smoky-grey towels so the bathroom does not become a dark timber copy of the lounge. Retain all existing black fittings and warm-grey tiles, illuminated only from FL04 and ML10.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: ZA-B: mirror W60 × H85 × D4 cm overall, safety-backed glass in a black metal frame with safe rounded edges, mechanical tile-wall fixing; opal luminaire separate, no wired mirror. One W30 × H60 × D25 cm light compact-laminate storage unit, sealed edges and grounded feet. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: new recessed niches, wood slats in the shower, a luminous floor, moving the basin light for symmetry. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S06_ZenitAtelier_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S07 — Lake Forest Couture · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Light couture luxury through rounded upholstered mass, genuine shallow relief, pale wood and small real-metal accents; pearl textile contours in the master and soft grey bathroom layers avoid a uniformly beige apartment.

Room composition: Let the exact left-hand Wolke L be the principal soft sculpture, facing the west TV without increasing its dimensions. Pair it with a pale cabinet ending in one restrained curve and a separate genuine shallow mineral relief, leaving a visible white gap between the objects. Use the Sheffield marble-and-metal table as the only small natural-stone accent, with its final product height verified before rendering. Keep the Toni dining oval secondary and carry the pale outdoor textile onto one simple terrace bench without recolouring the terrace.

Products (verified records): P15: Westwing Wolke left-hand L, light-beige textured woven upholstery, 25WES29958; 258 × 167 × 65 cm; recorded price 1,050,000 HUF, 2026-10-24; https://www.westwing.hu/modular-corner-sofa-wolke-3-seater-en-25wes29958.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

P09: Westwing Toni oval dining table, light oak veneer/MDF, 200 cm version, DEQ19WES60483-150724; 200 × 90 × 75 cm; recorded price 320,000 HUF (not the price of the 160 cm version), 2026-10-24; https://www.westwing.hu/toni-ovalis-alaku-fa-etkezoasztal-200-x-90-cm-hu-19wes60483.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-CISELIA-BG: Kave Home Ciselia chair, beige chenille and beige steel legs; outer dimensions NOT RECORDED in the source; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-beige-steel-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-MARELY-W: Kave Home Marely white wool rug; 200×300 cm; recorded price 499 EUR, 2026-10-24; https://kavehome.com/hu/en/p/marely-white-wool-rug-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CT-SHEFF: Kave Home Sheffield coffee table, genuine white marble and golden steel legs; Ø80 cm; recorded price 365 EUR, 2026-10-24; https://kavehome.com/hu/en/p/sheffield-coffee-table-in-white-marble-and-golden-steel-legs-o-80-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-BRISIA: Kave Home Brisia pendant, brushed brass and four frosted glass balls; gömb Ø15 cm; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/brisia-metal-ceiling-lamp-with-brushed-brass-finish-and-4-frosted-glass-balls-o15cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: LF-L: cabinet W220 × H50 × D40 cm, white carcass and pale oak-effect laminate sample, one formed MDF end with compatible laminate skin, 2 mm matching edge, recessed grounded plinth. LF-R: W100 × H130 × D4 cm lightweight mineral/gypsum relief on a rigid frame, broad shallow folds, mechanically fixed under K6, never represented as travertine. LF-O: W160 × H42 × D60 cm aluminium/HPL bench, pale outdoor cushion. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,850 M HUF, 03b cap 1,050 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-BRISIA only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: fake travertine, golden sunlight as a luxury substitute, smoothing away the existing floor grain, enlarging the sofa. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S07_LakeForestCouture_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S07 — Lake Forest Couture · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Light couture luxury through rounded upholstered mass, genuine shallow relief, pale wood and small real-metal accents; pearl textile contours in the master and soft grey bathroom layers avoid a uniformly beige apartment.

Room composition: Compose a pale matte kitchen with one vertical oak-effect laminate front field, leaving all other fronts calm and flat. Render the grey-beige stone-effect laminate worktop honestly, with visible edge thickness rather than a marble slab illusion. The Toni oak-veneer oval and six beige-leg Ciselia chairs create a quiet rounded group beneath a single Brisia frosted-glass pendant at ML04. Keep the existing parapet and white upper wall clear; do not repeat the living-room relief in the kitchen.

Products (verified records): P09: Westwing Toni oval dining table, light oak veneer/MDF, 200 cm version, DEQ19WES60483-150724; 200 × 90 × 75 cm; recorded price 320,000 HUF (not the price of the 160 cm version), 2026-10-24; https://www.westwing.hu/toni-ovalis-alaku-fa-etkezoasztal-200-x-90-cm-hu-19wes60483.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-CISELIA-BG: Kave Home Ciselia chair, beige chenille and beige steel legs; outer dimensions NOT RECORDED in the source; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ciselia-chair-in-beige-chenille-and-beige-steel-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-BRISIA: Kave Home Brisia pendant, brushed brass and four frosted glass balls; gömb Ø15 cm; recorded price 199 EUR, 2026-10-24; https://kavehome.com/hu/en/p/brisia-metal-ceiling-lamp-with-brushed-brass-finish-and-4-frosted-glass-balls-o15cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-33: IKEA EKBACKEN grey-beige stone-effect laminate worktop, 20604320; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-szuerke-bezs-ko-hat-laminalt-20604320/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: LF-K: METOD carcasses with light laminate fronts, one pale oak-effect sample field within the actual door grid; AG-33 worktop, sealed joins and matching edges. Straight end panels only, no stone waterfall, no curved island added to the plan. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-BRISIA at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: gold wire chairs substituted for the specified product, faux marble slab islands, a uniformly beige colour grade. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S07_LakeForestCouture_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S07 — Lake Forest Couture · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Light couture luxury through rounded upholstered mass, genuine shallow relief, pale wood and small real-metal accents; pearl textile contours in the master and soft grey bathroom layers avoid a uniformly beige apartment.

Room composition: Create a pearl-coloured master with two broad softly convex textile headboard fields separated by a quiet recessed seam. Keep bedding in pale grey and chalk-white rather than repeating cream on every surface, and retain the white NORDLI platform as the functional base. Small pale bedside blocks and plain niche fronts should support, not compete with, the headboard sculpture. Show the real fabric curvature and shadow in neutral daylight without artificial halo lighting.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: LF-M: W260 × H95 × D8 cm overall padded plywood headboard, two removable broad panels with 3–5 cm convex padding contained in the stated depth, pearl upholstery, wall cleats and D20–23 access. Two W30 × H42 × D30 cm pale oak-effect laminate bedside blocks; PAX light flat fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,300 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: tufted palace upholstery, a complete cream filter, mirrored wardrobe wings invented outside the niche. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S07_LakeForestCouture_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S07 — Lake Forest Couture · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Light couture luxury through rounded upholstered mass, genuine shallow relief, pale wood and small real-metal accents; pearl textile contours in the master and soft grey bathroom layers avoid a uniformly beige apartment.

Room composition: Introduce one slender oval safety-backed mirror with a fine pale-metal frame, balancing the existing black fittings rather than replacing them. Use pearl-grey towels and a single light storage piece with gently softened corners; keep the original tile visible and unaltered. The oval reflection and the textile softness are the room's signature, not new wall treatment. Use neutral artificial light from the existing points only.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: LF-B: oval mirror W55 × H90 cm, safety backing and mechanically fixed thin metal frame; one W30 × H65 × D25 cm moisture-resistant compact-laminate storage box, slightly eased external corners, sealed joints and floor feet. No timber lamella or stone veneer in the wet zone. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: new travertine walls, gold tap replacement, glowing oval halo, plants requiring fictional daylight. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S07_LakeForestCouture_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S08 — Milano Radical · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A collector's composition of orthogonal bodies, one muted-yellow plane, graphite and quiet grey-beige upholstery; a walnut dining circle, black-and-chalk bedroom blocks and an offset bathroom frame sustain the geometric language.

Room composition: Use the exact grey-beige JÄTTEBO U, open to the west TV, with the small central bay left clear. Opposite it, compose two grounded cabinet bodies of unequal height and a separately supported connecting plane, using muted yellow on only one broad face. The Naanim walnut dining circle and six light-grey Eamy chairs interrupt the orthogonal rhythm without adding another sculptural lounge chair. Keep the rug quiet enough to expose the cabinet geometry and repeat only one graphic outdoor cushion on the terrace bench.

Products (verified records): P05: IKEA JÄTTEBO 3.5-seat modular U with two chaises and arms, Samsala grey-beige, 294.713.87; 285 × 160 × 71 cm; recorded price 928,000 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/jaettebo-3-5-szemelyes-elemes-kanape-heverok-karfak-samsala-szuerke-bezs-s29471387/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-DT-NAANIM-W120: Kave Home Naanim round dining table, walnut veneer; Ø120 cm; recorded price 539 EUR, 2026-10-24; https://kavehome.com/hu/en/p/naanim-round-table-in-walnut-veneer-o-120-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-LG: Kave Home Eamy chair, light-grey chenille, natural ash veneer and black metal; outer dimensions NOT RECORDED in the source; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-light-grey-chenille-and-ash-wood-veneer-with-a-natural-finish-and-black-metal; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-NIFELIA: Kave Home Nifelia beige wool jacquard rug; 200×300 cm; recorded price 439 EUR, 2026-10-24; https://kavehome.com/hu/en/p/nifelia-beige-wool-jacquard-rug-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-NOVAE40: Kave Home Novae pendant, light-grey brushed metal and frosted glass; Ø40 cm; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/novae-ceiling-lamp-in-light-grey-brushed-metal-and-frosted-glass-o-40-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: MR-L: combined W220 × H70 × D40 cm composition, two white carcass boxes with graphite/yellow laminate faces (samples/codes pending), supported connecting plane on visible slender legs, no seating load assumed, 2 mm ABS edges, removable D16/D17 cable access. MR-O: W150 × H42 × D60 cm aluminium/HPL outdoor bench, pale cushion with one graphite rectangular inset. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,750 M HUF, 03b cap 0,928 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-NOVAE40 only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: Memphis props, copied design icons, blue sofa substitution, an unsupported bridge, a crowded central bay. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S08_MilanoRadical_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S08 — Milano Radical · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A collector's composition of orthogonal bodies, one muted-yellow plane, graphite and quiet grey-beige upholstery; a walnut dining circle, black-and-chalk bedroom blocks and an offset bathroom frame sustain the geometric language.

Room composition: Set one large muted-yellow laminate door within a disciplined white METOD front grid, leaving the rest of the kitchen free of colour blocks. Use a light-grey concrete-effect laminate worktop and keep all appliances on their planned services. The Naanim walnut circle with six light-grey Eamy chairs and one Novae pendant creates a calm round counterpoint to the rectangular fronts. Show all six seats honestly and keep the table at the prescribed shifted centre pending the chair-use check.

Products (verified records): KH-DT-NAANIM-W120: Kave Home Naanim round dining table, walnut veneer; Ø120 cm; recorded price 539 EUR, 2026-10-24; https://kavehome.com/hu/en/p/naanim-round-table-in-walnut-veneer-o-120-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-LG: Kave Home Eamy chair, light-grey chenille, natural ash veneer and black metal; outer dimensions NOT RECORDED in the source; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-light-grey-chenille-and-ash-wood-veneer-with-a-natural-finish-and-black-metal; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-NOVAE40: Kave Home Novae pendant, light-grey brushed metal and frosted glass; Ø40 cm; recorded price 179 EUR, 2026-10-24; https://kavehome.com/hu/en/p/novae-ceiling-lamp-in-light-grey-brushed-metal-and-frosted-glass-o-40-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-31: IKEA EKBACKEN light-grey concrete-effect laminate worktop, 40616275; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-vilagosszuerke-beton-hatasu-laminalt-40616275/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: MR-K: METOD straight white laminate fronts with one yellow sample panel occupying an actual module, AG-31 laminate worktop, matching ABS edges, no extra-depth face panels. Service and appliance doors fully operable. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-NOVAE40 at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: random coloured cabinet doors, yellow walls, a terrazzo island, moving appliances for symmetry. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S08_MilanoRadical_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S08 — Milano Radical · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A collector's composition of orthogonal bodies, one muted-yellow plane, graphite and quiet grey-beige upholstery; a walnut dining circle, black-and-chalk bedroom blocks and an offset bathroom frame sustain the geometric language.

Room composition: Translate the collector's geometry into two broad chalk-white upholstered headboard fields with one graphite frame plane extending beyond them on only one side. Use yellow only in a small removable textile detail, never as a bedroom wall. Keep the NORDLI base white and the wardrobe fronts plain; two compact bedside blocks at different heights provide the secondary rhythm. Preserve all socket access and drawer movement so the composition remains a usable room.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: MR-M: W260 × H90 × D6 cm overall laminate-frame and padded-panel headboard, graphite sample frame with one 15 cm side extension within overall width, removable chalk textile inserts and wall cleats; bedside blocks W30 × D30 cm, H38 and H48 cm, grounded. PAX plain light fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,300 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: a giant yellow headboard, many coloured cushions, fake Memphis antiques, blocking the electrical sockets. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S08_MilanoRadical_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S08 — Milano Radical · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A collector's composition of orthogonal bodies, one muted-yellow plane, graphite and quiet grey-beige upholstery; a walnut dining circle, black-and-chalk bedroom blocks and an offset bathroom frame sustain the geometric language.

Room composition: Use one rectangular safety-backed mirror with an intentionally wider black frame edge on one side, creating an offset object without moving the basin. Balance it with one narrow graphite storage unit and chalk-white towels edged by a fine muted-yellow band. Keep every built line and sanitary fitting unchanged; the geometry comes from the added objects only. A simple opal basin light and the existing ceiling point provide neutral artificial illumination.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: MR-B: mirror overall W60 × H80 cm, frame 10 mm on three sides and 40 mm on one side, safety backing and mechanical fixings; one W30 × H60 × D25 cm sealed compact-laminate graphite storage box on feet, dry free-zone placement. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: yellow retiling, a new niche, multiple cube shelves, fake daylight. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S08_MilanoRadical_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S09 — Paris Collector · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A personal collector's home built around an original plum-and-chalk graphic composition, an olive L sofa, a contrasting sculptural chair and brown glass; smoky-plum bedroom textiles and ivory-black bathroom framing carry the curated character.

Room composition: Pair the exact olive left-hand Melva L with the documented Corvena olive armchair as a different silhouette, retaining its recorded 98 cm width and verifying the remaining dimensions before use. Make original artwork PC-A01 the focal point: an ivory field with one large plum rectangle, a narrow charcoal vertical and a small chalk circle, composed with generous empty margins rather than copying an artist. Keep the brown Anouk table, six brown Eamy chairs and dark cabinet subordinate; one existing-point floor lamp unifies the group. Do not shrink the chair into the former 80 cm target or block circulation to obtain the composition.

Products (verified records): P02: Westwing Melva, olive fine-woven upholstery, left-hand L, DEQ23WES08157-200447; 238 × 143 × 75 cm; recorded price 650,000 HUF product-page / 850,000 HUF search extract; unresolved discrepancy, inherited planning cap 850,000 HUF, 2026-10-24; https://www.westwing.hu/melva-sarokkanape-3-szemelyes-hu-23wes08157.html; status: SOURCE-VERIFIED PRODUCT, PRICE DISPUTED / CONDITIONAL K8.

P07: Westwing Anouk dining table, transparent brown glass, DEQ23WES69048-203420; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes69048.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-MALENKA: Kave Home Malenka brown wool rug; 200×300 cm; recorded price 499 EUR, 2026-10-24; https://kavehome.com/hu/en/p/malenka-brown-wool-carpet-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-AC-CORVENA-OL: Kave Home Corvena armchair, olive-green chenille; 98 cm; recorded price 509 EUR, 2026-10-24; https://kavehome.com/hu/en/p/corvena-armchair-in-olive-green-chenille-fsc-100-98-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-FL-MADALI-BK: Kave Home Madali floor lamp, glossy black steel and black marble base; outer dimensions NOT RECORDED in the source; recorded price 219 EUR, 2026-10-24; https://kavehome.com/hu/en/p/madali-floor-lamp-in-steel-with-glossy-black-finish-and-black-marble; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-ARDALI50: Kave Home Ardali pendant, smoked glass and brushed steel; Ø50 cm; recorded price 319 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ardali-ceiling-lamp-in-smoked-glass-and-steel-with-brushed-finish-o50cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: PC-L: cabinet W220 × H60 × D40 cm, white carcass and H3710 dark wood-effect laminate, one open book bay, supported plinth and D16/D17 cable access. PC-A01: original design specification for W140 × H180 cm pigment print on matte cotton paper in a thin black aluminium frame, rigid backing and safety glazing if required; no existing artwork or licence claimed, production quote required. PC-O: W150 × H43 × D60 cm aluminium/HPL terrace bench with muted plum outdoor cushion. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,800 M HUF, 03b cap 0,850 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-ARDALI50 only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D16/D17 at the west factory block, antenna G08.  Madali floor lamp at A902-D18 only, no cable crossing a route; final lamp envelope must be verified. No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: fake antiques, brand posters, random gallery walls, copying a known artwork, reducing Corvena to an invented compact chair. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S09_ParisCollector_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S09 — Paris Collector · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A personal collector's home built around an original plum-and-chalk graphic composition, an olive L sofa, a contrasting sculptural chair and brown glass; smoky-plum bedroom textiles and ivory-black bathroom framing carry the curated character.

Room composition: Keep the kitchen an orderly light matte working volume with dark pulls and one narrow walnut-effect end panel. Carry the collector's character through the brown Anouk table, six brown Eamy chairs and one smoked-glass Ardali pendant rather than through objects on the worktop. Preserve the planned appliances and the existing parapet, with clear space around the dining group. The kitchen should feel cultivated and practical, not like an extension of the gallery wall.

Products (verified records): P07: Westwing Anouk dining table, transparent brown glass, DEQ23WES69048-203420; 180 × 90 × 75 cm; 84 kg; recorded price 320,000 HUF, 2026-10-24; https://www.westwing.hu/anouk-uveg-etkezoasztal-180-x-90-cm-hu-23wes69048.html; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-ARDALI50: Kave Home Ardali pendant, smoked glass and brushed steel; Ø50 cm; recorded price 319 EUR, 2026-10-24; https://kavehome.com/hu/en/p/ardali-ceiling-lamp-in-smoked-glass-and-steel-with-brushed-finish-o50cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-32: IKEA EKBACKEN brown walnut-effect laminate worktop, 10442984; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-barna-dio-hat-laminalt-10442984/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: PC-K: straight light laminate fronts on METOD, dark metal pulls, H3710 end panel within the existing envelope, AG-32 walnut-effect laminate worktop with sealed edges and accessible services. No extra open shelving or art niche. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-ARDALI50 at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: books beside the hob, antique brass kitchen fittings, a gallery wall above the sink, a new island. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S09_ParisCollector_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S09 — Paris Collector · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A personal collector's home built around an original plum-and-chalk graphic composition, an olive L sofa, a contrasting sculptural chair and brown glass; smoky-plum bedroom textiles and ivory-black bathroom framing carry the curated character.

Room composition: Use two broad smoky-plum textile headboard fields with a slight height difference, softer in colour than the living-room artwork. Pair the white NORDLI bed with two deliberately different compact bedside silhouettes: one closed grounded box and one open supported frame. Keep pale bedding and plain wardrobe fronts quiet, with only one book as a personal detail. Do not repeat the large artwork or turn the bedroom into a gallery; the tension between unequal objects is its own signature.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: PC-M: W260 × H105/90 × D6 cm overall two-field padded plywood headboard, removable plum textile panels and wall cleats with D20–23 access. Bedside units W30 × H43 × D30 cm, one H3710 laminate box and one black metal open frame with laminate top, grounded; PAX light fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,350 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: matching hotel bedside sets, antique reproductions, an additional large painting, full plum walls. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S09_ParisCollector_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S09 — Paris Collector · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): A personal collector's home built around an original plum-and-chalk graphic composition, an olive L sofa, a contrasting sculptural chair and brown glass; smoky-plum bedroom textiles and ivory-black bathroom framing carry the curated character.

Room composition: Treat the basin mirror like a carefully framed object: a broad ivory moisture-resistant surround with a very fine black outer edge, never a paper mount in a wet room. Pair it with one narrow dark storage piece and chalk-white towels with a tiny plum loop detail. Leave the original tile visible around it and add no separate picture. The signature is the frame proportion under neutral artificial light, not heritage moulding or new wall finish.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: PC-B: mirror overall W65 × H90 cm, safety-backed glass, 5 cm ivory compact-laminate surround and thin black metal outer edge, sealed joints and mechanical tile-wall fixing. One W30 × H60 × D25 cm dark compact-laminate storage box on feet, dry free-zone placement. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: paper artwork in the shower zone, ornate gilded mirrors, faux heritage mouldings, new tile patterns. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S09_ParisCollector_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

---

### S10 — Desert Modern 70 · nappali–terasz (Cam_02)

Fixed blocks: source template v3.1 §1 + §2 Cam_02, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Desert-modern warmth through stepped grounded furniture, modular beige seating, ochre textile and real clay, visually related to the existing layered roof garden; cocoa-linen bedroom tones and sandy-grey bathroom objects keep the language distinct.

Room composition: Use the documented beige Neom chaise L facing the south TV, preserving its 263 cm recorded width and requiring the full outer dimensions and chosen handedness before rendering. Compose the media area from two adjacent grounded volumes of unequal height beneath one large geometric relief, with deliberate white space above. Relate their stepped rhythm to the existing terrace levels and a separate low outdoor bench, without adding a platform or altering the roof garden. The Naanim walnut circle and six brown Eamy chairs provide a compact solid counterweight rather than a transparent LA-style horizon.

Products (verified records): KH-SOF-NEOM-CH: Kave Home Neom 3-seat modular sofa with reversible right/left chaise, beige; selected L handedness to be fixed before rendering; width 263 cm; full outer depth/height NOT RECORDED, do not infer from seat or another Neom; recorded price 1570 EUR, 2026-10-24; https://kavehome.com/hu/en/p/neom-3-seater-modular-sofa-rightleft-chaise-longue-in-beige-263-cm-fsc-mix-credit; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-DT-NAANIM-W120: Kave Home Naanim round dining table, walnut veneer; Ø120 cm; recorded price 539 EUR, 2026-10-24; https://kavehome.com/hu/en/p/naanim-round-table-in-walnut-veneer-o-120-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-RUG-MALENKA: Kave Home Malenka brown wool rug; 200×300 cm; recorded price 499 EUR, 2026-10-24; https://kavehome.com/hu/en/p/malenka-brown-wool-carpet-200-x-300-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-DRAVA: Kave Home Drava pendant, burgundy ceramic; outer dimensions NOT RECORDED in the source; recorded price 45.99 EUR, 2026-10-24; https://kavehome.com/hu/en/p/drava-ceiling-lamp-in-burgundy-ceramic; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: DM-L: combined W220 cm stepped cabinet, module depths D35/D45 cm and heights H35/H60 cm, white carcasses, H3710 wood-effect laminate and matching ABS edges, grounded and clear of D19 switch column. DM-R: W120 × H120 × D5 cm framed lightweight plywood/textile relief with three offset rectangular planes, no stone imitation. DM-O: W160 × H40 × D65 cm aluminium/outdoor-HPL bench with ochre-edged outdoor cushion, on existing gres only. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 03a cap 0,750 M HUF, 03b cap 0,850 M HUF, 03c/e/f, 10 lighting, 11/12 art where specified, 13c outdoor furniture. PREMIUM differences remain conditional; no new total calculated.

Light: Series A: neutral overcast daylight and identical comparison exposure/white balance. Dining pendant KH-PL-DRAVA only at A902-ML04; retain A902-ML05 as the existing living point, with no additional decorative fixture specified. TV power A902-D19 on the south wall, stopping the cabinet before the switch column.   No new wired terrace lights; retain FL05/06/07. No ceiling drilling, no warm grading.

Avoid: an orange colour grade, cactus scenery, a new stone platform, shrinking the Neom depth, a U sofa in L2. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_02 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png; image 2 = A902 site material-photo set ME-BAL-080, 045, 046, 042, 044, 053 plus the actual panorama A902_terasz_panorama_v0b_videobol.jpg; image 3 = optional original Zenit/Lake Forest living-room reference, mood/quality only, never geometry; image 4 = exact selected sofa, table, chair, rug and lamp product photos. Follow the source template §0/a order, including its unresolved input conditions.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S10_DesertModern70_1_nappali-terasz_Cam_02_A.png (+ same basename .prompt.txt)

---

### S10 — Desert Modern 70 · konyha–étkező (Cam_03)

Fixed blocks: source template v3.1 §1 + §2 Cam_03, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Desert-modern warmth through stepped grounded furniture, modular beige seating, ochre textile and real clay, visually related to the existing layered roof garden; cocoa-linen bedroom tones and sandy-grey bathroom objects keep the language distinct.

Room composition: Compose walnut-effect lower kitchen fronts beneath quiet sand-tone laminate uppers, keeping the actual walls white. Use a grey-beige stone-effect laminate worktop with a clearly manufactured edge, not a thick natural-stone slab. The Naanim walnut circle and six brown Eamy chairs create a compact social cluster, distinct from LA's long glass table. A single burgundy ceramic Drava pendant at ML04 supplies the clay note without adding multiple ceiling drops.

Products (verified records): KH-DT-NAANIM-W120: Kave Home Naanim round dining table, walnut veneer; Ø120 cm; recorded price 539 EUR, 2026-10-24; https://kavehome.com/hu/en/p/naanim-round-table-in-walnut-veneer-o-120-cm; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-CH-EAMY-BR: Kave Home Eamy chair, brown polyurethane, walnut-finish ash veneer and black metal; not leather; outer dimensions NOT RECORDED in the source; recorded price 179 EUR; source discount note: igen: 161.1 €, 2026-10-24; https://kavehome.com/hu/en/p/eamy-chair-in-brown-polyurethane-ash-veneer-with-walnut-and-black-metal-finish; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

KH-PL-DRAVA: Kave Home Drava pendant, burgundy ceramic; outer dimensions NOT RECORDED in the source; recorded price 45.99 EUR, 2026-10-24; https://kavehome.com/hu/en/p/drava-ceiling-lamp-in-burgundy-ceramic; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

AG-33: IKEA EKBACKEN grey-beige stone-effect laminate worktop, 20604320; 246x2.8 cm; recorded price 24990 HUF; source discount note: igen (új alacsonyabb ár), 2026-10-24; https://www.ikea.com/hu/hu/p/ekbacken-munkalap-szuerke-bezs-ko-hat-laminalt-20604320/; status: SOURCE PRICE RECORDED 2026-10-24; complete dimensions/material specification and HU delivered total may be unresolved; CONDITIONAL K8.

Dining quantity: exactly one table and six identical chairs, the same configuration in Cam_02 and Cam_03. Missing outer dimensions are a pre-image blocker; do not estimate or substitute.

Custom pieces: DM-K: METOD straight H3710 lower fronts, sand-tone upper laminate sample, AG-33 worktop with sealed joints and edge bands; actual module grid and appliance service access preserved. No stepped plinth entering the aisle and no decorative island. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 02a target 1.50 M HUF (source band 1.20–2.00), 02b 1.10, 02c 0.30, 03d 0.60 for table plus six chairs, 10 lighting. Chair-related PREMIUM/reallocation flags remain unresolved; no new total calculated.

Light: Series A: neutral overcast daylight. KH-PL-DRAVA at A902-ML04 only, no displaced ceiling anchor. Worktop task light from A902-FL01, ceiling light at A902-ML03; actual fitting/mounting verified before use, no new electrical points and no lighting added along every edge.

Avoid: sand-coloured walls, orange glazing, a rustic stone kitchen, false leather on the chairs. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_03 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_03_etkezo-konyha.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_2_etkezo_konyha.png; image 2 = A902 site photographs ME-BAL-056, 080 and 045; image 3 = optional original Zenit/Lake Forest kitchen-dining reference, mood only; image 4 = the specified front/worktop samples and the same table, six chairs and pendant product photos used for this style's living view. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S10_DesertModern70_2_etkezo-konyha_Cam_03_A.png (+ same basename .prompt.txt)

---

### S10 — Desert Modern 70 · master (Cam_04)

Fixed blocks: source template v3.1 §1 + §2 Cam_04, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Desert-modern warmth through stepped grounded furniture, modular beige seating, ochre textile and real clay, visually related to the existing layered roof garden; cocoa-linen bedroom tones and sandy-grey bathroom objects keep the language distinct.

Room composition: Translate the stepped furniture into a two-height textile headboard, one cocoa field and one raw-linen field, with the change of level occurring away from the bed centre. Keep the NORDLI platform white and grounded, using ochre only as a narrow throw border. Plain light wardrobe fronts and compact bedside blocks prevent the room from becoming a heavy seventies set. Preserve the glazing, sockets and storage access without adding a platform bed or any new architectural step.

Products (verified records): P10: IKEA NORDLI white storage bed for 180 × 200 cm mattress, 203.498.53; outer frame 180 × 202 × 30 cm; mattress and headboard separate; recorded price 189,900 HUF, 2026-10-24; https://www.ikea.com/hu/hu/p/nordli-agykeret-taroloval-feher-20349853/; status: SOURCE-VERIFIED on 2026-10-24, not freshly researched or an order quote.

IKEA PAX carcasses plus flat style fronts in the existing niche; exact module count and outer envelope to follow the measured niche, not an invented full wall. The selected headboard and bedside pieces are custom records below. No Kave Home bed alternative is rendered before its actual outer dimensions are verified.

Custom pieces: DM-M: W270 × H80/100 × D6 cm overall headboard, laminate-backed removable padded panels in cocoa and raw linen, wall cleats and D20–23 cut-outs; two W30 × H40 × D30 cm H3710 bedside boxes on feet, PAX plain light fronts. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited budget rows: 04a 0.55 M HUF, 04b cap 0,300 M HUF, 04c and 04d 0.45 each; electrical system in 10 without double counting. Fabrication quotation required.

Light: Series A: neutral overcast daylight, equal exposure. Compact plug-in reading luminaires only at A902-D20/21 and D22/23, ML06 ceiling point retained, niche light from D26 after on-site identification; fixture SKU, shade envelope and mount remain a pre-image gate. No new wall light points, ceiling coves or drilling into heating/cooling panels.

Avoid: a sunken bed pit, a new platform, orange velvet on every surface, a cactus mural. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = the verified v2b-1 Cam_04 empty geometry base at 04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_04_master.png plus 04_renderek/semleges_v2b/A902_semlegesv2b_3_master.png; image 2 = A902 ME-BAL-080 and room-confirmed ME-BAL-060, 069, 063 (their 05.1 assignment must be established, not assumed); image 3 = optional original Zenit/Lake Forest master reference, quality only; image 4 = NORDLI bed product photo, headboard material sample and final niche-front sample. Follow source template §0/a.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S10_DesertModern70_3_master_Cam_04_A.png (+ same basename .prompt.txt)

---

### S10 — Desert Modern 70 · fürdő 06.2 (Cam_10)

Fixed blocks: source template v3.1 §1 + §2 Cam_10, verbatim, before this block; source commit 46e3c5cbe2607479d7eba8037b1fbbc164365fe6. Do not generate until the KEP-004 gate is open.

Style DNA (common to the four rooms): Desert-modern warmth through stepped grounded furniture, modular beige seating, ochre textile and real clay, visually related to the existing layered roof garden; cocoa-linen bedroom tones and sandy-grey bathroom objects keep the language distinct.

Room composition: Use a restrained two-level upper mirror outline, keeping its lower edge calm above the existing basin. Pair it with one sandy-grey storage piece and a small genuine clay dish against the unchanged warm-grey tile. A cocoa towel and a chalk-white towel provide tactile depth without importing the living room's ochre as a large colour field. The composition must remain convincing under the same neutral artificial lighting as every other bathroom, with no invented sun or window.

Products (verified records): Existing built basin, WC, walk-in shower and black fittings retained from authoritative image 1; exact brand/SKU beyond the source is not asserted. New hero objects are the individually dimensioned, made-to-order mirror and single storage piece below: quotation-required, not a verified catalogue product. Textile and small accessory samples must match the approved material sheet; no invented designer SKU.

Custom pieces: DM-B: safety-backed mirror W60 × H85 cm overall, upper edge offset by 8 cm between two broad sections, safe rounded corners and thin graphite metal frame, mechanically fixed. One W30 × H60 × D25 cm sandy-grey compact-laminate storage box, sealed edges and floor feet. These are proposed fabrication envelopes, not verified site dimensions; wall/anti-tip fixing, substrate, service access and material samples require approval before the image phase. Inherited row 07: 0.50 M HUF target, source band 0.30–0.70 for BOTH bathrooms and WC together. This bathroom uses a portion only; allocation and quotations unresolved, never assume the entire row is available.

Light: Windowless bathroom: neutral artificial light only from A902-FL04 above the basin and A902-ML10 at the ceiling. Target 3500 K within the template's 3000–4000 K range, identical exposure/white balance for all ten bathrooms; use a simple opal-diffused basin fitting after its exact size and wet-zone suitability are approved. No new point, no backlit mirror circuit, no daylight, skylight or light shaft.

Avoid: desert views, new stone cladding, a sunlit shower, multiple decorative shelves. No unlisted hero furniture, no product recolouring, no invented dimensions or geometry; no people, logos or text on the image.

Inputs (in order): Image 1 = verified empty bathroom 06.2 base with built sanitary fixtures, to be produced after Claude fixes Cam_10 in the lock; it does not yet exist. Image 2 = targeted, room-confirmed 06.2 site photos; ME-BAL-064/066 are provisional and must not be assumed to show 06.2. Image 3 = no original bathroom reference exists; optional living/master calibration mood only, never bathroom geometry. Image 4 = approved mirror/storage fabrication sheets and textile samples (product photos if an approved ready-made equivalent is selected). Follow source template §0/a; missing image 1 or 2 blocks image generation, not this creative specification.

Output: 04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S10_DesertModern70_4_furdo-06-2_Cam_10_A.png (+ same basename .prompt.txt)

## Források (rögzített bázis)

- **[A]** [ai-coordination/results/WSG-20261024-STYLE10-002.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/ai-coordination/results/WSG-20261024-STYLE10-002.md)
- **[B]** [ai-coordination/audits/WSG-20261024-STYLE10-002_CLAUDE_AUDIT.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/ai-coordination/audits/WSG-20261024-STYLE10-002_CLAUDE_AUDIT.md)
- **[C]** [ai-coordination/inputs/STYLE_CLAUDE_ASTRA_FORRASOK_20261024.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/ai-coordination/inputs/STYLE_CLAUDE_ASTRA_FORRASOK_20261024.md)
- **[D]** [ai-coordination/inputs/A902_v2b/ARKONYVTAR_A902_2026-10-24.csv](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/ai-coordination/inputs/A902_v2b/ARKONYVTAR_A902_2026-10-24.csv)
- **[E]** [05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md)
- **[F]** [03_blender/geometry_lock_A902_v2b.json](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/03_blender/geometry_lock_A902_v2b.json)
- **[G]** [03_blender/geometry_A811_A812/meretproba/MERETPROBA_KANAPE_A902.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/03_blender/geometry_A811_A812/meretproba/MERETPROBA_KANAPE_A902.md)
- **[H]** [01_alaprajzok/villamos_kiallasok/OSSZESITO.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/01_alaprajzok/villamos_kiallasok/OSSZESITO.md)
- **[I]** [ai-coordination/inputs/A902_v1/KOLTSEG_KIINDULAS_A902.csv](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/ai-coordination/inputs/A902_v1/KOLTSEG_KIINDULAS_A902.csv)
- **[J]** [06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md)
- **[K]** [ai-coordination/inputs/A902_v2b/arforras/kavehome_hu_kereses_20261024.txt](https://github.com/peterkapusi88-hub/wsg-berendezes/blob/46e3c5cbe2607479d7eba8037b1fbbc164365fe6/ai-coordination/inputs/A902_v2b/arforras/kavehome_hu_kereses_20261024.txt)

**Zárás:** 40/40 kreatív promptblokk, kép nélkül; KONCEPCIÓ – NEM VALIDÁLT. KEP-004 nem indult, termék-/méret-/kamera-/költségkapuk nyitottak.
