# A-902 – Cam_02 render prompt template, 10-style round (v2, 2026-10-24 evening) – PHASE KEP-004 ONLY, NOT STARTED

Supersedes `A902_STYLE10_Cam02_prompt_sablon_v1.md` (whose image 1 was the obsolete v1 neutral render). Used by `ai-coordination/requests/WSG-20261024-STYLE10-KEP-004.md`. Status of every image made from this: **KONCEPCIÓ – NEM VALIDÁLT** until Claude's post-render Gate audit (`ai-coordination/RENDER_REALITY_GATE.md`). Style blocks = Astra's own Phase-A drafts (result file §10, verbatim) + Claude's mandatory additions from the audit (`ai-coordination/audits/WSG-20261024-STYLE10-002_CLAUDE_AUDIT.md`, H1–H4). Astra may refine the creative wording of its own block; the mandatory additions (products, handedness, layout family, gesture, points) may only change with a verified product record and a geometry re-run.

**Input images (in this order):**
1. `04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_02_nappali-terasz.png` – **geometry and camera only**, empty room, neutral diffuse daylight, AgX, exposure +0.75. **Prerequisite (audit H7): re-rendered or verified against the v2b-1 .blend (PR #11 parapet/facade fix) before use.** Cross-check: `04_renderek/semleges_v2b/A902_semlegesv2b_1_nappali_ellenorzo.png` (points, TV block, HF03 field drawn in).
2. `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg` – floor and skirting material.
3. `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg` – wall white, door colour, frame colour, terrace materials.
4. `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg` – the real view.
5. One product photo per hero product named in the style block (sofa, dining table), from the verified product page.

---

## FIXED BLOCK (copy verbatim into every prompt)


> **CONCEPT ONLY – NOT VALIDATED. Do not generate before the KEP-004 gate is open.** Create a photorealistic interior image of the A-902 living room, style "{STYLE_NAME}", for a ten-way comparison.
>
> **Geometry and camera (image 1 is authoritative).** Use image 1 strictly for room geometry, openings and camera: Cam_02_Nappali_terasz, position (8.30, 4.40, 1.55) m, Euler rotation (1.479, 0, 0.858) rad, 20 mm lens, 36 mm sensor, shift 0, 1600 × 1000, eye level. Keep the exact framing, wall contours, the 2.90 m white ceiling, the glazing layout, the terrace levels (ceramic tiles −0.15 m, raised WPC deck +0.62 m, green roof) and the real Buda hillside view. Do not widen the room, do not add or move walls, columns, niches, bulkheads, coves, ceiling fixtures or ceiling construction. The ceiling carries heating/cooling panels: nothing is attached to it except the existing pendant point.
>
> **Existing surfaces – must not change.** Floor: the existing Egger Grey Treviso Oak EL2184 laminate as in image 2 – medium grey-brown oak, strong grain and knots, 6 cm matching skirting; not light oak, not cool grey, not concrete; do not invent plank width or direction. Walls and ceiling: painted white, smooth, no colour cast (evening light may tint them, they remain white paint). Window and door frames: white inside, anthracite outside in a dark brick reveal. Interior doors: light grey with black handles. Switches, thermostat, sensors and the south switch column (x ≈ 7.15) stay visible and free.
>
> **Furniture and products.** Use only the products and envelopes named in the style block, at their exact real dimensions and handedness; do not enlarge furniture or shrink it to fit. Keep a minimum 90 cm circulation route from the entrance to the terrace sliding door, the kitchen, the bedroom corridor and the master door (accepted side route 0.75 m on the terrace side only); 45–50 cm between sofa and coffee table; the dining table 0.30 m west of the plan position with 90 cm chair pull-out. Powered items only at the existing point IDs named in the style block. Laminate reads as laminate, fabric as the named fabric; real metal, glass and ceramics only where specified; no faux stone, no faux travertine, no fake marble.
>
> **Light and grading – comparison rules.** Series A (mandatory first): neutral overcast daylight, no sun, exposure and white balance identical for all ten images and for the two calibration images; no warm grading, no haze, no bloom. Series B (only after Series A is approved): identical evening scene with the existing points lit, same camera. Luxury must come from silhouette, material depth, proportion, layering and negative space – not from warmer light, larger imaginary furniture, a wider lens or a fictional skyline.
>
> **Style block follows. Unresolved fields are blockers, not creative freedom.**

---

## CALIBRATION PAIR (render first, same fixed block) – the measurable creative minimum (audit H5)

### C1 — Zenit (original concept, re-rendered on the Cam_02 base)

> Style "Zenit – calibration". Reproduce the original Zenit concept of `06_koncepcio/WSG_berendezes_Zenit_es_LakeForest_verzio.md` on this exact geometry: greige upholstery, smoked-oak-effect laminate (Egger H1180/H3710 family) floor-standing media composition on the west block, concrete-effect laminate accents, black metal, one bronze-tinted mirror, mustard/olive accent in textiles only; L sofa Westwing Lennon 238×180 greyish-brown or Kave Home Blok corner 290×230; Toni oval dining table; layout L3. Honest materials: laminate as laminate, no real stone, no plaster, no ceiling work. This image is the creative minimum reference, not a competitor.

### C2 — Lake Forest (original concept, re-rendered on the Cam_02 base)

> Style "Lake Forest – calibration". Reproduce the original Lake Forest concept of the same document: cream textured upholstery (Westwing Wolke 258×167 left corner, off-white teddy bouclé), light-oak-effect laminate cabinet with one curved end, travertine-look only as a clearly described printed/laminate panel (never real stone), champagne-gold metal in small real pieces, white marble-effect only on a small real table top; Toni oval or Kave Home Nealy round ecru Ø150 dining table; layout L3. Same neutral daylight as Series A. This image is the creative minimum reference, not a competitor.

---

## STYLE BLOCKS S01–S10 (Astra draft verbatim + mandatory additions)

### S01 — Kyoto Ink

**Astra draft (Phase A, §10, verbatim):**
> Compose a contemporary Japanese private residence around a low, deep L-shaped seating island, a long dark floor-supported cabinet and a single asymmetric translucent textile plane. Balance horizontal mass with a narrow open lattice detail and substantial empty white wall. Use the approved taupe woven sofa, charcoal laminate, natural linen and one real ceramic object. The dining table is a calm oval timber volume. Avoid generic beige Japandi, decorative bonsai and fake shoji architecture. The composition must remain distinctive without warm lighting.

**Mandatory additions (Claude audit, binding):**
> Sofa: Westwing Lennon modular L 238×180×68 cm, greyish-brown woven, right corner element (alternative: Kave Home Vera 232 cm chaise sofa) – exact footprint, no enlargement. Layout L3: seating pulled inward, TV on the west factory block (points D16/D17). Dining: Westwing Toni oval oak 200×90 cm, 6 chairs, table centre shifted 0.30 m west of the plan position (P902_24A). Primary gesture A: one translucent textile field with a narrow black lattice; everything else quiet.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S01_KyotoInk_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S02 — BiBo Nocturne

**Astra draft (Phase A, §10, verbatim):**
> Create a sculptural residential salon inspired by the spatial confidence of BiBo Budapest: a verified navy U-shaped conversation group, a low matte-blue cabinet composition and one softly irregular safety-backed mirror plane integrated with the furniture. Contrast opaque blue mass with the transparent dining table and a restrained opal light cluster at the existing ceiling point. Preserve generous white negative space. Do not reproduce restaurant logos, artworks, floral ceiling installations or a new panorama. Use the measured L alternative if the U fails circulation.

**Mandatory additions (Claude audit, binding):**
> Sofa: a real U – IKEA JÄTTEBO 3.5-seat with two chaises, Samsala dark blue, 285×160×71 cm (premium alternative: Kave Home Gala 210 cm double chaise, colour to be verified); L fallback: Lennon 238×180 in dark blue woven. Layout L3 ONLY (U does not fit with a south TV). Dining: Westwing Anouk clear glass 180×90 cm. Primary gesture B: one rounded safety-backed mirror plane integrated into a low matte-blue cabinet (approx. 240×40×50 cm, floor-standing).
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S02_BiBoNocturne_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S03 — Alelí Casa

**Astra draft (Phase A, §10, verbatim):**
> Make the oval timber dining table the social centre of a contemporary Italian residence. Relate it to a generous olive L sofa, a low cabinet with one rounded end, tactile linen and a single authentic ceramic relief. Terracotta appears in actual ceramic and approved textiles, never as an invented plaster finish over the existing white shell. Keep the room composed and architectural through proportions and depth. Avoid rustic beams, faux brick and themed trattoria decoration.

**Mandatory additions (Claude audit, binding):**
> Sofa: olive L – Westwing Melva olive 238×143×75 cm or Kave Home Vera olive green 232 cm chaise. Layout L2: sofa with its back to the glazing, low media element on the south wall ending before the switch column (x ≈ 7.15), TV at point D19. Dining as the social centre: Kave Home Nealy round dark walnut Ø150 cm (or Toni oval 200×90), six chairs with 90 cm pull-out. Primary gesture F: the round table is the sculpture; one framed ceramic relief approx. 100×100 cm.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S03_AlelCasa_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S04 — LA Horizon

**Astra draft (Phase A, §10, verbatim):**
> Build a cinematic Los Angeles-inspired penthouse composition through low lounge seating, long layered furniture horizons, a brown glass dining table and an uninterrupted reading of the real window openings. Use two offset, floor-supported cabinet planes, not a monumental new TV wall. The approved sofa and terrace furniture should create a visual relationship while maintaining the measured circulation and level changes. Retain the real Buda hills. Avoid gold-marble clichés and LED outlining of every edge.

**Mandatory additions (Claude audit, binding):**
> Sofa: low L only – Westwing Lennon 238×180×68 (or Kave Home Blok 300 cm chaise sofa); NO U in this layout. Layout L2: sofa back to the glazing, two offset floor-supported cabinet planes on the south wall (total approx. 240 cm, depths 35/45 cm, heights 30/55 cm), TV at D19, switch column free. Dining: Westwing Anouk brown glass 180×90 cm. Primary gesture E: panorama framing – uninterrupted reading of the real window openings and the real Buda hills.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S04_LAHorizon_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S05 — Miami Streamline

**Astra draft (Phase A, §10, verbatim):**
> Interpret Art Deco through streamlined furniture geometry: a substantial dusty-rose L sofa, a stepped cabinet with rounded end profiles, two carefully proportioned vertical ribbed accents and a restrained glass dining plane. Add muted turquoise only through approved materials. Balance the curves with a graphic rug border and quiet white wall areas. Use real brushed metal sparingly. Do not add neon lettering, new arches, palm-pattern wallpaper or decorative plaster ceilings.

**Mandatory additions (Claude audit, binding):**
> Sofa: Westwing Melva dusty-rose corduroy L 238×143×75 cm. Layout L3, TV on the west block (D16/D17). Dining: Westwing Anouk clear glass 180×90 cm. Primary gesture G: material rhythm – one stepped, round-ended cabinet (approx. 220×40×55 cm) and two vertical ribbed MDF panels (approx. 40×160 and 65×160 cm) on the white wall; no plaster architecture, no ceiling work.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S05_MiamiStreamline_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S06 — Zenit Atelier

**Astra draft (Phase A, §10, verbatim):**
> Develop the original Zenit quality into a confident asymmetric residence: a low, deep taupe L sofa, a smoked-oak-effect floor-supported media cabinet, one offset taller storage volume and a broad rounded coffee table. Layer matte fabric, honest wood-effect laminate, brown glass and restrained dark metal. Concentrate integrated lighting within the approved furniture and existing electrical points. Keep a generous unfilled wall field. Avoid repeating slats everywhere, continuous ceiling LEDs and generic greige hotel styling.

**Mandatory additions (Claude audit, binding):**
> Sofa: deep L – Westwing Lennon 238×180×68 greyish-brown woven, or Kave Home Blok 3-seater corner sofa 290×230 cm (both fit layout L3). Layout L3, TV inside the dark low cabinet on the west block (D16/D17). Dining: Westwing Anouk brown glass 180×90 or Kave Home Argo round glass Ø119. Primary gesture C: asymmetric built-in-looking mass – low smoked-oak-effect cabinet approx. 240×40×45 cm plus one offset tall element approx. 45×35×190 cm, floor-standing with anti-tip fixing; one large low round coffee table (e.g. Kave Home Mosi Ø90).
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S06_ZenitAtelier_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S07 — Lake Forest Couture

**Astra draft (Phase A, §10, verbatim):**
> Develop Lake Forest into a light sculptural salon with the exact approved rounded L sofa, a broad pale cabinet with one curved end, a genuine shallow relief and a small real-metal table. Contrast smooth planes with textured upholstery and finely woven curtains; maintain a generous continuous seating composition rather than scattered decorative objects. Preserve white window frames and the existing strongly grained grey-brown floor. Do not fake travertine, enlarge the sofa, or substitute golden sunlight for material richness.

**Mandatory additions (Claude audit, binding):**
> Sofa: Westwing Wolke modular L 258×167×65 cm, LEFT corner element, textured light beige or teddy bouclé off-white (verified 1,050,000 HUF); curved alternative: Kave Home Martina curved 3-seater 246×112 cm + Neom end pouf. Layout L3. Dining: Toni oval oak 200×90 or Kave Home Nealy round ecru Ø150. Primary gesture F: the soft rounded sofa is the sculpture; one genuine shallow mineral relief approx. 100×130 cm on a frame; one small real-metal table (e.g. Kave Home Sheffield Ø80).
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S07_LakeForestCouture_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S08 — Milano Radical

**Astra draft (Phase A, §10, verbatim):**
> Compose a contemporary Italian collector's apartment from contrasting geometric bodies: the verified block-like U or L sofa, two cabinet volumes of different heights, an actually supported connecting plane, transparent dining glass and one genuine metal accent. Use a single large muted-yellow plane against navy and white, with a controlled geometric rug. Leave substantial gaps between objects. Avoid copied design icons, random colourful accessories and a crowded showroom arrangement.

**Mandatory additions (Claude audit, binding):**
> Sofa: a real U – IKEA JÄTTEBO 285×160×71 in Samsala dark blue or dark yellow-green; L fallback Lennon 238×180. Layout L3 ONLY. Dining: Westwing Anouk clear glass 180×90. Primary gesture B: geometric bodies – two ready cabinet volumes of different heights with a leg-supported bridging plane (total approx. 220×40×70 cm), one large muted-yellow laminate plane; at least 90 cm clear between sofa and cabinets.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S08_MilanoRadical_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S09 — Paris Collector

**Astra draft (Phase A, §10, verbatim):**
> Create a personal Parisian collector's salon through distinct furniture silhouettes, not a matched suite. Pair the verified olive L sofa with one slender chair, a brown glass dining table, a low dark cabinet and one large licensed artwork within a controlled plum-textile composition. Use layered curtains and an existing-point floor lamp to unify the group. Keep the white architecture quiet. Avoid invented heritage mouldings, counterfeit antiques and a scattered gallery wall.

**Mandatory additions (Claude audit, binding):**
> Sofa: olive L – Melva olive 238×143 or Kave Home Vera olive 232 – plus ONE different-silhouette armchair (e.g. Kave Home Corvena olive chenille, 98 cm). Layout L3; floor lamp at point D18 only, cable not crossing the route. Dining: Westwing Anouk brown glass 180×90. Primary gesture H: one large licensed artwork approx. 140×180 cm in a real frame on a plum textile field; low dark cabinet approx. 220×40×60 cm with one open book bay.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S09_ParisCollector_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

### S10 — Desert Modern 70

**Astra draft (Phase A, §10, verbatim):**
> Compose a contemporary desert-modern residence using low taupe lounge mass, a stepped floor-supported cabinet profile, one large geometric relief and earthy textiles. Generate depth through the actual furniture shadows and different plane depths. Use honest wood-effect laminate, real clay ceramic, ochre fabric and the existing white shell. Preserve the real green roof terrace and Buda view. Avoid cactus-themed decoration, faux stone formations and artificial orange colour grading.

**Mandatory additions (Claude audit, binding):**
> Sofa: low L only – Westwing Lennon 238×180 in terracotta or rust woven, or Kave Home Blok 300 cm chaise; NO U in this layout. Layout L2: sofa back to the glazing, stepped floor-standing cabinet on the south wall interrupted before the switch column, TV at D19. Dining: Toni oval oak 200×90 or Kave Home Naanim round walnut Ø120. Primary gesture C: terraced cabinet profile (approx. 220 × 35/45 × 35/60 cm) and one large geometric relief approx. 120×120 cm; stepped profile and relief must differ clearly from S04.
> Output file: `04_renderek/ai_chatgpt/STYLE10_KEP004/A902_S10_DesertModern70_1_nappali_Cam02_A.png` (Series A) / `_B.png` (Series B). Gate status at delivery: KONCEPCIÓ – NEM VALIDÁLT.

---

## Delivery and evaluation protocol (Claude, after the images exist)

1. **Thumbnail silhouette test:** each image at 400 px wide must be identifiable among the ten by massing alone; two images that read the same at thumbnail scale fail the differentiation rule (audit H1) and go back to Astra for silhouette, not colour, changes.
2. **Greyscale test:** desaturated copies must still show the composition (depth layers, negative space, light hierarchy).
3. **Calibration comparison:** every style is judged against C1/C2 rendered with the same fixed block – equal or better in presence, material depth and composition, or it does not pass the creative threshold.
4. **Reality Card per image** (Gate): floor, white walls/frames, openings, terrace levels, points, every dominant product with its verified record; deviations listed; status KONCEPCIÓ – NEM VALIDÁLT / ELŐSZŰRT – FELTÉTELES / FAIL. No PASS from an image.
5. Only after Series A is reviewed by Péter: Series B (evening), same camera.
