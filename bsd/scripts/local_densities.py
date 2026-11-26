"""Densités locales de types de réduction pour les modèles E_{A,B} : y^2 = x^3 + A x + B, (A,B) dans Z_l^2,
normalisées comme chez BSZ (§3.1) : mu_l(P) = mesure{(A,B) minimaux : P} / (1 - l^-10), où « minimal »
signifie : l^4 | A  =>  l^6 ne divise pas B.

Méthode exacte avec borne d'erreur : on parcourt toutes les cellules (A,B) mod l^k. Une cellule est
« déterminée » si le type (exposant du conducteur f, et a_l mod l si f = 0) est le même pour le
représentant et pour R relevés aléatoires mod l^(k+6). La masse des cellules non déterminées borne
l'erreur. Usage : python3 local_densities.py l k [R]"""
import sys, json, random
from cypari import pari

pari.allocatemem(2 * 10**9)
l, k = int(sys.argv[1]), int(sys.argv[2])
R = int(sys.argv[3]) if len(sys.argv) > 3 else 3
pari('localtype(a,b,l) = my(E = ellinit([a,b]), r, f); if (E == [], return([-1, -1])); '
     'r = elllocalred(E, l); f = r[1]; if (f > 0, return([f, -1])); '
     '[0, ellap(ellminimalmodel(E), l) % l]')
lt = pari('localtype')
rng = random.Random(1)
M, Mk = l ** (k + 6), l ** k
counts = {}
undet = 0
nonmin = 0
for a in range(Mk):
    for b in range(Mk):
        # cellule non minimale : l^4 | A et l^6 | B (déterminée dès que k >= 6)
        if a % l**4 == 0 and b % l**min(6, k) == 0 and k >= 6:
            nonmin += 1
            continue
        t0 = tuple(int(x) for x in lt(a, b, l))
        ok = t0[0] >= 0
        for _ in range(R):
            if not ok:
                break
            a2 = a + Mk * rng.randrange(M // Mk); b2 = b + Mk * rng.randrange(M // Mk)
            if tuple(int(x) for x in lt(a2, b2, l)) != t0:
                ok = False
        if ok:
            counts[t0] = counts.get(t0, 0) + 1
        else:
            undet += 1
tot = Mk * Mk
norm = 1 - l ** -10.0
res = {str(t): c / tot / norm for t, c in sorted(counts.items())}
semistable = sum(c for t, c in counts.items() if t[0] <= 1) / tot / norm
good = sum(c for t, c in counts.items() if t[0] == 0) / tot / norm
ordinary = sum(c for t, c in counts.items() if t[0] == 0 and t[1] != 0) / tot / norm
out = dict(l=l, k=k, R=R, types=res, semistable=semistable, good=good, good_ordinary=ordinary,
           undetermined_mass=undet / tot / norm, nonminimal_mass=nonmin / tot)
print(json.dumps(out, indent=1))
json.dump(out, open(sys.path[0] + f"/../results/local_density_l{l}_k{k}.json", "w"), indent=1)
