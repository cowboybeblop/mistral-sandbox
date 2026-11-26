"""Test de « l'absorption » de Ш[2] par isogénie, par rang, sur les fichiers allbsd (N < 500 000).
Pour chaque courbe à torsion paire et Ш analytique pair, on regarde si sa classe d'isogénie
contient une courbe avec v_2(Ш) strictement plus petit. (Test de classe : les degrés des
isogénies ne sont pas dans allbsd ; la mission 3 vérifie la 2-isogénie elle-même en rang 2.)"""
import glob, collections, json, math
classes = collections.defaultdict(list)
for f in sorted(glob.glob(__file__.rsplit('/', 2)[0] + '/data/allbsd/*')):
    for l in open(f):
        t = l.split()
        classes[(t[0], t[1])].append((int(t[4]), int(t[5]), round(float(t[10]))))
v2 = lambda n: (n & -n).bit_length() - 1
C = collections.Counter(); ex = collections.defaultdict(list)
for k, cs in classes.items():
    r = cs[0][0]
    mins = min(v2(s) for _, _, s in cs)
    for (_, tors, sha) in cs:
        if tors % 2 == 0 and sha % 2 == 0:
            C[(r, 'n')] += 1
            if v2(sha) > mins: C[(r, 'absorbed')] += 1
            else:
                C[(r, 'not')] += 1
                if len(ex[r]) < 3: ex[r].append(f"{k[0]}{k[1]} {cs}")
print(json.dumps({r: dict(n=C[(r, 'n')], absorbed=C[(r, 'absorbed')], not_absorbed=C[(r, 'not')], examples=ex[r]) for r in range(4)}, indent=1))
