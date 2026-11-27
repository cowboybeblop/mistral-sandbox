"""Vérification indépendante des signes locaux (piste 1). Bhargava-Shankar (arXiv 1312.7859), tables 3 et 4, et nos
signes locaux (PARI ellrootno) diffèrent sur quelques lignes. Méthode indépendante :
  1. signe global w(E) et w(E_{-1}) par l'équation fonctionnelle de L(E, s) : lfuncheckfeq avec eps = +1 puis -1
     (le bon signe donne une erreur ~ 2^-70, le mauvais ~ 1) ;
  2. d = w(E) w(E_{-1}) = prod_p d_p ; pour p > 3, d_p = -1 ssi réduction multiplicative et p = 3 mod 4
     (BS Lemme 36, d'après Rohrlich) ;
  3. on fixe l'autre petit premier dans une classe où BS et PARI s'accordent et donnent un d déterministe :
     pour tester l = 3 : v2(A) >= 3, v2(B) = 2 (BS table 3 : d_2 = +1 ; PARI idem) ;
     pour tester l = 2 : 3 ne divise pas A (BS table 4 : d_3 = +1 ; PARI idem) ;
  4. on en déduit d_l = d / (d_autre * prod_{p>3} d_p) et on compare à PARI et à BS.
Usage : python3 feq_check.py [nombre par ligne]"""
import sys
from cypari import pari
pari.allocatemem(2 * 10**9); pari.set_real_precision(38)
NB = int(sys.argv[1]) if len(sys.argv) > 1 else 6
def v(x, p): return 99 if x == 0 else int(pari.valuation(x, p))
def w_L(E):
    L = pari.lfuncreate(E); res = []
    for eps in (1, -1):
        L[5] = eps; res.append(float(pari.lfuncheckfeq(L)))
    if min(res) > -50 or max(res) < -10: return None   # test non concluant
    return 1 if res[0] < res[1] else -1
def d_big(A, B):
    E = pari.ellinit([A, B]); D = -4 * A**3 - 27 * B**2; s = 1
    for p in pari.factor(abs(D))[0]:
        p = int(p)
        if p > 3 and p % 4 == 3 and int(pari.elllocalred(E, p)[1]) > 4: s = -s   # kodaira I_n (code n+4)
    return s
ROWS = [  # (nom, l, prédicat 3-adique ou 2-adique, valeurs BS de P(d_l = +1))
 ("l=3 : v3(A)=1, v3(B)=0, v3(D)=3", 3, lambda A, B, D: v(A,3)==1 and v(B,3)==0 and v(D,3)==3, "BS : P(d3=+1)=5/6"),
 ("l=3 : v3(A)=1, v3(B)=0, v3(D)=5", 3, lambda A, B, D: v(A,3)==1 and v(B,3)==0 and v(D,3)==5, "BS : P(d3=+1)=1/2"),
 ("l=3 : v3(A)=2, v3(B)>=3",         3, lambda A, B, D: v(A,3)==2 and v(B,3)>=3, "BS : d3=-1"),
 ("l=3 : v3(A)>=4, v3(B)=3",         3, lambda A, B, D: v(A,3)>=4 and v(B,3)==3, "BS : P(d3=+1)=1/3"),
 ("l=2 : v2(A)=1, v2(B)=2",          2, lambda A, B, D: v(A,2)==1 and v(B,2)==2, "BS : Delta'_2 = 1 mod 4, P(d2=+1)=1/2"),
 ("l=2 : v2(A)=2, v2(B)=4, v2(16D)=13", 2, lambda A, B, D: v(A,2)==2 and v(B,2)==4 and v(16*D,2)==13, "BS : d2 = +1 (Delta'=1) ou -1 (Delta'=3)"),
]
other = {3: lambda A, B: v(A, 2) >= 3 and v(B, 2) == 2, 2: lambda A, B: v(A, 3) == 0}
fails = 0
for name, l, pred, bs in ROWS:
    print("==", name, "|", bs); found = 0
    for H in range(1, 400):
        for A in range(-H, H + 1):
            for B in (H, -H) if abs(A) < H else range(-H, H + 1):
                if found >= NB: break
                D = -4 * A**3 - 27 * B**2
                if D == 0 or B <= 0 or not pred(A, B, D) or not other[l](A, B): continue
                E, Em = pari.ellinit([A, B]), pari.ellinit([A, -B])
                w1, w2 = w_L(E), w_L(Em)
                if w1 is None or w2 is None: print("  non concluant", A, B); continue
                dl = w1 * w2 * d_big(A, B)          # d_autre = +1 par construction
                dl_pari = int(pari.ellrootno(E, l) * pari.ellrootno(Em, l))
                u = (D // 2**v(D, 2)) % 4
                ok = dl == dl_pari and int(pari.ellrootno(E)) == w1 and int(pari.ellrootno(Em)) == w2
                fails += not ok; found += 1
                print(f"  (A,B)=({A},{B}) N={int(pari.ellglobalred(E)[0])},{int(pari.ellglobalred(Em)[0])} "
                      f"w={w1:+d},{w2:+d}  d_{l} déduit={dl:+d}  d_{l} PARI={dl_pari:+d}  Delta'_2 mod 4={u}  {'OK' if ok else 'ECHEC'}")
        if found >= NB: break
print("désaccords PARI / équation fonctionnelle :", fails)
