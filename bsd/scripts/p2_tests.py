"""Tests en p = 2 : (1) Lemme 8.13 de Wan (support et valeurs de Phi pour f_chi de niveau K_t) ;
(2) Proposition R (probleme_A_note §13) pour pi non ramifiée, Steinberg, série principale ramifiée.
Caractères de Z_2^x = {+-1} x <5> : chi_{e,j}(+-5^k) = (-1)^{e*[signe -]} exp(2 i pi j k / 2^(M-2))."""
from fractions import Fraction as Fr
import cmath, random
p = 2; M = 12; N = p**M
LOG = {}
x = 1
for k in range(N//4):
    LOG[x] = (0, k); LOG[(-x) % N] = (1, k); x = x*5 % N
def v(q):
    q = Fr(q)
    if q == 0: return 10**9
    n, d, e = q.numerator, q.denominator, 0
    while n % 2 == 0: n //= 2; e += 1
    while d % 2 == 0: d //= 2; e -= 1
    return e
def unit(q):
    q = Fr(q); u = q / Fr(2)**v(q)
    return u.numerator * pow(u.denominator, -1, N) % N
def mkchar(e, j, A):
    def chi(q):
        s, k = LOG[unit(q)]
        return (A**v(q)) * ((-1)**(e*s)) * cmath.exp(2j*cmath.pi*j*k/(N//4))
    return chi
def cond(e, j):
    ch = mkchar(e, j, 1)
    for m in range(0, M+1):
        if all(abs(ch(u)-1) < 1e-9 for u in range(1, N, 2) if (u-1) % 2**m == 0): return m
def mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]
def bdec(g):
    (a, b), (c, d) = g
    if d == 0: return None
    det = a*d - b*c; return Fr(det)/d, Fr(d), Fr(c)/d
# ---------- (1) Wan 8.13 ----------
def phi_813(g, chi1, chi2, t, L):
    s = 0
    for y in range(0, 2**L, 2**t):
        r = bdec(mul([[1,0],[y,1]], g))
        if r is None: continue
        b11, b22, yp = r
        if v(yp) < t: continue
        s += chi1(b11)*chi2(b22)*2**(-(v(b11)-v(b22))/2)
    return s / 2**L
# ---------- (2) Proposition R ----------
def phi_R(g, chi1, chi2, A, r, L):
    s = 0
    for y in range(2**r, 2**L, 2**r):
        if v(y) != r: continue
        m = bdec(mul([[1,0],[y,1]], g))
        if m is None: continue
        b11, b22, yp = m
        if v(yp) != r: continue
        val = chi1(b11)*chi2(b22)*2**(-(v(b11)-v(b22))/2)*A(yp/2**r).conjugate()
        s += val * A(Fr(y, 2**r))
    return s / 2**L
def test_R(label, chi1, chi2, A, r, t1, L):
    random.seed(7)
    one = [[1,0],[0,1]]; P1 = phi_R(one, chi1, chi2, A, r, L); out = []
    for n in range(1, 4):
        m1 = max(abs(phi_R(mul([[1, random.randrange(2**L)], [0, 1]], [[2**n, 0], [0, 1]]), chi1, chi2, A, r, L)) for _ in range(3))
        m2 = max(abs(phi_R(mul([[Fr(1, 2**n), 0], [0, 1]], [[1, 0], [2**(t1-n)*u, 1]]), chi1, chi2, A, r, L)) for u in [1, 3, 5, 7])
        out.append(max(m1, m2))
    err = 0
    for _ in range(8):
        a_, d_ = random.choice([1,3,5,7,9,11]), random.choice([1,3,5,7,9,11])
        k = [[a_, random.randrange(2**L)], [2**t1*random.randrange(2**L), d_]]
        det = k[0][0]*k[1][1]-k[0][1]*k[1][0]
        pred = chi1(Fr(det, d_))*chi2(Fr(d_))*A(Fr(det, d_)).conjugate()*A(Fr(d_))*P1
        err = max(err, abs(phi_R(k, chi1, chi2, A, r, L) - pred))
    print(f"{label}: |Phi(1)|={abs(P1):.4f} ; max|Phi| cellules n=1..3 : {['%.1e'%x for x in out]} ; erreur de type sur K_t1 : {err:.1e}")
if __name__ == "__main__":
    # (1) Wan 8.13, t = 3 : chi1 non ramifié, chi2 de conducteur 3
    t = 3; e2, j2 = [(e, j) for e in (0, 1) for j in range(N//4) if cond(e, j) == t][0]
    A1, A2 = 0.7+0.4j, 1.3-0.2j
    c1, c2 = mkchar(0, 0, A1), mkchar(e2, j2, A2)
    print(f"(1) Wan 8.13, p = 2, t = {t}, cond chi2 = {cond(e2, j2)}")
    w = [[0, 1], [-1, 0]]
    def Iw():
        while True:
            a, b, c, d = (random.randrange(N) for _ in range(4)); c = c*2 % N
            if a % 2 and d % 2: return [[a, b], [c, d]]
    random.seed(1)
    for n in range(0, 3):
        sig = [[2**n, 0], [0, 1]]
        res = {}
        for name, mk in {"K1 s K1": lambda: mul(mul(Iw(), sig), Iw()), "K1 w s w K1": lambda: mul(mul(Iw(), mul(mul(w, sig), w)), Iw()),
                         "K1 w s K1": lambda: mul(mul(Iw(), mul(w, sig)), Iw()), "K1 s w K1": lambda: mul(mul(Iw(), mul(sig, w)), Iw())}.items():
            vals = [abs(phi_813(mk(), c1, c2, t, min(M-1, t + 2*n + 3))) for _ in range(5)]
            res[name] = max(vals)
        print(f"  n={n}: " + " ; ".join(f"{k} max {v_:.3g}" for k, v_ in res.items()))
    print(f"  valeurs attendues : Vol(K_t)*|alpha|^n*2^(-n/2) = {[round(2**-t*abs(A1)**n*2**(-n/2),4) for n in range(3)]} et {[round(2**-t*abs(A2)**n*2**(-n/2),4) for n in range(3)]}")
    # (2) Proposition R
    print("(2) Proposition R, p = 2")
    eA, jA = [(e, j) for e in (0, 1) for j in range(N//4) if cond(e, j) == 2][0]   # A de conducteur 2
    A = mkchar(eA, jA, 1.0)
    test_R("non ramifiée", mkchar(0, 0, 0.83+0.31j), mkchar(0, 0, 1.21-0.47j), A, 2, 4, 9)
    test_R("Steinberg", mkchar(0, 0, 2**-0.5), mkchar(0, 0, 2**0.5), A, 2, 4, 9)
    # série principale ramifiée : chi quadratique de conducteur 2 (chi(-1) = -1), A' de conducteur 3 avec chi A' de conducteur 3
    chi_e, chi_j = 1, 0
    eB, jB = [(e, j) for e in (0, 1) for j in range(N//4) if cond(e, j) == 3 and cond((e + chi_e) % 2, j) == 3][0]
    test_R("SP ramifiée (chi quadratique cond 2)", mkchar(chi_e, chi_j, 0.83+0.31j), mkchar(chi_e, chi_j, 1.21-0.47j),
           mkchar(eB, jB, 1.0), 3, 6, 10)
