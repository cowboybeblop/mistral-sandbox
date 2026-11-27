"""Raffinement de local_types_v2.py pour le côté B (relecture_adverse_2.md, objection N2).
Pour chaque cellule (A, B) mod l^k, on calcule le type local (comme v2) et un drapeau « non minimal »
au sens du système de Taylor-Wiles de Chida-Hsieh §6 (Sigma = vide), p = 5 :
  E1 : réduction multiplicative en l avec 5 | v_l(Delta_min)   (rho-barre non ramifiée en l, m_l = 1) ;
  E2 : Steinberg tordu (j non entier) avec 5 | v_l(j)            (rho-barre|I_l scalaire, f de type Steinberg) ;
  E3 : série principale quadratique (tordue de bonne réduction E^d) avec a_l(E^d) = ±(l+1) mod 5
       (congruences possibles avec des formes de type Steinberg tordu au même niveau).
Usage : python3 local_types_v3.py l k [R]"""
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
# renvoie 10*classe + drapeau (drapeau 1 = non minimal), -1 si singulière
pari('ltype3(a,b,l,tw) = my(E = ellinit([a,b]), f, j, vj); if (E == [], return(-1)); '
     'f = elllocalred(E, l)[1]; j = E.j; vj = if (j == 0, 10^6, valuation(j, l)); '
     'if (f == 0, return(0)); '
     'if (f == 1, return(0 + (vj % 5 == 0))); '
     'if (vj < 0, return(10 + (vj % 5 == 0))); '
     'for (i = 1, #tw, my(d = tw[i], Ed = ellinit([d^2*a, d^3*b])); if (elllocalred(Ed, l)[1] == 0, '
     '  my(ap = ellap(Ed, l)); return(20 + ((ap - (l+1)) % 5 == 0 || (ap + (l+1)) % 5 == 0)))); '
     'if (goodover(a, b, tw), return(30)); 40')
lt = pari('ltype3'); tw = pari(str(TW))
names = ["semistable", "steinberg_tordu", "sp_quadratique", "ps_sup", "sc"]
rng = random.Random(2); Mk = l ** k; M = l ** (k + 6)
cnt = {}; undet = 0
for a in range(Mk):
    for b in range(Mk):
        if k >= 6 and a % l**4 == 0 and b % l**6 == 0:
            continue
        t = int(lt(a, b, l, tw)); ok = t >= 0
        for _ in range(R):
            if not ok: break
            if int(lt(a + Mk * rng.randrange(M // Mk), b + Mk * rng.randrange(M // Mk), l, tw)) != t: ok = False
        if ok: cnt[t] = cnt.get(t, 0) + 1
        else: undet += 1
norm = (1 - l ** -10.0) * Mk * Mk
out = dict(l=l, k=k, R=R)
for t, c in sorted(cnt.items()):
    out[names[t // 10] + ("_nonmin" if t % 10 else "")] = c / norm
out["indetermine"] = undet / norm
print(json.dumps(out, indent=1))
json.dump(out, open(sys.path[0] + f"/../results/local_types_v3_l{l}_k{k}.json", "w"), indent=1)
