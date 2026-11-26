import time
from cypari import pari
pari.allocatemem(4*10**9)
pari('read("scripts/mtt.gp")')
for ainv,p in [([0,1,1,-2,0],5),([0,1,1,-2,0],7),([0,0,1,-1,0],5),([0,-1,1,-10,-20],7),([1,0,0,0,1],5)]:
    E=pari.ellinit(ainv); MS=pari.msfromell(E,1)
    for n in [5,6,7]:
        t=time.time()
        c=pari('mtt_series')(E,MS,p,n,3,30); s=pari('mtt_s_coeffs')(c,p,30)
        print(ainv,p,n,'c=',[str(x)[:40] for x in c[:3]],'%.1fs'%(time.time()-t))
        print('   s-coeffs*k!:', [str(s[k]*pari.factorial(k))[:60] for k in range(3)])
    print('   PARI ellpadicL derivs:', [str(pari.ellpadicL(E,p,6,0,k))[:60] for k in range(3)])
