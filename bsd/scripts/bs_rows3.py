"""Piste 1 : Monte-Carlo par ligne des tables de BS (arXiv 1312.7859, table 4) : distribution de (Delta' mod 4, d_3)
par classe (v(A), v(B), v(Delta)), à comparer aux lignes imprimées. Usage : python3 bs_rows3.py"""
import random
from cypari import pari
rng=random.Random(1); N=3**20
def v(x): return 99 if x==0 else int(pari.valuation(x,3))
rows={}
for _ in range(200000):
    a=rng.randrange(N); b=rng.randrange(N)
    if a%3**4==0 and b%3**6==0: continue
    D=-4*a**3-27*b**2; vD=v(D)
    d=int(pari.ellrootno(pari.ellinit([a,b]),3)*pari.ellrootno(pari.ellinit([a,-b]),3))
    va,vb=min(v(a),6),min(v(b),6)
    key=(va,vb, vD if (va,vb)==(1,0) else None)
    m=3**vD%4
    rows.setdefault(key,{}); rows[key][(m,d)]=rows[key].get((m,d),0)+1
tot={}
for key in sorted(rows, key=str):
    s=sum(rows[key].values())
    print(key, s/200000, {kk:round(c/s,3) for kk,c in sorted(rows[key].items())})
    for kk,c in rows[key].items(): tot[kk]=tot.get(kk,0)+c/200000
print(tot)
