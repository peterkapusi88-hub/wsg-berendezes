# KEP006 – GPT-6 Astra V3.3 A/B/C renderkör (nappali + Kyoto Ink)

Státusz minden képen: **KONCEPCIÓ – NEM VALIDÁLT**. Ezek AI-koncepcióképek, nem kivitelezési dokumentumok.

- Kreatív forrás: Astra V3.3 csomag (`05_promptok/KEP006_GPT6ASTRA_V3_3_r1/`). A promptok szó szerint mentek át (BEGIN..END blokk), az integrátori megjegyzések külön blokkban vannak.
- Generálás: ChatGPT képgenerálás, High beállítással, 2026-10-26. Chat-azonosítók a `KEPNYILVANTARTAS_V33.csv` fájlban.
- Terjedelem (Péter, 2026-10-26):
  - csak nappali (Cam_12, Cam_02), S16/S17 elsőként;
  - S16/S17 A/B/C változat;
  - S01–S15 C változat;
  - soron kívül a teljes Kyoto Ink C-sor (Cam_03/04/11c/10).
- Javítások:
  - S02 Cam_12 C v2: nappali fény, teljes magasságú W02;
  - S17 Cam_12 C v2: W02 szélessége visszaállítva;
  - S17 Cam_02 C v2: TV-tengely (határeset maradt).
- A G 63 autófotók csak szín- és anyagreferenciák.
- Hiányzó termékfotók: Nordli, Jättebo, Ciselia, Melva. Ezek nincsenek csatolva, a csomagban „Not attached” jelöléssel szerepelnek.
- Visszatérő eltérés a Cam_02-n: a TV-fal kompozíciója általában 5–12%-kal balra tolódik a TV-ponttól. A vonatkozó képek „határeset” jelölést kaptak.
- Mappák:
  - `images/`: a képek;
  - `prompts_sent/`: a ténylegesen elküldött üzenetek;
  - `qa/gate/`: bázis/render összevetés;
  - `qa/kontaktlap/`: kontaktlapok;
  - `qa/naplo.json`: QA-napló.
- Korábbi ágakat (V3.1, V3.2, PR #21–24) ez a kör nem módosít.
