# Stílusfüggetlen költségstratégia – A-811 · A-812 · A-902 (v1, 2026-10-24)

**Státusz:** minden összeg **BECSLÉS**. **Írásos ajánlattal alátámasztott tétel jelenleg: 0 Ft.** Külső ajánlatot ebben a körben nem kértünk, és nem is kérünk Péter „mehet”-je nélkül. A 8 lakberendező cégnek korábban kiment megkeresésre (GOAL 6.) eddig nincs rögzített válasz.

## 1. Keretek
| Lakás | Keret bruttó | Tartalék (min. 10%) | Tervezhető | Kiindulási tábla |
|---|---|---|---|---|
| A-811 | 10,0 M | 1,0 M | 9,0 M | `KOLTSEG_KIINDULAS_A811.csv` (új) |
| A-812 | 10,0 M | 1,0 M | 9,0 M | `KOLTSEG_KIINDULAS_A812.csv` (új) |
| A-902 | 20,0 M | 2,0 M | 18,0 M | `ai-coordination/inputs/A902_v1/KOLTSEG_KIINDULAS_A902.csv` (v1, a terasz-sorok felülvizsgálata lent) |
| **Összesen** | **40,0 M** | **4,0 M** | **36,0 M** | |

A tartalék **lakásszinten** van, nem tételenként. Csak Péter jóváhagyásával szabad elkölteni. Ha egy lakás tervezhető összege túllép, a csökkentett tételeket ki kell mondani: mit, mennyivel, milyen hatással.

## 2. Bizonyítéki szintek (minden tételsoron kötelező oszlop)
1. **BECSLÉS:** tapasztalati sáv, forrás nélkül. Csak koncepciós szűrésre jó.
2. **WEBÁR + dátum:** konkrét termék, cikkszám, link, bruttó ár, a lekérés dátuma; szállítás külön sorban.
3. **ÍRÁSOS AJÁNLAT:** asztalos, villanyszerelő, konyha, jakuzzi-emelés; méretezett rajzra adott, bruttó, érvényességi idővel.
4. **Független ellenőrzés:** minden 2. és 3. szintű tételt Astra **és** Claude külön forrásból ellenőriz. Az eltérést `ar_elteres.md`-ben rögzítjük; ±10% felett döntési kérdés lesz belőle.

A render státusza a Render Reality Gate szerint csak akkor léphet „RENDER REALITY PASS – TÉTELES”-re, ha a látható fő tételek legalább 2. szintűek. „AJÁNLATTAL VALIDÁLT” csak a 3. szintű asztalos-, szerelési és konyhatételekkel lehet.

## 3. Lakásonkénti szerkezet (stílustól független)
| Blokk | A-811 | A-812 | A-902 | Miért |
|---|---|---|---|---|
| Konyha (korpusz, front, gépek, szerelés) | 2,20 | 2,10 | 2,90 | konyhabútor sehol nincs; a legnagyobb, nem alkuképes blokk |
| Nappali–étkező (hős-darabokkal) | 2,30 | 2,20 | 3,60 | itt születik a „drágaság” első benyomása |
| Hálók és gardróbok | 1,60 | 1,95 | 3,60 | minden hálóhoz gardrób (GOAL 4.6) |
| Fürdő, WC, HTH, mosó | 0,60 | 0,65 | 0,95 | szaniterek kész; csak tükör, fény, tároló, gépek |
| Előtér, közlekedő | 0,35 | 0,25 | 0,50 | az első 3 másodperc |
| Világítás (Hue, LED, villanyszerelő) | 0,60 | 0,65 | 1,00 | a fény a luxus egyik fő eszköze; a szerelés is költség |
| Falfelület (tapéta, panel) az asztaloson kívül | – | – | 0,50 | A-811/812: a hős-darab soron belül |
| Textil, dekor | 0,35 | 0,30 | 0,50 | |
| Kültér | 0,30 | 0,15 | 3,60 | A-902: lásd 4. pont |
| Tervezés + szállítás/szerelés | 0,70 | 0,75 | 0,85 | |
| **Összesen** | **9,00** | **9,00** | **18,00** |

A blokkösszegek a CSV-sorokból számolva egyeznek (ellenőrizve 2026-10-24). |

## 4. A-902 terasz – a valós állapot alapján felülvizsgálandó (még nem módosítva)
- **Meglévő érték:** két greslap-terasz, 25 m² emelt WPC-dobogó lépcsőkkel, 71 m² gondozott zöldtető öntözéssel, térdmagas betonszegély, pálcás korlát. **Burkolatra, kertépítésre és kaspóra nem kell pénz.** A 13e sor (növények, kaspók 0,45 M) várhatóan csökkenthető; a kültéri fény marad.
- **Jakuzzi** (13a–b, 2,0 M): csak akkor maradhat a tervben, ha a statikus nyilatkozat, a 9. emeleti emelés (daru) és a bekötés **igazolt**. Ha nem, ez a 2,0 M felszabadul.
- **Új kockázat:** a kültéri textil és párna az esőztető közelében. Időjárásálló anyag kell, vagy a bútort távolabb kell tenni a szórásképtől.
- **Lehetőség, nem javaslat:** a meglévő szintváltásokra, a betonszegélyekre és a panorámára épülő fény és ülés kis pénzből nagy hatást adhat. A kreatív döntés Astráé.

## 5. Független ellenőrzés menete (stílusdöntés után, döntős stílusokra)
1. Astra: termékjelöltek (név, link, ár, dátum, méret).
2. Claude: ugyanazok a tételek saját lekérésből (webshop, IKEA API), más forrásból is. A Kave Home ár csak a webshopban látszik.
3. Eltéréslista, majd keret újraszámolása lakásszinten (+10%), végül döntési kérdések Péternek.
4. Asztalos és konyha: méretezett rajz és szabásjegyzék → ajánlatkérés **csak „mehet” után** → 2–3 ajánlat ugyanarra a rajzra (teljes ár és csak munkadíj).
