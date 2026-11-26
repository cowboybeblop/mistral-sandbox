# Le calcul local en 2 (composante supercuspidale) : tentative

26 novembre 2026. **Statut : ESQUISSE.** C'est une réduction à des résultats publiés, avec une liste de vérifications non faites. Aucune relecture par un spécialiste. Le but est de voir si l'hypothèse « N sans facteur carré » des réciproques supersinguliers (BSTW Thm 12.3 et 1.6, via Castella–Liu–Wan [CLW] et Wan [W]) peut être levée aux premiers de réduction additive, ce qui ferait passer la borne BSZ d'environ 67 % à environ 79 % (`amelioration_BSZ.md` §7).

## 1. Ce que les auteurs disent eux-mêmes

- Wan, arXiv 1408.4044, p. 3 : « The square-freeness of N is put at the moment for simplicity (mainly to avoid local triple product integrals for supercuspidal representations and we may come back to remove it in the future). » ÉTABLI (citation).
- BSTW, preuve du Th. 9.24 : la semistabilité sert au « explicit calculation of local triple product periods » ; les premiers où la composante est une série principale sont déjà traités. ÉTABLI (citation).
- CLW (arXiv 2109.08375), §7.11 : la constante C₂ contient « the local triple product integrals divided by the norms at v ∈ Σ ∪ {ℓ, ℓ′}, which are nonzero constants ». Le résultat est une divisibilité dans Λ ⊗ ℚ. **Il suffit donc que ces intégrales soient non nulles**, en chaque spécialisation, et non qu'elles soient des unités p-adiques. ÉTABLI (lecture).
- CLW §5.2 : hypothèse locale globale « π_v non ramifiée, Steinberg, ou Steinberg tordue par un quadratique non ramifié ». Elle sert aux places non décomposées (Prop. 7.12.1, via Frobenius sur π_v ⊂ Ind_B) et aux places décomposées Σ_s (calculs « précis », Lemmes 6.22 et 6.24 de [W], et normes locales de [Hsi19, Prop. 6.3]). ÉTABLI (lecture partielle).

## 2. Réduction proposée

**Choix du corps auxiliaire K.** On prend K tel que tous les premiers de réduction additive de E (en particulier 2 et 3) soient **décomposés** dans K. On met dans N⁻ (non décomposés) deux premiers de réduction multiplicative avec E[5] ramifiée : ils existent pour 100 % des courbes, par le Lemme 20 de BSZ. Ainsi, aux places non décomposées, π_v est Steinberg et la Prop. 7.12.1 de CLW s'applique telle quelle. Les conditions (spl) et (indef) de BSTW Th. 9.24 et 10.5 semblent alors satisfaites : 2 est décomposé, et q | N⁻ vérifie (ram). **À VÉRIFIER.**

**Places décomposées avec π_v supercuspidale.** En v = w w̄ décomposé, les composantes locales des deux formes CM auxiliaires θ et h sont des séries principales π(χ_w, χ_w̄). La forme trilinéaire locale porte donc sur π_v ⊗ σ_θ ⊗ σ_h, avec une seule supercuspidale.
- *Existence.* Par Prasad (Th. 1.4 de [P], rappelé dans Dimitrov–Nyssen [DN] Th. 1), ε(π_v ⊗ σ_θ ⊗ σ_h) = −1 exige trois séries discrètes. Ici ε = +1, et la forme G-invariante ℓ ≠ 0 existe dès que ω₁ω₂ω₃ = 1, condition déjà imposée dans [CLW]. ÉTABLI (énoncés).
- *Vecteur test explicite.* [DN, arXiv 1005.0724, Th. 4] : si l'une au moins des trois n'est pas supercuspidale, si le triplet est minimal et si ε = 1, alors v₁ ⊗ γ^{n₃−n₂}·v₂ ⊗ v₃ (vecteurs nouveaux, γ = diag(ϖ⁻¹, 1)) n'est pas dans le noyau de ℓ. Aucune restriction sur la caractéristique résiduelle dans ce cas. ÉTABLI (énoncé lu).
- *Intégrale d'Ichino.* L'intégrale locale I_v(φ) = ∫ ⟨Π(g)φ, φ⟩ dg est, à une constante non nulle près, |ℓ(φ)|². Elle est donc non nulle sur un vecteur test. SECONDAIRE (forme standard de la formule d'Ichino, non relue ici).
- *Variation en τ.* τ est non ramifiée hors de p. En v, la famille ne change σ_θ et σ_h que par des tordues non ramifiées. Celles-ci préservent conducteurs, vecteurs nouveaux, minimalité et ε = 1. Le vecteur test de [DN] l'est donc **pour chaque spécialisation**, et l'intégrale ne s'annule en aucun caractère κ, ce qu'exige la preuve de CLW Prop. 7.11.3. DÉDUCTION.

**Variante directe (DÉDUCTION).** Par Frobenius, comme en CLW (7.12.4)–(7.12.6), ℓ se ramène à une intégrale de Rankin–Selberg ∫_{ℚ_v^×} W(a)W′(a)ν(a)|a|^{s} d^×a. Pour π_v supercuspidale, le modèle de Kirillov est C_c^∞(ℚ_v^×). Avec W = 1_{a₀(1+ϖ^m O)} et W′(a₀) ≠ 0, l'intégrale vaut W′(a₀)ν(a₀)·vol ≠ 0, et une tordue non ramifiée ne la multiplie que par une valeur de caractère en a₀, inversible dans Λ. Cela suffit si l'on a la liberté de choisir le vecteur de π_v ; sinon on utilise [DN].

## 3. Ce qui reste à vérifier (liste honnête)

1. **Compatibilité des vecteurs.** En Σ_s, les vecteurs de θ et h sont imposés par les sections d'Eisenstein et les fonctions de Schwartz de [W, Lemme 6.24], sous des contraintes de conducteur sur χ_θ,v (Remarque 6.25 : « flexibility on choosing χ_θ,v »). Il faut vérifier qu'on peut réaliser le vecteur test de [DN], soit par des translatés γ^k, soit par des opérateurs T_v comme en CLW Prop. 7.12.1, et qu'on peut rendre le triplet minimal par le choix de χ_θ, χ_h.
2. **Calculs de Fourier–Jacobi en Σ_s** ([W, Lemmes 6.22 et 6.24]) : il faut voir s'ils utilisent la structure de π_v (Steinberg ou non ramifiée) ou seulement les données auxiliaires.
3. **Normes locales** ([Hsi19, Prop. 6.3], utilisées par CLW) : elles sont non nulles pour tout vecteur non nul, mais il faut vérifier que la normalisation reste interpolable p-adiquement.
4. **Invariants μ** cités par BSTW Th. 10.5 ([116] et [21] de BSTW) : hypothèses à lire.
5. **Autres usages de la semistabilité** dans BSTW : Th. 10.1 et la descente vers ℚ (Prop. 10.7 et suivantes), Th. 12.3 pour le rang 1 (cas a_p = 0 et N sans facteur carré : origine de l'hypothèse à confirmer), ainsi que le choix de L, la descente et l'usage de la conjecture principale de Kobayashi.
6. **Hsieh** [Hsi19] pose peut-être lui-même des hypothèses de ramification dans ses calculs de produit triple, à lire.

## 4. Bilan

- **Ce que cette tentative apporte.** L'ingrédient local qui manquait, la non-annulation des intégrales triples locales quand π_v est supercuspidale à une place décomposée, semble **déjà disponible** : [DN, Th. 4] et la formule d'Ichino, et seule la non-annulation est requise (CLW travaillent dans Λ ⊗ ℚ). C'est le type de combinaison de résultats existants que décrit la note zêta.
- **Ce qu'elle n'apporte pas.** Une preuve. Les points 1 à 6 demandent la lecture complète de [W] (≈ 100 p.), [CLW] (90 p.) et des §9 à 12 de BSTW, puis une vérification par un spécialiste. Si tout passe, la borne BSZ devient ≈ 79,0 % (et ≈ 80,4 % si les premiers additifs autres que 2 et 3 sont aussi couverts, ce que la même réduction donne). Si un seul point casse, le gain peut retomber à 67 %.

## Références

[W] X. Wan, arXiv 1408.4044 (ANT 14, 2020). [CLW] Castella–Liu–Wan, arXiv 2109.08375 (Forum Math. Sigma 10, 2022). [BSTW] arXiv 2409.01350. [DN] Dimitrov–Nyssen, arXiv 1005.0724. [P] D. Prasad, Trilinear forms for representations of GL(2) and local ε-factors (cité par [DN], non ouvert). [Hsi19] M.-L. Hsieh, Hida families and p-adic triple product L-functions (cité par CLW, non ouvert). Hu, arXiv 1409.8173 : intégrales locales de produit triple en niveau général (non lu ; utile si l'on veut des valeurs explicites).

## 5. Résultat des six vérifications (26 novembre 2026)

| # | Vérification | Verdict | Détail |
|---|---|---|---|
| 1 | Vecteurs imposés en Σ_s compatibles avec Dimitrov–Nyssen | **OUVERT, reformulé** | **Corrigé le 26 novembre 2026** (note d'une autre discussion, vérifiée ici sur les PDF). Ma version précédente attribuait à tort les vecteurs au cas (Ia) de Hsieh. En réalité, CLW (preuve de la Prop. 7.11.2) citent [Wan20, Lemmes 8.13–8.17] en Σ_s, et Hsieh, Prop. 6.3, seulement en v = p. Les vecteurs sont ceux de Wan : pour θ et h, des vecteurs supportés sur K_t se transformant par un caractère ; pour π, le vecteur nouveau tordu par l'opérateur (5.6.10) de CLW. Ce qui exclut les supercuspidales, c'est que Wan calcule dans le **modèle induit** (séries principales), et non l'hypothèse (sf) de Hsieh. La condition (iv) de CLW est exactement t₁ + s = t₂ du Lemme 8.17 de Wan, avec t₁ = c(π). Ce lemme donne, pour π série principale, I_v = (q − 1)²/q^{2s+1}·Vol(K₁)·Vol(K_{t₂})², valeur non nulle et indépendante des caractères. **Le problème A est donc l'analogue du Lemme 8.17 pour π supercuspidale.** La route Dimitrov–Nyssen est bloquée : (iv) fixe les conducteurs des caractères de χ_h à a et a − c (a ≥ 2c + 2), donc σ_h n'est jamais minimale, et tordre pour la rendre minimale change les vecteurs. Dans le modèle de Kirillov, le vecteur de π est ϑ⁻¹(−y)·1_{O^×}(y), à une somme de Gauss près : c'est le vecteur nouveau de π ⊗ ϑ, de conducteur 2s. L'argument de support ne marcherait que pour a ≤ 2c, ce que CLW excluent. Il faut donc la fonction de Bessel de π ⊗ ϑ. À vérifier : le rôle des vecteurs dans Wan §8.3, la normalisation de σ_h dans CLW §7.10, la minimalité de π. Prochaine étape : test numérique en v = 3, c = 2 (niveau zéro), **calibré d'abord sur le Lemme 8.17 avec π série principale**. |
| 2 | Fourier–Jacobi et pullback aux places ramifiées décomposées | ✓ | [W, Lemme 6.20] : le pullback vaut τ(yȳ)·|·|·Vol(Y)·ϕ pour **tout** ϕ invariant par Y. Les Lemmes 6.22 et 6.24 et le §5.7.3 de CLW ne dépendent pas du type de π_v (seulement de c_v > cond(π_v) + …). |
| 3 | Normes locales (Hsieh Lemme 6.4) | ✓ | Elles sont non nulles pour tout vecteur non nul, et seule la non-annulation est requise. |
| 4 | Invariants μ utilisés par BSTW Th. 10.5 | **OBSTACLE, refondu** | Lecture de PW §2.3–2.4 et §6 (26 novembre 2026). BSTW ont besoin de μ(L°,ac_p) = 0 dans leur normalisation, et cela n'est pas contournable rationnellement : un premier de hauteur 1 de Λ^cyc forcerait μ(L°,ac) ≥ 1. Le besoin se coupe en (B1) μ(L±_W) = 0 pour la période de Gross (PW Th. 2.5(1), via l'équidistribution de Vatsal, que Chida–Hsieh font avec N⁺ quelconque en ordinaire : probablement accessible) et (B2) la comparaison des périodes η_f(N) ~ ξ_f(N⁺,N⁻) (PW Th. 6.8, via Ribet–Takahashi et la liberté du Th. 6.2, en niveau sans facteur carré). Sous (ram) en tout q \| N⁻, (B2) se réduit (DÉDUCTION) à la **liberté de Pic(X_{N⁺,N⁻})_m sur T_m (multiplicité un)**. N⁺ est ρ̄-minimal en 2 et 3, car l'inertie y est d'ordre premier à 5. Détails : `bsd/DEUX_PROBLEMES_OUVERTS.md`. |
| 5 | Autres usages de la semistabilité (BSTW §10.3) | ✓ (sauf via 1 et 4) | Le lemme de Ribet pour (ram) est remplaçable par le Lemme 20 de BSZ (100 % des courbes). Le reste passe par le Th. 10.5, donc par les points 1 et 4. Le Th. 10.4 (Kato) et la Prop. 10.7 (contrôle) n'ont pas d'hypothèse sur N. |
| 6 | Hypothèses de Hsieh | ✓ | [Hsi14b] (1112.1580, Th. A) demande « (sf) n⁻ square-free », satisfaite si les premiers additifs sont décomposés dans K. [Hsi19, Prop. 6.3] ne sert qu'en v = p (corrigé, voir point 1), où π est non ramifiée. |

**Bilan.** Il reste **deux obstacles précis** pour lever la semistabilité dans les réciproques supersinguliers en 5 :
- **(A) local** : la non-annulation de l'intégrale de produit triple aux places décomposées, pour les vecteurs de CLW, quand π_v est supercuspidale et σ_h éventuellement non minimale ;
- **(B) global** : l'annulation de l'invariant μ± anticyclotomique (cas supersingulier, a_p = 0) quand N⁺ n'est pas sans facteur carré.

Aucun des deux n'est résolu ici. La borne d'environ 79 % reste donc **conditionnelle à (A) et (B)**, et non à « six vérifications de routine ».
