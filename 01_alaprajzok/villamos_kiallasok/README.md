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

## Koordináták
Egység: méter. x a rajzon jobbra, y a rajzon felfelé. Pontosság a rajzhoz képest ±1 cm (1:50), illetve ±2 cm (1:100).

**Origó lakásonként:**
- **A-902:** x=0 a 05.1 szoba homlokzati belső falsíkja, y=0 a 05.2 szoba alsó belső falsíkja. **Azonos a Blender-modellel** (`03_blender/WSG_A902_*`).
- **A-811:** x=0 a 04 nappali erkély felőli belső falsíkja, y=0 a 05.1 szoba rajzon alsó belső falsíkja.
- **A-812:** x=0 a 04 nappali erkély felőli belső falsíkja, y=0 a 04 nappali rajzon alsó belső falsíkja.
- Az A-811 és az A-812 helyi rendszer, mert Blender-modell még nincs.

**Mezők:**
- `x_m`, `y_m`: a rajzi jel középpontja. Mennyezeti lámpánál ez maga a kiállás helye.
- `doboz_x_m`, `doboz_y_m`: a fali szerelvénydoboz helye a falsíkon. **Fali eszköznél ez a fizikai hely.**
  - Ha több jel egy vezetővonalon ül (például kapcsolóoszlop, TV-blokk, ágy melletti kapcsoló + dugalj), mind a vezetővonal falnál lévő végére kerül.
- `magassag_m`: szerelési magasság a padlótól. Csak ott van kitöltve, ahol a rajzon „m=…” felirat szerepel.

**Helyiség-hozzárendelés:** az A-902-n a Blender-geometria helyiségein alapul. Az A-811-en és az A-812-n kézzel rögzített, közelítő téglalapokon (a koordináta a mérvadó).

## Jelkulcs – mennyire biztos
A lapokon ez áll: „Jelmagyarázatot lásd mellékletben!”. Maga a jelmagyarázat **nincs** a feldolgozott PDF-ben.

| Jel | Jelentés | Biztonság |
|---|---|---|
| ⊗ kör + X, kisbetűvel | mennyezeti lámpakiállás, a betű az áramkör | IGAZOLT (a módosítási szöveg így hivatkozik rá, pl. „»h« mennyezeti lámpakiállás”) |
| félbevágott ⊗ a falon | fali lámpakiállás (falikar), pl. A-902 nappali 2,85 m, A-811 nappali 2,65 m | IGAZOLT (a módosítási szöveg alapján) |
| kis kör szárral, betűvel | kapcsoló; a betű a kapcsolt áramkör | IGAZOLT |
| félkör a falnál | dugalj; kódok: P pult, H hűtő, MG mosogatógép, Mi mikró, S sütő, EL elszívó, M mosógép, SZ szárítógép, TSZ törölközőszárító, B fürdőszobai (tükör melletti) | IGAZOLT a felsoroltakra, a „B” jelentése NEM IGAZOLT |
| S/F kör | főzőlap/sütő fix bekötése | VALÓSZÍNŰ |
| M körben | elszívó ventilátor; a betű a kapcsoló áramkör | VALÓSZÍNŰ |
| ⊓ 1 / 2 / 3, illetve BK a TV-blokkban | gyengeáramú aljzat (TV-blokk, szobák) | a kódok jelentése NEM IGAZOLT (valószínűleg TV/adat/telefon) |
| önálló BK doboz (kisebb felirattal) | riasztó (biztonsági) központ | VALÓSZÍNŰ: az A-811 módosítási szövege szerint a 05.2-3 összevonásakor „a biztonsági központ áthelyezésre kerül”, és az A-811 egyetlen önálló BK doboza a 05.2-3 gardróbjában van |
| négyzet + kör | TV/antenna aljzat | VALÓSZÍNŰ |
| R körben, minden ablaknál | motoros redőny kiállása | VALÓSZÍNŰ (a `GOAL.md` szerint a lakásokban motoros redőny van) |
| kupola hullámokkal | mozgásérzékelő (riasztó) | VALÓSZÍNŰ: az A-811 módosítási szövege a „g”, „c,d” kapcsolókkal és a termosztáttal együtt mozgásérzékelőt tesz a nappali válaszfal sarkára, és ott ez a jel áll |
| billentyűzet, kaputelefon, ajtótok-eszköz, EL4, kék T | riasztó-kezelő, videós kaputelefon, elektromos zár vagy nyitásérzékelő, lakáselosztó, hűtő-fűtő termosztát | VALÓSZÍNŰ |
| kék szaggatott átló | mennyezeti hűtő-fűtő mező; a téglalap az átló végpontjaiból, ±10 cm | VALÓSZÍNŰ (a felirat: „mennyezeti hűtés-fűtés”) |

A nem igazolt jelentések a `WGR1_műszaki melléklet.pdf`-ből vagy a fejlesztőtől tisztázhatók. Ehhez Péter engedélye kell.

## Mire készült egy-egy kiállás
A rajzlapok „Elektromos módosítás (erős és gyengeáram)” blokkja megmondja, melyik kiállás miért készült. Lakásonként tömörítve az `OSSZESITO.md`-ben és a JSON `meta.modositasok_villamos` mezőjében. Tervezéshez a legfontosabbak:
- **A-902:** a 05.1-ben 1, a 05.3-ban 2 dugalj **szekrényvilágításhoz** készült – a gardrób LED-je ezekről megy, új kiállás nélkül. Melyik dugalj az, a rajz nem jelöli külön: helyszínen azonosítandó.
- **A-902:** a nappali falikarja (2,85 m) a 05.1 felé eső válaszfalon van; a „b” (étkező) és az „n,p” (nappali) mennyezeti kiállást a módosítás eltolta – a CSV a módosított helyet tartalmazza.
- **A-811:** a 05.2-3 „m” lámpája 3 helyről, a közlekedő „h” lámpája 3 helyről kapcsolható; a TV-blokk a 05.1-ben m=1,20 m.
- **A-812:** a 05.2 TV-blokkja m=1,20 m; a 08/09 fürdő „m” és „l” lámpája egy csillárkapcsolón van.
- **Lakáson kívül** mindhárom lakásnál: a szinti tárolóban (AT8-01/-02/-03) 2-2 dugalj, az egyik beállóban (P-0-65 / P-0-32 / P-0-33) autótöltő.
- **Álmennyezet** Péter átvételi összesítője szerint csak az előtérben, a WC-ben és a fürdőben van (min. 2,40 m). A rajz zöld „gk. álm.” feliratait az `OSSZESITO.md` lakásonként felsorolja; a pontos kiterjedés helyszínen ellenőrizendő.

## Kötelező tervezési szabályok (minden AI-nak)
1. **Világítás és minden áramot igénylő elem csak meglévő kiállásra kerülhet.** Ezek a mennyezeti ⊗, a fali lámpakiállás és a dugalj. Új kiállás, vésés, falon kívüli új kábelezés **nincs**.
2. **Függeszték, csillár, mennyezeti lámpa csak a ⊗ kiállás helyére kerülhet.** Ha máshová kell fény: dugaljról táplált állólámpa vagy bútorba épített LED, illetve akkus lámpa.
   - Kiállástól eltolt függeszték mennyezeti rögzítést igényel, ezért csak Péter külön jóváhagyásával.
3. **A hűtő-fűtő mezőkbe (HF) nem fúrunk.** Függönysín a szemöldökre vagy a falra kerül, a mezőn kívül.
4. **Bútor, panel vagy tapéta nem takarhatja** a kapcsolót, a termosztátot, a lakáselosztót (EL4), a BK-dobozt, a kaputelefont, a riasztó-kezelőt és a mozgásérzékelőt (a szobaajtók sarkában is van; magas szekrény ne kerüljön elé).
   - A dugalj hozzáférhető marad.
   - Falpanelen és lamellán kivágás kell a doboz helyén (`doboz_x/y` + magasság).
5. **A TV-blokk helye kötött:**
   - A-902: a nappali nyugati válaszfalán, a 05.1 felé, kb. y 6,0–6,5 m;
   - A-811: a nappali és a 05.2-3 közötti falon;
   - A-812: a nappali alsó falán.
   - Máshová tett TV-hez nincs antenna/adat aljzat és dugalj.
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
  - a jelmagyarázat;
  - az alapértelmezett szerelési magasságok (dugalj, kapcsoló, mozgásérzékelő), ahol a rajzon nincs „m=”;
  - melyik dugalj a szekrényvilágításé (A-902 05.1, 05.3).

## Független ellenőrzés (2026-10-24)
Egy külön ellenőrző futás a kinyerést nem látva, 300 dpi-s kivágásokon szobáról szobára vetette össze a CSV-t a rajzzal. A mennyezeti és fali lámpák, kapcsolók, dugaljak darabszáma, betűje, kódja és magassága mindhárom lakásnál egyezett. Javítva:
- **Hiányzó mozgásérzékelők:** a szobaajtók sarkára mutató, ferdén rajzolt jelek (A-811: S06, S07; A-902: S08, S09).
- **Hiányzó ventilátor:** A-811 06.1 fürdő, „s” (V03); az A-811 08 WC ventilátora (V02) megkapta a „b” betűt.
- **Rossz helyiség:** A-811 K20, T03, D40 a 05.1 szoba saját kapcsolója, termosztátja és dugalja (az ajtó előtti részen), nem a közlekedőé, illetve a HTH-é.
- **Téves „jel nélküli doboz”:** a bejárati ajtón kívüli csengőnyomó dobozai kizárva (A-811: 1, A-812: 2); a fix bekötés és a TSZ fali doboza a saját jeléhez rendelve (A-811: X01; A-812: X01, D42).
