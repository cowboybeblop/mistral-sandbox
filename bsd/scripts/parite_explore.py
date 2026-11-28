"""Suite 2 (cadrage du problème de parité) : explorations numériques.
(a) Vérifie w_p(E) = -(-c6 / p) en réduction multiplicative, p >= 5 (déployée ssi -c6 est un carré mod p).
(b) Mesure la moyenne du signe r(E) et de mu(4A^3 + 27B^2) dans des boîtes de hauteur X croissantes
    (tirages uniformes), pour voir l'ordre de grandeur de la compensation attendue (conjecture : o(1)).
Usage : python3 parite_explore.py"""
import random, math
from cypari import pari
rng = random.Random(8)
# (a)
bad = tot = 0
while tot < 3000:
    A, B = rng.randint(-10**4, 10**4), rng.randint(-10**6, 10**6)
    D = -16 * (4 * A**3 + 27 * B**2)
    if D == 0: continue
    E = pari.ellinit([A, B])
    for p in list(pari.factor(abs(D))[0])[:6]:
        p = int(p)
        if p < 5 or int(pari.elllocalred(E, p)[0]) != 1: continue
        c6 = int(E.c6()) if hasattr(E, 'c6') else int(pari('(e)->e.c6')(E))
        tot += 1; bad += int(pari.ellrootno(E, p)) != -int(pari.kronecker(-c6, p))
print(f"(a) w_p = -(-c6/p) en réduction multiplicative : {tot - bad}/{tot} cas conformes")
# (b)
for e in (4, 6, 8):
    Amax = 10**e; Bmax = int(math.sqrt(4 * Amax**3 / 27)); n = 40000; sr = sm = 0; k = 0
    while k < n:
        A, B = rng.randint(-Amax, Amax), rng.randint(-Bmax, Bmax)
        if max(4 * abs(A)**3, 27 * B * B) > 4 * Amax**3: continue
        D = 4 * A**3 + 27 * B * B
        if D == 0 or any(A % p**4 == 0 and B % p**6 == 0 for p in (2, 3, 5, 7)): continue
        k += 1; sr += int(pari.ellrootno(pari.ellinit([A, B]))); sm += int(pari.moebius(abs(D)))
    print(f"(b) |A| <= 1e{e} : moyenne de r(E) = {sr / n:+.4f} ± {1 / math.sqrt(n):.4f} ;"
          f" moyenne de mu(4A^3+27B^2) = {sm / n:+.4f} ± {1 / math.sqrt(n):.4f}")
