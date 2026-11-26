"""Test numerique du Lemme 8.13 de Wan (1408.4044) : support du coefficient matriciel
Phi(g) = <pi(g) f_chi, f~_chi> pour f_chi in pi(chi1,chi2), supporte sur K_t et valant chi1(a)chi2(d).
Modele : B\\G, carte n^-(y). Phi(g) = int_{y in p^t Z_p} f(n^-(y) g) dy (f~ = 1 sur n^-(p^t Z_p)).
p = 3, calcul exact en rationnels, caracteres de Z_3^x mod 3^M."""
from fractions import Fraction as Fr
import cmath, random, itertools, sys
p = 3; M = 7; N = p**M; PHI = N - N//p
log = {}; x = 1
for e in range(PHI): log[x] = e; x = x*2 % N

def v(q):
    q = Fr(q)
    if q == 0: return 10**9
    n, d, e = q.numerator, q.denominator, 0
    while n % p == 0: n //= p; e += 1
    while d % p == 0: d //= p; e -= 1
    return e

def unit(q):
    q = Fr(q); e = v(q); u = q / Fr(p)**e
    return u.numerator * pow(u.denominator, -1, N) % N

def mkchar(j, A):  # chi(p^e u) = A^e * exp(2 pi i j log(u)/PHI)
    return lambda q: (A**v(q)) * cmath.exp(2j*cmath.pi*j*log[unit(q)]/PHI)

def cond(j):
    for m in range(M+1):
        if all(abs(cmath.exp(2j*cmath.pi*j*log[u]/PHI)-1) < 1e-9 for u in range(1, N) if u % p and (u-1) % p**m == 0):
            return m

def mul(A, B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def f(g, chi1, chi2, t):
    (a, b), (c, d) = g
    if d == 0: return 0
    det = a*d - b*c; yp = Fr(c) / d
    if v(yp) < t: return 0
    b11, b22 = Fr(det) / d, Fr(d)
    return chi1(b11) * chi2(b22) * (Fr(p)**(-(v(b11)-v(b22))/2) if False else p**(-(v(b11)-v(b22))/2))

def Phi(g, chi1, chi2, t, L=None):
    L = L or M
    s = 0
    for y in range(0, p**L, p**t):
        s += f(mul([[1, 0], [y, 1]], g), chi1, chi2, t)
    return s / p**L

if __name__ == "__main__":
    t = 2
    jr = [j for j in range(PHI) if cond(j) == t][0]
    A1, A2 = 0.7+0.4j, 1.3-0.2j   # parametres non ramifies generiques
    chi1, chi2 = mkchar(0, A1), mkchar(jr, A2)
    D = lambda a, d: [[Fr(a), 0], [0, Fr(d)]]
    w = [[0, 1], [-1, 0]]
    def Iw():  # element aleatoire de l'Iwahori K1 (c = 0 mod p)
        while True:
            a, b, c, d = (random.randrange(N) for _ in range(4)); c = c*p % N
            if a % p and d % p: return [[a, b], [c, d]]
    random.seed(1)
    print("t =", t, " cond(chi2) =", cond(jr))
    for n in range(0, 4):
        sig = D(p**n, 1)
        cells = {"K1 s_n K1": lambda: mul(mul(Iw(), sig), Iw()),
                 "K1 w s_n w K1": lambda: mul(mul(Iw(), mul(mul(w, sig), w)), Iw()),
                 "K1 w s_n K1": lambda: mul(mul(Iw(), mul(w, sig)), Iw()),
                 "K1 s_n w K1": lambda: mul(mul(Iw(), mul(sig, w)), Iw())}
        for name, gen in cells.items():
            vals = [abs(Phi(gen(), chi1, chi2, t, L=min(M, t+2*n+2))) for _ in range(6)]
            print(f"n={n} {name:14s} max|Phi| = {max(vals):.4g}  nb non nuls = {sum(x>1e-9 for x in vals)}/6")
