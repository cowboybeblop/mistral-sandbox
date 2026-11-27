"""Vérification finale (autocritique) : le critère « constant sur R relèvements aléatoires » de local_types_v3,
local_signs et refine_cells peut manquer des sous-ensembles rares d'une cellule (constaté pour p = 3 ordinaire).
Méthode indépendante : Monte-Carlo sur (A, B) mod l^40 (hors l^4 | A et l^6 | B), sans cellules.
On estime : mu_l prudent (types non « nonmin »), mu_l avec E1, les classes de signe (opt_±, pru_± avec fermeture
par (A, -B)), et on compare à refine_cells.py. Erreur type affichée.
Usage : python3 mc_check_23.py l n"""
import sys, json, random, math
from cypari import pari
pari.allocatemem(2 * 10**9)
l, n = int(sys.argv[1]), int(sys.argv[2])
TW = {2: [-1, 2, -2, -5, 10, -10], 3: [3, -3]}[l]
POLS = {3: ["x^3-3*x+1"], 2: ["x^4-4*x^2+2", "x^4+4*x^2+2"]}[l]
pari(f'NFS = [{",".join("nfinit("+p+")" for p in POLS)}];')
pari(f'PRS = vector(#NFS, i, idealprimedec(NFS[i], {l})[1]);')
pari('goodover(a,b,tw) = my(T = concat([1], tw)); for (i = 1, #NFS, for (j = 1, #T, my(d = T[j], '
     'E = ellinit([0,0,0,d^2*a,d^3*b], NFS[i])); if (#E && elllocalred(E, PRS[i])[1] == 0, return(1)))); 0')
pari('ltype3(a,b,l,tw) = my(E = ellinit([a,b]), f, j, vj); if (E == [], return(-1)); '
     'f = elllocalred(E, l)[1]; j = E.j; vj = if (j == 0, 10^6, valuation(j, l)); '
     'if (f == 0, return(0)); '
     'if (f == 1, return(0 + (vj % 5 == 0))); '
     'if (vj < 0, return(10 + (vj % 5 == 0))); '
     'for (i = 1, #tw, my(d = tw[i], Ed = ellinit([d^2*a, d^3*b])); if (elllocalred(Ed, l)[1] == 0, '
     '  my(ap = ellap(Ed, l)); return(20 + ((ap - (l+1)) % 5 == 0 || (ap + (l+1)) % 5 == 0)))); '
     'if (goodover(a, b, tw), return(30)); 40')
pari('sgn3(a,b,l) = my(D = -4*a^3 - 27*b^2, v, d); v = valuation(D, l); '
     'd = ellrootno(ellinit([a,b]), l) * ellrootno(ellinit([a,-b]), l); '
     'if (l == 2, d * if ((D / 2^v) % 4 == 1, 1, -1), d * (-1)^v)')
lt = pari('ltype3'); sg = pari('sgn3'); tw = pari(str(TW))
rng = random.Random(17); M = l**40; c = dict(mu_pru=0, e1=0, opt_p=0, opt_m=0, pru_p=0, pru_m=0, pru_not_closed=0)
done = 0
while done < n:
    a, b = rng.randrange(M), rng.randrange(M)
    if (a % l**4 == 0 and b % l**6 == 0) or 4 * a**3 + 27 * b**2 == 0: continue
    t = int(lt(a, b, l, tw)); beta = int(sg(a, b, l)); done += 1
    c["opt_p" if beta == 1 else "opt_m"] += 1
    if t == 1: c["e1"] += 1
    if t % 10 == 0:
        c["mu_pru"] += 1
        if int(lt(a, -b, l, tw)) % 10: c["pru_not_closed"] += 1
        else: c["pru_p" if beta == 1 else "pru_m"] += 1
ref = json.load(open(sys.path[0] + f"/../results/refine_l{l}_" + {2: "k8_18", 3: "k5_11"}[l] + ".json"))
t, s = ref["types"], ref["signes"]
refv = dict(mu_pru=sum(v for k, v in t.items() if k != "indetermine" and not k.endswith("_nonmin")),
            e1=t.get("semistable_nonmin", 0), **{k: s[k] for k in ("opt_p", "opt_m", "pru_p", "pru_m", "pru_not_closed")})
out = {}
for k, v in c.items():
    p = v / n; se = math.sqrt(p * (1 - p) / n); out[k] = dict(mc=p, se=se, cellules=refv[k], ecart_en_se=(p - refv[k]) / se if se else None)
    print(f"{k:16s} MC = {p:.5f} ± {se:.5f}   cellules = {refv[k]:.5f}   écart = {(p - refv[k]) / se if se else 0:+.1f} σ")
json.dump(dict(l=l, n=n, resultats=out), open(sys.path[0] + f"/../results/mc_check_l{l}.json", "w"), indent=1)
