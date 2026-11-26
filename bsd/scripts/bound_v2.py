"""Premier chiffrage de la borne BSZ avec A et B (supposés validés) et le raccord (raccord_A_B.md).
Formule identique à gain_table.py (branche claude/artifact-review-prompt-pfjqwc) :
  borne = base + (19/24) * SS5 * mu2 * mu3 * P7 * (1 - eps),
où mu_l = densité des types admis en l (local_types_v2), P7 = semistable en l >= 7,
eps = exclusion des premiers multiplicatifs q >= 7 avec 5 | v_q(Delta) (niveau non minimal), approx.
Scénarios : S_A (supercuspidal + semistable), S_A+SP (+ séries principales ramifiées), référence (tous types)."""
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
def mu(t, kinds): return mpf(sum(t[x] for x in kinds))
scen = [("S_A : semistable + supercuspidal", ["semistable", "sc"]),
        ("S_A+SP : + séries principales ramifiées", ["semistable", "sc", "sp_quadratique", "ps_sup"]),
        ("S_rep : réparation uniforme (+ Steinberg tordu)", ["semistable", "sc", "sp_quadratique", "ps_sup", "steinberg_tordu"]),
        ("référence : tous types (table d'origine)", None)]
rows = []
for name, kinds in scen:
    m2 = mpf(1) if kinds is None else mu(t2, kinds); m3 = mpf(1) if kinds is None else mu(t3, kinds)
    e = 0 if kinds is None else eps
    g = mpf(19) / 24 * SS5 * m2 * m3 * P7 * (1 - e)
    rows.append(dict(scenario=name, mu2=float(m2), mu3=float(m3), eps=float(e), gain=float(g), borne=float(base + g)))
    print(f"{name:45s} mu2={float(m2):.4f} mu3={float(m3):.4f}  borne = {float(base+g)*100:.3f} %")
print("base (sans la famille supersinguliere) =", float(base), " eps =", float(eps))
json.dump(rows, open(R + "bound_v2.json", "w"), indent=1, ensure_ascii=False)
