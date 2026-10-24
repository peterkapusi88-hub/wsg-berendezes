# ajtó-nyitásívek: Bézier-ív -> középpont (zsanér), sugár, kezdő/vég pont
import pymupdf, sys, math, json
PDF='/mnt/user-data/uploads/Downloads/WGR1_meretezett_alaprajzok.pdf'
FL={'A811':dict(page=5,scale=50,X0=434.02,Y0=748.0,box=(-2.8,-0.9,9.0,12.3)),
    'A812':dict(page=12,scale=100,X0=539.36,Y0=600.95,box=(-2.8,-0.8,9.4,17.6))}
flat=sys.argv[1]; P=FL[flat]; d=pymupdf.open(PDF); pg=d[P['page']-1]
M=72/25.4*1000/P['scale']; X0,Y0=P['X0'],P['Y0']; bx=P['box']
tm=lambda p:((p.x-X0)/M,(Y0-p.y)/M)
def center(p0,p1,p2,p3):
    # normálisok metszéspontja p0-ban és p3-ban
    t0=(p1[0]-p0[0],p1[1]-p0[1]); t3=(p3[0]-p2[0],p3[1]-p2[1])
    n0=(-t0[1],t0[0]); n3=(-t3[1],t3[0])
    det=n0[0]*(-n3[1])-n0[1]*(-n3[0])
    if abs(det)<1e-12: return None
    dx,dy=p3[0]-p0[0],p3[1]-p0[1]
    s=(dx*(-n3[1])-dy*(-n3[0]))/det
    return (p0[0]+s*n0[0],p0[1]+s*n0[1])
arcs=[]
for D in pg.get_drawings():
    c=D.get('color'); w=round(D.get('width') or 0,2)
    if D['type']!='s' or c is None: continue
    c=tuple(round(v,3) for v in c)
    for it in D['items']:
        if it[0]!='c': continue
        p=[tm(q) for q in it[1:5]]
        if not all(bx[0]<=q[0]<=bx[2] and bx[1]<=q[1]<=bx[3] for q in p): continue
        C=center(*p)
        if not C: continue
        r0=math.dist(C,p[0]); r3=math.dist(C,p[3])
        if not(0.5<r0<1.3 and abs(r0-r3)<0.02): continue
        a0=math.degrees(math.atan2(p[0][1]-C[1],p[0][0]-C[0])); a3=math.degrees(math.atan2(p[3][1]-C[1],p[3][0]-C[0]))
        sw=(a3-a0+540)%360-180
        arcs.append(dict(c=[round(C[0],3),round(C[1],3)],r=round((r0+r3)/2,3),p0=[round(v,3) for v in p[0]],p3=[round(v,3) for v in p[3]],a0=round(a0),sw=round(sw),col=c,w=w))
# összevonás: egy ív több Bézier-darabból állhat (azonos középpont, sugár)
arcs.sort(key=lambda a:(a['c'][0],a['c'][1]))
grp=[]
for a in arcs:
    for g in grp:
        if math.dist(g['c'],a['c'])<0.02 and abs(g['r']-a['r'])<0.02: g['parts'].append(a); break
    else: grp.append(dict(c=a['c'],r=a['r'],parts=[a],col=a['col'],w=a['w']))
for g in grp:
    pts=[q for a in g['parts'] for q in (a['p0'],a['p3'])]
    tot=sum(abs(a['sw']) for a in g['parts'])
    g['ossz_szog']=tot; g['pontok']=pts
    print(f"közép {g['c']} r {g['r']} szög {tot:4d}° részek {len(g['parts'])} szín {g['col']} {g['w']}  végpontok {[tuple(q) for q in pts]}")
json.dump(grp,open(f'{sys.argv[2]}/{flat}_ivek.json','w'))
