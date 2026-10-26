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

## Állapot – 2026-10-26 16:50 (KÉSZ)
- **104 kép kész:** a teljes 47 × 2 = 94 kép (v1) + 10 javítókép (v2–v4). Minden kép QA-zva, státusz: KONCEPCIÓ – NEM VALIDÁLT.
- 11:20-kor a ChatGPT Plus képkerete elfogyott (seq 49 SKIPPED_LIMIT); 15:35-től **ChatGPT Pro**-n folytatva, a seq 49 új chatben újra lefutott. Kerülőút nem volt.
- Gondolkodási szint: minden képnél **High**, kivéve X05 A/B (S11 Cam_F_3488), amely a véletlenül „Pro” modellre állított választóval készült (segédügynökkel) – a naplóban jelölve.
- X06 A: az első chat (6adf6e03) nem töltött be, kép nem jött → új chatben újraküldve (6adf6f96).
- Extráknál (Cam_F_*, Vanity) az A/B különbség a várakozásnak megfelelően kicsi; QA-ban „A≈B” jelölve.
- Javítási jelöltek (nem futtatva, tulajdonosi döntésre): X10 A/B és X11 A – a fotón fehér falak greige-re színeződtek; több képen pendant/kültéri lámpa villamos kiállás nélkül; X06/X13 gardrób takarja a meglévő aljzatot.
- Kontaktlapok: `qa/kontaktlap/V32_S11..S15_*_kontaktlap_AB.jpg` (alap) és `V32_EXTRA_1/2_kontaktlap_AB.jpg` (extrák). Chat-azonosítók: `checkpoints/chat_azonositok_pro.txt`.
