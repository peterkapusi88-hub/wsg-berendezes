# A-902 – bútor nélküli alapképek a v2b modellből · Render Reality Card (2026-10-24)

**Azonosító:** `A902-ALAP-V2B-20261024` · **Cél:** az Astra-féle B fázis (azonos kamerás stílusképek) geometriai alapja. Nem látványterv.

**Gate-státusz:** `ALAPKÉP – TERV SZERINT` · `ELŐSZŰRT – FELTÉTELES`. Nem PASS, mert a padló dekorja nem igazolt, a falsík pedig a hétfői helyszíni mérésig terv szerinti.

## Bemenet és beállítás
| | |
|---|---|
| Modell | `03_blender/WSG_A902_v2b_alaprajz_ELOZETES_20261024.blend` – a KORR 2 terv szerint javított geometria (125 tétel). Lock: `geometry_lock_A902_v2b.json`. Validátor v2: LOCK 0, TERASZ 0, kamera rendben. |
| Szkript | `03_blender/geometry_v2/render_alapkepek_v2b.py`, „semleges” változat. Csak a betöltött példányon módosít, nem ment. |
| Render | Blender 5.2.3, EEVEE, 1600 × 1000, AgX + Medium High Contrast, expozíció +0,75. Háttér-Blender a Macen; az élő `WSG_A902_stilusok.blend`-hez nem nyúlt. |
| Fény | Egyenletes, szórt nappali fény (egyszínű égbolt, 0,86/0,88/0,92, erősség 1,0). Nincs nap, mert az iránya nem igazolt, és nincsenek belső lámpák. |
| Rejtve | Mindkét stílusréteg, a 185 bútorelem és a kiállás-réteg. Látszik a 12 beépített szaniter-elem (kád, mosdó, WC, zuhany, törölközőszárító). |
| Kamerák | A lock szerint, változatlanul: Cam_02_Nappali_terasz, Cam_03_Etkezo_konyha, Cam_04_Master. |

**A „lock” fénybeállítás elvetve:** az égbolt-textúra, a nap és a belső lámpák −1,0-s expozícióval próbaképen kékes, sötét falat adtak (sRGB ~180/177/172, kék árnyalattal) és sötét kékesszürke padlót. Ez a Gate szerint falszín- és padlóhiba lett volna. Az expozíciósorozat (0–3, három kontrasztgörbe) után a +0,75 adja a fehér falat és a szürkésbarna padlót.

## Felületek – kamera szerint
| Felület | Cam_02 nappali → terasz | Cam_03 étkező → konyha | Cam_04 master (05.1) | Státusz |
|---|---|---|---|---|
| Padló | szürkésbarna sík tónus, sRGB ~144/140/136 | ~146/143/141 | ~143/139/136 | MEGLÉVŐ/MEGTARTOTT – csak tónus, **deszkaminta nincs modellezve**, Egger-dekor NEM IGAZOLT |
| Falak | fehér, ~202/199/195 | ~206/207/208 | ~203/200/196 | MEGLÉVŐ fehér; a halvány melegség a padlóról visszaverődő fény, nem festés |
| Mennyezet | fehér | fehér | fehér | MEGLÉVŐ; a hűtő-fűtő mező nem látszik (a kiállás-rétegben van) |
| Nyílászáró | belül fehér profil, 2,53 m-es teraszüvegfal | belül fehér | – | IGAZOLT-F (2026-10-21) |
| Beltéri ajtó | – | világosszürke lap, szürke tok | – | IGAZOLT-F |
| Konyha | – | **nincs konyhabútor** (a lakás konyha nélkül kerül átadásra), látszik a 85 cm-es fal | – | TERV SZERINT (KORR 2) |
| Kilátás | **nincs modellezve** – egyszínű világos égbolt; látszik a tetőkert (korlát, zöldtető, lépcső) | – | – | a valós kilátás csak a helyszíni videókból; generikus skyline tilos |
| Terasz | v2 tetőkert, változatlan | – | – | ELŐZETES (v2) |

## Képek
- `A902_Alap-v2b_blender_02_nappali-terasz.png`
- `A902_Alap-v2b_blender_03_etkezo-konyha.png`
- `A902_Alap-v2b_blender_04_master.png`
- `A902_Alap-v2b_blender_06_alaprajz-kiallasok.png`: **ellenőrző felülnézet, nem Astrának szól.** Workbench, 1 m-es rács, rajta a 130 kiállás és az 5 hűtő-fűtő mező. Az x/y koordináták megegyeznek a `01_alaprajzok/villamos_kiallasok/A902_villamos.csv` értékeivel.
- `render_log.json`: a futás pontos beállításai.

## Astrának – a B fázis promptjában kötelező
- Őrizze meg a falakat, nyílásokat, ajtókat, a kamera nézetét és a padló szürkésbarna tónusát. A padló meglévő szürke tölgy parketta, nem beton és nem mikrocement.
- Új elem csak a reality card és a tételes lista szerint kerülhet a képre. Lámpa csak a mennyezeti kiállás helyére, kiállás-azonosítóval.
- A kilátás valós forrásból jöjjön (Budai hegyek, városi tetőtáj), ne kitalált.

## Észrevétel a kiállás-rétegből – tervezést érinti
A nappali, étkező, konyha és a három háló **mennyezeti lámpakiállása (ML03–ML08) a hűtő-fűtő mezőn belül van**. A csövek a födémben futnak. A lámpa rögzítőcsavarjait ezért csak akkor lehet behajtani, ha a helyszínen kiderül, hogy a dobozban van-e rögzítési pont (horog, csavarhely), és hogy a kiállás körül csőmentes-e a sáv: hőkamerával, fűtési üzemben. **Hétfőn ellenőrizendő.**
