#!/usr/bin/env python3
"""R16J – független önellenőrzés (nem a generátorok kódjával): forrás-hash, méretek, befoglaló-egyezés, furatok a darabon belül.
Futtatás: python3 ellenorzes.py  → 0 = minden rendben."""
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

H = Path(__file__).resolve().parent
F1, F2B = H / "10_F1_adatmodell", H / "30_F2b_vasalat"
j = lambda p: json.loads(p.read_text(encoding="utf-8"))
ok = True


def check(cond, msg):
    global ok
    print(("OK   " if cond else "HIBA ") + msg)
    ok &= bool(cond)


src = F1 / "forras_R16" / "parts.json"
audit = j(F1 / "forras_R16" / "audit_eredmeny_CLAUDE_ATADAS.json")
check(hashlib.sha256(src.read_bytes()).hexdigest() == audit["source_parts_sha256"], "forras_R16/parts.json SHA-256 = ChatGPT-audit forrás-hash")
r16 = {p["id"]: p for p in j(src)}
rj = {p["id"]: p for p in j(F1 / "forras_R16J" / "parts.json")}
doc = j(F1 / "parts_v1.json")
A = doc["alkatreszek"]
check(len(A) == len(r16) == len(rj) == 106, f"alkatrészszám 106 = R16 = R16J = parts_v1 ({len(A)})")
check(all(min(a["meret"]["kesz"].values()) > 0 for a in A), "minden kész méret > 0")
check(all(min(v for v in a["meret"]["nyers"].values() if v is not None) > 0 for a in A if any(a["meret"]["nyers"].values())), "minden megadott nyers méret > 0")
bad = []
for a in A:
    p = r16[a["id"]]
    x, y, z, dx, dy, dz = p["assembly_box_mm"]
    exp = [x, 418 - (y + dy), z, dx, dy, dz]
    if not np.allclose(a["befoglalo_globalis"], exp) or not np.allclose(rj[a["id"]]["box"], exp):
        bad.append(a["id"])
    if sorted([a["meret"]["kesz"][k] for k in "LWT"]) != sorted(p["assembly_box_mm"][3:]):
        bad.append(a["id"] + "(LWT)")
check(not bad, f"parts_v1 befoglaló = forras_R16J box = R16 assembly_box (Y_S16 = 418 − Y_R16), L/W/T = befoglaló élei {bad[:5]}")
fixed = [a["id"] for a in A if sorted(r16[a["id"]][k] for k in ("x", "y", "t")) != sorted(a["meret"]["kesz"].values())]
want = sorted(m["id"] for m in audit["parts_dimension_mismatches"])
check(sorted(fixed) == want, f"javított listaméretek = a ChatGPT-audit 12 eltérése ({len(fixed)} db)")
v = j(F2B / "vasalat_terv.json")
check(len(v["furatok"]) == 956, f"furatszám 956 = R16 holes.json ({len(v['furatok'])})")
R = {a["id"]: a for a in A}
out = []
for h in v["furatok"]:
    a = R[h["alkatresz"]]
    k = a["meret"]["kesz"]
    u, vv, n = h["helyi"]
    if not (-0.05 <= u <= k["L"] + 0.05 and -0.05 <= vv <= k["W"] + 0.05 and -0.05 <= n <= k["T"] + 0.05):
        out.append(h["r16_id"])
    # tengely-végpont a darab befoglalóján belül (átmenőnél a túlsó felületen)
    lo = np.array(a["befoglalo_globalis"][:3]); hi = lo + np.array(a["befoglalo_globalis"][3:])
    e = np.array(h["start"]) + np.array(h["irany"]) * min(h["melyseg"], 1e9)
    mid = np.array(h["start"]) + np.array(h["irany"]) * 0.5
    if not (np.all(mid >= lo - 0.05) and np.all(mid <= hi + 0.05)):
        out.append(h["r16_id"] + "(irány)")
    if not h["atmeno"] and not (np.all(e >= lo - 0.05) and np.all(e <= hi + 0.05)):
        out.append(h["r16_id"] + "(vég)")
check(not out, f"minden furat helyi koordinátája a darabon belül, iránya az anyagba mutat {out[:5]}")
blind_thru = [h["r16_id"] for h in v["furatok"] if not h["atmeno"] and h["melyseg"] >= R[h["alkatresz"]]["meret"]["kesz"]["T"] and h["cel"] == "lap"]
check(not blind_thru, "vak lapfurat mélysége < lapvastagság")
qa = j(F1 / "qa_report.json")
check(qa["osszesites"].get("BLOKKOLO", 0) == 0, f"F1 QA: 0 BLOKKOLÓ ({qa['osszesites']})")
check(not [p for p in v["problemak"] if p["sulyossag"] in ("BLOKKOLO", "HIBA")], "F2b: 0 BLOKKOLÓ / HIBA")
sys.exit(0 if ok else 1)
