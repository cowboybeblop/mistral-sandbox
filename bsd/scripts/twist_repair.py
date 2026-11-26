"""Seconde passe pour les couples (E_D, p) où ellpadicbsd a renvoyé r != 2.

Diagnostic (jeu de calibrage, Ш = 1) : avec v_p(Reg_p) élevé, les coefficients d'ordre 2 et 3
de L_p tombent sous la précision et ellpadicbsd renvoie le coefficient d'ordre r = 4.
Règle fixée a priori : on ne compare que si r = 2 ; sinon on remonte n de 2 puis de 4 ;
si r reste != 2, le couple est « précision insuffisante » (ni succès ni désaccord).
Usage : python3 twist_repair.py ENTREE.jsonl SORTIE.jsonl [pile_Go] [workers]"""
import json, sys, multiprocessing as mp
sys.path.insert(0, sys.path[0])
import twist_bsd as tb

CAP = {3: 14, 5: 12, 7: 10, 11: 8, 13: 6}


def init():
    from cypari import pari
    pari.allocatemem(int(sys.argv[3]) * 10**9 if len(sys.argv) > 3 else 6 * 10**9)
    tb._pari = pari


def repair(r):
    pari = tb._pari
    if "padic" not in r:
        return r
    E = pari.ellinit(pari(r["base"])); ED = pari.ellinit(r["ainv"]); W = pari(r["gens"])
    S = round(r["sha_real"])
    for i, x in enumerate(r["padic"]):
        if x.get("r") == 2:
            continue
        p, n0 = x["p"], x["n"]
        if "error" in x:   # débordement de pile en première passe : même n, plus de mémoire
            new = dict(p=p, first_pass=dict(n=n0, error=x["error"]))
            levels = (n0, n0 + 2, n0 + 4)
        else:              # r != 2 : précision insuffisante, on remonte n
            new = dict(p=p, first_pass=dict(n=n0, r=x["r"], sha_p=x["sha_p"]))
            levels = (n0 + 2, n0 + 4)
        for n in levels:
            if n > CAP[p]:
                break
            try:
                rr, Lp = pari.ellpadicbsd(E, p, n, r["D"])
            except Exception as ex:
                new["error"] = repr(ex)[:100]; break
            if int(rr) == 2:
                shap = Lp / pari.ellpadicregulator(ED, p, n + 8, W) / r["u"]
                e = shap - S
                new.update(n=n, r=2, sha_p=str(shap)[:90],
                           agree_digits=int(pari.valuation(e, p)) if e != 0 else int(pari.padicprec(shap, p)),
                           v_sha_p=int(pari.valuation(shap, p)) if shap != 0 else None)
                break
        else:
            pass
        if new.get("r") != 2:
            new["insufficient_precision"] = True
        r["padic"][i] = new
    r["repaired"] = True
    for x in r["padic"]:
        if "error" in x and "agree_digits" not in x and "first_pass" in x:
            x["insufficient_memory"] = True
    return r


if __name__ == "__main__":
    R = [json.loads(l) for l in open(sys.argv[1])]
    with mp.get_context("spawn").Pool(int(sys.argv[4]) if len(sys.argv) > 4 else 2, initializer=init) as pool, open(sys.argv[2], "w") as f:
        for o in pool.imap(repair, R):
            f.write(json.dumps(o) + "\n")
