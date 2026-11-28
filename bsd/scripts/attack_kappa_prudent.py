"""Relecture adverse n° 4 : test global du kappa PRUDENT (piste 1), sans cellules.
Famille : 5 | A, 5 ne divise pas B ; semistable en l >= 7 sans multiplicatif à 5 | v_l ; en 2 et 3, type admis
(drapeau « non minimal » nul, classification de local_types_v3.py appliquée à la courbe elle-même).
F' : d(E) = r(E) r(E_{-1}) = -1 (signes globaux) et E_{-1} aussi admise en 2 et 3.
Prévu : kappa_ss prudent = 0,5687 (bound_v6, étape « + piste 1 »).
Usage : python3 attack_kappa_prudent.py n Amax"""
import sys, random, math
from cypari import pari
pari.allocatemem(2 * 10**9)
n, Amax = int(sys.argv[1]), int(sys.argv[2]); Bmax = int(math.sqrt(4 * Amax**3 / 27)); rng = random.Random(41)
for l, pols in ((2, ["x^4-4*x^2+2", "x^4+4*x^2+2"]), (3, ["x^3-3*x+1"])):
    pari(f'NFS{l} = [{",".join("nfinit("+p+")" for p in pols)}]; PRS{l} = vector(#NFS{l}, i, idealprimedec(NFS{l}[i], {l})[1]);')
pari('goodover(a,b,tw,NF,PR) = my(T = concat([1], tw)); for (i = 1, #NF, for (j = 1, #T, my(d = T[j], '
     'E = ellinit([0,0,0,d^2*a,d^3*b], NF[i])); if (#E && elllocalred(E, PR[i])[1] == 0, return(1)))); 0')
pari('ltype3(a,b,l,tw,NF,PR) = my(E = ellinit([a,b]), f, j, vj); '
     'f = elllocalred(E, l)[1]; j = E.j; vj = if (j == 0, 10^6, valuation(j, l)); '
     'if (f == 0, return(0)); if (f == 1, return(0 + (vj % 5 == 0))); if (vj < 0, return(10 + (vj % 5 == 0))); '
     'for (i = 1, #tw, my(d = tw[i], Ed = ellinit([d^2*a, d^3*b])); if (elllocalred(Ed, l)[1] == 0, '
     '  my(ap = ellap(Ed, l)); return(20 + ((ap - (l+1)) % 5 == 0 || (ap + (l+1)) % 5 == 0)))); '
     'if (goodover(a, b, tw, NF, PR), return(30)); 40')
lt = pari('ltype3'); TW = {2: pari('[-1,2,-2,-5,10,-10]'), 3: pari('[3,-3]')}
NF = {l: pari(f'NFS{l}') for l in (2, 3)}; PRS = {l: pari(f'PRS{l}') for l in (2, 3)}
def admis(A, B): return all(int(lt(A, B, l, TW[l], NF[l], PRS[l])) % 10 == 0 for l in (2, 3))
def fam(A, B, D):
    if A % 5 or B % 5 == 0: return False
    for p in pari.factor(abs(D))[0]:
        p = int(p)
        if p >= 7 and ((A % p == 0 and B % p == 0) or int(pari.valuation(D, p)) % 5 == 0): return False
    return admis(A, B)
done = m = 0
while done < n:
    A = 5 * (rng.randint(-Amax, Amax) // 5); B = rng.randint(-Bmax, Bmax)
    if max(4 * abs(A)**3, 27 * B * B) > 4 * Amax**3: continue
    D = -4 * A**3 - 27 * B**2
    if D == 0 or any(A % p**4 == 0 and B % p**6 == 0 for p in (2, 3, 7, 11, 13)) or not fam(A, B, D): continue
    done += 1
    d = int(pari.ellrootno(pari.ellinit([A, B]))) * int(pari.ellrootno(pari.ellinit([A, -B])))
    m += d == -1 and admis(A, -B)
p = m / n; se = math.sqrt(p * (1 - p) / n)
print(f"famille prudente, n = {n} : P(F') = {p:.4f} ± {se:.4f} ; prévu 0,5687 (écart {(p - 0.5687) / se:+.1f} σ)")
