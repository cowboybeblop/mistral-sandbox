# Relecture adverse, deuxième tour (27 novembre)

Objet : tout ce qui a été produit, y compris la revérification du 27/11 (`reverification_27_11.md`), la Prop. R′, la lecture (L1), l'espace élargi (5.6.12′), le côté B et le chiffrage. Gravité : **C** = critique, **I** = importante, **M** = mineure. Chaque objection est suivie de son traitement.

---

## N1 (C) — La lacune de CLW et la nécessité de la Prop. R′ reposent sur la lecture (L1)

**Objection.** La Prop. V (le Lemme 8.17 donne 0) est démontrée. En revanche, que la construction globale de CLW produise ces vecteurs aux places décomposées ne l'est pas. Si la bonne lecture est (L2), il n'y a pas de lacune, et la Prop. R′ est inutile (sans être fausse).

**Traitement.**
- Trois indices indépendants vont dans le sens de (L1) (ÉTABLI, lu) :
  - Wan, Rem. 8.19 : les intégrales locales aux places décomposées « are the ones considered in this subsection ».
  - CLW p. 72 citent « [Wan20, Lemmas 8.13-8.17] ».
  - Les fonctions de Schwartz de θ et h₀ passent par la même application (7.1.6), avec des fonctions de même forme (`probleme_A_note.md` §12).
- **Dans les deux lectures, A est résolu** : en (L1) par la Prop. R′, en (L2) par la recette (iv) de CLW telle quelle (`probleme_A_note.md` §11.3). L'amélioration de la borne ne dépend donc pas de la réponse. Seul le diagnostic sur la littérature (« lacune possible ») en dépend.

**Statut.** Ouvert, mais sans effet sur le résultat conditionnel. C'est la question 3 à Wan, à reformuler avec la Prop. V, dont la preuve tient en quatre lignes et se vérifie immédiatement.

---

## N2 (C pour le chiffrage) — Niveau « minimal » en 2 et 3 côté B : congruences à changement de type

**Objection.**
- L'étape 4 de B (liberté de S_∅ sur T_∅, CH Prop. 6.8 avec Σ = ∅) utilise la surjection R_∅ → T_∅ (CH Lemme 6.5). Il faut donc que **toutes** les formes propres de T(N_∅)_m aient une représentation galoisienne minimalement ramifiée.
- Au niveau sans facteur carré, c'est automatique. En q² \| N, une forme congruente à f **de même conducteur mais d'un autre type inertiel** pourrait se trouver dans T(N_∅)_m. Ce serait le cas d'une forme de type χ ⊗ St congruente à une forme de type χ ⊗ (non ramifiée).
- CH ne vérifient pas ce point. L'ancien raisonnement (« supercuspidal en 2 et 3, donc minimal ») ne couvre pas les autres types, que la Prop. R′ fait maintenant entrer.

**Traitement (DÉDUCTION).**
1. **Types inertiels en q ∈ {2, 3}.** Comme q ≢ ±1 mod 5, toute représentation de Weil–Deligne de dimension 2 de G_q à inertie finie a une image d'ordre premier à 5.
   - La partie modérée d'un type de dimension 2 est d'ordre divisant q² − 1, qui vaut 3 ou 8. La partie sauvage est un q-groupe.
   - Pour un groupe d'ordre premier à p, deux représentations de mêmes réductions sont isomorphes : les caractères sont des sommes de racines de l'unité d'ordre premier à p, qui restent distinctes modulo λ.
   - Une forme congruente à f, de type à inertie finie, a donc **le même type** que f.
   - Seul le type Steinberg tordu χ ⊗ St (inertie infinie, unipotente) peut se réduire sur un type à inertie finie, à savoir χ ⊕ χ, lorsque sa partie unipotente s'annule modulo 5.
   - Il n'existe pas de caractère ramifié d'ordre 5 de ℚ₂^× ni de ℚ₃^× : ℤ₂^× et ℤ₃^× n'ont pas de quotient d'ordre 5. Le changement de caractère est donc exclu.
2. **Les cas à changement de type possible en q ∈ {2, 3}** sont exactement :
   - **E1** : réduction multiplicative avec 5 \| v_q(Δ_min). ρ̄ est non ramifiée en q et m_q = 1, donc Σ ≠ ∅ dans CH.
   - **E2** : Steinberg tordu (j non entier en q) avec 5 \| v_q(j). ρ̄\|I_q = χ ⊕ χ, et f elle-même n'est pas minimale au sens rigide.
   - **E3** : série principale quadratique (E ⊗ χ_d de bonne réduction en q) avec a_q(E ⊗ χ_d) ≡ ±(q + 1) mod 5. Des formes de type χ ⊗ St congruentes à f peuvent alors exister au même niveau, par la montée de niveau de Ribet appliquée à E ⊗ χ_d.
   - Hors de ces cas, ρ̄\|I_q détermine le type. La déformation est rigide si p ∤ #ρ̄(I_q). Elle est de type Steinberg tordu, invariante par torsion puisque ad⁰(ρ ⊗ χ) = ad⁰ρ, si la partie unipotente survit. R_∅ → T_∅ est alors surjective.
3. **Décision.** On **exclut** E1, E2 et E3 du chiffrage. Les densités sont calculées par `local_types_v3.py` (voir le chiffrage ci-dessous).
   - Ce choix est prudent. Par torsion par χ_d (d ∈ {−1, 2, −2} en 2, d = −3 en 3, ramifiés seulement en q et non ramifiés en 5), E2 et E3 se ramènent aux cas non minimaux m_q = 1 et m_q = 2 de E ⊗ χ_d. CH les traitent par montée de niveau (Lemmes 6.3, 6.4, Cor. 6.7, [Tay06 §3]) et [Dia97b, Th. 2.4], ce dernier non ouvert.
   - Une récupération est donc possible plus tard, au prix de [Dia97b] et d'un argument d'invariance par torsion des modules de congruence.

**Statut.** Réglée par exclusion (coût chiffré ci-dessous).

---

## N3 (I) — Existence des caractères auxiliaires avec les nouvelles conditions locales

**Objection.** La Prop. R′ remplace la seconde clause de (iv) par « (χ_hχ_θ^c)_𝔳·A non ramifié ». Le choix des caractères repose sur les théorèmes de non-annulation modulo p de [Hsi14b] (pour (5.6.1)) et de [Hsi12] (pour (5.6.3) et (5.6.4)). Il faut vérifier que leurs hypothèses ne portent pas sur ces conducteurs.

**Traitement.**
- [Hsi14b] = arXiv 1112.1580 (lu, Th. A et C). Les hypothèses sont (ord), l'Hypothèse A (signes locaux +1 aux places v \| 𝔫⁻, non décomposées), 𝔫⁻ sans facteur carré et ρ̄ irréductible. **Aucune condition aux places décomposées** : la construction du §3.6.2 traite les places décomposées de conducteur quelconque (ÉTABLI).
- Aux places décomposées, le signe local de BC(π) ⊗ χ vaut 1 dès que χ\|_{ℚ_v^×} = 1. La contrainte globale χ_hχ_θ^c\|_{A_ℚ^×} = 1 donne χ_𝔳̄ = χ_𝔳^{-1}, et alors ε(π ⊗ χ_𝔳)ε(π ⊗ χ_𝔳^{-1}) = χ_𝔳(−1)² = 1 (DÉDUCTION).
- Les facteurs d'Euler locaux en v des valeurs (5.6.1)-(5.6.5) restent finis et non nuls (inverses de polynômes). Ce sont des unités 5-adiques dès que les caractères en jeu sont ramifiés. Avec (χ_hχ_θ^c)_𝔳 non ramifié, le facteur de (5.6.2) en v est [(1 − α q^{-1/2})(1 − β q^{-1/2})]^{-1}·[…]^{-1}, de valuation 5-adique à contrôler : voir N4.
- **[Hsi12] n'a pas été ouvert** (NON VÉRIFIÉ). Ses hypothèses éventuelles sur le conducteur de χ_hχ_θ^cξ₀τ₀ aux places décomposées restent à lire.

**Statut.** Partiellement réglée. Il reste à lire [Hsi12].

---

## N4 (I) — Les constantes locales doivent-elles être des unités 5-adiques ?

**Objection.** CLW p. 72 demandent seulement « a nonzero constant independent of τ ». Mais la conclusion « ∉ P » du §8 de CLW pourrait demander une unité si P contient p.

**Traitement.**
- La constante de la Prop. R′, normalisée par les produits scalaires, vaut Vol(K_{t₁}) = 1/((ℓ + 1)ℓ^{t₁−1}). Pour ℓ ∈ {2, 3}, cela donne 1/(3·2^{t₁−1}) ou 1/(4·3^{t₁−1}) : **une unité 5-adique** (DÉDUCTION).
- Aux autres places décomposées (semistables), le facteur ℓ + 1 est le même que dans la constante de Wan (Lemme 8.17 : Vol(K₁)²), donc la situation n'est pas pire que dans le texte publié.
- Pour le facteur d'Euler de (5.6.2) en v ∈ {2, 3} avec (χ_hχ_θ^c)_𝔳 non ramifié : on peut choisir A **ramifié** (permis par la Prop. R′) pour rendre tous les facteurs d'Euler en v égaux à 1, tout en gardant n₀ = c(π ⊗ A) ≤ a. Il suffit de prendre cond A ≤ a/2, ce qui est possible puisque a ≥ 2c + 2.

**Statut.** Réglée (choix de A ramifié de petit conducteur).

---

## N5 (I) — La Prop. R′ s'appuie sur le Lemme 8.13 de Wan, voisin du Lemme 8.14 qui est faux

**Traitement.**
- Le Lemme 8.13 est vérifié numériquement en p = 3 (t = 2) et en p = 2 (t = 3), sur les quatre familles de cellules d'Iwahori, pour n ≤ 3 (26/11).
- Preuve partiellement refaite (DÉDUCTION). Φ_θ s'annule sur les doubles classes K_t x K_t qui ne portent aucune fonction bi-équivariante non nulle :
  - **classes antidiagonales** : la conjugaison échange a et d, et χ₁χ₂^{-1} est ramifié ;
  - **classes K_t n(x)diag(ϖ^m, 1)K_t avec v(x) = −r < 0 et −r < m < t − r** : le test avec n⁻(c), c ∈ ϖ^{max(t, 2r+m)}O, fait apparaître (χ₁^{-1}χ₂)(1 + cx), qui est non trivial.
  - Reste le cas des classes « intermédiaires » K_t n⁻(ϖ^r) w diag(·) K_t avec 1 ≤ r < t. Les types y sont compatibles : l'annulation est un vrai calcul de sommes de caractères, que Wan fait (« it is not difficult to check that the integration is 0 since cond(χ₁χ₂^{-1}) = (ϖ^t) »). Les tests numériques le confirment.

**Statut.** ÉTABLI chez Wan, vérifié numériquement, preuve refaite en partie. À faire relire.

---

## N6 (C pour le rang 1, hérité de BSTW) — B pour la tordue g_K aux premiers de D_K

**Objection.**
- Le rang 1 utilise le Th. 10.1 pour g_K = g ⊗ χ_K (K corps de Heegner), de niveau N·D_K². En ℓ \| D_K, ρ̄_K\|I_ℓ = χ_K ⊕ χ_K est scalaire.
- Des formes de même conducteur ℓ² et d'un autre type peuvent être congruentes à g_K. C'est le cas du type χ_K ⊗ St si a_ℓ(E) ≡ ±(ℓ + 1) mod 5. C'est aussi le cas de types modérés si ℓ ≡ ±1 mod 5 : caractères d'ordre 5 de ℤ_ℓ^×, ou supercuspidales de niveau zéro.
- C'est le phénomène de N2, en des premiers ℓ \| D_K que l'on ne contrôle pas : D_K provient du théorème de non-annulation de [51].

**Traitement.**
- **BSTW rencontrent exactement le même point** dans le cas sans facteur carré publié. Leur Th. 10.5 affirme « the same holds for g_K », et la preuve applique [116] (PW, niveau sans facteur carré) sans autre justification, alors que g_K est de niveau N·D_K². L'objection est donc **héritée** : notre extension n'ajoute rien en ℓ \| D_K.
- Piste. Par torsion par χ_K, global et non ramifié hors de D_K, les formes congruentes à g_K de niveau N·D_K² correspondent aux formes congruentes à g de niveau N·D_K². Pour g, ce sont des cas non minimaux (m_ℓ = 2), traités par CH avec Σ ∋ ℓ via [Tay06 §3] et [Dia97b]. Il faut en plus un argument d'invariance par torsion de l'égalité Ω_{N⁻} ~ Ω_can.
- Ce point est **à soumettre en priorité** aux spécialistes de B (Hsieh, Kim–Ota, Pollack–Weston).

**Statut.** Ouvert, hérité de BSTW. Le rang 0 (Th. 1.6) n'est pas concerné.

---

## N7 (I) — Cohérence de la condition (iv) de CLW en v = ℓ (premier auxiliaire décomposé)

**Objection.**
- CLW imposent (iv) aussi en v = ℓ, le premier décomposé auxiliaire où π_ℓ est non ramifiée : χ_{θ,𝔩} doit être non ramifié.
- Ils tordent ensuite χ_θ et χ_h par un caractère ν de conducteur ℓ-primaire. La contrainte χ_hχ_θ\|_{A_ℚ^×} = 1 force ν²\|_{A_ℚ^×} = 1, donc ν\|_{ℤ_ℓ^×} d'ordre ≤ 2. Si ν est ramifié en 𝔩̄ avec un grand conducteur, il l'est aussi en 𝔩, et χ_{θ,𝔩} cesse d'être non ramifié.
- Je ne vois pas comment (iv) en v = ℓ reste vraie après la torsion. C'est peut-être une imprécision de rédaction, ou une lecture fautive de ma part.
- Avec (iv) telle quelle, la Prop. V annule aussi l'intégrale en v = ℓ dès que a ≥ 3.

**Traitement.**
- La Prop. R′ s'applique en v = ℓ à condition que les vecteurs de θ et h y soient des f_χ du Lemme 8.13. Le Lemme 8.13 ne demande **pas** χ_{θ,1} non ramifié, seulement cond(χ_{θ,1}χ_{θ,2}^{-1}) = t₁.
- On prend A = ((χ_hχ_θ^c)_𝔩)^{-1}\|_{O^×}, qui ne dépend pas de ν si ν est anticyclotomique. On prend aussi t₁ ≥ n₀(A).
- Mais la forme exacte du vecteur de θ en ℓ, quand χ_{θ,𝔩} est ramifié, n'est pas donnée par CLW Prop. 7.7.3.

**Statut.** Ouvert. **Question à ajouter pour Wan** : comment (iv) en v = ℓ est-elle compatible avec la torsion par ν ?

---

## N8 (I) — Admissibilité de φ_A dans l'espace (5.6.12′)

**Traitement.**
- φ_A est propre pour K₀(ϖ^{n₀}), de caractère A^{-1}(a)A(d). Ce caractère est trivial sur le sous-groupe de congruence principal de niveau max(n₀, cond A). On a donc φ_A ∈ π^{K_v} dès que 2c_v + ord(δs) ≥ max(n₀, cond A).
- (5.6.6) ne donne qu'une borne inférieure sur c_v (objection 5).
- φ_A ne dépend pas de τ.

**Statut.** Réglée.

---

## N9 (M) — Le chiffrage

On recalcule la borne avec :
- Prop. R′ : tous les types en 2 et 3 sont admis côté A ;
- exclusions côté B : E1, E2, E3 en 2 et 3 (N2) et les cellules indéterminées ;
- ε pour q ≥ 7, comme avant.

Résultats (`bound_v3.py`, `bsd/results/bound_v3.json` ; types locaux `local_types_v3_l2_k8.json`, `local_types_v3_l3_k7.json`).

**Types locaux.**

| ℓ | E1 (mult., 5 \| v(Δ)) | E2 (St tordu, 5 \| v(j)) | E3 (SP quadratique, a_ℓ(E^d) ≡ ±(ℓ+1)) | indéterminé | μ_ℓ côté B |
|---|---|---|---|---|---|
| 2 (k = 8) | 0 | 0 | 3,177 % | 0,040 % | 0,96783 |
| 3 (k = 7) | 0 | 6·10⁻⁷ | 0,274 % | 0,006 % | 0,99720 |

E1 est nul en pratique. Dans la normalisation de BSZ (y² = x³ + Ax + B), on a c₄ = −48A, donc 3 \| c₄ et 2 \| c₄. La réduction multiplicative en 2 ou 3 n'apparaît que pour des modèles non minimaux, déjà rares.

**Bornes.**

| Scénario | Hypothèses | Borne |
|---|---|---|
| S3_prudent | A : tous types (Prop. R′) ; B : sans E1-E3 ni indéterminées ; ε (q ≥ 7) | **78,61 %** |
| S3_optimiste | A et B : tous types (CH avec Σ ≠ ∅ via [Dia97b], plus invariance par torsion) ; ε | **79,03 %** |
| référence | table d'origine | 79,03 % |

Aujourd'hui (BSZ + BSTW + Castella) : 67,02 %.

---

## N10 (I) — Les deux rangs sont nécessaires au facteur 19/24

**Objection.** BSZ Th. 25 minore la proportion de 5-rang de Selmer 0 **ou** 1. Il ne donne aucune minoration du rang 0 seul : la moyenne 6 est compatible avec x₀ = 0 et x₁ = 19/20. Le gain dépend donc du rang 1, c'est-à-dire de N6.

**Statut.** Constat. Le chiffrage est conditionnel à N6, au même titre que celui de BSTW pour ses propres courbes semistables.

---

## Bilan du deuxième tour

| N° | Gravité | Statut |
|---|---|---|
| N1 | C | ouvert, sans effet sur la borne (A résolu dans les deux lectures) |
| N2 | C (chiffrage) | réglée par exclusion (coût : voir bilan) |
| N3 | I | en partie ; [Hsi12] à lire |
| N4 | I | réglée |
| N5 | I | établi chez Wan et vérifié ; preuve refaite en partie |
| N6 | C (rang 1) | ouvert, **hérité de BSTW** |
| N7 | I | ouvert : question à Wan |
| N8 | I | réglée |
| N9 | M | recalculé |
| N10 | I | constat |

**Troisième tour.** Il n'apparaît pas de nouvelle objection critique qui ne soit pas héritée de BSTW, ou qui ne soit pas une question de lecture de CLW (N1, N7). Conformément à la règle « s'arrêter si deux étapes n'apportent rien », je m'arrête ici. Je passe à la rédaction du document anglais, qui liste N1, N3, N6 et N7 comme points ouverts.

---

## Mise à jour (27/11, après les articles fournis par l'utilisateur)

- **Casselman, Math. Ann. 201 (1973)**, lu sur les images p. 301-304. Th. 1 : l'espace des v tels que ρ(g)v = ε(d)v sur Γ₀(𝔠) est non nul exactement pour 𝔠 ⊆ 𝔠(ρ), et de dimension 1 en 𝔠(ρ). Le Lemme p. 303 fait l'échange a ↔ d par H. **La théorie des formes nouvelles utilisée dans la Prop. V est maintenant ÉTABLIE sur source.**
- **N3 RÉGLÉE.** Hsieh, *On the non-vanishing of Hecke L-values modulo p* (= [Hsi12], fichier NVCMv2). Le Th. B, utilisé par CLW, suppose : (unr), (ord), (pl, D_{K/F}𝔠) = 1, (L) μ_p(χ_v) = 0 aux places inertes et ramifiées du conducteur, et (N) χ non résiduellement autodual. **Aucune condition sur la partie décomposée du conducteur.**
- **Objection 20 RÉGLÉE (autrement que chez BSTW).** Bump–Friedberg–Hoffstein, Invent. Math. 102 (1990), Théorème (ii), lu p. 543-544. Pour f newform de niveau M **quelconque**, de signe ε, et S fini contenant les premiers divisant M, il existe D fondamental avec εD > 0, tout premier de S décomposé dans ℚ(√D) et L(k/2, f, χ_D) ≠ 0. Avec ε = −1 et 5 ∈ S, c'est exactement le corps de Heegner de BSTW Th. 12.3. (BSTW citent Friedberg–Hoffstein 1995, non fourni ; BFH 1990 suffit.)
- **N2 (minimalité), éclairage.** Wiles, Annals 141 (1995), Ch. 1 : en q ≠ p, les déformations standard sont de types (A) (Steinberg), (B) (ρ₀\|I_q = χ_q ⊕ 1, χ_q ≠ 1) et (C) (H¹(ℚ_q, W_λ) = 0). L'inertie résiduelle scalaire χ ⊕ χ du cas E3 n'en fait pas partie : il faut [Dia97a], toujours manquant. L'exclusion prudente de E1-E3 reste donc justifiée.
- Genestier–Tilouine (Astérisque 302) porte sur GSp₄ et ne remplace pas Diamond 1997a/b.
- **Toujours manquants** : la version publiée de CLW (Forum Math. Sigma 2022), Diamond 1997a (Déf. 3.1) et Diamond 1997b (Th. 2.4).
