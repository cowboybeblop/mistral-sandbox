# Problème B : tentative de preuve (cas (def)), avec liste des pas non justifiés

26 novembre 2026. **Ce n'est pas une preuve.** C'est l'assemblage proposé, étape par étape, avec la source de chaque étape et ce qui n'est pas écrit. Sources ouvertes : Chida–Hsieh (CH), arXiv 1204.2427 ; Pollack–Weston (PW), math/0610694 ; BSTW, 2409.01350 ; Hsieh, 1112.1580 ; et, via les notes de recherche, Darmon–Iovita (DI, préprint McGill) et Kim–Ota (KO), 1905.02926.

## 0. Énoncé visé

Hypothèses :
- E/ℚ, p = 5, bonne réduction supersingulière avec a_p = 0, et ρ̄ = E[5] surjective ;
- K quadratique imaginaire avec (D_K, 2N) = 1 et 5 décomposé ;
- N = N⁺N⁻, avec N⁻ produit d'un nombre impair de premiers inertes, chacun multiplicatif avec ρ̄ ramifiée, c'est-à-dire (ram) ;
- N⁺ quelconque (premiers décomposés, par exemple 2⁸ et 3^k supercuspidaux) ;
- le niveau est minimal pour ρ̄ en tout q | N⁺ (voir l'étape 4).

**But** (ce dont a besoin BSTW Th. 10.5 dans le cas (def)) : μ(L°_W(g/K)) = 0 et (L°,ac_p(g/K)) = (∏_{q|N⁻} c_q · L°_W(g/K)), pour ° ∈ {+, −}.

## Pourquoi pas la voie BDP (indef) (DÉDUCTION, vérifiée sur les textes)

Hsieh (1112.1580, Th. B) donne μ = 0 pour la fonction BDP **sans condition sur N⁺**, et sans hypothèse ordinaire sur π_p : (ord) y porte sur le type CM. Il faut toutefois (sf) 𝔫⁻ sans facteur carré et l'**Hypothèse A** (ε*(π_{E,v}, λ_v) = +1 pour v | 𝔫⁻). Or BSTW Th. 9.24, qui repose sur CLW, exige (spl) : « There exists a prime q | N⁻ ». Le cas de Heegner N⁻ = 1 est donc exclu. Pour q inerte avec π_q Steinberg et λ_q non ramifié, le signe local ε* vaut a priori −1, et l'Hypothèse A échoue. **La voie Hsieh ne couvre donc pas le cadre de BSTW.** C'est à confirmer par le calcul du signe local ; je le fais ici de mémoire, et c'est le point « Shimura curve » traité par Burungale II sous (H1). Il reste la voie (def).

## Étape 1. Éléments thêta et fonctions L± pour N⁺ quelconque

- **Construction.** DI (Th. 1.4, §2.1, d'après la note B1) travaillent avec un ordre d'Eichler ℤ[1/p] de conducteur N⁺ **quelconque**. Leurs θ_n = Σ_σ f(σ⋆v_n)σ^{-1} vérifient la relation à trois termes donnée par T_p (Prop. 2.3, Lemme 2.6). Les L^± s'obtiennent en divisant par ω̃_n^∓ (Prop. 2.8, Lemme 2.9). **ÉTABLI (secondaire, note B1).**
- **Interpolation.** CH Th. 3.11 et Prop. 4.3 donnent la formule de valeur centrale pour le vecteur p-stabilisé, **avec N⁺ quelconque**. L'hypothèse (ord) n'intervient qu'à partir du Cor. 4.5 (intégralité). **ÉTABLI (lu).** On passe aux θ_n non stabilisés de DI par la relation standard Θ_n^α = α^{-n}(θ_n − α^{-1}θ_{n−1}), avec α racine de X² + 5. On obtient ainsi l'interpolation des θ_n, donc de L^±, par L(E/K, χ, 1)/Ω_{f,N⁻}. **DÉDUCTION.**
- **Constantes locales en ℓ | N⁺.** Elles sont formées de puissances de ℓ et de facteurs ℓ ± 1, ℓ² − 1, issus des volumes et des facteurs L locaux. Pour ℓ ∈ {2, 3}, aucun n'est divisible par 5 : 1, 3, 8 et 2, 4, 8 sont premiers à 5. **DÉDUCTION, à vérifier sur la formule exacte de CH §3 (Prop. 3.8 et 3.10).**

## Étape 2. μ(θ_n mod 5) = 0 pour n ≫ 0

- **Argument de CH Th. 5.7 (ÉTABLI, lu).** On montre que Σ_τ f(x_n(aτ))χ_t(τ) ≢ 0 mod ϖ pour un a, par le Cor. 5.2 (équidistribution des points CM de Cornut–Vatsal, Prop. 5.1, pour un U ouvert compact **arbitraire**). Le Cor. 5.2 s'applique à toute forme mod ϖ **non Eisenstein**, ce que donne le Lemme 5.6 quand ρ̄ est irréductible.
- **Supersingulier (DÉDUCTION).** On applique ce même argument à f_{D₀} au lieu de f†_{D₀} = R_p(f_{D₀}). L'étape R_p (Lemme 5.8, seule étape ordinaire) disparaît, puisque f_{D₀} est non Eisenstein directement par le Lemme 5.6. On obtient μ(θ_n) = 0 pour n ≫ 0. C'est la lecture précise de « [32, §5.9] generalize immediately » (PW, preuve du Th. 2.5).
- **Hypothèses de CH à contrôler.** (ST) est automatique car (D_K, N⁻) = 1. Les conditions p > k − 2 et p ∤ 2r₀ restent à voir : r₀ vient du Th. 4.8 de CH, non relu.

## Étape 3. μ(L^±_W) = 0

PW, preuve du Th. 2.5 : θ_n est divisible par ω_n^ε, et μ(ω_n^±) = 0. Donc μ(L^±) = 0 dès que μ(θ_n) = 0 pour n ≫ 0 de parité fixée. **ÉTABLI (lu)** comme implication. Avec l'étape 2, on obtient μ(L^±_W) = 0 **avec N⁺ quelconque. DÉDUCTION.**

## Étape 4. Comparaison des périodes : Ω_{f,N⁻} ~ Ω_f^can

- **KO, Th. 6.5 et Cor. 6.7 (ÉTABLI d'après la note B2 ; KO lu par l'agent).**
  - Cadre : N⁺ arbitraire, hypothèses (CR⁺) de leur Assumption 6.3, plus (FL) et (TW).
  - Énoncé : ord_λ(Ω_f^{N⁻}/Ω_f) = Σ_{q|N⁻} t_f(q).
  - KO, Remarque 6.6(1) : le remplacement de la condition ordinaire de CH (D3) par la condition cristalline de petit poids « does not affect any of result in [CH18, §6] ». C'est une **remarque d'expert**, sans preuve détaillée.
- **Sous (ram).** t_f(q) = 0 pour q | N⁻, puisque le nombre de Tamagawa en un premier multiplicatif où ρ̄ est ramifiée est premier à p. Donc Ω_{f,N⁻} ~ Ω_f. **DÉDUCTION.**
- **Hypothèses (CR⁺) pour nos courbes (DÉDUCTION, cf. `probleme_B_note.md` §1 et §4).**
  - (4) est un coût négligeable, d'environ 5·10⁻⁶.
  - (5) demande que N_{ρ̄} et N/N_{ρ̄} soient premiers entre eux : vrai en 2 et 3 dans le cas supercuspidal (image de l'inertie d'ordre premier à 5). C'est faux pour certains Steinberg tordus avec 5 | v(j), ce qui reste marginal.
  - Premiers vexants (note B2) : ℓ ≡ −1 mod 5 avec ρ̄|G_ℓ irréductible et ρ̄|I_ℓ réductible. Ni 2 ni 3 n'en sont. Il faut vérifier les autres ℓ | N⁺ avec ℓ ≡ 4 mod 5, réduction additive.

## Étape 5. L'égalité de BSTW

L°,ac_p(g/K) est normalisée par la période canonique (Th. 6.17 et §2.2.7 de BSTW), et L°_W par Ω_{f,N⁻}. Les deux interpolent les mêmes valeurs L(E/K, χ, 1) aux mêmes facteurs d'Euler près. Leur quotient est donc (Ω_f^can/Ω_{f,N⁻}) × (constantes locales). C'est une unité par les étapes 1 et 4, au facteur ∏ c_q près, qui est une unité sous (ram). C'est exactement l'argument « in view of the interpolation formulas » de BSTW (p. 88). **DÉDUCTION.**

## Pas non justifiés (liste honnête)

1. **Étape 2 :** CH §5 adapté à f_{D₀} non stabilisé. La structure de la preuve le suggère, mais personne ne l'a écrit. Il faut aussi le lien exact entre les θ_n de DI et les sommes de CH (normalisation par a, τ, D₀ et D₁).
2. **Étape 1 :** l'interpolation des θ_n non stabilisés via CH Th. 3.11, et le caractère unité des constantes locales en 2 et 3. À vérifier sur les Prop. 3.8 et 3.10 de CH.
3. **Étape 4 :** le cristallin au lieu de l'ordinaire dans CH §6. KO l'affirment sans preuve. Il faut vérifier que le système de Taylor–Wiles de [Tay06, §2] accepte la condition plate (Taylor 2006, non ouvert) et que le critère [Dia97b, Th. 2.4] s'applique (Diamond 1997, non ouvert).
4. **Étape 5 :** la comparaison exacte des formules d'interpolation de BSTW (Th. 6.17) et de L°_W, en particulier les facteurs en p de la théorie ±.
5. **Hors B :** BSTW Th. 10.5 suppose « N square-free » à cause de Th. 9.24, c'est-à-dire du problème A. B seul ne suffit pas.

## Contre-exemple et contrôle numérique

Un contrôle numérique est envisageable pour l'étape 2 : calculer θ_n mod 5 sur l'algèbre de quaternions définie ramifiée en {q, ∞}, avec un ordre d'Eichler de niveau 2^a (matrices de Brandt), pour une courbe de conducteur 2^a·q supersingulière en 5. Il faut Sage ou Magma, absents du conteneur ; PARI n'a pas de matrices de Brandt natives. **Non fait.**
