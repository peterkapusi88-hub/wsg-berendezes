#!/usr/bin/env python3
"""Manifest-frissítő (B versenyző): a 20_PROMPTOK mappában meglévő promptfájlokat COMPLETE-re állítja,
karakterszámot számol (a BEGIN/END jelölők közötti szöveg), ellenőrzi a jelölőket és a tiltott helykitöltőket.
Használat: python3 manifest_update.py <CPx>"""
import csv, re, sys, pathlib
cp = sys.argv[1] if len(sys.argv) > 1 else "CP?"
base = pathlib.Path(__file__).parent
man = base / "01_MANIFEST_66.csv"
rows = list(csv.DictReader(open(man, encoding="utf-8"), delimiter=";"))
bad = []
for r in rows:
    if r["statusz"] == "KOZOS":
        continue
    f = base.parent.parent / r["fajl"]
    if not f.exists():
        continue
    t = f.read_text(encoding="utf-8")
    kid = r["kep_id"]
    m = re.search(rf"=== BEGIN PROMPT {re.escape(kid)} ===\n(.*?)\n=== END PROMPT {re.escape(kid)} ===", t, re.S)
    if not m:
        bad.append((kid, "BEGIN/END jelölő hiányzik vagy nem egyezik")); continue
    body = m.group(1)
    for ph in ["same as above", "see previous", "TBD", "lásd az előző", "…\n"]:
        if ph.lower() in body.lower():
            bad.append((kid, f"helykitöltő: {ph!r}"))
    r["karakterszam"] = str(len(body))
    if r["statusz"] != "COMPLETE":
        r["statusz"] = "COMPLETE"; r["checkpoint"] = cp
    r["validalas"] = "NEEDS_CLAUDE_VALIDATION"
with open(man, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter=";")
    w.writeheader(); w.writerows(rows)
done = sum(1 for r in rows if r["statusz"] == "COMPLETE")
print(f"COMPLETE: {done}/60 saját; KOZOS: {sum(1 for r in rows if r['statusz']=='KOZOS')}/6")
for b in bad: print("HIBA:", *b)
sys.exit(1 if bad else 0)
