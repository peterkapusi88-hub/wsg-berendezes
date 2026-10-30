#!/usr/bin/env python3
"""R16J F2b – vasalat- és furatterv a S16 vasalat_terv.json sémájában.

Elsődleges forrás az R16 saját adata (forras_R16: holes.json 956 furat, hinges.json, shelf_pins.json, new_connections.json,
hardware_geometry.json, pending_hardware_operations.json) – új furatot NEM találunk ki. Transzformáció a S16 konvencióba:
X = X, Z = Z, Y_S16 = 418 − Y_R16, irány: (ax, −ay, az). Minden furatot ellenőrzünk a javított alkatrész-testen:
a kezdőpont a lap felületén, a furat tengelye az anyagban, vakfurat mögött ≥ 5 mm marad (S16 f2b szabály).
Funkciónevek: a S16-tal közös nevek (TIPLI_EL/TIPLI_LAP, PANTKEHELY, PANTTALP, POLCTARTO), a többi az R16 név ASCII-ra igazítva.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
F1 = HERE.parent / "10_F1_adatmodell"
S16_F1 = HERE.parents[1] / "S16_GYARTAS" / "10_F1_adatmodell"
sys.path.insert(0, str(S16_F1))
sys.path.insert(0, str(F1))
from s16_geom import LocalFrame, load_json  # noqa: E402
from r16_build_parts import r16_solid  # noqa: E402

FAL_Y = 418.0
MIN_MARADEK = 5.0
SRC = F1 / "forras_R16"


def to_s16(p):
    return [float(p[0]), round(FAL_Y - float(p[1]), 4), float(p[2])]


def dir_s16(v):
    return [float(v[0]), -float(v[1]), float(v[2])]


def ascii_name(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^A-Z0-9_]", "_", s.upper())


def main():
    doc = load_json(F1 / "parts_v1.json")
    rules = load_json(F1 / "gyartasi_szabalyok_v1.json")
    nez = rules["koordinata_konvencio"]["nezetek"]
    R = {r["id"]: r for r in doc["alkatreszek"]}
    FR = {k: LocalFrame(r["befoglalo_globalis"], r["helyi_rendszer"]["A_normal"], nez) for k, r in R.items()}
    srcj = {p["id"]: p for p in load_json(F1 / "forras_R16J" / "parts.json")}
    SOL = {k: r16_solid(srcj[k]) for k in R}
    H = load_json(SRC / "holes.json")
    hinges = load_json(SRC / "hinges.json")
    pins = load_json(SRC / "shelf_pins.json")
    newc = load_json(SRC / "new_connections.json")
    hwg = load_json(SRC / "hardware_geometry.json")
    pend = load_json(SRC / "pending_hardware_operations.json")

    problems = []
    holes = []
    byid = {}
    for h in H:
        pid = h["part"]
        if pid not in R:
            problems.append({"sulyossag": "BLOKKOLO", "alkatresz": pid, "uzenet": f"{h['id']}: ismeretlen alkatrész"})
            continue
        fr = FR[pid]
        st = np.array(to_s16(h["xyz"]))
        d = np.array(dir_s16(h["axis"]))
        loc = fr.to_local(st)
        ld = np.array([d @ fr.U, d @ fr.V, d @ fr.N])
        k = int(np.argmax(np.abs(ld)))
        extent = [fr.L, fr.W, fr.T][k]
        base = ascii_name(h["kind"].split(" ")[0])
        if base in ("CSAP", "MEREVITO_CSAP"):
            funk = "TIPLI_LAP" if k == 2 else "TIPLI_EL"
        else:
            funk = {"PANT_CSESZE": "PANTKEHELY", "PANT_CSAVAR_ELOFURAT": "PANT_CSAVAR", "TALP_CSAVAR_ELOFURAT": "PANTTALP"}.get(base, base)
        rec = {"alkatresz": pid, "cel": "lap" if k == 2 else "él", "start": [round(float(c), 3) for c in st],
               "irany": [round(float(c), 6) for c in d], "d": float(h["diameter"]), "melyseg": float(h["depth"]),
               "funkcio": funk, "kapcsolat": h["id"], "helyi": [round(float(c), 3) for c in loc],
               "r16_id": h["id"], "r16_kind": h["kind"], "r16_forras": h["source"], "atmeno": bool(h["depth"] >= extent - 1e-6)}
        # ellenőrzés: kezdőpont a befoglalón (felületen), tengely az anyagban, maradék anyag
        tol = 0.05
        inb = all(-tol <= loc[i] <= [fr.L, fr.W, fr.T][i] + tol for i in range(3))
        onsurf = abs(loc[k]) < tol if ld[k] > 0 else abs(loc[k] - extent) < tol
        if not inb or not onsurf:
            problems.append({"sulyossag": "BLOKKOLO", "alkatresz": pid, "uzenet": f"{h['id']} {funk}: a kezdőpont nem a lap felületén (helyi {rec['helyi']})"})
        sol = SOL[pid]
        dep = min(h["depth"], extent)
        inner = st + d * np.linspace(0.3, dep - 0.3, 5)[:, None]
        if not sol.contains(inner).all():
            problems.append({"sulyossag": "BLOKKOLO", "alkatresz": pid, "uzenet": f"{h['id']} {funk}: a furat tengelye részben az anyagon kívül"})
        if rec["atmeno"]:
            szandekos = "ATMENO" in base or base in ("HATLAP_LEC", "LEC_OLDAL", "SERVICE_M4_ATMENO", "SERVICE_KABEL")
            if h["depth"] > extent + 1e-6:
                problems.append({"sulyossag": "FIGYELMEZTETES", "alkatresz": pid,
                                 "uzenet": f"{h['id']} {funk}: mélység {h['depth']} > anyag {extent:g} mm a fúrás irányában – átmenő, a túlnyúlás a következő alkatrészbe megy"})
            elif not szandekos:
                problems.append({"sulyossag": "HIBA", "alkatresz": pid, "uzenet": f"{h['id']} {funk}: átmenő ({h['depth']} mm / {extent:g} mm), nem átmenőnek jelölt"})
        else:
            behind = st + d * (h["depth"] + MIN_MARADEK - 0.3)
            if not sol.contains(behind[None, :])[0]:
                maradek = extent - h["depth"]
                problems.append({"sulyossag": "HIBA", "alkatresz": pid,
                                 "uzenet": f"{h['id']} {funk}: a furat mögött {maradek:g} mm < {MIN_MARADEK:g} mm anyag marad (átfúrás veszélye)"})
        holes.append(rec)
        byid[h["id"]] = rec

    hardware, kotesek = [], []
    # 1. csappárok: azonos kezdőpont, ellentétes irány
    grp = defaultdict(list)
    for r in holes:
        if r["funkcio"] in ("TIPLI_EL", "TIPLI_LAP"):
            grp[tuple(np.round(r["start"], 2))].append(r)
    pairs = Counter()
    for key, rs in grp.items():
        el = [r for r in rs if r["funkcio"] == "TIPLI_EL"]
        lap = [r for r in rs if r["funkcio"] == "TIPLI_LAP"]
        if len(el) == 1 and len(lap) == 1 and np.allclose(np.array(el[0]["irany"]), -np.array(lap[0]["irany"])):
            a, b = el[0], lap[0]
            n = pairs[(a["alkatresz"], b["alkatresz"])]
            pairs[(a["alkatresz"], b["alkatresz"])] += 1
            tag = f"{a['alkatresz']}:CSAP:{b['alkatresz']}:{n}"
            a["kapcsolat"] = b["kapcsolat"] = tag
            hardware.append({"tipus": "TIPLI_D8x30", "cikkszam": "Ø8×30 bükk csap, ragasztott (R12/R14: 22 mm él + 12 mm lap furat)",
                             "pozicio": b["start"], "irany": b["irany"], "kapcsolat": tag, "db": 1,
                             "geometria": {"d": 8, "hossz": 30, "el_melyseg": a["melyseg"], "lap_melyseg": b["melyseg"]}})
        else:
            for r in rs:
                problems.append({"sulyossag": "HIBA", "alkatresz": r["alkatresz"], "uzenet": f"{r['r16_id']}: csapfurat pár nélkül"})
    for (a, b), n in sorted(pairs.items()):
        kotesek.append({"A": a, "B": b, "tipus": "TIPLI", "db": n, "forras": "R16 holes.json CSAP/MEREVITO_CSAP"})

    # 2. pántok (R16 hinges.json) – kehely + 2 csavar az ajtón, 2 talpfurat a korpuszoldalon
    hb = [h for h in hwg if h["name"].startswith("Blum pánt")]
    for k, hg in enumerate(hinges):
        door, side = hg["front"], hg["side"]
        cup = next((r for r in holes if r["alkatresz"] == door and r["funkcio"] == "PANTKEHELY"
                    and np.allclose(r["start"], to_s16(hg["xyz"]), atol=0.01)), None)
        if cup is None:
            problems.append({"sulyossag": "BLOKKOLO", "alkatresz": door, "uzenet": f"pánt {k}: kehelyfurat nincs a holes.json-ban"})
            continue
        tag = f"{door}:PANT:{k}"
        cup["kapcsolat"] = tag
        z = hg["xyz"][2]
        scr = [r for r in holes if r["alkatresz"] == door and r["funkcio"] == "PANT_CSAVAR" and abs(r["start"][2] - z) < 30]
        tal = [r for r in holes if r["alkatresz"] == side and r["funkcio"] == "PANTTALP" and abs(r["start"][2] - z) < 20]
        for r in scr + tal:
            r["kapcsolat"] = tag
        if len(scr) != 2 or len(tal) != 2:
            problems.append({"sulyossag": "HIBA", "alkatresz": door, "uzenet": f"pánt {k}: csavar {len(scr)}/2, talpfurat {len(tal)}/2"})
        # kehely – ajtóél távolság (B) ellenőrzés
        fr = FR[door]
        u = cup["helyi"][0]
        bdist = min(u, fr.L - u) - cup["d"] / 2
        if not (3 - 1e-6 <= bdist <= 6 + 1e-6):
            problems.append({"sulyossag": "HIBA", "alkatresz": door, "uzenet": f"pánt {k}: kehely-éltávolság B = {bdist:.1f} mm (Blum: 3–6 mm)"})
        env = next((h for h in hb if abs(h["box"][2] - (z - 25)) < 0.6 and abs(h["box"][0] - (7.0 if hg["hand"] == "L" else 678.0)) < 0.6), None)
        hardware.append({"tipus": "PANT_CLIPTOP_110", "cikkszam": f"Blum {hg['sku']} (CLIP top 110°, rugó nélküli – TIP-ON-hoz) + {hg['plate']} talplemez",
                         "pozicio": cup["start"], "irany": cup["irany"], "ajto": door, "korpusz": side, "kez": hg["hand"], "kapcsolat": tag,
                         "kehely_B_mm": round(bdist, 2), "db": 1,
                         "befoglalo_globalis": None if env is None else [env["box"][0], round(FAL_Y - (env["box"][1] + env["box"][4]), 3), *env["box"][2:3], *env["box"][3:]]})
    # 3. polctartók
    for i, sp in enumerate(pins):
        r = next((r for r in holes if r["alkatresz"] == sp["part"] and r["funkcio"] == "POLCTARTO"
                  and np.allclose(r["start"], to_s16(sp["xyz"]), atol=0.01)), None)
        if r is None:
            problems.append({"sulyossag": "HIBA", "alkatresz": sp["part"], "uzenet": f"polctartó {i}: furat nincs a holes.json-ban"})
            continue
        r["kapcsolat"] = sp["shelf"]
        hardware.append({"tipus": "POLCTARTO", "cikkszam": "Ø5 csapos, lapos felfekvésű polctartó (R16 – típus nyitott)",
                         "pozicio": r["start"], "irany": r["irany"], "kapcsolat": sp["shelf"], "db": 1})
    # 4. csavarkötések (new_connections)
    for a, b, txt in newc:
        tag = f"{a}+{b}"
        ra, rb = byid.get(a), byid.get(b)
        if not (ra and rb):
            problems.append({"sulyossag": "HIBA", "alkatresz": tag, "uzenet": "new_connections hivatkozott furata hiányzik"})
            continue
        ra["kapcsolat"] = rb["kapcsolat"] = tag
        m = re.match(r"(\d+(?:[.,]\d+)?)x(\d+)", txt.replace(" ", ""))
        hardware.append({"tipus": f"CSAVAR_{m.group(1)}x{m.group(2)}" if m else "CSAVAR", "cikkszam": f"{txt} (R16 new_connections)",
                         "pozicio": ra["start"], "irany": ra["irany"], "kapcsolat": tag, "db": 1})
        kotesek.append({"A": ra["alkatresz"], "B": rb["alkatresz"], "tipus": "CSAVAR", "db": 1, "ok": txt})
    # 5. megvásárolt szerelvények befoglalói (hardware_geometry, a pánt-befoglalók a pántnál)
    for h in hwg:
        if h["name"].startswith("Blum pánt"):
            continue
        b = h["box"]
        hardware.append({"tipus": ascii_name(str(h.get("sku") or h["name"]))[:40], "cikkszam": f"{h.get('sku')} – {h['name']}",
                         "pozicio": [b[0], round(FAL_Y - (b[1] + b[4]), 3), b[2]], "irany": None, "kapcsolat": h["id"], "db": 1,
                         "befoglalo_globalis": [b[0], round(FAL_Y - (b[1] + b[4]), 3), b[2], b[3], b[4], b[5]],
                         "kategoria": "BEFOGLALO (R16 hardware_geometry – nem gyári 3D geometria)", "statusz": h.get("status")})
    # 6. nyitott gyári műveletek (nem találunk ki koordinátát)
    for p in pend:
        problems.append({"sulyossag": "FIGYELMEZTETES", "alkatresz": p["drawer"],
                         "uzenet": "NYITOTT gyári sablonművelet (nincs koordináta, nem kerül MPR-be): " + "; ".join(p["operations"])})
    out = {"modell_revizio": doc["modell_revizio"], "datum": date.today().isoformat(), "generator": "r16_vasalat.py",
           "parameterek": {"forras": "forras_R16 (R16 holes/hinges/shelf_pins/new_connections/hardware_geometry)", "fal_y_r16": FAL_Y,
                           "min_maradek": MIN_MARADEK},
           "pantoldal_javaslat": {h["front"]: {"oldal": "-X" if h["hand"] == "L" else "+X", "korpusz": h["side"],
                                               "db": sum(1 for x in hinges if x["front"] == h["front"])} for h in hinges},
           "furatok": holes, "vasalat": hardware, "kotesek": kotesek, "problemak": problems,
           "statusz": "TERVI – R16 tervezői furatkép; MOVENTO/TIP-ON gyári sablonfuratok nyitottak; woodWOP/gépi próba nincs"}
    (HERE / "vasalat_terv.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    fc = Counter(h["funkcio"] for h in holes)
    vc = Counter(w["tipus"] for w in hardware)
    pc = Counter(p["sulyossag"] for p in problems)
    L = [f"# R16J F2b – vasalat- és furatterv ({doc['modell_revizio']})", "",
         f"Generálva: {date.today().isoformat()} · `r16_vasalat.py` · forrás: R16 saját furatadatai (nem kitalált) · státusz: TERVI", "",
         f"Furat: {len(holes)} · átmenő: {sum(h['atmeno'] for h in holes)} · vasalat-tétel: {len(hardware)} · problémák: {dict(pc)}", "",
         "| Furat-funkció | db |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(fc.items())] + [
         "", "| Vasalat-típus | db |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sorted(vc.items())] + [
         "", "## Problémák", "", "| Súlyosság | Alkatrész | Megállapítás |", "|---|---|---|"]
    order = {"BLOKKOLO": 0, "HIBA": 1, "FIGYELMEZTETES": 2}
    for p in sorted(problems, key=lambda p: (order.get(p["sulyossag"], 9), p["alkatresz"])):
        L.append(f"| {p['sulyossag']} | {p['alkatresz']} | {p['uzenet']} |")
    L += ["", "## Kötések", "", "| A | B | típus | db |", "|---|---|---|---|"]
    L += [f"| {k['A']} | {k['B']} | {k['tipus']} | {k['db']} |" for k in kotesek]
    (HERE / "vasalat_jelentes.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print("furat:", len(holes), dict(fc), "| vasalat:", len(hardware), "| problémák:", dict(pc))


if __name__ == "__main__":
    main()
