"""dim Hom_{K0(p^n)}(rho1(a)rho2(d), pi(chi1,chi2)) par la formule des caracteres.
pi(chi1,chi2)|K = Ind_{B(Z/p^M)}^{GL2(Z/p^M)} (chi1 x chi2), M = n.
Usage : test du critere c(pi (x) rho1^{-1}) <= n (Casselman apres torsion)."""
import cmath, itertools, sys
p = 3

def chars(M):
    N = p**M; phi = N - N//p
    g = 2  # racine primitive mod 3^M
    log = {}; x = 1
    for e in range(phi): log[x] = e; x = x*g % N
    def chi(j):
        return lambda u: cmath.exp(2j*cmath.pi*j*log[u % N]/phi)
    return phi, log, chi

def cond(chi, M):
    N = p**M
    for m in range(0, M+1):
        if all(abs(chi(u)-1) < 1e-9 for u in range(1, N) if u % p and (u-1) % (p**m) == 0):
            return m
    return None

def dim_iso(n, chi1, chi2, rho1, rho2):
    M = n; N = p**M
    pts = [(c, 1) for c in range(N)] + [(1, d) for d in range(0, N, p)]
    idx = {pt: i for i, pt in enumerate(pts)}
    def norm(c, d):
        c %= N; d %= N
        if d % p: inv = pow(d, -1, N); return (c*inv % N, 1)
        inv = pow(c, -1, N); return (1, d*inv % N)
    def rep(pt):
        c, d = pt
        return ((1, 0), (c, 1)) if d == 1 and not (c == 1 and d % p == 0 and False) and pt[1] == 1 else ((0, N-1), (1, d))
    reps = [((1, 0), (c, 1)) for c in range(N)] + [((0, N-1), (1, d)) for d in range(0, N, p)]
    def mul(A, B):
        return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % N for j in range(2)) for i in range(2))
    def inv(A):
        (a, b), (c, d) = A; det = pow((a*d-b*c) % N, -1, N)
        return ((d*det % N, (-b)*det % N), ((-c)*det % N, a*det % N))
    reps_inv = [inv(k) for k in reps]
    tot = 0; cnt = 0
    for a, b, c, d in itertools.product(range(N), range(N), range(0, N, p**n) if n else range(N), range(N)):
        if a % p == 0 or d % p == 0: continue
        g = ((a, b), (c, d))
        tr = 0
        for i, k in enumerate(reps):
            r = mul(k, g)
            if norm(r[1][0], r[1][1]) == pts[i]:
                bb = mul(r, reps_inv[i])
                tr += chi1(bb[0][0]) * chi2(bb[1][1])
        tot += (rho1(a)*rho2(d)).conjugate() * tr; cnt += 1
    return tot/cnt

if __name__ == "__main__":
    n = int(sys.argv[1])
    phi, log, X = chars(n)
    # chi_f1 = 1, chi_f2 = caractere d'ordre 2 (conducteur 1), theta de conducteur 2
    one = X(0)
    f2 = X(phi//2)
    th = [j for j in range(phi) if cond(X(j), n) == 2][0]
    th = X(th); thinv = lambda u: th(u).conjugate()
    print("cond chi_f2 =", cond(f2, n), " cond theta =", cond(th, n))
    # type de Wan : rho1 = chi_f1 * theta, rho2 = chi_f2 * theta^-1
    r1 = lambda u: one(u)*th(u); r2 = lambda u: f2(u)*thinv(u)
    print(f"n={n} type Wan (chi_f1 th, chi_f2 th^-1) : dim =", round(dim_iso(n, one, f2, r1, r2).real, 6))
    # temoin : type (chi_f1, chi_f2) sans theta
    print(f"n={n} type temoin (chi_f1, chi_f2)      : dim =", round(dim_iso(n, one, f2, one, f2).real, 6))
