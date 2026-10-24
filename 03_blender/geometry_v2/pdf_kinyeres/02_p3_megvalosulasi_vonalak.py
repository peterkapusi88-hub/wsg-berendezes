import pymupdf, json, collections, numpy as np
d=pymupdf.open('/mnt/user-data/attachments/9b8b9da8-4b7d-59ea-8424-77210777ae42/ab86005a-WGR1_meretezett_alaprajzok.pdf')
pg=d[2]; M=72/25.4*1000/125
R=pymupdf.Rect(30,60,500,580)
segs=[];styles=collections.Counter()
for dr in pg.get_drawings():
    if not dr['rect'].intersects(R): continue
    if dr['type'] not in ('s','fs'): continue
    w=round(dr.get('width') or 0,2); col=dr.get('color')
    styles[(w,col)]+=1
    for it in dr['items']:
        if it[0]=='l': segs.append((it[1].x,it[1].y,it[2].x,it[2].y,w,col))
        elif it[0]=='re':
            r=it[1];c=[(r.x0,r.y0),(r.x1,r.y0),(r.x1,r.y1),(r.x0,r.y1)]
            for i in range(4): segs.append((*c[i],*c[(i+1)%4],w,col))
print(styles.most_common(12))
json.dump(segs,open('p3_segs_pt.json','w'))
# texts in region
for w in pg.get_text('words'):
    if R.contains(pymupdf.Rect(w[:4])): pass
