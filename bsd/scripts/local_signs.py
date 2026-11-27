"""Piste 1 (LISTE_GAINS.md) : signes locaux en l = 2, 3 pour l'équirépartition des signes (BSZ Th. 16, BS §5).
Reformulation locale de Bhargava-Shankar (arXiv 1312.7859, §5) : pour E = E_{A,B}, avec d(E) = r(E) r(E_{-1}),
   d(E) = beta_2(E) * beta_3(E) * sgn(Delta) * prod_{p > 3, p = 3 mod 4} alpha_p(E),
   beta_2 = r_2(E) r_2(E_{-1}) * chi_4(Delta'_2),   beta_3 = r_3(E) r_3(E_{-1}) * (-1)^{v_3(Delta)},
   alpha_p = d_p(E) (-1)^{v_p(Delta)} (BS (31)),   Delta = -4A^3 - 27B^2.
Pour chaque cellule (A, B) mod l^k on calcule : le type local et le drapeau « non minimal » (comme local_types_v3.py),
beta_l, et on teste la constance sur R relèvements aléatoires. Twist par -1 : (A, B) -> (A, -B).
Sortie : mesures (normalisées par 1 - l^-10) des classes
   opt_{+,-}      : cellules à beta déterminé (scénario optimiste : tous types admis) ;
   pru_{+,-}      : cellules du scénario prudent (type déterminé, non « nonmin ») dont la tordue par -1 est aussi
                    dans le scénario prudent, et beta déterminé ;
   pru_total      : mesure de toute la famille prudente (doit redonner mu_l de bound_v3) ;
   table          : distribution de (Delta'_2 mod 4, d_2) [l = 2] ou (3^{v_3} mod 4, d_3) [l = 3], pour comparer aux
                    tables 3 et 4 de BS.
Usage : python3 local_signs.py l k [R]"""
import sys, json, random
from cypari import pari
pari.allocatemem(2 * 10**9)
l, k = int(sys.argv[1]), int(sys.argv[2]); R = int(sys.argv[3]) if len(sys.argv) > 3 else 2
TW = {2: [-1, 2, -2, -5, 10, -10], 3: [3, -3]}[l]
POLS = {3: ["x^3-3*x+1"], 2: ["x^4-4*x^2+2", "x^4+4*x^2+2"]}[l]
pari(f'NFS = [{",".join("nfinit("+p+")" for p in POLS)}];')
pari(f'PRS = vector(#NFS, i, idealprimedec(NFS[i], {l})[1]);')
pari('goodover(a,b,tw) = my(T = concat([1], tw)); for (i = 1, #NFS, for (j = 1, #T, my(d = T[j], '
     'E = ellinit([0,0,0,d^2*a,d^3*b], NFS[i])); if (#E && elllocalred(E, PRS[i])[1] == 0, return(1)))); 0')
# identique à local_types_v3.py
pari('ltype3(a,b,l,tw) = my(E = ellinit([a,b]), f, j, vj); if (E == [], return(-1)); '
     'f = elllocalred(E, l)[1]; j = E.j; vj = if (j == 0, 10^6, valuation(j, l)); '
     'if (f == 0, return(0)); '
     'if (f == 1, return(0 + (vj % 5 == 0))); '
     'if (vj < 0, return(10 + (vj % 5 == 0))); '
     'for (i = 1, #tw, my(d = tw[i], Ed = ellinit([d^2*a, d^3*b])); if (elllocalred(Ed, l)[1] == 0, '
     '  my(ap = ellap(Ed, l)); return(20 + ((ap - (l+1)) % 5 == 0 || (ap + (l+1)) % 5 == 0)))); '
     'if (goodover(a, b, tw), return(30)); 40')
# code = 4*dl_index + 2*table_index ... : renvoie [d_l, m] avec m = Delta'_2 mod 4 (l=2) ou 3^v mod 4 (l=3) ; 0 si singulière
pari('sgn3(a,b,l) = my(D = -4*a^3 - 27*b^2, v, d); if (D == 0, return(0)); v = valuation(D, l); '
     'd = ellrootno(ellinit([a,b]), l) * ellrootno(ellinit([a,-b]), l); '
     'if (l == 2, [d, (D / 2^v) % 4], [d, (3^v) % 4])')
lt = pari('ltype3'); sg = pari('sgn3'); tw = pari(str(TW))
rng = random.Random(7); Mk = l ** k; M = l ** (k + 6)
def info(a, b):
    t = int(lt(a, b, l, tw))
    if t < 0: return None
    s = sg(a, b, l); return t, int(s[0]), int(s[1])
cell = {}
for a in range(Mk):
    for b in range(Mk):
        if k >= 6 and a % l**4 == 0 and b % l**6 == 0:
            continue
        x = info(a, b); tdet = sdet = x is not None
        for _ in range(R):
            if not (tdet or sdet): break
            y = info(a + Mk * rng.randrange(M // Mk), b + Mk * rng.randrange(M // Mk))
            if y is None or y[0] != x[0]: tdet = False
            if y is None or y[1:] != x[1:]: sdet = False
        cell[(a, b)] = (x, tdet, sdet)
norm = (1 - l ** -10.0) * Mk * Mk
def prudent(c):
    x, tdet, _ = cell.get(c, (None, False, False))
    return x is not None and tdet and x[0] % 10 == 0
out = dict(l=l, k=k, R=R, opt_p=0, opt_m=0, opt_undet=0, pru_p=0, pru_m=0, pru_total=0, pru_not_closed=0,
           pru_undet=0, sym_violations=0)
table = {}
for (a, b), (x, tdet, sdet) in cell.items():
    if x is not None and sdet:
        beta = x[1] * (1 if x[2] == 1 else -1)
        out["opt_p" if beta == 1 else "opt_m"] += 1
        key = f"({x[2]},{x[1]})"; table[key] = table.get(key, 0) + 1
        y = cell.get((a, (-b) % Mk))
        if y and y[2] and y[0][1:] != x[1:]: out["sym_violations"] += 1
    else:
        out["opt_undet"] += 1
    if prudent((a, b)):
        out["pru_total"] += 1
        if not prudent((a, (-b) % Mk)): out["pru_not_closed"] += 1
        elif not sdet: out["pru_undet"] += 1
        else: out["pru_p" if beta == 1 else "pru_m"] += 1
for key in list(out):
    if key not in ("l", "k", "R", "sym_violations"): out[key] /= norm
out["table"] = {key: v / norm for key, v in sorted(table.items())}
print(json.dumps(out, indent=1))
json.dump(out, open(sys.path[0] + f"/../results/local_signs_l{l}_k{k}.json", "w"), indent=1)
