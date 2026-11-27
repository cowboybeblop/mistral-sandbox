"""Relecture adverse (piste 1 et piste 4) : test global de kappa, indépendant de toute la machinerie locale.
On tire (A, B) uniformément dans la boîte de hauteur max(4|A|^3, 27 B^2) <= X (modèles réduits : pas de p^4 | A et
p^6 | B pour p <= 50), et on calcule d(E) = r(E) r(E_{-1}) avec le signe GLOBAL de PARI (ellrootno(E)).
  - famille « toutes » : P(d = -1) doit valoir kappa = 0,5587 (bound_v6) et non 0,5501 (tables de BS) ;
  - famille « ss » (5 | A, 5 ne divise pas B, semistable en l >= 7, sans multiplicatif avec 5 | v_l en l >= 7, tous
    types en 2 et 3) : P(d = -1) doit valoir kappa_ss optimiste = 0,5585 (bound_v4).
Usage : python3 attack_kappa_global.py famille n Amax"""
import sys, random, math
from cypari import pari
pari.allocatemem(10**9)
fam, n, Amax = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
Bmax = int(math.sqrt(4 * Amax**3 / 27)); rng = random.Random(31)
SMALL = [p for p in range(2, 50) if all(p % d for d in range(2, p))]
def ok_ss(A, B, D):
    if A % 5 or B % 5 == 0: return False
    for p in pari.factor(abs(D))[0]:
        p = int(p)
        if p < 7: continue
        if A % p == 0 and B % p == 0: return False               # additif en p >= 7 (modèle minimal)
        if int(pari.valuation(D, p)) % 5 == 0: return False        # multiplicatif avec 5 | v_p
    return True
done = m = 0
while done < n:
    A = rng.randint(-Amax, Amax); B = rng.randint(-Bmax, Bmax)
    if fam == "ss": A = 5 * (A // 5)
    if max(4 * abs(A)**3, 27 * B * B) > 4 * Amax**3: continue
    D = -4 * A**3 - 27 * B**2
    if D == 0 or any(A % p**4 == 0 and B % p**6 == 0 for p in SMALL): continue
    if fam == "ss" and not ok_ss(A, B, D): continue
    d = int(pari.ellrootno(pari.ellinit([A, B]))) * int(pari.ellrootno(pari.ellinit([A, -B])))
    m += d == -1; done += 1
p = m / n; se = math.sqrt(p * (1 - p) / n)
pred = {"toutes": (0.55872, 0.5501), "ss": (0.55850, None)}[fam]
print(f"famille {fam}, n = {n}, |A| <= {Amax} : P(d = -1) = {p:.4f} ± {se:.4f} ; prévu {pred[0]} "
      f"(écart {(p - pred[0]) / se:+.1f} σ)" + (f" ; valeur BS {pred[1]} : écart {(p - pred[1]) / se:+.1f} σ" if pred[1] else ""))
