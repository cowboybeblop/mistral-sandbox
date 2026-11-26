import sys, time
from cypari import pari
pari.allocatemem(6*10**9)
ainv=eval(sys.argv[1]); p=int(sys.argv[2]); n=int(sys.argv[3])
E = pari.ellinit(ainv)
t=time.time()
def step(name, f):
    t=time.time()
    try:
        x=f(); print(name,'ok %.1fs'%(time.time()-t), flush=True); return x
    except Exception as e:
        print(name,'FAIL',str(e)[:50],'%.1fs'%(time.time()-t), flush=True); sys.exit()
M = step('msinit', lambda: pari.msinit(pari.ellglobalred(E)[0], 2, 1))
Ms = step('msfromell', lambda: pari.msfromell(E,1))
Mp = step('mspadicinit', lambda: pari.mspadicinit(Ms[0], p, n, 0))
mu = step('moments', lambda: pari.mspadicmoments(Mp, Ms[1]))
S = step('series', lambda: pari.mspadicseries(mu))
print(S)
