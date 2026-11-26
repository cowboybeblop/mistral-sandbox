"""Certification de ord_T L_p(E, T) <= 2 pour les couples (E, p) de la mission 2.

Argument (voir rapport, section « Certification ») :
  * la somme de Riemann de niveau n est l'image EXACTE de L_p dans Lambda / omega_{n-1},
    omega_{n-1} = (1+T)^{p^{n-1}} - 1, car les classes {a : <a> dans gamma^j Gamma^{p^{n-1}}}
    sont les réunions de boules a + p^n Z_p sommées ;
  * L_p est dans D^{-1} Lambda, D = dénominateur du symbole x^+ (valeurs sur les générateurs) ;
  * donc L_p - L_n = omega_{n-1} g avec g dans D^{-1} Lambda, et pour m <= 2 (p impair)
    l'erreur sur le coefficient c_m est de valuation >= n - 1 - v_p(D) ;
  * si v_p(c_2) < n - 1 - v_p(D), le vrai coefficient c_2 est non nul : ord_T L_p <= 2.
Conséquence (conditionnelle, voir rapport) : si de plus E[p] est irréductible,
la conjecture principale cyclotomique rationnelle (Wan, cité par BCGS Thm 3.2.6) et le
théorème de contrôle de Mazur donnent corang Sel_{p^infini}(E/Q) <= 2, donc, avec deux
points indépendants, rang = 2 et Ш(E/Q)[p^infini] fini.
"""
import json, sys, multiprocessing as mp

_pari = None


def init():
    global _pari
    from cypari import pari
    pari.allocatemem(2 * 10**9)
    _pari = pari


def work(line):
    pari = _pari
    r = json.loads(line)
    out = dict(label=r["label"], N=r["N"], certs=[])
    if "padic" not in r:
        out["error"] = r.get("error", "pas de données p-adiques")
        return out
    E = pari.ellinit(r["ainv"])
    M, xs = pari.msfromell(E, 1)
    D = int(pari('(M,x)->denominator(mseval(M,x))')(M, xs))
    out["D"] = D
    for x in r["padic"]:
        p, n = x["p"], x["n"]
        vD = int(pari.valuation(D, p))
        bound = n - 1 - vD
        try:
            L = pari.ellisomat(E, p, 1)
            irreducible = (len(L[0]) == 1)
        except Exception as ex:
            irreducible = None
        out["certs"].append(dict(p=p, n=n, v_c2=x["v_c2"], bound=bound, ord_le_2=(x["v_c2"] < bound),
                                 c0_exact_zero=(x["v_c0"] >= 10**6), irreducible=irreducible,
                                 v_Regp=x["v_Regp"], agree_real_digits=x["agree_real_digits"]))
    return out


def main():
    lines = open(sys.argv[1]).read().splitlines()
    with mp.get_context("spawn").Pool(4, initializer=init) as pool, open(sys.argv[2], "w") as fo:
        for o in pool.imap_unordered(work, lines):
            fo.write(json.dumps(o) + "\n")
            fo.flush()


if __name__ == "__main__":
    main()
