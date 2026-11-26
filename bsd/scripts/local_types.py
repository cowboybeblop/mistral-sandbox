"""Types de composante locale en l (l = 2, 3) pour E_{A,B}, par cellules (A,B) mod l^k, avec la
normalisation de BSZ. Classes (conservatrices) :
  semistable        : f <= 1 (bonne ou multiplicative)            -> Steinberg ou non ramifiée
  steinberg_tordu   : f >= 2 et v_l(j) < 0                         -> additive potentiellement multiplicative
  sp_quadratique    : f >= 2, v_l(j) >= 0, et une tordue quadratique ramifiée a bonne réduction
                      -> série principale (caractère quadratique)
  autre             : le reste (supercuspidale, ou série principale d'ordre 3, 4 ou 6 : non décidé ici)
Tordues ramifiées : l = 2 : d in {-1, 2, -2, -5, 10, -10} ; l = 3 : d in {3, -3}.
Usage : python3 local_types.py l k [R]"""
import sys, json, random
from cypari import pari
pari.allocatemem(2 * 10**9)
l, k = int(sys.argv[1]), int(sys.argv[2]); R = int(sys.argv[3]) if len(sys.argv) > 3 else 2
TW = {2: [-1, 2, -2, -5, 10, -10], 3: [3, -3]}[l]
pari('ltype(a,b,l,tw) = my(E = ellinit([a,b]), f, j); if (E == [], return(-1)); '
     'f = elllocalred(E, l)[1]; if (f <= 1, return(0)); j = E.j; '
     'if (j != 0 && valuation(j, l) < 0, return(1)); '
     'for (i = 1, #tw, my(d = tw[i], Ed = ellinit([d^2*a, d^3*b])); if (elllocalred(Ed, l)[1] == 0, return(2))); 3')
lt = pari('ltype'); tw = pari(str(TW))
names = ["semistable", "steinberg_tordu", "sp_quadratique", "autre"]
rng = random.Random(2); Mk = l ** k; M = l ** (k + 6)
cnt = [0, 0, 0, 0]; undet = 0; nonmin = 0
for a in range(Mk):
    for b in range(Mk):
        if k >= 6 and a % l**4 == 0 and b % l**6 == 0:
            nonmin += 1; continue
        t = int(lt(a, b, l, tw)); ok = t >= 0
        for _ in range(R):
            if not ok: break
            if int(lt(a + Mk * rng.randrange(M // Mk), b + Mk * rng.randrange(M // Mk), l, tw)) != t: ok = False
        if ok: cnt[t] += 1
        else: undet += 1
norm = (1 - l ** -10.0) * Mk * Mk
out = dict(l=l, k=k, **{n: c / norm for n, c in zip(names, cnt)}, indetermine=undet / norm)
print(json.dumps(out, indent=1))
json.dump(out, open(sys.path[0] + f"/../results/local_types_l{l}_k{k}.json", "w"), indent=1)
