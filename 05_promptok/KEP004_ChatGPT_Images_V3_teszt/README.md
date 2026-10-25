# KEP-004 · ChatGPT Images · Astra Creative Upgrade V3 – két Cam_02 próbakép (KEP004-CGI-V3TEST-r1, 2026-10-25)

**Mi ez:** az S01 Kyoto Ink és az S02 BiBo Nocturne V3 Cam_02 próbaképének futtatott promptja.
- **Jóváhagyás:** Péter, 2026-10-25 02:06 („MEHET A KÉT CAM_02 TESZTKÉP GENERÁLÁSA”), képenként egy generálással.
- **Mindkettő lefutott** (02:18 és ≈02:23, CEST).
- **Eredmény és Gate-audit:** `ai-coordination/results/WSG-20261025-KEP-004_V3teszt_r1.md`.
- **Képek:** `04_renderek/ai_chatgpt/STYLE10_KEP004/CREATIVE_UPGRADE_V3/`.

**Nem végleges csomag.**
- A végleges S01/S02-sorozat Astra V3.1 világítási kiegészítésére vár (Péter, 01:49).
- A teljes 66 képes sorozatra nincs generálási engedély.
- A PR #16 nincs beolvasztva.

## Összefűzési sorrend
A promptot a `_eszkozok/epito_v3teszt.py` állítja elő, ellenőrzésekkel.
1. **Futtatási fejléc** (Claude): kép-ID, verzió, jóváhagyás, a 9 csatolmány sorrendje.
   - Új: **1b kép = a V3 befoglalók szürke tömbképe** ugyanarról a kameráról.
   - A függeszték fotója nincs csatolva, mert az ML04 a képen kívül van.
2. **Közös FIXED blokk** (sablon v3.1 §1), szó szerint, a v1 promptból, egy kivétellel: a „Walls and ceilings: painted white…” mondat helyére **Astra V3 r1 felületkivétele** került (a W01–W04 tapéta, panel és front), szó szerint.
3. **Cam_02 helyiség-FIXED** (v3.1 §2), szó szerint.
4. **Philips Hue követelmény**, szó szerint.
5. **GEOMETRY v2 + V3 FRAME LAYOUT** (Claude): stílusonként külön blokk.
   - A V3 befoglalók képtéri helye Blenderrel vetítve: `04_renderek/A902_cam02_tomeg_v1/A902_Cam02_tomeg_V3_kepteri_v1.json`.
   - A tömbképek: `A902_Cam02_tomeg_S0x_V3_v1.png`.
6. **Stílusblokk:** Astra V3 r1 (PR #16, commit `be6b1f3`), szó szerint, kivéve a **„Light” bekezdést**.
   - Helyette **tesztre szóló** bekezdés áll: nappali fény, csak a meglévő, igazolt fénypontok, rejtett LED nincs.
   - Ok: Péter 01:49 és 02:06 – a V3 általános LED-tiltása nem jövőbeli szabály, de a tesztben V3.1-es LED-megoldást sem szabad kitalálni.
   - Az eredeti mondat a `_eszkozok/epites_v3teszt.json`-ban rögzítve van.
7. **RUN NOTES** (Claude):
   - a P902_24A tűrése (0,36–0,38 m a kanapéhát és a széktámla között – ne mozgassa a modell);
   - nincs anyagminta-fotó;
   - a hibás első kép nincs csatolva;
   - székméretek.

## Fájlok
| Fájl | Karakter | sha256 |
|---|---|---|
| `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A_V3_r1.prompt.txt` | 18 957 | `8a26bfad37d527c41e60c069276552d73d0d0a06a54f46bf05b4425c81f845ce` |
| `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A_V3_r1.prompt.txt` | 19 275 | `03966065d536df71ca6a40de0307e221d5b5c73d321066a463315b27416b785f` |

**Nem módosított források:**
- Astra V3 r1: `05_promptok/A902_S01_S02_Cam02_CREATIVE_UPGRADE_V3_r1.md` @ `be6b1f3`, sha256 `848739b4…a592`;
- v1 promptok: `KEP004_ChatGPT_Images_v1/A902_S0x_…_Cam_02_A.prompt.txt`, sha256 `9981b35c…` és `2961e872…`.

**Csatolmánycsomag** (Mac, nem kerül a repóba a termékfotók miatt): `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/probakor_v3teszt_2026-10-25/`.

## Futtatási megjegyzés
- **A prompt bevitele:** a fájlt rejtett fájlmezőn keresztül olvastam be a lapba (sha256-tal ellenőrizve), beillesztés-eseményként adtam át, majd a „Megjelenítés a szövegmezőben” paranccsal tettem a mezőbe. Így nincs kézi másolás.
- **Az S02-nél** a ChatGPT a szövegmezőbe helyezéskor azonnal elküldte az üzenetet. A beküldött szöveg utólag ellenőrizve azonos (+1 záró sortörés), a 9 csatolmány sorrendben megvan.
- **A következő futtatásnál:** a mezőbe helyezés után nincs további kattintás, amíg a tartalom ellenőrzése le nem futott.
