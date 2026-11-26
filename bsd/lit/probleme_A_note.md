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

## 9. Avancées du 26 novembre (suite) : vérification de Fouquet–Wan et test des lemmes de Wan

### 9.1 FW Prop. 7.27 démontrée pour tout ℓ, y compris ℓ = 2 (DÉDUCTION, preuve complète)

On travaille dans le modèle de Kirillov de π, supercuspidale de conducteur c et de caractère central trivial, avec le vecteur nouveau W₀ = 1_{O^×}. On utilise la formule de Hu (IMRN 2018, (2.66), lue dans la version publiée fournie) : π(ω)1_{χ,n} = C·1_{χ^{-1}w₀^{-1}, −n+n_χ}, avec n_1 = −c pour χ trivial.
- **Cellules diag(ℓⁿ, 1)n(ℓ^{-n}y)K_t.** On a diag(ℓⁿ, 1)n(ℓ^{-n}y) = n(y)diag(ℓⁿ, 1), donc Φ = ∫ψ(yα)W₀(ℓⁿα)W₀(α)d^×α. Ce n'est non nul que si les supports O^× et ℓ^{-n}O^× se rencontrent, c'est-à-dire n = 0. Pour n = 0, Φ = ∫_{O^×}ψ(yα) = 1 si y ∈ O.
- **Cellules diag(1, ℓⁿ)n⁻(ℓ^{t−n}x)K_t.** À un élément central près, c'est diag(ℓ^{-n}, 1)n⁻(ϖ^iu) avec i = t − n et m = 0.
  - On écrit π(n⁻(ϖ^i)) = π(ω^{-1})π(n(−ϖ^i))π(ω).
  - π(ω)W₀ est porté par la couche v = −c. On le multiplie par ψ(−ϖ^ix), puis on décompose sur les caractères de O^×.
  - Sous π(ω^{-1}), **seule la composante triviale** donne une composante triviale, sur la couche c + n_1 = 0. Les autres caractères χ restent non triviaux.
  - Avec m = 0, Φ(diag(a, 1)n⁻(ϖ^i)) = ∫_{v(α)=0}W^{(i)}(aα)d^×α ne voit que la composante triviale. Elle est non nulle seulement si v(a) = 0, c'est-à-dire n = 0.
- **Conclusion.** On n'utilise que n_1 = −c, qui est la définition du conducteur. **On n'utilise pas la Prop. 2.9 de Hu**, affaiblie pour p = 2 et i = c/2. La réserve du rapport (cas 2⁸) **tombe**.

### 9.2 Le Lemme 8.13 de Wan, confirmé numériquement

Script `bsd/scripts/wan_lemma813.py`, avec p = 3, t = 2, χ₁ non ramifié, cond χ₂ = 2, paramètres non ramifiés génériques. On calcule Φ par l'intégrale à une variable dans la carte n⁻(y) de B\G.
- Sur K₁wσ_nK₁ et K₁σ_nwK₁, Φ = 0 pour n ≤ 3, à 10⁻¹⁵ près.
- Sur K₁σ_nK₁ et K₁wσ_nwK₁, les valeurs coïncident avec Vol(K_t)·α_i^n·3^{-n/2} à 4 décimales : n = 1 : 0,0517 et 0,0844 ; n = 2 : 0,0641 ; n = 3 : 0,0112 et 0,0486.
- **Avec 9.1, cela établit FW Cor. 7.28 (DÉDUCTION vérifiée).** Φ_π s'annule sur toutes les cellules n ≠ 0 où Φ_θΦ_h ≠ 0. Sur K_{t₁}, Φ_π = 1 (t₁ > t) et Φ_θΦ_h = Vol²·(χ_{θ,1}χ_{h,1})(a)(χ_{θ,2}χ_{h,2})(d), qui est trivial par la condition de FW. Donc I = Vol(K_{t₁}), **indépendant des tordues non ramifiées**.

### 9.3 Le Lemme 8.14 de Wan, contredit numériquement

Script `bsd/scripts/wan_lemma814.py`, avec p = 3, t₁ = 1, s = 2, t₂ = 3, et f = f_{χ,ϑ} défini par f(b·n⁻(y)) = χ(b)δ^{1/2}(b)ϑ(y/p^{t₁})·1[v(y) = t₁].
- Lemme 8.14, énoncé : « if g ∈ K_{t+s} with Φ(g) ≠ 0, then its upper right entry is divisible by ϖ^{s−t} ».
- Calcul : Φ_f(n(b)) = **−1/9 ≠ 0** pour b ∈ {1, 2, 4} (unités), et 2/9 pour v(b) ≥ 1.
- La projection sur le type (K₀(p^{t₂}), Ξ^{-1}) vaut Σ_{b mod p^{s−t₁}} Φ_f(n(b)) = **0** exactement, comme le prédit le lemme du §4. On a vérifié par ailleurs que la dimension isotypique est nulle (`k0_isotypic.py`).
- **Conséquence (DÉDUCTION).** Dans la configuration du Lemme 8.17 de Wan (vecteurs f_χ de θ et h au même point, type Ξ sur K₀(p^{t₂})), l'intégrale d'Ichino est **nulle**, contrairement à la valeur annoncée. Deux explications possibles :
  - (a) les vecteurs locaux de θ et h produits par la construction globale (Schwartz de CLW Prop. 7.6.1 et Wan §6.7) ne sont pas ces f_χ, par exemple parce que leurs orientations sont opposées ;
  - (b) le Lemme 8.17 (et 8.14) est erroné. L'enjeu dépasse alors le cas supercuspidal : les places déployées de CLW dans le cas semistable seraient touchées.
  
  Le fait que FW passent, pour les supercuspidales, à des données (vecteur nouveau, χ_{h,i}χ_{θ,i} non ramifiés) qui satisfont le critère est compatible avec les deux hypothèses.
- **Réserve.** Ma lecture de f_{χ,ϑ} suppose le support c/ϖ^{t₁} unité, ce qu'impose la lissité en c = 0. Si Wan définit f_{χ,ϑ} autrement, le test ne s'applique pas.

### 9.4 Compatibilité du remplacement de (iv) dans CLW (DÉDUCTION, sur lecture de CLW)

- **Où sert (iv).** Les seules occurrences de la condition (iv) et de cond((χ_hχ_θ^c)_v) aux places de Σ_s sont la définition (p. 35) et l'intégrale triple locale (via Wan 8.13–8.17, p. 72). La relation « a − c » est exactement t₁ + s = t₂ du Lemme 8.17.
- **Facteurs L locaux.** Les valeurs L de (vi) et de (5.6.1)–(5.6.5), comme le facteur global L(1/2, BC(π) × χ_hχ_θλ²)L(1/2, BC(π) × χ_hχ_θ^c) (7.5.12), n'ont en v ∈ Σ_s supercuspidal que des facteurs locaux égaux à 1, puisque π_v ⊗ (caractère) reste supercuspidale. La constante C₂ (p. 72-73) reste non nulle : L_v(1/2, Π) = 1 et L_v(1, Π, Ad) est fini non nul et indépendant de τ.
- **Contraintes qui restent.** La première clause de (iv), « χ_{θ,v} non ramifié », est **imposée** par la fonction de Schwartz de θ (CLW Prop. 7.6.1 : 1_{O_{K,v}}(y₁)·1_{O^×}(y₂)χ_{θ,v̄}λ_{v̄}(y₂)). La condition de FW reste compatible avec elle : il suffit que χ_h compense χ_θ composante par composante. La torsion (5.6.10) devient inutile, puisque le vecteur nouveau est de nebentypus trivial et que le type de θ ⊗ h sur K_{t₁} est trivial.
- **Reste à vérifier.** (i) L'appariement des indices 1 et 2 de FW avec w et w̄ (question 2 à Wan). (ii) La fonction de Schwartz de h dans CLW (p. 65 ; extraction texte confuse : 1_{ℤ_v}(y₁)·1_{ℤ_v^×}(y₂)·χ_{h,v}^{-1}χ_{h,v̄}^{-1}λ_{v̄}(y₂) ?). (iii) Le point (a)/(b) du §9.3.

## 10. Relecture et recherche web (26 novembre, suite)

- **Définition de f_{χ,ϑ}, relue sur l'image de la page 82 (ÉTABLI).** « f = f_{χ,ϑ}(k_v) = χ₁(a)χ₂(d)ϑ(c/ϖ_v^t), a, d ∈ ℤ_v^×, b ∈ ℤ_v, **c ∈ ϖ_v^tℤ_v^×** ; 0 otherwise », pour k_v = (a b ; 0 d)(1 0 ; c 1). C'est la lecture utilisée dans les scripts.
- **Contre-vérification indépendante** (`wan_lemma814_fini.py`, somme exacte sur GL₂(ℤ/27)). Φ(n(b))/Φ(1) = −1/2 pour b unité et 1 pour v(b) ≥ 1, et Σ_{b mod 3} Φ(n(b)) = 0. Les deux méthodes concordent. **L'énoncé de support du Lemme 8.14 (« if g ∈ K_{t+s} with Φ(g) ≠ 0, then its upper right entry is divisible by ϖ^{s−t} ») est faux pour le vecteur tel que défini.** Ce n'est pas une erreur de lecture de la définition. La preuve de Wan (« we easily see that b is divisible by ϖ^{s−t} ») ne détaille pas ce pas.
- **Recherche web.** Aucun erratum ni discussion des Lemmes 8.14 et 8.17 trouvés. La version publiée (ANT 14 (2020), https://msp.org/ant/2020/14-2/ant-v14-n2-p04-p.pdf) est bloquée par le réseau de la session ; l'utilisateur peut la télécharger pour comparaison. Le Lemme 5.1 de Wan 1411.6352 porte sur la place p, pas sur les places déployées.
- **Indice sur les conventions (ÉTABLI, lu).** BSTW, note 19 (preuve du Th. 9.21, argument de type Skinner–Urban) : « the triple product is a special case of the construction of triple product p-adic L-functions in [Hsieh, AJM 2021]. Note that the test vectors in [73, §3] are the same as ours ». Il s'agit des vecteurs-tests de Hsieh, des vecteurs nouveaux **translatés** (cas (Ia) : ξ₁ ⊗ π₂(η^{c*−c₂})ξ₂ ⊗ π₃(η^{c*−c₃})ξ₃), et non des f_χ littéraux au même point. Le contexte est celui du Th. 9.21, pas des places Σ_s de CLW : c'est un indice, pas une preuve.
- **Conséquence (DÉDUCTION).** Si les vecteurs réellement produits aux places déployées sont ceux de Hsieh, le lemme du §4 ne s'applique pas, puisque les vecteurs ne sont pas du même type K₀ au même point. Le calcul de Hsieh, Prop. 6.3, sous-cas (a) (relu au §1 de cette note : il n'utilise que c₁ ≤ c₂ et c₃ ≤ c₂) donne alors, **avec les données (iv) de CLW elles-mêmes** et π supercuspidale :
  Ψ = (constante non nulle) × ∫W₁(y)W₂(−y)χ₃|·|^{-1/2}(y)d^×y, avec W₁ = W₂ = 1_{O^×}, car σ_h a ses deux caractères ramifiés sous (iv).
  Cette quantité est non nulle et indépendante des tordues non ramifiées. Le problème A serait alors résolu par la route (2) de l'énoncé initial, **sans changer la recette de CLW**.
- **Point 4 (bilan).** Deux lectures cohérentes subsistent :
  - (L1) vecteurs de Wan littéraux, et alors la recette de FW est nécessaire ;
  - (L2) vecteurs de Hsieh, et alors la recette (iv) de CLW suffit.
  
  Dans les deux cas, **le cas supercuspidal admet un choix qui marche**. L'erreur du Lemme 8.14 pèse sur (L1) pour les places semistables publiées. Si (L2) est la bonne lecture, elle n'est qu'une imprécision de rédaction sans conséquence. Seul Wan, ou une relecture de la construction des vecteurs (CLW §7.6–7.7 et Wan §6.7), peut trancher.

## 11. Points 1 et 2 : vecteurs de θ et h, et résolution dans les deux lectures

### 11.1 Ce que dit CLW sur les vecteurs (ÉTABLI, lu sur l'image des p. 64-65)

- CLW Prop. 7.7.3, pour v = 𝔳𝔳̄ ∈ Σ_s : φ_{θ,τ,v} = image par (7.1.6) de (y₁, y₂) ↦ 1_{O_{K,𝔳}}(y₁)·1_{O^×_{K,𝔳̄}}(y₂)·χ_{θ,𝔳̄}λ_{𝔳̄}(y₂). Ici « χ_{θ,𝔳} unramified » est **imposé** par cette forme.
- CLW Prop. 7.7.1 : φ_{h,τ,v} = image par (7.1.6) de (y₁, y₂) ↦ 1_{ℤ_v}(y₁)·1_{ℤ_v^×}(y₂)·χ_{h,𝔳}χ_{h,𝔳̄}^{-1}λ_{𝔳̄}^{-1}(y₂), pour h₀. Ensuite h = h₀ tordu par χ_hχ_θ^c (Déf. 7.7.2 et (7.5.7)), ce qui est une torsion par un caractère du déterminant.
- **Espaces.** θ ∈ V_{U(2),ξ}, alors que h₀ ∈ V′_{U(2),ξ^{-1}}, avec h′₀ ∈ V_{U(2),ξ}. Selon la preuve de la Prop. 7.7.1, h₀ s'obtient en restreignant à U(V) × U(V⁻) puis en évaluant en u_aux ∈ U(V), ce qui donne une famille sur U(V⁻). Les deux formes ne sont donc pas réalisées dans le même modèle de Weil.
- **DÉDUCTION, calcul de Godement.** Dans le modèle linéaire de GL₁ × GL₂ sur S(F²), la fonction 1_O(x₁)·1_{O^×}(x₂)ξ(x₂) donne la section f(k) = c·ξ(d)·1[d ∈ O^×]. Elle est invariante par n⁻(O) et propre pour le groupe des matrices **triangulaires inférieures** modulo ϖ^{cond ξ}, c'est-à-dire le transposé de K₀ = wK₀w^{-1}. Deux fonctions de même forme réalisées dans le **même** modèle donnent donc la **même** orientation. Si le passage V ↔ V⁻ agit en v déployé par g ↦ ᵗg^{-1}, ou par la composante 𝔳̄ au lieu de 𝔳, l'orientation s'inverse. Je ne tranche pas ce point (conventions de (7.1.1) et (7.1.6)).
- **Argument de cohérence (DÉDUCTION).** Supposons la même orientation. Le lemme du §4 et le contre-exemple au Lemme 8.14 annuleraient alors les intégrales locales de CLW **aussi aux places Steinberg déployées** du cas semistable publié (c = 1, a ≥ 4, s = a − 1, 2s > a). Supposons l'orientation opposée. Le critère devient 2·cond(ρ₁) ≤ 2a, toujours satisfait, et tout le cadre publié reste cohérent. **La lecture « orientations opposées » (L2) est la seule compatible avec la validité du cas semistable publié.** C'est un argument de cohérence, pas une preuve.

### 11.2 Lecture (L1) (même orientation) : résolution par la recette de FW

- Il suffit de remplacer, en v ∈ Σ_s supercuspidal, la seconde clause de (iv) par la condition de FW Cor. 7.28 (χ_{h,i}χ_{θ,i} non ramifiés, conducteurs a > c), et de prendre pour ϕ_v le vecteur nouveau de π_v.
- **Compatibilité avec la forme imposée de φ_θ.** χ_{θ,𝔳} est non ramifié. On choisit χ_{h,𝔳} et χ_{h,𝔳̄} pour compenser χ_θ composante par composante. Les deux appariements possibles des indices 1 et 2 avec 𝔳 et 𝔳̄ restent compatibles avec la contrainte globale χ_hχ_θ|_{A_ℚ^×} = 1, qui donne χ_{h,𝔳}χ_{h,𝔳̄} = (χ_{θ,𝔳}χ_{θ,𝔳̄})^{-1} sur ℚ_v^× (vérifié dans les deux cas).
- **Existence globale.** CLW choisissent χ_{θ,1}, χ_{h,1} vérifiant les conditions locales (1)-(5), puis tordent par ν de conducteur ℓ-primaire pour obtenir (6), « via mod p nonvanishing [Hsi14b, Hsi12] ». La condition modifiée en v ∈ Σ_s est locale et indépendante de ℓ ∉ Σ : l'argument s'applique tel quel. Les facteurs L locaux en v valent 1 (§9.4).
- **Calcul local.** FW Cor. 7.28, démontré au §9.1 pour tout ℓ et confirmé numériquement sur le Lemme 8.13 au §9.2 : I_v = Vol(K_{t₁}) ≠ 0, indépendant de τ. **Résolu (DÉDUCTION vérifiée).**

### 11.3 Lecture (L2) (orientations opposées) : résolution avec la recette (iv) de CLW telle quelle

- **Vecteurs.** f_θ est le vecteur nouveau de σ_θ = π(χ_{θ,𝔳} non ramifié, χ_{θ,𝔳̄}) (conducteur a, type K₀(ϖ^a)). f_h est de type transposé. On tord le triplet par (μ, 1, μ^{-1}) avec μ = χ_{h,𝔳̄}, ce qui ne change pas ℓ (DN, (2)). On obtient π′ = π ⊗ μ, supercuspidale de conducteur 2s avec s = a − c > c/2 (Hsieh, Lemme 6.8), et σ′_h = π(ρ, 1) avec cond ρ = a. Alors f_h = π(w)ξ′_h ∝ π(diag(ϖ^a, 1))ξ′_h, où ξ′_h est le vecteur nouveau de σ′_h (relation d'Atkin–Lehner w = diag(1, ϖ^{-a})·AL_a). Ce vecteur est invariant par n⁻(O), donc par n⁻(ϖ^aO).
- **Rankin–Selberg** (σ_θ en modèle induit, Ψ(W, W′, f) = ∫_{NZ\G}W(g)W′(Jg)f(g)dg, forme invariante non nulle, donc égale à ℓ à une constante près par unicité de Prasad). En coordonnées g = diag(y, 1)n⁻(x), avec f_θ(diag(y, 1)n⁻(x)) = χ_{θ,𝔳}|·|^{1/2}(y)·1_{ϖ^aO}(x) :
  Ψ = vol(ϖ^aO)·∫ (P_aW_φ)(y)·W_h(−y)·χ_{θ,𝔳}|·|^{-1/2}(y) d^×y,
  où W_h(y) = W_{ξ′}(ϖ^ay) = |ϖ^ay|^{1/2}·1_O(ϖ^ay), à un caractère non ramifié près, est porté par v(y) ≥ −a, et P_a est la moyenne sur n⁻(ϖ^aO).
- **Choix de ϕ_v.** On prend φ₀ ∈ π′ de type trivial sur O^×, invariant par n⁻(ϖ^aO) et porté par **une seule couche** v(y) = m₀. Par l'équation fonctionnelle, avec γ monomial car π′ est supercuspidale, π(w) envoie une couche m de type trivial sur la couche −m − 2s. Un tel φ₀ existe pour tout m₀ ≤ a − 2s = 2c − a. On prend m₀ = 2c − a, qui est ≥ −a. Alors P_aφ₀ = φ₀, la couche m₀ rencontre le support de W_h, et
  Ψ = (constante non nulle) × (paramètre non ramifié)^{m₀},
  **non nul et monomial, donc non nul pour toute tordue non ramifiée.**
- **Admissibilité de ϕ_v dans CLW.** φ₀ est lisse. Il est invariant par K_v (congruence principale mod q_v^{2c_v+…}) pour c_v assez grand, et (5.6.6) permet d'augmenter c_v. Il est aussi invariant par Y pour le calcul de Fourier–Jacobi (Wan, Lemme 6.20 : « for any ϕ invariant under Y »). Son type sur le tore est celui qui fait coïncider les nebentypus : c'est le rôle de la torsion (5.6.10), et c'est automatique par le choix isotypique. **Résolu (DÉDUCTION).** Ce calcul reprend celui du §4 avec l'orientation opposée.

### 11.4 Bilan

**Dans les deux lectures, le cas supercuspidal en v ∈ Σ_s admet un choix explicite de données (L1) ou de vecteur ϕ_v (L2) pour lequel l'intégrale locale est une constante non nulle indépendante de τ.** C'est ce qu'exige la preuve de CLW Prop. 7.11.3. Conformément à la décision de l'utilisateur, **A est considéré comme résolu en attente de validation** par un spécialiste (Wan), au même titre que B.

**Pas à faire valider en priorité.**
1. Laquelle des lectures (L1) ou (L2) est la bonne. Ce point n'affecte pas le résultat, seulement la recette.
2. En (L2) : la forme exacte du vecteur de h (type transposé, à une translation près) et l'admissibilité du ϕ_v choisi dans l'espace (5.6.12).
3. En (L1) : l'appariement des indices de FW.
4. Indépendamment : le Lemme 8.14 de Wan, faux tel qu'énoncé.

## 12. Point 6 tranché : la lecture littérale de CLW donne (L1), même orientation

### 12.1 Calcul (DÉDUCTION, à partir d'énoncés lus sur les images p. 53, 64 et 65 de CLW)

- **Polarisation en v = 𝔳𝔳̄ décomposé (ÉTABLI, p. 53).** V_v⁻ ⊗ W_{β,v} = (𝒦_𝔳e₁⁻ ⊕ 𝒦_𝔳e₂⁻) ⊕ (𝒦_𝔳̄e₁⁻ ⊕ 𝒦_𝔳̄e₂⁻), et (7.1.6) : S(𝒦_𝔳e₁⁻ ⊕ 𝒦_𝔳e₂⁻) → S(ℚ_ve₁⁻ + ℚ_ve₂⁻).
- **θ et h₀ passent tous deux par (7.1.6) (ÉTABLI, p. 64-65).** On a φ_θ = 1_O(y₁)·1_{O^×}(y₂)·ξ_θ(y₂), avec ξ_θ = χ_{θ,𝔳̄}λ_𝔳̄, et φ_h = 1_O(y₁)·1_{O^×}(y₂)·ξ_{h₀}(y₂), avec ξ_{h₀} = χ_{h,𝔳}χ_{h,𝔳̄}^{-1}λ_𝔳̄^{-1}. Ensuite h = h₀ ⊗ (χ_hχ_θ^c ∘ det).
- **Vecteurs.** Dans le modèle linéaire, le vecteur associé à 1_O(y₁)1_{O^×}(y₂)ξ(y₂) est, à des caractères du déterminant près, f(k) = ξ(d_k)·1[d_k ∈ O^×]. Il est invariant par n⁻(O), et propre pour K₀ᵀ(ϖ^r) = {b ≡ 0 mod ϖ^r} avec r = cond ξ, de caractère ξ(δ) sur le tore. **θ et h ont donc la même orientation : c'est (L1).** Ce point est robuste : quelle que soit la convention d'action (Φ(Xg), Φ(Xᵗg^{-1}), composante 𝔳 ou 𝔳̄), elle est **la même** pour θ et h puisqu'ils utilisent la même application. La torsion de h par un caractère du déterminant ne change pas l'orientation.
- **Critère du §4, en version transposée.** On a f_θ ⊗ f_h propre pour K₀ᵀ(ϖ^a), de caractère Ξ(k) = A(α_k)A^{-1}(δ_k) une fois normalisé le caractère central (ω_π = 1 force B = A^{-2}). Ici A² = (ξ_θξ_{h₀})^{-1} sur les unités, et les λ se simplifient : ξ_θξ_{h₀} = χ_{θ,𝔳̄}χ_{h,𝔳}χ_{h,𝔳̄}^{-1}. La contrainte globale χ_hχ_θ|_{A_ℚ^×} = 1 donne χ_{h,𝔳̄}^{-1} = χ_{h,𝔳}χ_{θ,𝔳}χ_{θ,𝔳̄}, d'où ξ_θξ_{h₀} = (χ_{h,𝔳}χ_{θ,𝔳̄})²·χ_{θ,𝔳} = ((χ_hχ_θ^c)_𝔳)²·(non ramifié). **Condition de non-annulation : c(π_v ⊗ A) ≤ a, avec cond(A) ≈ cond((χ_hχ_θ^c)_𝔳)** (égalité pour ℓ impair ; en ℓ = 2, il faut tenir compte du carré).

### 12.2 Conséquences

1. **Supercuspidales (notre A).** Il faut la recette de FW, qui revient ici à « (χ_hχ_θ^c)_𝔳 non ramifié en v ». Alors A est non ramifié, c(π ⊗ A) = c ≤ a, et FW Cor. 7.28 (démontré au §9) donne I_v = Vol(K_{t₁}) ≠ 0 indépendant de τ. **A est résolu, en lecture (L1).** La condition est compatible avec « χ_{θ,𝔳} non ramifié » (§11.2).
2. **La recette (iv) de CLW donne une intégrale nulle aux places décomposées ramifiées.**
   - Avec cond((χ_hχ_θ^c)_𝔳) = a − c, on a c(π ⊗ A) = 2(a − c) > a dès que a > 2c, ce que (iv) impose. La forme ℓ(· ⊗ f_θ ⊗ f_h) est donc identiquement nulle, **pour tout ϕ_v**.
   - Cela vaut pour π_v Steinberg (c = 1, a ≥ 4) et pour les séries principales ramifiées.
   - Exception : π_v non ramifiée avec a = 2 (alors s = 1 et 2s = a).
   - C'est cohérent avec le contre-exemple numérique au Lemme 8.14 (§9.3, §10). **Cela indique une lacune possible dans CLW, et donc dans BSTW Th. 1.6 et 12.3, même dans le cas semistable**, aux premiers multiplicatifs décomposés dans le corps auxiliaire. C'est une DÉDUCTION à faire confirmer d'urgence (question 3 à Wan).
3. **Impact sur notre raccord (correction importante).** Le rang 1 (BSTW Th. 12.3) utilise le Th. 10.1 **pour la tordue g′ = g ⊗ χ_L**. Aux ℓ | D_L, g′ est une **série principale ramifiée** (tordue quadratique d'une non ramifiée), placée à une place décomposée de L″. Ces ℓ ne peuvent pas être inertes dans L″ : CLW §5.2 n'y admet que les représentations non ramifiées et les Steinberg. **Notre rang 1 dépend donc du cas « série principale ramifiée », que la lecture (L1) met en défaut avec la recette (iv).** C'est vrai aussi pour BSTW dans le cas semistable. Le scénario S_A (77,71 %) **n'est donc pas indépendant** de ce point. Le rang 0 (Th. 1.6, seulement g) l'est.
4. **Piste de réparation, à étudier.** Appliquer aux séries principales ramifiées et aux Steinberg la même idée qu'en 1, c'est-à-dire choisir (χ_hχ_θ^c)_𝔳 non ramifié pour satisfaire le critère. Le calcul de non-annulation n'est plus le cas « une seule cellule » de FW : Φ_π n'est pas à support compact. L'intégrale devient une série en paramètres de Satake. Il faut alors montrer qu'elle est non nulle et contrôlée en τ, éventuellement après une ℓ-stabilisation du vecteur de π, comme le fait le Lemme 8.16 de Wan pour les non ramifiées. **C'est le nouveau point bloquant**, pour nous comme pour la littérature.

## 13. Réparation uniforme aux places décomposées (toute π_v) : proposition et vérification

**Origine de l'échec.** Le vecteur f_{χ,ϑ} de Wan (Lemmes 8.14 et 8.16-8.18) prend ϑ de conducteur s **strictement supérieur** à la profondeur t du support (c ∈ ϖ^tO^×). Le vecteur obtenu n'est pas propre pour K₀(ϖ^{t+s}) : c'est le contre-exemple du §9.3. Avec la recette (iv) de CLW, le critère du §4 l'annule (§12).

**Proposition R (DÉDUCTION, preuve ci-dessous, vérifiée numériquement).** Soient v une place décomposée, π_v générique de caractère central trivial, et A un caractère de ℚ_v^× avec **L(s, π_v ⊗ A^{±1}) = 1**. C'est le cas, A étant ramifié, pour π_v non ramifiée, Steinberg, Steinberg tordue St ⊗ χ₀ (avec χ₀A ramifié), série principale π(χν₁, χν₂) (avec χA ramifié), et pour toute supercuspidale, avec A quelconque, trivial compris (c'est FW). On pose n_A = c(π_v ⊗ A).
- On prend pour ϕ_v le vecteur de Kirillov W = A^{-1}·1_{O^×}, c'est-à-dire le vecteur nouveau de π_v ⊗ A vu dans π_v. En modèle induit, f(n⁻(y)) = A^{-1}(y/ϖ^r)·1[v(y) = r] avec r = cond A, ce qui est le f_{χ,ϑ} de Wan **avec s = t**. Ce vecteur est propre pour K₀(ϖ^{n_A}), de type A^{-1}(a)A(d).
- On choisit les données auxiliaires pour que f_θ ⊗ f_h ait sur K_{t₁} le type A(a)A^{-1}(d), avec t₁ ≥ n_A. D'après le §12.1, il suffit que (χ_hχ_θ^c)_𝔳 vaille A^{∓1} à un caractère non ramifié près. C'est compatible avec χ_{θ,𝔳} non ramifié (imposé), puisque A est porté par χ_h.

Alors I_v = Vol(K_{t₁})³·⟨ϕ_v, ϕ̃_v⟩ ≠ 0 (à la normalisation de Wan près), **indépendant des tordues non ramifiées**.

*Preuve.*
- (1) Wan 8.13 : Φ_θΦ_h est porté par K_{t₁} et par les deux familles de cellules n ≥ 1, où il vaut Vol²·α^n q^{-n/2}·(type). Cette partie est vérifiée numériquement (§9.2).
- (2) Φ_ϕ est nul sur les cellules diag(ℓⁿ, 1)n(y), n ≥ 1, car les supports O^× et ℓ^{-n}O^× sont disjoints.
- (3) Φ_ϕ est nul sur les cellules diag(ℓ^{-n}, 1)n⁻(ϖ^iu), n ≥ 1. On écrit n⁻ = ω^{-1}nω. Par l'équation fonctionnelle de Jacquet–Langlands, γ(s, π ⊗ A^{±1}) est **monomial** puisque L = 1 : π(ω) envoie la couche 0 de type A^{-1} sur une seule couche (−n_A). Après multiplication par ψ, seule la composante de type A^{-1} revient sur la couche 0. Φ(diag(a, 1)n⁻) avec m = 0 est donc non nul seulement si v(a) = 0. On utilise uniquement le caractère monomial de γ, ce qui vaut aussi pour ℓ = 2.
- (4) Sur K_{t₁}, Φ_ϕ(k) = A^{-1}(a)A(d)·Φ_ϕ(1), et ce type compense celui de Φ_θΦ_h.
- Il ne reste que la cellule n = 0 : aucun α^n n'apparaît, d'où l'indépendance en τ. ∎

**Vérification numérique** (`bsd/scripts/reparation_ps.py`, `reparation_ps2.py`, p = 3).

| π_v | A | max\|Φ\| sur les cellules n = 1..3 | erreur de type sur K_{t₁} |
|---|---|---|---|
| non ramifiée, paramètres génériques | cond 1 | 0 (exact) | 1,1·10⁻¹³ |
| Steinberg (sous-module de π(\|·\|^{1/2}, \|·\|^{-1/2})) | cond 1 | 0 | 1,6·10⁻¹³ |
| série principale π(χν₁, χν₂), χ quadratique | cond 2 (χA ramifié) | 0 | 3,9·10⁻¹⁴ |

**Conséquences (DÉDUCTION, sous validation).**
1. A est réparé **uniformément**, pour les supercuspidales, les séries principales ramifiées, Steinberg et Steinberg tordu, en remplaçant la seconde clause de (iv) par « (χ_hχ_θ^c)_𝔳 = A^{∓1} × non ramifié, avec L(π_v ⊗ A^{±1}) = 1 et t₁ ≥ c(π_v ⊗ A) », et le vecteur ϕ_v par celui de la Prop. R (licite d'après l'objection 5).
2. Cette réparation comble aussi la lacune possible de CLW et BSTW signalée au §12 (places Steinberg décomposées, tordue g′), **si** la lecture (L1) est la bonne.
3. Le rang 1 (tordue g′, séries principales ramifiées aux ℓ | D_L) est couvert, ce qui lève l'objection 26.

**Borne recalculée** (`bound_v2.py`, scénario S_rep : tous les types en 2 et 3, Steinberg tordu compris, cellules indéterminées et niveaux non minimaux exclus) : voir `raccord_A_B.md` §7.

### 13.1 Vérification en ℓ = 2 (`bsd/scripts/p2_tests.py`, caractères de ℤ₂^× = {±1} × ⟨5⟩)

- **Wan, Lemme 8.13** (t = 3, χ₁ non ramifié, cond χ₂ = 3). Φ = 0 sur K₁wσ_nK₁ et K₁σ_nwK₁ pour n = 0, 1, 2. Sur les deux autres familles, les valeurs valent 0,125 ; 0,0713 ; 0,0406 et 0,125 ; 0,116 ; 0,108, contre 0,125 ; 0,0713 ; 0,0406 et 0,125 ; 0,1163 ; 0,1081 attendus. **Confirmé en ℓ = 2.**
- **Proposition R.**

  | π_v | A | max\|Φ\| sur les cellules n = 1..3 | erreur de type sur K_{t₁} |
  |---|---|---|---|
  | non ramifiée | cond 2, t₁ = 4 | 0 (exact) | 0 |
  | Steinberg | cond 2, t₁ = 4 | 0 | 0 |
  | série principale π(χν₁, χν₂), χ quadratique de conducteur 2 | cond 3 (χA de cond 3), t₁ = 6 | 0 | 1,2·10⁻¹⁴ |

  **La Proposition R est confirmée en ℓ = 2 et ℓ = 3** pour les trois types non supercuspidaux. Le cas supercuspidal (A trivial) est la Prop. 7.27 et le Cor. 7.28 de FW, démontrés au §9.1 pour tout ℓ. Il n'est pas testé numériquement : il faudrait un modèle de Kirillov explicite d'une supercuspidale en 2.
