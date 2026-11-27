# Bilan du 27 novembre 2026 (branche ccr-1b1ab8f4-2hr1mt)

**Statut : rien n'est démontré au sens d'une preuve validée.** Tout reste conditionnel à la relecture par des spécialistes, et à BSTW et Castella (des prépublications) pour la base.

## 1. Revérification demandée (`lit/reverification_27_11.md`)

| Affirmation | Verdict |
|---|---|
| « Le Lemme 8.14 de Wan est faux tel qu'énoncé » | **Confirmé.** On a maintenant une preuve de trois lignes, valable pour tout s > t : Φ(n(ϖ^{s−t−1})) = −Φ(1)/(q−1) ≠ 0. Le calcul numérique est concordant dans trois cas, exactement |
| « La recette de CLW pourrait avoir une lacune aux places décomposées » | **Confirmé et renforcé.** Avec les vecteurs mêmes du Lemme 8.17 de Wan, l'intégrale locale est **nulle** (Prop. V). La preuve est courte et n'utilise que la théorie des formes nouvelles. Ce résultat ne dépend pas du 8.14. CLW en dépendent si, comme Wan l'écrit lui-même (Rem. 8.19), ce sont bien les vecteurs de leur construction. D'où le « pourrait » |
| « La Proposition R la corrigerait » | **Confirmé, avec une preuve plus simple et plus générale** (Prop. R′). Elle vaut pour toute π_v et tout caractère A, trivial compris. Elle n'utilise que le support dans le modèle de Kirillov. Nouvelle vérification numérique dans le modèle induit (non ramifiée, Steinberg) |

**Conséquence pratique.** Côté A, plus besoin de classer les types locaux en 2 et 3 : tous sont couverts.

## 2. Les 26 objections (`lit/relecture_adverse.md`, section du 27/11)

Toutes ont été traitées :
- **réglées** : 1-8, 12, 14, 17, 18, 25 ;
- **caduques** : 7, 10, 11, 21, 23 ;
- **réparées** : 13, 19, 26 ;
- **en grande partie réglées** : 9, 15, 16 (il reste [Dia97a] à confirmer) ;
- **en partie** : 24 ;
- **héritée de BSTW** : 20 ;
- **inchangée** (mineure) : 22.

## 3. Deuxième tour d'autocritique (`lit/relecture_adverse_2.md`)

Dix nouvelles objections. Les trois importantes :
- **N2 (nouvelle, côté B).** En 2 et 3, certaines courbes ne sont pas au « niveau minimal » qu'utilise la preuve de B : des formes d'un autre type peuvent leur être congruentes au même niveau. On les exclut prudemment. Elles représentent 3,2 % des courbes en 2 et 0,27 % en 3.
- **N6 (héritée).** Le rang 1 utilise la tordue g_K. Aux premiers de D_K, le même phénomène peut se produire. BSTW ont exactement le même point non traité dans leur cas publié.
- **N7 (question pour Wan).** La condition (iv) de CLW au premier auxiliaire ℓ semble incompatible avec la torsion par ν.

Le troisième tour n'a pas fait apparaître de nouvelle objection critique propre à notre travail. J'ai donc arrêté là.

## 4. Chiffrage (`scripts/bound_v3.py`)

| Scénario | Borne |
|---|---|
| Aujourd'hui (BSZ + BSTW + Castella) | 67,02 % |
| **Prudent** (A : tous types ; B : sans les cas non minimaux N2) | **78,61 %** |
| Optimiste (si les cas N2 se récupèrent) | 79,03 % |

## 5. Document anglais et spécialistes

- `bsd/REPORT_EN.pdf` : 13 pages au format amsart, style article, avec énoncés, preuves, statut de chaque résultat, tables numériques, 5 questions précises et références (toutes ouvertes, sauf la liste explicite de celles qui ne l'ont pas été).
- `bsd/SPECIALISTES.md` : Wan (déjà contacté), Hsieh, Castella, Kim (ou Ota), Burungale, avec les adresses tirées des articles. **Rien n'a été envoyé.**

## 6. Pour la suite

- **Si Wan répond.** Lui envoyer la Prop. V (quatre lignes), qui est plus nette que le contre-exemple au 8.14, et poser la Question 3 (condition (iv) en v = ℓ).
- **Lectures à faire.** [Hsi12] et Diamond 1997a, Déf. 3.1.
- **Ce qui pourrait redonner 0,4 point** : récupérer les cas N2 via [Dia97b] et l'invariance par torsion.
