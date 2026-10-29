"""Run: python3 ellenoriz_meretek.py /path/to/R16_feluletek_fiokok/data/parts.json
Checks nominal local blank dimensions against assembly bounds; no CAD/CNC release.
"""
import json, sys
from pathlib import Path
p = Path(sys.argv[1])
parts = json.loads(p.read_text())
issues = []
for part in parts:
    dims = part['assembly_box_mm'][3:]
    expected = [sum(abs(a)*b for a,b in zip(part['frame'][axis], dims))
                for axis in ['U','V','outward_A']]
    listed = [part[k] for k in ['x','y','t']]
    if min(listed) <= 0 or any(abs(a-b)>0.001 for a,b in zip(expected, listed)):
        issues.append(dict(id=part['id'], listed_mm=listed, expected_mm=expected))
print(json.dumps(dict(scope='LOCAL_DIMENSIONS_ONLY_NOT_MANUFACTURING_RELEASE',
                      count=len(parts), issues=issues), ensure_ascii=False, indent=2))
sys.exit(1 if issues else 0)
