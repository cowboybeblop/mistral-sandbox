"""Plan 85 % : carte des plafonds. Quelle borne obtient-on si l'on suppose tel ou tel ingrédient ?
Borne de type BSZ pour une famille F où la proportion de signes +1 vaut rho (si connue), avec la moyenne
de Sel_p égale à p + 1 :  minimisation linéaire de x0 + x1 sous
   x0 + p^2 (rho - x0) + p x1 + p^3 (1 - rho - x1) <= p + 1,  0 <= x0 <= rho, 0 <= x1 <= 1 - rho
(rho inconnu : minimum sur rho, ce qui redonne (p^2 - p - 1)/(p^2 - 1) ; rho = 1/2 redonne (2p - 3)/(2p - 2)).
Régions de la famille de toutes les courbes :
  R5 = bonne ordinaire, multiplicative ou supersingulière en 5 (réciproques en p = 5) : 1 - 1/25 ;
  U  = additive en 5 : 1/25 (normalisations n(5) négligées) ;
  en p = 3 : 4/9 des courbes (bonne supersingulière, a_3 = 0) ; en p = 7 : 1 - 1/49 (si la moyenne de Sel_7 était 8).
Usage : python3 plafonds.py"""
from fractions import Fraction as Fr
def best(p, rho):
    """borne inférieure exacte de x0 + x1 (programme linéaire à 2 variables, sommets)"""
    p = Fr(p); rho = Fr(rho); cands = []
    for x0 in (Fr(0), rho):
        # x1 minimal compatible : (p^3 - p) x1 >= p^2 rho + p^3 (1-rho) - (p+1) - (p^2 - 1) x0
        need = (p**2 * rho + p**3 * (1 - rho) - (p + 1) - (p**2 - 1) * x0) / (p**3 - p)
        x1 = max(Fr(0), need)
        if x1 <= 1 - rho: cands.append(x0 + x1)
    for x1 in (Fr(0), 1 - rho):
        need = (p**2 * rho + p**3 * (1 - rho) - (p + 1) - (p**3 - p) * x1) / (p**2 - 1)
        x0 = max(Fr(0), need)
        if x0 <= rho: cands.append(x0 + x1)
    return min(cands)
def unknown(p): return min(best(p, Fr(k, 200)) for k in range(201))
for p in (3, 5, 7):
    print(f"p = {p} : signe inconnu {float(unknown(p)):.4f} ; signes équirépartis {float(best(p, Fr(1,2))):.4f} ; "
          f"tous de signe -1 {float(best(p, 0)):.4f}")
k = 0.5587
def f(p, kap): return kap * best(p, Fr(1, 2)) + (1 - kap) * unknown(p)
R5, U, P3 = 1 - Fr(1, 25), Fr(1, 25), Fr(4, 9)
rows = [
 ("Aujourd'hui (prudent, bound_v6)", None, 0.7981),
 ("p = 5 parfait (aucune exclusion, N6 réglé), kappa = 0,5587", float(R5) * float(f(5, k)), None),
 ("+ p = 3 sur U (supersingulier a_3 = 0)", float(R5) * float(f(5, k)) + float(U * P3) * float(f(3, k)), None),
 ("p = 5 parfait, kappa = 1 (conjecture mu_equi = mu de BSZ)", float(R5) * float(best(5, Fr(1,2))), None),
 ("  + p = 3 sur U, kappa = 1", float(R5) * float(best(5, Fr(1,2))) + float(U * P3) * float(best(3, Fr(1,2))), None),
 ("Si moyenne Sel_7 = 8 (ouvert), kappa = 0,5587, p = 7 seul", float(1 - Fr(1,49)) * float(f(7, k)), None),
 ("Si moyenne Sel_7 = 8 et kappa = 1", float(1 - Fr(1,49)) * float(best(7, Fr(1,2))), None),
]
for name, v, fixed in rows:
    print(f"{name:62s} {100 * (fixed if fixed else v):.2f} %")
# kappa nécessaire pour 85 % avec p = 5 parfait + p = 3 sur U
for kap in [x / 1000 for x in range(500, 1001)]:
    if float(R5) * float(f(5, kap)) + float(U * P3) * float(f(3, kap)) >= 0.85:
        print(f"kappa minimal pour 85 % (p = 5 parfait + p = 3 sur U) : {kap:.3f}"); break
else: print("85 % inaccessible même avec kappa = 1 (p = 5 parfait + p = 3 sur U)")
