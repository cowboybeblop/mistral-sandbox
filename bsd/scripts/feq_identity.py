"""Piste 1 : contrôle global de la reformulation locale de BS §5 utilisée dans bound_v4.py :
   d(E) = r(E) r(E_{-1}) = beta_2 * beta_3 * sgn(Delta) * prod_{p > 3, p = 3 mod 4} alpha_p,
   beta_2 = d_2 chi_4(Delta'_2), beta_3 = d_3 (-1)^{v_3(Delta)}, alpha_p = d_p (-1)^{v_p(Delta)}, d_p (p > 3) par BS Lemme 36.
Les signes globaux w(E), w(E_{-1}) sont obtenus par l'équation fonctionnelle (lfuncheckfeq, eps = +1 et -1),
indépendamment de ellrootno. d_2, d_3 viennent de PARI (ellrootno local), vérifiés par feq_check.py.
Usage : python3 feq_identity.py [nombre] [hauteur]"""
import sys, random
from cypari import pari
pari.allocatemem(2 * 10**9); pari.set_real_precision(38)
NB = int(sys.argv[1]) if len(sys.argv) > 1 else 150; H = int(sys.argv[2]) if len(sys.argv) > 2 else 300
rng = random.Random(11)
def v(x, p): return 99 if x == 0 else int(pari.valuation(x, p))
def w_L(E):
    L = pari.lfuncreate(E); res = []
    for eps in (1, -1):
        L[5] = eps; res.append(float(pari.lfuncheckfeq(L)))
    if min(res) > -50 or max(res) < -10: return None
    return 1 if res[0] < res[1] else -1
done = bad = skip = 0
while done < NB:
    A, B = rng.randint(-H, H), rng.randint(1, H)
    D = -4 * A**3 - 27 * B**2
    if D == 0 or any(A % p**4 == 0 and B % p**6 == 0 for p in (2, 3, 5, 7)): continue
    E, Em = pari.ellinit([A, B]), pari.ellinit([A, -B])
    w1, w2 = w_L(E), w_L(Em)
    if w1 is None or w2 is None: skip += 1; continue
    b2 = int(pari.ellrootno(E, 2) * pari.ellrootno(Em, 2)) * (1 if (D // 2**v(D, 2)) % 4 == 1 else -1)
    b3 = int(pari.ellrootno(E, 3) * pari.ellrootno(Em, 3)) * (-1) ** v(D, 3)
    al = 1
    for p in pari.factor(abs(D))[0]:
        p = int(p)
        if p > 3 and p % 4 == 3:
            mult = int(pari.elllocalred(E, p)[1]) > 4
            al *= (-1 if mult else 1) * (-1) ** v(D, p)
    pred = b2 * b3 * (1 if D > 0 else -1) * al
    bad += pred != w1 * w2; done += 1
print(f"{done} courbes (|A|, B <= {H}), {skip} tests non concluants : identité fausse pour {bad} courbes")
