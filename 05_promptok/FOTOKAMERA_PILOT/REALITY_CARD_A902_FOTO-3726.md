# Reality card – A-902 · fotókamera KZS_3726-506 · S01 Kyoto Ink pilot (2026-10-25)

**Cél:** módszerpróba – meg tudja-e tartani a ChatGPT Images a valós fotót, ha csak bútort teszünk rá (A szint, `FOTOKAMERA_LATVANYTERV.md`). **Státusz: KONCEPCIÓ – NEM VALIDÁLT.** Jóváhagyás: Péter, 2026-10-25 19:32 („aha próbálhatjuk”), egy kép.

| | |
|---|---|
| Bemenet | `08_allapotfelmeres/fotok_profi_20261025/A902/KZS_3726-506.jpg`, 2400 px-es munkapéldány a csomagban (Mac: `~/Downloads/WSG/KEP-004/03_chatgpt_images_csomagok/FOTOKAMERA_PILOT_2026-10-25_A902_3726/`) |
| Nézet | 03 étkező / 04 nappali → É, teraszüveg (4,50 m, tolórész jobbra), 05.3 ajtó jobbra hátul; a kamera a nappali déli részén, a TV-fal (W01) a bal szélen kívül |
| Eszköz | ChatGPT Images (Péter Plus-fiókja, Chrome), egy generálás |
| Prompt | `A902_S01_KyotoInk_FOTO-3726_etkezo-terasz_A.prompt.txt` (sha256 `c8c6aac07b7df8ef…`) |

## Felületek
| Felület | Állapot | Forrás |
|---|---|---|
| Padló | MEGLÉVŐ – Egger Grey Treviso Oak EL2184, a fotó szerint | ADAT_STATUSZ, fotó |
| Falak, mennyezet | MEGLÉVŐ – fehér; az S01 tapéta (W01/W04) ebben a próbában szándékosan **nincs** rajta, hogy a hűség mérhető legyen | – |
| Nyílászárók, terasz, kilátás | MEGLÉVŐ, a fotó szerint | fotó |
| 05.3 ajtó, kapcsolók | MEGLÉVŐ, szabadon | fotó |

## Új elemek (C elrendezés, GOAL 2026-10-25 04:08)
| Elem | Termék | Méret | Státusz |
|---|---|---|---|
| Kanapé | Westwing Lennon L jobbos, taupe | 238×180×68 | S01 terméklista (Astra V3) – ár itt nincs újraellenőrizve |
| Étkezőasztal | Westwing Toni ovális, világos tölgy | 160×90×75 | ua. |
| Székek | 6 × Kave Home Eamy világosszürke | 55×53×75 | ua. |
| Függeszték | Kave Home Somar Ø76 az ML04-en | Ø76 | ua. |
| Szőnyeg | Kave Home Nifelia | 200×300 | ua. |

**Nem része a próbának:** Blender-kameraillesztés és méretvezető (az B szint), költségkapu, TV-fal-együttes (képen kívül), terasz-bútor.

## Ellenőrzés a kép után
`_eszkozok/foto_huseg.py`: az üres fotó és az eredmény összevetése a bútor nélküli zónákban (mennyezet, teraszüveg és kilátás, jobb fal és 05.3 ajtó, kapcsolók): színeltolódás, élek egyezése, eltéréstérkép. Eredmény: `RESULT_FOTO-3726_A.md`.
