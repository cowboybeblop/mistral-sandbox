"""Même test que reparation_ps.py pour (i) Steinberg (nu1/nu2 = |.|, sous-espace de pi(|.|^1/2,|.|^-1/2) :
f est d'intégrale nulle sur K car A est ramifié) et (ii) série principale ramifiée pi(chi nu1, chi nu2),
chi quadratique de conducteur 1 (cas de la tordue g' aux premiers de D_L), avec rho = A tel que chi*A ramifié."""
import sys, random, cmath; sys.path.insert(0, '/home/user/mistral-sandbox/bsd/scripts')
from wan_lemma813 import Fr, v, mkchar, cond, mul, p, PHI
def run(chi1, chi2, A, r, t1, L, label):
    Ainv = lambda u: A(u).conjugate()
    def fv(g):
        (a, b), (c, d) = g
        if d == 0: return 0
        det = a*d - b*c; yp = Fr(c)/d
        if v(yp) != r: return 0
        b11, b22 = Fr(det)/d, Fr(d)
        return chi1(b11)*chi2(b22)*p**(-(v(b11)-v(b22))/2)*Ainv(yp/p**r)
    def ft(y):  # vecteur dual dans pi~ : chi^-1, A
        return A(Fr(y, p**r))
    def Phi(g):
        s = 0
        for y in range(p**r, p**L, p**r):
            if v(y) != r: continue
            s += fv(mul([[1,0],[y,1]], g)) * ft(y)
        return s / p**L
    P1 = Phi([[1,0],[0,1]]); random.seed(5); out = []
    for n in range(1, 4):
        m1 = max(abs(Phi(mul([[1, random.randrange(p**L)], [0, 1]], [[p**n, 0], [0, 1]]))) for _ in range(3))
        m2 = max(abs(Phi(mul([[Fr(1, p**n), 0], [0, 1]], [[1, 0], [p**(t1-n)*u, 1]]))) for u in [1, 2, 4])
        out.append(max(m1, m2))
    err = 0
    for _ in range(8):
        a_, d_ = random.choice([1,2,4,5,7,8]), random.choice([1,2,4,5,7,8])
        k = [[a_, random.randrange(p**L)], [p**t1*random.randrange(p**L), d_]]
        det = k[0][0]*k[1][1]-k[0][1]*k[1][0]
        pred = chi1(Fr(det, d_))*chi2(Fr(d_))*Ainv(Fr(det, d_))*A(Fr(d_))*P1
        err = max(err, abs(Phi(k) - pred))
    print(f"{label}: Phi(1)={abs(P1):.4f} ; max|Phi| cellules n=1..3 : {['%.1e'%x for x in out]} ; erreur de type sur K_t1 : {err:.1e}")
if __name__ == "__main__":
    r, t1, L = 1, 3, 7
    jA = [j for j in range(PHI) if cond(j) == 1]
    A = mkchar(jA[0], 1.0)
    # (i) Steinberg : chi1 = |.|^{1/2}, chi2 = |.|^{-1/2}  (valeurs en p : 3^{-1/2}, 3^{1/2})
    run(mkchar(0, 3**-0.5), mkchar(0, 3**0.5), A, r, t1, L, "Steinberg (sous-module de pi(|.|^1/2,|.|^-1/2))")
    # (ii) série principale ramifiée : chi quadratique de conducteur 1 (j = PHI/2), A tel que chi*A ramifié
    chi = PHI // 2
    jB = [j for j in jA if (j + chi) % PHI != 0 and cond((j + chi) % PHI) >= 1][0]
    run(mkchar(chi, 0.83+0.31j), mkchar(chi, 1.21-0.47j), mkchar(jB, 1.0), r, t1, L, "SP ramifiée pi(chi nu1, chi nu2), chi quadratique")
