"""Piste 5 (p = 3) : répartition des types en 3 par Monte-Carlo (tirages (A, B) mod 3^30, hors 3^4 | A et 3^6 | B).
Classes : bonne ordinaire, bonne supersingulière avec a_3 = 0 (condition (1.7) de BSTW), avec a_3 = ±3,
multiplicative, additive. (Une version par cellules avec test sur 3 relèvements aléatoires ratait la classe
« bonne ordinaire », de mesure ~1e-4 concentrée dans v_3(A) = v_3(B) = 3 : d'où ce Monte-Carlo.)
Usage : python3 p3_montecarlo.py [n]"""
import sys, random, json
from cypari import pari
n = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
rng = random.Random(13); M = 3**30; c = {}
pari('t3(a,b) = my(E = ellinit([a,b]), f, ap); f = elllocalred(E, 3)[1]; if (f == 1, return(4)); if (f > 1, return(5)); '
     'ap = ellap(E, 3); if (ap % 3, 1, if (ap == 0, 2, 3))')
t3 = pari('t3'); names = {1: "bonne_ordinaire", 2: "bonne_ss_a3=0", 3: "bonne_ss_a3=±3", 4: "multiplicative", 5: "additive"}
done = 0
while done < n:
    a, b = rng.randrange(M), rng.randrange(M)
    if (a % 81 == 0 and b % 729 == 0) or 4 * a**3 + 27 * b**2 == 0: continue
    k = names[int(t3(a, b))]; c[k] = c.get(k, 0) + 1; done += 1
res = {k: v / n for k, v in sorted(c.items())}; res["n"] = n
print(json.dumps(res, indent=1)); json.dump(res, open(sys.path[0] + "/../results/p3_montecarlo.json", "w"), indent=1)
