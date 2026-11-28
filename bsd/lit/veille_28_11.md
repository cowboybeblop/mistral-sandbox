# Veille du 28 novembre 2026 : y a-t-il des avancées ?

Recherches web et lecture des résumés arXiv (pages /abs). **Aucune avancée trouvée ne débloque nos verrous.** Le détail suit.

## 1. Proportion de courbes vérifiant BSD
Aucune amélioration de 66,48 % / 67,02 % trouvée. arXiv 2601.16044 (janvier 2026) cite encore « at least 66% ».

## 2. Équirépartition des signes et problème de parité
- **Helfgott** (math/0408141, annexe C, lu) : pour la famille de toutes les courbes, il faudrait « show that λ(a² − b³) averages to zero », ce qui « remains open ».
- **Teräväinen** (2010.07924, Th. 2.12, lu) : λ(am² + bn^k) prend les deux signes une infinité de fois, ce qui couvre 27B² + 4A³. Il précise : « unable to say anything about this much stronger mean 0 property ».
- **Wang–Yang** (2610.34912, octobre 2026, résumé lu) : Chowla dynamique pour des polynômes à plusieurs variables « whose Birch rank is sufficiently large in terms of their degree ». **Ne s'applique pas** à un polynôme en 2 variables comme 4A³ + 27B².
- **Formes binaires aléatoires** (2506.18065, juin 2025, résumé lu) : Chowla « with probability 1 » pour des formes **homogènes** prises au hasard. **Ne s'applique pas** à notre polynôme, fixé et non homogène.
- **Sawin–Sutherland** (2504.12295, lu) : leur résultat porte sur ε(E)·a_n avec n de l'ordre de N(E), pas sur la moyenne de ε.
- Dalal et Gerbelli-Gauthier (2410.01976) : signes pour des représentations autoduales sur GL_N, dans un autre cadre (familles automorphes, pas courbes ordonnées par hauteur). Non lu en détail.

## 3. Groupes de Selmer
- Rien pour n ∉ {2, 3, 4, 5} sur ℚ.
- 2604.16978 (avril 2026) étend n = 2 à 5 aux corps globaux.
- 2508.21406 et 2606.06327 portent sur des familles à isogénie ou des Selmer d'isogénie (familles minces).
- Second moment de Sel₂ ≤ 15 (Bhargava–Shankar–Swaminathan, 2110.09063, 2021) ; nous avons montré qu'il n'aide pas (`HORIZONS_85.md` §3).

## 4. Réciproques (p-converse) et conducteur non sans facteur carré
- **Kim** (2109.12344, résumé lu) : réciproque « soft » en p > 3 ordinaire, « no condition on the conductor ». Mais elle suppose Ш fini (« rank one and Ш finite iff analytic rank one »), donc elle est **inutilisable pour des bornes de Selmer**.
- Rien de nouveau pour le cas supersingulier non sans facteur carré (le nôtre), ni pour p = 3.

## 5. Cas non minimaux (E2/E3) et modules de congruence
- **Böckle–Khare–Manning** (1910.08507, 2108.09729, résumés lus) : « If ρ̄ is scalar at some primes dividing the discriminant of the quaternion algebra, then Hecke algebra is still isomorphic to the deformation ring, but is not a complete intersection, or even Gorenstein ». Ils calculent le défaut de Wiles.
- **Signal d'alerte.** Dans les situations non minimales, le rapport des périodes peut ne pas être une unité. Notre E3 n'est pas exactement leur cas : en q = 2 ou 3, la tordue a des valeurs propres de Frobenius {±1, ±q}, distinctes mod 5. Mais il faut garder ce point en tête pour la piste 3.

## 6. Non-annulation pour N6
- **Chao Li** (1606.03172, Th. 1.4 et 1.12, lus) : tordues explicites de rang 0 et 1, avec d produit de premiers dans un ensemble de Chebotarev S = {ℓ ∤ 2N : ℓ décomposé dans K, Frob_ℓ d'ordre 3 dans Gal(ℚ(E[2])/ℚ)}. C'est sous l'hypothèse (⋆) : 2 décomposé dans K, et une condition mod 2 sur log P de Heegner.
  - (⋆) **n'est pas une condition locale**, donc on ne peut pas en faire une famille large. Cela ne règle N6 que courbe par courbe, pas en densité.
  - C'est quand même la meilleure piste connue pour des discriminants à facteurs premiers prescrits.
- **arXiv 2610.31631** (octobre 2026, résumé lu) : classes de Kolyvagin 2-primaires par tordues simultanées, sous surjectivité mod 2^L. Même remarque : utile courbe par courbe.
