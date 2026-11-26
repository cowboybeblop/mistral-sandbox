"""Seconde passe pour les couples (E_D, p) où ellpadicbsd a renvoyé r != 2.

Diagnostic (jeu de calibrage, Ш = 1) : avec v_p(Reg_p) élevé, les coefficients d'ordre 2 et 3
de L_p tombent sous la précision et ellpadicbsd renvoie le coefficient d'ordre r = 4.
Règle fixée a priori : on ne compare que si r = 2 ; sinon on remonte n de 2 puis de 4 ;
si r reste != 2, le couple est « précision insuffisante » (ni succès ni désaccord).
Usage : python3 twist_repair.py ENTREE.jsonl SORTIE.jsonl"""
import json, sys, multiprocessing as mp
sys.path.insert(0, sys.path[0])
import twist_bsd as tb

CAP = {3: 14, 5: 12, 7: 10, 11: 8, 13: 6}


def init():
    from cypari import pari
    pari.allocatemem(3 * 10**9)
    tb._pari = pari


def repair(r):
    pari = tb._pari
    if "padic" not in r:
        return r
    E = pari.ellinit(pari(r["base"])); ED = pari.ellinit(r["ainv"]); W = pari(r["gens"])
    S = round(r["sha_real"])
    for i, x in enumerate(r["padic"]):
        if x.get("r") == 2 or "agree_digits" not in x:
            continue
        p, n0 = x["p"], x["n"]
        new = dict(p=p, first_pass=dict(n=n0, r=x["r"], sha_p=x["sha_p"]))
        for n in (n0 + 2, n0 + 4):
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
    return r


if __name__ == "__main__":
    R = [json.loads(l) for l in open(sys.argv[1])]
    with mp.get_context("spawn").Pool(4, initializer=init) as pool, open(sys.argv[2], "w") as f:
        for o in pool.imap(repair, R):
            f.write(json.dumps(o) + "\n")
