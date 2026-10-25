# Opus 5.5 V3.1 – integrátori szövegcsere v1.2 (K-02, K-03) a négy induló promptra – végleges forrás (PR #22 @ 7d3c67f)

**Claude integrátor, 2026-10-25.** A versenyzői fájlok (PR #22 ága) és a stílusok eredeti dokumentációja (`10_STILUS_SPEC`) **változatlanok**. Ezek a renderpromptok javított másolatai. Régebbi termékválasztás nem került vissza: az S02 a végleges Westwing Dancing (ML05) és Kave Home Idela (ML04) lámpát tartja. **Végleges renderengedély nincs** (lásd az átadási csomagot).

## Forrás
- Commit: `7d3c67f823c646d9daef06b294826e89c1c61467` (`competition/opus55-v3-1-20261025`, CP14 + naplózárás, 2026-10-25 06:51). A szkript közvetlenül ebből a git-objektumból olvas (`git show 7d3c67f:…`), nem munkamásolatból.
- A b24bee7 → 7d3c67f diff: az S01 Cam_02 és Cam_12 azonos; az S02 Cam_02 és Cam_12 eltér (lámpák). A b24bee7-alapú v1.1 ezért csak tervezet: `../KEP004_OPUS55_V3_1_INTEGRATOR_PATCH_v1_1_TERVEZET_b24bee7/`.

## Cserék (pontos egyezés, mindegyik pontosan egyszer)
| Kép | Lelet | Régi szöveg (7d3c67f) | Új szöveg |
|---|---|---|---|
| S01 Cam_02 | K-02 | „The dining pendant at ML04 – the Kave Home Somar, Ø 76 cm, in pale synthetic fibre with fine steel rods – glows at the right edge.” | „The dining pendant at ML04 hangs outside this frame: do not draw any pendant at the right edge; at most a faint warm spill of its light reaches the right edge of the floor and the table.” |
| S02 Cam_02 | K-02 | „…; at the right edge the dining pendant at ML04, the Kave Home Idela pendant, Ø 26 cm smoked glass with a black marble detail, glows warm.” | ugyanaz, mint fent (külön mondatként) |
| S01, S02 Cam_02 | K-02 | „Avoid these proven errors: …” | a lista elejére: „a pendant lamp drawn at the right edge or anywhere above the dining table;” |
| S01 Cam_12 | K-03 | „One tall dark-leafed plant in a matt black pot stands in the south-west corner beside W02, away from the camera position.” | törölve |
| S02 Cam_12 | K-03 | „A tall olive tree in a matt cream pot stands in the corner beside W02, not in the walkway.” | törölve |
| S01, S02 Cam_12 | K-03 | „Avoid these proven errors: …” | a lista elejére: „a plant, tree or any object standing in front of W02 or in the mouth of the bedroom corridor;” |

Más szöveg nem változott (soronkénti diff: fájlonként két csere).

## Verziók
| Kép | Forrás sha256 (7d3c67f) | Javított `_v1_2` sha256 | Karakter |
|---|---|---|---|
| `A902_S01_KyotoInk_1_nappali-hero_Cam_12_A` | `914f0b9e8f0cc620…` | `95a34f6998b5fec723f7d1f275f3ce959c970c59807bfc8ce08d328494e9bfa1` | 5629 → 5601 |
| `A902_S01_KyotoInk_1_nappali-terasz_Cam_02_A` | `7096e13f81621ea7…` | `68f66d63581ff31e18fd0ee267eb8fcde2a942410473dabea812f1a691846651` | 6168 → 6299 |
| `A902_S02_BiBoNocturne_1_nappali-hero_Cam_12_A` | `0a1b8cbf9ba14df5…` | `c89b71d1a2f94f60fdbe3c52d0c3422de2ed2ee20020175b35d4cba275f9037e` | 5253 → 5256 |
| `A902_S02_BiBoNocturne_1_nappali-terasz_Cam_02_A` | `91b2ffb3128d8633…` | `bc8b73e6867d9d296ec43d1325771ebfa5e0a8c6cc2d0eb71ff78f2acefa7e99` | 5782 → 5908 |

Újrafuttatás: `python3 -I apply_patch_v1_2.py <wsg-berendezes repó> <kimeneti mappa>`. A szkript leáll, ha egy régi szöveg nem pontosan egyszer szerepel.

## Nem része (nyitva)
- **K-02 a többi 8 stílus Cam_02-jében** (S03–S10): regisztrálva az auditban (pontos mondattal), de javított példány nem készült – nem részei az induló csomagnak.
- **K-03 a stílusdokumentációban és az S04 Cam_12-ben:** a `10_STILUS_SPEC` érintetlen (Péter kérése); az S04 Cam_12 olajfája nyitott.
- **K-05:** az S02 ML04 Kave Home Idela foglalata nem igazolt (Opus is FELTÉTELES-nek jelöli; az Idela asztali lámpa G9-es).
- **K-06:** a fekete Toni 160 × 90 igazolása.
