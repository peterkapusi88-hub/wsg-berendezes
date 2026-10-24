# A-902 Cam_02 nappali – Rubin Szalon / Ezüst Orbit Gemini-koncepcióteszt, prompt v1 (2026-10-24)

> **KONCEPCIÓ – NEM VALIDÁLT.** Gyors, összehasonlító stílusteszt, nem Render Reality Gate PASS. Eredmény és audit: `ai-coordination/results/WSG-20261024-GEMINI-RENDER-TEST-002.md`.

## Forrás
- Promptok: `ai-coordination/results/WSG-20261024-PILOT-001.md`, „Rubin Szalon — prompt” és „Ezüst Orbit — prompt” (commit `f307765`, sha256 `5e2f3e82…8343a`, változatlan). A szöveg **szó szerint** azonos a pilotéval, géppel kiolvasva; csak a `> ` idézőjelek és a sortörések lettek bekezdésekké fűzve.
- Egyetlen kiegészítés: a prompt elé tett **képjelmagyarázat** (lent). Ez megmondja, melyik feltöltött kép mire szolgál, mert a pilotprompt „supplied site photographs”, „registered floor reference” és „supplied camera-matched corrected terrace background” hivatkozásai fájlnév nélküliek. A kamerához illesztett, javított teraszháttér **nem létezik** (Claude-audit 4.1: KIMARAD), ezért a jelmagyarázat ezt kimondja, és a valós helyszíni képeket jelöli meg külső referenciaként. Stílus, bútor, anyag, fény: változatlan.

## Bemeneti képek (feltöltési sorrend, mindkét futásnál azonos)
| # | Repóútvonal | Méret | sha256 (eleje) | Szerep |
|---|---|---|---|---|
| 1 | `04_renderek/semleges/A902_semleges_1_nappali.jpg` | 1600×1000 | `fb383459` | geometria + kamera (Cam_02) |
| 2 | `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-080_parketta_szegely_kozel.jpg` | 1200×1600 | `88f93864` | meglévő padló + szegőléc |
| 3 | `08_allapotfelmeres/fotok/A902/04_nappali/A902_04_20261021_ME-BAL-045_nappali_terasz_fele.jpg` | 1600×1200 | `06981c28` | fehér fal, belül fehér profil, világosszürke ajtó, greslap + WPC-lépcső |
| 4 | `08_allapotfelmeres/fotok/A902/12_zoldtető/A902_12_20261021_ME-BAL-006_zoldtető_domb_agyas_kilatas.jpg` | 1600×1200 | `6190a908` | valós tetőkert (WPC, betonszegély, évelődomb, gyep, korlát) |
| 5 | `02_referenciak/A902_helyszin/terasz_video_2026-10-21/A902_terasz_panorama_v0b_videobol.jpg` | 1678×1377 | `9d0457ee` | valós távoli kilátás (budai hegyek) |

A `terasz-v2_07` Blender-előnézetet szándékosan **nem** adtam be: nem valós referencia, és tengerszerű horizontot mutat.

## Beállítások (Gemini webapp, 2026-10-24)
- Fiók: peter.kapusi88@gmail.com (Google AI Plus), `gemini.google.com/u/0/app`, két **külön, új csevegés** (nincs Gem, nincs közös előzmény).
- Modellválasztó: **3.1 Pro**, gondolkodási szint **Alacsony** (alapértelmezett). Eszköz: **„Kép létrehozása”** („Képek” chip). Képek száma: **1**. Méretarány: **nem választva** (a kínálat 1:1 / 9:16 / 3:4 / 4:3 / 16:9; 16:10 nincs). Stíluspreset: **nincs**.
- Csatolás: rejtett file-input + paste-esemény; szöveg: `insertText`.

## Beküldött szöveg – közös képjelmagyarázat (mindkét futás eleje)

```
Reference images, in upload order:
1 – A902_semleges_1_nappali.jpg = the Cam_02 neutral render. Use it ONLY for room geometry, camera and framing; keep its composition exactly. Its black frames, flat grey floor and flat green terrace are obsolete placeholders.
2 – Site photo: the existing floor and skirting (the registered floor reference).
3 – Site photo of the same living room from another viewpoint: white walls, white interior window frames, light-grey door, terrace paving and WPC steps outside. Do not copy its viewpoint or its opening layout.
4 – Site photo: the real roof garden (WPC deck, concrete edging, perennial mound, lawn, anthracite bar railing). The cranes are temporary, not part of the view.
5 – The real distant view from the terrace: Buda hills with villas, city rooftops.
A camera-matched corrected terrace background does not exist yet; images 3–5 are the real exterior references to show through the glazing of image 1.
```

## Rubin Szalon – a jelmagyarázat után, szó szerint a pilotból

```
Create a photorealistic CONCEPT ONLY image of the A-902 living room, style “Ruby Salon”. Use A902_semleges_1_nappali.jpg strictly for the interior geometry and camera: Cam_02_Nappali_terasz, position (8.3, 4.4, 1.55) metres, Euler rotation (1.4791, 0, 0.8577) radians, 20 mm lens, 1600 × 1000. Preserve the exact framing, walls, openings, glazing divisions and ceiling geometry. Do not widen the room.

Use the supplied site photographs for existing materials. Retain the actual cool grey, knotty oak laminate flooring, documented as Egger Grey Treviso Oak EL2184, including its skirting. Do not reproduce the neutral render’s flat grey placeholder floor. Do not invent board dimensions or orientation; use the registered floor reference. Keep all walls and the ceiling painted white. Interior window-frame faces are white; exterior faces are anthracite. Retain the existing light-grey interior doors where visible.

Use the same furniture layout as the paired Silver Orbit concept: one low grey sofa along the left solid wall, with a 240 × 100 × 69 cm reference envelope; a coffee-table zone in front; unobstructed entrance-to-terrace circulation. Furniture dimensions must not be reduced to simulate clearance.

Above the sofa, show three separate ruby-red upholstered textile panels, each approximately 60 × 120 cm, with narrow white wall gaps. Show actual fabric texture and shallow upholstered edges, not lacquer or stone. Add one smoked-glass coffee table with a restrained dark frame, a limited-size grey rug, white sheer curtains and ruby side curtains gathered clear of the glazing. Add one slender floor lamp. Do not add extra chairs, sculpture or ceiling fixtures.

Use soft neutral daylight with restrained 2700 K practical lighting, identical exposure and white balance to the paired concept. Keep substantial flooring visible. Use only the supplied camera-matched corrected terrace background; do not invent a skyline or reproduce the obsolete flat garden. No people, text, gold ornament, marble, wall repainting or architectural changes.
```

## Ezüst Orbit – a jelmagyarázat után, szó szerint a pilotból

```
Create a photorealistic CONCEPT ONLY image of the A-902 living room, style “Silver Orbit”. Use A902_semleges_1_nappali.jpg strictly for the interior geometry and camera: Cam_02_Nappali_terasz, position (8.3, 4.4, 1.55) metres, Euler rotation (1.4791, 0, 0.8577) radians, 20 mm lens, 1600 × 1000. Preserve the exact framing, walls, openings, glazing divisions and ceiling geometry. Do not widen the room.

Use the supplied site photographs for existing materials. Retain the actual cool grey, knotty oak laminate flooring, documented as Egger Grey Treviso Oak EL2184, including its skirting. Do not reproduce the neutral render’s flat grey placeholder floor. Do not invent board dimensions or orientation; use the registered floor reference. Keep all walls and the ceiling painted white. Interior window-frame faces are white; exterior faces are anthracite. Retain the existing light-grey interior doors where visible.

Use the same furniture layout as the paired Ruby Salon concept: one low grey sofa along the left solid wall, with a 240 × 100 × 69 cm reference envelope; a coffee-table zone in front; unobstructed entrance-to-terrace circulation. Furniture dimensions must not be reduced to simulate clearance.

Above the sofa, show one approximately 140 cm circular mirror with a thin silver-coloured frame and subtle concealed 2700 K backlighting. The mirror must reflect the actual room geometry, not an invented window or landscape. In front of the sofa, show two offset circular tables, approximately 70 and 45 cm in diameter, 32 and 42 cm high. Their surfaces are matte graphite laminate/HPL with realistic edge banding, not solid stone or seamless metal. Add a limited-size pale-grey rug, white sheers, ice-blue side curtains and one slender floor lamp. No additional furniture or ceiling fixtures.

Use soft neutral daylight, identical exposure and white balance to the paired concept. Keep substantial flooring visible. Use only the supplied camera-matched corrected terrace background; do not invent a skyline or reproduce the obsolete flat garden. No people, text, RGB lighting, marble, champagne gold, wall repainting or architectural changes.
```
