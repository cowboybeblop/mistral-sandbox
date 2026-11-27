"""Piste 1 : Monte-Carlo par ligne des tables de BS (arXiv 1312.7859, table 3) : distribution de (Delta' mod 4, d_2)
par classe (v(A), v(B), v(Delta)), à comparer aux lignes imprimées. Usage : python3 bs_rows2.py"""
import random
from cypari import pari
rng=random.Random(3); N=2**30
def v(x): return 99 if x==0 else int(pari.valuation(x,2))
rows={}; n=100000
for _ in range(n):
    a=rng.randrange(N); b=rng.randrange(N)
    if a%2**4==0 and b%2**6==0: continue
    D=-4*a**3-27*b**2; vD=v(D); u=(D>>vD)%4
    d=int(pari.ellrootno(pari.ellinit([a,b]),2)*pari.ellrootno(pari.ellinit([a,-b]),2))
    va,vb=min(v(a),6),min(v(b),6)
    key=(va,vb, vD if (va,vb) in ((0,1),(2,4)) else None)
    rows.setdefault(key,{}); rows[key][(u,d)]=rows[key].get((u,d),0)+1
for key in sorted(rows, key=str):
    s=sum(rows[key].values())
    if s>100: print(key, round(s/n,5), {kk:round(c/s,3) for kk,c in sorted(rows[key].items())})
