# A-902 – validátor-nyilvántartás: figyelmeztetések és ismert régi hibák (kameracsomag C, 2026-10-25)

**Kérés:** Péter, 2026-10-25 04:39 – a validátor figyelmeztetései és a régi szaniterhibák külön dokumentálandók.
- **Lock:** v2b-1-k13. **Blend:** `e01170d3…` (draft PR #20).
- **Fontos:** a figyelmeztetés nem hiba (a validátor PASS), de minden terv integrálásakor kezelni kell.

## 1. Régi, ismert hibák – „referencia” mód (beépített szaniterek), nem a kameracsomag tárgya
A k12-ben és a k13-ban ugyanez a 6 hiba és 3 figyelmeztetés áll fenn. Csak a fürdő-modellt érinti, a nappali–étkező–konyhát nem.

| # | Elem ↔ fal | Átfedés | Valószínű ok | Teendő |
|---|---|---|---|---|
| E1 | Torolkozoszarito_06_1 ↔ Fal_05_2_furdo_0 | 3,0 cm | a szárító mélysége vagy tengelye a falba ér a modellben | hétfői fotó, mérés: a modell igazítása |
| E2 | Zuhanytalca_06_2_182x85 ↔ Kulso_K_06_2_0 | 3,0 cm | 182 × 85-ös tálca, a helyiség keleti fala a modellben 3 cm-rel beljebb | mérés |
| E3 | Zuhanyuveg_06_2 ↔ Kulso_K_06_2_0 | 2,0 cm | ugyanaz | mérés |
| E4 | Mosdo_06_2 ↔ Kulso_K_06_2_0 | 10,0 cm | a mosdó helye vagy mélysége bizonytalan | mérés, fotó |
| E5 | WC_tartaly_06_2 ↔ Akna_06_2 | 2,0 cm | az akna befoglalója közelítő | mérés |
| E6 | WC_tartaly_06_2 ↔ Fal_06_2_D_v2b | 2,0 cm | ugyanaz | mérés |
| W1–W3 | zuhanytálca, üveg, mosdó „kilóg a helyiségből” | – | az E2–E4 következménye | – |

**Hatás:**
- A Cam_10 (fürdő 06.2) a meglévő burkolattal és szaniterekkel dolgozik, ezért ezek a hibák a képi kontrollt 2–10 cm-es pontossággal érintik.
- A nappali–étkező–konyhai versenyt nem érintik.
- Javítás: a hétfői helyszíni mérés után, külön PR-ben.

## 2. Figyelmeztetések a C elrendezés tömbjeivel (minden versenyterv integrálásakor kezelendő)
| Kiállás (TERV SZERINT) | Hol | Mi kerül elé | Teendő a tervben |
|---|---|---|---|
| D16, D17 dugalj; G08 antenna | W01, x 3,69, y 6,17–6,33 | alsó TV-szekrény vagy sík panel | kivehető vagy szellőző hátfal; panelnél kivágás vagy szervizajtó |
| G01–G04 gyengeáramú aljzatok | W01, x 3,91–4,03, y 6,11–6,44 (a doboz helye a rajzon bizonytalan) | alsó TV-szekrény | hátfal-kivágás, kábelút; helyszínen mérendő |
| D18 dugalj | W01, y 4,75 | déli magas szekrény (60 cm) vagy sík panel | szervizkivágás; a rejtett LED tápegységének is lehetséges helye |
| TV-képernyő ↔ északi magas szekrény | próbatömb (szekrények: y 4,25–5,05 és 6,85–7,65) | 75"-os képernyő | a középső mező legyen legalább 1,75 m, vagy 65–70"-os TV |

**Kerek asztalos próbák** (`validator_v2b1k13_kerek_*.json`): PASS 0 hiba.
- R1/R2: 4 figyelmeztetés (D16, D17, D18, G08 a sík panel mögött).
- R3: 7 figyelmeztetés (a TV-alsószekrény, mint fent).

## 3. Ami nem validált (helyszín, hétfő 2026-10-26)
- teraszajtó: melyik szárny nyílik;
- az üvegfal kávájának mélysége (függönysín);
- a TV-csatlakozók tényleges helye;
- a parketta dekorja;
- a fürdő 06.2 szaniterei (1. pont).
