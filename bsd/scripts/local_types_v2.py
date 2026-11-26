"""Raffinement de local_types.py (branche claude/artifact-review-prompt-pfjqwc) : on sépare la classe
« autre » en
  ps_sup : série principale d'ordre > 2 (inertie abélienne cyclique d'ordre 3, 4, 6), détectée par
           bonne réduction sur une extension cyclique ramifiée (l = 3 : Q(zeta_9)^+ ;
           l = 2 : les deux corps quartiques cycliques de conducteur 16), éventuellement après une tordue
           quadratique ramifiée ;
  sc     : le reste, supercuspidal (inertie non abélienne).
Classes : semistable, steinberg_tordu, sp_quadratique, ps_sup, sc.
Usage : python3 local_types_v2.py l k [R]"""
import sys, json, random
from cypari import pari
pari.allocatemem(2 * 10**9)
l, k = int(sys.argv[1]), int(sys.argv[2]); R = int(sys.argv[3]) if len(sys.argv) > 3 else 1
TW = {2: [-1, 2, -2, -5, 10, -10], 3: [3, -3]}[l]
POLS = {3: ["x^3-3*x+1"], 2: ["x^4-4*x^2+2", "x^4+4*x^2+2"]}[l]
pari(f'NFS = [{",".join("nfinit("+p+")" for p in POLS)}];')
pari(f'PRS = vector(#NFS, i, idealprimedec(NFS[i], {l})[1]);')
pari('goodover(a,b,tw) = my(T = concat([1], tw)); for (i = 1, #NFS, for (j = 1, #T, my(d = T[j], '
     'E = ellinit([0,0,0,d^2*a,d^3*b], NFS[i])); if (#E && elllocalred(E, PRS[i])[1] == 0, return(1)))); 0')
pari('ltype(a,b,l,tw) = my(E = ellinit([a,b]), f, j); if (E == [], return(-1)); '
     'f = elllocalred(E, l)[1]; if (f <= 1, return(0)); j = E.j; '
     'if (j != 0 && valuation(j, l) < 0, return(1)); '
     'for (i = 1, #tw, my(d = tw[i], Ed = ellinit([d^2*a, d^3*b])); if (elllocalred(Ed, l)[1] == 0, return(2))); '
     'if (goodover(a, b, tw), return(3)); 4')
lt = pari('ltype'); tw = pari(str(TW))
names = ["semistable", "steinberg_tordu", "sp_quadratique", "ps_sup", "sc"]
rng = random.Random(2); Mk = l ** k; M = l ** (k + 6)
cnt = [0] * 5; undet = 0
for a in range(Mk):
    for b in range(Mk):
        if k >= 6 and a % l**4 == 0 and b % l**6 == 0:
            continue
        t = int(lt(a, b, l, tw)); ok = t >= 0
        for _ in range(R):
            if not ok: break
            if int(lt(a + Mk * rng.randrange(M // Mk), b + Mk * rng.randrange(M // Mk), l, tw)) != t: ok = False
        if ok: cnt[t] += 1
        else: undet += 1
norm = (1 - l ** -10.0) * Mk * Mk
out = dict(l=l, k=k, **{n: c / norm for n, c in zip(names, cnt)}, indetermine=undet / norm)
print(json.dumps(out, indent=1))
json.dump(out, open(sys.path[0] + f"/../results/local_types_v2_l{l}_k{k}.json", "w"), indent=1)
