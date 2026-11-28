"""Suite de test_multiplicite_un.py : cas construits.
  E2 en 3 : E = tordue par 3 d'une courbe E' multiplicative en 3 avec 5 | v_3(Delta(E')) : (A, B) = (9a, 27b) ;
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
while n < NC:      # E2 en 3
    a, b = 5 * rng.randint(-40, 40), rng.randint(-300, 300)
    if b % 5 == 0 or a % 3 == 0 or 4 * a**3 + 27 * b * b == 0: continue
    Ep = pari.ellinit([a, b]); lr = pari.elllocalred(Ep, 3)
    if int(lr[0]) != 1 or int(pari.valuation(Ep.disc(), 3)) % 5: continue     # multiplicatif, 5 | v_3
    n += test(9 * a, 27 * b, "E2 en 3", out)
n = 0
while n < NC:      # E3 en 7 (I0*)
    a, b = 5 * rng.randint(-40, 40), rng.randint(-300, 300)
    if b % 5 == 0 or 4 * a**3 + 27 * b * b == 0 or (4 * a**3 + 27 * b * b) % 7 == 0: continue
    a7 = int(pari.ellap(pari.ellinit([a, b]), 7))
    if (a7 - 8) % 5 and (a7 + 8) % 5: continue
    n += test(49 * a, 343 * b, "E3 en 7 (I0*)", out)
open(sys.path[0] + "/../results/test_multiplicite_un_construit.txt", "w").write("\n".join(out) + "\n")
