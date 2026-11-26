"""Test du Lemme 8.14 de Wan : f = f_{chi,theta} in pi(chi1,chi2), cond(chi1/chi2)=t1, cond(theta)=s>t1,
f(b n^-(y)) = chi(b) delta^1/2(b) * theta(y/p^t1) * 1[v(y)=t1]  (pour y entier).
On calcule Phi_f(n(b)) = <pi(n(b)) f, f~> pour b de diverses valuations, et la projection
sur le type (K0(p^t2), Xi^-1), t2 = t1+s, via sum_b Phi_f(n(b))."""
import sys; sys.path.insert(0, '/home/user/mistral-sandbox/bsd/scripts')
from wan_lemma813 import *

def f_ct(g, chi1, chi2, th, t1):
    (a, b), (c, d) = g
    if d == 0: return 0
    det = a*d - b*c; yp = Fr(c) / d
    if v(yp) != t1: return 0
    b11, b22 = Fr(det) / d, Fr(d)
    return chi1(b11) * chi2(b22) * th(yp / p**t1) * p**(-(v(b11)-v(b22))/2)

def Phi_ct(g, chi1, chi2, th, t1, L):
    s = 0
    for y in range(p**t1, p**L, p**t1):
        if v(y) != t1: continue
        ft = (th(Fr(y, p**t1))).conjugate()   # f~ = f_{chi^-1, theta^-1} en n^-(y)
        s += f_ct(mul([[1, 0], [y, 1]], g), chi1, chi2, th, t1) * ft
    return s / p**L

if __name__ == "__main__":
    t1, s = 1, 2; t2 = t1 + s
    j1 = [j for j in range(PHI) if cond(j) == t1][0]
    js = [j for j in range(PHI) if cond(j) == s][0]
    chi1, chi2 = mkchar(0, 0.9+0.1j), mkchar(j1, 1.1-0.3j)
    th = mkchar(js, 1.0)
    L = 6
    print(f"t1={t1} s={s} t2={t2} ; cond chi2/chi1={cond(j1)}, cond theta={cond(js)}")
    print("Phi_f(1) =", Phi_ct([[1,0],[0,1]], chi1, chi2, th, t1, L))
    for k in range(0, s+1):
        for u in [1, 2, 4]:
            b = u * p**k
            val = Phi_ct([[1, b], [0, 1]], chi1, chi2, th, t1, L)
            print(f"v(b)={k} b={b}: Phi_f(n(b)) = {val:.5f}")
    # projection sur le type K0(p^t2) : moyenne de Phi_f(n(b)) sur b in O/p^(s-t1)
    tot = sum(Phi_ct([[1, b], [0, 1]], chi1, chi2, th, t1, L) for b in range(p**(s-t1)))
    print("sum_{b mod p^(s-t1)} Phi_f(n(b)) =", round(abs(tot), 6))
