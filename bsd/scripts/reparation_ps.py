"""Test de la réparation (probleme_A_note §13) : pi0 = pi(nu1, nu2) NON RAMIFIÉE (p = 3), A caractère de
conducteur r. Vecteur phi in pi0 : f(n^-(y)) = A^{-1}(y/p^r) 1[v(y) = r]  (= vecteur nouveau de pi0 (x) A,
propre pour K0(p^2r) de type A^{-1}(a)A(d)). On vérifie :
 (a) Phi_f s'annule sur les cellules n != 0 de Wan 8.13 (niveau t1 >= 2r) ;
 (b) sur K_{t1}, Phi_f(k) = A^{-1}(a_k)A(d_k) Phi_f(1).
Phi(g) = int_{v(y)=r} f(n^-(y) g) f~(n^-(y)) dy, f~ = vecteur analogue dans pi0~ (A au lieu de A^{-1})."""
import sys, random, cmath; sys.path.insert(0, '/home/user/mistral-sandbox/bsd/scripts')
from wan_lemma813 import Fr, v, unit, mkchar, cond, mul, p, PHI
nu1, nu2 = mkchar(0, 0.83+0.31j), mkchar(0, 1.21-0.47j)       # non ramifiés génériques
def f_val(g, Ainv, r):
    (a, b), (c, d) = g
    if d == 0: return 0
    det = a*d - b*c; yp = Fr(c) / d
    if v(yp) != r: return 0
    b11, b22 = Fr(det)/d, Fr(d)
    return nu1(b11)*nu2(b22)*p**(-(v(b11)-v(b22))/2)*Ainv(yp/p**r)
def Phi(g, A, Ainv, r, L):
    s = 0
    for y in range(p**r, p**L, p**r):
        if v(y) != r: continue
        s += f_val(mul([[1,0],[y,1]], g), Ainv, r) * A(Fr(y, p**r))
    return s / p**L
if __name__ == "__main__":
    r = 1; t1 = 3; L = 7
    jA = [j for j in range(PHI) if cond(j) == r][0]
    A = mkchar(jA, 1.0); Ainv = lambda u: A(u).conjugate()
    one = [[1,0],[0,1]]; P1 = Phi(one, A, Ainv, r, L)
    print("Phi(1) =", P1)
    random.seed(3)
    for n in range(0, 4):
        m1 = max(abs(Phi(mul([[1, random.randrange(p**L)], [0, 1]], [[p**n, 0], [0, 1]]), A, Ainv, r, L)) for _ in range(4))
        m2 = max(abs(Phi(mul([[Fr(1, p**n), 0], [0, 1]], [[1, 0], [p**(t1-n)*u, 1]]), A, Ainv, r, L))
                 for u in [1, 2, 4, 5])
        print(f"n={n}: max|Phi| cellule diag(p^n,1)n(y) = {m1:.3e} ; cellule diag(p^-n,1)n^-(p^(t1-n)u) = {m2:.3e}")
    # (b) type sur K_{t1}
    err = 0
    for _ in range(12):
        a_, d_ = random.choice([1,2,4,5,7,8]), random.choice([1,2,4,5,7,8])
        b_, c_ = random.randrange(p**L), p**t1 * random.randrange(p**L)
        k = [[a_, b_], [c_, d_]]
        val = Phi(k, A, Ainv, r, L)
        pred = Ainv(Fr(a_*d_ - b_*c_, d_)) * A(Fr(d_)) * P1
        err = max(err, abs(val - pred))
    print("(b) max |Phi(k) - A^-1(a)A(d)Phi(1)| sur K_t1 :", f"{err:.2e}")
