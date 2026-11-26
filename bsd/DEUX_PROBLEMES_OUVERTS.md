# Deux problèmes ouverts pour étendre la borne BSZ à 80 %

26 novembre 2026. Version fichier du doc Claude du même nom (https://claude.ai/artifact/KsnM1nQng6eF4c62LpyctY), à lire dans une autre discussion qui n'a pas accès aux docs Claude.

## Sources de référence (ce qui est acquis)

Branche `claude/artifact-review-prompt-pfjqwc` du dépôt `cowboybeblop/mistral-sandbox` :
- `bsd/lit/calcul_local_supercuspidal.md`, **§5** : tableau des six vérifications (lequel passe, lequel bloque, où dans les articles). C'est **la source de référence** sur ce qui est acquis.
- `bsd/lit/amelioration_BSZ.md` : la borne 66,99 % (conditionnelle), relecture adverse, §6–7 (verrou, types locaux, table des gains).
- `bsd/lit/inventaire_converses.md` : inventaire des théorèmes réciproques p-adiques.
- `bsd/NOTE_EXPERT.md` : note en anglais pour un spécialiste.
- Scripts : `bsd/scripts/bsz_bound.py`, `gain_table.py`, `local_densities.py`, `local_types.py`, `check_deductions.py`.

En cas de divergence entre ce fichier et `calcul_local_supercuspidal.md` §5, c'est ce dernier qui fait foi.

## Contexte et enjeu

Résoudre deux énoncés, A (local) et B (global), étendrait les réciproques p-adiques en p = 5 supersingulier aux courbes non semistables. La borne de Bhargava–Skinner–Zhang (BSZ, arXiv 1407.1826 : au moins 66,48 % des courbes, classées par hauteur, vérifient rang = rang analytique ≤ 1) passerait alors d'environ 67 % à environ 79 %.

Avec les réciproques de BSTW (arXiv 2409.01350, Th. 12.3) et de Castella (arXiv 2409.01360, Th. 1.1), la même méthode donne 66,99 % (conditionnel). Les modèles y² = x³ + Ax + B avec 5 | A et 5 ∤ B (16 % des courbes) sont supersinguliers en 5, et tous les réciproques supersinguliers connus exigent un conducteur sans facteur carré (BSTW Th. 1.6 et 12.3, Sprung 1610.10017, Castella–Wan 1607.02019). Wan, arXiv 1408.4044, p. 3 : « The square-freeness of N is put at the moment for simplicity (mainly to avoid local triple product integrals for supercuspidal representations and we may come back to remove it in the future). »

Types locaux en 2 pour ces modèles (calcul exact mod 2⁸) : semistable 0,3 % ; Steinberg tordu 0,1 % ; série principale quadratique 6,5 % ; autre, essentiellement supercuspidal, **93,1 %**.

| Réciproques supersinguliers en 5 disponibles quand les composantes en 2 et 3 sont | Borne BSZ |
|---|---|
| non ramifiées ou Steinberg (aujourd'hui) | 67,02 % |
| + série principale et Steinberg tordu | 67,55 % |
| de type quelconque en 2 et 3 | **79,03 %** |
| sans aucune condition sur le conducteur | 80,39 % |

## Problème A (local) : produit triple avec une composante supercuspidale

**Cadre.** F = ℚ_v, v = 2 ou 3, place décomposée dans le corps auxiliaire K. π = π_{E,v} supercuspidale, de caractère central trivial et de conducteur c(π) ≥ 2 ; σ_θ = π(χ_{θ,w}, χ_{θ,w̄}) avec χ_{θ,w} non ramifié et ord cond(χ_{θ,w̄}) ≥ 2c(π) + 2 ; σ_h = π(χ_{h,w}, χ_{h,w̄}), avec χ_hχ_θ|ℚ_v^× = 1 et la condition de conducteur de CLW §5.6 (iv). Par Prasad, une forme trilinéaire ℓ ≠ 0 existe (ε = −1 exigerait trois séries discrètes).

**Vecteurs imposés.** Ceux du cas (Ia) de Hsieh (arXiv 1705.02717, §6) : φ* = ξ₁ ⊗ π₂(η^{c*−c₂})ξ₂ ⊗ π₃(η^{c*−c₃})ξ₃. Le calcul de Hsieh suppose (sf), ce qui force c₁ ≤ 1. À vérifier dans CLW §7.7–7.11 : quelle représentation joue quel rôle.

**À démontrer.** ℓ(φ*) ≠ 0 (de façon équivalente, l'intégrale d'Ichino est non nulle) pour toute tordue non ramifiée de σ_θ et σ_h. CLW travaillent dans Λ ⊗ ℚ (Prop. 7.11.3) : seule la non-annulation est requise.

**Routes.**
1. Rendre σ_h minimale par un autre choix de χ_h compatible avec CLW, puis appliquer Dimitrov–Nyssen (arXiv 1005.0724, Th. 4).
2. Calcul direct par Frobenius et modèle de Kirillov (comme CLW (7.12.4)–(7.12.6)). Le vecteur nouveau supercuspidal est 1_{O^×}, et des orthogonalités de caractères ramifiés peuvent tout annuler.

## Problème B (global) : invariant μ anticyclotomique ± sans semistabilité

**Cadre.** p = 5 de bonne réduction supersingulière (a_p = 0), E[5] irréductible, K quadratique imaginaire avec p décomposé et (D_K, 2N) = 1. N = N⁺N⁻, avec N⁻ sans facteur carré (premiers multiplicatifs vérifiant (ram)) et N⁺ quelconque (contient 2⁸).

**À démontrer.** μ(L±_W(g/K)) = 0 dans le cas défini, ou l'annulation de μ de la fonction de type BDP dans le cas indéfini. Un seul des deux cas suffit.

**Où elle sert.** BSTW Th. 10.5 : redescendre la divisibilité « L°ₚ divise ξ(X°) » une fois inversés les éléments de Λ^cyc.

| Résultat | Annulation de μ | Limite |
|---|---|---|
| Pollack–Weston, Th. 1.1(2) | ±, a_p = 0, (def) | niveau sans facteur carré |
| Burungale 1504.02342 | BDP, (indef) | (H1) niveau sans facteur carré, ordinaire |
| Chida–Hsieh 1204.2427, Th. C | défini, N⁺ quelconque | ordinaire seulement |
| Burungale–Büyükboduk–Lei 2211.03722, Rem. 7.11 | abaissement du niveau (KPW17) | repose sur Pollack–Weston |

**Pistes.** (1) Adapter Chida–Hsieh au cas ±. (2) Montrer que l'hypothèse de Pollack–Weston sur N⁺ n'est que locale. (3) Éviter μ dans la version rationnelle de BSTW Th. 10.5.

## Prompt prêt à coller

```markdown
Tu es chercheur en théorie des nombres (représentations locales de GL2, théorie d'Iwasawa). Lis d'abord, sur la branche claude/artifact-review-prompt-pfjqwc du dépôt cowboybeblop/mistral-sandbox, le fichier bsd/DEUX_PROBLEMES_OUVERTS.md (cadre, notations, table des gains) puis bsd/lit/calcul_local_supercuspidal.md §5, qui est la référence sur ce qui est déjà acquis. En cas de divergence, c'est ce §5 qui fait foi. Ne refais pas ce qui y est marqué acquis.

Objectif : faire avancer le problème [A ou B, choisir un seul].

Problème A (local). F = Q_v, v = 2 ou 3. pi supercuspidale de GL2(F), caractère central trivial, conducteur c >= 2 ; sigma_theta = pi(chi1, chi2) avec chi1 non ramifié, cond(chi2) >= 2c + 2 ; sigma_h série principale avec les contraintes de Castella-Liu-Wan (arXiv 2109.08375, §5.6 (iv)). Vecteurs : cas (Ia) de Hsieh (arXiv 1705.02717, §6). Montrer que la forme trilinéaire invariante l (Prasad) ne s'annule pas sur ces vecteurs, pour toute tordue non ramifiée de sigma_theta et sigma_h. Routes : (1) rendre sigma_h minimale par un autre choix de chi_h compatible avec CLW, puis appliquer Dimitrov-Nyssen (arXiv 1005.0724, Th. 4) ; (2) calcul direct par Frobenius et modèle de Kirillov, comme CLW (7.12.4)-(7.12.6), sachant que le vecteur nouveau supercuspidal est 1_{O^x} et que des orthogonalités de caractères ramifiés peuvent tout annuler.

Problème B (global). E de bonne réduction supersingulière en p = 5 (a_p = 0), E[5] irréductible, K quadratique imaginaire, p décomposé, N = N+ N- avec N- sans facteur carré (premiers multiplicatifs vérifiant (ram)) et N+ quelconque (contient 2^8). Montrer l'annulation de mu pour la fonction L p-adique anticyclotomique +/- (cas défini, Pollack-Weston math/0610694, qui supposent N sans facteur carré), ou pour la fonction de type BDP (cas indéfini, Burungale 1504.02342, (H1)). Pistes : adapter Chida-Hsieh (arXiv 1204.2427, Th. C, N+ quelconque mais ordinaire) au cas +/-, ou montrer que l'hypothèse de Pollack-Weston sur N+ n'est que locale. Alternative : éviter mu dans la version rationnelle de BSTW (arXiv 2409.01350) Th. 10.5.

Règles non négociables :
- Ouvre chaque article avant de le citer (arXiv). Cite l'énoncé et l'endroit. Rien de mémoire présenté comme source.
- Étiquette chaque énoncé : ÉTABLI (référence ouverte), DÉDUCTION (ton raisonnement, à vérifier), CONJECTURE, SPÉCULATION.
- N'annonce jamais une preuve. Si une piste semble marcher, écris la preuve complète puis la liste des pas non justifiés, et cherche un contre-exemple, numérique si possible (PARI/GP : modèles de Kirillov, sommes de caractères mod 2^k).
- Fais une relecture adverse avant de rendre : cherche la faille comme un rapporteur hostile.
- Arrête-toi si deux étapes de suite n'apportent rien.

Livrable : une note de 3 pages au plus. Elle doit contenir l'énoncé exact obtenu ou l'obstruction trouvée, les références ouvertes, et ce qu'il faudrait faire relire par un spécialiste.
```

## Sources ouvertes

BSZ 1407.1826 ; Bhargava–Shankar 1312.7859 ; BSTW 2409.01350 ; Castella 2409.01360 ; Castella–Liu–Wan 2109.08375 ; Wan 1408.4044 ; Hsieh 1705.02717 et 1112.1580 ; Dimitrov–Nyssen 1005.0724 ; Pollack–Weston math/0610694 ; Burungale 1504.02342 ; Chida–Hsieh 1204.2427 ; Burungale–Büyükboduk–Lei 2211.03722 ; Sprung 1610.10017 ; Castella–Wan 1607.02019. Non ouverts : Prasad, Ichino, Kim–Pollack–Weston 2017, Hu 1409.8173 (résumé seulement).
