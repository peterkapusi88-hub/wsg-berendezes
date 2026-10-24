import json, numpy as np, collections
M3=72/25.4*1000/125
P3=json.load(open('p3_segs_pt.json')); P18=json.load(open('pdf_segs_blendercoords.json'))
def vh(segs):
    V=[];H=[]
    for x1,y1,x2,y2 in segs:
        L=abs(x1-x2)+abs(y1-y2)
        if L<1.0: continue
        if abs(x1-x2)<0.01: V.append((x1,min(y1,y2),max(y1,y2)))
        elif abs(y1-y2)<0.01: H.append((y1,min(x1,x2),max(x1,x2)))
    return V,H
s3=[(x1/M3,-y1/M3,x2/M3,-y2/M3) for x1,y1,x2,y2,w,c in P3 if c==[0.0,0.0,0.0] or c==(0.0,0.0,0.0)]
s18=[(a[0],a[1],b[0],b[1]) for a,b,w in P18 if w==0.71]
V3,H3=vh(s3);V18,H18=vh(s18)
def best(A,B):
    c=collections.Counter()
    for a in A:
        for b in B: c[round(b[0]-a[0],2)]+= min(a[2]-a[1],b[2]-b[1])
    return c.most_common(5)
print('dx',best(V3,V18)); print('dy',best(H3,H18))
def score(A,B,d,tol=0.03):
    s=0
    for a in A:
        for b in B:
            if abs(b[0]-a[0]-d)<=tol: s+=max(0,min(a[2],b[2]-0)-max(a[1],b[1]))*0+min(a[2]-a[1],b[2]-b[1])
    return s
import itertools
# restrict to A-902 region of p3 roughly
V3r=[v for v in V3 if 2<v[0]<22 and -26<v[1]<-3]; H3r=[h for h in H3 if -26<h[0]<-3 and 1<h[1]<22]
bx=max(((score(V3r,V18,d/100),d/100) for d in range(-500,-300)),key=lambda t:t[0])
by=max(((score(H3r,H18,d/100),d/100) for d in range(2300,2550)),key=lambda t:t[0])
print(bx,by)
json.dump({'dx':bx[1],'dy':by[1],'M3':M3},open('p3_align.json','w'))
