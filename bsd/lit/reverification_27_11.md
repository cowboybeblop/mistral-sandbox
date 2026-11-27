# Revérification (27 novembre) : Lemme 8.14 de Wan, recette de CLW aux places décomposées, Proposition R

Demande de l'utilisateur : revérifier les trois affirmations « le Lemme 8.14 de Wan est faux tel qu'énoncé », « la recette de CLW pourrait avoir une lacune aux places décomposées » et « la Proposition R la corrigerait ». Sources rouvertes pour cette note : Wan 1408.4044 §8D (texte p. 80-84) ; CLW 2109.08375 §5.6 (p. 35-36, conditions (i)-(vi), (5.6.6)-(5.6.12), Rem. 5.6.2) et p. 72 (intégrales locales) ; BSTW 2409.01350 (Th. 9.24, note 20, Th. 10.5) ; Hu, IMRN 2018 (2.63)-(2.65).

**Résultat de la revérification.**
- Les trois affirmations **tiennent**.
- Les deux premières ont maintenant une **preuve analytique courte**, qui ne dépend plus d'aucun calcul numérique (§1, §2).
- La troisième a une **preuve plus simple et plus générale** qu'au §13 de `probleme_A_note.md` (§4). Elle n'utilise plus ni l'équation fonctionnelle ni la formule (2.66) de Hu. Elle n'exige plus L(π_v ⊗ A) = 1, et elle permet A trivial.
- Une réserve demeure sur la deuxième affirmation (§3).

Contrôles numériques : `bsd/scripts/verif_27.py`, sortie dans `bsd/results/verif_27.txt`.

---

## 1. Le Lemme 8.14 de Wan est faux tel qu'énoncé (DÉDUCTION, preuve complète, confirmée numériquement)

**Énoncé (ÉTABLI, lu p. 82).** On suppose cond(χ₁χ₂^{-1}) = (ϖ^t), t > 0, et ϑ de conducteur (ϖ^s) avec s > t. Pour k = (a b ; 0 d)(1 0 ; c 1), on pose :
- f = f_{χ,ϑ}(k) = χ₁(a)χ₂(d)ϑ(c/ϖ^t) si a, d ∈ ℤ_v^×, b ∈ ℤ_v et c ∈ ϖ^tℤ_v^× ;
- f = 0 sinon ;
- f̃ = f̃_{χ^{-1},ϑ^{-1}}.

Le lemme affirme : « if g ∈ K_{t+s} with Φ_{f,f̃}(g) ≠ 0, then its upper right entry is divisible by ϖ^{s−t} ». Ici Φ(g) = ∫_K f(kg)f̃(k)dk, et K_t est le groupe des matrices de GL₂(ℤ_v) triangulaires supérieures modulo ϖ^t (c'est K₀(ϖ^t)).

**Calcul.** On prend g = n(b) = (1 b ; 0 1), qui appartient à K_{t+s}.
- Si k = q·n⁻(c) avec c ∈ ϖ^tℤ_v^×, alors n⁻(c)n(b) = (1/(1+cb), b ; 0, 1+cb)·n⁻(c/(1+cb)).
- On a v(cb) ≥ t et cond(χ₁^{-1}χ₂) = t, donc (χ₁^{-1}χ₂)(1+cb) = 1.
- Il reste Φ(n(b)) = C·∫_{u∈ℤ_v^×} ϑ^{-1}(1 + ϖ^t b u) du.
- Si v(b) = j, l'ensemble {1 + ϖ^tbu} est (1 + ϖ^{t+j}O) ∖ (1 + ϖ^{t+j+1}O). ϑ est non trivial sur 1 + ϖ^mO si et seulement si m < s. On obtient donc :

| v(b) | Φ(n(b))/Φ(1) |
|---|---|
| ≥ s − t | 1 |
| = s − t − 1 | −1/(q − 1) |
| < s − t − 1 | 0 |

**Conclusion.** Pour **tout** s > t, b = ϖ^{s−t−1} donne Φ(n(b)) ≠ 0 alors que ϖ^{s−t} ∤ b. L'énoncé de support du Lemme 8.14 est faux. Le cas testé le 26/11 (t = 1, s = 2, b unité, rapport −1/2) en est le cas particulier s = t + 1, q = 3.

**Vérification** (`verif_27.py`, partie a, p = 3, rapports exacts) :

| (t, s) | v(b) = s − t − 1 | v(b) = s − t | prédiction |
|---|---|---|---|
| (1, 2) | −0,500000 | +1,000000 | −1/2, 1 |
| (1, 3) | −0,500000 (et 0 en v(b) = 0) | +1,000000 | −1/2, 1 |
| (2, 3) | −0,500000 | +1,000000 | −1/2, 1 |

Cela recoupe les deux méthodes indépendantes du 26/11 : intégration dans la carte n⁻ et somme exacte sur GL₂(ℤ/27).

---

## 2. La valeur annoncée par le Lemme 8.17 est incompatible avec la théorie des représentations (DÉDUCTION, preuve complète)

Ce point est **plus fort que le §1 et ne dépend pas de lui**.

**Énoncé (ÉTABLI, lu p. 83).**
- Hypothèses : t₁ < s < t₂, avec t₁ + s = t₂ si t₁ ≠ 0 et s + 1 = t₂ si t₁ = 0 ; cond(χ_{f,1}χ_{f,2}^{-1}) = ϖ^{t₁} ; cond ϑ = ϖ^s ; cond(χ_{θ,1}χ_{θ,2}^{-1}) = cond(χ_{h,1}χ_{h,2}^{-1}) = ϖ^{t₂}.
- Conditions sur les caractères : χ_{f,1}χ_{θ,1}χ_{h,1}ϑ = 1 et χ_{f,2}χ_{θ,2}χ_{h,2}ϑ^{-1} = 1. Le signe −1 sur le second ϑ est **forcé** : sans lui, le caractère central du triplet vaudrait ϑ^{-2} ≠ 1, et aucune forme trilinéaire invariante n'existerait.
- Vecteurs : f_{χ_f,ϑ} (Lemme 8.14, ou sa variante p. 82 si t₁ = 0), f_{χ_θ} et f_{χ_h} (Lemme 8.13).
- Conclusion annoncée : I_v = (q_v − 1)²/q_v^{2s+1}·Vol(K₁)²Vol(K_{t₂})² ≠ 0.

**Proposition V.** Avec ces vecteurs, **I_v = 0** dès que s > t₁ (si t₁ ≠ 0), ou dès que s ≥ 2 (si t₁ = 0).

*Preuve.*
1. Le vecteur f_χ du Lemme 8.13, supporté sur K_{t₂}, est propre pour K_{t₂} : π(k)f_χ = χ₁(a_k)χ₂(d_k)f_χ. On a χ₁(a)χ₂(d) = χ₁(det k)·(χ₁^{-1}χ₂)(d), et le second facteur ne dépend que de d mod ϖ^{t₂}. Donc f_θ ⊗ f_h est propre pour K_{t₂}, de caractère Ξ(k) = (χ_{θ,1}χ_{h,1})(a)(χ_{θ,2}χ_{h,2})(d) = (χ_{f,1}ϑ)^{-1}(a)·(χ_{f,2}ϑ^{-1})^{-1}(d).
2. L'intégrale d'Ichino est invariante par l'action diagonale de G sur (φ₁, φ₂, φ₃) : on change de variable g ↦ gk. En moyennant sur k ∈ K_{t₂}, on obtient I_v(φ ⊗ f_θ ⊗ f_h, …) = I_v(Pφ ⊗ f_θ ⊗ f_h, …), où P est le projecteur sur les vecteurs de π_f de type Ξ^{-1}(k) = (χ_{f,1}ϑ)(a)(χ_{f,2}ϑ^{-1})(d).
3. Ce sous-espace isotypique est **nul**.
   - Un vecteur de K₀(ϖ^n)-type μ₁(a)μ₂(d) dans π est, dans π′ = π ⊗ μ₂^{-1}, un vecteur de type ω_{π′}(a).
   - Par la théorie de Casselman, un tel vecteur existe si et seulement si n ≥ c(π′). La convention {a ≡ 1} ou {d ≡ 1} est indifférente, puisque l'élément d'Atkin–Lehner normalise K₀(ϖ^n) et échange a et d.
   - Ici π′ = π(χ_{f,1}χ_{f,2}^{-1}ϑ, ϑ). On a cond(χ_{f,1}χ_{f,2}^{-1}) = t₁ < s, donc les deux caractères ont le conducteur s, et c(π′) = 2s.
   - Or 2s > t₂, puisque t₂ = t₁ + s < 2s si t₁ ≠ 0, et t₂ = s + 1 < 2s si s ≥ 2.
4. Donc Pφ = 0 pour tout φ, et I_v = 0. ∎

**Remarques.**
- Le résultat est **indépendant du vecteur choisi dans π_f** : il ne dépend que de f_θ ⊗ f_h. Le seul cas non nul est t₁ = 0, s = 1 (π_f non ramifiée, t₂ = 2).
- C'est le « lemme du §4 » de `probleme_A_note.md`, appliqué ici à l'énoncé même de Wan.
- L'origine probable de l'erreur : le lemme traite f_{χ,ϑ} comme s'il était propre pour K_{t+s}, de type (χ₁ϑ)(a)(χ₂ϑ^{-1})(d). C'est ce que suggère la seconde phrase du Lemme 8.14. Un tel vecteur n'existe pas dans π : il lui faudrait un niveau 2s > t + s.
- Le contre-exemple du §1 est la trace de cette non-propreté.

---

## 3. Ce que cela implique pour CLW et BSTW (DÉDUCTION, avec une réserve)

**Ce que disent les textes (ÉTABLI, lu).**
- CLW p. 72, places v ∈ Σ_s ∪ {ℓ} : « this is [Wan20, Lemmas 8.13-8.17]. Note that the twist at v ∈ Σ_s ∪ {ℓ} in (5.6.10) guarantees that the local integrals are nonzero constants ».
- Wan, Rem. 8.19 : « The reason why the local integrals at split primes showing up in the triple product formula later on are the ones considered in this subsection is a consequence of the computations in Subsection 6.7 ».
- CLW (5.6.10) : f^{GU(2)}_{χ_h} = ∏_v Σ_{n∈(ℤ_v/q_v^{t_v})^×} χ_{h,v̄}(−n) R((1 0 ; n 1)(q_v^{−t_v} 0 ; 0 1)) f^{GU(2)}, avec t_v = ord cond χ_{h,v̄}. C'est exactement la somme des Lemmes 8.16 et 8.18 de Wan. Le vecteur de π aux places décomposées est donc f_{χ,ϑ}, avec ϑ = χ_{h,v̄} et s = t_v.
- BSTW, preuve du Th. 9.24 et note 20 : « The square-free-ness was assumed in loc. cit. for explicit calculation of local triple product periods. However, at any prime dividing D_K, the local automorphic representation associated to g is principal series, and the computation of the local period has already appeared in [141, §8D] ».

**Conséquence.** Si les vecteurs de θ et h aux places décomposées sont ceux du Lemme 8.17 (même orientation), la Prop. V s'applique avec t₂ = a = ord cond χ_{θ,v̄} et s = ord cond((χ_hχ_θ^c)_v), fixé par (iv). Ce point est affirmé par Wan (Rem. 8.19), cité par CLW, et c'est la lecture (L1) obtenue au §12 de `probleme_A_note.md` à partir des fonctions de Schwartz de CLW (7.1.6). On obtient :

| π_v en v ∈ Σ_s | (iv) de CLW | c(π_v ⊗ A) | intégrale locale |
|---|---|---|---|
| non ramifiée | s = a − 1, a ≥ 2 | 2(a − 1) | nulle si a ≥ 3 ; non nulle si a = 2 |
| Steinberg (c = 1) | s = a − 1, a ≥ 4 | 2(a − 1) > a | **nulle** |
| série principale ramifiée (c ≥ 2) | s = a − c, a ≥ 2c + 2 | 2(a − c) > a | **nulle** |
| supercuspidale (c ≥ 2) | s = a − c, a ≥ 2c + 2 | 2(a − c) > a (cond A > c/2) | **nulle** (c'est le problème A d'origine) |

Pour BSTW, les places décomposées de Σ_s contiennent les premiers multiplicatifs de N/q (tous décomposés dans le corps auxiliaire L″, preuve du Th. 10.1). D'après le Lemme 20 de BSZ, il y en a au moins un pour 100 % des courbes. Elles contiennent aussi les premiers de D_K pour la tordue g_K. **Si (L1) est la bonne lecture, l'argument publié de CLW, et donc BSTW Th. 1.6 et 12.3, a une lacune en ces places**, même en conducteur sans facteur carré. Il ne s'agit pas d'une erreur sur l'énoncé final, mais d'une étape de preuve.

**Réserve (pourquoi « pourrait »).** La Prop. V porte sur l'énoncé du Lemme 8.17. Que les vecteurs réellement produits par la construction globale (CLW Prop. 7.7.1 et 7.7.3, Wan §6.7) soient ceux de ce lemme est affirmé par Wan et par notre lecture, mais je ne l'ai pas démontré à partir de la correspondance thêta locale. Si les vecteurs de θ et h avaient des orientations opposées (lecture (L2)), la recette (iv) serait correcte (`probleme_A_note.md` §11.3). **C'est la question 3 posée à Wan, et elle reste la plus importante.**

---

## 4. La Proposition R corrige la lacune (DÉDUCTION, nouvelle preuve, confirmée numériquement)

**Proposition R′ (version générale).**
- **Données.**
  - v est une place décomposée, et π = π_v est générique unitaire de caractère central trivial.
  - A est un caractère quelconque de O_v^× (trivial autorisé).
  - φ_A ∈ π est le vecteur de fonction de Kirillov x ↦ A^{-1}(x)·1_{O^×}(x), et n₀ est le plus petit entier tel que φ_A soit propre pour K₀(ϖ^{n₀}).
  - f_θ et f_h sont les vecteurs f_χ du Lemme 8.13, de niveau t₁ ≥ max(n₀, 1), et le type joint Ξ de f_θ ⊗ f_h sur K_{t₁} vaut A(a)A^{-1}(d).
- **Conclusion.** I_v(φ_A ⊗ f_θ ⊗ f_h, …) = Vol(K_{t₁})·Φ_θ(1)Φ_h(1)·⟨φ_A, φ_A⟩ ≠ 0. Cette valeur est indépendante des torsions non ramifiées de θ et h, et donc de τ.

*Preuve.*
- **(0) φ_A est bien défini et propre.**
  - Dans π ⊗ A, la fonction 1_{O^×} est fixée par n(O), car ψ est non ramifié (Hu (2.64)), par diag(O^×, 1), et par n⁻(ϖ^nO) pour n grand, par lissité. Le centre agit par A² = ω_{π⊗A}.
  - Par la décomposition d'Iwahori K₀(ϖ^n) = n⁻(ϖ^nO)·T(O)·n(O), elle est propre pour K₀(ϖ^n), de type A²(d).
  - Vu dans π, le vecteur φ_A a le type A^{-1}(det)A²(d) = A^{-1}(a)A(d) = Ξ^{-1}.
  - Si L(s, π ⊗ A) = 1, φ_A est le vecteur nouveau de π ⊗ A et n₀ = c(π ⊗ A). Sinon n₀ ≤ c(π ⊗ A) + deg L(s, π ⊗ A) ≤ c + 2.
- **(1) Le produit des trois coefficients matriciels est bi-invariant.** Φ_ϕ(k₁gk₂) = Ξ^{-1}(k₁)Ξ^{-1}(k₂)Φ_ϕ(g) et Φ_θΦ_h(k₁gk₂) = Ξ(k₁)Ξ(k₂)Φ_θΦ_h(g). Le produit F est donc bi-K_{t₁}-invariant, et I_v = Σ_{x ∈ K_{t₁}\PGL₂/K_{t₁}} vol(K_{t₁}xK_{t₁})·F(x).
- **(2) Support (Wan, Lemme 8.13).** Φ_θ, et donc Φ_θΦ_h, est nul hors de ⋃_{m∈ℤ} K_{t₁}diag(ϖ^m, 1)K_{t₁}.
  - Les ensembles du Lemme 8.13 sont ces doubles classes : diag(1, ϖ^n)n⁻(ϖ^{t−n}ℤ)K_t = n⁻(ϖ^tℤ)diag(1, ϖ^n)K_t = K_tdiag(1, ϖ^n)K_t, et de même diag(ϖ^n, 1)n(ϖ^{−n}ℤ)K_t = n(ℤ)diag(ϖ^n, 1)K_t = K_tdiag(ϖ^n, 1)K_t.
  - Ce lemme est confirmé numériquement en p = 3 (t = 2) et en p = 2 (t = 3), le 26/11.
- **(3) Le coefficient de φ_A sur le tore.** Avec le produit scalaire unitaire G-invariant dans le modèle de Kirillov (Hu (2.63) et (2.65) : ⟨f₁, f₂⟩ = ∫ f₁ f̄₂ d^×x, valable pour tout π générique unitaire par le modèle de Whittaker), on a Φ_ϕ(diag(ϖ^m, 1)) = ∫ A^{-1}(ϖ^mx)1_{O^×}(ϖ^mx)·A(x)1_{O^×}(x)d^×x. C'est nul pour m ≠ 0, puisque les supports sont disjoints.
- **(4) Conclusion.** Seule la double classe K_{t₁} contribue, d'où I_v = vol(K_{t₁})·Φ_ϕ(1)Φ_θ(1)Φ_h(1). Les torsions non ramifiées sont triviales sur K_{t₁}, ce qui donne l'indépendance en τ. ∎

**Ce qui change par rapport au §13 du 26/11.**
- Le point (3) ne fait plus appel à γ monomial ni à la formule (2.66) de Hu : seul le support de Kirillov sert. Cela clôt l'objection 8 et rend caduques les objections 10 et 11.
- L(π ⊗ A) = 1 n'est plus nécessaire, et A peut être trivial. La condition sur les données devient alors « (χ_hχ_θ^c)_𝔳 non ramifié », c'est-à-dire la condition de FW étendue à toute π_v.
- **Plus aucune classification des types locaux n'est nécessaire côté A.**

**Vérification numérique du cas A trivial** (`verif_27.py`, partie b). φ est construit **dans le modèle induit**, comme combinaison de translatés du vecteur sphérique ou du vecteur nouveau. Le coefficient est calculé par intégration directe sur B\G (carte n⁻, |y| ≤ 3^{14}), donc indépendamment du modèle de Kirillov.

| π | φ | Φ_φ(diag(3^m, 1))/Φ_φ(1), m = −2, −1, 1, 2 | invariance par K₀(9) |
|---|---|---|---|
| non ramifiée, α = e^{0,7i} | f − 3^{−1/2}(α + α^{-1})π(diag(3^{−1}, 1))f + 3^{−1}π(diag(3^{−2}, 1))f | 1,5·10⁻⁸ ; 2,7·10⁻⁸ ; 8,0·10⁻⁸ ; 1,4·10⁻⁷ | exacte |
| non ramifiée, α = e^{2,1i} | idem | idem | exacte |
| Steinberg | f_new − 3^{−1}π(diag(3^{−1}, 1))f_new (appariement avec la contragrédiente, Wan p. 84) | 1,3·10⁻⁹ ; 3,9·10⁻⁹ ; 3,5·10⁻⁸ ; 1,0·10⁻⁷ | exacte |

Les résidus sont de l'ordre de l'erreur de troncature (3^{−14} ≈ 2·10⁻⁷). Le cas A ramifié était déjà vérifié le 26/11 en ℓ = 2 et ℓ = 3 (non ramifiée, Steinberg, série principale ramifiée).

**Insertion dans CLW (DÉDUCTION).** On remplace la seconde clause de (iv) par « (χ_hχ_θ^c)_𝔳·A non ramifié » pour un A choisi (A = 1 est le plus simple). On garde la première clause, χ_{θ,𝔳} non ramifié et ord cond χ_{θ,𝔳̄} ≥ 2c + 2. Celle-ci donne t₁ = a ≥ 2c + 2 ≥ c + 2 ≥ n₀, ce qui assure l'hypothèse de niveau. On remplace aussi le vecteur (5.6.10) par φ_A, ce qui est licite d'après l'objection 5 (espace (5.6.12′)). Les autres conditions de CLW (i)-(vi) sont examinées dans `relecture_adverse_2.md`, objections N3 et N4.

---

## 5. Bilan

| Affirmation | Statut au 27/11 | Base |
|---|---|---|
| Le Lemme 8.14 de Wan est faux tel qu'énoncé | **DÉDUCTION, preuve complète** (3 lignes), confirmée numériquement de trois façons | §1 |
| La valeur du Lemme 8.17 est fausse (l'intégrale est nulle) | **DÉDUCTION, preuve complète** (critère isotypique) | §2 |
| La recette de CLW a une lacune aux places décomposées ramifiées | **DÉDUCTION conditionnelle** à l'identification des vecteurs locaux de θ et h, affirmée par Wan (Rem. 8.19) et par notre lecture (L1) | §3 |
| La Prop. R′ corrige la lacune, pour toute π_v | **DÉDUCTION, preuve complète modulo le Lemme 8.13 de Wan** (vérifié numériquement), confirmée numériquement | §4 |

**Formulation honnête pour un spécialiste.** « The support statement of [Wan, Lemma 8.14] fails, and with the vectors of [Wan, Lemma 8.17] the local triple product integral vanishes identically. If these are indeed the local vectors produced at split places by the construction of [CLW, §7], the non-vanishing claimed on p. 72 of [CLW] fails at split places where π_v is ramified. A modification of the local data (Proposition R′) restores a non-zero constant, independent of the family, for every generic π_v. »
