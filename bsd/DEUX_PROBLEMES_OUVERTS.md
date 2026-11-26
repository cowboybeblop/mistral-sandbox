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

**Vecteurs imposés (corrigé).** Ce sont ceux de Wan, Lemmes 8.13–8.17 (cités par CLW, preuve de la Prop. 7.11.2) : pour θ et h, des vecteurs supportés sur K_t se transformant par un caractère ; pour π, le vecteur nouveau tordu par (5.6.10) de CLW. La condition (iv) de CLW est t₁ + s = t₂ du Lemme 8.17, avec t₁ = c(π). Pour π série principale, ce lemme donne I_v = (q − 1)²/q^{2s+1}·Vol(K₁)·Vol(K_{t₂})² ≠ 0. **Le problème A est l'analogue du Lemme 8.17 pour π supercuspidale.**

**À démontrer.** ℓ(φ*) ≠ 0 (de façon équivalente, l'intégrale d'Ichino est non nulle) pour toute tordue non ramifiée de σ_θ et σ_h. CLW travaillent dans Λ ⊗ ℚ (Prop. 7.11.3) : seule la non-annulation est requise.

**Routes.**
1. ~~Rendre σ_h minimale puis appliquer Dimitrov–Nyssen~~ : **bloqué**, car (iv) fixe les conducteurs des caractères de χ_h à a et a − c, donc σ_h n'est jamais minimale.
2. Calcul direct : le vecteur de π est ϑ⁻¹(−y)·1_{O^×}(y) dans le modèle de Kirillov, soit le vecteur nouveau de π ⊗ ϑ, de conducteur 2s. L'argument de support exige a ≤ 2c, exclu par CLW (a ≥ 2c + 2) : il faut la fonction de Bessel de π ⊗ ϑ. Test numérique proposé : v = 3, c = 2, a = 6, s = 4, **calibré d'abord sur le Lemme 8.17 avec π série principale**.

## Problème B (global) : invariant μ anticyclotomique ± sans semistabilité — refondu le 26 novembre 2026

**Ce qu'il faut exactement.** Dans la preuve du Th. 10.5 de BSTW, cas (def) (ν(N⁻) impair, chaque q | N⁻ vérifiant (ram)), il faut μ(L°,ac_p(g/L)) = 0 pour la fonction L p-adique anticyclotomique ±, avec la **normalisation de BSTW** (période canonique). BSTW l'obtiennent via (L°,ac_p) = (∏_{q|N⁻} c_q · L°_W), où L°_W est normalisée par la période de Gross, et via μ(L°_W) = 0 (Pollack–Weston [PW]). ÉTABLI (lecture de BSTW §10.2.2).

**On ne peut pas contourner μ, même rationnellement** (DÉDUCTION). La divisibilité est d'abord obtenue après inversion de Λ^cyc. Si un premier de hauteur 1 de Λ^cyc, (g(T_cyc)) avec g distingué ou g = p, divisait L°, alors L°,ac = g(0)·h avec g(0) ∈ pℤ_p, d'où μ(L°,ac) ≥ 1. C'est μ(L°,ac) = 0 qui exclut tous ces premiers. *L'ancienne piste « éviter μ » est abandonnée.*

**Décomposition (lecture de PW, arXiv math/0610694, §2.3–2.4 et §6).** Le besoin se coupe en deux.

- **(B1) μ(L±_W) = 0 pour la normalisation de Gross.** C'est PW, Th. 2.5(1), dont la preuve dit : « The results of [32] (Vatsal) extend easily to the supersingular case ». Ce sont les arguments d'équidistribution de Vatsal (points CM sur l'algèbre de quaternions définie, Ratner), appliqués aux éléments thêta ± de Darmon–Iovita. Chida–Hsieh (1204.2427, Th. C) font ce type d'argument avec **N⁺ quelconque**, mais en réduction ordinaire. **Probablement accessible, À VÉRIFIER** : relire Vatsal (Duke 2003, non ouvert ici) pour l'hypothèse sur N⁺, puis Darmon–Iovita pour la construction ± en niveau N⁺ quelconque.
- **(B2) La comparaison des périodes : η_f(N) ~ ξ_f(N⁺, N⁻).** Chez PW, c'est le Th. 6.8, dont la preuve passe par la Prop. 6.5 (isomorphisme de Ribet), la Prop. 6.7, le Th. 6.2 (liberté) et le résultat principal de Ribet–Takahashi [28, 29], le tout en niveau sans facteur carré. **Sous (ram) en tout q | N⁻, cela se simplifie** (DÉDUCTION) :
  - (i) η_f(N) = η_f(N⁺, N⁻) : toute forme congruente à f est nouvelle aux q | N⁻ (argument de PW dans la preuve de la Prop. 6.7) ;
  - (ii) ξ_f(N⁺, N⁻) = η_f(N⁺, N⁻) : c'est la **liberté de M = Pic(X_{N⁺,N⁻}) ⊗ O localisé en m sur l'algèbre de Hecke** (PW, Th. 6.2 et Prop. 6.4, prouvés en niveau sans facteur carré via Wiles [34, Th. 2.1] et Helm [18]).

**Le cœur de B est donc (B2)(ii) : un théorème de multiplicité un** pour l'algèbre de quaternions définie de discriminant N⁻, en niveau d'Eichler N⁺ non sans facteur carré, localisé en un idéal maximal non d'Eisenstein vérifiant (CR).

**Indice favorable** (DÉDUCTION). En 2 et en 3, l'inertie de nos courbes a un ordre premier à 5 (2, 3, 4, 6, 8, 12 ou 24). Le conducteur de ρ̄ = E[5] y est donc celui de ρ : **N⁺ est ρ̄-minimal**. C'est le cadre où la multiplicité un est en général attendue, voire connue (méthode de Taylor–Wiles et Diamond ; résultats de liberté en niveau minimal). La littérature n'a pas été vérifiée ici.

**À démontrer (version refondue).**
- (B1) μ(L±_W(g/K)) = 0, pour a_p = 0, p décomposé dans K, N⁻ sans facteur carré avec ν(N⁻) impair et (ram), et N⁺ quelconque.
- (B2) Pic(X_{N⁺,N⁻})_m ⊗ O est libre de rang 1 sur T_m, pour N⁺ ρ̄-minimal non sans facteur carré, sous (CR). Ou, plus faiblement, ξ_f = η_f(N⁺, N⁻) à une unité près.

| Résultat | Ce qu'il donne | Limite pour nous |
|---|---|---|
| Pollack–Weston, Th. 2.5(1) | (B1) pour a_p = 0 | énoncé en niveau sans facteur carré ; preuve « Vatsal s'étend » |
| Pollack–Weston, Th. 6.2 et 6.8 | (B2) | niveau sans facteur carré (Wiles, Helm, Ribet–Takahashi) |
| Chida–Hsieh, Th. C | (B1)-type, N⁺ quelconque | ordinaire seulement |
| Burungale (1504.02342) | cas (indef) | (H1) niveau sans facteur carré |
| Burungale–Büyükboduk–Lei, Rem. 7.11 | abaissement du niveau (KPW17) | repose sur PW |

**Pistes, par ordre de priorité.** (1) Chercher un théorème de liberté (multiplicité un) en niveau ρ̄-minimal pour les algèbres de quaternions définies : Diamond, Taylor, Helm, et la littérature sur « freeness of Hecke modules ». C'est (B2)(ii). (2) Vérifier que l'équidistribution de Vatsal et la construction ± de Darmon–Iovita valent pour N⁺ quelconque : c'est (B1). (3) Vérifier que l'identité (L°,ac_p) = (∏ c_q · L°_W) de BSTW se réduit bien à (B2)(i)–(ii) sous (ram).

## Prompt prêt à coller

```markdown
Tu es chercheur en théorie des nombres (représentations locales de GL2, théorie d'Iwasawa). Lis d'abord, sur la branche claude/artifact-review-prompt-pfjqwc du dépôt cowboybeblop/mistral-sandbox, le fichier bsd/DEUX_PROBLEMES_OUVERTS.md (cadre, notations, table des gains) puis bsd/lit/calcul_local_supercuspidal.md §5, qui est la référence sur ce qui est déjà acquis. En cas de divergence, c'est ce §5 qui fait foi. Ne refais pas ce qui y est marqué acquis.

Objectif : faire avancer le problème [A ou B, choisir un seul].

Problème A (local). F = Q_v, v = 2 ou 3. pi supercuspidale de GL2(F), caractère central trivial, conducteur c >= 2 ; sigma_theta = pi(chi1, chi2) avec chi1 non ramifié, cond(chi2) >= 2c + 2 ; sigma_h série principale avec les contraintes de Castella-Liu-Wan (arXiv 2109.08375, §5.6 (iv)). Vecteurs : cas (Ia) de Hsieh (arXiv 1705.02717, §6). Montrer que la forme trilinéaire invariante l (Prasad) ne s'annule pas sur ces vecteurs, pour toute tordue non ramifiée de sigma_theta et sigma_h. Routes : (1) rendre sigma_h minimale par un autre choix de chi_h compatible avec CLW, puis appliquer Dimitrov-Nyssen (arXiv 1005.0724, Th. 4) ; (2) calcul direct par Frobenius et modèle de Kirillov, comme CLW (7.12.4)-(7.12.6), sachant que le vecteur nouveau supercuspidal est 1_{O^x} et que des orthogonalités de caractères ramifiés peuvent tout annuler.

Problème B (global, refondu). E de bonne réduction supersingulière en p = 5 (a_p = 0), E[5] irréductible, K quadratique imaginaire, p décomposé, N = N+ N- avec N- sans facteur carré, nu(N-) impair, chaque q | N- vérifiant (ram), et N+ quelconque (contient 2^8, rhobar-minimal). Il faut mu = 0 pour la fonction L p-adique anticyclotomique +/- normalisée comme BSTW (arXiv 2409.01350, §10.2.2). Contourner mu est impossible (voir le fichier). Cela se coupe en (B1) mu(L+/-_W) = 0 pour la normalisation de Gross : Pollack-Weston math/0610694 Th. 2.5(1) via Vatsal, Chida-Hsieh 1204.2427 Th. C pour N+ quelconque en ordinaire ; et (B2) la comparaison des périodes eta_f(N) ~ xi_f(N+,N-), qui sous (ram) se réduit à la liberté de Pic(X_{N+,N-}) localisé en m sur l'algèbre de Hecke (multiplicité un), prouvée par PW (Th. 6.2) en niveau sans facteur carré seulement. Priorité : chercher un théorème de multiplicité un en niveau rhobar-minimal pour les algèbres de quaternions définies, puis vérifier (B1) pour N+ quelconque.

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
