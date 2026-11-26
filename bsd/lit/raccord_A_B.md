# Raccord de A et B dans la chaîne de BSTW (p = 5 supersingulier)

26 novembre 2026. A et B sont **supposés validés** (décision de l'utilisateur, en attente des spécialistes) : `probleme_A_note.md` §11 et `probleme_B_redaction.md`. Source : BSTW, arXiv 2409.01350, lu aux §10.1–10.3 et 12.1. Ce document est une DÉDUCTION, sauf mention contraire.

## 1. La chaîne de BSTW (ÉTABLI, lu)

- **Rang 0 (Th. 1.6).** La conjecture principale de Kobayashi pour g (Th. 10.1) donne : corang 0 ⇒ L(1, E) ≠ 0.
- **Rang 1 (Th. 12.3).** On choisit L vérifiant (2.15) (p décomposé), (9.9) ((D_L, N) = 1) et (Heeg) (tout ℓ | N décomposé dans L), avec ord_{s=1}L(s, g/L) = ord_{s=1}L(s, g), d'après Friedberg–Hoffstein [51]. Puis « by Theorem 9.21(c) and **Theorem 10.1** Kato's main conjecture holds for **g and the quadratic twist g′ = g ⊗ χ_L** », et la Prop. 12.1 conclut. La Prop. 12.1 n'a **aucune** hypothèse « sans facteur carré ».
- **Th. 10.1, preuve au §10.3.** « Since g is semistable, there exists a prime q | N satisfying (ram) [...] Pick an imaginary quadratic field L such that (2.15) holds and (D_L, 2N) = 1. Suppose also that either q is inert in L and the primes dividing N/q split, or that (def) holds. » On applique ensuite le Th. 10.5 (c'est là qu'interviennent A et B), la Prop. 10.7 et le Th. 10.4(b). « The same argument applies for the quadratic twist g_K. »
- **Hypothèse sans facteur carré.** Les Th. 10.4 et 10.7 et la Prop. 12.1 n'en ont pas (déjà noté au §5, point 5, de `calcul_local_supercuspidal.md`). L'hypothèse « N square-free » des Th. 10.1, 1.6 et 12.3 vient uniquement du Th. 10.5, c'est-à-dire de A et B.

**Conséquence.** Il faut A + B pour **deux** formes : f = g (le conducteur N de E) et f = g′ = g ⊗ χ_L. Pour g′, le conducteur est N·D_L², non sans facteur carré même si E est semistable. BSTW traitent ce cas avec « essentially the same argument ».

## 2. Choix du corps auxiliaire L″ pour f ∈ {g, g′} (Th. 10.1 appliqué à f)

Données :
- q, un premier multiplicatif de E avec E[5] ramifiée en q, c'est-à-dire (ram) (5 ∤ v_q(Δ)). Il existe pour 100 % des courbes (BSZ, Lemme 20, acquis au §5) ;
- D_L, le discriminant du corps de Heegner L du Th. 12.3.

On demande à L″ (imaginaire quadratique) :
1. 5 décomposé, (2.15) ;
2. (D_{L″}, 2·5·N·D_L) = 1, ce qui donne (9.9), (2.16) et (D_{L″}, 2N(f)) = 1 ;
3. q inerte ;
4. **tous** les autres premiers divisant N(f) décomposés : 2, 3, les autres premiers multiplicatifs, et les premiers de D_L pour f = g′.

**Existence.** C'est un nombre fini de conditions locales en des premiers distincts, plus « imaginaire ». Le théorème des restes chinois et Dirichlet donnent une infinité de tels L″. **DÉDUCTION standard.**

**Vérification des hypothèses, point par point.**

| Exigence | Où | Satisfaite ? |
|---|---|---|
| (spl) CLW/BSTW Th. 9.24 : un q \| N⁻ ; 2 décomposé | A | ✓ : q inerte, 2 décomposé |
| CLW §5.2 : aux places non décomposées, π_v non ramifiée, Steinberg ou Steinberg tordue par le quadratique non ramifié | A | ✓ : seule q est inerte. Pour g, π_q est Steinberg. Pour g′, π_q = St ⊗ χ_{L,q} avec χ_L non ramifié en q (car q ∤ D_L), donc tordue par un quadratique non ramifié |
| Places supercuspidales (2, 3) décomposées | A | ✓ (condition 4). Pour g′, χ_L est non ramifié en 2 et 3, donc π_2 ⊗ χ_L reste supercuspidale de même conducteur |
| Places de D_L (f = g′) : série principale ramifiée π(χ_{L,ℓ}μ, χ_{L,ℓ}μ^{-1}), décomposée | A | voir §3, point 2 |
| (def) : N⁻ = q, un nombre impair de premiers, (ram) | B | ✓. Pour g′, ρ̄′ = ρ̄ ⊗ χ_L est ramifiée en q si et seulement si ρ̄ l'est |
| Niveau minimal en N⁺ (B, étape 4) | B | ✓ en 2 et 3 supercuspidaux (inertie d'ordre premier à 5). ✓ en ℓ \| D_L : inertie d'ordre 2, conducteur ℓ² = cond(ρ̄′). ✗ aux premiers multiplicatifs décomposés où ρ̄ est non ramifiée : voir §3, point 3 |
| Premiers vexants (ℓ ≡ 4 mod 5, ρ̄\|G_ℓ irréductible, ρ̄\|I_ℓ réductible) | B | ✓ : 2 et 3 ne le sont pas. Pour ℓ \| D_L, ρ̄′\|G_ℓ = χ_{L,ℓ}⊗(non ramifiée) est réductible, donc non vexant. Il n'y a pas d'autre premier additif dans le périmètre des 79 % (additif seulement en 2 et 3) |
| (CR⁺)(4) : q′ ‖ N⁺, q′ ≡ 1 mod 5 ⇒ ρ̄ ramifiée en q′ | B | exclusion d'environ 5·10⁻⁶ (`probleme_B_note.md` §4) |

## 3. Ce que le raccord laisse en suspens ou exclut

1. **Steinberg tordu par un caractère ramifié en 2 ou 3** (réduction potentiellement multiplicative). Ni la lecture (L1) ni la lecture (L2) de A ne couvrent ce cas : les arguments utilisent la supercuspidalité. CLW §5.2 ne l'autorise pas aux places non décomposées, et Wan §8 ne le traite pas aux places décomposées. **On l'exclut.** D'après la table des types en 2 (`DEUX_PROBLEMES_OUVERTS.md`), c'est 0,1 % des modèles concernés.
2. **Séries principales ramifiées** : en 2 et 3 (« série principale quadratique », 6,5 % des modèles en 2) et aux ℓ | D_L pour g′. BSTW les couvrent par Wan §8D (Lemmes 8.13–8.17). Le contre-exemple au Lemme 8.14 (`probleme_A_note.md` §9.3, §10) **met cet appui en doute dans la lecture (L1)**. En lecture (L2), le critère du §4 est satisfait, mais je n'ai pas refait de calcul explicite pour une série principale. **Point à faire valider avec la question 3 à Wan.** C'est aussi un point dont dépend BSTW lui-même, pour g_K.
3. **Premiers multiplicatifs décomposés où ρ̄ est non ramifiée** (5 | v_q(Δ)). Le niveau n'est pas minimal, donc Σ ≠ ∅ dans CH §6. Deux options :
   - les traiter par la montée de niveau de CH (Lemmes 6.3, 6.4, Cor. 6.7), plus le critère de Diamond 1997b, Th. 2.4, qui n'a pas été ouvert ;
   - les exclure. Le coût est de l'ordre de Σ_{q ≥ 5}(q − 1)²/q⁷ ≈ 6·10⁻⁵, à recalculer.
4. **(ram) pour E.** Il faut un premier multiplicatif avec E[5] ramifiée. L'existence vient de BSZ, Lemme 20 (« 100 % »), acquis au §5 mais non relu ici.

## 4. Bilan chiffré provisoire

D'après la table des gains (`DEUX_PROBLEMES_OUVERTS.md`) :
- 67,02 % aujourd'hui ;
- + séries principales et Steinberg tordu en 2 et 3 → 67,55 % ;
- + type quelconque en 2 et 3 → **79,03 %**.

Avec A et B validés et le raccord ci-dessus :
- le gain supercuspidal (≈ 11,5 points) est acquis ;
- les séries principales (≈ 0,5 point au plus) dépendent du point 2 ;
- le Steinberg tordu est perdu (une fraction de 0,5 point) ;
- les autres exclusions sont de l'ordre de 10⁻⁴.

**Fourchette attendue : environ 78,5 % à 79,0 %.** C'est une DÉDUCTION, à recalculer avec `gain_table.py` en retirant explicitement ces cas.

## 5. Reste à faire

- Recalculer la borne avec `bsd/scripts/gain_table.py` et `local_types.py` (branche `claude/artifact-review-prompt-pfjqwc`) en retirant les cas du §3.
- Relire BSZ, Lemme 20 (existence de q).
- Point 2 du §3, à ajouter à la validation par Wan.

## 6. Premier chiffrage (26 novembre)

Scripts : `bsd/scripts/local_types_v2.py` (raffinement de `local_types.py`) et `bsd/scripts/bound_v2.py` (même formule que `gain_table.py`). Résultats dans `bsd/results/`.

- **Types locaux** (cellules (A, B) mod 2⁸ et mod 3⁵, normalisation de BSZ, cellules indéterminées exclues). La classe « autre » de l'ancien script est scindée :
  - « ps_sup » : bonne réduction sur une extension cyclique ramifiée, Q(ζ₉)⁺ en 3 et les deux quartiques cycliques de conducteur 16 en 2, éventuellement après une tordue quadratique. Inertie abélienne, donc série principale ;
  - « sc » : supercuspidale.

  | | semistable | Steinberg tordu | SP quadratique | SP d'ordre > 2 | supercuspidale | indéterminé |
  |---|---|---|---|---|---|---|
  | ℓ = 2 (k = 8) | 0,29 % | 0,10 % | 6,45 % | 0,81 % | 92,33 % | 0,02 % |
  | ℓ = 3 (k = 5) | 66,67 % | 0,27 % | 0,82 % | 2,75 % | 29,47 % | 0,01 % |

- **Bornes (DÉDUCTION, A et B supposés validés).** ε ≈ 5,3·10⁻⁵ exclut les premiers multiplicatifs ≥ 7 de niveau non minimal.

  | Scénario | μ₂ | μ₃ | Borne |
  |---|---|---|---|
  | **S_A** : semistable + supercuspidal (séries principales et Steinberg tordu exclus) | 0,926 | 0,961 | **77,71 %** |
  | **S_A+SP** : + séries principales ramifiées (si le point 2 du §3 est validé) | 0,999 | 0,997 | **78,98 %** |
  | Référence (tous types, table d'origine) | 1 | 1 | 79,03 % |
  | Aujourd'hui (semistable partout) | | | 67,02 % |

- **Lecture.** Le gain certain (S_A) est de **+10,7 points** sur 67,02 %. La part qui dépend de la validation des séries principales (point 2 du §3, Lemme 8.14 de Wan) est de 1,27 point. Le Steinberg tordu et les autres exclusions coûtent environ 0,05 point.
- **Réserves.**
  - La constante 19/24, la famille de base et P₇ (semistable en ℓ ≥ 7) sont repris tels quels de `gain_table.py`, sans nouvelle vérification ici.
  - Le classement ps_sup / sc repose sur un critère d'abélianité de l'inertie, vérifié seulement sur ces corps tests (DÉDUCTION : en ℓ = 3 l'inertie abélienne d'ordre 3 ou 6 provient de Q(ζ₉)⁺ ; en ℓ = 2 l'ordre 4 provient des deux quartiques de conducteur 16).
  - ε est une approximation.
