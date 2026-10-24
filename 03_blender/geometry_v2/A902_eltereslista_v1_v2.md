# A-902 geometria: eltéréslista, Blender lock v1 vs. tervdokumentum v2 (2026-10-24)

**v1:** `geometry_lock_A902.json` (brosúra-alaprajzból, 2026-10-23). **v2:** `A902_geometria_v2_ELOZETES.json`, a méretezett alaprajz (1:50, vektoros) és a 9. emeleti megvalósulási terv (1:125, 2026-07-08) alapján.
**Fontos:** a terv méretei *vakolatlan* falra vonatkoznak, tájékoztató jellegűek. A kész falsík oldalanként kb. 1–3 cm-rel beljebb van. **Semmi nem IGAZOLT helyszínen**, ez hétfő feladata.

## 1. Összegzés
- A belső v1-modell **±15 cm-en belül** egyezik a tervvel. Szerkezeti tévedés nincs, a berendezést ez nem borítja.
- A legnagyobb belső eltérések: **05.3** a nyugati falnál −15 cm, a keletinél −13 cm (a szoba 3,525 széles, de nyugatabbra van). **06.2** −13/−10 cm. **Közlekedő** keleti fala −15 cm. **Konyha** nyugati fala −10 cm. **Nappali** keleti fala +11 cm (a hossz 7,08, a v1-ben 6,92 volt).
- **A terasz a nagy eltérés.** A v1 sík, egyszintű terasz volt üvegkorláttal. A valóság: greslap a −0,15 szinten, WPC-dobogó a +0,47 szinten (62 cm-rel magasabban), zöldtető, lépcsők és pálcás fémkorlát. A teraszkontúr is kisebb: x 3,44–16,27 a v1 3,40–16,80-a helyett, a zöldtető északi széle 19,80 a 20,40 helyett.
- **Belmagasság: 2,90 m.** IGAZOLT, Péter közlése 2026-10-24. Megegyezik a v1-gyel.

## 2. Helyiségek (cm; + = a v2-ben nagyobb x/y koordináta)

| Helyiség | v1 [x0,y0,x1,y1] | v2 [x0,y0,x1,y1] | Δ Ny | Δ D | Δ K | Δ É | Terv m² | Megjegyzés |
|---|---|---|---|---|---|---|---|---|
| 05_2 | [0, 0, 3.62, 2.55] | [0.0, 0.0, 3.65, 2.65] | 0 | 0 | 3 | 10 | 11.66 | 3.65 × 3.35 a fülkével |
| 05_2_gardrob | [0, 2.55, 2.42, 3.35] | [0.0, 2.65, 2.42, 3.35] | 0 | 10 | 0 | 0 |  | fülke 2.42 széles |
| 05_1 | [0, 3.45, 3.62, 7.97] | [0.0, 3.45, 3.57, 8.05] | 0 | 0 | -5 | 8 | 19.58 | 5.50 a fülkével; K-i rész 4.00 (4.05–8.05); D-i fal x 2.42–3.57 között y 4.05-nél |
| 05_1_eszaki | [0, 7.97, 2.95, 8.95] | [0.0, 8.05, 3.02, 8.95] | 0 | 8 | 7 | 0 |  | északi fülke (pillér mögött) |
| kozlekedo | [2.52, 2.65, 5.45, 4.04] | [2.52, 2.65, 5.3, 4.05] | 0 | 0 | -15 | 1 | 3.23 | 2.48 × 1.20 (+ ajtózsebek) |
| nappali_etkezo | [3.72, 4.04, 10.64, 7.97] | [3.67, 4.05, 10.75, 8.05] | -5 | 1 | 11 | 8 | 27.87 | 7.08 hossz; É-i falsík 8.05, üvegfal belső síkja ~7.93–8.27 tok |
| konyha | [8.55, 1.3, 10.64, 5.15] | [8.45, 1.35, 10.55, 4.05] | -10 | 5 | -9 | -110 | 5.24 | konyhafal (K) 3.90: y 1.35–5.25; 10.55–10.75 szerelt gk. technikai fal y 4.1–4.55 (elszívó) |
| eloter | [5.55, 0, 8.45, 1.95] | [5.6, 0.0, 8.35, 2.0] | 5 | 0 | -10 | 5 | 6.98 | bejárati fülke x 6.70–8.30, y 0.00–0.85; ajtó 1.05×2.10 |
| eloter_atjaro | [7.4, 1.95, 8.45, 4.04] | [7.3, 2.0, 8.35, 4.05] | -10 | 5 | -10 | 1 |  | előtér → nappali átjáró |
| wc | [5.55, 2.05, 6.6, 3.94] | [5.6, 2.1, 6.6, 3.95] | 5 | 5 | 0 | 1 | 1.88 | 1.30 × 1.85 (bidés ülőke); pontos kontúr L-alakú – helyszínen mérendő |
| furdo_06_1 | [3.72, 0, 5.45, 2.55] | [3.75, 0.0, 5.5, 2.65] | 3 | 0 | 5 | 10 | 4.46 | 1.75 × 2.65, kád 170×70 |
| 05_3 | [11.0, 4.04, 14.5, 7.97] | [10.85, 4.1, 14.37, 8.05] | -15 | 6 | -13 | 8 | 14.65 | 3.525 × 3.95 |
| furdo_06_2 | [14.6, 5.13, 16.5, 7.97] | [14.47, 5.2, 16.4, 8.05] | -13 | 7 | -10 | 8 | 4.39 | 1.925 × 2.85; épített zuhany 1.825 × 0.85 (y 7.20–8.05), 5/5 padka |

A konyha É-i −110 cm-e definíciós különbség: a v1 a konyhazónát a nappaliba benyúlva 5,15-ig vette, a v2 a falig (4,05) veszi. A konyhafal (K) hossza a terven 3,90 (y 1,35–5,25).

## 3. Terasz (v2)

| Zóna | Terület (terv) | Doboz [x0,y0,x1,y1] | z (belső padló = 0) | Státusz |
|---|---|---|---|---|
| T09_greslap_Ny | 23.62 | [3.44, 8.5, 9.29, 12.4] | -0.15 | DOKUMENTUM + VIDEÓ |
| T10_greslap_K | 19.34 | [11.39, 8.5, 16.27, 12.4] | -0.15 | DOKUMENTUM + VIDEÓ |
| T11_WPC_kozepso | 25.00 (a T11 összesen) | [9.29, 8.5, 11.39, 12.4] | 0.47 | DOKUMENTUM + VIDEÓ |
| T11_WPC_harant |  | [3.44, 12.4, 16.27, 13.41] | 0.47 | DOKUMENTUM + VIDEÓ |
| T11_WPC_eszaki_nyelv |  | [9.29, 13.41, 11.39, 14.46] | 0.47 | ELŐZETES – vonalból értelmezve |
| T11_WPC_panorama_pont |  | [7.62, 18.95, 11.42, 19.79] | 0.47 | ELŐZETES – terv-kontúr + videó |
| Zoldtető | 71.18 | [3.71, 13.41, 16.04, 19.8] | 0.77 | terület DOKUMENTUM; felszínmagasság ELŐZETES (videóbecslés), terhelhetőség HIÁNYZIK; NEM bútorozható/járható alapból |
| Lepcso_Ny |  | [6.48, 12.1, 7.68, 12.4] | -0.15→0.47 | DOKUMENTUM (nyíl) + VIDEÓ |
| Lepcso_K |  | [11.39, 12.1, 12.59, 12.4] | -0.15→0.47 | DOKUMENTUM (nyíl) + VIDEÓ |
| Jakuzzi_elokeszites |  | [4.1, 9.74, 6.1, 11.74] | -0.15 |  |

**Zöldtető tagolása (ELŐZETES, videó + Péter):** sík fű Ny [3.71,13.41,7.62,19.80], dombos évelőágyás [7.62,14.58,12.00,18.83] (+0,25 m), sík fű K [12.00,13.41,16.04,19.80]; betonszegély kb. térdmagas; pop-up esőztető a füvön, csepegtető az ágyásban.

## 4. Tények (IGAZOLT / ELŐZETES / HIÁNYZIK)

- **belmagassag:** {"ertek": 2.9, "status": "IGAZOLT – Péter közlése 2026-10-24 (+ brosúra)", "megj": "a 18. oldalon 'm=2.85' egy szerelési/nyílásmagasság-jelölés, nem belmagasság"}
- **parketta_A902:** {"ertek": "Egger Grey Treviso Oak EL2184, Classic 8/32 4V Aqua+ (591760), szegőléc 6 cm (1818766), burkolatváltó szálcsiszolt titán T-profil", "status": "IGAZOLT – dokumentum (burkolatkiosztási terv, 21. old.); helyszíni fotóval megerősítendő"}
- **parketta_A811_A812:** {"ertek": "Egger Grey Soria Oak EL2065, Classic 8/32 4V Aqua (593610)", "status": "IGAZOLT – dokumentum (7. és 14. old.)"}
- **konyha_padlo_A902:** {"ertek": "ELLENTMONDÁS: 18. old. 'kerámia' vs. 21. old. 'lam.parketta'", "status": "HIÁNYZIK – hétfőn fotó"}
- **meretek_jellege:** a terven szereplő méretek vakolatlan falfelületre vonatkoznak (−1…−3 cm/oldal vakolat), tájékoztató jellegűek
- **terulet_A902:** {"belso_m2": 99.94, "terasz_m2": 79.22, "bontas": "T09 23.62 + T11 25.00 + T10 19.34 + erkély 11.26", "zoldtető_m2": 71.18, "osszes_kulter": 150.4, "src": "PDF p3 megvalósulási terv 1:125 (2026-07-08)"}
- **mennyezeti_hutes_futes:** a 18. oldalon zónák jelölve; fúrás/rögzítés csak panelmentes sávban – pontos panelkiosztás HIÁNYZIK

## 5. Teendő
1. Hétfő: lézeres mérés a `08_allapotfelmeres/ALLAPOTFELMERES_CHECKLIST.md` szerint. A nappali hosszát, a 05.3 helyét, a közlekedőt, a teraszszinteket és a fellépőket kell mérni.
2. A mérés után: `geometry_lock_A902_v2.json`, az eltérések átvezetése egy **új** .blend-be, validátor, majd Péter jóváhagyása.
3. Addig a v1 lock marad érvényes, a v2 csak ELŐZETES réteg.