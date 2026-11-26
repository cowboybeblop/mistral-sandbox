"""Verification independante (groupe fini GL2(Z/27)) de Phi_f(n(b)) pour f = f_{chi,theta} de Wan, Lemme 8.14.
f(k) = chi1(a)chi2(d)theta(c/p^t1) si k = (a b;0 d)(1 0;c 1) avec v(c) = t1 ; f~ idem avec chi^-1, theta^-1.
Phi(g) = (1/|K|) sum_k f(k g) f~(k), pour g = n(b) dans K."""
import cmath, itertools
p, M = 3, 3; N = p**M; PHI = N - N//p
log = {}; x = 1
for e in range(PHI): log[x] = e; x = x*2 % N
def ch(j): return lambda u: cmath.exp(2j*cmath.pi*j*log[u % N]/PHI)
def cond(j):
    for m in range(M+1):
        if all(abs(ch(j)(u)-1)<1e-9 for u in range(1,N) if u%p and (u-1)%p**m==0): return m
t1 = 1
j1 = [j for j in range(PHI) if cond(j)==1][0]; js = [j for j in range(PHI) if cond(j)==2][0]
chi1, chi2, th = ch(0), ch(j1), ch(js)
def val(k, inv=False):
    a_, b_, c_, d_ = k
    if d_ % p == 0: return 0
    di = pow(d_, -1, N); c = c_*di % N
    if c % p != 0 or c % p**2 == 0: return 0      # v(c) = t1 = 1 exactement (mod 27, v(c)<=2 visible)
    a = (a_ - b_*c_*di) % N
    cu = (c//p)                                     # c/p mod 9 suffit (theta de conducteur 2)
    z = chi1(a)*chi2(d_)*th(cu if cu % p else 1)
    return z.conjugate() if inv else z
def Phi(b):
    s = 0; cnt = 0
    for a_,b_,c_,d_ in itertools.product(range(N), repeat=4):
        if (a_*d_-b_*c_) % p == 0: continue
        cnt += 1
        ft = val((a_,b_,c_,d_), inv=True)
        if ft == 0: continue
        s += val((a_, (a_*b+b_) % N, c_, (c_*b+d_) % N)) * ft   # k * n(b)
    return s/cnt
for b in [0, 1, 2, 3, 9]:
    print(f"b={b}: Phi_f(n(b)) = {Phi(b):.5f}")
