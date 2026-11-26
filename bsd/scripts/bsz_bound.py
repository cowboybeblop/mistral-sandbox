"""Borne inférieure à la BSZ sur la proportion de courbes (classées par hauteur) vérifiant la partie
« rang » de BSD, avec les théorèmes réciproques actuels. Reproduit d'abord BSZ (Cor. 26) à l'identique.

Notations (BSZ §3) : mu = densité ; kappa = 0,5501 (Théorème 16) ; Théorème 25 : 7/8 si les signes
sont équirépartis, 19/24 sinon ; Théorème 21 : 3/8 pour le rang 0 seul.

Familles nouvelles (p = 5) :
  S1new = bonne ordinaire en 5  U  multiplicative en 5, sauf (déployée et 5 | ord_5 Delta).
     Rang 0 : BSZ Thm 5 (inchangé). Rang 1 : bonne ordinaire, BSTW Thm 12.3 ; multiplicative,
     Castella 2409.01360 Thm 1.1 (E(Q_5)[5] = 0 vérifié : non déployée, toujours ; déployée, si 5 ne divise pas k).
     Défini par des congruences en 5 seulement, donc le Théorème 16 s'applique (5 = 1 mod 4).
  SS5ss = supersingulière en 5 (5 | A, 5 ne divise pas B) et semistable partout.
     Rang 0 : BSTW Thm 1.6. Rang 1 : BSTW Thm 12.3 (a_5 = 0, N sans facteur carré).
     Conditions en 2 et 3 : Théorème 16 inapplicable, donc 19/24 (Théorème 25, première partie).
Densités locales en 2 et 3 : scripts/local_densities.py (calcul exact par cellules, algorithme de Tate)."""
from fractions import Fraction as F
import json, sys
from mpmath import mp, zeta, mpf

mp.dps = 30
KAPPA = mpf("0.5501")
norm = lambda l: 1 - mpf(l) ** -10

# ---------- 1. Reproduction de BSZ, Corollaire 26 ----------
mu_S0 = mpf(4) / 5 / norm(5)                                   # Lemme 17
mu_S1p = (mpf(99) / 125 - mpf(19) / 125 * 4 / (5**5 - 1)) / norm(5)   # Lemme 18
bsz = (mpf(7) / 8 * KAPPA + mpf(19) / 24 * (1 - KAPPA)) * mu_S1p \
      - (mpf(7) / 8 + mpf(19) / 24) * mpf("0.00001") + mpf("0.00169")
print("BSZ reproduit :", mu_S1p, bsz)                          # attendu .7918054..., .664816...

# ---------- 2. Nouvelle famille S1new ----------
split_5k = mpf(8) / 25 / 3124          # mesure des déployées avec 5 | k (somme_{5|k} 8/5^(k+2))
mu_S1new = (mpf(4) / 5 - split_5k) / norm(5)
main = (mpf(7) / 8 * KAPPA + mpf(19) / 24 * (1 - KAPPA)) * mu_S1new
left0 = mpf(3) / 8 * KAPPA * (mu_S0 - mu_S1new)                # reste de S0 : rang 0 seul (Cor. 22)

# ---------- 3. Supersingulière en 5 et semistable ----------
d2 = json.load(open(sys.path[0] + "/../results/local_density_l2_k10.json"))
d3 = json.load(open(sys.path[0] + "/../results/local_density_l3_k5.json"))
mu2_ss = mpf(d2["semistable"])                                 # = 3/1023, 0 cellule indéterminée
mu3_ss = mpf(d3["semistable"])                                 # borne inférieure (cellules déterminées)
P_ge7 = zeta(10) / zeta(2)
for l in (2, 3, 5):
    P_ge7 /= (1 - mpf(l) ** -2) / norm(l)
mu5_ss5 = mpf(4) / 25 / norm(5)
mu_SS5ss = mu5_ss5 * mu2_ss * mu3_ss * P_ge7
gain_ss = mpf(19) / 24 * mu_SS5ss

total = main + left0 + gain_ss
out = dict(bsz_reproduit=float(bsz), mu_S1p=float(mu_S1p), mu_S1new=float(mu_S1new),
           part_principale=float(main), reste_rang0=float(left0), mu2_ss=float(mu2_ss), mu3_ss=float(mu3_ss),
           produit_l_ge_7=float(P_ge7), mu_SS5ss=float(mu_SS5ss), gain_supersingulier=float(gain_ss),
           gain_castella=float(main - (mpf(7) / 8 * KAPPA + mpf(19) / 24 * (1 - KAPPA)) * mu_S1p),
           borne_totale=float(total))
print(json.dumps(out, indent=1))
json.dump(out, open(sys.path[0] + "/../results/bsz_bound.json", "w"), indent=1)
