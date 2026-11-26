# Borne BSZ mise à jour : 66,48 % → 66,99 % (67,02 % avec la part supersingulière)

26 novembre 2026. **Statut : CONDITIONNEL.** Le résultat repose sur deux prépublications (BSTW arXiv 2409.01350 ; Castella arXiv 2409.01360), dont j'ai lu les énoncés et non les preuves, et sur des déductions de ma part listées en §4. Il n'a été relu par aucun spécialiste. Calcul : `scripts/bsz_bound.py`, `results/bsz_bound.json`.

## 1. Énoncé obtenu

Si les théorèmes cités en §2 sont corrects, alors, pour les courbes elliptiques sur ℚ classées par hauteur, au moins **66,99 %** vérifient rang = rang analytique ≤ 1 avec Ш fini. C'est **67,02 %** si l'on ajoute la part supersingulière (§3, ligne 3), qui repose sur un calcul de densité 2-adique contrôlé par sondage et non démontré cellule par cellule. BSZ obtenaient 66,48 %. Le même calcul donne pour le rang 1 seul **20,90 %** (BSZ : 20,68 %).

## 2. Ce qui change par rapport à BSZ, et pourquoi

Diagnostic tiré de BSZ §3.2 : les conditions de ramification ne coûtent presque rien. Lemme 20 : 100 % des courbes les vérifient, et la condition (c) du Théorème 9 ne coûte que 0,00001 (inégalité (2)). La perte vient de la réduction en 5 : la famille S₀(5) = {5 ∤ A} a une densité de 0,8, et S₁′(5), qui ajoute les conditions de rang 1 dans le cas multiplicatif, a une densité de 0,7918054.

| Famille | Densité | Rang 0 | Rang 1 | Proportion appliquée |
|---|---|---|---|---|
| BSZ : S₀(5) ∩ S₁′(5) | 0,7918054 | BSZ Thm 5 | BSZ Thm 9 | 7/8 (signes équirépartis, κ ≥ 0,5501), sinon 19/24 |
| **Nouveau : S₁new** = bonne ordinaire en 5 ∪ multiplicative en 5, sauf (déployée et 5 \| ord₅ Δ) | **0,7998976** | BSZ Thm 5 | bonne ordinaire : **BSTW Thm 12.3** ; multiplicative : **Castella Thm 1.1** | idem (Théorème 16 applicable : conditions en 5 seulement, 5 ≡ 1 mod 4) |
| **Nouveau : SS5ss** = supersingulière en 5 ({5 \| A, 5 ∤ B}) et semistable | 0,000297 | **BSTW Thm 1.6** | **BSTW Thm 12.3** (a₅ = 0, N sans facteur carré) | 19/24 (Théorème 25, première partie : pas besoin d'équirépartition) |

Pourquoi le gain supersingulier est minuscule : les modèles y² = x³ + Ax + B ne sont semistables en 2 que sur une densité de 3/1023 ≈ 0,29 %. C'est un calcul exact par cellules mod 2¹⁰ (algorithme de Tate de PARI), stable entre les profondeurs 8 et 10. Pourquoi p = 3 n'aide pas : pour ces modèles, la réduction en 3 n'est jamais bonne ordinaire (j ≡ 0 mod 3 si 3 ∤ A, réduction additive sinon), et les réciproques supersinguliers en 3 exigent aussi N sans facteur carré.

## 3. Calcul (reproduit `results/bsz_bound.json`)

1. Reproduction de BSZ, Corollaire 26 : **0,664817** (article : 0,664816…).
2. Part principale : (7/8 · κ + 19/24 · (1 − κ)) · μ(S₁new) = 0,837508 × 0,799898 = **0,669921**.
3. Reste de S₀(5) \ S₁new (déployées avec 5 | k), rang 0 seul : 3/8 · κ · 0,000102 = 0,000021.
4. Part supersingulière : 19/24 × μ(SS5ss) = 19/24 × (4/25 · 3/1023 · 2/3 · ∏_{ℓ≥7}(1 − ℓ⁻²)/(1 − ℓ⁻¹⁰)), normalisations comprises, soit 0,000235.

Total des lignes 2 et 3 : 0,669942 (**66,99 %**). Avec la ligne 4 : 0,670177 (**67,02 %**).

Densité des déployées avec 5 | ord₅ Δ : la mesure des multiplicatives d'ordre k vaut 8/5^{k+2} pour chaque type (BSZ, preuve du Lemme 18). Donc Σ_{5|k} 8/5^{k+2} = (8/25)/3124.

## 4. Relecture adverse : chaque étape et son statut

| # | Étape | Statut | Vérification |
|---|---|---|---|
| 1 | BSTW Thm 12.3 : p ∤ 2N, bon ordinaire, E[p] irréductible ⇒ (corang 1 et Ш[p^∞] fini ⇒ ord L = 1), sans condition sur le conducteur si p ≥ 5 | ÉTABLI (énoncé lu, prépublication) | hypothèses relues dans le texte |
| 2 | Castella Thm 1.1 : multiplicative en p > 3, (i) E[p] irréductible, (ii) une place q ≠ p de réduction multiplicative non déployée avec E[p] ramifiée, (iii) E(ℚ_p)[p] = 0 ⇒ (corang 1 ⇒ ord L = 1) | ÉTABLI (énoncé lu, prépublication) | — |
| 3 | (iii) est vraie sur S₁new : non déployée, E₀/E₁ est d'ordre p + 1 = 6 et la composante est d'ordre ≤ 2, donc pas de 5-torsion ; déployée avec 5 ∤ k, une 5-torsion de ℚ₅^×/q^ℤ forcerait 5 \| j·k, donc 5 \| j, et μ₅(ℚ₅) = 1 | DÉDUCTION | à faire vérifier |
| 4 | (ii) est vraie pour 100 % des courbes : en chaque ℓ ≥ 7, la densité de « non déployée avec ord_ℓ Δ = 1 » est ≍ 1/(2ℓ), Σ 1/ℓ diverge, et l'argument est celui du Lemme 20 de BSZ | DÉDUCTION | esquisse ; densité « ≍ 1/2 des multiplicatives » non calculée exactement |
| 5 | S₅(E) ≅ ℤ/5 et E[5] irréductible ⇒ corang Sel_{5^∞} = 1 et Ш[5^∞] = 0 (accouplement de Cassels–Tate) | DÉDUCTION, utilisée aussi par BSZ (Thm 9) et Castella (Cor. 1.2) | — |
| 6 | Théorème 16 (κ ≥ 0,5501) applicable à S₁new : congruences en 5 seulement | ÉTABLI (énoncé BSZ) + DÉDUCTION | S₁new est stable par la tordue par −1 (−1 est un carré mod 5 : type de réduction, déployé/non déployé et ord₅ Δ inchangés), comme l'exige la preuve du Cor. 26 |
| 7 | Rang 0 sur S₁new : BSZ Thm 5 inchangé (Skinner–Urban) | ÉTABLI | — |
| 8 | BSTW Thm 1.6 (rang 0) et 12.3 (rang 1) sur SS5ss | ÉTABLI (énoncés) | a₅ = 0 automatique pour p ≥ 5 (BSTW (1.7)) |
| 9 | μ₂(semistable) = 3/1023, μ₃(semistable) ≥ 0,666678 | VÉRIFIÉ NUMÉRIQUEMENT | la « détermination » d'une cellule repose sur 3 relevés aléatoires, pas sur une preuve. Borne totale sans ce terme : 66,99 %. |
| 10 | Personne n'a déjà publié cette mise à jour | NON VÉRIFIÉ À FOND | recherche arXiv par titre et résumé et recherche web : rien trouvé ; ni BSTW ni Castella n'en parlent |

## 5. Portée

- C'est une amélioration de niveau A au sens de la barre d'évaluation, mais **modeste** (+0,5 point) et **conditionnelle**. Pour comparaison, la note zêta d'Anthropic passait de 41,6 % à 67,2 %.
- Le plafond de la méthode avec p = 5 seul reste ≈ 0,8 × 0,8375 ≈ 67 % tant que κ = 0,5501. **Le vrai levier restant est κ**, la part de la famille où l'on sait que les signes sont équirépartis : avec κ = 1, la part principale passerait de 0,6699 à 7/8 × 0,7999 ≈ 0,700. BSZ conjecturent μ_equi(F) = μ(F). Prouver l'équirépartition des signes dans ces familles est donc la cible suivante la plus rentable.
- Il faudrait ensuite faire relire les étapes 3 et 4 par un spécialiste, et vérifier les preuves de BSTW 12.3 et Castella 1.1.
