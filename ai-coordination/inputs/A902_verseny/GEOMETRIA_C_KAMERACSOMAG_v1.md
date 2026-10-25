# A-902 – közös geometriai bemenet a tervversenyhez: C elrendezés + kamerák (v1, Claude, 2026-10-25)

**Kinek:** Astra, Fable és Opus – mindhárom versenyzőnek azonos.
- Kiegészíti a közös §0 blokkot (`ai-coordination/requests/WSG-20261025-DESIGN-CHALLENGE-2026_KOZOS_BLOKK_v1.md`, PR #19).
- Részletek és bizonyítékok: `ai-coordination/results/WSG-20261025-A902-KAMERACSOMAG-C_r1.md`.
- **Státusz:** terv szerinti geometria, helyszínen nem mért. A kamerák JAVASLAT státuszúak, amíg Péter a kameracsomagot jóvá nem hagyja.

**Elv:** a régi Blender-bútortömbök nem kreatív korlátok. Ami alább szerepel, az valós geometriai és használati szabály. Ezen belül a forma, az anyag és a termék szabad.

## 1. Kötött
| Mi | Érték |
|---|---|
| Étkező | 160 × 90-es asztalbefoglaló, hosszanti, x 8,00–8,90; y 5,40–7,00; hat hely 2+2+1+1 (oldalszékek tengelye y 6,10 és 6,70; végszékek: dél és észak); az ML04 függeszték 0,12 m-re az asztal közepétől |
| Kanapé | L vagy U (minimum L, inkább U); a háttámla legfeljebb x 6,67 (L) / 6,60 (U); a kanapé legközelebbi pontja és a TV-fal bútora között ≥ 0,60 m |
| Közlekedés | fő utak ≥ 0,90 m betolt székkel (terasz, konyha, hálók folyosója, 05.3 ajtó); székkihúzás ≥ 0,90 m |
| TV-fal (W01, x 3,67) | zárt szekrénytest legfeljebb 60 cm mély (felső lehetőség, nem kötelező); ≤ 4 cm-es panel a mennyezetig. A TV maga a falsíkon vagy a fülke hátfalán (képernyő x ≈ 3,77, nézőtáv 2,3–2,4 m). Ha a TV egy 60 cm-es szekrény elejére kerülne, a nézőtáv 2,0 m alá esne → kerülendő. |
| TV-tengely | a TV-csatlakozók (G01–G04, D16, D17, G08) y 6,11–6,44 között vannak (TERV SZERINT). A TV és a középső mező ehhez igazodjon. |
| Szervizhozzáférés | D18 (y 4,75), D16, D17, G01–G04 és G08 előtt kivehető vagy szellőző hátfal, szervizkivágás |
| **A Cam_12 miatt** | a TV-fal északi végén (y 7,65–8,05) nincs mennyezetig érő szekrény; ott alacsony (≤ 0,90 m) elem vagy ≤ 4 cm-es panel. A kamerahely (x 4,30–4,50; y 7,75–8,05) környékére nem kerül magas bútor vagy állólámpa. |
| Függöny | a nappali üvegfal előtt a sín a szemöldök belső síkján vagy a kávában (mélység: hétfőn mérendő); mennyezeti hűtő-fűtő mezőbe nem fúrunk |

## 2. Kamerák (lock v2b-1-k13 JAVASLAT)
| Kamera | Hely [x; y; z] | Irány | Optika | Fény | Mit mutat |
|---|---|---|---|---|---|
| **Cam_12** nappali hero v3 | [4,40; 7,88; 1,60] | θ −48° (délkelet), vízszintes | 22 mm, shift_y −0,05 | kék óra / este, Hue | előtérben a kanapé eleje (a kép kb. 16–23 %-a); az étkező az ML04-gyel; a konyha; a W03 a 05.3 ajtóval; a W02 (fő felület); a W07. A TV-fal és a terasz nem látszik. |
| **Cam_03** K1 | [9,45; 7,55; 1,50] | dél, vízszintes | 20 mm, shift_y −0,08 | nappal | a két konyhai pultsor, a hűtőoszlop (D13), a déli magas elemfal; jobb előtérben az étkező és az ML04 (a lámpatest közel, a kép része) |
| Cam_02 (változatlan) | [8,30; 4,40; 1,55] | északnyugat | 20 mm | nappal | TV-fal és terasz – geometriai kontroll |

## 3. Helyszínen ellenőrizendő (hétfő) – most ne találd ki
- **A teraszajtó nyíló szárnya.** Ha csak a legkeletibb, 0,93 m-es tábla nyílik, az északi végszék pótszék lesz (5 fix + 1).
- **A káva mélysége** a függönysínhez.
- **A TV-csatlakozók tényleges helye.**
- **A parketta dekorja** (NEM IGAZOLT).
