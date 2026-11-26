"""BSD p-adique (sommes de Riemann MTT) sur une courbe de rang 2 et Ш = 4 de grand conducteur.
Usage : python3 padic_big.py LABEL p:n [p:n ...]   (générateurs lus dans results/m3_sha4_rank2.jsonl)"""
import json, sys, time
sys.path.insert(0, sys.path[0])
import mission2_padic as m2
m2.init()
pari = m2._pari
label = sys.argv[1]
r = next(json.loads(l) for l in open(sys.path[0] + '/../results/m3_sha4_rank2.jsonl') if json.loads(l)['label'] == label)
ainv = next(json.loads(l.split()[3]) for l in open(sys.path[0] + '/../data/rank2_sha_ge4.txt') if ''.join(l.split()[:3]) == label)
E = pari.ellinit(ainv); W = pari(r['gens']); re = r['real']
t = time.time(); MS = pari.msfromell(E, 1); print(label, 'msfromell %.0fs' % (time.time() - t), flush=True)
D = int(pari('(M,x)->denominator(mseval(M,x))')(MS[0], MS[1]))
out = dict(label=label, N=r['N'], D=D, msfromell_s=round(time.time() - t), res=[])
for spec in sys.argv[2:]:
    p, n = map(int, spec.split(':'))
    t = time.time()
    shaN, info = m2.padic_sha(pari, E, MS, W, p, n, re['cinf'], re['tam'], re['tors'])
    shaM, _ = m2.padic_sha(pari, E, MS, W, p, n - 1, re['cinf'], re['tam'], re['tors'])
    d = shaN - shaM; e = shaN - 4
    irr = len(pari.ellisomat(E, p, 1)[0]) == 1
    res = dict(p=p, n=n, digits_levels=int(pari.valuation(d, p)) if d != 0 else None,
               agree_with_4=int(pari.valuation(e, p)) if e != 0 else None,
               bound=n - 1 - int(pari.valuation(D, p)), irreducible=irr, sha_p=str(shaN)[:100],
               time=round(time.time() - t), **info)
    out['res'].append(res); print(res, flush=True)
with open(sys.path[0] + '/../results/m3_padic_%s.json' % label, 'w') as f: json.dump(out, f, indent=1)
