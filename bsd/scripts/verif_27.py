"""Contrôles numériques du 27/11 (reverification.md).
(a) Lemme 8.14 de Wan : prédiction analytique Phi(n(b))/Phi(1) = 1 si v(b) >= s-t, -1/(q-1) si v(b) = s-t-1,
    0 sinon ; testée pour (t, s) = (1, 2), (1, 3), (2, 3) en p = 3 (méthode de wan_lemma814.py).
(b) Proposition R avec A trivial : vecteur phi de Kirillov 1_{O^x}, construit DANS LE MODÈLE INDUIT comme
    combinaison de translatés du vecteur sphérique (non ramifiée) ou du vecteur nouveau (Steinberg).
    On vérifie Phi_phi(diag(p^m, 1)) = 0 pour m != 0 par intégration directe sur B\\G (carte n^-(y)),
    indépendamment du modèle de Kirillov, et l'invariance de phi par K0(p^2)."""
import sys, random, cmath; sys.path.insert(0, sys.path[0])
from fractions import Fraction as Fr
from wan_lemma813 import v, mkchar, cond, mul, p, PHI
from wan_lemma814 import Phi_ct

def part_a():
    print("(a) Lemme 8.14 : Phi(n(b))/Phi(1), prédiction entre crochets")
    for t, s, L in [(1, 2, 6), (1, 3, 7), (2, 3, 7)]:
        jt = [j for j in range(PHI) if cond(j) == t][0]; js = [j for j in range(PHI) if cond(j) == s][0]
        chi1, chi2, th = mkchar(0, 0.9+0.1j), mkchar(jt, 1.1-0.3j), mkchar(js, 1.0)
        P1 = Phi_ct([[1, 0], [0, 1]], chi1, chi2, th, t, L)
        for k in range(0, s - t + 1):
            pred = 1 if k >= s - t else (-1/(p-1) if k == s - t - 1 else 0)
            vals = [Phi_ct([[1, u*p**k], [0, 1]], chi1, chi2, th, t, L) / P1 for u in (1, 2)]
            print(f"  t={t} s={s} v(b)={k}: {vals[0].real:+.6f} {vals[1].real:+.6f}  [{pred:+.6f}]"
                  + ("   <- contredit l'énoncé (v(b) < s-t)" if k < s - t and abs(vals[0]) > 1e-9 else ""))

# ---------- (b) modèle induit sur G entier ----------
def iwasawa(g):
    (a, b), (c, d) = g; det = a*d - b*c
    if c == 0 or (d != 0 and v(c) >= v(d)):
        return Fr(det, 1)/d, Fr(d), (v(Fr(c)/d) >= 1)          # k = n^-(c/d), Iwahori ssi v(c/d) >= 1
    return Fr(det, 1)/c, Fr(c), False                            # k = (0 -1; 1 d/c), hors Iwahori

def make_f(kind, al, dual=False):
    be = 1/al
    def f(g):
        b11, b22, iw = iwasawa(g); e = v(b11) - v(b22)
        if kind == "sph":                                        # induite unitaire : f~ = conj(f)
            return (al**v(b11) * be**v(b22)).conjugate()**(1 if dual else 0) * (al**v(b11) * be**v(b22))**(0 if dual else 1) * float(p)**(-e/2)
        sg = -1 if dual else 1                                   # Steinberg dans pi(|.|^1/2,|.|^-1/2) ;
        return float(p)**(-e/2 - sg*e/2) * (p if iw else -1)     # dual : pi(|.|^-1/2,|.|^1/2) (Wan, p. 84)
    return f

def make_phi(kind, al, dual=False):
    f = make_f(kind, al, dual); be = 1/al
    if dual and kind == "sph": al, be = al.conjugate(), be.conjugate()
    D = lambda j: [[Fr(1, p**j), 0], [0, 1]]
    if kind == "sph":
        cs = [(0, 1), (1, -p**-0.5*(al+be)), (2, 1/p)]
    else:
        cs = [(0, 1), (1, -1/p)]
    return lambda g: sum(c * f(mul(g, D(j))) for j, c in cs)

def Phi_ind(phi, g, phit, K=14, L=6):
    """<pi(g) phi, phit> = int_{B\\G} phi(x g) phit(x) dx, carte x = n^-(y), y in Q_p (tronquée)."""
    tot = 0
    for y in range(0, p**L):                                     # v(y) >= 0
        n = [[1, 0], [Fr(y), 1]]
        tot += phi(mul(n, g)) * phit(n) / p**L
    for k in range(1, K+1):                                      # v(y) = -k
        for u in range(1, p**L):
            if u % p == 0: continue
            n = [[1, 0], [Fr(u, p**k), 1]]
            tot += phi(mul(n, g)) * phit(n) * p**k / p**L
    return tot

def part_b():
    print("(b) Prop. R, A trivial : Phi_phi(diag(p^m,1))/Phi_phi(1)  (attendu : 0 pour m != 0)")
    random.seed(5)
    for kind, al in [("sph", cmath.exp(0.7j)), ("sph", cmath.exp(2.1j)), ("st", 1)]:
        phi, phit = make_phi(kind, al), make_phi(kind, al, dual=True)
        P0 = Phi_ind(phi, [[1, 0], [0, 1]], phit)
        vals = [abs(Phi_ind(phi, [[Fr(p)**m, 0], [0, 1]], phit) / P0) for m in (-2, -1, 1, 2)]
        err = 0
        for _ in range(4):                                       # invariance par K0(p^2)
            a, d = random.choice([1, 2, 4, 5]), random.choice([1, 2, 4, 5])
            k = [[a, random.randrange(p**4)], [p**2*random.randrange(p**3), d]]
            x = [[1, 0], [Fr(random.randrange(1, 50), p**random.randrange(0, 3)), 1]]
            err = max(err, abs(phi(mul(x, k)) - phi(x)))
        print(f"  {kind:4s} alpha={al:.3f}: |Phi(1)|={abs(P0):.4f}  m=-2,-1,1,2 : "
              + " ".join(f"{x:.1e}" for x in vals) + f"   ecart K0(p^2) = {err:.1e}")

if __name__ == "__main__":
    (part_b if "b" in sys.argv else (lambda: (part_a(), part_b())))()
