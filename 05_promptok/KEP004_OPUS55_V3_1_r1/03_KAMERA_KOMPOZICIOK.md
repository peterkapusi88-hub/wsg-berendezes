# 03 · Kamerakompozíciók – a hat kamera (VB.3 szerint)

Forrás: VB.3, `GEOMETRIA_C_KAMERACSOMAG_v2.md` 3. pont, `WSG-20261025-A902-KAMERACSOMAG-C_r1.md` 3–4. pont (képterület-arányok), `A902_Cam10_…_v1.md`, `A902_Cam11_…_v1.md`. A kamera geometriája és a kep_id-k változatlanok; **kameraértéket nem adok meg és nem találok ki** – a pozíció csak tájékoztatásul, a lock szerint áll itt. A végleges FRAME LAYOUT Claude integrátoré. A promptok a látható elemek **hierarchiáját** írják le (mi uralja a képet, mi kísér, mi szél).

| Kamera | Fény | Szerep |
|---|---|---|
| Cam_02 nappali–terasz | kék óra / kora este, rétegzett Hue 2200–2700 K, RGB nélkül, közepes expozíció | a TV-fal = fő WOW; geometriai kontroll |
| Cam_12 nappali hero v3 | nappal, természetes, világos | közös hero- és összehasonlító nézet |
| Cam_03 K1 konyha–étkező | nappal | a konyha a kép tárgya |
| Cam_04 master | este, Hue-jelenet | fejvégfal + északi gardróbfal |
| Cam_11 master panoráma | nappal | üvegfal + valódi kilátás, kontroll |
| Cam_10 fürdő 06.2 | csak műfény | tükör/tároló/fény a beépített burkolat előtt |

## Cam_02 – nappali–terasz (lock: [8,30; 4,40; 1,55], ÉNy, 20 mm)
**Hierarchia:** (1) **W01 TV-fal** a bal harmadban, teljes magasságban – a kép fő eleme, rejtett Hue-vonalakkal; (2) az ülőcsoport középen (a kanapé háttal felénk/keletre, a TV felé nyitva), dohányzóasztal, szőnyeg, fotel; (3) jobbra a 4,50 m-es üvegfal, a terasz (−0,15 greslap, +0,62 WPC, zöldtető, antracit korlát) és a budai panoráma kék órában; (4) jobb alsó sarok: az étkezőasztal nyugati hosszoldala és két szék; (5) felső szél: az ML05 lámpateste; a W01 és az üvegfal közti tömör sáv (W04) a sarokban.
**Fény:** a TV-fal rejtett vonalai (alsó lebegő sáv, felső/oldalsó súrolás) adják a képet; az ML05 tompítva; egy állólámpa; az ML04 a jobb szélen. A TV kikapcsolt, sötét üvegfelület. Az ég mélykék, a város első fényei.
**Kontroll:** falélek, nyílások, padló–fal vonal, terasz, korlát, zöldtető olvasható; nincs bebukó fekete.

## Cam_12 – nappali hero v3 (lock: [4,40; 7,88; 1,60], θ −48°, 22 mm, shift_y −0,05)
**Hierarchia:** (1) a **W02** a kép jobb közepén, szinte szemből – az összekötő fal fő felülete (kb. 22 %, takaratlan); (2) a **W07** a jobb szélen (a hálók felé vezető közlekedő torka, kb. 10 %); (3) középen-balra az **étkező** az ML04 függesztékkel (kb. 7–9 %), mögötte a **konyha** (kb. 11 %): a pultsorok frontja, a hűtőoszlop a W03-a előtt; (4) bal szél: a **W03** a szürke 05.3 ajtóval és a szemöldöksávval; (5) **előtér**: a kanapé háttámlája és karja, alacsony sávként (L: kb. 16 %, U: kb. 23 %), rajta párnák, pléd; (6) felső sáv: fehér mennyezet (kb. 16 %), az ML05 lámpateste a felső szélen beléphet.
**Nem látszik:** a TV-fal, az üvegfal, a terasz (a kamera mögött / balra).
**Fény:** nappali, természetes, világos luxusenteriőr-fotó; a Hue visszafogott vagy ki van kapcsolva; a fal textúráit a nappali fény olvassa ki.
**Kötöttség:** a kamera állóhelye (x 4,30–4,50; y 7,75–8,05) szabad – ott nincs állólámpa, növény, magas bútor.

## Cam_03 – konyha–étkező K1 (lock: [9,45; 7,55; 1,50], dél felé, 20 mm, shift_y −0,08)
**Hierarchia:** (1) a **konyha** „galéria” nézetben, a két pultsor közé nézve: a nyugati sor (a kb. 85 cm-es mellvéd mögött, főzőlappal) és a keleti sor (mosogató, mosogatógép) frontja, munkalapja, hátfala; (2) a kép mélyén a **déli magas elemfal** (sütő, mikró) és a **hűtőoszlop** a W03-a előtt (D13), 100 %-ban takaratlan; (3) jobb előtér: az **étkező** széle, két szék, és a jobb felső sarokban közel lógó **ML04** lámpatest (a kép része!); (4) a konyhai mennyezet fehér, a konyhában a terv szerinti +2,45 m-es álmennyezeti sáv a felsőszekrények felső határa.
**Nem látszik:** terasz, TV-fal, kanapé; a keleti pultfal (x 10,55) a keleti sor mögött takarásban van.
**Fény:** nappal; a pult alatti szekrényfény visszafogottan.

## Cam_04 – master este (lock: [0,35; 4,30; 1,50], ÉK, 20 mm)
**Hierarchia:** (a kamera a DNy-i sarokból ÉK felé néz: balra észak, jobbra kelet) (1) a **keleti fejvégfal** az ággyal (180 × 200, tengely y 6,40), a kép közepén-jobbján – a stílus fő hálószobai gesztusa; (2) **bal oldalt / a kép mélyén** az északi fülke **teljes, mennyezetig érő gardróbfala** (≈ 3,00 × 0,90 × 2,90 m, front a pillér síkjában); (3) éjjeliszekrények és olvasólámpák (D20/21 északon, D22/23 délen), ágytextil, pléd, szőnyeg; (4) a déli 2,42 m-es gardróbsáv ugyanabban a frontcsaládban, ahol a kép jobb szélén belép; (5) a mennyezet fehér, ML06.
**Fény:** este, Hue-jelenet 2200–2700 K: fejvégmögötti fény, olvasólámpák, fülkefény (D26); közepes expozíció, élek olvashatók.
**Kötöttség:** K13/K14 kapcsolók és a D20–D23 dugaljak hozzáférhetők; az ágy mellett ≥ 60 cm.

## Cam_11 – master panoráma nappal (lock: [3,20; 6,10; 1,20], nyugat, 20 mm, ülő szemmagasság)
**Hierarchia:** (1) a **3,64 m-es nyugati üvegfal** három fehér keretes mezővel (bal/déli végen nyíló szárny, keskeny középső, széles fix jobb), az erkély (15 cm-rel lejjebb, világosszürke greslap, fekete pálcás korlát) és a **valódi kilátás** (városi tetők, templomtorony, budai hegyek); (2) alsó előtér: az ágy lábvége, ágytextil, pléd; (3) jobb szél: az **északi gardróbfal** frontja; bal szél: a **déli gardróbsáv**; (4) függöny a 0,33 m-es falsávon, oldalra húzva; szőnyeg.
**Nem látszik:** a fejvég (a kamera mögött).
**Fény:** nappal, semleges fehéregyensúly; a Hue ki van kapcsolva.

## Cam_10 – fürdő 06.2 (lock: [14,50; 6,62; 1,50], kelet, 16 mm)
**Hierarchia:** (1) a **távoli keleti fal**: az aknától az üvegig érő **lebegő mosdópult**, benne a meglévő fehér Geberit mosdó (belesüllyesztve), fölötte a **stílus tükörkompozíciója** és a FL04-pont (z ≈ 2,00); (2) **bal oldal**: a walk-in zuhany az **új 100 × 200 cm-es fix üvegfallal** a padkán, mögötte az Esagonetta dekorfal, fekete fejzuhany, 70 cm-es folyóka; (3) **jobb oldal**: a keskeny **fali tároló-oszlop** az aknához simulva, a DK-i akna/falblokk; a WC-fülke a jobb képszél mögött; (4) **rejtett fények** (tükörglória / pult alatti padlófény / oszlopfény) és 1–2 stílustárgy; (5) mennyezet: ML10 – 3 fejes spotsín, egy fej a hatszög-dombordekort súrolja. (r1b, Péter 2026-10-25 16:00/16:04)
**Fény:** csak műfény a meglévő pontokról (ML10, FL04 – a rejtett 24 V-os fények is a FL04-ről), esti hangulat 2200–2700 K; nincs ablak, nincs nappali fény.
**Kötöttség:** semmit nem burkolunk újra; D43/D44 (a mosdótól délre) szabad.

## Nézetek közötti azonosság
Cam_02 = Cam_12 = Cam_03: egyetlen nappali–étkező–konyha terv, csak a fény más. Cam_04 = Cam_11: egyetlen master. Minden termék minden nézetben azonos névvel, mérettel, színnel.
