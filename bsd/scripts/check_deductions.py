"""B2 : contrôles des déductions 3 et 4 de lit/amelioration_BSZ.md.
(3) E(Q_5)[5] = 0 pour E multiplicative en 5 : non déployée (tout k) et déployée avec 5 ne divisant pas k.
    Test : racines 5-adiques du polynôme de 5-division, puis y^2 = f(x) carré dans Q_5.
(4) densité en l de « multiplicative non déployée avec ord_l Delta = 1 », comparée à (l-1)^2/(2 l^3)."""
import random, json
from cypari import pari
pari.allocatemem(2 * 10**9)
pari('has5tors(a,b) = my(E = ellinit([a,b]), f = elldivpol(E,5), R = polrootspadic(f, 5, 40), c = 0); '
     'for (i = 1, #R, my(x0 = R[i], y2 = x0^3 + a*x0 + b); if (y2 != 0 && issquare(y2), c++)); c')
has = pari('has5tors')
rng = random.Random(7)
stats = {}
tries = 0
while sum(v[0] for v in stats.values()) < 600 and tries < 10**6:
    tries += 1
    a = rng.randrange(-10**6, 10**6); b = rng.randrange(-10**6, 10**6)
    if a % 5 == 0: continue
    D = -16 * (4 * a**3 + 27 * b**2)
    if D == 0 or D % 5: continue
    E = pari.ellinit([a, b]); k = int(pari.valuation(D, 5)); ap = int(pari.ellap(E, 5))
    typ = ("déployée" if ap == 1 else "non déployée") + (", 5|k" if k % 5 == 0 else ", 5∤k")
    c = int(has(a, b)) > 0
    s = stats.setdefault(typ, [0, 0]); s[0] += 1; s[1] += c
print("(3) courbes testées par type : [nombre, avec E(Q_5)[5] != 0]")
for t, v in sorted(stats.items()): print("   ", t, v)
# cas rares 5 | k : on en fabrique, A = 3 mod 5 et B choisi pour forcer v_5(Delta) = 5
print("(4) densité de « non déployée, ord_l Delta = 1 » :")
res4 = {}
for l in (7, 11, 13, 17, 19, 23, 29):
    cnt = 0
    for a in range(l * l):
        for b in range(l * l):
            D = -16 * (4 * a**3 + 27 * b**2)
            if a % l == 0 or D % l or (D // l) % l == 0: continue
            if int(pari.ellap(pari.ellinit([a, b]), l)) == -1: cnt += 1
    dens = cnt / l**4 / (1 - l ** -10.0)
    res4[l] = dens
    print(f"    l={l}: {dens:.6f}   (l-1)^2/(2 l^3) = {(l-1)**2/(2*l**3):.6f}   l * densité = {l*dens:.3f}")
json.dump(dict(deduction3=stats, deduction4=res4), open("results/check_deductions.json", "w"), indent=1, ensure_ascii=False)
