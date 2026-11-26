# État de l'art (2015–2026) : levée de « N squarefree » dans les p-converses / conjectures principales supersingulières, et μ = 0 pour les fonctions L p-adiques anticyclotomiques (BDP, ±) à niveau non squarefree

Méthode : sources TeX arXiv téléchargées et lues avec grep (les numéros de ligne renvoient au fichier source arXiv, version courante au 2026-11-26). Étiquettes : **ÉTABLI** (texte lu), **DÉDUCTION** (mon raisonnement à partir de textes lus), **NON VÉRIFIÉ** (vu dans un résumé ou une citation secondaire seulement). Notation : N = N⁺N⁻, où N⁺ (resp. N⁻) est divisible par des premiers déployés (resp. inertes ou ramifiés) dans K.

---

## Q1. Quels résultats (2020–2026) prouvent une p-converse ou une conjecture principale sans niveau squarefree, ou avec des hypothèses plus faibles aux premiers déployés ?

### Takeaway
La découverte principale va à l'encontre du contexte donné (« toutes les converses supersingulières connues demandent N squarefree »). Bertolini–Longo–Venerucci (arXiv 2306.17784) prouvent les conjectures principales anticyclotomiques et des formules BSD sur K, cas supersingulier inclus. Leurs hypothèses : **N⁻ squarefree** et, pour q | N⁺, ρ̄ ramifié en q avec H⁰(G_{Q_q}, E_p) = 0. Elles **n'imposent pas que N⁺ soit squarefree**. Par la remarque n = 0 de l'article, cela donne au caractère trivial « corang Sel(E/K) = 1 ⟺ L′(E/K,1) ≠ 0 », donc une p-converse en rang 1 sur K. Dans le cas ordinaire, Burungale–Castella–Skinner (2405.00270) et Burungale–Castella–Kim (1806.01691) se passent explicitement de squarefree. Fouquet–Wan (2107.13726) ne demandent pas N squarefree, mais exigent un premier ℓ ∥ N avec une condition résiduelle de type Steinberg. Dans BSTW, l'hypothèse squarefree vient explicitement de calculs de périodes triples locales (goulot A).

### Cited Findings

**Bertolini–Longo–Venerucci, « The anticyclotomic main conjectures for elliptic curves » (2023, révisé), arXiv 2306.17784**
- ÉTABLI. Hypothèse 1.1 (BLV-revision.tex, l. 474–489), citée textuellement : « (1) The rational prime p is ⩾ 5 and does not divide N. (2) The rational prime p does not divide the class number h_K and the discriminant of K. (3) The representation ρ̄_{E,p} : G_Q → GL₂(F_p) […] is surjective. (4) N⁻ is squarefree. (5) If E has good ordinary reduction at p, then a_p(E) ≢ ±1 (mod p) if p is inert in K, and a_p(E) ≢ 1 (mod p) if p splits in K. (6) If q is a prime dividing N⁺, then H⁰(G_{Q_q},E_p)=0 and ρ̄_{E,p} is ramified at q. (7) If q ∥ N⁻ and q ≡ ±1 (mod p), then ρ̄_{E,p} is ramified at q. » On suppose aussi N premier au discriminant de K (l. 472). — [arXiv 2306.17784](https://arxiv.org/abs/2306.17784)
- ÉTABLI. Le Théorème A (DAMC & IAMC) dit, citation : « (L_p^ε(f)) ⊆ (Char_p^ε(f)) with equality in the non-exceptional case ». « Exceptional » signifie : E supersingulière en p, p inerte dans K, et ε = +. Le cas p déployé est donc toujours non exceptionnel. — [arXiv 2306.17784](https://arxiv.org/abs/2306.17784)
- ÉTABLI. Le Théorème C (« Indefinite BSD formulas ») dit, citation : « Let χ be a finite order character of conductor pⁿ […]. Then Sel(K,A_f(χ)) has corank equal to 1 if and only if L′(E/K,χ,1) ≠ 0 ». La Remarque « remark:n=0 » (l. 531–533) précise : « The case n=0 can be obtained more directly by applying [S-U, FW] in the setting of Theorem B and the techniques of [weiz, BBV] in the setting of Theorem C. In the non-exceptional case it follows as well from the AMCs proved in this paper. » Le cas indéfini correspond à un nombre pair de facteurs premiers de N⁻ (l. 552). — [arXiv 2306.17784](https://arxiv.org/abs/2306.17784)
- ÉTABLI. Dans le corps du texte, une section suppose « N⁻ > 1 » (l. 880 : « Assume that N⁻>1 and that N⁻ has an odd (resp., even) number of prime divisors »). Je n'ai pas vérifié si cette restriction s'étend au Théorème C. — [arXiv 2306.17784](https://arxiv.org/abs/2306.17784)

**Burungale–Skinner–Tian–Wan (BSTW), arXiv 2409.01350 : ce qui impose squarefree, et pourquoi**
- ÉTABLI. Le Thm « KoMC_r » (Kobayashi MC, main.tex l. 7315) commence par : « Let g ∈ S₂(Γ₀(N)) be an elliptic newform with N square-free, and p∤2N a prime of supersingular reduction ». Le Thm « p-converse » (l. 8153) demande : « Either a_p(g)=0 and N is square-free or λ ∤ a_p(g) ». Le Thm « p-BSD » (l. 8040) demande : « If a_p(g)=0, then N is square-free. » — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI. La convention générale (l. 1813–1816) est « N_L is squarefree », où N_L est la partie de N première aux diviseurs de D_L. Les auteurs ajoutent : « While neither condition is always needed, each is an essential feature of some of our later arguments. » — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI. Source du goulot A (l. 7282–7285), citation : « The square-free-ness was assumed in loc. cit. [W1, CLW] for explicit calculation of local triple product periods. However, at any prime dividing D_K, the local automorphic representation associated to g is principal series, and the computation of the local period has already appeared in [W1, §8D]. » La note de bas de page précise que ces périodes apparaissent dans le développement de Fourier–Jacobi d'une série d'Eisenstein sur GU(3,1). — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI. Le Thm « KoMC'_lb » (l. 7385–7398) suppose lui aussi N squarefree. Il demande soit « (def) Each prime dividing N⁻ satisfies (ram) and ν(N⁻) is odd », soit « (indef) Each prime dividing N⁻≠1 satisfies (ram) and ν(N⁻) is even ». La preuve utilise μ = 0 de Pollack–Weston [PW, Thm 1.2] dans le cas (def). Pour (indef), citation : « the μ-invariant of the BDP p-adic L-function vanishes [Bu] under (indef) », où [Bu] = Burungale 1504.02342. Le texte ajoute : « The hypothesis (indef) may be generalised as in [CLW, Thm 8.2.3(2)]. » — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI. Remarque utile (avant le Thm p-converse), citation : « For non-ordinary prime p∤N, the p-converse is also a consequence of lower bound for the strict Selmer group as predicted by Kato's main conjecture (cf. [BKO2]). » La preuve de la p-converse n'utilise que la conjecture de Kato pour g et pour g′ = g⊗χ_L, dans Λ_L ⊗ Q_p (« By Theorem KaMC_r(c) and Theorem KoMC_r »). — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI. BSTW (l. 973) décrit FW ainsi : « an ingredient in the recent proof of a result towards Kato's main conjecture at primes of additive reduction [FW] ». — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)

**Fouquet–Wan, arXiv 2107.13726**
- ÉTABLI. Le Théorème « TheoIntro » (l. 810–825) demande : p > 2 ; ρ̄ absolument irréductible et impaire. Puis, citation : « (1) There is no character χ̄ : G_{Q_p} → F× such that the semisimplification of ρ̄|G_{Q_p} is equal to χ̄ ⊕ χ̄_cyc χ̄. (2) There exists ℓ∤p such that ρ̄|G_{Q_ℓ} is a ramified extension 0→μχ_cyc^{1−k/2}→ρ̄|G_{Q_ℓ}→μχ_cyc^{−k/2}→0 where μ : G_{Q_ℓ}→{±1} is the non-trivial unramified quadratic character. Let f ∈ S_k(Γ₀(N)) […] such that ρ̄_f ≃ ρ̄. If ℓ∥N, then the Iwasawa Main Conjecture holds for M(f). » Il n'y a aucune condition squarefree sur N et aucune condition sur ρ_f|G_{Q_p}. — [arXiv 2107.13726](https://arxiv.org/abs/2107.13726)
- ÉTABLI. Les hypothèses techniques HypTW (l. 1070) et HypNakamura (l. 1355) disent : ρ̄|G_{Q(√p*)} absolument irréductible ; si ρ̄|G_{Q_p} est une extension de χ₂ par χ₁, alors χ₁⁻¹χ₂ ∉ {1, χ̄_cyc}. — [arXiv 2107.13726](https://arxiv.org/abs/2107.13726)

**Cas ordinaire sans squarefree**
- ÉTABLI. Burungale–Castella–Skinner, « Base change and Iwasawa Main Conjectures for GL₂ » (2405.00270). Thm « HPMC » : E de conducteur N, p bon ordinaire, K vérifiant (disc) « D_K is odd and D_K≠−3 », (Heeg) « every prime ℓ|N splits in K » et (spl). Sous (irr) et p > 3, l'égalité tient dans Λ_K⁻ ⊗ Q_p ; sous (sur), elle tient dans Λ_K⁻. Le texte en tire « a p-converse to the Gross–Zagier and Kolyvagin theorem ». Les auteurs notent que Wan [GU(3,1)] exigeait « that N is square-free » et que leur approche « dispenses with any of the ramification hypotheses ». Le Thm « BDP » donne la conjecture principale BDP dans les mêmes conditions. — [arXiv 2405.00270](https://arxiv.org/abs/2405.00270)
- ÉTABLI (résumé). Burungale–Castella–Kim, « Indivisibility of Heegner points and arithmetic applications » : « our main result allows for the classical Heegner hypothesis and non-squarefree conductors ». — [arXiv 1806.01691](https://arxiv.org/abs/1806.01691)
- NON VÉRIFIÉ (résumé seulement). Yan–Zhu, « Main conjectures for non-CM elliptic curves at good ordinary primes » : « more general cases of p-converse theorem and p-part BSD formula » sous (irr). — [arXiv 2412.20078](https://arxiv.org/abs/2412.20078)
- NON VÉRIFIÉ (résumé). Burungale–Castella–Grossi–Skinner prouvent la conjecture de Kolyvagin pour p bon ordinaire déployé dans K. — [arXiv 2312.09301](https://arxiv.org/abs/2312.09301)

**Supersingulier anticyclotomique (BBL I et II) : encore squarefree ou minimal**
- ÉTABLI. Burungale–Büyükboduk–Lei I (2211.03722). Hypothèses (V4.tex l. 318–362) : « (def) N⁻ is a square-free product of odd number of primes » ; « (Im) If p=5, then ρ̄_f(G_{Q(μ_{p^∞})}) contains a conjugate of SL₂(F_p). If p>5, the G_Q-representation ρ̄_f is irreducible » ; « (ram) ρ̄_f is ramified at ℓ in the following cases: ℓ | N⁻ with ℓ² ≡ 1 mod p ; ℓ | N⁺ ». Le texte ajoute : « (Im) and (ram) are precisely the ones required in [pollack-weston11] ». — [arXiv 2211.03722](https://arxiv.org/abs/2211.03722)
- ÉTABLI. BBL I, Remarque « remark_V4_HappyChanHo » (l. 1922–1930 ; le numéro « 7.11 » n'est pas vérifié dans le PDF). Citation : « If a_p(f)=0, then one may relax the condition based on the strategy in [kimpollackweston] as follows. The strategy proceeds via level-lowering of f modulo p to a newform g for which the N⁺-minimality holds, and utilizing vanishing of the μ-invariant of the plus/minus anticylotomic Selmer group associated to g. The latter in turn relies on vanishing of the μ-invariant of the plus/minus anticyclotomic p-adic L-function associated to g due to Pollack and Weston [Theorem 1.1(2)] if p splits in K. The inert case is an ongoing work of the first-named author with Kobayashi and Ota. » [kimpollackweston] = Kim–Pollack–Weston, « On the freeness of anticyclotomic Selmer groups of modular forms », IJNT 13(6) (2017) 1443–1455. — [arXiv 2211.03722](https://arxiv.org/abs/2211.03722)
- ÉTABLI. BBL II (2310.06813). Le résultat principal couvre p inerte et E semi-stable, sous l'hypothèse « (H) N⁻ is a square-free product of an even number of primes ». La Remarque « rmk:lr » dit : « Theorem thm:main assumes the hypothesis (ram) and N₀ to be square-free. With an eye towards eventual removal of these hypotheses, we include the above more general setting », à savoir le relèvement de Fakhruddin–Khare–Patrikis via Sweeting. Une note de bas de page (l. 2177) ajoute : « These results require the level to be square-free » (à propos de [bstw, Thm 1.5] et [CCSS, Thm C]). — [arXiv 2310.06813](https://arxiv.org/abs/2310.06813)
- NON VÉRIFIÉ (résumé). Chan-Ho Kim (2609.15328, sept. 2026) traite le cas « semi-stable elliptic curves […] any good reduction prime p ≥ 5 » : encore squarefree. — [arXiv 2609.15328](https://arxiv.org/abs/2609.15328)
- ÉTABLI (résumé). Castella–Liu–Wan (2109.08375) prouvent une divisibilité Iwasawa–Greenberg pour f non ordinaire via GU(3,1) ; c'est l'ingrédient clé de la ± conjecture de Kobayashi. — [arXiv 2109.08375](https://arxiv.org/abs/2109.08375)

### Inferences
- DÉDUCTION (forte). Pour p ≥ 5 et q ≠ p premier de réduction **additive**, les conditions (6) de BLV et (ram) aux q | N⁺ sont automatiques :
  - *Cas potentiellement bon.* ρ_{E,p}(I_q) est fini, d'ordre divisant 24 lorsque q ∈ {2,3}. Il s'injecte modulo p, puisque le noyau de GL₂(Z_p) → GL₂(F_p) est un pro-p-groupe. Donc ρ̄ est ramifié en q et son exposant de conducteur en q est conservé.
  - *Cas potentiellement multiplicatif.* L'inertie agit par un caractère quadratique ramifié, qui reste non trivial modulo p.
  - *Condition H⁰ = 0.* E(Q_q)[p] = 0 car E₁(Q_q) est pro-q, E₀/E₁ ≅ F_q (additif) et [E : E₀] ≤ 4.
  - *Conséquence.* Pour les courbes de BSZ à réduction additive en 2 et 3, l'obstruction de minimalité de niveau ne vient **pas** de 2 et 3. Elle vient uniquement des premiers multiplicatifs q | N⁺ tels que p | ord_q(Δ).
- DÉDUCTION (à vérifier). Une p-converse en rang 1 sur Q, p = 5 supersingulier, sans N squarefree, découlerait de BLV Thm C (n = 0) par la descente usuelle (comme dans BSTW, preuve du Thm p-converse). On choisit K tel que :
  - 2 et 3 sont déployés dans K ;
  - N⁻ est un produit squarefree d'un nombre pair de premiers ;
  - 5 est déployé dans K, 5 ∤ h_K et (N, D_K) = 1 ;
  - L(E^K,1) ≠ 0.

  Alors Sel(E/K) a corang 1, donc L′(E/K,1) ≠ 0, donc ord_{s=1} L(E,s) = 1. Conditions restantes : ρ̄_{E,5} surjective ; aucun premier multiplicatif q | N⁺ avec 5 | ord_q(Δ) ; existence de K (type Friedberg–Hoffstein avec conditions de déploiement) ; et, point à vérifier, que le Thm C couvre bien N⁻ = 1 (cf. l. 880 « N⁻>1 »).
- DÉDUCTION. FW + BSTW (preuve de la p-converse, qui n'utilise que la conjecture de Kato pour g et g⊗χ_L dans Λ⊗Q_p) donnerait une p-converse supersingulière sans squarefree, **à condition** qu'existe ℓ ∥ N avec ρ̄|G_ℓ du type (2) de FW (extension ramifiée tordue par le caractère quadratique non ramifié). Cela exclut les courbes de conducteur 2^a·3^b et celles sans premier multiplicatif adéquat. BSTW ne fait pas cette déduction et qualifie FW de résultat « towards » Kato.
- DÉDUCTION. Le goulot A (périodes triples locales aux places déployées supercuspidales) n'est contourné par aucun article lu. BCS 2405.00270 le contourne dans le cas **ordinaire** par changement de base et GU(2,2) (« sidesteps the period comparison »). Il n'existe pas d'analogue supersingulier connu de moi.

### Gaps
- Je n'ai pas vérifié si BLV Thm C (n = 0) couvre N⁻ = 1 (hypothèse de Heegner classique), ni si d'autres hypothèses cachées dans le corps du texte imposent squarefree. Je n'ai pas vérifié non plus le statut de publication de 2306.17784.
- Je n'ai pas lu les hypothèses précises de Wei Zhang (Kolyvagin, 2014) ni de BBV, invoqués dans la remarque n = 0 de BLV.
- Je n'ai pas consulté Castella–Ciperiani–Skinner–Sprung [CCSS, Thm C]. BBL II indique qu'il exige un niveau squarefree.
- Je n'ai trouvé aucun article calculant les intégrales triples locales sur GU(3,1) pour des composantes supercuspidales aux places déployées (Hsieh–Yamana et articles analogues non consultés).
- Je n'ai pas lu les hypothèses exactes de Yan–Zhu 2412.20078.

---

## Q2. Existe-t-il μ = 0 pour BDP (cas indéfini) ou pour ± sans (H1) squarefree ? p supersingulier est-il permis ?

### Takeaway
**Oui pour BDP sous l'hypothèse de Heegner.** Hsieh 2014 (arXiv 1112.1580), Théorème B, prouve μ = 0 pour la fonction L p-adique anticyclotomique de Rankin–Selberg (généralisant BDP). L'unique contrainte de niveau est **« (sf) 𝔫⁻ square-free »**, sans aucune condition sur 𝔫⁺. Les autres hypothèses : Σ p-ordinaire (c'est-à-dire p déployé dans K), ρ̄|G_K absolument irréductible, et une condition sur le conducteur non déployé de λ. **Aucune hypothèse d'ordinarité sur a_p.** L'hypothèse (H1) « N square-free » n'apparaît que dans Burungale II (courbes de Shimura, N⁻ ≠ 1), que BSTW cite pour (indef). Burungale I (courbes modulaires) ne demande que « N⁻ square-free ». Pour les ± définies, je n'ai trouvé que la stratégie Kim–Pollack–Weston, qui passe par l'abaissement de niveau.

### Cited Findings
- ÉTABLI. Hsieh, « Special values of anticyclotomic Rankin–Selberg L-functions », Doc. Math. 19 (2014).
  - *Théorème A* (Waldmain.tex l. 100–106) : « In addition to (ord) and Hypothesis A, we further assume that (sf) 𝔫⁻ is square-free. Then there exists an element 𝒫_Σ(π,λ) ∈ Λ such that […] ». Ici 𝔫 = 𝔫⁺𝔫⁻ est le conducteur de π, 𝔫⁻ la partie inerte ou ramifiée. (ord) est : « Σ is p-ordinary » (pour F = Q, cela équivaut à p déployé dans K). L'Hypothèse A porte sur les signes locaux ε* = +1 aux v | 𝔫⁻ et est vide si 𝔫⁻ = 1.
  - *Théorème B* (l. 113–118) : « With the assumptions in Theorem A, suppose further that (1) p is unramified in 𝓕, (2) the residual Galois representation ρ̄_p(π_𝒦) := ρ_p(π)|_{G_𝒦} (mod 𝔪_p) is absolutely irreducible, (3) p ∤ ∏_{v|𝔠_λ⁻} #(Δ_{λ,v}). Then μ⁻_{π,λ,Σ} = 0. » Le texte ajoute : « suppose that (𝔫,𝒟_{𝒦/𝓕})=1 and ρ_p(π) is residually irreducible. Then we always have μ⁻_{π,λ}=0 whenever λ has split conductor over 𝓕 (i.e. 𝔠_λ⁻=(1)). »
  - *Origine de (sf)*, citation : « The restriction (sf) is due to the computational difficulty on the local period integrals and the local Fourier coefficients, and it is expected to be unnecessary. » La note mentionne aussi le lien avec BDP : « When 𝓕=Q, π is unramified at p and 𝔫⁻ is only divisible by primes ramified in 𝒦, ℒ_Σ(π,λ) is constructed in [BDP] ».
  - *Version raffinée* (Thm « T:mu-invariant », Waldvmu.tex l. 179–185) : sous Hypothèse A, (sf), p non ramifié dans 𝓕 et (ai_𝒦), on a μ = 0 ⟺ Σ_{v|𝔠_λ⁻} μ_p(χ_π,v) = 0. Les places déployées v | p𝔑⁺ sont traitées pour un conducteur arbitraire via des fonctions de Kirillov explicites (« The split case », l. 386).
  — [arXiv 1112.1580](https://arxiv.org/abs/1112.1580)
- ÉTABLI. Burungale, « On the non-triviality of the p-adic Abel–Jacobi image of generalised Heegner cycles modulo p, II: Shimura curves », JIMJ 16 (2017). Hypothèses (heegnersh1.tex l. 135–139) : « (H1) The level N is square-free and prime to the discriminant of K. (H2) The number of primes dividing N⁻ is positive and even. (H3) The conductor N_ε divides N⁺. » s'ajoutent à (ord) « p splits in K » et (irr). — [arXiv 1504.02342](https://arxiv.org/abs/1504.02342)
- ÉTABLI. Burungale, « …, I: modular curves » (1410.0300). Le Théorème A (heegnerv4.tex l. 298–313) suppose (ord) et (Hg), plus : « (1) The residual representation ρ_f|_{G_K} mod 𝔪_p is absolutely irreducible, (2) N⁻ is square-free and (3) p ∤ ∏_{v|c⁻}|Δ_{η,v}| ». La conclusion porte sur la **ℓ-tour** anticyclotomique (ℓ ≠ p) : non-annulation mod p pour presque tout ν ∈ 𝔛_ℓ. Ce n'est pas μ = 0 dans la direction p. — [arXiv 1410.0300](https://arxiv.org/abs/1410.0300)
- ÉTABLI. Castella–Hsieh, « Heegner cycles and p-adic L-functions » (1505.08165). Le niveau y est contraint par « N_f⁻ is a square-free product of primes ramified in 𝒦 » (l. 345). Dans le Thm « BDP » (interpolation), ψ est « an anticyclotomic Hecke character of infinity type (r,−r) and conductor 𝔠₀𝒪_K with (𝔠₀,Np)=1 ». Je n'ai pas repéré d'énoncé μ = 0 propre à cet article par grep. — [arXiv 1505.08165](https://arxiv.org/abs/1505.08165)
- ÉTABLI. BSTW n'invoque pour BDP que [Bu] = 1504.02342, et seulement sous (indef) avec N⁻ ≠ 1 (main.tex l. 7394, 7436). [Hs] = 1112.1580 figure dans la bibliographie (l. 8574). — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI. BCS 2405.00270 relie BDP (construit dans [cas-hsieh1]) à la conjecture de Heegner « In light of the Λ_K⁻-adic analogue of the p-adic Waldspurger formula of [BDP] (see [cas-hsieh1]) ». Ceci vaut sous (Heeg) sans squarefree, dans le cas ordinaire. — [arXiv 2405.00270](https://arxiv.org/abs/2405.00270)
- ÉTABLI (résumé). Hatley–Lei (1706.04531) : sous l'hypothèse de Heegner, « the mu-invariant vanishes for one modular form if and only if it vanishes for the other » pour des formes congruentes (Selmer de corang positif). — [arXiv 1706.04531](https://arxiv.org/abs/1706.04531)
- ÉTABLI (résumé). Pollack–Weston (math/0610694) vérifient « the μ-part of the main conjecture » anticyclotomique. Selon BBL I, (Im) et (ram) (ρ̄ ramifié en tout ℓ | N⁺) sont « precisely the ones required » par Pollack–Weston 2011. — [arXiv math/0610694](https://arxiv.org/abs/math/0610694) ; [arXiv 2211.03722](https://arxiv.org/abs/2211.03722)

### Inferences
- DÉDUCTION (forte). Prenons E/Q de conducteur N arbitraire (réduction additive en 2 et 3 permise), p ≥ 5 bon (supersingulier permis), et K vérifiant l'hypothèse de Heegner (tous les q | N déployés, donc 𝔫⁻ = 1 et (N,D_K) = 1). Alors (sf) et l'Hypothèse A sont vides. Pour λ de type à l'infini (1,−1), anticyclotomique et de conducteur 1 (il en existe si 𝒪_K^× = {±1}), la condition (3) est vide. Il reste ρ̄|G_K absolument irréductible. Hsieh Thm B donne alors **μ(BDP) = 0 sans aucune hypothèse squarefree sur N⁺**.

  Le goulot B se pose donc **seulement** dans les situations (def) et (indef avec N⁻ ≠ 1), c'est-à-dire lorsque des premiers de N sont inertes dans K. En pratique on peut l'éviter en choisissant K « de Heegner » (2 et 3 déployés). Il faut vérifier que la normalisation de 𝒫_Σ(π,λ)² coïncide, à une unité près, avec la BDP utilisée dans BSTW et Castella–Wan (Castella–Hsieh l'utilisent).
- DÉDUCTION. La présence de p supersingulier ne gêne pas : l'hypothèse (ord) de Hsieh porte sur le type CM (p déployé dans K) et non sur π_p.
- DÉDUCTION. Pour les ± définies, aucune référence lue ne donne μ = 0 sans N⁺-minimalité. La voie connue est celle de Kim–Pollack–Weston (abaissement de niveau vers g N⁺-minimal, puis comparaison des invariants μ des Selmer). Vu l'inférence de Q1, la minimalité aux premiers additifs est automatique pour p ≥ 5 : seuls les premiers multiplicatifs q | N⁺ avec p | ord_q Δ posent problème.

### Gaps
- Je n'ai pas vérifié si Hsieh Thm B suppose implicitement π non ramifié en p, ni s'il existe une version publiée corrigée (Doc. Math. 19).
- Je n'ai pas lu l'article de Kim–Pollack–Weston 2017 lui-même.
- Je n'ai trouvé aucun travail postérieur (2017–2026) de Burungale retirant (H1) dans le cas Shimura.
- Je n'ai pas consulté Burungale, « On the μ-invariant of the cyclotomic derivative of a Katz p-adic L-function » (1304.4298). Il concerne Katz (CM), pas BDP.
- Je n'ai pas consulté Kriz, Longo–Vigni, Kobayashi–Ota ni Büyükboduk–Lei sur μ.

---

## Q3. Préprints 2024–2026 améliorant la proportion BSZ (66,48 %) ?

### Takeaway
Je n'ai trouvé aucun préprint améliorant 66,48 % ou annonçant BSD en rang ≤ 1 pour une proportion plus grande. Les avancées 2024–2026 portent sur des familles explicites (tordues quadratiques) et sur des 2-converses en rang 0.

### Cited Findings
- ÉTABLI (résumé). BSZ 1407.1826 donne la borne 66,48 % ; selon le résumé de recherche, les auteurs notent qu'une analyse plus fine pourrait l'améliorer. — [arXiv 1407.1826](https://arxiv.org/abs/1407.1826)
- ÉTABLI (résumé). BSTW : « first infinite families of non-CM elliptic curves for which the BSD conjecture is true ». — [arXiv 2409.01350](https://arxiv.org/abs/2409.01350)
- ÉTABLI (résumé). Banwait–Huang (2601.16044, janv. 2026) identifient, par algorithme sur la LMFDB, les courbes de conducteur ≤ 500 000 qui admettent une infinité de tordues satisfaisant BSD fort, en s'appuyant sur BSTW. — [arXiv 2601.16044](https://arxiv.org/abs/2601.16044)
- ÉTABLI (résumé). Burungale–Tian (2611.11566, nov. 2026) : « finiteness of Sel_{2^∞}(E/Q) implies L(E,1)≠0 » pour E à corps de 2-division abélien. Citation : « The proof follows the quadratic twist deformation approach of OpenAI », avec un invariant μ cohomologique dépendant de E[2]. — [arXiv 2611.11566](https://arxiv.org/abs/2611.11566)
- ÉTABLI (résumé). Bhargava–Burungale (2611.16130) mentionnent « the 2-converse or 2-adic Fontaine–Mazur results announced and invoked by OpenAI ». Ces résultats sont annoncés mais leur source primaire n'a pas été consultée. — [arXiv 2611.16130](https://arxiv.org/abs/2611.16130)
- ÉTABLI (résumé). Burungale–Tian, « A rank zero p-converse to a theorem of Gross–Zagier, Kolyvagin and Rubin » (2506.03465) traite le cas CM. — [arXiv 2506.03465](https://arxiv.org/abs/2506.03465)

### Inferences
- DÉDUCTION. Les 2-converses récentes (Burungale–Tian 2026, annonces attribuées à OpenAI) pourraient à terme alimenter une amélioration de BSZ. BSZ utilise des converses en p = 2, 3, 5 selon les conditions de réduction. Aucun calcul de proportion n'a été trouvé.

### Gaps
- Je n'ai pas fait de recherche Google Scholar « cited by » sur 1407.1826 (outil indisponible). Seuls arXiv et une recherche web ont été utilisés.
- Je n'ai pas trouvé de source primaire pour les résultats « annoncés par OpenAI ».
