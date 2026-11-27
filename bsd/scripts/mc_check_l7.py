"""Vérification finale (piste 2) : densités des types de Kodaira en l = 7 et 13, Monte-Carlo sur (A, B) mod l^30
(hors l^4 | A et l^6 | B), comparées aux formules de bound_v5.py / bound_v6.py, divisées par n(l) = 1 - l^-10.
Usage : python3 mc_check_l7.py l n"""
import sys, random, math
from cypari import pari
l, n = int(sys.argv[1]), int(sys.argv[2]); rng = random.Random(23); M = l**30
q = float(l); nl = 1 - q**-10
th = {"II": (q-1)/q**3, "III": (q-1)/q**4, "IV": (q-1)/q**5, "I0*": (1-1/q)/q**5,
      "In*": sum((q-1)**2/q**(k+7) for k in range(1, 60)), "IV*": (q-1)/q**8, "III*": (q-1)/q**9, "II*": (q-1)/q**10,
      "In": sum((q-1)**2/q**(m+2) for m in range(1, 60)), "bonne": 1 - 1/q}
kod = {2: "II", 3: "III", 4: "IV", -1: "I0*", -4: "IV*", -3: "III*", -2: "II*", 1: "bonne"}
c = {}; done = 0
while done < n:
    a, b = rng.randrange(M), rng.randrange(M)
    if (a % l**4 == 0 and b % l**6 == 0) or 4 * a**3 + 27 * b**2 == 0: continue
    k = int(pari.elllocalred(pari.ellinit([a, b]), l)[1]); done += 1
    name = kod.get(k, "In" if k > 4 else "In*"); c[name] = c.get(name, 0) + 1
for name, t in th.items():
    p = c.get(name, 0) / n; se = math.sqrt(max(p * (1 - p), 1 / n) / n)
    print(f"l={l} {name:5s} MC = {p:.6f} ± {se:.6f}   formule = {t / nl:.6f}   écart = {(p - t / nl) / se:+.1f} σ")
