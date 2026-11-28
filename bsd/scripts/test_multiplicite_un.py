"""Programme réaliste, étape « multiplicité un » (lit/programme_realiste.md §4).
Réduction (DÉDUCTION, d'après Vatsal 2003 §2.4-4.3, Pollack-Weston Rem. 2.4, ARS Th. 3.6) : le problème B en un
premier q de N+ (E2, E3, N6) revient à ord_5(eta_0/xi_B) = 0, où eta_0 est le nombre de congruence de Hida
(niveau N) et xi_B celui du module de Brandt (algèbre définie ramifiée en N- = q0).
Formule de Gross : L(E,1) L(E^D,1) = (f,f) |theta_D|^2 / (sqrt|D| u^2 xi_B) * (unités en 5), et (f,f) ~ deg(phi) * Omega^+ Omega^-,
ord_5 deg(phi) = ord_5 eta_0 (ARS, 5^2 ne divise pas N). D'où :
      L_alg(E) * L_alg(E^D) = |theta_D|^2 * eta_0 / xi_B   (à des unités en 5 près),
avec D < 0 tel que q0 soit inerte et les autres premiers de N décomposés. Donc : s'il existe un tel D avec
v_5(L_alg(E) L_alg(E^D)) = 0, alors eta_0/xi_B est une unité (pas de problème B pour cette courbe).
On teste des courbes de la famille supersingulière (5 | A, 5 ne divise pas B) ayant un type E3 en 2 ou 3, et des témoins.
Usage : python3 test_multiplicite_un.py [ncourbes] [nD]"""
import sys, random
from fractions import Fraction
from cypari import pari
pari.allocatemem(2 * 10**9); pari.set_real_precision(30)
NC = int(sys.argv[1]) if len(sys.argv) > 1 else 6; ND = int(sys.argv[2]) if len(sys.argv) > 2 else 6
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
pari('lalg(E) = my(Em = ellinit(ellminimalmodel(E)), om = Em.omega[1] * if (Em.disc > 0, 2, 1)); bestappr(lfun(Em, 1) / om, 10^7)')
LALG = pari('lalg')
lt = pari('ltype3'); TW = {2: pari('[-1,2,-2,-5,10,-10]'), 3: pari('[3,-3]')}
NF = {l: pari(f'NFS{l}') for l in (2, 3)}; PRS = {l: pari(f'PRS{l}') for l in (2, 3)}
def lalg(E):
    """L(E,1)/Omega_E (Omega = période réelle du modèle minimal, fois 2 si Delta > 0), reconnu comme rationnel"""
    return Fraction(str(LALG(E)))
def v5(x):
    if x == 0: return None
    n, d, v = x.numerator, x.denominator, 0
    while n % 5 == 0: n //= 5; v += 1
    while d % 5 == 0: d //= 5; v -= 1
    return v
rng = random.Random(3); found = {"E3": 0, "témoin": 0}; out = []
while min(found.values()) < NC:
    A = 5 * rng.randint(-60, 60); B = rng.randint(-400, 400)
    if B % 5 == 0 or 4 * A**3 + 27 * B * B == 0: continue
    t2, t3 = (int(lt(A, B, l, TW[l], NF[l], PRS[l])) for l in (2, 3))
    fl = t2 % 10 + t3 % 10
    kind = "E3" if 21 in (t2, t3) and fl == 1 else ("témoin" if fl == 0 else None)
    if kind is None or found[kind] >= NC: continue
    E = pari.ellinit([A, B]); N = int(pari.ellglobalred(E)[0])
    if N > 60000 or int(pari.ellrootno(E)) != 1: continue
    fac = [int(p) for p in pari.factor(N)[0]]
    q0s = [q for q in fac if q >= 7 and q % 5 not in (1, 4) and int(pari.elllocalred(E, q)[0]) == 1
           and int(pari.valuation(pari.ellglobalred(E)[0], q)) == 1 and int(pari.valuation(E.disc(), q)) % 5]
    if not q0s: continue
    q0 = q0s[0]; LE = lalg(E)
    if LE == 0 or v5(LE) != 0: continue
    res = []
    for D in range(-3, -6000, -1):
        if len(res) >= ND: break
        if not int(pari.isfundamental(D)) or any(D % p == 0 for p in fac): continue
        if int(pari.kronecker(D, q0)) != -1 or any(int(pari.kronecker(D, p)) != 1 for p in fac if p != q0): continue
        LD = lalg(pari.ellinit(pari.elltwist(E, D)))
        res.append((D, v5(LE * LD)))
    found[kind] += 1
    ok = any(v == 0 for _, v in res)
    line = (f"[{kind}] E=[{A},{B}] N={N} types(2,3)=({t2},{t3}) q0={q0} L_alg(E)={LE}  D,v5 : {res}  "
            f"=> eta0/xi_B unité en 5 : {'OUI' if ok else 'non démontré'}")
    print(line, flush=True); out.append(line)
open(sys.path[0] + "/../results/test_multiplicite_un.txt", "w").write("\n".join(out) + "\n")
