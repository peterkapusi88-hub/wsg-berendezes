# A902 Lake Forest – nappali, videó-záróképkocka stílusozása v1

- Cél: a Veo 3.1 Lite kezdő+záró képkockás tesztjéhez a **záróképkocka**.
- 1. kép (stílus + bútor + anyag): `04_renderek/ai_chatgpt/A902_LakeForest_1_nappali_chatgpt.png`
- 2. kép (geometria + kamera): `04_renderek/ai_video_tests/A902_LakeForest_1_nappali_blender_zarokep_jelolt_A.png` (Cam_02-ből 40 cm előre, 20° balra; lásd `03_blender/validator_report_2026-10-24_videozarokep.md`)
- Kimenet: `04_renderek/ai_video_tests/A902_LakeForest_1_nappali_zarokep_stilusozott_v1.png`, 1586×992 (a kezdőképpel azonos arány)
- Státusz: KONCEPCIÓ – NEM VALIDÁLT
- Dátum: 2026-10-24

## Prompt

Create a photorealistic interior image that is the SAME living room as Image 1, seen from the camera position and angle of Image 2.

Image 1 is the master for style: keep exactly the same furniture designs, materials, colors and lighting as Image 1 — cream bouclé L-shaped modular sofa with chaise, cream bouclé pouf, round white marble coffee table on a champagne-gold drum base, cream bouclé armchair with light oak frame, textured cream relief artwork in a light oak frame, champagne-gold glass-globe chandelier, cream linen floor lamp, sheer white curtains with taupe side panels, light oak floor, cream shaggy rug, black-framed floor-to-ceiling glass wall, terrace with olive tree, wooden spa and white hydrangeas, Budapest Danube view, warm late-afternoon daylight.

Image 2 is the master for geometry and camera only: copy its viewpoint, perspective, wall positions, window positions, ceiling height and furniture positions exactly. Its grey materials and white globe lamp are placeholders — replace them with Image 1's design. On the left wall Image 2 shows the TV wall: render it as a travertine panel with a thin bronze frame, a large black wall-mounted TV, a low floating light oak media bench with warm LED underlight, and narrow vertical light oak slats on both sides.

Do not add new rooms, doors, windows, columns, ceiling coves or objects. Do not move or resize furniture. Keep the glass wall and terrace exactly where Image 2 shows them. No people, no text, no logos. Same color grading and exposure as Image 1, so the two images can be the first and last frame of one continuous video shot. Aspect ratio 16:10.
