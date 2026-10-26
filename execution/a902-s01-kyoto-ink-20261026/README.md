# A-902 Kyoto Ink S01 – megvalósítás

Állapot: FOLYAMATBAN / CP1a, szakaszolt átadás. Nem megrendelési vagy jóváhagyott kiviteli terv.

Feladat: a kiválasztott hat render alapján a teljes lakás és teljes kültér megvalósítási terve. Tervezhető keret 18 000 000 Ft bruttó; külön, érintetlen tartalék 2 000 000 Ft. Feltételes időtáv 13–17 hét, beszállítói visszaigazolás nélkül nem vállalt határidő.

Eredeti ág: competition/gpt6astra-v3-1-20261025. Forráscommit: 2bef09ae6081b5bafb86bc876ef8410be44bb567. Megvalósítási ág: execution/a902-s01-kyoto-ink-design-to-budget-20261026. Eredeti fájlokat nem módosítunk. A main későbbi fotó- és műszaki forrásai külön pillanatképekben vannak.

## Munkarend
1. CP0: forrásleltár, minden helyiség és szakma előzetes költségregisztere, távoli mentés és visszaolvasás.
2. CP1: tényleges termékjelöltek, rendereltérések, műszaki és gyártási specifikációk, tételes költségfrissítés.
3. CP2: ajánlatkérési csomagok, feltételes ütemterv, hiánytalansági és pénzügyi audit, tulajdonosi átadás.

Árstátuszok: ellenőrzött webshopár / beszállítói ajánlat / előzetes becslés. A tervezési becslés nem kínálati ár. SKU, méret, készlet, átfutás és szakági jóváhagyás hiányában UNKNOWN/PENDING szerepel. A/B/C a megvalósítás módja; az A minősítés csak igazolt konkrét termék esetén adható.

Az aktuális Excel lesz az egyetlen szerkesztendő pénzügyi nyilvántartás. CSV és JSON csak ugyanannak a verziónak az ellenőrzött exportja, külön nem szerkesztendő. A régi COST csomagsorok csak összehasonlítási baseline-ok, az új részletekkel együtt nem összegezhetők.

Külső ajánlatkérés, megrendelés és üzenetküldés nincs elindítva. A végleges méretekhez helyszíni felmérés, a villamos és vizes helyiségi megoldásokhoz szakember, a tetőteraszhoz terhelési és rögzítési ellenőrzés szükséges.

## CP0 ismert lényeges eltérések
- A 8,4 M fix csomagból 3,6 M a kültér, benne 1,7 M jakuzzi és 0,3 M emelés/bekötés. Feltételes marad, az előirányzatban szerepel, de nem igazolt ajánlati ár és nem automatikusan elhagyható tétel.
- A hat kiválasztott kép: Cam12 v1, Cam02 v1, Cam03 v2, Cam04 v1, Cam10 v1, Cam11 v2. Más változat nem lép helyükbe.
- Cam03 v2: korábbi QA szerint GEOMETRY_NEAR; nyújtott konyha, széles hűtőtorony, falikar rossz oldalon. A meglévő kiállás és alaprajz elsődleges.
- Cam12 v1: tulajdonos által elfogadott tervközeli hangulatkép, nem méretezési forrás.
- Meglévő padló hűvösebb és a fürdő relief hatszögletű, nem a render négyzetrácsa. Burkolatcsere nincs automatikusan tervezve.
- A nappali üveg előtti belső fellépés fotó alapján hiányzik a régi modellből; helyszínen felmérendő.
- Az S01 17 611 000 Ft gazdaságos és 18 450 000 Ft fő baseline becslés. A keretmegfelelés nincs bizonyítva.

## Aktuális átadás
CP0 commit: `884788f70bdcade7d603f5e90d2f4085c99b939c`. CP1a: `01_CP1a_KIEMELT_TERMEKEK.md`; folytatás: `02_FOLYTATAS_ATADAS.md`; ellenőrzés: `03_ELLENORZESI_NYUGTA.md`. A fő előirányzat20083350Ft. Az Excel gazdaságos oszlopa még ugyanaz a változat, nem kész megtakarítási terv.
