"""Plan 85 %, E4 : que gagnerait-on avec des moments supérieurs de #Sel_p ?
Programme linéaire : minimiser P(rang de Selmer s <= 1) sur les lois de s (s = 0..S) sous
   E[p^(j s)] <= M_j = prod_{i=1..j} (p^i + 1)   pour j = 1..m   (valeurs de Poonen-Rains ; j = 1 démontré pour
   p <= 5 [BS], j = 2 majoré par 15 pour p = 2 [BSS, arXiv 2110.09063], le reste ouvert),
avec parité inconnue, ou P(s pair) = 1/2 (signes équirépartis).
Usage : python3 moments_lp.py"""
import numpy as np
from scipy.optimize import linprog
S = 6   # rangs de Selmer au-delà de 6 : coût énorme dans les moments, sans effet (vérifié avec S = 8 pour p = 2, 3)
def lp(p, m, equi):
    c = np.array([1.0 if s <= 1 else 0.0 for s in range(S + 1)])
    A = [[float(p) ** (j * s) for s in range(S + 1)] for j in range(1, m + 1)]
    b = [float(np.prod([p**i + 1 for i in range(1, j + 1)])) for j in range(1, m + 1)]
    Aeq = [[1.0] * (S + 1)]; beq = [1.0]
    if equi: Aeq.append([1.0 if s % 2 == 0 else 0.0 for s in range(S + 1)]); beq.append(0.5)
    # mise à l'échelle des lignes pour la stabilité numérique
    A = [[x / bj for x in row] for row, bj in zip(A, b)]; b = [1.0] * m
    r = linprog(c, A_ub=A, b_ub=b, A_eq=Aeq, b_eq=beq, bounds=[(0, 1)] * (S + 1), method="highs")
    return r.fun, {s: round(v, 4) for s, v in enumerate(r.x) if v > 1e-6}
for p in (2, 3, 5, 7):
    for equi in (False, True):
        out = []
        for m in (1, 2, 3, 4):
            v, sup = lp(p, m, equi); out.append(f"m={m}: {v:.4f}")
        print(f"p={p} {'équirépartis' if equi else 'parité inconnue':16s} " + "  ".join(out) + f"   (loi extrémale m=4 : {sup})")
