"""Suite de test_multiplicite_un.py : cas construits.
  E2 en 3 : E' = (27u, 54w) multiplicative en 3 avec 5 | v_3(Delta(E')) (seule forme réduite possible : le modèle
           court n'est jamais multiplicatif en 3 si 3 ne divise pas A), et E = sa tordue par ±3, réduite : (3u, ±2w) ;
  E3 en 7 (I0*, même situation locale que N6) : E = tordue par 7 de E' de bonne réduction en 7 avec
           a_7(E') = ±(7+1) mod 5 : (A, B) = (49a, 343b).
Même test : existe-t-il D < 0 (q0 inerte, autres premiers de N décomposés) avec v_5(L_alg(E) L_alg(E^D)) = 0 ?
Usage : python3 test_multiplicite_un_construit.py [ncourbes] [nD]"""
import sys, random
from fractions import Fraction
from cypari import pari
pari.allocatemem(4 * 10**8); pari.set_real_precision(30)
NC = int(sys.argv[1]) if len(sys.argv) > 1 else 4; ND = int(sys.argv[2]) if len(sys.argv) > 2 else 6
LALG = pari('(E) -> my(Em = ellinit(ellminimalmodel(E)), om = Em.omega[1] * if (Em.disc > 0, 2, 1)); bestappr(lfun(Em, 1) / om, 10^7)')
def v5(x):
    if x == 0: return None
    n, d, v = x.numerator, x.denominator, 0
    while n % 5 == 0: n //= 5; v += 1
    while d % 5 == 0: d //= 5; v -= 1
    return v
def test(A, B, label, out):
    E = pari.ellinit([A, B]); N = int(pari.ellglobalred(E)[0])
    if N > 60000 or int(pari.ellrootno(E)) != 1: return False
    fac = [int(p) for p in pari.factor(N)[0]]
    q0s = [q for q in fac if q >= 11 and q % 5 not in (1, 4) and int(pari.valuation(N, q)) == 1
           and int(pari.valuation(E.disc(), q)) % 5]
    if not q0s: return False
    q0 = q0s[0]; LE = Fraction(str(LALG(E)))
    if LE == 0 or v5(LE) != 0: return False
    res = []
    for D in range(-3, -3000, -1):
        if len(res) >= ND: break
        if N * D * D > 5 * 10**11: break
        if not int(pari.isfundamental(D)) or any(D % p == 0 for p in fac): continue
        if int(pari.kronecker(D, q0)) != -1 or any(int(pari.kronecker(D, p)) != 1 for p in fac if p != q0): continue
        res.append((D, v5(LE * Fraction(str(LALG(pari.ellinit(pari.elltwist(E, D))))))))
    ok = any(v == 0 for _, v in res)
    line = (f"[{label}] E=[{A},{B}] N={N} q0={q0} L_alg(E)={LE}  D,v5 : {res}  => eta0/xi_B unité en 5 : "
            f"{'OUI' if ok else 'non démontré'}")
    print(line, flush=True); out.append(line); return True
rng = random.Random(5); out = []
n = 0
tries = 0
while n < NC and tries < 200000:      # E2 en 3
    tries += 1
    u, w = 5 * rng.randint(-30, 30), rng.randint(-200, 200)
    if w % 5 == 0 or u % 3 == 0 or w % 3 == 0 or 4 * (27*u)**3 + 27 * (54*w)**2 == 0: continue
    Ep = pari.ellinit([27 * u, 54 * w])
    if int(pari.elllocalred(Ep, 3)[0]) != 1: continue
    Epm = pari.ellinit(pari('ellminimalmodel')(Ep))
    if int(pari.valuation(Epm.disc(), 3)) % 5: continue
    for sgn in (1, -1):
        if n < NC: n += test(3 * u, sgn * 2 * w, "E2 en 3", out)
print("E2 : essais", tries, flush=True)
n = 0; tries = 0
while n < NC and tries < 200000:      # E3 en 7 (I0*)
    tries += 1
    a, b = 5 * rng.randint(-40, 40), rng.randint(-300, 300)
    if b % 5 == 0 or 4 * a**3 + 27 * b * b == 0 or (4 * a**3 + 27 * b * b) % 7 == 0: continue
    a7 = int(pari.ellap(pari.ellinit([a, b]), 7))
    if (a7 - 8) % 5 and (a7 + 8) % 5: continue
    n += test(49 * a, 343 * b, "E3 en 7 (I0*)", out)
print("E3 en 7 : essais", tries, flush=True)
open(sys.path[0] + "/../results/test_multiplicite_un_construit.txt", "w").write("\n".join(out) + "\n")
