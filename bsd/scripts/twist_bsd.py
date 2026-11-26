"""BSD réelle et p-adique sur des tordues quadratiques E_D de rang 2 (sorties de twist_scan.py).

Réel : sur le modèle minimal de E_D (ellanalyticrank, ellrank, ellsaturation, ellbsd).
p-adique : ellpadicbsd(E, p, n, D) de PARI, qui calcule avec les symboles modulaires de E au
niveau N (et non N D^2), d'où le contournement de la limite mémoire. Il renvoie [r, L_p] avec
L_p conjecturalement = Reg_p(E_D) * #Ш(E_D). On divise par ellpadicregulator(E_D, p, ., points).
Usage : python3 twist_bsd.py ENTREE.jsonl SORTIE.jsonl [n_padique] [workers]"""
import json, sys, time, multiprocessing as mp

PRIMES = [3, 5, 7, 11, 13]
LEVEL = {3: 8, 5: 8, 7: 8, 11: 6, 13: 5}   # p^n borné : 13^8 déborde 2 Go
_pari = None


def init():
    global _pari
    from cypari import pari
    pari.allocatemem(2 * 10**9)
    pari.set_real_precision(38)
    _pari = pari


def work(arg):
    c, n0 = arg
    pari = _pari
    t0 = time.time()
    out = dict(c)
    try:
        E = pari.ellinit(pari(c["base"]))
        ED = pari.ellinit(c["ainv"])
        rk, Lr = pari.ellanalyticrank(ED)
        out["rank_an"] = int(rk)
        if int(rk) != 2:
            return out
        Lstar = Lr / 2
        d = pari.ellrank(ED)
        pts = d[3]
        if len(pts) < 2:
            pts = pari.ellrank(ED, 4)[3]
        out["descent"] = [int(d[0]), int(d[1]), int(d[2])]
        if len(pts) < 2:
            out["error"] = "points non trouvés"
            return out
        W = pari.ellsaturation(ED, pts, 100)
        Reg = pari.matdet(pari.ellheightmatrix(ED, W))
        sha = Lstar / (pari.ellbsd(ED) * Reg)
        out.update(Lstar=float(Lstar), Reg=float(Reg), sha_real=float(sha), gens=str(W),
                   tors=int(pari.elltors(ED)[0]), tam=int(pari.ellglobalred(ED)[2]))
        # u : changement de variable entre le modèle elltwist(E, D) (celui de ellpadicbsd)
        # et le modèle minimal de E_D ; rapport des périodes Omega_min / Omega_twist = u.
        u = int(pari('(E,D)->my(v);ellminimalmodel(ellinit(elltwist(E,D)),&v);v[1]')(E, c["D"]))
        out["u"] = u
        res = []
        for p in PRIMES:
            if c["N"] % p == 0 or c["D"] % p == 0:
                continue
            ap = int(pari.ellap(E, p))
            if ap % p == 0:
                continue
            t = time.time()
            n = min(n0, LEVEL[p])
            try:
                r, Lp = pari.ellpadicbsd(E, p, n, c["D"])
            except Exception as ex:  # compté comme échec pour ce p, pas comme succès
                res.append(dict(p=p, n=n, error=repr(ex)[:120]))
                continue
            Rp = pari.ellpadicregulator(ED, p, n + 6, W)
            raw = Lp / Rp
            shap = raw / u   # correction de normalisation (calibrée sur les cas Ш = 1)
            S = round(float(sha))
            e = shap - S
            agree = int(pari.valuation(e, p)) if e != 0 else int(pari.padicprec(shap, p))
            res.append(dict(p=p, n=n, r=int(r), sha_p=str(shap)[:90], sha_p_raw=str(raw)[:60], agree_digits=agree,
                            v_sha_p=int(pari.valuation(shap, p)) if shap != 0 else None,
                            time=round(time.time() - t, 1)))
        out["padic"] = res
    except Exception as ex:
        out["error"] = repr(ex)[:200]
    out["time"] = round(time.time() - t0, 1)
    return out


if __name__ == "__main__":
    cands = [json.loads(l) for l in open(sys.argv[1])]
    n = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    w = int(sys.argv[4]) if len(sys.argv) > 4 else 4
    with mp.get_context("spawn").Pool(w, initializer=init) as pool, open(sys.argv[2], "w") as f:
        for o in pool.imap_unordered(work, [(c, n) for c in cands]):
            f.write(json.dumps(o) + "\n"); f.flush()
            print(o["D"], o.get("rank_an"), round(o.get("sha_real", 0), 6), o.get("error", ""),
                  [(x["p"], x.get("agree_digits", "err")) for x in o.get("padic", [])], o.get("time"), flush=True)
