"""Piste 1 (LISTE_GAINS.md) : équirépartition des signes dans la famille supersingulière.
Formule (BSZ Th. 25 et preuve du Cor. 26, arXiv 1407.1826) appliquée à notre famille F_ss :
   gain = SS5 * mu2 * mu3 * P7 * (1 - eps) * [ 19/24 + (7/8 - 19/24) * kappa_ss ],
   kappa_ss = mu(F') / mu(F_ss), F' = sous-famille fermée par torsion par -1 sur laquelle d(E) = r(E) r(E_{-1}) = -1.
Reformulation locale de BS §5 (arXiv 1312.7859) : d(E) = beta_2 beta_3 sgn(Delta) prod_{p>3, p=3 (4)} alpha_p.
Si C_v = P(cellule admise, fermée, beta_v = +1) + P(..., -1) et D_v = P(+1) - P(-1), conditionnellement à la
famille en v, et si mu_inf(Delta < 0) = 4/5 (volume de {-u^3 > w^2} dans [-1,1]^2 : 1/5 pour Delta > 0), alors
   kappa = (4/5) P(prod beta = +1) + (1/5) P(prod beta = -1) = prod C / 2 + (3/10) prod D.
Contrôles : (i) reproduire 59,179 % / 40,32 % (BS Prop. 35) et 96,689 % / 3,26 % (Prop. 37) et kappa = 0,5501 à partir
des tables de BS ; (ii) kappa « vrai » de la famille de toutes les courbes avec nos signes locaux (corrigés).
Usage : python3 bound_v4.py signs_l2.json signs_l3.json"""
import json, sys
from fractions import Fraction as Fr
from mpmath import mp, mpf, zeta
mp.dps = 20
R = sys.path[0] + "/../results/"
def isp(m): return m > 1 and all(m % d for d in range(2, int(m**.5) + 1))
n = lambda l: 1 - mpf(l) ** -10
X0, MMAX = 10**4, 2      # premiers exceptionnels < X0, au plus MMAX (comme BS Prop. 37)
PR = [p for p in range(5, 2 * 10**5) if isp(p)]

# ---------- (i) reproduction de BS ----------
T3 = [  # (densité, (1,1), (1,-1), (3,1), (3,-1)) -- table 3 de BS (lue sur l'image de la page 25)
 (Fr(1,4),[Fr(3,4),Fr(1,4),0,0]),(Fr(1,4),[Fr(3,4),Fr(1,4),0,0]),(Fr(1,8),[Fr(1,2),Fr(1,2),0,0]),
 (Fr(1,8),[Fr(1,4),Fr(1,4),Fr(1,2),0]),(Fr(1,32),[Fr(1,2),Fr(1,2),0,0]),(Fr(1,64),[Fr(1,2),Fr(1,2),0,0]),
 (Fr(1,64),[1,0,0,0]),(Fr(1,32),[0,Fr(3,4),0,Fr(1,4)]),(Fr(1,64),[Fr(1,2),0,Fr(1,2),0]),
 (Fr(1,256),[Fr(7,16),Fr(7,16),Fr(1,16),Fr(1,16)]),(Fr(1,512),[0,1,0,0]),(Fr(1,256),[Fr(1,2),0,Fr(1,4),Fr(1,4)]),
 (Fr(1,1024),[0,1,0,0]),(Fr(1,16),[Fr(1,2),0,0,Fr(1,2)]),(Fr(1,32),[Fr(1,4),Fr(1,4),Fr(1,2),0]),
 (Fr(1,64),[Fr(1,2),0,0,Fr(1,2)]),(Fr(1,128),[Fr(1,4)]*4),(Fr(1,256),[Fr(1,4)]*4),
 (Fr(1,512),[Fr(1,2),0,0,Fr(1,2)]),(Fr(1,1024),[0,Fr(1,2),0,Fr(1,2)]),(Fr(1,2048),[Fr(1,2),0,Fr(1,2),0])]
T4 = [  # table 4 de BS (page 26)
 (Fr(2,3),[1,0,0,0]),(Fr(2,27),[0,0,Fr(1,3),Fr(2,3)]),(Fr(4,81),[0,0,0,1]),(Fr(2,81),[0,0,0,1]),
 (Fr(2,81),[0,0,1,0]),(Fr(4,729),[1,0,0,0]),(Fr(2,729),[0,0,0,1]),(Fr(2,729),[0,1,0,0]),
 (Fr(2,3**8),[0,0,Fr(1,3),Fr(2,3)]),(Fr(4,3**9),[0,0,0,1]),(Fr(2,3**9),[0,0,0,1]),(Fr(2,3**9),[0,0,1,0]),
 (Fr(4,3**11),[1,0,0,0]),(Fr(2,3**11),[0,0,0,1]),(Fr(2,27),[0,0,Fr(5,6),Fr(1,6)]),(Fr(4,81),[1,0,0,0]),
 (Fr(4,3**5),[0,0,Fr(1,2),Fr(1,2)]),(Fr(1,2*3**4),[1,0,0,0]),(Fr(1,2*3**5),[0,0,1,0])]
def tab(T, l):
    tot = [sum(d * r[i] for d, r in T) for i in range(4)]
    # beta = d * chi(Delta) : (1,1) et (3,-1) -> +1 ; (1,-1) et (3,1) -> -1 ; normalisation par 1 - l^-10
    p, m = (tot[0] + tot[3]) / Fr(1) , (tot[1] + tot[2])
    return [float(x) for x in tot], mpf(p.numerator) / p.denominator / n(l), mpf(m.numerator) / m.denominator / n(l)
def big_BS():
    # BS Prop. 37 : alpha = +1 : bonne, mult. v in {1,3}, add. v in {2,4} ; alpha = -1 : mult. v = 2, add. v = 3
    lp, e1, e2 = mpf(1), mpf(0), mpf(0)
    for p in PR:
        if p % 4 != 3: continue
        q = mpf(p); a = (1 - 1/q + (q-1)**2/q**3 + (q-1)**2/q**5 + (q-1)/q**3 + (q-1)/q**5) / n(p)
        b = ((q-1)**2/q**4 + (q-1)/q**4) / n(p)
        lp *= a
        if p < X0: e2 += e1 * b / a; e1 += b / a
    return lp * (1 + e2), lp * e1          # F3 (0 ou 2 exceptionnels), F4 (1 exceptionnel)
def big_ss():
    # notre famille en l >= 7 : semistable, sans (mult. et 5 | v) ; alpha = -1 ssi mult. et v pair
    # renvoie (C, D) conditionnels à Sigma_l, avec au plus MMAX exceptionnels < X0, aucun au-delà
    poly = [mpf(1)] + [mpf(0)] * MMAX; tail = mpf(1)
    for p in PR:
        if p < 7 or p % 4 != 3: continue
        q = mpf(p); mult = lambda m: (q-1)**2 / q**(m+2)
        sig = 1 - 1/q**2 - sum(mult(m) for m in range(5, 200, 5))
        w = sum(mult(m) for m in range(2, 200, 2) if m % 5) / sig
        if p < X0:
            poly = [poly[j] * (1 - w) + (poly[j-1] * w if j else 0) for j in range(MMAX + 1)]
        else:
            tail *= 1 - w
    C = tail * sum(poly); D = tail * sum((-1)**j * c for j, c in enumerate(poly))
    return C, D
kap = lambda C, D: C / 2 + mpf(3) / 10 * D
t2, P2, M2 = tab(T3, 2); t3, P3, M3 = tab(T4, 3); F3, F4 = big_BS()
F1 = P2 * P3 + M2 * M3; F2 = P2 * M3 + M2 * P3
print("BS table 3 totaux", [round(x, 4) for x in t2], " table 4 totaux", [round(x, 4) for x in t3])
print(f"BS reproduit : F1 = {float(F1):.5f} (BS > .59179), F2 = {float(F2):.5f} (BS > .4032), "
      f"F3 = {float(F3):.5f} (BS > .96689), F4 = {float(F4):.5f} (BS > .0326)")
Fm, Fp = F1 * F3 + F2 * F4, F1 * F4 + F2 * F3
kBS = mpf(4)/5 * Fm + mpf(1)/5 * Fp
print(f"BS reproduit : F- = {float(Fm):.5f} (BS .58534), F+ = {float(Fp):.5f} (BS .40914), kappa = {float(kBS):.5f} (BS .5501)")

# ---------- (ii) nos signes locaux ----------
s2 = json.load(open(R + sys.argv[1])); s3 = json.load(open(R + sys.argv[2]))
def CD(s, which):
    p, m = mpf(s[which + "_p"]), mpf(s[which + "_m"])
    tot = mpf(s["pru_total"]) if which == "pru" else mpf(1)
    return (p + m) / tot, (p - m) / tot
C2o, D2o = CD(s2, "opt"); C3o, D3o = CD(s3, "opt"); C2p, D2p = CD(s2, "pru"); C3p, D3p = CD(s3, "pru")
C3BS, D3BS = F3 + F4, F3 - F4
kfull = kap(C2o * C3o * C3BS, D2o * D3o * D3BS)
print(f"\nnos signes : 2 : C = {float(C2o):.5f}, D = {float(D2o):.5f} (BS : {float(P2+M2):.5f}, {float(P2-M2):.5f}) ; "
      f"3 : C = {float(C3o):.5f}, D = {float(D3o):.5f} (BS : {float(P3+M3):.5f}, {float(P3-M3):.5f})")
print(f"kappa (toutes les courbes, conditions de BS en p > 3, nos signes en 2 et 3) = {float(kfull):.5f}  (BS : 0,5501)")
Cb, Db = big_ss()
k_opt = kap(C2o * C3o * Cb, D2o * D3o * Db); k_pru = kap(C2p * C3p * Cb, D2p * D3p * Db)
print(f"famille supersingulière, l >= 7 : C = {float(Cb):.6f}, D = {float(Db):.6f}")
print(f"kappa_ss prudent = {float(k_pru):.5f}   kappa_ss optimiste = {float(k_opt):.5f}")

# ---------- borne (mêmes constantes que bound_v3.py) ----------
K = mpf("0.5501")
fac = mpf(7) / 8 * K + mpf(19) / 24 * (1 - K)
S1new = (mpf(4) / 5 - mpf(8) / 25 / 3124) / n(5); SS5 = mpf(4) / 25 / n(5)
base = fac * S1new + mpf(3) / 8 * K * (mpf(4) / 5 / n(5) - S1new)
v3 = {r["scenario"].split(" ")[0]: r for r in json.load(open(R + "bound_v3.json"))}
rows = []
for name, key, k in [("S4_prudent : S3_prudent + équirépartition (kappa_ss prudent)", "S3_prudent", k_pru),
                     ("S4_optimiste : S3_optimiste + équirépartition (kappa_ss optimiste)", "S3_optimiste", k_opt)]:
    r = v3[key]; core = SS5 * mpf(r["mu2"]) * mpf(r["mu3"]) * (mpf(r["gain"]) / (mpf(19)/24 * SS5 * mpf(r["mu2"]) * mpf(r["mu3"])))
    g = core * (mpf(19) / 24 + (mpf(7) / 8 - mpf(19) / 24) * k)
    rows.append(dict(scenario=name, kappa_ss=float(k), gain=float(g), borne=float(base + g), borne_v3=r["borne"]))
    print(f"{name:70s} borne = {float(base+g)*100:.3f} %  (v3 : {r['borne']*100:.3f} %, +{float(base+g-r['borne'])*100:.3f} pt)")
json.dump(dict(kappa_BS_reproduit=float(kBS), kappa_toutes_courbes_signes_corriges=float(kfull),
               C_D={"2_opt": [float(C2o), float(D2o)], "3_opt": [float(C3o), float(D3o)], "2_pru": [float(C2p), float(D2p)],
                    "3_pru": [float(C3p), float(D3p)], "l>=7_ss": [float(Cb), float(Db)]},
               entrees=[sys.argv[1], sys.argv[2]], scenarios=rows), open(R + "bound_v4.json", "w"), indent=1, ensure_ascii=False)
