# Piste 8 : sécuriser le rang 1 (N6, la tordue g_K aux premiers de D_K)

27 novembre 2026, soir. **Aucune preuve n'est annoncée.** Aucun gain en pourcentage n'est attendu, mais toute la borne en dépend, puisque le facteur 19/24 demande le rang 1.

**Sources.**
- `lit/relecture_adverse_2.md` (N6), `lit/raccord_A_B.md`.
- Bump–Friedberg–Hoffstein 1990, Th. (ii), déjà lu (`relecture_adverse_2.md`, objection 20).
- `lit/piste2_additif_l7.md` : extension du Lemme types23 aux ℓ ≢ ±1 (mod 5).
- Chida–Wakatsuki, arXiv 2310.19496 (introduction lue). On y trouve le rappel « Ono and Skinner [OS98] proved that #{E : |Δ_E| ≤ X, L(1/2, π ⊗ η_E) ≠ 0} ≫ X/log X ». Leurs théorèmes portent sur des formes **particulières** (poids 8 niveau 2, poids 4 niveau 6), sans usage pour nous.

**Non accessible.** Ono–Skinner, *Non-vanishing of quadratic twists of modular L-functions*, Invent. Math. 134 (1998), 651–660. Les hôtes wstein.org et uva.theopenscholar.com sont bloqués et aucun texte ouvert lu ne cite l'énoncé exact. **NON VÉRIFIÉ.**

**Script.** `scripts/n6_heegner_search.py`, résultats dans `results/n6_heegner_search.txt`.

## 1. Réduction (DÉDUCTION)

- **Le problème N6.** En ℓ | D_K, la tordue g_K = g ⊗ χ_K a ρ̄|I_ℓ = χ_K ⊕ χ_K. Des formes congrues de type χ_K ⊗ St (ou d'un autre type modéré) peuvent alors exister au même niveau, et le Lemme 6.5 de CH ne s'applique pas tel quel. C'est exactement la situation E3.
- **Ce qui évite le problème.** Par le Lemme types23 étendu (piste 2), un tel ℓ est « propre » si ℓ ≢ ±1 (mod 5) et a_ℓ(E) ≢ ±(ℓ + 1) (mod 5). Dans ce cas, toutes les formes de T(N_∅)_𝔪 ont le type de g_K en ℓ, et le traitement minimal s'applique.
- **Le rang 1 est donc sauvé si l'on trouve K** tel que :
  - (i) les conditions de BSTW Th. 12.3 soient remplies : 5 et tous les premiers de N décomposés (Heeg et 2.15), (D_K, N) = 1 ;
  - (ii) **tout** premier de D_K soit propre ;
  - (iii) L(1, E ⊗ χ_K) ≠ 0.

## 2. Obstruction : D_K premier ne marche pas, sauf ℚ(i) (PROUVÉ, élémentaire ; corrigé par la relecture adverse 3)

- Prenons D = −ℓ avec ℓ premier **impair**. Comme (−1/5) = 1, on a (D/5) = (ℓ/5). La condition « 5 décomposé » impose donc ℓ ≡ ±1 (mod 5), ce qui contredit (ii).
- **Exception oubliée dans la première version : D = −4 (K = ℚ(i)).** On a (−4/5) = +1, donc 5 est décomposé, et 2 ≢ ±1 (mod 5). Ce corps ne convient que si 2 ∤ N (pour (Heeg) et (9.9)), a₂(E) ≠ ±2 et L(1, E ⊗ χ₋₄) ≠ 0. C'est un seul corps, sans latitude, et 2 ∤ N est rare dans notre famille (au plus 0,3 % des courbes sont semistables en 2). D = −8 ne marche pas : (−8/5) = −1. **L'exception est donc sans usage général.**
- **Règle exacte.** (D/5) = (−4/5)^{[4‖D]}·(−8/5)^{[8|D]}·∏_{ℓ|D impair} (ℓ/5). Un premier impair propre vérifie (ℓ/5) = −1. Il faut donc un nombre pair de « −1 », en comptant le facteur 2 quand 8 | D. Exemple : D = −ℓ₁ℓ₂.
- **Conséquence.** Les tordues **premières** impaires (conjecture de Goldfeld restreinte aux premiers, Chida–Wakatsuki) ne suffisent pas. Les tordues D₀·ℓ (méthode d'Ono–Skinner telle que je la crois, **non vérifiée**) **pourraient** convenir si D₀ a un nombre impair de facteurs propres. Ce n'est donc pas exclu par l'obstruction ; c'est à vérifier sur le texte d'Ono–Skinner. *(La première version disait à tort que l'obstruction « valait pour Ono–Skinner ».)*
- La remarque vaut aussi pour le cas publié de BSTW (semistable), qui ne traite pas N6. À signaler aux spécialistes.

## 3. Test numérique (indication, pas une preuve)

Six courbes de la famille (5 | A, 5 ∤ B, signe −1, N < 3000). On cherche D = −ℓ₁ℓ₂, |D| ≤ 4000, avec ℓ₁ et ℓ₂ propres, D ≡ 1 (mod 4) et tous les premiers de 5N décomposés.

| Courbe | D avec (i)+(ii) | dont L(1, E ⊗ χ_D) ≠ 0 |
|---|---|---|
| [5, 22], N = 53 | 26 | 26 |
| [−5, 4], N = 544 | 9 | 7 |
| [5, 18], N = 544 | 9 | 7 |
| [0, 8], N = 576 | 19 | 17 |
| [−15, 18], N = 792 | 2 | 1 |
| [−20, 16], N = 896 | 6 | 5 |

- Pour D = −ℓ premier, on trouve 0 cas sur 44 à 189 candidats par courbe, comme prévu au §2.
- Le seuil 10⁻⁸ sur la valeur L numérique n'est pas une preuve d'annulation ou de non-annulation.
- Un tel K existe donc pour chaque courbe testée, et la proportion de D non annulés parmi les candidats est élevée (≈ 85 %).

## 4. Ce qui manque (OUVERT)

Il manque un **théorème de non-annulation** de L(1, E ⊗ χ_D) pour une infinité, ou au moins un, D = −ℓ₁ℓ₂ (ou plus généralement à facteurs premiers dans un ensemble de Chebotarev 𝒫) sous des conditions locales en 5N. Pistes, toutes SPÉCULATION :
- (a) la méthode d'Ono–Skinner (Waldspurger, puis formes de poids demi-entier mod M, puis Chebotarev) avec deux facteurs premiers. À lire, référence à fournir ;
- (b) des résultats de moments ou de densité un-niveau pour des familles de discriminants restreintes. Je ne connais pas d'énoncé couvrant « tous les facteurs premiers dans 𝒫 » ;
- (c) l'autre voie de `LISTE_GAINS.md` : l'invariance par torsion des modules de congruence, qui contournerait le choix de K.

## 4 bis. Vérification finale
- (2.15) est vérifié sur le texte de BSTW (« p splits in L ») ; le Th. 12.3 demande L avec (2.15), (9.9) et (Heeg). L'obstruction du §2 tient.
- Coates–Li–Tian–Zhai (arXiv 1312.3884, Th. 1.1) donnent des tordues non annulées à exactement k facteurs premiers, mais sous l'hypothèse f([0]) ∉ 2E(ℚ), fausse dès que E(ℚ) n'a pas de 2-torsion. **Non applicable en général.**
- Aucun résultat « facteurs premiers de D dans un ensemble de Chebotarev » n'a été trouvé (recherche du 27/11).

## 5. Relecture adverse
1. **I — La notion de « propre » suffit-elle pour g_K ?** Pour g_K en ℓ | D_K, on a E de bonne réduction en ℓ. La seule congruence à changement de type compatible avec ρ̄|I = χ ⊕ χ est χ ⊗ St (montée de niveau, a_ℓ ≡ ±(ℓ + 1)) ou un caractère modéré d'ordre 5 (ℓ ≡ ±1). Cela demande encore la même vérification que E3 (question 4). **Réglée au niveau DÉDUCTION.**
2. **M — Calcul numérique des L(1).** L'indication est robuste (valeurs ≫ 10⁻⁸ dans les cas retenus), mais ce n'est pas une preuve. **Assumé.**
3. **I — L'obstruction du §2 suppose que 5 doit être décomposé (2.15).** C'est lu dans `raccord_A_B.md` (BSTW Th. 12.3 : « (2.15) (p décomposé) »). **Réglée.**

**Statut de la piste 8.** Elle est réduite à un énoncé analytique précis (§4), avec une obstruction pour les discriminants premiers et une indication numérique favorable. Elle reste **ouverte**.
