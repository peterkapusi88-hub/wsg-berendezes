WSG-RESULT: WSG-20261024-GEMINI-RENDER-TEST-002
Szerző-AI: Gemini webapp (Claude relay) + Péter kérésére ChatGPT-kontroll (Claude relay); audit és szöveg: Claude
Modell: Gemini „3.1 Pro” + „Kép létrehozása” eszköz (a képmodell neve a felületen nem látszik) | ChatGPT Chat mód, „Erős” gondolkodás, képmodell nem igazolt
Bázis-commit: 26a7b7e (prompt 2a504ec, Gemini-képek 35ef7f5, ChatGPT-képek 2653346)
Státusz: TELJES – a kért 2 Gemini-kép + jelentés, kiegészítve a ChatGPT-kontrollal

# A-902 Cam_02 – Rubin Szalon vs. Ezüst Orbit gyors stílusteszt (Gemini + ChatGPT), 2026-10-24

> **KONCEPCIÓ – NEM VALIDÁLT.** Gyors, összehasonlító stílusteszt. Egyik kép sem Render Reality Gate PASS, és mind a négy képben van Gate szerinti FAIL-elem (5. pont).

## 1. Röviden
- **Kamera:** egyik modell sem tartotta pontosan. A Gemini 16:9-re keretezte át (2752×1536). A ChatGPT megtartotta a 16:10-et (1586×992), és a **ChatGPT Rubin** áll a legközelebb a semleges nézethez. A szoba iránya mind a négy képen nagyjából megmaradt, de az üvegosztás és a hátsó falszakasz átíródott.
- **Melyik stílus működik jobban képen:** az **Ezüst Orbit**, mindkét modellben. A hátulvilágított kör tükör egyértelmű fókuszpont, és a világos paletta illik a panorámás penthouse-hoz. A Rubin három panelje filcnek, vászonképnek hat, a vörös panel + vörös függöny + vörös párna együtt pedig hotelszobás érzetet ad. Ez szubjektív értékelés. **Egyik kép sem éri el a „rohadt drágának néz ki” szintet**, ebben egyetértek Péterrel.
- **Gemini vagy a prompt?** Mindkettő, de **elsősorban a prompt és maga a pilotkoncepció.** Ugyanarra a promptra a ChatGPT érezhetően drágábbnak ható képet adott: jobb fény, mélység, anyag és styling. A Gemini tehát ront a helyzeten, de a luxushiány a ChatGPT-képeken is látszik. Részletek a 7. pontban.

## 2. Mit és hogyan futtattam
- **Prompt:** a pilot (`ai-coordination/results/WSG-20261024-PILOT-001.md`, commit `f307765`, sha256 `5e2f3e82…`, változatlan) két angol renderpromptja szó szerint, géppel kiolvasva. Elé egy rövid **képjelmagyarázat** került, amely megmondja, melyik feltöltött kép mire való, mert a pilotprompt fájlnév nélkül hivatkozik a referenciákra. A teljes beküldött szöveg: `05_promptok/A902_Cam02_RubinSzalon_EzustOrbit_gemini_koncepcioteszt_v1.md`.
- **Bemenet, mind a 4 futásnál azonos sorrendben:**
  1. `04_renderek/semleges/A902_semleges_1_nappali.jpg` (geometria + kamera);
  2. ME-BAL-080 (padló, szegőléc);
  3. ME-BAL-045 (fehér fal, belül fehér profil, ajtó, greslap/WPC);
  4. ME-BAL-006 (tetőkert);
  5. `A902_terasz_panorama_v0b_videobol.jpg` (kilátás).

  A kamerához illesztett, javított teraszháttér **nem létezik** (a pilot Claude-auditjának 4.1 pontja szerint KIMARAD), ezért a 3–5. kép volt a valós külső referencia.
- **Gemini:** gemini.google.com, peter.kapusi88 fiók (Google AI Plus). Két külön új csevegés, Gem nélkül. Modellválasztó: „3.1 Pro”, gondolkodás: „Alacsony” (alapértelmezett). Eszköz: „Kép létrehozása”, képek száma 1, méretarány nem választva (16:10 nincs a kínálatban), stíluspreset nincs. Beküldés: Rubin 08:24, Orbit 08:27.
- **ChatGPT (Péter kérésére, 08:29):** chatgpt.com, Chat mód (a Work-keret 11:50-ig elfogyott, a felület szerint). Gondolkodás: „Erős”, eszköz: „Kép létrehozása”, két külön csevegés. Beküldés: Rubin 08:43, Orbit 08:49 (1 p 9 mp). Az Orbit-futásnál a ChatGPT az 1. képet `A902_semleges_1_nappali(1).jpg` néven mutatta, mert ilyen nevű fájl már volt a fiókban. A sorrend azonos.
- **Átvétel:** a teljes méretű eredeti fájlok változatlan bájtokkal, Chrome-relay-jel kerültek a GitHub webes feltöltőjébe. A ChatGPT-PNG-k C2PA-blokkot (`caBX`) tartalmaznak, tehát eredeti generált fájlok. Közben a Gemini letöltés gombja a két JPEG-et valószínűleg a Mac `~/Downloads` gyökerébe is lementette. Ezt nem tudtam ellenőrizni, mert oda nincs hozzáférésem.

## 3. Kimenetek
| Fájl | Méret | Bájt | sha256 (eleje) |
|---|---|---:|---|
| `04_renderek/ai_gemini/A902_RubinSzalon_1_nappali_gemini.jpg` | 2752×1536 | 2 441 762 | `4d82f2d5` |
| `04_renderek/ai_gemini/A902_EzustOrbit_1_nappali_gemini.jpg` | 2752×1536 | 2 485 049 | `1c598cba` |
| `04_renderek/ai_chatgpt/A902_RubinSzalon_1_nappali_chatgpt.png` | 1586×992 | 2 664 776 | `5447a300` |
| `04_renderek/ai_chatgpt/A902_EzustOrbit_1_nappali_chatgpt.png` | 1586×992 | 2 354 880 | `2a5f172f` |
| `04_renderek/ai_gemini/A902_Cam02_RubinSzalon_EzustOrbit_gemini_vs_chatgpt_osszehasonlitas.jpg` | lap | | bemenet + 4 kép |
| `04_renderek/ai_gemini/A902_Cam02_kamerahuseg_atfedes.jpg` | lap | | kamerahűségi átfedés |

A javasolt `.png` helyett a Gemini-képek `.jpg`-ként szerepelnek, mert a Gemini eredetije JPEG. Átkódolva nem lettek, a kiterjesztés a valós formátumot mutatja.

## 4. Kamerahűség (mérés)
Módszer: a semleges render fal-, mennyezet-, padló- és üvegfal-élei (Canny) a generált képre vetítve, azonos kamerát feltételezve. A mérőszám az átlagos élponttávolság 800 px-es szélességen (chamfer). Önkontroll: a semleges kép önmagával **3,3 px**, ez a mérés alsó határa. A tájolópontok kézzel, %-os rácson mérve, ±1–2%.

| | Képarány | Chamfer, azonos kamera | Bal oldali sarok x | Üvegfal bal kávája x | 1. osztóborda x | Megjegyzés |
|---|---|---:|---:|---:|---:|---|
| **Semleges Cam_02** | 16:10 | 3,3 (önkontroll) | 47% | 53,5% | 67,5% | 2. borda 91%-nál |
| Gemini Rubin | **16:9** | 11,7 | ~46,5% | ~56% | ~66,5% | a hátsó falszakaszt függöny takarja |
| Gemini Orbit | **16:9** | 10,7 | ~45% | ~55% | ~65,5% | **kitalált ajtó** a sarok és az üvegfal között |
| ChatGPT Rubin | 16:10 | **6,5** | ~46,5% | ~55% | ~68,5% | a legközelebbi; a mennyezetvonal laposabb (más dőlés vagy fókusz) |
| ChatGPT Orbit | 16:10 | 9,7 | ~42% | ~59% | ~67% | a kamera elmozdult, az üvegfal nagyobb |

**Ítélet: nem sikerült pontosan ugyanazt a kamerát tartani.** Mindkét modell „hasonló nézetet” rajzol, nem azonos vetítést. A 16:9-es Gemini-kimenet eleve nem lehet azonos képkivágás. Látványhoz ez elég, kivitelezési összevetéshez nem. Bizonyíték: `A902_Cam02_kamerahuseg_atfedes.jpg`.

## 5. Render Reality Gate C – eltéréslista (rövid)
| Elem (előírás) | Gemini Rubin | Gemini Orbit | ChatGPT Rubin | ChatGPT Orbit |
|---|---|---|---|---|
| Padló (Grey Treviso, greige-szürke, csomós) | kékes-hideg (b\* −8,8), világos | kékes-hideg (b\* −8,8), erős erezet | **legközelebb** (b\* −1,6), meleg szürkésbarna | enyhén hideg (b\* −4,6) |
| Belső profil fehér | ✓ | ✓ | ✓ | **✗ fekete** (az 1. képet követte) |
| Üvegosztás (3 mező) | átrajzolva (tolóajtó + fátyol mögött) | átrajzolva | ≈ tartva (borda 1%-on belül) | ≈ 3 mező, a bal káva eltolva |
| Hátsó falszakasz, ajtó | függöny takarja | **✗ kitalált világosszürke ajtó** | függöny takarja | függöny takarja |
| Falak fehérek | ✓ | ✓ | fényhatástól meleg tónusú (nem festés) | ✓ |
| Terasz (előtér greslap −15 cm, WPC +62 cm, szegély, domb) | ültetőpárkány a padlószinten, a szintek nem valósak | **sötét WPC közvetlenül kint** (valójában greslap) | világos burkolat + párkány, a szintek nem valósak | világos burkolat, WPC-lépcső látszik, a szintek nem valósak |
| Kilátás (budai hegyek) | ✓ közelítő | ✓ + **daru és sárga tábla** | ✓ a legjobb | ✓ |
| Kanapé (szürke, 240×100×69 burok) | ✓ háromszemélyes | rövidebbnek tűnik (≈2,5 személyes) | nagy, greige felé hajló | nagy, szürke |
| Hős-elem | 3 panel, filces hatás | Ø140-es tükör, halo ✓ | 3 panel, **nagyobb** a 60×120 cm-esnél | tükör + halo ✓ |
| Asztal(ok) | átlátszó üveg (nem füstüveg) | 2 kerek, fémlábas | füstüveg ✓ + könyvek | **tömör dobok** (nem élzárt HPL-lap) + váza |
| Állólámpa | ✗ csupasz rúd | ✗ L-alakú, a közlekedőben | ✓ | ✓ |
| Fény (semleges nappali + 2700 K) | lapos | ✓ semleges | ✗ meleg délutáni napfény | ✓ |
| Extra tárgyak | nincs | nincs | párnák, könyvek | pléd, párnák, váza, könyvek |

A padlószín b\* értéke Lab-átlag a padlófelületről. Valós referencia: ME-BAL-046 in situ, b\* ≈ 0,1. A világosság (L\*) a megvilágítástól függ, ezért ezt nem hasonlítom.

**Gate-státusz:** mind a 4 kép `KONCEPCIÓ – NEM VALIDÁLT`. Kivitelezési jelöltként továbbvinni csak javítással lehetne, ezért Gate-szinten mind `FAIL – ÚJRATERVEZÉS`. Fő okok:
- Gemini Orbit: kitalált ajtó;
- ChatGPT Orbit: fekete profil;
- mind a négy képen nem valós teraszszintek és nem igazolt padló.

## 6. Használhatóság a továbbfejlesztéshez (1–5)
| Kép | Pont | Mire jó |
|---|---:|---|
| ChatGPT Ezüst Orbit | 3 | Hangulat- és stílusreferencia Astrának (fény, tömegarány, tükör). Geometriai alapnak nem jó: fekete profil, elmozdult kamera, extra dekor, a dobasztal eltér a specifikációtól. |
| ChatGPT Rubin Szalon | 3 | A legjobb kamera- és üvegosztás-egyezés. Arra mutat rá, mennyit dob a fény a Rubinon. A panelméret és a meleg fény nem a briefé. |
| Gemini Rubin Szalon | 2 | A kompozíció nagyjából megvan, de lapos fény, kékes padló és csupasz rúdlámpa miatt ez hat a legolcsóbbnak. |
| Gemini Ezüst Orbit | 1 | A kitalált ajtó miatt értékelhetetlen. Legfeljebb a tükör-halo részlet használható belőle. |

## 7. Gemini vagy a prompt? – diagnózis
**Prompt- és koncepciószintű okok (mindkét modellnél hatottak):**
1. **Kevés luxusforrás.** A koncepció egy üres fehér dobozban egy hétköznapi kanapé, egy falitárgy, egy asztal, függöny és egy lámpa. Nincs rétegzett fényterv, beépített bútortömeg, TV-/médiafal, anyagrétegzés vagy fotós képi irány. A pilot Claude-auditja ezt előre jelezte (WOW 5–6/10, „inkább ízléses, mint drága”).
2. **Tiltólista-prompt.** A szöveg nagyjából fele azt sorolja, mit ne csináljon a modell. Hiányoznak a pozitív minőségi leírások (fényminőség, árnyék, anyagtextúra, fotós stílus), ezért mindkét modell átlagos lakásfotót rajzolt.
3. **Konkrét sorok, amelyek hibát okoztak:**
   - „Retain the existing light-grey interior doors where visible”: a Cam_02-ben nem látszik ajtó, a Gemini mégis rajzolt egyet (lásd a lenti idézetet);
   - „cool grey … flooring”: kékes padló;
   - „Use only the supplied camera-matched corrected terrace background”: ilyen fájl nincs;
   - az alapkép fekete profilja: a ChatGPT Orbit a képet követte, nem a szöveget („a kép erősebb a szövegnél”, audit 4.1).

**Modellszintű okok:**
- **Gemini:**
  - **átírja a promptot**, mielőtt a képmodellnek adja. Az Ezüst Orbit átírt változatában ez áll: *„An interior door, partially visible in a hallway to the back-left, is a flat light-grey.”* Az átírásban a képindexek is összecserélődtek (a profilt a padlóképhez, a szegőlécet a helyszínfotóhoz kötötte). Mindkét átírt szöveg a függelékben;
  - 16:9-re keretezett át;
  - laposabb, „renderes” fény és anyag.
- **ChatGPT:**
  - drágábbnak ható fény és styling;
  - kéretlen dekor;
  - az Orbitnál a fekete profil és a kameraelmozdulás.

**Következtetés:** a luxushiány fő oka a prompt és a koncepció, a „gagyi” renderérzetet a Gemini tovább rontja. Ez cellánként 1-1 minta, tehát irányjelző, nem statisztikai eredmény.

## 8. Javaslat a következő körre (nem új stílus, csak a tanulság)
1. **Javított alapkép Blenderből** (audit 4.1, függő): fehér belső profil, valós padlótónus, v2 terasz, a bútorok valós méretű tömegként. Ez a geometria legerősebb kontrollja, mert a kép erősebb a szövegnél.
2. **Prompt v2 Astrának:**
   - pozitív luxusblokk (fényterv, anyagtextúra, fotós képi irány);
   - Cam_02-re: „a hátsó falszakaszon nincs ajtó”;
   - a padló legyen „greige-szürke, csomós tölgy”, ne „cool grey”;
   - a teraszszintek szövegesen (greslap −15 cm, WPC +62 cm).
3. **Állóképhez** ebben a tesztben a ChatGPT adott jobb kiindulást. A Gemini maradjon a jóváhagyott képek videójára (`ROUTER.md`). Ezt Péter dönti el.

## 9. Ellenőrzések, amiket nem módosítottam
- **Mac-tükör** (`~/Downloads/wsg-berendezes`): **nem git-klón** (nincs `.git`), legutóbb 04:46-kor módosult, így elmarad a `main`-től. Nem írtam bele. A bemeneti képek a tükörben azonosak a repóval: négy sha256 alapján, egy bájtméret alapján, a semleges kép pedig pixelre azonos.
- **Élő Blender** (`~/Downloads/WSG_A902_stilusok.blend`): `is_dirty = true`, aktív kamera Cam_04. Nem nyúltam hozzá, nem mentettem, nem rendereltem. A Validator nem futott, mert Blender-változás nem történt.
- **Egyéb:** nem indítottam új AI-rendszert, és nem vásároltam kreditet. A Gemini új csevegésének beviteli mezőjében egy el nem küldött vázlat volt (a `05_promptok/A902_LakeForest_1_nappali_video_prompt_v1.md` szövege). Ezt töröltem, a repóban megvan.

## Függelék A – a Gemini saját, átírt képpromptja (a kép alt-szövegéből)
**Rubin Szalon**
> A photorealistic, daytime interior view of a contemporary living room, preserving the exact geometry, camera angle, ceiling, and walls from <IMAGE_0>, while applying a 'Ruby Salon' design concept. The room is now fully finished, featuring the cool grey knotty oak laminate flooring from <IMAGE_1>. The walls and ceiling are flat white, and the large sliding glass door has white interior frames, matching the trim and finishes in <IMAGE_2>. No trim is gold or brass.
>
> Visible through the large sliding glass window is the exterior roof garden seen in <IMAGE_3>, featuring natural earth, small green shrubs, and dry plantings, enclosed by a dark metal railing. In the distance, the hilly urban skyline of Budapest from <IMAGE_4> is visible under a clear, hazy daytime sky.
>
> To the left, a low-profile, multi-seater grey fabric sofa is placed flush against the wall. Mounted on the white wall directly above the sofa are three separate, vertical ruby-red upholstered textile panels, evenly spaced with narrow slivers of the white wall showing between them. In front of the sofa sits a rectangular coffee table made of smoked glass with a dark, simple metal frame. On the floor is a textured, medium-grey area rug of limited size, sitting beneath the coffee table and partially under the sofa.
>
> The large window is dressed with soft, semi-translucent white sheer curtains that are partially drawn, alongside rich ruby-red side curtains that are gathered and tied back, completely clear of the glazing. At the corner where the window meets the left wall, a slender, minimalist dark-toned floor lamp stands, casting a very subtle, warm 2700K glow.
>
> The space is empty of people, captured in natural, soft daylight with very restrained warm practical lighting, maintaining a lived-in yet uncluttered, contemporary aesthetic. The space is completely devoid of marble, gold, or extra seating like armchairs.

**Ezüst Orbit**
> A photorealistic concept image of a modern living room in a 'Silver Orbit' style, strictly preserving the exact interior geometry, camera perspective, and window configuration of <IMAGE_0>.
>
> The room is rendered with realistic materials, lighting, and finishes. The walls and flat ceiling are painted smooth matte white, matching the interior window and sliding door frames (<IMAGE_1>). An interior door, partially visible in a hallway to the back-left, is a flat light-grey. The floor is covered in cool grey, knotty oak laminate planks with a natural, slightly textured grain, accompanied by a matching low-profile skirting board (<IMAGE_2>) running along the base of the white walls.
>
> Along the solid left wall is a low, modern sofa upholstered in textured mid-grey fabric with plush, square cushions. Directly above the sofa, mounted flat against the white wall, is a large, circular mirror about 140 cm in diameter with a very thin silver or brushed-metal frame, illuminated from behind by a soft, warm (2700K) halo backlighting that spills onto the wall.
>
> In front of the sofa on a pale-grey, low-pile rectangular rug of limited size are two offset circular coffee tables of varying heights. They have matte graphite laminate surfaces with visible edge banding and are supported by slender dark metal legs. Near the edge of the rug sits a very slim, minimalist dark floor lamp with a delicate arm.
>
> The large sliding glass doors and side windows on the right (<IMAGE_0>) are dressed with layered window treatments: sheer white curtains hanging from a recessed ceiling track, partially drawn to the side, paired with ice-blue side curtain panels that rest near the corners.
>
> Visible through the expansive glass is a realistic rooftop garden on the terrace, meticulously detailed based on <IMAGE_3> and <IMAGE_4>:
> - The outdoor terrace features dark-grey WPC (wood-plastic composite) decking with thin parallel grooved lines.
> - Concrete edging borders a raised, organic-shaped planted mound filled with dark mulch, pebbles, and sparse, naturalistic roof vegetation, including small green shrubs, grasses, and dried plants. A black drip irrigation hose is visible looping through the garden area.
> - A dark anthracite metal railing with vertical balusters (<IMAGE_3>) secures the terrace.
> - Beyond the railing, the expansive, slightly hazy view of Budapest’s distant Buda hills dotted with densely packed buildings, alongside urban rooftops and construction or infrastructure elements, is clearly visible under a natural, soft daylight sky (<IMAGE_4>).
>
> The scene has natural, indirect daylight pouring through the glass, highlighting the textures of the laminate floor, fabric, and outdoor elements. There are no other furniture pieces, no ceiling light fixtures, no gold or marble finishes, and no people present.

A ChatGPT átírt promptja a felületen nem látszik. A „Worked for 1m 9s” panel csak ennyit mutat: „Prepared the room visualization”, „Refined the render”.
