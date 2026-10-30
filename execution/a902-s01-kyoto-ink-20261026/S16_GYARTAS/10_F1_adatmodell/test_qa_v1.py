#!/usr/bin/env python3
"""Önteszt: a QA szándékosan elrontott adatokon BLOKKOL-e.

Futtatás:  python3 test_qa_v1.py      (kilépési kód 0 = minden teszt átment)
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import qa_parts_v1 as Q  # noqa: E402
from s16_geom import Solid, box_mesh, load_json  # noqa: E402

BASE = load_json(HERE / "parts_v1.json")
RULES = load_json(HERE / "gyartasi_szabalyok_v1.json")


def run_doc(doc):
    with tempfile.TemporaryDirectory() as td:
        p = Path(td) / "parts.json"
        p.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        out = str(Path(td) / "qa")
        rc = Q.main(["--parts", str(p), "--out", out])
        rep = json.loads(Path(out + ".json").read_text(encoding="utf-8"))
    return rc, rep


def codes(rep, sev=None):
    return {(t["kod"], t["alkatresz"]) for t in rep["tetelek"] if sev is None or t["sulyossag"] == sev}


def test_negativ_meret_blokkol():
    doc = copy.deepcopy(BASE)
    r = next(x for x in doc["alkatreszek"] if x["id"] == "D2-BOX-F")
    r["meret"]["kesz"]["L"] = -222          # az S01 101. oldali hibájának mintája
    r["meret"]["elzaras_elotti"]["L"] = -222
    rc, rep = run_doc(doc)
    assert rc == 2, "negatív méretnél a kilépési kód 2 kell legyen"
    assert ("Q01_NEM_POZITIV_MERET", "D2-BOX-F") in codes(rep, "BLOKKOLO")


def test_nulla_meret_blokkol():
    doc = copy.deepcopy(BASE)
    r = next(x for x in doc["alkatreszek"] if x["id"] == "T-L-S1")
    r["meret"]["kesz"]["W"] = 0
    rc, rep = run_doc(doc)
    assert rc == 2 and ("Q01_NEM_POZITIV_MERET", "T-L-S1") in codes(rep, "BLOKKOLO")


def test_lista_modell_elteres_blokkol():
    doc = copy.deepcopy(BASE)
    r = next(x for x in doc["alkatreszek"] if x["id"] == "D3-FRONT")
    r["meret"]["kesz"]["L"] = 425            # lista ≠ befoglaló (422)
    rc, rep = run_doc(doc)
    assert rc == 2 and ("Q04_LISTA_BEFOGLALO_ELTERES", "D3-FRONT") in codes(rep, "BLOKKOLO")


def test_duplikalt_id_blokkol():
    doc = copy.deepcopy(BASE)
    doc["alkatreszek"][5]["cimke_id"] = doc["alkatreszek"][4]["cimke_id"]
    rc, rep = run_doc(doc)
    assert rc == 2 and any(k == "Q08_DUPLIKALT_CIMKE_ID" for k, _ in codes(rep, "BLOKKOLO"))


def test_utkozes_felismerese():
    a = Solid.from_mesh("A", box_mesh([0, 0, 0, 100, 18, 100]), "teszt")
    b = Solid.from_mesh("B", box_mesh([95, 0, 0, 100, 18, 100]), "teszt")   # 5×18×100 = 9000 mm³ átfedés
    c = Solid.from_mesh("C", box_mesh([200, 0, 0, 100, 18, 100]), "teszt")  # érintés nélkül
    qa = Q.QA()
    Q.q_utkozes(BASE, {"A": a, "B": b, "C": c}, RULES, qa)
    hits = [i for i in qa.items if i["kod"] == "Q11_UTKOZES"]
    assert len(hits) == 1 and hits[0]["alkatresz"] == "A × B", hits
    assert "9000.0" in hits[0]["uzenet"], hits[0]["uzenet"]


def test_erintkezes_nem_utkozes():
    a = Solid.from_mesh("A", box_mesh([0, 0, 0, 100, 18, 100]), "teszt")
    b = Solid.from_mesh("B", box_mesh([100, 0, 0, 100, 18, 100]), "teszt")  # lapjával érintkezik
    qa = Q.QA()
    Q.q_utkozes(BASE, {"A": a, "B": b}, RULES, qa)
    assert not qa.items


def test_alap_adatmodell_nem_tartalmaz_negativ_meretet():
    rc, rep = run_doc(copy.deepcopy(BASE))
    assert not any(k.startswith("Q01") for k, _ in codes(rep, "BLOKKOLO"))
    assert not any(k == "Q11_UTKOZES" for k, _ in codes(rep))


if __name__ == "__main__":
    fails = 0
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print(f"OK    {name}")
            except AssertionError as e:
                fails += 1
                print(f"HIBA  {name}: {e}")
    print("ÖSSZES TESZT ÁTMENT" if not fails else f"{fails} teszt elbukott")
    sys.exit(1 if fails else 0)
