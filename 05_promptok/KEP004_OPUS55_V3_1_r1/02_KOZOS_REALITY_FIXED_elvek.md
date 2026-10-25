# 02 · Közös reality-elvek (angol) – C versenyző, V3.1 r1

**Mire:** minden saját prompt erre épül; a promptok a nézetre értelmezett, rövidített változatát tartalmazzák (önállóan, hivatkozás nélkül). Forrás: a promptsablon v3.1 §1 (`05_promptok/A902_STYLE10_4helyiseg_prompt_sablon_v3.md`) átvett részei – geometria és kamera, meglévő felületek, őszinte anyagnevek, közlekedési méretek – a VB-blokk szerint módosítva.

**Nem átvett, felülírt mondatok:**
- „Walls and ceilings: painted white” → helyette a stílus falterve; a **mennyezet fehér marad**, a stílus által nem kezelt falak fehérek.
- „Light and grading – Series A neutral overcast…” → helyette a VB.3 kameránkénti fénye (lent, R7).
- A v3.1 „Egger Grey Treviso Oak EL2184” padlónév → a VB.8 szerint a dekor NEM IGAZOLT, ezért a promptok a helyszíni fotó szerinti szürkésbarna tölgyet írják, terméknév nélkül.

A futtatási csomagban Claude ezeket a Blenderből ellenőrzött FIXED- és FRAME LAYOUT-blokkal cseréli vagy egészíti ki.

---

## R1 · Geometry and camera
Image 1 (the neutral Blender base of the named camera) is authoritative for geometry, openings and framing. Keep the exact framing and the vertical lines vertical; keep every wall contour, the 2.90 m ceiling height, door and window positions and the real exterior view. Do not widen or deepen the room, do not add or move walls, columns, niches, bulkheads, coves, dropped ceilings or ceiling fixtures.

## R2 · Ceiling and power
The ceiling is white and carries radiant heating/cooling panels: nothing is fixed to it except the existing light points named in the prompt (living ML05, dining ML04, kitchen ML03, master ML06, bathroom ML10). Every light and every powered element is fed from an existing point named by its ID (ceiling ML, wall FL, socket D); no new outlet, no chased cable. Switches, thermostats, sensors, sockets and the intercom stay visible and free.

## R3 · Existing surfaces that do not change
- Floor in living, dining, kitchen and bedrooms: the existing medium grey-brown oak-look floor exactly as in the site photo (image 2), with strong grain and a 6 cm matching skirting – not light oak, not cool grey, not concrete; its exact decor is not verified, so copy the photo, never re-invent it.
- Interior doors light grey with black handles, in their real position and size.
- Window and door frames white inside, anthracite outside, set in a dark brick reveal.
- Bathroom 06.2 exactly as built: Geostone Grigio 60×60 matt porcelain on floor and walls to 2.85 m, Esagonetta Grigio hexagonal 3D decor tile on the shower back wall and above the WC ledge, walk-in shower without glass screen, black Grohe fittings, white Geberit Smyle Square basin and WC, black towel radiator.
- Terrace exactly as built: porcelain tiles 15 cm below the floor, raised ribbed WPC deck at +0.62 m, green roof, anthracite bar railing; the real Buda view with city roofs and hills.

## R4 · Walls
Every significant visible solid wall follows the style's wall plan (wallcovering, laminate or textile panels, printed artwork, integrated storage, hidden light). Walls and areas the style does not treat stay smooth white. No plaster, microcement, tiles or real stone added; nothing is demolished or built.

## R5 · Honest materials
Laminate reads as laminate, decor board as decor board, vinyl wallcovering as wallcovering, printed or mineral panels as printed panels. Stone-, travertine-, marble- or concrete-effect decors are allowed only when named as effect decors and must never look like solid natural stone. Real metal, glass, mirror, ceramics, wool or marble only where a named product is made of it. Custom joinery: matt or structured laminate board, fluted MDF, bent MDF for curves, at most one veneered surface; interiors white; no painted fronts unless the prompt explicitly names an approved exception.

## R6 · Furniture, dimensions, circulation
Only the products named in the prompt, at their stated real dimensions, configuration and handedness – no enlarging, shrinking or extra hero furniture. Main routes at least 90 cm with chairs pushed in (terrace door, kitchen, bedroom corridor, door of room 05.3); 90 cm chair pull-out; sofa front to coffee table 45–50 cm; sofa to TV-wall furniture at least 60 cm; at least 60 cm beside the bed; every door swings free. Layout C: sofa back to the east facing the dining zone, long seat north–south, open to the TV wall in the west, north end clear of the glazing; dining table 160 × 90 cm on the long north–south axis under ML04, six seats 2+2+1+1.

## R7 · Light by camera (VB.3)
- Cam_02: blue hour / early evening, premium layered Philips Hue at 2200–2700 K, no RGB colour; mid-key exposure, no crushed blacks, no blown highlights; wall edges, openings, floor–wall line, terrace deck, railing and green roof stay readable; LED light comes evenly out of opal profiles, never as visible dots; light only from the named fixtures.
- Cam_12 and Cam_03: daytime, natural bright interior-photography light through the north glazing (no sun patches – north façade), Hue subdued or off.
- Cam_04: evening, Hue scene (headboard light, reading lights), readable edges.
- Cam_11: daytime, real panorama, neutral white balance.
- Cam_10: artificial light only from the existing bathroom points; no window, no daylight.
All Hue luminaires: E27, E14 or GU10 sockets with the Hue bulb physically fitting, or Philips Hue fixtures / light strips in aluminium profiles with opal covers.

## R8 · Proven failure modes (max. ~8 negatives per prompt, chosen per view)
A physically impossible mirror reflection; a light brick reveal instead of the real dark one; a floor lighter or cooler than the real one; a different number of fronts than specified; a floor-to-ceiling mirror where none is specified; furniture taller, larger or displaced from the stated size (heights are given in numbers); an invented ceiling cove, dropped ceiling or ceiling light line; a fictional view or changed glass division.

## R9 · Status line
Every image: CONCEPT – NOT VALIDATED. Geometry, power, Hue and cost are verified by the integrator before any comparison image.
