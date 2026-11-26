"""Seconde passe de la mission 2 sur les courbes qui ont échoué (pile PARI de 2 Go dépassée
dans msfromell), avec 6 Go de pile et 2 processus. Usage :
python3 mission2_rerun.py ENTREE.jsonl SORTIE.jsonl"""
import json, sys, multiprocessing as mp
sys.path.insert(0, sys.path[0])
import mission2_padic as m2

def init6():
    from cypari import pari
    pari.allocatemem(6 * 10**9)
    pari.set_real_precision(38)
    pari('read("%s")' % (sys.path[0] + "/mtt.gp"))
    m2._pari = pari

if __name__ == "__main__":
    failed = [json.loads(l) for l in open(sys.argv[1]) if '"error"' in l]
    cvs = [dict(label=r["label"], N=r["N"], ainv=r["ainv"], crem=r["crem"]) for r in failed]
    with mp.get_context("spawn").Pool(2, initializer=init6) as pool, open(sys.argv[2], "w") as f:
        for r in pool.imap_unordered(m2.work, cvs):
            r["second_pass"] = True
            f.write(json.dumps(r, ensure_ascii=False) + "\n"); f.flush()
            print(r["label"], r.get("error", ""), [(x["p"], x["agree_real_digits"]) for x in r.get("padic", [])], flush=True)
