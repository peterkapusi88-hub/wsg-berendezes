#!/usr/bin/env python3
"""R16J → parts_v1.json a S16 gyártási adatmodell sémájában (a S16 CAD/dokumentáció-lánc bemenete).

Bemenet: forras_R16J/ (r16_forras_javitas.py) + gyartasi_szabalyok_v1.json (R16 anyagokkal).
A S16 build_parts_v1.py segédfüggvényeit (él-szerep geometriából, méretblokk) importálja – azonos logika.
Él-jel: elsődlegesen az R16 edge mezője (R16 frame E1–E4 → globális irány → S16 E1–E4), anyag szerinti jellel;
a 15 mm-es lakkozott fiók-rétegeltnél (R16 edge = 0) a szabad élek 'L', a csatlakozók '0' (S16 M07 szabály).
"""
from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
S16_F1 = HERE.parents[1] / "S16_GYARTAS" / "10_F1_adatmodell"
sys.path.insert(0, str(S16_F1))
from s16_geom import IRANY_NEV, LocalFrame, Solid, box_mesh, build_solid, load_json, neg, sha256, vec_to_axis  # noqa: E402
import build_parts_v1 as S16B  # noqa: E402

SRC = HERE / "forras_R16J"
RULES = HERE / "gyartasi_szabalyok_v1.json"
MODEL_REV = "R16-J-GY-v1"


def r16_solid(p):
    """R16 lapalkatrész zárt teste: kontúros (sarokkivágásos hátlap) → kontúr-extrudálás; egyébként a pontos doboz (R16-ban minden
    más alkatrész derékszögű hasáb – a natív STL-visszaolvasás szerint is), ezért a dobozháló nem közelítés."""
    if p.get("outline"):
        return build_solid(p, None)
    return Solid.from_mesh(p["id"], box_mesh(p["box"]), "R16_doboz")


def moving_units(drawers):
    m = {}
    for d in drawers:
        for pid in d["moving"]:
            m[pid] = f"{d['id']}-FIOK"
    m["KI12-TV01F-01"] = "T-AJTO-BAL"
    m["KI12-TV01F-02"] = "T-AJTO-JOBB"
    return m


def r16_edge_flags(p):
    """R16 E1..E4 flagek globális (S16) irány szerint."""
    U, V = np.array(p["r16_frame"]["U"], float), np.array(p["r16_frame"]["V"], float)
    dirs = {"E1": vec_to_axis(-V), "E2": vec_to_axis(U), "E3": vec_to_axis(V), "E4": vec_to_axis(-U)}
    return {dirs[e]: p["r16_edge"][i] for i, e in enumerate(("E1", "E2", "E3", "E4"))}


def main():
    rules = load_json(RULES)
    parts = load_json(SRC / "parts.json")
    materials = {m[0]: m for m in load_json(SRC / "materials.json")}
    drawers = load_json(SRC / "drawers.json")
    moving = moving_units(drawers)
    nezetek = rules["koordinata_konvencio"]["nezetek"]
    jelmap = rules["el_jel_R16"]
    solids = {p["id"]: r16_solid(p) for p in parts}

    out = []
    for p in parts:
        pid = p["id"]
        exc = rules["a_oldal"]["kivetelek"].get(pid)
        a_n = exc["irany"] if exc else rules["a_oldal"]["alapertelmezes_tengely_szerint"][p["axis"]]
        fr = LocalFrame(p["box"], a_n, nezetek)
        # forrás-L/W/T a helyi rendszerből (a javított befoglalóból) – a QA ezt veti össze a listázott R16 mérettel
        p = dict(p, L=round(fr.L, 3), W=round(fr.W, 3), T=round(fr.T, 3))
        mat = rules["anyagok"][p["material"]]
        gt = rules["gyartasi_tipus"]["id"].get(pid) or rules["gyartasi_tipus"].get(p["kind"]) or rules["gyartasi_tipus"]["alapertelmezes"]
        is_sheet = gt not in rules["gyartasi_tipus"]["nem_lap_tipusok"]
        edges = S16B.edge_roles(pid, fr, solids, rules, moving)
        flags = r16_edge_flags(p)
        nyitott = []
        codes = {}
        for e, ed in edges.items():
            f = flags.get(ed["globalis_irany"])
            jm = jelmap.get(p["material"])
            if jm == "L_SZABAD":
                jel = "0" if ed["szerep"] == "CSATLAKOZO" else "L"
                ok = "R16 edge=0 (nincs élzárás); 15 mm rétegelt – szabad él csiszolt+lakk (S16 M07 szabály)"
            elif f is None:
                jel, ok = "0", "R16 edge = None (élkezelés nincs megadva)"
            else:
                jel = (jm or "0") if f else "0"
                ok = f"R16 edge={f}"
            codes[e] = jel
            ed["jel"] = jel
            ed["r16_edge_flag"] = f
            ed["indok"] = ok
            ed["elanyag"] = mat["elanyag"] if jel in ("V", "F", "L") else rules["el_kod_jelek"][jel]
            ed["elvastagsag_mm"] = mat.get("elvastagsag", 0.0) if jel == "V" else 0.0
            ed["gepi_utkozo"] = e in rules["gepi_utkozo"]["alapertelmezes"]
        if p["material"] == "M02":
            nyitott.append("Élkezelés: R16-ban nincs megadva (edge = None); M16-WALL szerint 'szélek zárása' – burkolat körbehajtás vagy festés műhelyi döntés.")
        if pid in ("KI12-TV01S-01", "KI12-TV01S-02", "KI12-TV01T-02"):
            nyitott.append("Látszó külső felület bronzbarna mintával (R16 face_finishes.json) az M03 hordozón – felületrendszer (fólia/festés/furnér) nyitott.")
        if p.get("outline"):
            nyitott.append("Hátlap-sarokkivágás (R16 notches.json): két egyenes vágás, CNC-szerszámút nincs kiadva.")
        if p["material"] in ("M01", "M01+nyomat", "M16-BRONZE", "M02"):
            nyitott.append("Nyers méret a S16 festett-MDF +10/+10 mm ráhagyási szabályával (becslés); R16: 'Élzárási ráhagyás és műhelyélkód még nem kiadott'.")
        if p["kind"] == "TV02-CAP":
            nyitott.append("3600 mm hosszú fedő: a becsült 2800 mm-es táblából nem jön ki – toldás vagy hosszú tábla (R12: '3600 mm tető lapkészlet') döntés.")
        # erezet
        gg = p.get("grain_global")
        grain_ax = None
        if gg == "Z":
            grain_ax = "U" if fr.u_ax in ("+Z", "-Z") else ("V" if fr.v_ax in ("+Z", "-Z") else None)
        elif gg == "LONG":
            grain_ax = "U" if fr.L >= fr.W else "V"
        size = S16B.size_block(p, fr, codes, edges, mat, rules)
        size["r16_listazott_xyt"] = p["r16_listed_xyt"]
        size["r14_raw_rule"] = p.get("raw_size_status")
        ops = []
        if p.get("outline"):
            for n in p["notches_r16"]:
                lb = fr.box_to_local([n["box_r16"][0], 418 - (n["box_r16"][1] + n["box_r16"][4]), n["box_r16"][2], *n["box_r16"][3:]])
                ops.append({"op": "KIMETSZES", "r16_muvelet": "SAROKKIVAGAS", "oldal": "A", "helyi_doboz": lb, "melyseg_mm": "atmeno", "r16_id": n["id"],
                            "megjegyzes": n["method"], "szerszam": None, "statusz": "NYITOTT – két egyenes vágás, nem MPR"})
        rec = {
            "id": pid, "cimke_id": f"{rules['cimke_azonosito']['elotag']}_{re.sub(r'[^A-Z0-9_-]', '_', pid.upper())}",
            "modell_revizio": MODEL_REV,
            "forras": {"r16_id": pid, "r16_revizio": p["r16_revision"], "r16_tipus": p["kind"]},
            "modul": p["modul"], "megnevezes": p["name"], "gyartasi_tipus": gt, "lap_alkatresz": is_sheet, "db": 1,
            "mozgo_egyseg": moving.get(pid),
            "anyag": {"kod": p["material"], "megnevezes": materials[p["material"]][1], "tipus": mat["tipus"],
                      "nevleges_vastagsag": mat["nevleges_vastagsag"], "latszo_felso_felulet": None, "alternativak": None, "kivitel": None},
            "meret": size,
            "befoglalo_globalis": p["box"],
            "helyi_rendszer": {"A_normal": a_n, "U": fr.u_ax, "V": fr.v_ax, "N": fr.n_ax,
                               "nullpont_globalis": [round(float(c), 3) for c in fr.origin], "leiras": nezetek[a_n]["leiras"]},
            "lapoldal": {"A": f"{a_n} ({IRANY_NEV[a_n]})", "B": f"{neg(a_n)} ({IRANY_NEV[neg(a_n)]})"},
            "elek": edges,
            "el_kod": "".join(codes[e] for e in ("E1", "E2", "E3", "E4")),
            "gepi_utkozo": rules["gepi_utkozo"]["alapertelmezes"],
            "szalirany": {"r14": p.get("r16_grain"), "helyi_tengely": grain_ax, "globalis": (fr.u_ax if grain_ax == "U" else fr.v_ax) if grain_ax else None,
                          "felulbiralva": None},
            "kontur": ({"van": True, "pontok": len(p["outline"]), "bbox_uv": [0.0, 0.0, round(fr.L, 3), round(fr.W, 3)],
                        "geometria": f"{SRC.name}/parts.json#{pid}.outline"} if p.get("outline") else {"van": False}),
            "muveletek": ops,
            "geometria_forras": solids[pid].method,
            "r14_megjegyzes": p.get("note", ""),
            "statusz": "TERVI ADATMODELL – nem gyártási kiadás",
            "nyitott": nyitott,
        }
        if p.get("outline"):
            a = np.asarray(p["outline"], float)
            rec["kontur"]["bbox_uv"] = [round(float(a[:, 0].min()), 3), round(float(a[:, 1].min()), 3),
                                        round(float(a[:, 0].max()), 3), round(float(a[:, 1].max()), 3)]
        out.append(rec)

    doc = {
        "modell": "R16 médiafal (Kyoto Ink, KI12/KI14/KI16) – gyártási adatmodell",
        "modell_revizio": MODEL_REV, "generalva": date.today().isoformat(), "generator": "r16_build_parts.py",
        "statusz": "TERVI ADATMODELL – nem gyártási kiadás; műhelyi konvenciók megerősítésre várnak",
        "forras": {"mappa": SRC.name, "eredeti": "forras_R16 (git execution/a902-s01-kyoto-ink-design-to-budget-20261026 @ 2514579, R16_feluletek_fiokok/data)",
                   "fajlok": {f.name: sha256(f) for f in sorted(SRC.glob("*.json"))}, "szabalyfajl": {RULES.name: sha256(RULES)}},
        "koordinata_konvencio": rules["koordinata_konvencio"], "el_kod_jelek": rules["el_kod_jelek"],
        "alkatreszek": out, "segedobjektumok_R14_jelenetbol": [],
    }
    (HERE / "parts_v1.json").write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    cols = ["cimke_id", "id", "modul", "megnevezes", "gyartasi_tipus", "anyag", "T", "kesz_L", "kesz_W", "nyers_L", "nyers_W",
            "szalirany", "A_oldal", "el_kod", "mozgo"]
    with (HERE / "parts_v1.csv").open("w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(cols)
        for r in out:
            m = r["meret"]
            w.writerow([r["cimke_id"], r["id"], r["modul"], r["megnevezes"], r["gyartasi_tipus"], r["anyag"]["kod"], m["kesz"]["T"],
                        m["kesz"]["L"], m["kesz"]["W"], m["nyers"]["L"], m["nyers"]["W"], r["szalirany"]["helyi_tengely"] or "",
                        r["helyi_rendszer"]["A_normal"], r["el_kod"], r["mozgo_egyseg"] or ""])
    print(f"OK: {len(out)} alkatrész → parts_v1.json")


if __name__ == "__main__":
    main()
