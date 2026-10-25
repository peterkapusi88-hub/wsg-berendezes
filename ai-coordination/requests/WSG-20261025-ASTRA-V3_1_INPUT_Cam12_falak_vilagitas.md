# Astra V3.1 – bemenet: hero kamera (Cam_12), látható falszakaszok, összekötő fal, rejtett LED műszaki kerete

**Task ID:** WSG-20261025-V3_1-INPUT · **Készítette:** Claude, 2026-10-25 03:00 (CEST) · **Cél:** Astra V3.1 (Work)

**Ez bemenet, nem feladatindítás:**
- Work-futást nem indítok. Az indítás Péteré; Ultra/Max munka és extra kredit csak az ő engedélyével.
- Generálási engedélyt nem ad.
- Forrás: Péter 01:39, 01:49, 01:58, 02:06 (GOAL 7. pont).

## 1. A hero kamera – Cam_12_Nappali_Hero (JAVASLAT v2, draft PR #17)
- **Hely:** az ÉNy-i sarok, [3,95; 7,90; 1,45] – a TV-fal és a teraszüveg találkozásánál.
- **Irány és optika:** délkelet felé, vízszintes kamera (a függőlegesek egyenesek), **22 mm**, shift_y −0,08, 1600 × 1000.
- **Képek** (PR #17 ág `kep004/cam12-nappali-hero-javaslat`, a beolvasztásig ott):
  - alapkép: `04_renderek/A902_cam12_hero_javaslat/A902_Alap-v2b1k12_blender_12_nappali-hero_JAVASLAT.png`;
  - V3 tömbképek: `…/A902_Cam12_tomeg_S01_V3_v2.png`, `…_S02_V3_v2.png`;
  - jelöltek és felülnézet: `…/jeloltek/`;
  - indoklás: `…/CAM12_JAVASLAT_v2.md`.
- **Nem látszik:** a TV-fal (W01), az üvegfal és a terasz – ezeket a Cam_02 mutatja.
- **Látszik:** előtérben a kanapé eleje; az étkező a függesztékponttal (ML04: u 0,21, v 0,05 – **az étkezőlámpa a hero képen látszik**); a konyha pultfala.
- **A kamera helye:** a sarokba (x < 4,40; y > 7,70) ne tervezz magas szekrényt.

## 2. A Cam_12-n ténylegesen látható falszakaszok
Mérés: ray cast a v2b-1-k12 modellen, csak építészet, valamint S01/S02 V3 tömbbel. Forrás: `03_blender/geometry_v2/cam12/cam12v2_ellenorzes_log.json` (PR #17).

- **u:** képtéri helyzet balról (0) jobbra (1).
- **Látható arány:** a falfelület látható része, bútor nélkül / S01 tömbbel / S02 tömbbel.

| ID | Falszakasz (terv szerint) | Méret | u | Látható arány | Kiállások a felületen (TERV SZERINT) | Megjegyzés |
|---|---|---|---|---|---|---|
| **W03-a** | keleti fal az étkező mögött, x 10,75; y 5,05–6,05 | 1,00 × 2,90 m | 0,15–0,25 | 100 / 86 / 87 % | **K07–K09 + D12** (y 5,65), **D13 hűtődugalj** (y 5,20, lent) | A terv **hűtőhelyet** jelöl itt (D13, „H”). **Konyhabútor nincs** → a hűtőszekrény-oszlop és a falkezelés együtt tervezendő |
| W03-ajtó | **05.3 szürke ajtó** + szemöldök, y 6,05–6,95 | 0,90 × 2,10 + 0,80 m | 0,05–0,15 | 94 / 76 / 76 % | – | Az ajtó, a tok és a kilincs változatlan. A szemöldöksáv (z 2,10–2,90) kezelhető |
| W03-akna | az akna nyugati lapja, x 9,80 | csak 0,25 m-es csík | 0,01–0,05 | 27 % | – | A bal szélen; a Cam_03-on teljesen látszik |
| **K-csonk** | konyhacsonk, x 10,55; y 4,10–5,05 | 0,95 × 2,90 m | 0,26–0,34 | 100 / 86 / 81 % | **D14 mosógép** (y 4,15) | A konyha része |
| **K-pultfal** | a konyha keleti fala, x 10,55; y 1,35–4,10 | 2,75 × 2,90 m | 0,34–0,50 | 90 / 85 / 86 % | D02, D03, D06, D07 pultdugalj; D04 mosogatógép; **FL01 fali lámpakiállás** (y 3,15) | **A hero képen a konyhabútor látszik:** front, munkalap, hátfal. Stílusonként a Cam_03-mal azonosan tervezendő |
| **W02** | a nappali déli tömör fala, y 4,05; x 5,20–7,30 | **2,10 × 2,90 m** | **0,54–0,81** | 100 / 100 / 92 % | **kapcsolóoszlop x 7,149:** K10–K12, T01 termosztát, S01 mozgásérzékelő, D19 dugalj | **Az „összekötő fal” fő felülete:** a hero kép jobb közepén, szinte szemből. V3: S01 KI3-A vászon 100×180 + tapéta; S02 BN3-A grafika 120×160 + tapéta |
| **W07** (új ID) | **a hálószobai közlekedő torka:** az x 5,20-as visszafordulás (y 3,45–3,95 látszik), a pillér (x 5,00–5,20; y 2,95–3,45) és a közlekedő déli fala (y 2,75; x 4,50–5,00) | kb. 0,5 + 0,5 + 0,5 m látható szélesség, 2,90 m magas | 0,82–0,99 | 44 / 100 / 37 % | **K25–K27 + D46** a sarokban (x 5,184; y 3,90) | A W02 folytatása a hálók felé. A közlekedő 1,20 m széles; a 06.1 fürdőajtó tokja x 4,574-nél |

**A Cam_02-n** (kontrollnézet, V3 r1) a W01 (TV-fal) és a W04 (a teraszüveg körüli tömör pillérek és szemöldök) látszik.

## 3. Kötelező kreatív igény: a hálókhoz vezető összekötő fal (Péter, 01:58)
- **Felületek:** W02 (fő felület) + W07 (a közlekedő torka). Egy gondolat legyen, stílusonként: tapéta, dekorpanel, egyedi grafika, textilpanel, később igazolt rejtett LED-del.
- **Nem lehet véletlenszerűen csupasz.** A V3 r1 W02-es vászna/grafikája önmagában nem elég, ha a fal többi része és a W07 kezeletlen marad.
- **Változatlan:**
  - a fal, az ajtók (06.1 tok), a kapcsolók és a közlekedők helye és mérete;
  - a W02 kapcsolóoszlopa (x 7,149): a kezelés a kapcsolóktól legalább 10–15 cm-re álljon meg, vagy körbevágva hagyja szabadon őket;
  - a K25–K27 + D46 a közlekedő sarkában szabadon marad.
- **A közlekedő nem szűkülhet indokolatlanul.**
  - A torokban és a közlekedőben legfeljebb kb. 2–3 cm vastag kezelés (tapéta, ≤2 cm panel vagy grafika).
  - Mélyebb rendszer (LED-es panel, polc) csak a W02 nappali felőli síkján.
- **Költség:** stílusonként egy fő és egy gazdaságos változat, bruttó sávval. Astra-becslés, ajánlat nélkül; Claude független ellenőrzése utána.

## 4. Rejtett, Hue-integrálható LED – műszaki keret (Péter, 01:49)
**Szabályok (CLAUDE.md, GOAL):**
- Fény és áram **csak meglévő kiállásra**, falvésés nincs.
- A mennyezeti hűtő-fűtő mezőbe nem fúrunk. A nappaliban a HF03 mező x 3,77–9,80, y 4,05–8,05 – szinte a teljes mennyezet.
- Rögzítés falra vagy szerelt takaróelemre.
- Ingyenes vagy már meglévő rejtett kiállást nem feltételezünk.
- Hue: minden általános és dekoratív fény igazoltan Hue-kompatibilis.
  - Eredeti Philips Hue lightstrip, vagy profilos 24 V LED + **gyártói dokumentummal igazolt** Hue-kompatibilis vezérlő.
  - Kivétel: a szekrénybelső funkcionális fénye.

| Zóna | Táp (TERV SZERINT) | Tápegység / vezérlő helye | Rögzítés, kábelút | Megítélés |
|---|---|---|---|---|
| TV-/tárolófal (W01): a szekrény alatt/fölött, a TV mögött, súrolófény a KI3-P/BN3-P síkon | D16, D17 (a TV-szekrény mögött); D18 (a magas szekrény mögött) | az alsó szekrény szellőző szervizrekeszében; a toronyban (D18) | A ≤4 cm-es panelszél és a szekrénylábazat ad helyet; a kábel a panel mögötti csatornában fut | **Megvalósítható.** Feltétel: a D18 szervizkivágása és a szellőzés |
| Fal–mennyezet indirekt fény a W01-en | **FL02** fali lámpakiállás (x 3,684; y 7,849; z 2,85) | a takaróléc mögött vagy a magas szekrényben | falra szerelt párkány/takaróléc z ≈ 2,60–2,80 között, a mennyezetet nem érinti | **Megvalósítható, villanyszerelővel.** Az FL02 áramköre és kapcsolója a rajzon nem azonosítható → helyszínen ellenőrizni. Hue-hoz állandó tápellátás kell (Hue fali kapcsolómodul) |
| Függöny mögötti indirekt fény (üvegfal, x 4,44–8,94) | **D15** (x 4,24; a nyugati pillér, lent), **D11** (x 9,09; a keleti pillér, lent) | a pillér melletti függönytakaró végében | Takarólécdoboz a szemöldök (y 8,05; z 2,53–2,90) belső síkjára | **Feltételes.** (1) A dugaljtól a szemöldökig kábelút kell, a pillérnél látható takarócsíkkal vagy a függönycsomag mögött. (2) Az R01/R02 motoros redőny szervizfedele nem takarható. (3) S02: a U északi vége 0,225 m-re van az üvegsíktól, ezért a függönycsomag szűk – ott áttetsző, vékony függöny vagy a U déli irányú eltolása kell |
| Súrolófény a W02 (összekötő fal) / W07 panelen vagy tapétán | **D19** (W02 keleti vége, lent), **D46** (a közlekedő sarka) | panelmögötti rekesz vagy lábazati doboz | csak **teljes magasságú panel vagy függőleges takarócsík** mögött vihető fel a kábel | **Feltételes.** Csak tapéta esetén nincs rejtett kábelút → alsó súrolófény a lábazatból, vagy panelos megoldás |
| Az étkező mögötti fal (W03-a) | **D12** (y 5,65) | a hűtőoszlop takaróelemében vagy polc mögött | a hűtőoszlop és a kapcsolósor között ~0,4 m szabad falsáv | **Szűk.** Inkább a hűtőoszlop/konyhai magasszekrény integrált fénye (szekrénybelső: lehet nem Hue) + az ML04 Hue-függeszték |
| Lábazati fény (TV-szekrény, konyha) | D16/D17; a konyhai pultdugaljak | a lábazat mögött | lábazati profil | Megvalósítható |
| Master fejvégfal és gardrób | D20–D23 (z 0,65, az ágy két oldalán); K13/K14 | a fejvégpanel mögött / a gardróbban | fejvégpanel hátsó fénye; gardrób: funkcionális (nem Hue is lehet) | Megvalósítható. A K13/K14 nem takarható (lásd a k11b riportot) |

**Nem fér bele, alternatívával:**
- **Mennyezeti süllyesztett vagy rejtett sín:** nem lehet (HF-mező) → falra szerelt párkány az FL02-ről.
- **Fal–mennyezet fény a W02/W03/W07 falon:** nincs felső kiállás → csak panelben vezetett kábellel, különben lábazati vagy alsó súrolófény.
- **Függönyfény az S02 U mellett:** szűk → vékony függöny, vagy csak a nyugati szakaszon.

**Költség (Astra árazza V3.1-ben, Claude független ellenőrzése után):** Hue-szalag és -toldás folyóméterre, tápegység, vezérlő, Hue fali modul, alumínium profil + diffúzor, takaróléc/párkány (asztalos), villanyszerelői óra (FL02), a Hue Bridge megléte.
- **Nagyságrend, becslés, nem ellenőrzött:** A-902 egész lakásra kb. 0,5–1,0 M Ft bruttó, 20–30 m szalaggal.
- A 18 M Ft-os keret nem nő, a 2 M tartalék érintetlen → ezt más tételből kell kigazdálkodni. A V3.1 mutassa meg, mi esik ki helyette.

## 5. Elrendezési adatok a hero promptokhoz (Cam_12, Blenderrel vetítve)
Képtéri befoglalók: u balról, v felülről, a kép arányában.

- **S01:**
  - Lennon L: a fő ülőrész u 0–0,42 (v 0,66–1,0), a chaise u 0,32–0,69 (v 0,61–1,0), a hát u 0–0,47 (v 0,55–0,80);
  - Toni lap u 0,03–0,38 (v 0,50–0,59), székek u 0,03–0,40;
  - KI3-A a W02-n u 0,57–0,69 (v 0,10–0,53).
- **S02:**
  - U: a hátsó ülőblokk u 0–0,58 (v 0,60–1,0), a déli kar u 0,46–0,68 (v 0,65–0,93), az északi kar u 0–0,36 (v 0,80–1,0);
  - Anouk u 0,05–0,37 (v 0,50–0,59);
  - BN3-A a W02-n u 0,57–0,71 (v 0,13–0,52).
- A TV-fal elemei (KI3/BN3) a képen kívül vannak.

## 6. Nyitott döntések (Péter)
1. **A Cam_12 és a Cam_03 átfedése.** Ugyanabból a sarokból néznek, 14°-kal elforgatva. Vagy mindkettő marad, vagy a Cam_03-at a konyhára irányítjuk.
2. **Kanapéhát – nyugati széktámla:** 0,36–0,38 m. Marad, vagy az étkező 0,15 m-rel keletre kerül.
3. **D18 szervizkivágás** a magas szekrényben (S01 és S02).
4. **A konyhabútor** (nincs gyári) a hero és a Cam_03 közös eleme: a V3.1 stílusonként adja meg (front, munkalap, hátfal, hűtőoszlop a W03-a előtt).
