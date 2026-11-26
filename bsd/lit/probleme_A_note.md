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
