"""Piste 6 (LISTE_GAINS.md) : résoudre les cellules indéterminées en 2 et 3 par raffinement adaptatif.
On part des cellules (A, B) mod l^k0. Une cellule est « résolue » si son type local (local_types_v3.py, drapeau non
minimal compris), ses signes (local_signs.py : d_l et Delta'_2 mod 4 ou 3^v mod 4) et le type de sa tordue
(A, -B) sont constants sur R relèvements aléatoires mod l^(k+6). Sinon on la découpe en l^2 sous-cellules mod l^(k+1),
jusqu'à k = kmax. Région non minimale (l^4 | A et l^6 | B) exclue, normalisation 1 - l^-10 (BSZ §3.1).
Sortie : mesures par type (comme local_types_v3) et par classe de signe (comme local_signs).
Usage : python3 refine_cells.py l k0 kmax [R]"""
import sys, json, random
from cypari import pari
pari.allocatemem(2 * 10**9)
l, k0, kmax = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]); R = int(sys.argv[4]) if len(sys.argv) > 4 else 3
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
pari('sgn3(a,b,l) = my(D = -4*a^3 - 27*b^2, v, d); if (D == 0, return(0)); v = valuation(D, l); '
     'd = ellrootno(ellinit([a,b]), l) * ellrootno(ellinit([a,-b]), l); '
     'if (l == 2, [d, (D / 2^v) % 4], [d, (3^v) % 4])')
lt = pari('ltype3'); sg = pari('sgn3'); tw = pari(str(TW))
rng = random.Random(5)
names = ["semistable", "steinberg_tordu", "sp_quadratique", "ps_sup", "sc"]
def info(a, b):
    t = int(lt(a, b, l, tw))
    if t < 0: return None
    s = sg(a, b, l); return (t, int(s[0]), int(s[1]))
def classify(a, b, k):
    Mk = l**k; M = l**(k + 6)
    base = [info(a, b), info(a, -b)]
    ok = [base[0] is not None, base[0] is not None, base[1] is not None]   # type, signes, type de la tordue
    for _ in range(R):
        if not any(ok): break
        da, db = Mk * rng.randrange(M // Mk), Mk * rng.randrange(M // Mk)
        x, y = info(a + da, b + db), info(a + da, -(b + db))
        if x is None or base[0] is None or x[0] != base[0][0]: ok[0] = False
        if x is None or base[0] is None or x[1:] != base[0][1:]: ok[1] = False
        if y is None or base[1] is None or y[0] != base[1][0]: ok[2] = False
    return base, ok
out = {}; sig = dict(opt_p=0, opt_m=0, opt_undet=0, pru_p=0, pru_m=0, pru_total=0, pru_not_closed=0, pru_undet=0)
def add(d, key, w): d[key] = d.get(key, 0) + w
cells = [(a, b, k0) for a in range(l**k0) for b in range(l**k0)]
ncells = 0
while cells:
    a, b, k = cells.pop(); ncells += 1
    if k >= 6 and a % l**4 == 0 and b % l**6 == 0: continue
    (x, y), ok = classify(a, b, k)
    if not all(ok) and k < kmax:
        cells += [(a + l**k * i, b + l**k * j, k + 1) for i in range(l) for j in range(l)]; continue
    w = 1.0 / l**(2 * k) / (1 - l**-10.0)
    if ok[0]: add(out, names[x[0] // 10] + ("_nonmin" if x[0] % 10 else ""), w)
    else: add(out, "indetermine", w)
    if ok[1]:
        add(sig, "opt_p" if x[1] * (1 if x[2] == 1 else -1) == 1 else "opt_m", w)
    else: add(sig, "opt_undet", w)
    if ok[0] and x[0] % 10 == 0:
        sig["pru_total"] += w
        if not (ok[2] and y[0] % 10 == 0): sig["pru_not_closed"] += w
        elif not ok[1]: sig["pru_undet"] += w
        else: add(sig, "pru_p" if x[1] * (1 if x[2] == 1 else -1) == 1 else "pru_m", w)
res = dict(l=l, k0=k0, kmax=kmax, R=R, cellules_examinees=ncells, types=out, signes=sig)
print(json.dumps(res, indent=1))
json.dump(res, open(sys.path[0] + f"/../results/refine_l{l}_k{k0}_{kmax}.json", "w"), indent=1)
