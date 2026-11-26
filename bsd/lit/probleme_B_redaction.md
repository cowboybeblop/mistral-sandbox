# Problème B (cas (def)) : rédaction des quatre étapes et vérification sur sources

26 novembre 2026. Fait suite à `probleme_B_tentative.md`. Sources ouvertes pour cette rédaction :
- Taylor, *On the meromorphic continuation of degree two L-functions* (Doc. Math. 2006), fichier fourni ;
- Terracini, Compositio 137 (2003) ;
- Cornut–Vatsal, *CM points and quaternion algebras* (Doc. Math. 2005) ;
- Vatsal 1999 (bah) et Vatsal 2002 (*Uniform distribution*) ;
- Kim–Pollack–Weston (IJNT 2017) ;
- Chida–Hsieh, arXiv 1204.2427 (CH) ; Pollack–Weston, math/0610694 (PW) ; BSTW, 2409.01350.

Toujours introuvables : **Diamond 1997** et **Vatsal 2003 (Duke 116)**.

**Statut global : DÉDUCTION. Ce n'est pas une preuve publiée.** Chaque pas renvoie à un énoncé lu. Les pas qui restent non justifiés sont listés au §6.

## Cadre

- E/ℚ, p = 5, a_5 = 0, et ρ̄ = E[5] surjective.
- K quadratique imaginaire avec (D_K, 2N·5) = 1 et 5 décomposé.
- N = N⁺N⁻, avec N⁻ produit d'un nombre impair de premiers inertes, chacun multiplicatif, et ρ̄ ramifiée en chacun, c'est-à-dire (ram).
- N⁺ quelconque. On suppose de plus **N = N(ρ̄)**, le niveau minimal, en tout ℓ | N⁺ ; la justification est au §4.
- B est l'algèbre de quaternions définie de discriminant N⁻, et R un ordre d'Eichler de niveau N⁺.

## 1. Construction et interpolation (étape 1)

**1a. Éléments thêta.** On note f : B^×\B̂^×/R̂^× → O la forme de Jacquet–Langlands de E, primitive, c'est-à-dire non divisible par ϖ. On note P_n = P_0·diag(p^n, 1) les points CM de conductor p^n, et
θ_n = Σ_{[u] ∈ Γ_n} Σ_{τ ∈ D₁} f(x_n(uτ)) [u]_n ∈ O[Γ_n].
- Ce sont les sommes de CH (5.1) **sans** p-stabilisation (pas d'α_p) et avec χ_t = 1. Ce sont aussi les L̃_n de Darmon–Iovita, projetés de G̃_n = Γ_n × Δ sur Γ_n.
- La relation à trois termes π_{n−1}(θ_n) = a_p θ_{n−1} − ν(θ_{n−2}) vient de l'action de T_p sur l'arbre de Bruhat–Tits en p. Elle ne fait pas intervenir N⁺. (ÉTABLI selon la note B1 : DI Prop. 2.3 et Lemme 2.6 ; l'énoncé de DI autorise N⁺ arbitraire, §2.1.)

**1b. Interpolation.** CH Th. 3.11 (lu) donne P(ς^{(n)}, φ†, χ)², avec P le **vecteur p-stabilisé**, égal à
(‖φ_π‖_{Γ₀(N)}/⟨f, f⟩_R)^{-1} × (2^{2−k}(−1)^m D_K^{(k−2)/2}/√D_K) × L(1/2, π_K ⊗ χ) × e_p(π, χ)^{2−ord_p N} × L(1, τ_{K_p})² × χ(N⁺)ε(π_p) × ∏_{q|(D_K,N⁻)}(…) × (α_p²p^{-2} si s = 0, p^{-s} si s > 0).
- **ÉTABLI (lu)** : aucun facteur local n'apparaît aux premiers ℓ | N⁺, quel que soit l'exposant de ℓ dans N⁺. Le §3 de CH (Prop. 3.8 et 3.10) traite le vecteur-test à N⁺ par une normalisation qui donne une période locale égale à 1. La crainte d'une constante divisible par 5 en 2 ou 3 (tentative, étape 1) **tombe**.
- L'hypothèse (ord) de CH n'intervient pas avant le Cor. 4.5, qui traite l'intégralité. Th. 3.11 et Prop. 4.3 sont des identités valables pour toute racine α de X² − a_pX + p, ici α = ±√−5.
- **DÉDUCTION standard (Pollack, DI).** Avec Θ_n^α = α^{-n}(θ_n − α^{-1}ν(θ_{n−1})), on obtient l'interpolation des θ_n, puis celle de L^±, par L(E/K, χ, 1)/Ω_{f,N⁻}. Ici Ω_{f,N⁻} = ‖φ‖_{Γ₀(N)}/⟨f, f⟩_R est la période « de Gross ».

## 2. μ(θ_n) = 0 pour n ≫ 0 (étape 2)

On reprend la preuve de CH Th. 5.7 (lue) en supprimant R_p.
1. **Lemme 5.6 (ÉTABLI).** Si ρ̄ est irréductible et ℓ > k − 2, alors f_v = ⟨v, f̂⟩ mod λ n'est pas Eisenstein, pour tout v ≢ 0. Ici k = 2, ℓ = p = 5, et f est primitive.
2. **f_{D₀} = Σ_{d ∈ D₀} f(·d)χ_t(d).** Sous (ST), CH écrivent f_{D₀} = 2^{r₀} R′_{q₁} ∘ … ∘ R′_{q_s}(f), où r₀ = #{q | (D_K, N⁻)} = **0** ici (CH Th. 4.8, lu) et R′_q = 1 + χ(ϖ_{K_q})ϱ(ϖ_{K_q}) pour q | D_K. Le lemme de type Ihara (Lemmes 5.4 et 5.5, invoqués dans la preuve du Lemme 5.8) montre que f_{D₀} n'est pas Eisenstein. **Ces étapes n'utilisent ni p ni l'hypothèse ordinaire** : ce sont des opérateurs en q | D_K. (ÉTABLI pour la structure ; les Lemmes 5.4 et 5.5 n'ont pas été relus ligne à ligne.) La condition p ∤ 2r₀ du Th. 5.7 est vide.
3. **Équidistribution.** CH Prop. 5.1 est « [CV05, Corollary 2.10] with S = {∅} and R = D₁ ». Cornut–Vatsal, Cor. 2.10 (lu) dit : « For all but finitely many x in 𝐇, Red(G·x) = C^{-1}(G·x̄) in X_H(S, R) ». L'énoncé vaut pour **tout sous-groupe ouvert compact H** de G(A_f) (§2.2.3, « Let H be a compact open subgroup of G(A_f) »). On prend H = R̂^×, d'où **N⁺ arbitraire. ÉTABLI.**
4. **CH Cor. 5.2 (ÉTABLI, lu).** Pour f ∈ M₂(U, A) non Eisenstein avec N(U) ⊃ ∏_{q|D_K} ℤ_q^×, et des β_τ dont au moins un est une unité, on a Σ_τ β_τ f(x_n(aτ)) ≠ 0 pour un a et pour n > n₀. La preuve n'utilise que la Prop. 5.1 et le fait que les P_n sont distincts dans K̂^×\B̂^×/R̂^×. Ce dernier point vaut pour R̂ maximal en p, puisque les P_n sont à distance n sur l'arbre.
5. **Conclusion.** On applique 4 à f_{D₀} (non Eisenstein par 2) avec β_τ = 1. On obtient θ_n ≢ 0 mod ϖ pour n > n₀, c'est-à-dire **μ(θ_n) = 0. DÉDUCTION** : transcription de CH §5.4 sans R_p. Dans CH, R_p ne sert qu'à passer de f_{D₀} à f†_{D₀} (Lemme 5.8), étape qui disparaît ici.

## 3. μ(L^±_W) = 0 (étape 3)

PW, preuve du Th. 2.5 (lue) : « L_n is divisible by ω_n^ε » et « µ(ω_n^±) = 0 », donc μ(L^±) = 0 dès que μ(L_n) = 0 pour n grand. Avec le §2 : **μ(L^±_W) = 0 pour N⁺ quelconque. DÉDUCTION** ; l'implication de PW est ÉTABLIE.

## 4. Comparaison des périodes : Ω_{f,N⁻} ~ Ω_f^can (étape 4)

**4a. Réduction au cas minimal.** Sous N = N(ρ̄) en N⁺ et (ram) en N⁻, on a N = N_∅ dans les notations de CH §6, donc Σ = ∅. CH Prop. 6.1 se réduit alors à la Prop. 6.8 pour Σ = ∅ : « S_∅ is a free T_∅-module of rank one », puis à l'argument final avec Jacquet–Langlands, qui est un isomorphisme puisque N⁻ | N_{ρ₀}. **Ni les montées de niveau (Lemmes 6.3, 6.4, Cor. 6.7), ni le Th. 2.4 de Diamond 1997b ne sont nécessaires.** CH ne s'en servent que pour Σ ≠ ∅. (ÉTABLI, lu : « First consider the case Σ = ∅ … Using the Taylor-Wiles system constructed in [Tay06, §2], we deduce that S_∅ is a free T_∅-module of rank one ».)

**4b. Le système de Taylor–Wiles de [Tay06, §2] est cristallin (ÉTABLI, lu).**
- Taylor écrit, §2, p. 18 : « Then Skinner and Wiles made a rather complete analysis of the ordinary case [SW2]. **We will treat the low weight, crystalline case.** » Le foncteur D_Σ impose, en chaque x | l : « (R/I)² is isomorphic to M(D) for some object D of MF_{F_x,O,k} » (Fontaine–Laffaille, 2 ≤ k ≤ l − 1).
- Le décompte local en l est « #H¹_f(G_x, ad⁰ρ) | #(O/λⁿ)#H⁰(G_x, ad⁰ρ) » (p. 21), et le théorème final est le Th. 2.6 : « R_∅ → h(U₀)_m is an isomorphism of complete intersections and S(U₀)_m is finite free ».
- **CH ont donc remplacé la condition cristalline de Taylor par la condition ordinaire (D3). L'étape 4 consiste à revenir à la condition d'origine de Taylor.**

**4c. Ce qui change entre Taylor §2 et CH §6 (DÉDUCTION, point par point).**
- **Le corps de base.** Taylor prend F totalement réel de degré pair, D ramifiée seulement à l'infini et ρ̄ non ramifiée hors de l. CH prennent ℚ, B ramifiée en N⁻·∞ et ρ̄ ramifiée en N. CH font eux-mêmes cette adaptation avec deux conditions locales : (D2) « minimally ramified outside N₁⁻Σ » (Diamond 1997a, Def. 3.1) et (D5), la sp-condition en q | N⁻ (Terracini, Déf. 2.2). Le décompte minimal « ♯(L_q) = ♯(H⁰(G_q, ad⁰ρ₀)) for all q » ([Ter03, §3.4], cité par CH) est **indépendant de la condition en p**.
- **La surjection R → T (CH Lemme 6.5).** Elle demande que les représentations attachées à T satisfassent la condition en p. Pour p ∤ N, poids 2 et p = 5 > 2, ρ_f|G_p est cristalline de poids de Hodge–Tate (0, 1), donc dans l'image de Fontaine–Laffaille (Taylor Lemme 1.4, via [FL] ; cas k = 2, K = ℚ_l de [DDT, §2.5]). C'est classique.
- **Le décompte en p dans la formule de Wiles.** On utilise la borne cristalline de Taylor (p. 21) au lieu de la borne ordinaire de CH. Les deux donnent la même contribution, d'où la même borne sur le nombre de générateurs de R_{Q_m} (Taylor Lemme 2.5).
- **Points fixes, Taylor Lemme 2.3.** Il faut l ∤ #(U₀A^× ∩ xD^×x^{-1})/F^×. Pour B définie sur ℚ et un ordre d'Eichler, les groupes O^×/{±1} sont d'ordre 1, 2, 3, 4, 6 ou 12, **premier à 5**. (DÉDUCTION, classique.)
- **Irréductibilité.** Taylor Th. 2.6 demande ρ̄|G_{F(√((−1)^{(l−1)/2}l))} irréductible : c'est (CR⁺)(2), vrai si ρ̄ est surjective. Il demande aussi l > 3 et 2 ≤ k ≤ l − 1 : ici l = 5 et k = 2.

**4d. Conclusion de l'étape 4.** S_∅ est libre de rang un sur T_∅, donc η_f(N⁺, N⁻) = ξ_f(N⁺, N⁻). Avec Jacquet–Langlands (isomorphisme sous (ram)) et l'argument final de CH §6.3, on a I_π(N) = (⟨f, f⟩_R), c'est-à-dire **Ω_{f,N⁻} = u·Ω_f^can**. C'est cohérent avec KO Rem. 6.6(1), lu par l'agent B2 : « the replacement of the ordinary deformation condition by the low weight crystalline deformation condition does not affect any of result in [CH18, §6] ». **DÉDUCTION forte** : la machinerie est celle de Taylor §2, dans sa version d'origine.

## 5. L'égalité de BSTW (étape 5)

BSTW (p. 88) normalisent L°,ac_p par la période canonique (« in view of the interpolation formulas »). L°_W, construite au §1, interpole les mêmes valeurs divisées par Ω_{f,N⁻} sans constante locale en N⁺ (§1b). Le quotient vaut donc Ω_f^can/Ω_{f,N⁻} × ∏_{q|N⁻} c_q (Tamagawa), ce qui est une unité par le §4 et (ram). D'où (L°,ac_p) = (∏ c_q · L°_W) et **μ(L°,ac_p) = 0**. **DÉDUCTION** ; même schéma que BSTW en niveau sans facteur carré.

## 6. Pas non justifiés (après cette rédaction)

1. **Lemmes 5.4 et 5.5 de CH** (Ihara en q | D_K) : non relus ligne à ligne. Ils sont indépendants de p, mais il faut vérifier qu'ils n'utilisent pas la p-stabilisation.
2. **Normalisation de BSTW.** La formule d'interpolation exacte de L°,ac_p (BSTW Th. 6.17 et §2.2.7) n'a pas été recopiée. Il faut vérifier qu'aucun facteur local en ℓ | N⁺ n'y apparaît, ce qui est attendu puisque L(s, π_ℓ ⊗ χ) = 1 pour π_ℓ supercuspidale.
3. **Étape 4c.** L'adaptation de Taylor §2 à ℚ avec (D2) et (D5) est faite par CH. Je n'ai pas revérifié que leur décompte en q | N⁺ avec ℓ² | N (supercuspidal, minimal) est bien ♯L_q = ♯H⁰. C'est le cas « minimally ramified » de Diamond 1997a, non ouvert.
4. **Hypothèse « N = N(ρ̄) en N⁺ ».** Vraie en 2 et 3 dans le cas supercuspidal (inertie d'ordre premier à 5). Aux premiers multiplicatifs q | N⁺ avec ρ̄ non ramifiée en q (5 | v_q(Δ)), on n'est plus au niveau minimal et il faut Σ ≠ ∅, donc les montées de niveau de CH et le Th. 2.4 de Diamond 1997b (non ouvert). Le coût est d'environ 5·10⁻⁶ si on exclut ces courbes (`probleme_B_note.md` §4).
5. **Darmon–Iovita.** Lu par l'agent B1, pas par moi.
6. **Hors B.** BSTW Th. 10.5 suppose « N square-free » à cause du problème A (Th. 9.24).

## 7. Relecture adverse

- *« CH utilisent (ord) ailleurs qu'en (D3) et R_p. »* Recherche de « ordinar » et « (ord) » dans tout CH : l'hypothèse n'apparaît qu'en tête du §6, dans (D3), dans (ord) au §4.3 et au Th. 5.7, et via R_p (Lemme 5.8). Aucune autre occurrence.
- *« La relation à trois termes demande a_p ≠ 0 ou un niveau en p. »* Avec a_p = 0, elle devient π(θ_n) = −ν(θ_{n−2}), exactement la forme utilisée par PW (« π_{n−1}^n L_n = −ξ_{n−1}L_{n−2} »).
- *« L'équidistribution exige un ordre d'Eichler sans facteur carré. »* Non : Cornut–Vatsal, Cor. 2.10 vaut pour H ouvert compact quelconque. Seul l'énoncé quantitatif §2.2.4 (« When H = R̂^× for some Eichler order R ») précise les poids, avec N de niveau quelconque.
- *« La liberté peut échouer (multiplicité 2). »* Les échecs connus (Ribet, Manning, Böckle–Khare–Manning, note B2) demandent q | N⁻ avec ρ̄ non ramifiée en q, exclu par (ram), ou des premiers « vexants ». ℓ = 2 et 3 ne sont pas vexants pour p = 5 (ℓ ≢ −1 mod 5). Les autres ℓ | N⁺ avec ℓ ≡ 4 mod 5 et réduction additive sont à exclure ou à vérifier : **point 7 de la liste, ajouté par cette relecture.**
- *« Kim–Pollack–Weston signalent une erreur dans PW et CH. »* Elle porte sur la liberté des groupes de Selmer, utilisée dans l'argument de système d'Euler (côté algébrique), pas sur μ analytique ni sur les périodes. Elle ne touche pas B tel que BSTW l'utilisent. KPW ajoutent aussi « a_p(f) ≢ ±1 (mod p) », automatique ici.

## 8. Contrôle numérique possible (non fait)

On prend une courbe de conducteur 2^a·q (q inerte dans K, multiplicative, (ram)), supersingulière en 5. Avec des matrices de Brandt pour B ramifiée en {q, ∞} et un ordre d'Eichler de niveau 2^a, on calcule θ_n mod 5 pour n = 1 à 4 et on vérifie θ_n ≢ 0. Il faut Sage ou Magma.
