# Piste 2 : réduction additive en ℓ ≥ 7

27 novembre 2026. Suite de `LISTE_GAINS.md`, piste 2. **Aucune preuve n'est annoncée.** Statut global : DÉDUCTION, qui étend aux ℓ ≥ 7 avec ℓ ≢ ±1 (mod 5) l'argument déjà rédigé pour 2 et 3.

**Sources.**
- `NEW_RESULTS_EN.tex` : Lemme `lem:types23`, Déf. `def:min` et la remarque qui suit (citation de Kim–Ota, Déf. 3.5).
- `lit/raccord_A_B.md` §2 : choix de L″, et la ligne « premiers vexants ».
- `lit/reverification_27_11.md` §4 : Prop. R′.
- Chida–Hsieh, arXiv 1204.2427, §6 (relu le 27/11, voir aussi `piste3_E1_E3.md`).

**Script.** `scripts/bound_v5.py`, résultats dans `results/bound_v5.json`.

## 1. Côté A (DÉDUCTION, héritée)

- La Prop. R′ vaut pour **toute** π_v générique unitaire en place décomposée, sans classification des types. Seul l'énoncé de support du Lemme 8.13 de Wan (vérifié numériquement en 2 et 3, pas en ℓ ≥ 7) sert.
- Il suffit d'ajouter les ℓ additifs à la condition 4 du choix de L″ (« tous les autres premiers divisant N(f) décomposés »). Ce sont des conditions locales en nombre fini, donc L″ existe toujours (restes chinois).
- Pour g′ = g ⊗ χ_L, le type en ℓ ∤ D_L est inchangé.

## 2. Côté B : extension du Lemme `lem:types23` (DÉDUCTION)

**Énoncé.** Soit ℓ ≥ 7 avec 5 ∤ ℓ² − 1, c'est-à-dire ℓ ≢ ±1 (mod 5). Alors :
- toute représentation de Weil–Deligne de dimension 2 de G_ℓ à inertie finie a une image d'inertie d'ordre premier à 5 ;
- deux telles représentations congrues mod λ ont le même type inertiel ;
- une représentation de type χ ⊗ St n'est congrue à une représentation à inertie finie que si les deux sont résiduellement de type χ ⊕ χ.

**Preuve.** Celle du lemme pour q ∈ {2, 3}, mot pour mot :
- la partie modérée du type divise ℓ² − 1, premier à 5 ;
- la partie sauvage est un ℓ-groupe ;
- ℤ_ℓ^× = μ_{ℓ−1} × (1 + ℓℤ_ℓ) n'a pas de quotient d'ordre 5, car 5 ∤ ℓ − 1.

La preuve de 2 et 3 n'utilisait que « 5 ∤ q² − 1 » (q² − 1 ∈ {3, 8}). ∎

**Minimalité.** Elle s'obtient avec les mêmes exclusions E1-E3 qu'en 2 et 3 (Déf. `def:min`) :

| Kodaira en ℓ ≥ 7 | Inertie | Statut si ℓ ≢ ±1 (5) |
|---|---|---|
| II, III, IV, IV*, III*, II* | ψ ⊕ ψ⁻¹, ψ d'ordre e ∈ {6, 4, 3}, non scalaire | admis (minimal, pas de changement de type possible) |
| I₀* | χ ⊕ χ (χ quadratique ramifié) | admis **sauf E3** : a_ℓ(E′) ≡ ±(ℓ + 1) (mod 5), avec E′ la tordue de bonne réduction |
| I_n* | χ ⊗ St | admis **sauf E2** (5 \| n) |

Si ℓ ≡ ±1 (mod 5) : on **exclut** tous les additifs. Il y a des caractères modérés d'ordre 5 (ℓ ≡ 1) ou des premiers vexants (ℓ ≡ −1, voir `raccord_A_B.md` §2).

Densités locales exactes (mesure dans ℤ_ℓ², modèle E_{A,B} minimal en ℓ ≥ 5) :

| Type | Mesure |
|---|---|
| II | (ℓ−1)/ℓ³ |
| III | (ℓ−1)/ℓ⁴ |
| IV | (ℓ−1)/ℓ⁵ |
| I₀* | (1−1/ℓ)/ℓ⁵ |
| I_n* | (ℓ−1)²/ℓ^{n+7} |
| IV* | (ℓ−1)/ℓ⁸ |
| III* | (ℓ−1)/ℓ⁹ |
| II* | (ℓ−1)/ℓ¹⁰ |

Avec la bonne réduction et I_n, le total vaut 1 − ℓ⁻¹⁰.

La fraction E3 parmi les I₀* est calculée exactement (énumération de a_ℓ sur 𝔽_ℓ) pour ℓ < 300. Au-delà, tous les I₀* sont exclus.

## 3. Chiffrage (`bound_v5.py`, k = 9 en 2, k = 6 en 3)

Le facteur multiplie la partie supersingulière ; le facteur maximal 1,0527 vaut 1/P₇.

| En 2, 3 | Additif en ℓ ≥ 7 | Facteur | Sans équirépartition | Avec équirépartition (piste 1) |
|---|---|---|---|---|
| prudent | aucun (actuel) | 1 | 78,61 % | 79,30 % |
| prudent | **prudent (§2)** | 1,0362 | **79,03 %** | **79,75 %** |
| prudent | tous (maximum) | 1,0527 | 79,22 % | 79,95 % |
| optimiste | prudent | 1,0362 | 79,46 % | **80,19 %** |
| optimiste | tous | 1,0527 | 79,66 % | 80,40 % |

- La piste 2 en version prudente rapporte **+0,42 pt** seule, et +0,45 pt en plus de la piste 1. La piste 1 est recalculée avec les α_ℓ des additifs : III et III* donnent α = −1 en ℓ ≡ 3 (mod 4), ce qui fait baisser κ_ss de 0,0003.
- Les premiers ℓ ≡ ±1 (mod 5) laissés de côté valent ≈ 0,19 pt.

## 4. Relecture adverse

1. **I — Steinberg tordu (I_n*, 5 ∤ n) et la Déf. 3.5 (2) de Kim–Ota prise à la lettre.** Le quotient de rang 1 de ρ\|I_ℓ est χ, ramifié. La même question se pose déjà pour « steinberg_tordu » en 2 et 3, admis dans S3 prudent. **Héritée**, à poser à Hsieh et Kim avec E2 et E3. *Mise à jour (relecture 4) : réglée au niveau DÉDUCTION, puisque la lecture littérale est vide (aucun relèvement ne la vérifie) et que Kim–Ota travaillent à torsion près (Rem. 2.2).* Effet si on exclut les I_n* : moins de 10⁻⁶.
2. **I — Le Lemme 8.13 (support) en ℓ ≥ 7.** C'est un lemme publié de Wan, valable pour tout p. Nous ne l'avons vérifié numériquement qu'en 2 et 3. **Héritée.**
3. **M — Conditions (c) et S1 de BSZ, Th. 9.** Elles portent sur les ℓ ‖ N avec ℓ ≡ ±1 (mod 5), qui ne sont pas concernés ici. **Réglée.**
4. **M — (CR⁺)(5) de CH.** cond(ρ̄) = cond(ρ) en ℓ, puisque l'inertie est d'ordre premier à 5 ou que l'on a χ ⊗ St avec 5 ∤ n. **Réglée.**
5. **M — Existence de (ram) et de L, L″.** BSZ Lemme 20 vaut pour 100 % des courbes. Les conditions de décomposition sont en nombre fini. **Réglée.**
6. **I — N6 (rang 1, tordue g_K).** Inchangé. **Héritée.**

**Bilan.** Pas d'objection critique propre. La piste 2 a le même statut que le traitement de 2 et 3 déjà soumis aux spécialistes. Il faudrait l'ajouter à la question 4 (Hsieh, Kim).
