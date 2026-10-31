#!/usr/bin/env python3
"""R16J – visszaolvasó QA a parts_v1.json-ra. A S16 qa_parts_v1.py ellenőrzéseit importálja (azonos logika);
R16-specifikus: fiók-ellenőrzés az R16 névadással, front-anyag élkód, forrás-befoglaló és listázott méret összevetése.
Kimenet: qa_report.md / qa_report.json; kilépési kód 2, ha BLOKKOLÓ van."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S16_F1 = HERE.parents[1] / "S16_GYARTAS" / "10_F1_adatmodell"
sys.path.insert(0, str(S16_F1))
import qa_parts_v1 as Q  # noqa: E402
from s16_geom import build_solid, load_json  # noqa: E402
from r16_build_parts import r16_solid  # noqa: E402

FRONT_ANYAG = ("M01", "M01+nyomat", "M16-BRONZE")


def q_forras(doc, parts_src, qa):
    src = {p["id"]: p for p in parts_src}
    ids = {r["id"] for r in doc["alkatreszek"]}
    for pid in sorted(set(src) ^ ids):
        qa.add("BLOKKOLO", "Q05_MODELL_LISTA_HIANY", pid, "csak a forrásban vagy csak az adatmodellben szerepel")
    for r in doc["alkatreszek"]:
        p = src[r["id"]]
        d = float(np.abs(np.array(r["befoglalo_globalis"], float) - np.array(p["box"], float)).max())
        if d > 0.01:
            qa.add("BLOKKOLO", "Q05_MODELL_LISTA_ELTERES", r["id"], f"parts_v1 befoglaló ≠ forras_R16J box ({d:.3f} mm)")
        k = r["meret"]["kesz"]
        listed = sorted(p["r16_listed_xyt"])
        if any(abs(a - b) > 0.01 for a, b in zip(listed, sorted([k["L"], k["W"], k["T"]]))):
            qa.add("FIGYELMEZTETES", "Q05R_R16_LISTA_JAVITVA", r["id"],
                   f"R16 listázott {p['r16_listed_xyt']} hibás → kész {k['L']:g}×{k['W']:g}×{k['T']:g} a befoglalóból (javitasi_naplo.json)")


def q_fiok_r16(doc, drawers, rules, qa):
    B = rules["qa"]["blum_movento"]
    P = {r["id"]: r for r in doc["alkatreszek"]}
    for d in drawers:
        did = d["id"]
        n = did[1]
        L, R, BB = P.get(f"KI16-{did}-L"), P.get(f"KI16-{did}-R"), P.get(f"KI16-{did}-B")
        sides = sorted([r for r in doc["alkatreszek"] if r["modul"] == did and r["forras"]["r16_tipus"] == "TV02-S"],
                       key=lambda r: r["befoglalo_globalis"][0])
        if not (L and R and BB) or len(sides) != 2:
            qa.add("BLOKKOLO", "Q13_FIOK_ALKATRESZ_HIANY", did, "hiányzó fiók-/korpuszalkatrész")
            continue
        CL, CR = sides
        if d["SKW"] != d["LW"] - B["SKW_eq_LW_minus"]:
            qa.add("HIBA", "Q13_BLUM_SKW", did, f"SKW {d['SKW']} ≠ LW {d['LW']} − {B['SKW_eq_LW_minus']}", forras=B["forras"])
        lw_geo = CR["befoglalo_globalis"][0] - (CL["befoglalo_globalis"][0] + CL["befoglalo_globalis"][3])
        skw_geo = R["befoglalo_globalis"][0] - (L["befoglalo_globalis"][0] + L["befoglalo_globalis"][3])
        if abs(lw_geo - d["LW"]) > 0.01:
            qa.add("HIBA", "Q13_LW_GEOMETRIA", did, f"korpusz belső szélesség {lw_geo} ≠ LW {d['LW']}")
        if abs(skw_geo - d["SKW"]) > 0.01:
            qa.add("HIBA", "Q13_SKW_GEOMETRIA", did, f"fiók belső szélesség {skw_geo} ≠ SKW {d['SKW']}")
        side_len = L["befoglalo_globalis"][4]
        if abs(side_len - (d["NL"] - B["fiokoldal_hossz_eq_NL_minus"])) > 0.01:
            qa.add("HIBA", "Q13_BLUM_OLDALHOSSZ", did, f"fiókoldal mélysége {side_len} ≠ NL {d['NL']} − {B['fiokoldal_hossz_eq_NL_minus']}", forras=B["forras"])
        if L["meret"]["kesz"]["T"] > B["oldal_max_vastagsag"]:
            qa.add("HIBA", "Q13_BLUM_OLDALVASTAGSAG", did, f"fiókoldal {L['meret']['kesz']['T']} mm > {B['oldal_max_vastagsag']} mm")
        recess = BB["befoglalo_globalis"][2] - L["befoglalo_globalis"][2]
        if recess < B["fenek_besullyesztes_min_magassag"]:
            qa.add("HIBA", "Q13_BLUM_FENEK_BESULLYESZTES", did, f"fenék besüllyesztés {recess:.1f} mm < {B['fenek_besullyesztes_min_magassag']} mm")
        else:
            qa.add("INFO", "Q13_FIOK_OK", did, f"LW {lw_geo:g}, SKW {skw_geo:g}, oldal {side_len:g} (NL {d['NL']}), fenék besüllyesztés {recess:g} mm – MOVENTO szabályok szerint")


def q_el_r16(doc, rules, qa):
    allowed = set(rules["el_kod_jelek"]) - {"etalon_megfeleltetes"}
    for r in doc["alkatreszek"]:
        code = r["el_kod"]
        if len(code) != 4 or any(c not in allowed for c in code):
            qa.add("BLOKKOLO", "Q19_EL_KOD_FORMATUM", r["id"], f"érvénytelen él-kód '{code}'")
        for e, ed in r["elek"].items():
            if ed["szerep"] == "SZABAD_ELOL" and ed["jel"] == "0" and r["lap_alkatresz"] and r["anyag"]["kod"] not in ("BEECH18", "PLY18", "M03-8"):
                qa.add("HIBA", "Q19_LATSZO_EL_KEZELETLEN", r["id"], f"{e} ({ed['irany_nev']}) szabad elülső él élkezelés nélkül")
        if r["anyag"]["kod"] in FRONT_ANYAG and "0" in code and r["mozgo_egyseg"]:
            qa.add("HIBA", "Q19_FRONT_EL_KEZELETLEN", r["id"], f"front él-kódja {code}")


def run(parts_path):
    doc = load_json(parts_path)
    rules = load_json(HERE / "gyartasi_szabalyok_v1.json")
    src = HERE / doc["forras"]["mappa"]
    parts_src = load_json(src / "parts.json")
    materials = load_json(src / "materials.json")
    drawers = load_json(src / "drawers.json")
    sb = {p["id"]: p for p in parts_src}
    solids = {r["id"]: r16_solid(sb[r["id"]]) for r in doc["alkatreszek"]}
    qa = Q.QA()
    Q.q_meretek(doc, qa)
    Q.q_nyers_vs_kesz(doc, rules, qa)
    Q.q_lwt_box(doc, qa, rules["qa"]["tures_mm"])
    q_forras(doc, parts_src, qa)
    Q.q_kontur(doc, qa, rules["qa"]["mesh_tures_mm"])
    Q.q_vastagsag(doc, rules, qa)
    Q.q_id(doc, rules, qa)
    Q.q_anyag(doc, materials, rules, qa)
    Q.q_lapmeret(doc, rules, qa)
    npairs = Q.q_utkozes(doc, solids, rules, qa)
    front_rows = Q.q_frontres(doc, solids, rules, qa)
    q_fiok_r16(doc, drawers, rules, qa)
    Q.q_fiok_mozgas(doc, drawers, solids, rules, qa)
    Q.q_mennyezet(doc, rules, qa)
    q_el_r16(doc, rules, qa)
    Q.q_muveletek(doc, rules, qa)
    Q.q_geom_forras(doc, qa)
    meta = {"alkatresz": len(doc["alkatreszek"]), "vizsgalt_utkozo_par": npairs, "frontres_sorok": front_rows,
            "geometria_forrasok": dict(Counter(s.method for s in solids.values()))}
    return doc, qa, meta


def main():
    doc, qa, meta = run(HERE / "parts_v1.json")
    cnt = Q.write_report(doc, qa, meta, HERE / "qa_report.md", HERE / "qa_report.json")
    md = (HERE / "qa_report.md").read_text(encoding="utf-8")
    md = md.replace("# S16 F1 – QA-jelentés", "# R16J F1 – QA-jelentés").replace("`qa_parts_v1.py`", "`r16_qa.py` (a S16 qa_parts_v1.py ellenőrzéseivel)")
    md = md.replace("- Valós pánt/sín kinematika, kábelpálya, LED-profilok és a 32 segédobjektum ütközése (csak a 120 fő alkatrész tömör geometriája).",
                    "- Valós pánt/sín kinematika, kábelpálya, LED-profilok, R16 hardware_geometry befoglalók ütközése (csak a 106 lapalkatrész).")
    md = md.replace("- Ajtónyitás (pánttípus és -oldal nincs véglegesítve) – 2. fázis gyári CLIP top geometriával.",
                    "- Ajtónyitás söpört térfogata (R16 pánt: Blum 70T3550.TL + 173H7100, gyári kinematika nélkül).")
    (HERE / "qa_report.md").write_text(md, encoding="utf-8")
    print(f"QA: {dict(cnt)}")
    return 2 if cnt.get("BLOKKOLO") else 0


if __name__ == "__main__":
    sys.exit(main())
