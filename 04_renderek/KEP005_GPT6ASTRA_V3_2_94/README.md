# A-902 · GPT-6 Astra V3.2 · 47 × 2 renderkör (A eredeti + B profi fotóalapú)

**Státusz minden képen: KONCEPCIÓ – NEM VALIDÁLT** (műszaki, villamos, termék- és költségkapu nyitott).

- Forrás: `competition/gpt6astra-v3-2-five-new-20261025` @ 9738655, `05_promptok/KEP005_GPT6ASTRA_V3_2_r1/` (30 alap + 17 extra prompt, szó szerint, BEGIN..END).
- Generálás: ChatGPT Képek (Claude Browser, két fül), 2026-10-26. A V3.1 képek (`KEP004_…`) érintetlenek.
- **A – eredeti Astra V3.2:** Blender-alap a fix kamerából + helyszíni padlófotó (ME-BAL-080) + helyszíni felületfotó + pendant termékfotó + Astra saját képreferenciái (S12: tulajdonosi IMG_2589; S13: WSG-lobby KZS_3896, KZS_3914). Cam_11 = a kötelező eredeti Cam_11 (nem Cam_11c).
- **B – profi fotóalapú:** ugyanaz a dizájn; padló = profi KZS_3695; Cam_02-nél 15 cm-es belső fellépést mutató Blender-alap; anyagszabály-blokk (szürke padló, taupe lábazat, fehér falak/keretek, szürke ajtók, sík fehér 2,90 m mennyezet; fürdő: szürke Geostone + Esagonetta hatszög). Szabályforrás: `05_promptok/PROMPT_ELVEK_FOTOVALIDALT_A902.md` v1.
- **Extrák:** Cam_F_* = a profi fotó maga az 1. kép (fotó-natív kamera, numerikus Blender-illesztés nem igazolt); A és B ugyanazt a kamerát kapja, B-ben csak anyag-/teraszszabály és padlófotó többlet → az A/B különbség itt várhatóan kicsi (QA jelöli). Cam_X_06_2_Vanity = **FELTÉTELES** (javasolt kamera, Blender-validálás nélkül; KZS_3598 csak anyag). Cam_11c (S15) = külön, tulajdonos által jóváhagyott kiegészítő nézet.
- Javítóképek: `_v2`, `_v3` utótag; az eredeti v1 megmarad. Indok a `KEPNYILVANTARTAS_V32.csv` `javitas` oszlopában.

## Mappák
- `images/` – generált képek (`<kep_id>__V32_<A|B>_<verzió>.png`)
- `prompts_sent/` – a ténylegesen elküldött teljes üzenetek
- `KEPNYILVANTARTAS_V32.csv` – képenként: stílus, kép-ID, kamera, kamerastátusz, A/B, verzió, javítás, promptfájl + SHA, referenciák, QA, státusz, chat
- `qa/gate/` – Blender-lockpont és élátfedés kapukép; `qa/kontaktlap/` – A/B kontaktlapok
- `checkpoints/` – terv, QA-napló, építő- és futtató szkriptek
