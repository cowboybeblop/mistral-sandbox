"""Synthèse du test BSD p-adique sur tordues quadratiques (twist_bsd.py).
Jeu de calibrage : Ш réel = 1 (fixe le facteur u). Jeu de test : Ш réel > 1, non utilisé au calibrage."""
import json, sys, collections
R = [json.loads(l) for l in open(sys.argv[1])]
C = collections.Counter()
for r in R:
    C["rang_an=%s" % r.get("rank_an")] += 1
    if "error" in r:
        C["échec : " + r["error"][:40]] += 1
print("tordues traitées :", len(R)); [print("  ", k, v) for k, v in sorted(C.items())]
ok = [r for r in R if "padic" in r]
far = [r for r in ok if abs(r["sha_real"] - round(r["sha_real"])) > 1e-6]
print("Ш réel non entier (à 1e-6) :", len(far), [(r["D"], r["sha_real"]) for r in far][:5])
print("Ш réel :", sorted(collections.Counter(round(r["sha_real"]) for r in ok).items()))
for name, sel in (("calibrage (Ш = 1)", lambda r: round(r["sha_real"]) == 1), ("test (Ш > 1)", lambda r: round(r["sha_real"]) > 1)):
    S = [r for r in ok if sel(r)]
    pairs = [(r, x) for r in S for x in r["padic"] if "agree_digits" in x and x.get("r", 2) == 2]
    insuf = [(r["D"], x["p"]) for r in S for x in r["padic"] if x.get("insufficient_precision") or ("agree_digits" in x and x.get("r", 2) != 2)]
    errs = [(r["D"], x["p"]) for r in S for x in r["padic"] if "error" in x]
    bad = [(r["base"], r["D"], round(r["sha_real"]), x["p"], x["sha_p"][:30]) for r, x in pairs if x["agree_digits"] < 1]
    print(f"\n{name} : {len(S)} tordues, {len(pairs)} couples (E_D, p), échecs p-adiques {len(errs)}, précision insuffisante (r != 2) {len(insuf)}")
    print("  désaccords mod p :", len(bad), bad[:8])
    byp = collections.defaultdict(list)
    for r, x in pairs: byp[x["p"]].append(x["agree_digits"])
    for p in sorted(byp):
        a = sorted(byp[p]); print(f"  p={p}: {len(a)} couples, chiffres min/méd/max {a[0]}/{a[len(a)//2]}/{a[-1]}")
    print("  u :", collections.Counter(r["u"] for r in S))
    if name.startswith("test"):
        div = [(r["base"], r["D"], round(r["sha_real"]), x["p"], x["v_sha_p"], x["agree_digits"]) for r, x in pairs if round(r["sha_real"]) % x["p"] == 0]
        print("  cas p | Ш (la p-partie de Ш doit sortir) :", len(div))
        for d in div[:20]: print("    ", d)
