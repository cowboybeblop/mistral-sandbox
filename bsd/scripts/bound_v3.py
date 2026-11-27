"""Chiffrage du 27/11 (relecture_adverse_2.md, N2 et N9).
Même formule que bound_v2.py / gain_table.py :  borne = base + (19/24) * SS5 * mu2 * mu3 * P7 * (1 - eps).
Côté A (Prop. R', reverification_27_11.md §4) : tous les types locaux en 2 et 3 sont admis.
Côté B (N2) : on exclut en l = 2, 3 les cellules « non minimales » E1, E2, E3 et les cellules indéterminées.
Scénarios :
  S3_prudent  : exclusions E1-E3 + indéterminées en 2 et 3, eps (q >= 7) ;
  S3_optimiste: aucune exclusion en 2 et 3 (suppose CH Sigma != vide via [Dia97b] et invariance par torsion), eps ;
  référence   : table d'origine (tous types, eps = 0).
Usage : python3 bound_v3.py local_types_v3_l2_k10.json local_types_v3_l3_k7.json"""
import json, sys
from mpmath import mp, mpf, zeta
mp.dps = 20
R = sys.path[0] + "/../results/"
K = mpf("0.5501"); n = lambda l: 1 - mpf(l) ** -10
fac = mpf(7) / 8 * K + mpf(19) / 24 * (1 - K)
S1new = (mpf(4) / 5 - mpf(8) / 25 / 3124) / n(5); SS5 = mpf(4) / 25 / n(5)
base = fac * S1new + mpf(3) / 8 * K * (mpf(4) / 5 / n(5) - S1new)
P7 = zeta(10) / zeta(2)
for l in (2, 3, 5): P7 /= (1 - mpf(l) ** -2) / n(l)
def isp(m): return m > 1 and all(m % d for d in range(2, int(m**.5) + 1))
eps = sum(sum(mpf(q - 1)**2 / mpf(q)**(m + 2) for m in range(5, 80, 5)) / ((1 - mpf(q)**-2) / n(q))
          for q in range(7, 3000) if isp(q))
t2 = json.load(open(R + sys.argv[1])); t3 = json.load(open(R + sys.argv[2]))
def mu_prudent(t): return mpf(sum(v for k, v in t.items() if k not in ("l", "k", "R", "indetermine") and not k.endswith("_nonmin")))
rows = []
for name, m2, m3, e in [("S3_prudent : A tous types ; B sans E1-E3 ni indéterminées", mu_prudent(t2), mu_prudent(t3), eps),
                        ("S3_optimiste : A et B tous types", mpf(1), mpf(1), eps),
                        ("référence : tous types, eps = 0 (table d'origine)", mpf(1), mpf(1), mpf(0))]:
    g = mpf(19) / 24 * SS5 * m2 * m3 * P7 * (1 - e)
    rows.append(dict(scenario=name, mu2=float(m2), mu3=float(m3), eps=float(e), gain=float(g), borne=float(base + g)))
    print(f"{name:60s} mu2={float(m2):.5f} mu3={float(m3):.5f}  borne = {float(base+g)*100:.3f} %")
print("base =", float(base), " eps =", float(eps))
json.dump(rows, open(R + "bound_v3.json", "w"), indent=1, ensure_ascii=False)
