# Inventaire : théorèmes réciproques p-adiques utilisables pour améliorer les 66,48 % de BSZ

Lu le 26 novembre 2026. Les PDF viennent d'arXiv (`lit/raw/`, non versionné) ; les références de lignes renvoient à leur conversion texte. Étiquettes : **ÉTABLI** (énoncé lu dans l'article), **DÉDUCTION** (mon raisonnement à partir d'énoncés lus, à faire vérifier), **À VÉRIFIER**.

## 0. Point de départ : BSZ (arXiv 1407.1826 v2)

- Résultat : au moins **66,48 %** des courbes, classées par hauteur, vérifient la partie « rang » de BSD et ont Ш fini (intro, p. 1). ÉTABLI.
- Ingrédients : moyenne du 5-Selmer égale à 6 (Bhargava–Shankar) ; Théorème 5 (rang 0) ; Théorème 9 (rang 1) ; équirépartition des signes sur une sous-famille de densité ≥ 55 % ; parité de Dokchitser. ÉTABLI.
- **Théorème 5 (rang 0)**, p impair : (a) réduction bonne ordinaire ou multiplicative en p ; (b) E[p] irréductible ; (c) un ℓ ≠ p avec ℓ ‖ N et E[p] ramifiée en ℓ ; (d) S_p(E) = 0. Conclusion : rang = rang analytique = 0. ÉTABLI.
- **Théorème 9 (rang 1)**, p ≥ 5 : (a) réduction bonne ordinaire ou multiplicative en p ; (b) E[p] irréductible ; (c) E[p] ramifiée en tout ℓ ‖ N avec ℓ ≡ ±1 mod p ; (d) si N n'est pas sans facteur carré, deux ℓ ‖ N, ℓ ≠ p, où E[p] est ramifiée ; (e) une condition en p dans le cas multiplicatif (invariant L). ÉTABLI.
- **Ce qu'ils prévoient (§4).** Théorème 5 renforcé selon la Remarque 6 (supersingulier, sans (b), (c) affaiblie) : 66,48 % → **69,6 %**. Théorème 9 renforcé selon la Remarque 10 (supersingulier en p ; p = 3 sous conditions) : → **79,7 %** ; et **> 80 %** en utilisant aussi p = 3. ÉTABLI.
- **Plafond** de la méthode à p fixé : facteur (p² − p − 1)/(p² − 1), soit 19/24 ≈ 79,2 % pour p = 5 (Théorème 27 et sa preuve). Le passage à 100 % exige la moyenne p + 1 du p-Selmer pour une infinité de p. ÉTABLI.

## 1. Rang 0 : remplaçants du Théorème 5

| Résultat | Hypothèses | Conclusion | Ce qu'il lève | Statut |
|---|---|---|---|---|
| BSTW, arXiv 2409.01350 v2, Thm 9.21(c) | p ∤ 6N **bon ordinaire**, E[p] irréductible (non CM) | conjecture principale cyclotomique dans Λ ⊗ ℚ_p (Skinner–Urban, Wan) | — | ÉTABLI (énoncé, l. 6007) |
| ⇒ réciproque de rang 0 | idem | corang Sel_{p^∞}(E/ℚ) = 0 ⇒ L(E, 1) ≠ 0 | **(c)** pour p bon ordinaire | DÉDUCTION, confirmée par BSTW Cor. 12.5 (r = 0 « from Theorem 9.21(c) ») |
| BSTW Thm 1.6 | E **semistable**, p > 2 **supersingulier** (p = 3 : a_3 = 0) | corang Sel_{p^∞} = 0 ⇒ L(E, 1) ≠ 0 | le cas supersingulier (Remarque 6), mais seulement pour N sans facteur carré | ÉTABLI (l. 189) |
| Burungale–Tian, arXiv 2506.03465 | E **à CM**, p quelconque | corang 0 ⇒ L(E, 1) ≠ 0 | — (densité nulle) | ÉTABLI (résumé) |
| Burungale–Tian, arXiv 2611.11566 | p = 2, corps de 2-division abélien | Sel_{2^∞} fini ⇒ L(E, 1) ≠ 0 | ouvre p = 2, mais pour une famille de densité nulle | ÉTABLI (résumé) |

## 2. Rang 1 : remplaçants du Théorème 9

| Résultat | Hypothèses | Conclusion | Ce qu'il lève | Statut |
|---|---|---|---|---|
| **BSTW Thm 12.3** | p ∤ 2N ; soit **bon ordinaire**, soit **a_p = 0 et N sans facteur carré** ; E[p] irréductible (non CM) ; (ram) seulement si p = 3 | corang Sel_{p^∞} = 1 et Ш[p^∞] fini ⇒ ord_{s=1} L = 1 | **(c), (d)** pour p ≥ 5 de bonne réduction ; et le **supersingulier** si N est sans facteur carré | ÉTABLI (l. ~6706) |
| BSTW Thm 1.10 | p ∤ 2N ordinaire, ρ̄ surjective, (ram) | corang 1 ⇒ ord = 1 (sans hypothèse sur Ш) | (c), (d) | ÉTABLI (l. 241) |
| Kim, arXiv 2109.12344 v3, Cor. 1.2 | non CM, p > 3 bon ordinaire, E[p] irréductible, et (res) : res_p : Sel(ℚ, V) → E(ℚ_p) ⊗ ℚ_p isomorphisme | corang 1 ⇒ ord = 1 | toutes les conditions sur le conducteur, au prix de (res) | ÉTABLI (p. 1–2) |
| Castella, arXiv 2409.01360, Thm 1.1 | réduction **multiplicative** en p > 3, E[p] irréductible, réduction multiplicative non déployée en un q ≠ p où E[p] est ramifiée, E(ℚ_p)[p] = 0 | corang 1 ⇒ ord = 1 | **(e)** (invariant L) dans le cas multiplicatif | ÉTABLI (p. 1) |
| Castella–Wan, arXiv 1607.02019 | supersingulier | « version renforcée du réciproque de Skinner » | — | À VÉRIFIER (seul le résumé a été lu) |
| Keller–Yin, arXiv 2410.23241 | p ≥ 3 d'Eisenstein (E[p] réductible), potentiellement bon ordinaire | réciproques de rang 0 et 1 | densité nulle (p-isogénie) ; ils améliorent des proportions **dans des familles de tordues** | ÉTABLI (résumé, §0.7) |

**Du 5-Selmer au corang (DÉDUCTION).** Si E[p] est irréductible (donc E(ℚ)[p] = 0), si S_p(E) ≅ ℤ/p et si le signe vaut −1, alors le corang de Sel_{p^∞} est ≤ dim S_p = 1, et il est impair (théorème de p-parité de Dokchitser, déjà utilisé par BSZ), donc égal à 1. Sel_{p^∞} ≅ ℚ_p/ℤ_p, d'où Ш[p^∞] = 0. Les hypothèses de BSTW Thm 12.3 sont donc satisfaites. Castella (2409.01360, Cor. 1.2) fait la même remarque dans son cadre.

## 3. Ce que l'inventaire suggère (à confirmer à l'étape 2)

Avec p = 5, les nouveaux théorèmes remplacent :
- le Théorème 5 par : **bonne réduction ordinaire en 5** et E[5] irréductible (sans (c)), ou supersingulière avec N sans facteur carré (BSTW 1.6), ou multiplicative avec les hypothèses de Skinner–Urban ;
- le Théorème 9 par : **bonne réduction ordinaire en 5**, ou supersingulière avec N sans facteur carré (BSTW 12.3), ou multiplicative sous les hypothèses de Castella.

Les familles concernées sont définies par des conditions de congruence (réduction mod 5, N sans facteur carré), comme chez BSZ : la moyenne 6 du 5-Selmer s'y applique (Bhargava–Shankar, via BSZ §2.3). Il faudra refaire l'équirépartition des signes pour ces nouvelles familles (BSZ §3.2–3.5).

**Personne n'a refait ce calcul à ma connaissance** (recherches arXiv par titre et résumé, et web, le 26 novembre 2026). Je ne peux pas l'exclure : la recherche arXiv ne porte pas sur le texte intégral.

## 4. Réserves

- BSTW (2409.01350), Castella (2409.01360) et Keller–Yin sont des prépublications. Kim (2109.12344) indique une version de 2022 ; sa publication en revue n'est pas vérifiée.
- J'ai lu les énoncés, pas les preuves.
- Les cas CM et les premiers d'Eisenstein sont de densité nulle et ne changent rien au pourcentage.
- Le plafond ≈ 79 % pour p = 5 seul reste : au-delà, il faut combiner p = 3 et p = 5, ce qui demande une information sur la distribution jointe des Selmer que je n'ai pas vue dans la littérature lue.
