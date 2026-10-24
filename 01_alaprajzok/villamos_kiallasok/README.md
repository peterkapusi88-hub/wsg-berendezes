# Villamos kiállások – A-811, A-812, A-902 (TERV SZERINT, 2026-10-24)

**Mire való:** minden mennyezeti és fali lámpakiállás, kapcsoló, dugalj, gyengeáramú aljzat és mennyezeti hűtő-fűtő mező helye lakásonként, méterben. Ebből tervezünk lámpát, LED-et, bútort és falpanelt úgy, hogy **új kiállás, vésés és fúrás ne kelljen** (Péter, 2026-10-24).

Gyors áttekintés: **`OSSZESITO.md`**. Tételes adat: `<LAKÁS>_villamos.csv` / `.json`. Ellenőrző kép, 1 m-es rácson: `<LAKÁS>_villamos_atfedes.png`.

## Forrás és verzió
| Lakás | PDF-oldal | Rajz | Lépték | Érvényes változat |
|---|---|---|---|---|
| A-902 | 18. (dosszié 176) | Alaprajz M1 KORR 2 | 1:50 | rajz 2025.12.15., kiküldve 2025.12.18. Tartalmazza a 2025.10.13-i teraszfellépés-korrekciót és a 12.15-i „02 Konyha »d« kapcsoló változás”-t (váltókapcsoló, nem keresztkapcsoló). |
| A-811 | 5. (dosszié 150) | Alaprajz M1 | 1:50 | KORR-alaprajz nem készült. |
| A-812 | 12. (dosszié 179) | Alaprajz átnézeti M1 KORR | 1:100 | 2026.04.28. Az 1:50-es 11. oldal csak részlet, a teljes lakás az átnézeti lapon van. |

- **Forrásfájl:** `WGR1_meretezett_alaprajzok.pdf`, Péter összeállítása (2026.10.20.), sha256 `1a687246…9881`.
  - A fejlesztő M1/KORR rajzi mellékletei, Andrea egyeztetett vevői módosításaival.
  - Vevői adat, ezért **nincs a repóban**. A kinyerés a Mac Letöltések mappájából, Péter engedélyével történt.
- A lapokon ez áll: „a megvalósítás során a végleges méretek eltérhetnek”. Ezért minden tétel **TERV SZERINT**.

## Blender
Az A-902 kiállásai és hűtő-fűtő mezői a v2b modellben is megvannak: `A902_Villamos_TERV` gyűjtemény (renderben rejtve, nézetben látható), azonosítóval elnevezett jelölőkkel. Szkript: `03_blender/geometry_v2/add_kiallas_reteg.py`; ellenőrző felülnézet: `04_renderek/A902_alap_v2b/A902_Alap-v2b_blender_06_alaprajz-kiallasok.png`.

Az A-811-nek és az A-812-nek is van alaprajzi Blender-modellje (2026-10-24, ELŐZETES, draft PR). Az `A811_Villamos_TERV` és az `A812_Villamos_TERV` réteg ugyanígy épül:
- szkript: `03_blender/geometry_A811_A812/build_a8_modell.py`;
- ellenőrzés: `<lakás>_kiallas_reteg_ellenorzes.json`;
- felülnézet: `04_renderek/A811_alap_v1/`, `04_renderek/A812_alap_v1/`.

**A lámpajelölő magassága álmennyezetnél:**
- A-811: WC 2,40 (rajz); előtér és fürdők 2,40 (Péter összesítője).
- A-812: előtér 2,50 (rajz); fürdők 2,40.

## Koordináták
Egység: méter. x a rajzon jobbra, y a rajzon felfelé. Pontosság a rajzhoz képest ±1 cm (1:50), illetve ±2 cm (1:100).

**Origó lakásonként:**
- **A-902:** x=0 a 05.1 szoba homlokzati belső falsíkja, y=0 a 05.2 szoba alsó belső falsíkja. **Azonos a Blender-modellel** (`03_blender/WSG_A902_*`).
- **A-811:** x=0 a 04 nappali erkély felőli belső falsíkja, y=0 a 05.1 szoba rajzon alsó belső falsíkja.
- **A-812:** x=0 a 04 nappali erkély felőli belső falsíkja, y=0 a 04 nappali rajzon alsó belső falsíkja.
- Az A-811 és az A-812 rendszere azonos a Blender-modellel (`03_blender/WSG_A811_*`, `WSG_A812_*`, 2026-10-24).
- A 8. emeleti megvalósulási terv illesztése szerint a két lakás x-e közös, és y_A812 = y_A811 − 11,85: az A-811 felső fala az A-812 alsó fala.

**Mezők:**
- `x_m`, `y_m`: a rajzi jel középpontja. Mennyezeti lámpánál ez maga a kiállás helye.
- `doboz_x_m`, `doboz_y_m`: a fali szerelvénydoboz helye a falsíkon. **Fali eszköznél ez a fizikai hely.**
  - Ha több jel egy vezetővonalon ül (például kapcsolóoszlop, TV-blokk, ágy melletti kapcsoló + dugalj), mind a vezetővonal falnál lévő végére kerül.
- `magassag_m`: szerelési magasság a padlótól. Csak ott van kitöltve, ahol a rajzon „m=…” felirat szerepel.

**Helyiség-hozzárendelés:**
- Az A-902-n a Blender-geometria helyiségein alapul.
- Az A-811-en és az A-812-n kézzel rögzített, közelítő téglalapokon (a koordináta a mérvadó).
- A modell pontos helyiségkontúrjai a `geometry_lock_A811/A812.json` `rooms` kulcsában.

## Jelkulcs – mennyire biztos
A lapokon ez áll: „Jelmagyarázatot lásd mellékletben!”. Maga a jelmagyarázat **nincs** a feldolgozott PDF-ben, és a vevői **műszaki mellékletben** (`WGR1_műszaki melléklet.pdf`, 2024.02.13., Péter engedélyével átnézve, nincs a repóban) sincs. A melléklet szövege viszont több jel jelentését igazolja – ezek az alábbi táblában „műszaki melléklet (2024.02.13.)” forrással szerepelnek.

| Jel | Jelentés | Biztonság |
|---|---|---|
| ⊗ kör + X, kisbetűvel | mennyezeti lámpakiállás, a betű az áramkör | IGAZOLT (a módosítási szöveg így hivatkozik rá, pl. „»h« mennyezeti lámpakiállás”) |
| félbevágott ⊗ a falon | fali lámpakiállás (falikar), pl. A-902 nappali 2,85 m, A-811 nappali 2,65 m | IGAZOLT (a módosítási szöveg alapján) |
| kis kör szárral, betűvel | kapcsoló; a betű a kapcsolt áramkör | IGAZOLT |
| félkör a falnál | dugalj; kódok: P pult, H hűtő, MG mosogatógép, Mi mikró, S sütő, EL elszívó, M mosógép, SZ szárítógép, TSZ törölközőszárító, B fürdőszobai (tükör melletti) | IGAZOLT a felsoroltakra, a „B” jelentése NEM IGAZOLT |
| S/F kör | főzőlap/sütő fix bekötése | VALÓSZÍNŰ |
| M körben | falon kívüli elszívó ventilátor; páraérzékelős vagy a világításról kapcsolt; a betű a kapcsoló áramkör | IGAZOLT (műszaki melléklet (2024.02.13.): „falon kívüli légelszívó berendezések … a fürdő és WC helyiségekbe”) |
| ⊓ 1 / 2 / 3, illetve BK a TV-blokkban | informatikai aljzat (RJ45, CAT5E – tv/telefon/internet); minden lakóhelyiségben egy blokk | a jel jelentése VALÓSZÍNŰ (műszaki melléklet (2024.02.13.): „minden lakóhelyiségbe kerül egy-egy informatikai blokk … CAT5E”); az 1/2/3 és a TV-blokkon belüli BK kód jelentése NEM IGAZOLT |
| önálló BK doboz (kisebb felirattal) | a riasztó központi egységének előkészített helye | VALÓSZÍNŰ: az A-811 módosítási szövege szerint a 05.2-3 összevonásakor „a biztonsági központ áthelyezésre kerül”, és az A-811 egyetlen önálló BK doboza a 05.2-3 gardróbjában van; műszaki melléklet (2024.02.13.): „központi és kezelő egység elhelyezés részére előkészítés” |
| négyzet + kör | TV/antenna aljzat | VALÓSZÍNŰ |
| R körben, minden ablaknál | motoros redőny (külső árnyékoló) kiállása a redőnyszekrénynél, nyílászárónként 1 | IGAZOLT (műszaki melléklet (2024.02.13.): „a redőnyszekrényeknél elektromos kiállás … nyílászárónként egy kiállással”; motor, palást, távirányító nem része az alapnak) |
| kupola hullámokkal | mozgásérzékelő (riasztó-elővezetékezés) | IGAZOLT: műszaki melléklet (2024.02.13.): „az erkéllyel, terasszal rendelkező lakóhelyiségek esetében mozgásérzékelős riasztó … elővezetékezés” – a jelek pontosan ezekben a helyiségekben vannak (az A-812 erkély nélküli szobáiban nincs); az A-811 módosítási szövege is így nevezi |
| billentyűzet, kaputelefon, ajtótok-eszköz, EL4, kék T | riasztó-kezelő helye, videós kaputelefon beltéri egység, riasztó-nyitásérzékelő a bejárati ajtón, lakáselosztó, hűtő-fűtő termosztát | kaputelefon és termosztát IGAZOLT (műszaki melléklet (2024.02.13.)); kezelő és nyitásérzékelő VALÓSZÍNŰ (a melléklet szerint a riasztó csak elővezetékezés, a kezelő helye előkészítve); EL4 VALÓSZÍNŰ |
| kék szaggatott átló | mennyezeti hűtő-fűtő mező; a téglalap az átló végpontjaiból, ±10 cm | VALÓSZÍNŰ (a felirat: „mennyezeti hűtés-fűtés”) |

A még nem igazolt kódok (1/2/3, a TV-blokkon belüli BK, a „B” dugalj, a négyzet + kör) a fejlesztőtől vagy a helyszínen tisztázhatók.

## Mire készült egy-egy kiállás
A rajzlapok „Elektromos módosítás (erős és gyengeáram)” blokkja megmondja, melyik kiállás miért készült. Lakásonként tömörítve az `OSSZESITO.md`-ben és a JSON `meta.modositasok_villamos` mezőjében. Tervezéshez a legfontosabbak:
- **A-902:** a 05.1-ben 1, a 05.3-ban 2 dugalj **szekrényvilágításhoz** készült – a gardrób LED-je ezekről megy, új kiállás nélkül. Melyik dugalj az, a rajz nem jelöli külön: helyszínen azonosítandó.
- **A-902:** a nappali falikarja (2,85 m) a 05.1 felé eső válaszfalon van; a „b” (étkező) és az „n,p” (nappali) mennyezeti kiállást a módosítás eltolta – a CSV a módosított helyet tartalmazza.
- **A-811:** a 05.2-3 „m” lámpája 3 helyről, a közlekedő „h” lámpája 3 helyről kapcsolható; a TV-blokk a 05.1-ben m=1,20 m.
- **A-812:** a 05.2 TV-blokkja m=1,20 m; a 08/09 fürdő „m” és „l” lámpája egy csillárkapcsolón van.
- **Lakáson kívül** mindhárom lakásnál: a szinti tárolóban (AT8-01/-02/-03) 2-2 dugalj, az egyik beállóban (P-0-65 / P-0-32 / P-0-33) autótöltő.
- **Álmennyezet** Péter átvételi összesítője szerint csak az előtérben, a WC-ben és a fürdőben van (min. 2,40 m). A rajz zöld „gk. álm.” feliratait az `OSSZESITO.md` lakásonként felsorolja; a pontos kiterjedés helyszínen ellenőrizendő.

## A vevői műszaki mellékletből (2024.02.13.) – tervezéshez
Péter engedélyével átnézve (2026-10-24); a dokumentum szerződésmelléklet, ezért **nincs a repóban**, csak az alábbi műszaki tények.
- **A mennyezeti hűtő-fűtő panelek a vasbeton födémbe integráltak** (nappali, étkező, hálószobák). A HF-mezőkbe fúrni ezért tilos; függeszték csak a meglévő ⊗ kiállásra.
- A melléklet szerint **kiegészítő fal- vagy padlóba épített hűtés-fűtés is készülhetett**, ahol a hőtechnika megkívánta. A rajzon csak mennyezeti mezőt találtunk; falra fúrás előtt (TV-konzol, polc) vezetékkereső, kétség esetén hőkamera fűtési üzemben.
- **A villamos vezetékek födémben, falban és padlóban, védőcsőben** futnak. Csavarozás, fúrás előtt vezetékkereső.
- **Minden lakóhelyiségben van informatikai blokk** (CAT5E, RJ45; tv/telefon/internet). Mesh Wi-Fi-pont, okos-otthon központ ezekre köthető.
- **Riasztó:** az alap csak elővezetékezés (bejárati ajtón nyitásérzékelő, erkélyes/teraszos szobákban mozgásérzékelő, központ és kezelő helye). Ha nincs beépítve, a dobozok vakon is szabadon maradjanak.
- **Redőny:** a műanyag nyílászárók redőnyszekrénnyel készültek, nyílászárónként 1 kiállással; a melléklet szerint a nyári hűtés csak külső árnyékolóval hatékony.
- **Elszívók:** falon kívüliek, a fürdőben és a WC-ben; páraérzékelős vagy a világításról kapcsolt.
- **Szerelvények:** Schneider vagy azzal egyenértékű. Belmagasság: 8. em. 2,70 m, 9. em. 2,90 m (±3 cm), álmennyezet alatt min. 2,40 m.

## Kötelező tervezési szabályok (minden AI-nak)
1. **Világítás és minden áramot igénylő elem csak meglévő kiállásra kerülhet.** Ezek a mennyezeti ⊗, a fali lámpakiállás és a dugalj. Új kiállás, vésés, falon kívüli új kábelezés **nincs**.
2. **Függeszték, csillár, mennyezeti lámpa csak a ⊗ kiállás helyére kerülhet.** Ha máshová kell fény: dugaljról táplált állólámpa vagy bútorba épített LED, illetve akkus lámpa.
   - Kiállástól eltolt függeszték mennyezeti rögzítést igényel, ezért csak Péter külön jóváhagyásával.
   - **A-902:** a nappali, étkező, konyha és a három háló mennyezeti kiállása (ML03–ML08) a hűtő-fűtő mezőn belül van. A lámpa rögzítése előtt ellenőrizni kell, van-e a dobozban rögzítési pont, és csőmentes-e a kiállás körüli sáv (hőkamera, fűtési üzemben) – hétfő.
3. **A hűtő-fűtő mezőkbe (HF) nem fúrunk.** Függönysín a szemöldökre vagy a falra kerül, a mezőn kívül. Máshol bútor, polc, TV-konzol rögzítéséhez fúrni szabad (Péter, 2026-10-24) – előtte vezetékkereső, a dobozok függőleges és vízszintes vonalában ne.
4. **Bútor, panel vagy tapéta nem takarhatja** a kapcsolót, a termosztátot, a lakáselosztót (EL4), a BK-dobozt, a kaputelefont, a riasztó-kezelőt és a mozgásérzékelőt (a szobaajtók sarkában is van; magas szekrény ne kerüljön elé).
   - A dugalj hozzáférhető marad.
   - Falpanelen és lamellán kivágás kell a doboz helyén (`doboz_x/y` + magasság).
5. **A TV helye szabad** (Péter döntése, 2026-10-24): a tartalom interneten jön, a TV-hez csak dugalj kell; a gyári TV-blokk (RJ45 + antenna) nem köti a helyét.
   - A TV-fal mellett vagy mögött legyen dugalj, a kábel bútorban vagy panel mögött fusson, vésés nélkül. TV + hangprojektor + médialejátszó: rejtett elosztó.
   - A TV-fal nem takarhat kapcsolót, termosztátot, mozgásérzékelőt (4. szabály).
   - Wi-Fi: a vasbeton födém és a falazóblokk falak csillapítanak. Ha a TV messze van a routertől, mesh-pont javasolt, amely a legközelebbi szobai RJ45 aljzatra köthető (minden lakóhelyiségben van egy).
   - Falra szerelt TV: a konzolhoz fúrni szabad (3. szabály), előtte vezetékkereső.
   - Dugalj a nappaliban (TV-hely jelöltek, a fali doboz helye):

     | Lakás | Gyári TV-blokk | További dugalj a nappaliban |
     |---|---|---|
     | A-902 | nyugati válaszfal, y 6,25–6,33 (D16, D17; RJ45 G01–G04, antenna G08) | déli fal x 7,15 a fő kapcsolóoszlopnál (D19 – a TV ne takarja a kapcsolókat); nyugati fal y 4,75 (D18); északi (terasz felőli) fal x 4,24 (D15) |
     | A-811 | a 05.2-3 felé eső fal, x 1,87–1,95 (D15, D16; RJ45 G01–G04, antenna G07) | erkélyfal y 10,59 (D14); felső fal (y 11,53) x 0,6 és 3,2 (D10, D11); kapcsolóoszlop x 4,97 (D17) |
     | A-812 | alsó fal, x 1,60–1,68 (D17, D18; RJ45 G01–G04, antenna G08) | alsó fal x 4,6 (D19); erkélyfal y 0,77 és 4,73 (D16, D14); felső falszakaszok: x 2,22 (D13), x 3,87 (D15) |
6. Minden renderen és tételes listán a lámpa, a TV és az áramot igénylő bútor **kiállás-azonosítóval** szerepeljen (pl. „függeszték → A902-ML04 »b«”).

## Frissítés
- **Újrakinyerés:**
  - `python3 kinyeres/villamos_kinyeres.py <helyi>/WGR1_meretezett_alaprajzok.pdf`
  - majd `python3 kinyeres/osszesito.py`
- **Helyszíni ellenőrzés:** a hétfői fotózás „mennyezet, panelek/kiállások” sorai alapján (`08_allapotfelmeres/FOTO_KAMERA_KAPCSOLAT.csv`).
  - Az eltérő tételek a CSV-ben **HELYSZÍNEN MÉRT** státuszt kapnak, a mért koordinátával és a fotó azonosítójával.
  - A tervi értéket megjegyzésben megtartjuk.
- **Azonosítók:** a már kiadott azonosító nem számozódik át. Újrakinyeréskor a szkript a korábbi JSON alapján megtartja (azonos típus, ≤3 cm); új tétel a következő szabad sorszámot kapja, megszűnt tétel száma nem kerül újra kiosztásra.
- **Tudott hiányok:**
  - a jelmagyarázat (a műszaki mellékletben sincs; a maradék kódok: 1/2/3, TV-blokkon belüli BK, „B”, négyzet + kör);
  - hogy a riasztó (érzékelők, központ, kezelő) ténylegesen beépült-e – a melléklet szerint az alap csak elővezetékezés, a rendszer külön rendelhető volt (a motoros redőny a `GOAL.md` szerint megvan);
  - az alapértelmezett szerelési magasságok (dugalj, kapcsoló, mozgásérzékelő), ahol a rajzon nincs „m=”;
  - melyik dugalj a szekrényvilágításé (A-902 05.1, 05.3).

## Független ellenőrzés (2026-10-24)
Egy külön ellenőrző futás a kinyerést nem látva, 300 dpi-s kivágásokon szobáról szobára vetette össze a CSV-t a rajzzal. A mennyezeti és fali lámpák, kapcsolók, dugaljak darabszáma, betűje, kódja és magassága mindhárom lakásnál egyezett. Javítva:
- **Hiányzó mozgásérzékelők:** a szobaajtók sarkára mutató, ferdén rajzolt jelek (A-811: S06, S07; A-902: S08, S09).
- **Hiányzó ventilátor:** A-811 06.1 fürdő, „s” (V03); az A-811 08 WC ventilátora (V02) megkapta a „b” betűt.
- **Rossz helyiség:** A-811 K20, T03, D40 a 05.1 szoba saját kapcsolója, termosztátja és dugalja (az ajtó előtti részen), nem a közlekedőé, illetve a HTH-é.
- **Téves „jel nélküli doboz”:** a bejárati ajtón kívüli csengőnyomó dobozai kizárva (A-811: 1, A-812: 2); a fix bekötés és a TSZ fali doboza a saját jeléhez rendelve (A-811: X01; A-812: X01, D42).
