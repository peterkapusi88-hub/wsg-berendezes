# A-902 – tér- és geometriai adatlap

**Mértékegység: méter.** Minden alábbi koordináta a meglévő modell adata; nem kész helyszíni felmérés. Tervi területet nem helyettesít modell-befoglaló. A fő terasz a rajzon a lakás felett, az oldalerkély balra található.

## Tájolás

A tulajdonos észak-felfelé műholdképe (U07), a Szabolcs utca tengelye és az 1:50-es terv északjele együtt kb. **53°** földrajzi azimutot ad a rajzi +y iránynak. A térképről leolvasható irány nagyjából 50–55°; ez nem földmérési pontosságú intervallum. +x ≈143° (DK), −x ≈323° (ÉNy), −y ≈233° (DNy). A nappaliból egyenesen kifelé tehát **ÉK**, balra **ÉNy**, jobbra **DK**. A korábbi x=K/y=É címkéket csak helyi tengelynévként szabad kezelni.

A 3. lap kis helyszínvázlatának északjele kb. 12,5°-kal, a 18. lapé kb. 52,8°-kal tér el a papír függőlegesétől. Az első nem adható át automatikusan a nagy alaprajz északjaként. A műholdkép a 18. lap szerinti elfordulást támogatja. Az utcavonal, a tetőkontúr és a piros nyíl helyazonosításra használható; a ferde fotogrammetriai tetőképből centiméteres távolság vagy épületmagasság nem.

## Felületek

| Elem | Terv m² | Modell x₁,y₁ → x₂,y₂ | Modell befoglaló m² | Modell felső z |
|---|---:|---|---:|---:|
| T09 gres | 23.62 | [3.44, 8.5, 9.29, 12.4] | 22.815 | -0.15 |
| T10 gres | 19.34 | [11.39, 8.5, 16.27, 12.4] | 19.032 | -0.15 |
| WPC közép | – | [9.29, 8.5, 11.39, 12.4] | 8.19 | 0.47 |
| WPC haránt | – | [3.44, 12.4, 16.27, 13.41] | 12.9583 | 0.47 |
| WPC nyelv | – | [9.29, 13.41, 11.39, 14.46] | 2.205 | 0.47 |
| WPC távoli | – | [7.62, 18.95, 11.42, 19.79] | 3.192 | 0.47 |
| Zöldtető befoglaló | 71.18 | [3.71, 13.41, 16.04, 19.8] | 78.7887 | 0.77 |

A WPC négy téglalapjának összege 26,5453 m², a terv 25,00 m²-éhez képest +1,5453 m² (+6,18%). A zöldtető befoglalója 78,7887 m², de ebből nem következik tényleges kertterület: a kontúr bemetszéseit és burkolati határait külön kell kezelni. A terv elsődleges területadata 71,18 m².

Az L-erkély modellpoligonja: (−0,30;−0,20), (−2,01;−0,20), (−2,01;5,69), (−1,12;5,69), (−1,12;7,90), (−0,30;7,90). Modellterület 11,8841 m²; terv 11,26 m². A két szélesség 1,71 és 0,82 m, a teljes modellhossz 8,10 m. A régi rejtett téglalap nem érvényes erkélykontúr.

## Szintek, átjárások

- Terv: gres +28,40; WPC +29,02; különbség 0,62 m. A modellben beltéri padló z=0, gres −0,15, WPC +0,47. A két referencia-rendszert ne keverd össze.
- Fotó: a haránt WPC-sáv és a középső platform/nyelv között további fellépés van. Ennek pontos magassága ismeretlen. A modell valamennyi WPC-t azonos z=+0,47-re teszi: képi ellenbizonyíték miatt nem helyszínhű.
- Modell-lépcső bal: x 6,48–7,68; jobb: x 11,39–12,59; mindkettő y 11,50–12,40. Szélesség 1,20; futás 0,90 m. Három köztes fok teteje +0,005 / +0,160 / +0,315; felső WPC +0,470. Ebből 4 ×15,5 cm emelkedés és 30 cm belépő adódik a modellben, nem mérésként.
- A régi geometriai JSON 0,30 m mély lépcsődobozát nem szabad a teljes 0,90 m lépcsőfutásnak tekinteni.
- Fő nappali nyílás tervi 4,50×2,53 m, 05.3 ajtó 1,80×2,53 m; mindkettőnél tervi 15 cm belső fellépő. A fotók megerősítik a fellépőt. Névleges méret nem szabad átjárási méret.
- Master nyílás tervi 3,65×2,57 m; 05.2 ajtó 1,88×2,57 m. Az oldalerkély kapcsolatait külön kell kezelni.
- A középső WPC előtt a folytonos modell-betonszegély x 3,44–16,27; y 13,41–13,53; z +0,47–+0,82. Ez a nyelv bejáratánál téves akadályt képez.
- Távoli WPC megközelítése, kert járószintjei, korlát tényleges magassága és szabad közlekedősávok: nem kimértek.

## Közmű-koordináták: külön a jel és a valós hely

| Tétel | Forrásadat | Értelmezés |
|---|---|---|
| D47 / D48 | (4,180;8,538) / (14,119;8,538) a villamos JSON-ban | Két teraszdugalj jelölése; szerelési magasság és áramkör nem ismert. |
| Jakuzzi áram | Modellközép (3,82;9,69); új jelkinyerés S07 (3,77;9,29), fizikai fal x≈3,50 | Kb. 40 cm y-eltérés; nem lehet valamelyiket pontos helyszíni pontként kijelölni. |
| Csap | Modellközép (4,14;9,00); T09 fotó igazolja | Pontos faltól/padlótól mért távolság ismeretlen. |
| Öntözőakna | Modell x 9,17–9,45; y 13,30–13,41 | Becsült; fotó fedlapot igazol, ezt a helyet nem. |
| FL05 / FL06 / FL07 | (6,689;8,529), (12,959;8,529), (−0,47;3,11) | Tervi lámpapontok; nem igazolt készülék- vagy Hue-azonosság. |

## Blender-ellenőrzés

Két másolaton csak olvasási ellenőrzés történt, automatikus fájlszkriptek nélkül; mentés és render nélkül. A v2-ben 795, a v2b-ben 970 objektum volt. A 43 vizsgált terasz-lock elem legnagyobb koordinátaeltérése 0,000479 m. Ez kerekítési nagyságrendű belső egyezés. A v2→v2b terasz-befoglalók között a nyugatinak nevezett mellvéd y-min értéke 8,50-ről 9,25-re változott; a többi ellenőrzött elem befoglalója változatlan.

A fájl elnevezésében, verziómezőjében szereplő „draft” felirat nem bizonyít jelenlegi GitHub-státuszt: az audit a rögzített commit tényleges fájlbájtjait vizsgálta. Nem készült Render Reality PASS.

[43 elem összehasonlítása](evidence/terrace_lock_comparison.json) · [Gépi tényadatok](geometry.json) · [Forrásjegyzék](FORRASJEGYZEK.md)
