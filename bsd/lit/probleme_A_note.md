# Problème A (local) : note d'étape

26 novembre 2026. Base : `bsd/lit/calcul_local_supercuspidal.md` §5 (branche `claude/artifact-review-prompt-pfjqwc`). Je ne refais pas les points 2, 3, 5 et 6, marqués acquis. **Aucune preuve n'est annoncée.**

Articles ouverts pour cette note (PDF arXiv lus) : CLW 2109.08375 ; Hsieh 1705.02717 ; Dimitrov–Nyssen 1005.0724 ; Wan 1408.4044.

## 1. Correction du §5, point 1 : les vecteurs sont ceux de Wan, pas ceux de Hsieh (Ia)

- **ÉTABLI.** CLW, preuve de la Prop. 7.11.3, liste des intégrales locales (p. 72 du PDF), pour v ∈ Σ_s ∪ {∞, ℓ} : « this is [Wan20, Lemmas 8.13-8.17]. Note that the twist at v ∈ Σ_s ∪ {ℓ} in (5.6.10) guarantees that the local integrals are nonzero constants. » Hsieh [Hsi19, Prop. 6.3] n'est cité qu'**en v = p**.
- **ÉTABLI.** Wan 1408.4044, §8, « Split Case Principal Series » (p. 80-83) : les trois représentations y sont des **séries principales** ; π₃ peut aussi être spéciale de conducteur sans facteur carré. Les vecteurs sont :
  - pour θ et h, le vecteur f_χ supporté sur K_t et valant χ₁(a)χ₂(d) ;
  - pour f, le vecteur f_{χ,ϑ}, obtenu en appliquant au vecteur nouveau l'opérateur de torsion (Lemme 8.16).
  
  C'est l'opérateur de torsion (5.6.10) de CLW : Σ_n χ_{h,v̄}(−n) R((1, n/q^t ; 0, 1)), avec t = ord cond(χ_{h,v̄}).
- **Conséquence (DÉDUCTION).** Ce n'est pas l'hypothèse (sf) de Hsieh qui exclut les supercuspidales. C'est le fait que les Lemmes 8.13 à 8.17 de Wan sont démontrés pour π_f série principale. La formulation du problème A (« vecteurs du cas (Ia) de Hsieh ») est à remplacer par celle du §3.

*Remarque (DÉDUCTION, accessoire).* Dans Hsieh, Prop. 6.3, sous-cas (a), la réduction de Ψ(W₁, W₂, f₃*) à ∫ W₁(y)W₂(−y)χ₃|·|^{-1/2}(y) d^×y n'utilise que c₁ ≤ c₂ et c₃ ≤ c₂, pas c₁ ≤ 1. Ce point n'est plus utile au problème A.

## 2. Route (1) : obstruction

Notation : à v = w w̄ décomposé, a := ord cond(χ_{θ,w̄}) ≥ 2c + 2, où c = c(π).

- **ÉTABLI.** CLW, §5.6, condition (iv) : χ_{θ,v} est non ramifié en w, ord_v̄ cond(χ_{θ,v̄}) ≥ 2 ord cond(π_v) + 2, et ord cond((χ_h χ_θ^c)_v) = ord cond(χ_{θ,v̄}) − ord cond(π_v) quand π_v est ramifiée. CLW imposent aussi χ_h χ_θ|_{A_Q^×} = 1.
- **DÉDUCTION.** Posons μ = χ_{h,w}χ_{θ,w̄}. Son conducteur vaut a − c, donc χ_{h,w} = μ χ_{θ,w̄}^{-1} a pour conducteur a. La condition sur ℚ_v^× donne ensuite cond(χ_{h,w̄}) = a − c. Ainsi σ_h = π(χ_{h,w}, χ_{h,w̄}) a pour conducteur 2a − c, alors que sa tordue minimale a pour conducteur a. **σ_h n'est jamais minimale sous (iv)**, quel que soit le choix de χ_h : (iv) fixe exactement les conducteurs.
- On peut rendre le triplet minimal au sens de Dimitrov–Nyssen (Déf. 1.1, p. 3-4, tordues η₁η₂η₃ = 1, cf. leur (2)). Il suffit de tordre π par χ_{h,w̄} et σ_h par χ_{h,w̄}^{-1}. Mais le Th. 4 de DN donne alors des vecteurs nouveaux **des représentations tordues**, qui ne sont pas les vecteurs de Wan et CLW. **La route (1) ne s'applique donc pas telle quelle.** DÉDUCTION.

## 3. Reformulation exacte du problème A

- **DÉDUCTION.** Avec les données de CLW §5.6, on a t₂ := cond(χ_{θ,1}/χ_{θ,2}) = cond(χ_{h,1}/χ_{h,2}) = a, s := cond(ϑ) = cond(χ_{h,v̄}) = a − c et t₁ := c. On retrouve exactement l'hypothèse « t₁ + s = t₂ » du Lemme 8.17 de Wan (ÉTABLI : énoncé, p. 83). **La condition (iv) de CLW est la condition de Wan, avec t₁ = c(π).**
- **Problème A′.** Soit π supercuspidale de conducteur c ≥ 2, à caractère central trivial, et φ_ϑ = Σ_n ϑ(−n) π((1, n/ϖ^s ; 0, 1)) φ_new. Il faut montrer que l'intégrale d'Ichino I_v(φ_ϑ ⊗ f_{χθ} ⊗ f_{χh}) est non nulle, pour toute tordue non ramifiée de σ_θ et σ_h. C'est le Lemme 8.17 de Wan avec π_f supercuspidale.
- **DÉDUCTION (Kirillov).** Le vecteur nouveau de π est W = 1_{O^×}, et π((1, x ; 0, 1)) multiplie W(y) par ψ(xy). On obtient W_{φ_ϑ}(y) = G(ϑ) ϑ^{-1}(−y) 1_{O^×}(y), où G(ϑ) ≠ 0 est la somme de Gauss. φ_ϑ est donc le vecteur nouveau de π ⊗ ϑ. Comme s ≥ c + 2 > c/2, son conducteur est 2s (Hsieh, Lemme 6.8, lu, pour π minimale).

## 4. Critère de non-annulation (nouveau)

Notations. Les vecteurs f_θ et f_h de Wan sont supportés sur K_t (matrices triangulaires supérieures modulo ϖ^t, c'est-à-dire K₀(ϖ^t)) et y valent χ₁(a)χ₂(d) (ÉTABLI : définition avant le Lemme 8.13, p. 81). Aux places décomposées, Wan prend g_{i,v} = 1 (ÉTABLI : Déf. 8.20, p. 85). Il n'y a donc aucun translaté, et les trois vecteurs sont « au même point ».

**Lemme (DÉDUCTION, preuve complète ci-dessous).** Soit π une représentation irréductible lisse de GL₂(ℚ_v), et soient f_θ ∈ π(χ_{θ,1}, χ_{θ,2}), f_h ∈ π(χ_{h,1}, χ_{h,2}) les vecteurs de Wan de niveau K₀(ϖ^t). Posons ρ₁ = (χ_{θ,1}χ_{h,1})^{-1}. Si c(π ⊗ ρ₁^{-1}) > t, alors ℓ(φ ⊗ f_θ ⊗ f_h) = 0 **pour tout φ ∈ π**, et pour toute tordue non ramifiée.

*Preuve.* Pour k ∈ K₀(ϖ^t), σ_θ(k)f_θ ⊗ σ_h(k)f_h = Ξ(k) f_θ ⊗ f_h, avec Ξ(k) = (χ_{θ,1}χ_{h,1})(a_k)(χ_{θ,2}χ_{h,2})(d_k). La forme ℓ est G-invariante, donc L(φ) := ℓ(φ ⊗ f_θ ⊗ f_h) vérifie L(π(k)φ) = Ξ(k)^{-1} L(φ). Ainsi L se factorise par la composante (K₀(ϖ^t), Ξ^{-1})-isotypique de π. Tordons par ρ₁^{-1} : cette composante devient l'espace des vecteurs de π ⊗ ρ₁^{-1} sur lesquels K₀(ϖ^t) agit par un caractère de d_k seul, c'est-à-dire les vecteurs fixes par K₁(ϖ^t). Par Casselman, cet espace est nul si t < c(π ⊗ ρ₁^{-1}). Les tordues non ramifiées ne changent ni Ξ sur K₀ ni les conducteurs. ∎

*Pas non justifiés.* (a) La lecture des conventions de Wan : quel caractère est « 1 », et K_t triangulaire supérieur ou inférieur. Une permutation des indices donne le même verdict (vérifié à la main). (b) Le théorème de Casselman est cité de mémoire. Il n'est pas ouvert ici, mais il est confirmé numériquement ci-dessous.

**Vérification numérique** (`bsd/scripts/k0_isotypic.py`, formule des caractères sur GL₂(ℤ/3^n)). On prend π = π(1, χ) avec χ quadratique de conducteur 1, ϑ de conducteur 2, et le type de Wan ρ₁ = χ_{f,1}ϑ, ρ₂ = χ_{f,2}ϑ^{-1}. La dimension de la composante isotypique vaut **0 en n = 2 et en n = 3**, puis **1 en n = 4**, égal à 2s. C'est exactement c(π ⊗ ρ₁^{-1}) = 2s. Le témoin sans ϑ donne les dimensions attendues 2 et 3, soit n − c + 1.

## 5. Conséquences

1. **Problème A, verdict négatif sous la lecture littérale (DÉDUCTION).** Sous CLW (iv), cond(ρ₁) vaut s = a − c ou a, selon l'appariement des indices, et ces deux valeurs dépassent c/2. On a donc c(π ⊗ ρ₁^{-1}) = 2 cond(ρ₁) ≥ 2a − 2c. C'est > a dès que a > 2c, ce que (iv) impose (a ≥ 2c + 2). Ici on utilise Hsieh, Lemme 6.8 (lu, pour π minimale) ; pour π non minimale, on se ramène à la tordue minimale. **Aucun vecteur de π, et donc aucun opérateur de torsion, ne rend ℓ non nulle.** La seule issue est de modifier les vecteurs de θ ou de h, par exemple par des translatés γ^k comme dans Dimitrov–Nyssen, Th. 4, ou la contrainte a ≥ 2c + 2. Les deux remontent dans la construction globale.
2. **Tension avec la littérature, point le plus important.** Le même lemme, appliqué tel quel au Lemme 8.17 de Wan (π_f série principale, t₁ + s = t₂, t₁ < s), donne c(π_f ⊗ ρ₁^{-1}) = 2s > t₂. L'intégrale serait donc **nulle**, alors que Wan annonce une valeur non nulle, (q_v − 1)²/q_v^{2s+1} · Vol². Le contrôle numérique ci-dessus est précisément ce cas, avec t₁ = 1, s = 2, t₂ = 3. Le même argument atteindrait aussi le cas π_v non ramifiée de CLW (iv). Il y a donc **soit une erreur dans ma lecture des vecteurs de Wan et CLW, soit une erreur dans le Lemme 8.17 de Wan.** Je ne tranche pas. Dans le premier cas, le problème A est à reformuler avec les vrais vecteurs. Dans le second, le défaut dépasse les supercuspidales.

## 6. À faire relire par un spécialiste (par priorité)

1. Les vecteurs locaux exacts de θ et h aux places décomposées. Wan, Remarque 8.19 (lue) : « The reason why the local integrals at split primes [...] are the ones considered in this subsection is a consequence of the computations in Subsection 6.7. » C'est donc **Wan §6.7** (calculs de Weil et de Fourier–Jacobi) qu'il faut lire, ainsi que CLW §7.10 ; je ne l'ai pas fait. Noter aussi que ϑ est défini par ϑ|Z_v^× = χ_h|O_{K,w}^× (Wan, Déf. 8.12). Sont-ils les f_χ de niveau K₀(ϖ^{t₂}), au même point que le vecteur de π ?
2. Si oui, le Lemme 8.17 de Wan face au lemme du §4.
3. Si non, refaire le §4 avec les vrais vecteurs. Le critère reste le même : un type compact de f_θ ⊗ f_h doit être réalisable dans π.

**Statut global : aucune preuve. Une obstruction conditionnelle à la lecture des vecteurs, et un conflit avec Wan, Lemme 8.17, à arbitrer.**

## 7. Lecture de Wan §6.7 et §8.1–8.2.1 (ajout)

- **ÉTABLI (lu).** Aux places décomposées (« Case 2 », p. 71-72), la fonction de Schwartz de θ est φ′₂(x″, x‴) = (λη)_v(x″) si x″ ∈ ℤ_v^× et x‴ ∈ ℤ_v, et 0 sinon. Celle de h (§8.2.1, p. 76) est « chosen as before except replacing η_{z,v} by η′_{z,v} ». **θ et h ont donc des fonctions de même forme.** Le vecteur de π (f_ϑ) est en revanche de forme différente (Déf. 8.22).
- **DÉDUCTION.** On suppose que le relèvement thêta local (GL₁ → GL₂, cas déployé) envoie φ′ sur la section de Godement f(g) = ∫ Φ((0, t)g)·(…)(t) d^×t. Dans ce cas, le vecteur associé à 1_{O^×}·ξ ⊗ 1_O est propre pour un sous-groupe de type K₀(ϖ^{cond ξ}). Les vecteurs de θ et h sont alors propres pour **le même** sous-groupe K₀(ϖ^a), et le lemme du §4 s'applique : obstruction.
- **Point non tranché, et décisif.** Les opérateurs d'entrelacement δ_ψ (transformées de Fourier partielles entre les polarisations X′ et X) peuvent échanger les deux orientations, K₀ (coin inférieur gauche) et K₀ᵀ (coin supérieur droit). Si θ et h se retrouvent d'orientations **opposées**, le groupe qui fixe f_θ ⊗ f_h est de niveau total 2a. Le critère du §4 devient 2·cond(ρ₁) ≤ 2a, qui est satisfait, **et l'obstruction tombe**. Je ne peux pas trancher sans refaire les conventions de Weil de Wan §2 et §6, et elles sont elles-mêmes en partie implicites.
- **Indice en faveur d'orientations opposées.** Sinon, le lemme du §4 annulerait aussi l'intégrale de CLW aux places où π_v est **non ramifiée** (Lemme 8.16 de Wan). Tout le cas semistable déjà publié serait faux. C'est peu probable, mais ce n'est pas une preuve.

## 8. Résultat trouvé dans la littérature : Fouquet–Wan (arXiv 2107.13726)

- **ÉTABLI (lu, p. 95).** Fouquet–Wan, *The Iwasawa Main Conjecture for universal families of modular motives* (preprint, v3 du 8 avril 2022), §7 : « to remove the square-free conductor assumption in [Wan, 1408.4044] for prime divisors of N split in K, we compute here a local triple product integral below for supercuspidals ».
  - **Prop. 7.27.** Soit π_ℓ supercuspidale, de caractère central trivial et de conducteur ℓ^t avec t ≥ 2, et φ_ℓ son vecteur nouveau. Alors le coefficient matriciel Φ est nul sur les cellules diag(ℓⁿ, 1)(…)K_t et diag(1, ℓⁿ)(…)K_t pour n ≠ 0, et vaut 1 pour n = 0. Les auteurs le déduisent de « [60, Proposition 3.1] ».
  - **Cor. 7.28.** Soient π_h = π(χ_{h,1}, χ_{h,2}) et π_θ = π(χ_{θ,1}, χ_{θ,2}), avec des caractères de conducteur ℓ^{t₁}, **t₁ > t**, tels que **χ_{h,1}χ_{θ,1} et χ_{h,2}χ_{θ,2} soient non ramifiés**. Prenons les vecteurs f_χ de Wan §8D. Alors I_ℓ(φ_ℓ ⊗ f_{χθ} ⊗ f_{χh}, …) = Vol(K_{t₁}) ≠ 0. Cette valeur ne dépend pas des tordues non ramifiées.
  - **Th. 7.32.** Conjecture principale de Greenberg sur K pour f, avec ρ̄_f|G_{ℚ_p} absolument irréductible ou f ordinaire. Les premiers non décomposés q doivent vérifier q ‖ N, et 2 non décomposé impose 2 ‖ N. **Aucune hypothèse sur les premiers décomposés.** Divisibilité « up to height one primes which are pullbacks of primes in O[[Γ⁺]] ».
- **Cohérence avec le §4 (DÉDUCTION).** Avec χ_{θ,1}χ_{h,1} non ramifié, ρ₁ est non ramifié. Le critère du §4 devient c(π) = t ≤ t₁, qui est satisfait. Fouquet–Wan choisissent donc précisément les données auxiliaires qui passent le critère. **Le lemme du §4 et leur résultat sont compatibles**, et le §5.1 se lit ainsi : la recette (iv) de CLW est la mauvaise pour une π supercuspidale, la bonne est celle de Fouquet–Wan.
- **Ce que cela change pour le problème A (DÉDUCTION).** Le calcul local est fait dans la littérature, pour le vecteur nouveau de π et des données auxiliaires adaptées. BSTW citent Fouquet–Wan ([56], p. 10), mais seulement comme application, pas pour ce calcul. Le problème A devient : **dans CLW, peut-on remplacer la condition (iv) aux places supercuspidales par celle de Fouquet–Wan**, sans casser les autres usages de χ_θ et χ_h ? Ces usages sont : le Lemme 6.24 de Wan (cond(λ) < cond(χ_θ) < ord(yȳ)), la condition (vi) de CLW (valeurs L unités p-adiques), les fonctions L₁ à L₆, et la twist (5.6.10), qui n'est plus nécessaire avec le vecteur nouveau. Fouquet–Wan font ce remplacement dans le cadre de Wan (même méthode Klingen–Eisenstein, même §8D). C'est un fort indice que l'adaptation à CLW (cas supersingulier anticyclotomique) est routinière, mais **ce n'est pas vérifié**.
- **Piste parallèle (SPÉCULATION).** Le Th. 7.32 de Fouquet–Wan pourrait peut-être remplacer directement l'entrée de CLW dans BSTW pour p = 5 supersingulier, puisque ρ̄|G_{ℚ_p} est irréductible quand a_p = 0. Ses exceptions (« pullbacks of primes in O[[Γ⁺]] ») rappellent l'étape d'inversion de Λ^cyc dans BSTW Th. 10.5, donc le problème B. À examiner.
- **Statut de la source.** Fouquet–Wan est un preprint, sans journal-ref sur arXiv au moment de la lecture. La Prop. 7.27 s'appuie sur [60, Prop. 3.1], que je n'ai pas ouvert.
