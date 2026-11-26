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

## 4. Réduction partielle et point bloquant

Les Lemmes 8.13 à 8.15 de Wan fixent le support et les valeurs de Φ_θΦ_h. Ce support est la réunion de K_{t₂} et de cellules indexées par n ≥ 1, où apparaissent les paramètres de Satake α^n, donc la tordue non ramifiée. Ces deux lemmes ne dépendent pas de π_f (ÉTABLI : énoncés p. 81-82). Il reste deux conditions sur π, toutes deux de statut DÉDUCTION :

- **(P1)** Φ_{φ_ϑ} est nulle sur les cellules n ≥ 1 où Φ_θΦ_h ≠ 0. Si (P1) est vraie, I_v ne dépend pas de la tordue non ramifiée, ce qui donne exactement la propriété voulue.
- **(P2)** ∫_{ϖ^a O} Φ'_new(n⁻(x)) dx ≠ 0, où Φ'_new est le coefficient du vecteur nouveau de π' = π ⊗ ϑ. Cette intégrale vaut ‖P_a φ'‖², où P_a est la projection sur les invariants de n⁻(ϖ^a O). Elle est donc ≥ 0, et nulle si et seulement si P_a φ' = 0.

**Où l'argument naïf échoue (DÉDUCTION, vérifiée à la main).** φ' est fixé par n⁻(ϖ^{2s}O), donc P_aφ' = φ' ≠ 0 dès que a ≥ 2s, c'est-à-dire a ≤ 2c. Or CLW imposent a ≥ 2c + 2. On est **toujours dans le régime a < 2s**, où P_aφ' peut s'annuler. C'est précisément l'orthogonalité des caractères ramifiés que craignait le §5. Pour conclure, il faut l'action de w, donc la fonction de Bessel de π'.

## 5. Statut et suite

- **Obtenu.** (i) La correction du §5 (sources des vecteurs). (ii) L'obstruction de la route (1). (iii) L'énoncé A′ et sa réduction à (P1) et (P2). (iv) La raison précise pour laquelle l'argument de support ne suffit pas.
- **Non obtenu.** La non-annulation. Aucun contre-exemple n'a été calculé.
- **Étape suivante proposée.** Un test numérique en v = 3, c = 2 : supercuspidales de niveau zéro, induites de caractères de 𝔽₉^×, avec une fonction de Bessel explicite donnée par des sommes de Gauss. On calculerait P_a φ' pour s = a − 2 ≥ 4 et Φ_{φ_ϑ} sur les cellules n ≥ 1. PARI/GP n'est pas installé ; Python suffit.
- **Relecture adverse.** (a) Le §1 repose sur une phrase de CLW. Il faut vérifier dans Wan §8.3 (p. 85 et suivantes) que les vecteurs utilisés en Σ_s pour π_E sont bien f_{χ,ϑ}. (b) Le calcul de conducteurs du §2 suppose la normalisation σ_h = π(χ_{h,w}, χ_{h,w̄}), à confirmer dans CLW §7.10. (c) L'égalité c(π ⊗ ϑ) = 2s demande que π soit minimale. Sinon, il faut prendre une tordue, ce qui ne change pas I_v.
- **À faire relire par un spécialiste.** Le §3 (identification t₁ = c(π) avec Wan, Lemme 8.17) et la réduction (P1)–(P2).
