"""Mission 3 : BSD réelle recalculée sur les 42 courbes de rang 2 avec Ш = 4 (N < 500 000).

Pour chaque courbe E (fichiers allbsd de Cremona) :
  1. L''(E,1)/2 par ellanalyticrank (PARI), comparé à la colonne de Cremona ;
  2. 2-descente (ellrank) : bornes de rang et s = rang de Ш[2]/2Ш[4] (accouplement de Cassels) ;
  3. générateurs : recherche propre (ellrank avec effort), sinon fichiers allgens de Cremona,
     vérifiés sur la courbe puis saturés (ellsaturation, B = 200) ;
  4. Ш analytique par deux voies (ellbsd ; Omega, Tamagawa, torsion à la main) ;
  5. pour chaque courbe E' 2-isogène (ellisomat) : mêmes quantités, points poussés par
     l'isogénie puis saturés, et Ш(E') analytique. Le quotient BSD est invariant par isogénie
     (Cassels), donc Ш(E)/Ш(E') se lit sur Omega, Tamagawa, torsion et régulateurs seuls.

Usage : python3 mission3_sha4.py SORTIE.jsonl
"""
import json, sys, time, multiprocessing as mp

HERE = sys.path[0]
_pari = None


def init():
    global _pari
    from cypari import pari
    pari.allocatemem(3 * 10**9)
    pari.set_real_precision(38)
    _pari = pari


def load():
    out = []
    for line in open(HERE + "/../data/rank2_sha_ge4.txt"):
        t = line.split()
        out.append(dict(label=f"{t[0]}{t[1]}{t[2]}", N=int(t[0]), cls=t[1], num=int(t[2]), ainv=json.loads(t[3]),
                        crem=dict(tors=int(t[5]), tam=int(t[6]), Omega=float(t[7]), Lr=float(t[8]),
                                  Reg=float(t[9]), Sha=float(t[10]))))
    return out


def allgens_points(N, cls, num):
    k = N // 10000
    name = f"allgens.{k*10000:05d}-{k*10000+9999}" if k else "allgens.00000-09999"
    with open(HERE + "/../data/allgens/" + name) as f:
        for line in f:
            t = line.split()
            if int(t[0]) == N and t[1] == cls and int(t[2]) == num:
                r = int(t[4])
                pts = []
                for s in t[6:6 + r]:
                    X, Y, Z = (int(u) for u in s.strip("[]").split(":"))
                    pts.append(f"[{X}/{Z},{Y}/{Z}]")
                return "[" + ",".join(pts) + "]"
    return None


def bsd_terms(pari, E, W):
    Reg = pari.matdet(pari.ellheightmatrix(E, W))
    tam = int(pari.ellglobalred(E)[2])
    tors = int(pari.elltors(E)[0])
    cinf = 2 if pari('e->e.disc')(E) > 0 else 1
    Omega = pari('e->e.omega[1]')(E) * cinf
    return dict(Reg=Reg, tam=tam, tors=tors, Omega=Omega, cinf=cinf)


def f(x):
    return float(x)


def work(cv):
    pari = _pari
    t0 = time.time()
    out = dict(label=cv["label"], N=cv["N"], crem=cv["crem"])
    try:
        E = pari.ellinit(cv["ainv"])
        gr = pari.ellglobalred(E)
        out["conductor_ok"] = int(gr[0]) == cv["N"]
        out["minimal"] = str(gr[1]) == "[1, 0, 0, 0]"
        rk, Lr = pari.ellanalyticrank(E)
        out["rank_an"] = int(rk)
        Lstar = Lr / pari.factorial(int(rk))
        out["Lstar"] = f(Lstar)
        # 2-descente
        d = pari.ellrank(E)
        out["descent"] = dict(r=int(d[0]), R=int(d[1]), s=int(d[2]))
        pts = d[3]
        src = "ellrank"
        if len(pts) < 2:
            d2 = pari.ellrank(E, 4)
            pts = d2[3]
        if len(pts) < 2:
            g = allgens_points(cv["N"], cv["cls"], cv["num"])
            pts = pari(g)
            src = "allgens"
            out["allgens_on_curve"] = all(int(pari.ellisoncurve(E, P)) for P in pts)
        out["points_source"] = src
        W = pari.ellsaturation(E, pts, 200)
        out["gens"] = str(W)
        bt = bsd_terms(pari, E, W)
        shaA = Lstar / (pari.ellbsd(E) * bt["Reg"])
        shaB = Lstar * bt["tors"] ** 2 / (bt["Omega"] * bt["tam"] * bt["Reg"])
        out["real"] = dict(Reg=f(bt["Reg"]), tam=bt["tam"], tors=bt["tors"], Omega=f(bt["Omega"]),
                           cinf=bt["cinf"], shaA=f(shaA), shaB=f(shaB))
        # courbes 2-isogènes
        L, M = pari.ellisomat(E, 2)
        isos = []
        for i in range(1, len(L)):
            if int(M[0][i]) != 2:
                continue
            Ei_short, fi, gi = L[i]
            Ei0 = pari.ellinit(Ei_short)
            mm = pari('e->my(v); [ellminimalmodel(e,&v), v]')(Ei0)
            Ei, ch = mm[0], mm[1]
            imgs = [pari.ellchangepoint(pari.ellisogenyapply(fi, P), ch) for P in W]
            ok = all(int(pari.ellisoncurve(Ei, P)) for P in imgs)
            Wi = pari.ellsaturation(Ei, imgs, 200)
            bi = bsd_terms(pari, Ei, Wi)
            shai = Lstar * bi["tors"] ** 2 / (bi["Omega"] * bi["tam"] * bi["Reg"])
            di = pari.ellrank(Ei)
            isos.append(dict(ainv=str(pari('e->[e.a1,e.a2,e.a3,e.a4,e.a6]')(Ei)), images_on_curve=ok,
                             Reg=f(bi["Reg"]), tam=bi["tam"], tors=bi["tors"], Omega=f(bi["Omega"]),
                             sha=f(shai), descent=dict(r=int(di[0]), R=int(di[1]), s=int(di[2])),
                             ratio_sha=f(shaB / shai)))
        out["isogenous_deg2"] = isos
    except Exception as ex:
        out["error"] = repr(ex)[:300]
    out["time"] = round(time.time() - t0, 1)
    return out


def main():
    curves = load()
    with mp.get_context("spawn").Pool(int(sys.argv[2]) if len(sys.argv) > 2 else 4, initializer=init) as pool, \
            open(sys.argv[1], "w") as fo:
        for r in pool.imap_unordered(work, curves):
            fo.write(json.dumps(r, ensure_ascii=False) + "\n")
            fo.flush()
            print(r["label"], r.get("error", ""), r.get("real", {}).get("shaB"), r.get("descent"),
                  [(x["sha"], x["descent"]["s"]) for x in r.get("isogenous_deg2", [])], r.get("time"), flush=True)


if __name__ == "__main__":
    main()
