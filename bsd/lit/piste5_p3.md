# Piste 5 : le premier p = 3 (étude de faisabilité)

27 novembre 2026, soir. **Aucune preuve n'est annoncée.** Il s'agit d'un cadrage : ingrédients, obstacles et gain plafond.

**Sources ouvertes.**
- BSZ, arXiv 1407.1826 : Th. 5, Rem. 6 à 8, Th. 9, Rem. 10, Th. 13, Th. 25, §4.
- BSTW, arXiv 2409.01350 v2 : Th. 1.3, 1.5, 1.6, 1.9, 1.10, condition (1.7) p. 6.
- Chida–Hsieh, arXiv 1204.2427 : hypothèse (CR⁺).

**Scripts.** `scripts/p3_montecarlo.py`, résultats dans `results/p3_montecarlo.json`.

## 1. Ce que dit la littérature (ÉTABLI, lu)

- **BSZ Th. 13** : la moyenne de Sel₃ vaut 4 dans toute famille large.
- Avec l'argument du Th. 25 en p = 3, le rang de Selmer est ≤ 1 pour au moins (p² − p − 1)/(p² − 1) = **5/8** de la famille, et **3/4** si les signes sont équirépartis (DÉDUCTION immédiate).
- **Réciproques en p = 3 ordinaire**, toutes sans hypothèse « sans facteur carré » :
  - rang 0 : BSZ Th. 5, « Let p be an odd prime », avec (a) bonne réduction ordinaire ou multiplicative, (b) E[p] irréductible, (c) un ℓ ‖ N où E[p] est ramifiée ;
  - rang 1 : BSTW **Th. 1.10**, « p ∤ 2N an ordinary prime », avec (sur_Q) et (ram).
- **Réciproques en p = 3 supersingulier** : BSTW Th. 1.6 (rang 0) et le rang 1 (Th. 12.3). Elles demandent :
  - la condition (1.7), « a_p(E) = 0 [...] This is automatic for p ≥ 5 » ;
  - E **semistable** (« Let E/Q be a semistable elliptic curve »).

## 2. Constat : en 3, presque aucune courbe n'est ordinaire (PROUVÉ + Monte-Carlo)

- **Argument.** Si 3 ∤ A, le modèle E_{A,B} a bonne réduction en 3, puisque Δ ≡ −4A³ ≢ 0. Son invariant est j = 1728·4A³/(4A³ + 27B²) ≡ 0 (mod 3) : la réduction est **supersingulière**. Si 3 | A et 3 ∤ B, la réduction est additive (v₃(Δ) = 3). La réduction ordinaire ou multiplicative demande v₃(A) = v₃(B) = 3, ce qui fait une densité de l'ordre de 10⁻⁴.
- **Monte-Carlo** (300 000 tirages mod 3³⁰) :

  | Type en 3 | Proportion | Théorie |
  |---|---|---|
  | bonne supersingulière avec a₃ = 0 | 0,4428 | 4/9 ≈ 0,4444 |
  | a₃ = ±3 | 0,2233 | 2/9 |
  | additive | 0,3340 | 1/3 |
  | ordinaire | 1,7·10⁻⁵ | — |
  | multiplicative | 3·10⁻⁶ | — |

  La valeur 4/9 vient de l'énumération sur 𝔽₃ : a₃ = 0 pour 4 des 6 courbes avec 3 ∤ A.
- **Conséquence.** Les réciproques ordinaires (Skinner–Urban, BSTW Th. 1.10) ne servent quasiment à rien pour p = 3. Il faut le **cas supersingulier avec a₃ = 0**, qui ne vaut aujourd'hui que pour E semistable (BSTW). C'est exactement le même verrou que pour p = 5, mais en p = 3.

## 3. Gain plafond (DÉDUCTION, chiffrage grossier)

- **Courbes que p = 5 ne couvre pas** :
  - les courbes additives en 5 : (1/25 − 5⁻¹⁰)/n(5) ≈ 0,0400 ;
  - les exclus de la famille supersingulière : SS5·(1 − μ₂μ₃P) ≈ 0,0079.
  
  Au total, U ≈ 0,048.
- **Si p = 3 marchait** pour toute courbe bonne supersingulière en 3 avec a₃ = 0 (4/9 de U, par indépendance des conditions locales), on aurait U·(4/9)·[5/8 + κ/8] avec κ ≈ 0,56. Cela donne **≈ +1,5 pt** (+1,3 pt sans équirépartition), soit environ **81,3 %** en partant de 79,81 %.
- C'est moins que les « jusqu'à ≈ +2,5 pts » de `LISTE_GAINS.md`. Ce chiffre supposait implicitement des courbes ordinaires en 3, qui n'existent pas en densité notable. **Je corrige.**
- Les courbes des familles p = 5 dont Sel₅ est de rang ≥ 2 ne sont pas récupérables sans moyennes **jointes** de Sel₃ et Sel₅, inconnues à ma connaissance. Une recherche de vérification est prévue.

## 4. Obstacles pour p = 3 (OUVERT)

1. **Côté B (CH §6).** L'hypothèse (CR⁺)(1) de CH exige « p > k + 1 », soit p > 3 en poids 2. **La Prop. 6.1 de CH ne s'applique pas en p = 3.** Il faudrait une autre preuve de la comparaison des périodes Ω_{N⁻} ~ Ω_can.
2. **Minimalité.** Le Lemme types23 repose sur « p ∤ q² − 1 ». Pour p = 3, **tout** premier q ≥ 5 vérifie 3 | q² − 1, et en 2 aussi (2² − 1 = 3).
   - Les types supercuspidaux en 2 ont une inertie d'ordre 8 ou 24 ; si elle est d'ordre 24, 3 divise #ρ̄(I₂).
   - Chaque premier additif devient donc potentiellement « vexant ». Il faudrait une analyse de type Diamond, voire Kisin, à chaque premier additif, y compris en 5 pour les courbes visées.
3. **Côté A.** La Prop. R′ est indépendante de p (Kirillov). Mais la construction de CLW et Wan en p = 3 supersingulier (avec (1.7)) n'a pas été relue.
4. **Rang 1.** BSZ Rem. 10 signale, pour l'extension en p = 3 du résultat de Skinner, une condition supplémentaire (« the image of the local restriction S_p(E) → E(Q_p)/pE(Q_p) not lie in the image of E(Q_p)[p] »). Il faut vérifier si un analogue intervient dans la voie BSTW Th. 12.3 en p = 3.

## 5. Bilan
- **Gain plafond** : ≈ +1,5 pt, conditionnel à l'extension de BSTW en p = 3 supersingulier, niveau non sans facteur carré.
- **Difficulté** : la plus élevée de la liste. Le verrou B de CH ((CR⁺)(1)) et la minimalité en p = 3 sont de vrais problèmes de recherche, pas des adaptations.
- **Découpage possible**, si l'on veut avancer :
  - (a) chercher une preuve de la comparaison des périodes valable en p = 3, par exemple chez Pollack–Weston ou des travaux récents sur μ = 0 ;
  - (b) chiffrer précisément U et κ₃ ;
  - (c) écrire aux spécialistes.

## 6. Relecture adverse
1. **I — « Ordinaire en 3 ≈ 0 » est-il un artefact du modèle court ?** Non : la densité porte sur les courbes ordonnées par hauteur, chacune ayant un unique (A, B) réduit. Le calcul de j le montre, et le Monte-Carlo le confirme. **Réglée.**
2. **I — Indépendance des conditions en 3 et en 5 pour U.** Les conditions sont locales en des premiers distincts (BSZ §3.1). **Réglée.**
3. **M — Le plafond ignore les exclusions en 2 pour p = 3** (types où 3 divise #ρ̄(I₂)). C'est donc un majorant. **Assumé.**
