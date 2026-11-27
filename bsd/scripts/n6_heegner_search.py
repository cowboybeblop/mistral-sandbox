"""Piste 8 (N6) : test numérique. Pour des courbes E de notre famille (5 | A, 5 ne divise pas B : supersingulière en 5),
de signe -1, on cherche des corps de Heegner K = Q(sqrt(-l)), l premier = 3 mod 4, tels que
  (Heeg) tout premier de 5N est décomposé dans K ;
  (adm)  l est « propre » : l != ±1 mod 5 et a_l(E) != ±(l+1) mod 5 (Lemme types23 étendu, piste 2) ;
  L(E^K, 1) != 0, i.e. L(1, E ⊗ chi_{-l}) != 0 (BSTW Th. 12.3 / BFH).
Constat : avec D = -l premier, (Heeg) en 5 impose (-l/5) = 1, i.e. l = ±1 mod 5, incompatible avec (adm).
On cherche donc aussi D = -l1*l2 (l1 l2 = 3 mod 4, l1 < l2), les deux premiers propres.
On compte, parmi les D testés, ceux qui vérifient tout. Ce n'est qu'une indication (pas une preuve).
Usage : python3 n6_heegner_search.py [lmax] [Dmax]"""
import sys
from cypari import pari
pari.allocatemem(2 * 10**9); pari.set_real_precision(19)
LMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 400
DMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 3000
curves = []
for A in range(-40, 41, 5):
    for B in range(1, 30):
        if B % 5 == 0 or 4 * A**3 + 27 * B**2 == 0: continue
        E = pari.ellinit([A, B]); N = int(pari.ellglobalred(E)[0])
        if int(pari.ellrootno(E)) == -1 and N < 3000: curves.append((N, A, B))
curves = sorted(set(curves))[:6]
for N, A, B in curves:
    E = pari.ellinit([A, B]); bad = [int(p) for p in pari.factor(5 * N)[0]]
    heeg = adm = good = 0; ex = []
    for l in pari.primes(LMAX):
        l = int(l)
        if l % 4 != 3 or l in bad: continue
        if any(int(pari.kronecker(-l, q)) != 1 for q in bad): continue
        heeg += 1
        al = int(pari.ellap(E, l))
        if l % 5 in (1, 4) or (al - l - 1) % 5 == 0 or (al + l + 1) % 5 == 0: continue
        adm += 1
        Et = pari.ellinit(pari.elltwist(E, -l))
        if abs(float(pari.lfun(Et, 1))) > 1e-8: good += 1; ex.append(l)
    print(f"E=[{A},{B}] N={N} : l <= {LMAX} avec (Heeg) {heeg}, + propres {adm}, + L(E^K,1) != 0 : {good}  ex. {ex[:5]}")
    # D = -l1 l2
    def okprime(l):
        al = int(pari.ellap(E, l))
        return l not in bad and l % 5 not in (1, 4) and (al - l - 1) % 5 and (al + l + 1) % 5
    P = [int(l) for l in pari.primes(DMAX // 3) if int(l) > 2 and okprime(int(l))]
    heeg = good = 0; ex = []
    for i, l1 in enumerate(P):
        for l2 in P[i+1:]:
            D = -l1 * l2
            if -D > DMAX: break
            if D % 4 != 1: continue
            if any(int(pari.kronecker(D, q)) != 1 for q in bad): continue
            heeg += 1
            Et = pari.ellinit(pari.elltwist(E, D))
            if abs(float(pari.lfun(Et, 1))) > 1e-8: good += 1; ex.append(D)
    print(f"      D = -l1 l2, |D| <= {DMAX}, l1, l2 propres : (Heeg) {heeg}, + L(E^K,1) != 0 : {good}  ex. {ex[:6]}")
