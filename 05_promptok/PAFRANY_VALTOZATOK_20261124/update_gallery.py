import json,pathlib,html,os
p=pathlib.Path(__file__).resolve().parent;m=json.loads((p/'MANIFEST.json').read_text());refs={r['id']:r for r in json.loads((p/'02_REFERENCE_INDEX.json').read_text())};styles=json.loads((p/'01_VARIANTS.json').read_text());root=p.parents[1]
h=['<!doctype html><html lang="hu"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Páfrány – 811 / 812 / 902</title><style>body{margin:0;background:#eeeae4;color:#272723;font:16px system-ui}header,main{max-width:1500px;margin:auto;padding:24px}h1{font-size:32px}nav{display:flex;gap:15px;flex-wrap:wrap}a{color:#685239}section{margin:40px 0}.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px}article{background:white;padding:14px;border-radius:12px}img{width:100%;height:auto}small{color:#6b6258}.refs{display:flex;gap:12px;overflow:auto}.refs a{min-width:150px;width:220px}.refs img{height:130px;object-fit:cover}.pending{padding:35px;background:#e6e1d9}.id{overflow-wrap:anywhere}details{margin:10px 0}@media(max-width:650px){.grid{grid-template-columns:1fr}header,main{padding:14px}h1{font-size:25px}}</style><header><h1>Páfrány · négy teljes változat</h1><p>811 · 812 · 902 — minden korábbi helyiségnézet. Elkészült: '+str(m['completed_images'])+' / '+str(m['expected_images'])+'</p><p>Az eredeti referenciákból átvett anyag- és formavilág, a lakások megtartott elrendezésével. Koncepcióképek; műszaki és beszerzési ellenőrzés szükséges.</p><nav>']
for apt in ['A902','A812','A811']:h.append(f'<a href="#{apt}">{apt}</a>')
h.append('<a href="../../02_referenciak/BUKOSDI_PAFRANY_20261124/00_KEPES_ATTEKINTO.html">25 eredeti mintakép</a></nav></header><main>')
for apt in ['A902','A812','A811']:
 h.append(f'<h2 id="{apt}">{apt}</h2>')
 for s in styles:
  h.append(f'<section><h3>{s["id"]} · {html.escape(s["name"])}</h3><p>Nappali: {", ".join(s["living"])} · Háló: {", ".join(s["bed"])}. A helyiségek párosítása az új változat tervezési döntése.</p><div class="refs">')
  for rid in dict.fromkeys(s['living']+s['bed']+s['kitchen']+s['entry']+s['bath']):
   r=refs[rid];url='../../02_referenciak/BUKOSDI_PAFRANY_20261124/'+r['file'];h.append(f'<a href="{url}"><img loading="lazy" src="{url}" alt="{rid}">{rid}</a>')
  h.append('</div><div class="grid">')
  for j in m['jobs']:
   if j['apartment']!=apt or j['variant']!=s['id']:continue
   h.append(f'<article id="{j["id"]}"><h4>{html.escape(j["camera"])}</h4>')
   if (p/j['output']).exists():h.append(f'<a href="{j["output"]}"><img loading="lazy" src="{j["output"]}" alt="{j["id"]}"></a>')
   else:h.append('<div class="pending">Előkészítve · kép még nincs</div>')
   h.append(f'<small class="id">{j["id"]}</small><details><summary>Mintaképek és teljes angol prompt</summary><p>Referenciák: {", ".join(j["reference_ids"])}</p><a href="{j["prompt"]}">Teljes prompt</a></details></article>')
  h.append('</div></section>')
h.append('</main></html>');(p/'00_KEPES_ATTEKINTO.html').write_text(''.join(h))
