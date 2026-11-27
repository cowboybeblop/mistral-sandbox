# Plan pour dépasser 79 % (27 novembre 2026)

Statut des étiquettes : tout ce qui suit est SPÉCULATION ou CONJECTURE, sauf mention contraire. Rien de ce plan n'a été vérifié sur sources.

## 0. Préalable
- Vérifier l'annonce « 100 % » sur une source primaire : lien officiel, prépublication arXiv, auteurs. Non confirmée au 27/11. La recherche web n'a rien trouvé, et www-cdn.anthropic.com est bloqué depuis cette session.
- Attendre la réponse de Wan. A et B restent conditionnels.

## 1. Pourquoi 100 % est d'une autre nature
La méthode de BSZ minore une proportion à partir de la **moyenne** de Sel_5 (= 6). Cette moyenne seule plafonne :
- 19/24 sans équirépartition des signes ;
- 7/8 avec équirépartition.

Pour 100 %, il faudrait connaître la **distribution** complète des groupes de Selmer (ou de Sel_{p^∞}) dans la famille de toutes les courbes, et des réciproques p-adiques sans aucune exclusion. Aucune de ces deux choses n'est connue pour les courbes ordonnées par hauteur (à ma connaissance, à vérifier).

## 2. Étapes possibles, par gain estimé

| Étape | Gain espéré | Difficulté |
|---|---|---|
| E1. Récupérer les cas non minimaux N2 ([Dia97b] et invariance par torsion) | +0,4 pt (78,6 → 79,0 %) | moyenne |
| E2. Équirépartition des signes (BSZ Th. 16) dans notre famille avec conditions en 2 et 3, pour passer de 19/24 à 7/8 sur la partie supersingulière | quelques points (à chiffrer) | élevée |
| E3. Combiner p = 2, 3, 5 : utiliser les moyennes de Sel_2 et Sel_3 (Bhargava–Shankar) et des réciproques en p = 2 et 3 (BSTW pour p = 3 sous (1.7)) sur les courbes où Sel_5 est de rang ≥ 2 | à estimer, potentiellement le plus gros gain | très élevée (moyennes jointes non connues) |
| E4. Étendre les réciproques p = 5 au cas additif en 5 et aux cas exclus de la base | petit | élevée |
| E5. Résultats de distribution (type Smith, familles de tordues quadratiques), pour viser 100 % dans des **sous-familles** | 100 % dans des familles fines, pas pour toutes les courbes | très élevée |

## 3. Prochaine action concrète (si on continue)
- Chiffrer E2 et E3 avec bound_v3.py, en supposant les ingrédients acquis, pour savoir où est le vrai gain.
- Lire BSZ Th. 16 et §4 pour E2, et les résultats de distribution (Smith, Kane) pour E5. Chaque article sera ouvert avant d'être cité.

---

## Mise à jour (vérification du 27/11) : trois problèmes candidats

**1. Équirépartition des signes dans la famille supersingulière (recommandé, abordable).**
- ÉTABLI, BSZ Th. 16 : énoncé seulement pour des familles « defined by congruence conditions modulo powers of primes p ≡ 1 (mod 4) », avec κ ≥ 0,5501.
- ÉTABLI, BSZ p. 6 : « We conjecture that for any large family F, we have µequi(F) = µ(F). Although this seems difficult to prove ».
- La construction est celle de Bhargava–Shankar (arXiv 1312.7859, §5, Prop. 35) : d(E) = r(E)r(E₋₁), avec des familles F₁ et F₂ définies modulo des puissances de 2 et 3, fermées par la torsion par −1, et des tables de signes locaux en 2 et 3.
- Notre famille (conditions en 5 ≡ 1 mod 4, semistabilité en ℓ ≥ 7, exclusions E1-E3) n'est pas couverte telle quelle. Nos bornes utilisent encore 19/24 sur toute la partie supersingulière.
- DÉDUCTION, chiffrage grossier : si κ ≈ 0,55 tient dans notre famille, le facteur passe de 19/24 à 7/8 sur 55 % de la famille, soit environ +0,7 point (79,03 → ≈ 79,7 %, la prévision de BSZ ; 78,61 → ≈ 79,3 % en version prudente).
- Méthode : calcul des signes locaux avec PARI (ellrootno), vérification de la fermeture sous la torsion par −1 de nos conditions locales, recalcul de κ.

**2. N6 : la tordue g_K aux premiers de D_K (rang 1).**
- Ouvert, et déjà non traité dans le cas publié de BSTW.
- Théorique et difficile (liberté des modules de Hecke avec congruences à changement de type).

**3. Le premier p = 3.**
- ÉTABLI, BSZ §4 : « working also with the prime 3 would push this lower bound over 80% ».
- Aucun travail trouvé qui le fasse. Il faudrait les réciproques en p = 3 hors du cas sans facteur carré, et une combinaison des familles.
- Gros chantier.

**Recherches web (27/11).** Aucune généralisation du Th. 16 ni de l'amélioration avec p = 3 trouvée. Les μ = 0 récents (arXiv 2108.05958, 2508.11835) portent sur les groupes de Selmer, pas sur notre point B.
