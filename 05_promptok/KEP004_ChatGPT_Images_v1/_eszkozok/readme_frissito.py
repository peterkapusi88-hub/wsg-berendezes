# A 05_promptok/KEP004_ChatGPT_Images_v1/README.md dinamikus részeinek újragenerálása a nyilvántartásból (Claude, 2026-10-24).
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import forrasok as F, epito as E
RD = E.REPO_P + 'README.md'
s = open(RD, encoding='utf-8').read()
ny = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/csomag_nyilvantartas.json', encoding='utf-8'))
ell = json.load(open(os.path.dirname(os.path.abspath(__file__)) + '/ellenorzes_promptok_v1.json', encoding='utf-8'))
assert not ell['hibak'], ell['hibak']
ido = sys.argv[1]
# 1) hash-tábla
t = ['| # | Kép-ID | Lépés | Karakter | Csatolmány | Kave kézi | prompt sha256 |', '|---|---|---|---|---|---|---|']
for x in ny:
    kh = sum(1 for b in x['bemenetek'] if b['sha256'] is None)
    t.append(f"| {x['nr']:02d} | `{x['id']}` | {x['lepes']} | {x['prompt_karakter']} | {len(x['bemenetek'])} | {kh} | `{x['prompt_sha256'][:16]}…` |")
a = s.index('| # | Kép-ID | Lépés | Karakter'); b = s.index('\n\n## Csatolmányok képenként')
s = s[:a] + '\n'.join(t) + s[b:]
# 2) csatolmány-szakasz
c = ['## Csatolmányok képenként (sorrendben; repóútvonal vagy forrás)', '']
for x in ny:
    c.append(f"### {x['nr']:02d} · {x['id']} – {x['statusz']}")
    for i, bm in enumerate(x['bemenetek'], 1):
        c.append(f"{i}. `{bm['fajl']}` ← {bm['forras']} – {bm['szerep']}" + (f" (sha256 `{bm['sha256'][:12]}…`)" if bm['sha256'] else ''))
    c.append('')
a = s.index('## Csatolmányok képenként'); b = s.index('## Termékfotók forrása')
s = s[:a] + '\n'.join(c) + s[b:]
# 3) ellenőrzés időpontja + forrás-sha256 frissítés
s = re.sub(r'## Ellenőrzés \(2026-10-24 \d\d:\d\d, `ellenor.py`\)', f'## Ellenőrzés (2026-10-24 {ido}, `ellenor.py`)', s)
for p in (F.SABLON, F.ASTRA, F.CAM10, F.GARD, F.HUE, F.KONC):
    s = re.sub(r'(\| `' + re.escape(p) + r'` \| `)[0-9a-f]{64}(` \|)', lambda m: m.group(1) + F.fsha(p) + m.group(2), s)
open(RD, 'w', encoding='utf-8').write(s)
print('README frissítve', len(s))
