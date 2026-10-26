# Folytatási csomag – CP1b

A feladat szakaszolva van, nem lezárva. A felhasználó az Astra-keret kímélése érdekében most a 10–15 látványmeghatározó darabra korlátozta a részletes kutatást. Modellváltás és új chat indítása nem történt. A következő szakasz ugyanitt, a felhasználó által választott takarékosabb modellel folytatható.

## Kötelező indító olvasás
1. `sources/TELJES_MESTERTERV_MEGRENDELOI_BRIEF.txt` – a teljes eredeti követelmény változatlan másolata; minden követelmény érvényes.
2. `README.md`, `00_CP0_ELLENORZES.md`, `01_CP1a_KIEMELT_TERMEKEK.md`, `03_ELLENORZESI_NYUGTA.md`.
3. `outputs/A902_Kyoto_Ink_elo_regiszter.xlsx` – az aktuális pénzügyi munkafájl. A JSON/CSV ugyanennek az átadott verziónak pillanatképe. Kézi Excel-módosítás után NE futtasd rá vakon a generátort; először olvasd vissza és őrizd meg az új adatokat.
4. A hat kiválasztott render és a hozzájuk tartozó prompt az eredeti `05_promptok/KEP004_GPT6ASTRA_V3_1_r1` csomagban; `data/render_manifest.json` a helyi képfájlokat és hash-eket rögzíti.

## Kutatási sor – kis adagokban
|Adag|Tartalom|Kimenet és kapu|
|---|---|---|
|CP1b-1|Somar/Nifelia magyar ár és készlet; Brisia csak alternatíva; Eamy hat db HU szállítás; Lennon logisztika|12 sor hiányzó adatainak kitöltése, új és örökölt adat világosan megkülönböztetve|
|CP1b-2|Grafit dohányzó- és mellékasztal, két grafit éjjeli, teljes opálgömb éjjeli Hue-val, FL01 falikar|Legalább két tényleges jelölt minden jelentős megoldatlan késztermékhez; a kizárt DELIFE-változatot ne add vissza egyezőként|
|CP1b-3|Konyhai gépek; 05.2 és05.3; előtér/WC/fürdők; kültéri bútor és fény|Szobánként részletes SKU/qty/méret/ár/garancia/áfa/szállítás/átfutás és rendereltérés|
|CP1b-4|Hue teljes rendszer|Lámpatest+izzó+szalag+táp+profil+vezérlő+Bridge+kapcsoló; nincs kettős számolás, vizes zónák és HF-rögzítés szakági kapu|
|CP1c|Asztalos, kárpit, W01/W02/W07, grafikák, gardrób/konyha/fürdő|Méretezett, felmérési státusszal ellátott gyártási és ajánlatkérési csomag; burkolat/nyomtatás m²; anyag, vasalat, szerelés, szerviz|
|CP2|Teljes ütemezés, költségoptimalizálás, hiánytalansági audit|18M keret tényleges igazolása vagy számszerű döntési csomag; érintetlen2M tartalék; 13–17hét csak visszaigazolásokkal|

Minden adagnál először az ismert SKU közvetlen termékoldalát nyisd. Egy sikertelen közvetlen és egy böngészős/gyártói alternatív ellenőrzés után rögzíts PENDING-et és lépj tovább; ne ismételd ugyanazt korlátlanul. Keresőtalálat árát ne nevezd élő kosárárnak. Más ország áfáját és szállítását ne emeld át magyar végárként. Akció/feliratkozási kedvezmény ne legyen biztos megtakarítás. Csomagsort csak alkatrészekre bontva, a régit kiváltva módosíts; ne tedd az új sort a régi teljes ár mellé.

## Változatlan műszaki és vizuális határok
- Csak Cam12v1, Cam02v1, Cam03v2, Cam04v1, Cam10v1, Cam11v2; a render hangulati cél, a hiteles terv és valós kiállás elsődleges.
- Cam03v2 nyújtott konyha/hűtőtorony és rossz oldali falikar nem kiviteli alap. A kész padló hűvösebb, a fürdő relief hatszögletű. Új burkolatcsere nincs jóváhagyva.
- Teljes lakás és a teljes150,4m² kültér lefedendő; a meglévő teraszszintek változatlanok. A jakuzzi2M feltételes csomag továbbra is benne van, nem hagyható el csendben.
- Északi PAX299,4cm egy302cm névleges fülkében nem igazolt szerelés. A grafikus front és290cm magas lezárás külön tervezendő.
- A 100cm zuhanyüveg és integrált mosdóbútor kötelező irány. A meglévő kerámia nem vágható; gyártói beépítési engedély vagy külön cserealternatíva.
- Felmérés, villamos audit, vizes zóna, tetőterasz terhelés/rögzítés és beszállítói ajánlat nem helyettesíthető becsléssel.

## Következő ellenőrzési pont
**CP1b: a kiemelt termékek nyitott kérdései + a négy hiányzó vizuális termékcsoport alternatívái + frissített költséghíd.** Minden adagot ugyanarra az `execution/a902-s01-kyoto-ink-design-to-budget-20261026` ágra ments, majd olvasd vissza a commitot és a fájlhash-eket. A felhasználó kifejezetten jóváhagyta a teljes projekt feltöltését a saját privát `peterkapusi88-hub/wsg-berendezes` repó ezen ágára. Eredeti ágak és fájlok érintetlenek. Megrendelés, külső ajánlatkérés vagy üzenetküldés nincs engedélyezve.
