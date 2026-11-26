"""Recherche de tordues quadratiques E_D de rang analytique >= 2 d'une courbe E de petit conducteur.
Filtre exact : signe de E_D = +1 et L(E_D,1) = 0, ce dernier via la somme rationnelle
sum_{b mod |D|} chi_D(b) [b/|D|]^{sgn D} des symboles modulaires de E au niveau N.
Usage : python3 twist_scan.py AINV DMAX SORTIE.jsonl"""
import sys, json, time
from cypari import pari
pari.allocatemem(2 * 10**9)
arg = sys.argv[1]
E = pari.ellinit(pari(arg))  # a-invariants, ex. [0,-1,1,-10,-20] (pas de elldata ici)
N = int(pari.ellglobalred(E)[0])
Mp = pari.msfromell(E, 1); Mm = pari.msfromell(E, -1)
twsum = pari('(M,x,D)->my(m=abs(D)); sum(b=1,m-1, if(gcd(b,m)==1, kronecker(D,b)*mseval(M,x,[oo,b/m]),0))')
out = open(sys.argv[3], 'w'); t0 = time.time(); n = 0
for D in range(-int(sys.argv[2]), int(sys.argv[2]) + 1):
    if D in (0, 1) or not int(pari.isfundamental(D)) or pari.gcd(D, N) != 1:
        continue
    ED = pari('(E,D)->ellminimalmodel(ellinit(elltwist(E,D)))')(E, D)
    if int(pari.ellrootno(ED)) != 1:
        continue
    M, x = Mp if D > 0 else Mm
    s = twsum(M, x, D)
    if s == 0:
        n += 1
        out.write(json.dumps(dict(base=arg, N=N, D=D, N_D=int(pari.ellglobalred(ED)[0]),
                                  ainv=[int(a) for a in pari('e->[e.a1,e.a2,e.a3,e.a4,e.a6]')(ED)])) + "\n"); out.flush()
print(arg, 'candidats', n, '%.0fs' % (time.time() - t0))
