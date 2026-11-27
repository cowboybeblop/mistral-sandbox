"""Pistes 1 et 2 (LISTE_GAINS.md). Piste 2 : réduction additive en l >= 7.
Densités locales exactes en l >= 5 (modèle E_{A,B}, minimal sauf l^4 | A et l^6 | B), mesure dans Z_l^2 :
  bonne 1 - 1/l ; I_n : (l-1)^2/l^(n+2) ; II : (l-1)/l^3 ; III : (l-1)/l^4 ; IV : (l-1)/l^5 ;
  I0* : (1-1/l)/l^5 ; I_n* : (l-1)^2/l^(n+7) ; IV* : (l-1)/l^8 ; III* : (l-1)/l^9 ; II* : (l-1)/l^10  (total 1 - l^-10).
  (A = l^2 a, B = l^3 b avec v(A) >= 2, v(B) >= 3 : tordue par l de E_{a,b}.)  v_l(Delta) : II 2, III 3, IV 4,
  I0* 6, I_n* 6+n, IV* 8, III* 9, II* 10.
Admission côté B (Lemme types23 de NEW_RESULTS_EN étendu aux l avec 5 ne divisant pas l^2 - 1, i.e. l != ±1 mod 5) :
  prudent   : l != ±1 mod 5 : tous les types additifs sauf (E2) I_n* avec 5 | n et (E3) I0* avec a_l(E') = ±(l+1) mod 5
              (E' = E_{a,b} de bonne réduction ; fraction calculée exactement pour l < 300, I0* exclus au-delà) ;
              l = ±1 mod 5 : aucun additif ;
  maximal   : tous les additifs, tout l >= 7.
Signes (piste 1) : en l = 3 mod 4, alpha_l = (-1)^{v_l(Delta)} pour un additif, -1 pour I_n avec n pair.
Usage : python3 bound_v5.py signs_l2.json signs_l3.json"""
import json, sys
from mpmath import mp, mpf
from cypari import pari
mp.dps = 20
R = sys.path[0] + "/../results/"
def isp(m): return m > 1 and all(m % d for d in range(2, int(m**.5) + 1))
n = lambda l: 1 - mpf(l) ** -10
PR = [p for p in range(7, 2 * 10**5) if isp(p)]
X0, MMAX = 10**4, 2
def e3_frac(l):
    """fraction des (a, b) mod l de bonne réduction avec a_l = ±(l+1) mod 5"""
    if l >= 300: return mpf(1)
    tot = bad = 0
    for a in range(l):
        for b in range(l):
            if (4 * a**3 + 27 * b**2) % l == 0: continue
            ap = int(pari.ellap(pari.ellinit([a, b]), l)); tot += 1
            bad += (ap - l - 1) % 5 == 0 or (ap + l + 1) % 5 == 0
    return mpf(bad) / tot
def local(l, scen):
    q = mpf(l); mult = lambda m: (q-1)**2 / q**(m+2)
    s_old = 1 - 1/q**2 - sum(mult(m) for m in range(5, 300, 5))
    wm_old = sum(mult(m) for m in range(2, 300, 2) if m % 5)          # alpha = -1 (I_n, n pair, 5 ne divise pas n)
    add = {"II": ((q-1)/q**3, 2), "III": ((q-1)/q**4, 3), "IV": ((q-1)/q**5, 4), "IV*": ((q-1)/q**8, 8),
           "III*": ((q-1)/q**9, 9), "II*": ((q-1)/q**10, 10)}
    adm = []
    if scen == "max" or (scen == "pru" and l % 5 not in (1, 4)):
        adm = [(m, v) for m, v in add.values()]
        f3 = e3_frac(l) if scen == "pru" else mpf(0)
        adm.append(((1 - 1/q) / q**5 * (1 - f3), 6))                      # I0*
        adm += [((q-1)**2 / q**(k+7), 6 + k) for k in range(1, 200) if scen == "max" or k % 5]   # I_n*
    s_new = s_old + sum(m for m, _ in adm)
    wm = wm_old + sum(m for m, v in adm if v % 2)
    return s_old, s_new, (wm_old / s_old, wm / s_new)
def big(scen):
    ratio = mpf(1); poly = {0: [mpf(1)] + [mpf(0)] * MMAX, 1: [mpf(1)] + [mpf(0)] * MMAX}; tail = [mpf(1), mpf(1)]
    for p in PR:
        if scen == "none" or p > 3000: s_old = s_new = 1; w = (None, None)
        else: s_old, s_new, w = local(p, scen)
        ratio *= mpf(s_new) / s_old
        if p % 4 != 3: continue
        if w[0] is None:
            qq = mpf(p); mult = lambda m: (qq-1)**2 / qq**(m+2)
            so = 1 - 1/qq**2 - sum(mult(m) for m in range(5, 300, 5)); w = (sum(mult(m) for m in range(2, 300, 2) if m % 5) / so,) * 2
        for i in (0, 1):
            if p < X0: poly[i] = [poly[i][j] * (1 - w[i]) + (poly[i][j-1] * w[i] if j else 0) for j in range(MMAX + 1)]
            else: tail[i] *= 1 - w[i]
    CD = [(tail[i] * sum(poly[i]), tail[i] * sum((-1)**j * c for j, c in enumerate(poly[i]))) for i in (0, 1)]
    return ratio, CD[0], CD[1]
kap = lambda C, D: C / 2 + mpf(3) / 10 * D
s2 = json.load(open(R + sys.argv[1])); s3 = json.load(open(R + sys.argv[2]))
def CD(s, which):
    p, m = mpf(s[which + "_p"]), mpf(s[which + "_m"]); tot = mpf(s["pru_total"]) if which == "pru" else mpf(1)
    return (p + m) / tot, (p - m) / tot
K = mpf("0.5501"); fac = mpf(7) / 8 * K + mpf(19) / 24 * (1 - K)
S1new = (mpf(4) / 5 - mpf(8) / 25 / 3124) / n(5)
base = fac * S1new + mpf(3) / 8 * K * (mpf(4) / 5 / n(5) - S1new)
v3 = {r["scenario"].split(" ")[0]: r for r in json.load(open(R + "bound_v3.json"))}
rows = []
for sc23, key in (("pru", "S3_prudent"), ("opt", "S3_optimiste")):
    C2, D2 = CD(s2, sc23); C3, D3 = CD(s3, sc23); core = mpf(v3[key]["gain"]) * 24 / 19
    for sc7 in ("none", "pru", "max"):
        ratio, (Co, Do), (Cn, Dn) = big(sc7)
        k = kap(C2 * C3 * Cn, D2 * D3 * Dn)
        for equi in (False, True):
            g = core * ratio * (mpf(19) / 24 + ((mpf(7) / 8 - mpf(19) / 24) * k if equi else 0))
            name = f"2,3 : {key[3:]} ; l>=7 additif : {sc7} ; équirépartition : {'oui' if equi else 'non'}"
            rows.append(dict(scenario=name, facteur_l7=float(ratio), kappa_ss=float(k), borne=float(base + g)))
            print(f"{name:75s} facteur l>=7 = {float(ratio):.5f}  kappa = {float(k):.4f}  borne = {float(base+g)*100:.3f} %")
json.dump(dict(entrees=sys.argv[1:], scenarios=rows), open(R + "bound_v5.json", "w"), indent=1, ensure_ascii=False)
