# R16J – gyártási adatréteg (F1 + F2b)

Készült: 2026-10-30, Claude. Státusz: **TERVI ADATMODELL – nem gyártási kiadás.** Cél: a S16-hoz épült CAD/dokumentáció-lánc (`f2_cad_export.py`, `f34_dokumentacio.py`) ugyanazzal a sémával fusson az R16 médiafalra is.

## Futtatás (sorrendben)

```
cd 10_F1_adatmodell && python3 r16_forras_javitas.py && python3 r16_build_parts.py && python3 r16_qa.py
cd ../30_F2b_vasalat && python3 r16_vasalat.py
cd .. && python3 ellenorzes.py      # független önellenőrzés, 0 = rendben
```

A szkriptek a `../S16_GYARTAS/10_F1_adatmodell/` modulokat importálják (s16_geom, build_parts_v1 él-szerep/méret, qa_parts_v1 ellenőrzések) – a S16 fájlokat nem módosítják.

## Fájlok

| Fájl | Tartalom |
|---|---|
| `10_F1_adatmodell/forras_R16/` | R16 eredeti (git `2514579`, `R16_feluletek_fiokok/data` + audit + MPR_KORLATOK), `SHA256SUMS` |
| `10_F1_adatmodell/forras_R16J/` | javított forrás R14/S16-formátumban: parts.json, materials.json, drawers.json, layout.json, üres zárt jelenet, `javitasi_naplo.json` |
| `10_F1_adatmodell/gyartasi_szabalyok_v1.json` | R16 szabályfájl (S16 műhelyi feltételezései R16 anyagkódokra, élkód-leképezés, A-oldal kivételek) |
| `10_F1_adatmodell/parts_v1.json` / `.csv` | gyártási adatmodell a S16 sémájában (106 alkatrész, címke `R16_<id>`) |
| `10_F1_adatmodell/qa_report.md/.json` | QA: 0 BLOKKOLÓ, 2 HIBA (valós nyitott), 12 FIGYELMEZTETÉS (a javított listaméretek) |
| `30_F2b_vasalat/vasalat_terv.json`, `vasalat_jelentes.md` | 956 furat és 395 vasalat-tétel a S16 sémájában, az R16 saját furatadataiból |
| `ELTERES_JELENTES.md` | R16 eredeti ↔ javított: a 12 méreteltérés, egyéb javítások, `??` MPR-hiba |
| `ellenorzes.py` | független önellenőrzés (hash, méret, befoglaló, furat-helyzet) |

## Számok

- Alkatrész: 106 (modul: {'TORONY': 22, 'ALSO_KERET': 1, 'HATTER': 5, 'D1': 13, 'D2': 13, 'D3': 13, 'D4': 13, 'D5': 13, 'D6': 13})
- Anyag: {'M03': 33, 'M01+nyomat': 2, 'M03-8': 7, 'M01': 7, 'M02': 4, 'M16-BRONZE': 1, 'BEECH18': 14, 'PLY18': 8, 'M16-DRAWER15': 30}
- Furat funkciónként: BRONZ_MF375_PILOT 8, CAMAR807_DUBEL 56, FIOK_ELO_HAT_ATMENO 48, FIOK_ELO_HAT_PILOT 48, FIOK_FENEK_ATMENO 36, FIOK_FENEK_PILOT 36, FRONT_ROGZITES_ATMENO 24, FRONT_ROGZITES_PILOT 24, HATLAP_LEC 100, LEC_OLDAL 100, MF375_PANEL_CSAVAR 96, PANTKEHELY 10, PANTTALP 20, PANT_CSAVAR 20, POLCTARTO 40, SERVICE_KABEL 2, SERVICE_M4_ATMENO 8, TIPLI_EL 138, TIPLI_LAP 138, TIPON_ADAPTER 4
- Vasalat: TIPLI_D8x30 138, CSAVAR_4x35 84, MF375 52, POLCTARTO 40, CSAVAR_4x30 24, 760H3000S 12, 80702Z1IN_SX_DX 12, PANT_CLIPTOP_110 10, LOOX5_2194___LED3040__833_89_253 8, SR_ZG9101FA_DIM 3, 897ASZ11212 2, 956A1004___956A1201 2, 2MM_SZERELOLEMEZ_4SAROK_TAVTARTO 2, 80702Z1INSX 1, 80702Z1INDX 1, 3836050___TVM3605 1, QE65Q7FAAUXXH 1, LPV_150_24 1, 18X18_SAROKPROFIL_8MM_SZALAG_DIFFUZOR__M 1
- Átmenő furat (szándékos: csavar-átmenő, hátlap, kábel): 218 – `atmeno: true` mező jelöli

## Feltevések és nyitott tételek

- **Falsík:** Y_S16 = 418 − Y_R16 (FELTEVÉS, lásd ELTERES_JELENTES 4.).
- **Anyagkódok:** M01/M01+nyomat/M02/M03 az R16 materials.json-ban nincs definiálva; a face_finishes/M16-* leírásokból azonosítva (napló). 8 mm-es M03 hátlap → `M03-8`.
- **Élkód:** az R16 `edge` mezőjéből (R16 frame → globális irány → S16 E1–E4); M03 → V, festett MDF → F, fiók-rétegelt szabad él → L; M02 dekorpanel élkezelése NYITOTT (R16: None).
- **Nyers méret / ráhagyás / lapformátum:** a S16 szabályai átvéve, becslés (R16: „élzárási ráhagyás és műhelyélkód még nem kiadott”).
- **Pánt:** az R16 saját választása maradt – Blum 70T3550.TL + 173H7100 (5+5 db, B = 5,5 mm), mert konkrét, forrásolt cikkszám; a S16 döntése után egyeztetendő.
- **Csap:** Ø8×30 bükk (R16/R12), tipus `TIPLI_D8x30` – nem a S16 `TIPLI_D8x35`.
- **MOVENTO 760H3000S / T51.7601 / TIP-ON / ZS7M400MU gyári sablonfuratok:** nincsenek koordinátával (R16 pending_hardware_operations) – nem találtuk ki.
- Fedő 3600 mm táblaméret, mennyezeti rés 20 mm, tusgrafika nyomatpróba, bronz felületrendszer a torony M03 külső oldalain – nyitott.

