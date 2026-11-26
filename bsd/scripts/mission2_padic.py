"""Mission 2 : BSD p-adique contre BSD réelle sur des courbes de rang analytique 2.

Méthode p-adique : sommes de Riemann de Mazur–Tate–Teitelbaum sur le symbole
modulaire x^+ de E (scripts/mtt.gp), car ellpadicL / mspadicinit de PARI demandent
O(N^2 (n+k)^2 p) mémoire et débordent dès N ~ 1000 (6 Go à N = 9003).
Calibration : identique à ellpadicL de PARI sur 389a, 433a, 37a, 11a (scripts/calib.py).

Prédiction (Mazur–Tate–Teitelbaum, p bon ordinaire, p ne divisant pas N) :
  (1 - 1/alpha)^-2 * L_p^*(s=0) = c_inf * prod(c_v) * Sha * Reg_p / #tors^2
où L_p^* est le coefficient de s^r (s : variable cyclotomique, T = gamma^s - 1),
Reg_p = ellpadicregulator(E, p, ., générateurs saturés), et c_inf le nombre de
composantes réelles (le symbole est normalisé par Omega^+ = E.omega[1]).

Précision : on calcule aux niveaux n-1 et n ; le nombre de chiffres p-adiques
fiables de Sha_p est la valuation de la différence entre les deux.

Usage : python3 mission2_padic.py SORTIE.jsonl [taille_échantillon] [graine]
"""
import json, random, sys, time, multiprocessing as mp

LEVELS = {3: 11, 5: 8, 7: 6, 11: 5, 13: 4}   # niveau n (p^n ~ 1e5 a 4e5)
NPRIMES = 3
SEED_DEFAULT = 20261126


def load_rank2(path, nmax):
    curves = []
    with open(path) as f:
        for line in f:
            t = line.split()
            N, cl, num = int(t[0]), t[1], int(t[2])
            if N >= nmax or num != 1 or int(t[4]) != 2:
                continue
            curves.append(dict(label=f"{N}{cl}{num}", N=N, ainv=json.loads(t[3]),
                               crem=dict(tors=int(t[5]), tam=int(t[6]), Omega=float(t[7]),
                                         Lr=float(t[8]), Reg=float(t[9]), Sha=float(t[10]))))
    return curves


_pari = None


def init():
    global _pari
    from cypari import pari
    pari.allocatemem(2 * 10**9)
    pari.set_real_precision(38)
    pari('read("%s")' % (sys.path[0] + "/mtt.gp"))
    _pari = pari


def real_bsd(pari, E, W):
    """Sha analytique réel par deux voies : ellbsd de PARI, et Omega, Tamagawa, torsion à la main."""
    rk, Lr = pari.ellanalyticrank(E)
    rk = int(rk)
    Lstar = Lr / pari.factorial(rk)
    Reg = pari.matdet(pari.ellheightmatrix(E, W))
    shaA = Lstar / (pari.ellbsd(E) * Reg)
    gr = pari.ellglobalred(E)
    tam = int(gr[2])
    tors = int(pari.elltors(E)[0])
    cinf = 2 if pari('e->e.disc')(E) > 0 else 1
    Omega = pari('e->e.omega[1]')(E) * cinf
    shaB = Lstar * tors**2 / (Omega * tam * Reg)
    return dict(rank_an=rk, Lstar=float(Lstar), Reg=float(Reg), tam=tam, tors=tors, cinf=cinf,
                Omega=float(Omega), shaA=float(shaA), shaB=float(shaB))


def padic_sha(pari, E, MS, W, p, n, cinf, tam, tors):
    """Sha_p au niveau n (élément de Q_p) et données de contrôle."""
    prec = 3 * n + 10
    c = pari('mtt_series')(E, MS, p, n, 3, prec)
    s = pari('mtt_s_coeffs')(c, p, prec)
    ap = int(pari.ellap(E, p))
    al = pari('mtt_alpha')(ap, p, prec)
    lead = s[2] / (1 - 1 / al) ** 2
    Rp = pari.ellpadicregulator(E, p, prec, W)
    sha = lead * tors**2 / (cinf * tam * Rp)
    v = lambda x: int(pari.valuation(x, p)) if x != 0 else 10**6
    return sha, dict(v_c0=v(c[0]), v_c1=v(c[1]), v_c2=v(c[2]), v_Regp=v(Rp))


def work(cv):
    pari = _pari
    t0 = time.time()
    out = dict(label=cv["label"], N=cv["N"], ainv=cv["ainv"], crem=cv["crem"])
    try:
        E = pari.ellinit(cv["ainv"])
        if pari.ellglobalred(E)[1] != pari('[1,0,0,0]'):
            out["warn"] = "modèle non minimal"
        rk = pari.ellrank(E)
        pts = rk[3]
        if len(pts) < 2:
            rk = pari.ellrank(E, 5)
            pts = rk[3]
        out["ellrank"] = [int(rk[0]), int(rk[1]), int(rk[2])]
        if len(pts) < 2:
            out["error"] = "moins de 2 points trouvés"
            return out
        W = pari.ellsaturation(E, pts, 100)
        out["gens"] = str(W)
        rb = real_bsd(pari, E, W)
        out["real"] = rb
        N = cv["N"]
        MS = pari.msfromell(E, 1)
        res = []
        for p in sorted(LEVELS):
            if len(res) >= NPRIMES:
                break
            if N % p == 0:
                continue
            ap = int(pari.ellap(E, p))
            if ap % p == 0:
                continue  # supersingulier
            n = LEVELS[p]
            t = time.time()
            shaN, info = padic_sha(pari, E, MS, W, p, n, rb["cinf"], rb["tam"], rb["tors"])
            shaM, _ = padic_sha(pari, E, MS, W, p, n - 1, rb["cinf"], rb["tam"], rb["tors"])
            d = shaN - shaM
            digits = int(pari.valuation(d, p)) if d != 0 else int(pari.padicprec(shaN, p))
            shaR = round(rb["shaA"])
            e = shaN - shaR
            vR = int(pari.valuation(e, p)) if e != 0 else int(pari.padicprec(shaN, p))
            res.append(dict(p=p, n=n, ap=ap, anomalous=(ap % p == 1), digits=digits,
                            agree_real_digits=vR, consistent=(vR >= digits),
                            sha_p=str(shaN)[:120], time=round(time.time() - t, 1), **info))
        out["padic"] = res
    except Exception as ex:  # plantages comptés comme échecs, jamais comme succès
        out["error"] = repr(ex)[:300]
    out["time"] = round(time.time() - t0, 1)
    return out


def main():
    outpath = sys.argv[1]
    size = int(sys.argv[2]) if len(sys.argv) > 2 else 150
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else SEED_DEFAULT
    allc = load_rank2(sys.path[0] + "/../data/allbsd/allbsd.00000-09999", 10000)
    rng = random.Random(seed)
    sample = rng.sample(allc, size)
    for must in ("389a1", "433a1"):
        if must not in [c["label"] for c in sample]:
            sample.append(next(c for c in allc if c["label"] == must))
    sample.sort(key=lambda c: c["N"])
    with open(outpath + ".meta.json", "w") as f:
        json.dump(dict(seed=seed, size=size, population=len(allc), levels=LEVELS,
                       labels=[c["label"] for c in sample]), f, indent=1)
    with mp.get_context("spawn").Pool(4, initializer=init) as pool, open(outpath, "w") as f:
        for r in pool.imap_unordered(work, sample):
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
            f.flush()
            print(r["label"], r.get("error", ""), [(x["p"], x["digits"], x["consistent"]) for x in r.get("padic", [])],
                  r.get("time"), flush=True)


if __name__ == "__main__":
    main()
