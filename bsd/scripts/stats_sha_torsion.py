"""Statistiques Ш / torsion paire par rang, fichiers allbsd de Cremona (N < 500 000)."""
import glob, collections, json
C = collections.Counter()
for f in sorted(glob.glob(__file__.rsplit('/', 2)[0] + '/data/allbsd/*')):
    for l in open(f):
        t = l.split()
        r, tors, sha = int(t[4]), int(t[5]), round(float(t[10]))
        ev = 'tors_pair' if tors % 2 == 0 else 'tors_impair'
        C[(r, ev, 'sha1' if sha == 1 else 'sha>1')] += 1
        C[(r, 'all')] += 1
out = {}
for r in range(4):
    row = {}
    for ev in ('tors_pair', 'tors_impair'):
        a, b = C[(r, ev, 'sha1')], C[(r, ev, 'sha>1')]
        row[ev] = dict(n=a + b, sha_gt1=b, frac=(b / (a + b) if a + b else None))
    out[r] = row
print(json.dumps(out, indent=1))
