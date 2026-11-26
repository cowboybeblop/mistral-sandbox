"""Synthèse de la mission 2 : résultats p-adiques et certification."""
import json, sys, collections
res = [json.loads(l) for l in open(sys.argv[1])]
cert = {json.loads(l)["label"]: json.loads(l) for l in open(sys.argv[2])} if len(sys.argv) > 2 else {}
meta = json.load(open(sys.argv[1] + ".meta.json"))
print("graine", meta["seed"], "échantillon", len(meta["labels"]), "parmi", meta["population"])
err = [r for r in res if "error" in r]
print("échecs (comptés comme échecs) :", len(err), [(r["label"], r["error"][:80]) for r in err])
ok = [r for r in res if "error" not in r]
print("courbes traitées :", len(ok))
real_ok = sum(abs(r["real"]["shaA"] - 1) < 1e-8 and abs(r["real"]["shaB"] - 1) < 1e-8 for r in ok)
print("Ш réel = 1 (deux voies) :", real_ok, "/", len(ok))
print("Ш Cremona = 1 :", sum(abs(r["crem"]["Sha"] - 1) < 1e-8 for r in ok))
print("régulateur = Cremona (1e-8 rel.) :", sum(abs(r["real"]["Reg"] - r["crem"]["Reg"]) < 1e-8 * r["real"]["Reg"] for r in ok))
byp = collections.defaultdict(list)
for r in ok:
    for x in r["padic"]:
        byp[x["p"]].append(x)
tot = 0
print("p  couples  min/médiane/max chiffres d'accord avec Ш=1   désaccord mod p   anormaux")
for p in sorted(byp):
    L = byp[p]; tot += len(L)
    a = sorted(x["agree_real_digits"] for x in L)
    print(p, len(L), a[0], a[len(a) // 2], a[-1], sum(1 for v in a if v < 1), sum(x["anomalous"] for x in L))
print("couples (E, p) au total :", tot, " courbes avec >= 1 premier :", sum(1 for r in ok if r["padic"]))
print("courbes avec >= 8 chiffres pour au moins un p :", sum(1 for r in ok if any(x["agree_real_digits"] >= 8 for x in r["padic"])))
if cert:
    C = collections.Counter()
    for lab, c in cert.items():
        for x in c.get("certs", []):
            C["couples"] += 1
            C["ord<=2 certifié"] += x["ord_le_2"]
            C["E[p] irréductible"] += bool(x["irreducible"])
            C["certifié et irréductible"] += x["ord_le_2"] and bool(x["irreducible"])
            C["c0 exactement nul"] += x["c0_exact_zero"]
    for k in C: print(k, C[k])
    curves = [lab for lab, c in cert.items() if any(x["ord_le_2"] and x["irreducible"] for x in c.get("certs", []))]
    print("courbes avec au moins un p certifié et E[p] irréductible :", len(curves))
    print("dénominateurs D rencontrés :", collections.Counter(c.get("D") for c in cert.values()))
