# Cartographie de la littérature, rang analytique ≥ 2

Lu le 2026-11-26. Chaque article a été téléchargé depuis arXiv ou la page de l'auteur, converti en texte (`lit/raw/*.txt`, non versionnés) et lu à l'endroit indiqué. Étiquettes : **ÉTABLI** (énoncé lu dans l'article cité), **SECONDAIRE** (lu dans un autre article qui le cite, source primaire non ouverte), **SPÉCULATION** (interprétation de ma part).

## 1. Conjecture de Kolyvagin

**Énoncé (Kolyvagin 1991, d'après BCGS, intro p. 2).** Soit K imaginaire quadratique où tout ℓ | N est décomposé (hypothèse de Heegner). Les classes de Kolyvagin κ_n ∈ H¹(K, T/I_nT), dérivées des points de Heegner sur les corps de classes d'anneau K[n], ne sont pas toutes nulles. κ_1 est l'image de Kummer du point de Heegner P_K, et κ_1 ≠ 0 ⇔ L′(E/K, 1) ≠ 0 (Gross–Zagier).

**Ce qu'elle donne en rang ≥ 2.** Si on pose ord(κ) = min{ν(n) : κ_n ≠ 0} (ν = nombre de facteurs premiers), on a
max(r⁺, r⁻) = ord(κ) + 1, où r^± est le corang des parties ± du Selmer p^∞ de E/K
(BCGS, Corollaire A ; Sweeting, Corollaire B). La conjecture décrit donc le **rang du Selmer**, mais ne fabrique pas de points rationnels.

| Résultat | Hypothèses | Statut |
|---|---|---|
| W. Zhang 2014 (Camb. J. Math.) | p ∤ 6N bon ordinaire, ρ̄_{E,p} surjective, hypothèses de ramification | SECONDAIRE (BCGS p. 2, Sweeting §1.1) |
| Sweeting, arXiv 2012.11771 v3 (nov. 2022), Thm A | Heegner généralisée N = N⁺N⁻, ν(N⁻) pair, p ∤ 2N·disc K, image contenant un scalaire, T̄_f absolument irréductible (p = 3 : non induite de ℚ(√−3)), condition ♦ si p inerte ou a_p non unité | ÉTABLI |
| Burungale–Castella–Grossi–Skinner, arXiv 2312.09301 v2 (18 janv. 2026), Thm A | p impair bon ordinaire **décomposé dans K**, (Heeg), D_K impair ≠ −3, E(K)[p] = 0, **et** la conjecture principale anticyclotomique rationnelle 1.2.10. Inconditionnel si p > 3 et E[p] irréductible, ou si p est d'Eisenstein avec φ restreint à G_p ≠ 1, ω (via CGS25, BCS25) | ÉTABLI |
| BCGS Thm B (raffinement de Zhang : M_∞ = Σ ord_p(c_ℓ)) | p > 3, ρ̄ surjective, conjecture principale intégrale, paramétrisation p-optimale | ÉTABLI |
| BCGS Thm C (système de Kolyvagin de Kato non nul) | E sans CM, p impair bon ordinaire, E(ℚ_p)[p] = 0, conjecture principale cyclotomique rationnelle ; alors ord(κ^Kato) = corang du Selmer fin | ÉTABLI |

**Correction au document.** BCGS est une prépublication arXiv (v2 du 18 janvier 2026), pas un article publié en revue à ma connaissance ; sa conclusion « inconditionnelle » repose sur deux autres prépublications (CGS25, BCS25) que je n'ai pas ouvertes.

**Ce qui reste ouvert (SPÉCULATION, d'après la structure des énoncés).** Passer de « rang du Selmer = ord(κ) + 1 » à « rang de Mordell–Weil = ordre d'annulation de L » demande (a) la finitude de Ш[p^∞] et (b) un lien entre ord(κ) et ord_{s=1} L(E, s). Aucun des articles lus ne relie ord(κ) à L″(E, 1).

## 2. Classes de Kato généralisées (Darmon–Rotger)

**Conjecture (Darmon–Rotger, cas rang 2, Castella–Hsieh, Conj. 1.2, p. 3).** Soit K imaginaire quadratique, p > 2 bon ordinaire décomposé dans K, χ un caractère d'anneau de classes avec χ(𝔭) ≠ ±1. On suppose L(E^K, 1) ≠ 0 et L(E/K, χ², 1) ≠ 0. Alors sont équivalents : (1) les quatre classes κ_{α,α⁻¹}, … ∈ Sel(ℚ, V_pE) engendrent un sous-espace non nul ; (2) dim Sel(ℚ, V_pE) = 2 ; (3) rang E(ℚ) = 2 ; (4) ord_{s=1} L(E, s) = 2.

| Résultat | Hypothèses | Conclusion | Statut |
|---|---|---|---|
| Castella–Hsieh, arXiv 1809.09066 v4 (juillet 2019), Thm A | L(E^K,1) ≠ 0, L(E/K,χ²,1) ≠ 0, ρ̄_{E,p} irréductible, N⁻ sans carré, ρ̄ ramifiée en tout q \| N⁻ | κ_{α,β⁻¹} = κ_{β,α⁻¹} = 0, et κ_{α,α⁻¹} ≠ 0 ⇔ dim Sel_str(ℚ, V_pE) = 1 | ÉTABLI |
| Castella–Hsieh, Cor. B | idem, + rang 2 et Ш[p^∞] fini | κ_{α,α⁻¹}, κ_{β,β⁻¹} ≠ 0 engendrent Sel_str | ÉTABLI |
| Castella–Hsieh, Cor. C | idem | κ_{α,α⁻¹} ≠ 0 ⇒ dim Sel(ℚ, V_pE) = 2 (analogue rang 2 de Kolyvagin) | ÉTABLI |
| Castella, arXiv 2204.09608 v3 (13 févr. 2026), Thm B | E **à CM**, p ≥ 5 bon ordinaire décomposé dans le corps CM, L(E, s) d'ordre pair > 0 | κ_p ≠ 0 ⇒ dim Sel = 2 ; si dim Sel = 2, κ_p ≠ 0 ⇔ res_p ≠ 0 | ÉTABLI |
| Castella, Thm C | + Ш[p^∞] fini, ord L_p(s) = 2, ord L*_p(s) = 1 | base explicite de Sel : κ_p et une unité elliptique dérivée | ÉTABLI |

Ces classes vivent dans le **Selmer p-adique**, pas dans E(ℚ) : elles bornent ou engendrent le Selmer, elles ne donnent pas de point rationnel (Castella–Hsieh le disent eux-mêmes, Question 1.1, p. 2 : « a stumbling block in this setting is the lack of a systematic construction of algebraic points »).

**Point utile pour le calcul (Castella 2204.09608, Remarque 1.3.1, p. 6).** Dans le cas CM, dim Sel(ℚ, V_pE) = 2 ⇒ ord L_p ≥ 2, avec égalité si et seulement si la hauteur p-adique est non dégénérée (Perrin-Riou). C'est exactement ce que la mission 2 teste numériquement, dans le cas non CM.

## 3. Conjecture de Perrin-Riou

**Théorème A de Bertolini–Darmon–Venerucci** (« Heegner points and Beilinson–Kato elements: a conjecture of Perrin-Riou », PDF sur la page de H. Darmon, p. 2). Soit A/ℚ semistable en un premier impair p, avec L(A, 1) = 0. Il existe P ∈ A(ℚ) tel que (1) P est d'ordre infini si et seulement si L(A, s) a un zéro simple en 1 ; (2) log_{ω_A}(res_p ζ_A^Kato) = log²_{ω_A}(P) à un rationnel non nul près. ÉTABLI.

Le cas multiplicatif déployé est traité par Venerucci (BDV §1.3, p. 7, citant [Ven16]) : SECONDAIRE. Le cas CM ordinaire était connu par Perrin-Riou, Rubin et Bertrand (BDV §1.3) : SECONDAIRE.

**Conséquence en rang 2 (SPÉCULATION, mais directe).** Si ord_{s=1} L ≥ 2, alors P est de torsion et log(res_p ζ^Kato) = 0. L'élément de Kato de base est donc localement trivial en p et ne voit pas le rang 2. Il faut passer à ses dérivées de Kolyvagin (BCGS Thm C) ou aux classes de Darmon–Rotger. C'est le pendant, côté Kato, du verrou des points de Heegner décrit dans le document.

## 4. Conjecture principale cyclotomique (utile pour la mission 2)

**BCGS, Théorème 3.2.6, p. 24.** Soit p > 2 bon ordinaire. Si E[p] est irréductible, la conjecture principale cyclotomique **rationnelle** est vraie : char_Λ X_ord(E/ℚ_∞) = (L_p^MSD) dans Λ ⊗ ℚ_p (preuve attribuée à [Wan15]). Si E[p]^ss = 𝔽_p(φ) ⊕ 𝔽_p(ψ) avec φ restreint à G_p ≠ 1, ω, la conjecture intégrale est vraie ([CGS25]). ÉTABLI (énoncé lu ; les preuves sont dans les articles cités, non ouverts).

## 5. Vérifications de BSD par calcul

**Banwait–Huang, arXiv 2601.16044 v3 (4 juin 2026)**, introduction p. 1 : « the full BSD conjecture holds for all elliptic curves over ℚ with analytic rank 0 or 1 of conductor up to 5,000 » ; 31 073 courbes de conducteur < 5000, dont 691 de rang analytique > 1, soit ≈ 97,78 % vérifiées. SECONDAIRE (ils renvoient à la fin de la section 5 de leur référence [27] pour la preuve).

**Correction au document.** Le sujet principal de cet article n'est pas ce comptage. Il identifie toutes les courbes de conducteur ≤ 500 000 qui ont une infinité de tordues quadratiques satisfaisant BSD forte (méthode de Burungale–Skinner–Tian–Wan).

## 6. Articles cités dans le document mais non ouverts ici

- W. Zhang, « Selmer groups and the indivisibility of Heegner points » (2014) : pas sur arXiv sous ce titre ; contenu connu ici seulement par BCGS et Sweeting.
- Jetchev–Lauter–Stein (arXiv 0707.0032) et Venerucci (air.unimi.it) : non relus dans cette session.
- Stein–Wuthrich, « Algorithms for the arithmetic of elliptic curves using Iwasawa theory » : absent d'arXiv. À ma connaissance, il emploie déjà l'argument de la section « Certification » du rapport (fonction L p-adique et théorème de Kato ⇒ finitude de Ш[p^∞]). **Non ouvert : ne pas le citer comme source avant lecture.**
