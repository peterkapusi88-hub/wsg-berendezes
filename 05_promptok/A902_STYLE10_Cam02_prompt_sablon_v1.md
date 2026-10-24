# A-902 – Cam_02 render prompt template for the 10-style round (v1, 2026-10-24)

Used by: `ai-coordination/requests/WSG-20261024-STYLE10-002.md`. Fill the `{…}` fields per style. The fixed block must be copied **unchanged**, so that the ten images stay comparable. Status of every image made from this: **CONCEPT – NOT VALIDATED** until Claude's post-render audit.

**Input images (in this order):**
1. `04_renderek/semleges/A902_semleges_v2_1_nappali.png` (**FÜGGŐ, még nincs a repóban**): geometry, camera, glazing, terrace levels.
2. `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg`: floor and skirting material.
3. `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg`: wall white, door colour, frame colour, terrace materials.
4. `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg`: the real view.
5. Optional: one product photo per hero product.

---

## FIXED BLOCK (copy verbatim)

> Create a photorealistic **CONCEPT ONLY** interior image of the A-902 living room, style "{STYLE_NAME}".
>
> **Geometry and camera.** Use image 1 strictly for room geometry and camera: Cam_02_Nappali_terasz, position (8.30, 4.40, 1.55) m, Euler rotation (1.4791, 0, 0.8577) rad, 20 mm lens, 1600 × 1000, eye level. Preserve the exact framing, the walls, the 2.90 m white ceiling, the glazing size and divisions as shown in image 1, and the door and threshold positions. Do not widen the room. Do not add walls, columns, niches, bulkheads, coves or ceiling fixtures attached to the ceiling.
>
> **Existing surfaces – must not change.**
> - Floor: the existing Egger Grey Treviso Oak laminate exactly as in image 2. It is a medium grey-brown oak with strong grain and knots, with matching 6 cm skirting. It is not light oak, not cool blue-grey and not concrete. Do not invent plank width or direction beyond what image 2 shows.
> - Walls and ceiling: painted white, smooth, with no colour cast. Warm evening light may tint them, but they remain white paint.
> - Window and door frames: white on the inside. Exterior frame faces are anthracite, set in a dark anthracite brick reveal.
> - Interior doors, if visible: light grey with black handles.
>
> **Outside.** Show the real multi-level roof garden from image 1:
> - light grey stone-look porcelain terrace just below the interior floor;
> - raised grey-brown WPC deck with steps;
> - green roof with flat lawn edges and a gently mounded perennial bed;
> - knee-high concrete edging;
> - anthracite vertical-bar railing.
>
> The distant view is the one in image 4: Buda hills with villas and city rooftops. **No invented skyline, no sea, no generic Budapest landmarks.** Temporary cranes may be omitted.
>
> **Layout {L1|L2}.** {LAYOUT_SENTENCE – e.g. "One sofa against the left (west) solid wall, facing right; coffee table 45–50 cm in front; a clear walkway at least 90 cm wide from the right foreground to the terrace door"}. Furniture must keep its real product dimensions. Never shrink pieces to fake clearance.
>
> **Light.** Soft overcast daylight, neutral white balance, identical exposure for all ten styles. Optional second variant: the same frame at dusk with 2700 K practical light only from the fixtures listed below.
>
> **Prohibited.** No people, text, logos or watermarks. No marble, travertine or stone unless listed below with its real material. No gold unless listed. No wall paint colour, wallpaper or panelling except the items listed below. No extra furniture, plants, art or lamps beyond the list.

## STYLE BLOCK (fill in, max. ~120 words)

> **New items – show exactly these and nothing else:**
> 1. {HERO_1: product or custom piece, real size, visible material as actually specified (e.g. "matte graphite HPL with straight edge banding", "ruby cotton velvet upholstered panels, 2 mm gaps"), position}
> 2. {HERO_2 …}
> 3. {SOFA: product name, W × D × H, fabric and colour}
> 4. {TABLES / RUG (size) / CURTAINS (layers, colour, track at the window lintel)}
> 5. {TV: where and how – or "no TV in this room"}
> 6. {LIGHT: the visible fixtures and LED lines; for hidden LED say where the profile sits}
>
> **Palette:** {4–6 colours with materials}. **Mood:** {one sentence}.

---

**Post-render (Claude):** a deviation table per `RENDER_REALITY_GATE.md` C (floor / walls / frames / glazing / terrace / view / products / extra items), followed by the status.
