"""B1 : gain sur la borne BSZ selon l'ensemble S des premiers où les réciproques supersinguliers
en p = 5 exigeraient la semistabilité. Familles : S1new (fixe, Théorème 16 applicable) + SS5 ∩ {semistable en S}.
Si S est vide, SS5 n'impose de conditions qu'en 5 : Théorème 16 applicable (facteur 0,8375), sinon 19/24.
Densités locales : results/local_density_l2_k10.json, l3_k5 ; l >= 7 : (1 - l^-2)/(1 - l^-10)."""
import json, sys
from mpmath import mp, mpf, zeta
mp.dps = 20
K = mpf("0.5501"); n = lambda l: 1 - mpf(l) ** -10
fac = mpf(7) / 8 * K + mpf(19) / 24 * (1 - K)
S1new = (mpf(4) / 5 - mpf(8) / 25 / 3124) / n(5); SS5 = mpf(4) / 25 / n(5)
base = fac * S1new + mpf(3) / 8 * K * (mpf(4) / 5 / n(5) - S1new)
mu2 = mpf(json.load(open(sys.path[0] + "/../results/local_density_l2_k10.json"))["semistable"])
mu3 = mpf(json.load(open(sys.path[0] + "/../results/local_density_l3_k5.json"))["semistable"])
P7 = zeta(10) / zeta(2)
for l in (2, 3, 5): P7 /= (1 - mpf(l) ** -2) / n(l)
cases = [("semistable partout (situation actuelle)", mu2 * mu3 * P7, False),
         ("semistable hors de 2", mu3 * P7, False),
         ("semistable hors de 2 et 3", P7, False),
         ("semistable en 2 seulement", mu2, False),
         ("aucune condition sur le conducteur", mpf(1), True)]
rows = []
for name, frac, thm16 in cases:
    g = (fac if thm16 else mpf(19) / 24) * SS5 * frac
    rows.append(dict(cas=name, densite_famille_ss=float(SS5 * frac), gain=float(g), borne=float(base + g)))
    print(f"{name:45s} densité {float(SS5*frac):.5f}  gain {float(g):.4f}  borne {float(base+g):.4f}")
json.dump(rows, open(sys.path[0] + "/../results/gain_table.json", "w"), indent=1, ensure_ascii=False)
