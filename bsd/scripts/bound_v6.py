"""Chiffrage consolidé (pistes 6, 1, 2, 7, 4 de LISTE_GAINS.md), recalculé de bout en bout.
  borne = base(kappa_base) + SS5 * mu2 * mu3 * P(l>=7) * [19/24 + (7/8 - 19/24) * kappa_ss]
  base(K) = (7/8 K + 19/24 (1-K)) S1new + 3/8 K (4/5/n(5) - S1new)          (comme bound_v3.py)
  P(l>=7) = prod_{l>=7} mesure(Sigma_l) / n(l)                                 (produit exact, et non 1 - eps linéarisé)
  kappa = prod C / 2 + 3/10 prod D (voir bound_v4.py, lit/piste1_equirepartition.md §2).
Options cumulées :
  piste 6 : mu2, mu3 et signes tirés de refine_cells.py (indéterminées ~ 1e-7) ;
  piste 1 : équirépartition (kappa_ss) ;
  piste 2 : additifs en l >= 7, l != ±1 mod 5, sauf E2 et E3 (bound_v5.py) ;
  piste 7 : E1 admis si q != 1 mod 5 (CH §6, cas Sigma non vide, m_q = 1) : en q >= 7 l'exclusion eps ne porte plus que
            sur q = 1 mod 5 ; en 2 et 3, les cellules E1 (semistable_nonmin) sont admises (hors F', donc à 19/24) ;
  piste 4 : kappa de la base recalculé (toutes les courbes, tous types en p > 3, nos signes en 2 et 3).
Scénario optimiste : E2 et E3 admis en 2 et 3 (piste 3, si Diamond 1997b permet de les traiter).
Usage : python3 bound_v6.py refine_l2.json refine_l3.json"""
import json, sys
from mpmath import mp, mpf
from cypari import pari
mp.dps = 20
R = sys.path[0] + "/../results/"
def isp(m): return m > 1 and all(m % d for d in range(2, int(m**.5) + 1))
n = lambda l: 1 - mpf(l) ** -10
PR = [p for p in range(7, 2 * 10**5) if isp(p)]
X0, MMAX = 10**4, 2
_e3 = {}
def e3_frac(l):
    if l >= 300: return mpf(1)
    if l not in _e3:
        tot = bad = 0
        for a in range(l):
            for b in range(l):
                if (4 * a**3 + 27 * b**2) % l == 0: continue
                ap = int(pari.ellap(pari.ellinit([a, b]), l)); tot += 1
                bad += (ap - l - 1) % 5 == 0 or (ap + l + 1) % 5 == 0
        _e3[l] = mpf(bad) / tot
    return _e3[l]
def local(l, p2, p7, allfam=False):
    """mesure de Sigma_l (dans Z_l^2) et mesure de {alpha_l = -1} dans Sigma_l"""
    q = mpf(l); mult = lambda m: (q-1)**2 / q**(m+2)
    excl5 = not allfam and (not p7 or l % 5 == 1)              # exclure I_n avec 5 | n ?
    ms = [m for m in range(1, 300) if not (excl5 and m % 5 == 0)]
    s = 1 - 1/q + sum(mult(m) for m in ms); wm = sum(mult(m) for m in ms if m % 2 == 0)
    if allfam or (p2 and l % 5 not in (1, 4)):
        f3 = 0 if allfam else e3_frac(l)
        adm = [((q-1)/q**3, 2), ((q-1)/q**4, 3), ((q-1)/q**5, 4), ((q-1)/q**8, 8), ((q-1)/q**9, 9), ((q-1)/q**10, 10),
               ((1 - 1/q) / q**5 * (1 - f3), 6)]
        adm += [((q-1)**2 / q**(k+7), 6 + k) for k in range(1, 300) if allfam or k % 5]
        s += sum(m for m, _ in adm); wm += sum(m for m, v in adm if v % 2)
    return s, wm
def big(p2, p7, allfam=False):
    P = mpf(1); poly = [mpf(1)] + [mpf(0)] * MMAX; tail = mpf(1)
    for p in PR:
        if p > 5000:                                           # au-delà : semistable, contribution additive < 1e-8
            s, wm = local(p, False, p7, allfam) if p < 10**5 else (1 - 1/mpf(p)**2, (mpf(p)-1)**2/mpf(p)**4)
        else: s, wm = local(p, p2, p7, allfam)
        P *= s / n(p)
        if p % 4 == 3:
            w = wm / s
            if p < X0: poly = [poly[j] * (1 - w) + (poly[j-1] * w if j else 0) for j in range(MMAX + 1)]
            else: tail *= 1 - w
    return P, tail * sum(poly), tail * sum((-1)**j * c for j, c in enumerate(poly))
kap = lambda C, D: C / 2 + mpf(3) / 10 * D
r2 = json.load(open(R + sys.argv[1])); r3 = json.load(open(R + sys.argv[2]))
def mu(r, scen, e1):
    t = r["types"]
    return mpf(sum(v for k, v in t.items() if k != "indetermine" and (scen == "opt" or not k.endswith("_nonmin")
               or (e1 and k == "semistable_nonmin"))))
def CD(r, scen, e1):
    s = r["signes"]
    if scen == "opt": return mpf(s["opt_p"]) + mpf(s["opt_m"]), mpf(s["opt_p"]) - mpf(s["opt_m"])
    tot = mpf(s["pru_total"]) + (mpf(r["types"].get("semistable_nonmin", 0)) if e1 else 0)
    return (mpf(s["pru_p"]) + mpf(s["pru_m"])) / tot, (mpf(s["pru_p"]) - mpf(s["pru_m"])) / tot
S1new = (mpf(4) / 5 - mpf(8) / 25 / 3124) / n(5); SS5 = mpf(4) / 25 / n(5)
def base(K): return (mpf(7) / 8 * K + mpf(19) / 24 * (1 - K)) * S1new + mpf(3) / 8 * K * (mpf(4) / 5 / n(5) - S1new)
# kappa de la base : toutes les courbes, tous types en p > 3, nos signes en 2 et 3 (optimiste = toutes cellules)
Pall, Ca, Da = big(False, False, allfam=True)
C2, D2 = CD(r2, "opt", False); C3, D3 = CD(r3, "opt", False)
k_full = kap(C2 * C3 * Ca, D2 * D3 * Da)
print(f"kappa (toutes les courbes, tous types) = {float(k_full):.5f}  (BS : 0,5501) ; P(d = -1) maximal = {float((1 + 0.6*D2*D3*Da)/2):.5f}")
steps = [("v3 (78,61 %) recalculé : produit exact, cellules k=8/7", dict(p6=False, p1=False, p2=False, p7=False, p4=False)),
         ("+ piste 6 (cellules indéterminées)", dict(p6=True, p1=False, p2=False, p7=False, p4=False)),
         ("+ piste 1 (équirépartition)", dict(p6=True, p1=True, p2=False, p7=False, p4=False)),
         ("+ piste 2 (additif l >= 7, l != ±1 mod 5)", dict(p6=True, p1=True, p2=True, p7=False, p4=False)),
         ("+ piste 7 (E1 admis si q != 1 mod 5)", dict(p6=True, p1=True, p2=True, p7=True, p4=False)),
         ("+ piste 4 (kappa de la base recalculé)", dict(p6=True, p1=True, p2=True, p7=True, p4=True))]
v3 = {2: json.load(open(R + "local_types_v3_l2_k8.json")), 3: json.load(open(R + "local_types_v3_l3_k7.json"))}
def mu_v3(t): return mpf(sum(v for k, v in t.items() if k not in ("l", "k", "R", "indetermine") and not k.endswith("_nonmin")))
rows = []
cache = {}
for scen in ("pru", "opt"):
    print(f"\n=== scénario {'prudent' if scen == 'pru' else 'optimiste (E2, E3 admis en 2 et 3)'} ===")
    for name, o in steps:
        if o["p6"]: m2, m3 = mu(r2, scen, o["p7"]), mu(r3, scen, o["p7"])
        else: m2, m3 = (mu_v3(v3[2]), mu_v3(v3[3])) if scen == "pru" else (mpf(1), mpf(1))
        key = (o["p2"], o["p7"])
        if key not in cache: cache[key] = big(o["p2"], o["p7"])
        P, Cb, Db = cache[key]
        c2, d2 = CD(r2, scen, o["p7"]); c3, d3 = CD(r3, scen, o["p7"])
        k = kap(c2 * c3 * Cb, d2 * d3 * Db) if o["p1"] else mpf(0)
        g = SS5 * m2 * m3 * P * (mpf(19) / 24 + (mpf(7) / 8 - mpf(19) / 24) * k)
        b = base(k_full if o["p4"] else mpf("0.5501"))
        rows.append(dict(scenario=scen, etape=name, mu2=float(m2), mu3=float(m3), P7=float(P), kappa_ss=float(k), borne=float(b + g)))
        print(f"{name:58s} mu2={float(m2):.5f} mu3={float(m3):.5f} P={float(P):.5f} kappa={float(k):.4f}  borne = {float(b+g)*100:.3f} %")
json.dump(dict(entrees=sys.argv[1:], kappa_base=float(k_full), etapes=rows), open(R + "bound_v6.json", "w"), indent=1, ensure_ascii=False)
