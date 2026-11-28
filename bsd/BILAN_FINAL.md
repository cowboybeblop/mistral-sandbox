# Bilan final (27 novembre 2026)

**Statut : rien n'est démontré au sens d'une preuve validée par la communauté.** Tout est à faire relire par des spécialistes. La base (BSTW, Castella) repose sur deux prépublications.

## 1. Le problème
Faire passer la proportion de courbes elliptiques vérifiant BSD (partie rang, rang ≤ 1) de **67,02 %** vers environ 79 %. BSZ (§4) prévoyaient 79,7 % si leur théorème clé s'étendait au cas supersingulier. Le verrou : l'hypothèse « conducteur sans facteur carré » de BSTW et CLW. CLW eux-mêmes écrivent en août 2026 qu'elle « should be removable with some more work ».

## 2. Apports nouveaux (vérifiés sur sources)

| Apport | Statut |
|---|---|
| Le Lemme 8.14 de Wan (ANT 2020) est faux tel qu'énoncé | preuve de 3 lignes, 3 vérifications numériques |
| Avec les vecteurs du Lemme 8.17 de Wan, l'intégrale locale est **nulle** (Prop. V) | preuve courte (Casselman Th. 1 vérifié sur source) |
| La recette de CLW (version **publiée**, Forum Math. Sigma 2022, p. 39, 40, 70-71, 78, inchangée) annulerait l'intégrale aux places décomposées ramifiées, même en niveau sans facteur carré | conditionnel à l'identification des vecteurs locaux (affirmée par Wan, Rem. 8.19) |
| Réparation uniforme, pour tout type local (Prop. R′) | preuve complète modulo le support du Lemme 8.13 (vérifié numériquement en 2 et 3) |
| Côté B : cas non minimaux en 2 et 3 (E1-E3), réels au sens standard (Kim–Ota Déf. 3.5) ; observation sur le Lemme 6.5 de CH | exclus prudemment |
| Point laissé ouvert par BSTW : la tordue g_K aux premiers de D_K (rang 1) | signalé, hérité |

## 3. Ce qui n'est pas de nous (crédité)
- L'objectif 79-80 % (BSZ).
- N⁺ quelconque dans l'interpolation et dans μ = 0 (Chida–Hsieh, Cornut–Vatsal).
- Le passage ordinaire → cristallin (Kim–Ota Rem. 6.6, Taylor 2006).
- Le cas supercuspidal de base (Fouquet–Wan).

## 4. Chiffrage conditionnel
- **78,61 %** (prudent) ;
- 79,03 % si les cas E1-E3 sont récupérés via Diamond 1997b ;
- aujourd'hui : 67,02 %.

**Mise à jour du 27/11 au soir** (`scripts/bound_v5.py`, `lit/piste1_equirepartition.md`, `lit/piste2_additif_l7.md`) :
- **79,30 %** avec l'équirépartition des signes (piste 1) ;
- **79,75 %** en ajoutant la réduction additive en ℓ ≥ 7, ℓ ≢ ±1 (mod 5) (piste 2) ;
- **80,19 %** si E2 et E3 sont récupérés en plus (piste 3, bloquée par Diamond 1997a et 1997b).

**Mise à jour finale (nuit du 27/11)** (`scripts/bound_v6.py`, `lit/verification_finale_27_11.md`) : **79,81 %** en version prudente (pistes 1, 2, 4, 6, 7) ; 80,25 % si E2 et E3 sont récupérés ; plafond ≈ 81,3 % avec p = 3 (hors de portée aujourd'hui). Conditionnel à A, B, N6 (ouvert), BSTW et CLW. Relecture adverse n° 3 (`lit/relecture_adverse_3.md`) : κ confirmé par un test global indépendant (0,5587 ± 0,0008) ; deux erreurs corrigées dans la note sur N6 ; chiffre inchangé. Relecture n° 4 (`lit/relecture_adverse_4.md`) : κ prudent confirmé globalement (0,5709 ± 0,0029) ; Steinberg tordu réglé au niveau DÉDUCTION ; aucune nouvelle erreur.

**E3 (28/11)** : la comparaison des périodes se réduit à la multiplicité un (Vatsal 2003, Pollack–Weston). Tests numériques : 9 courbes E3 sur 9 OK. Appui théorique : Böckle–Khare–Manning, Prop. 6.2 (ρ̄ non scalaire, donc intersection complète). E3 est plausiblement récupérable (+0,4 pt), mais ce n'est pas démontré. Voir `lit/programme_realiste.md` §4.

**Horizons (28/11)** : 85 % est inaccessible avec les outils connus (plafond 81,7 %) ; 83,3 % si les signes sont équirépartis (conjecture de BSZ). Voir `HORIZONS_85.md`.

Constat en passant : des coquilles probables dans les tables 3 et 4 de Bhargava–Shankar (arXiv 1312.7859), sans effet sur leurs théorèmes (κ ≈ 0,558 ≥ 0,5501).

## 5. Vérifications externes
- Aucun erratum, aucune extension concurrente, aucune amélioration du pourcentage trouvés (recherches du 27/11).
- Indépendant de l'annonce sur l'hypothèse de Riemann (Alpöge et Claude, 20/11/2026), dont la portée vérifiée exclut les fonctions L de courbes elliptiques. Même GRH ne donnerait pas ce résultat (Young, Fiorilli).

## 5 bis. Réponse de Wan (fin novembre)
- **Le cas supercuspidal de A est confirmé par l'auteur** : la recette de Fouquet–Wan (Prop. 7.27) et notre lecture des conducteurs.
- Il n'a pas répondu sur les Lemmes 8.14 et 8.17 (séries principales et Steinberg), qui touchent le cas publié et notre rang 1.
- Une relance courte est prête (`lit/reponse_wan.md`). Il faut aussi lui demander l'autorisation de citer sa réponse.

## 6. Questions ouvertes pour les spécialistes
1. Séries principales et Steinberg : la Prop. V et la Prop. R′ (Wan, relance prête). Le cas supercuspidal est **réglé** par la réponse de Wan.
2. La condition (4) au premier auxiliaire ℓ est-elle compatible avec la torsion par ν ? (Wan)
3. L'insertion de la Prop. R′ dans CLW §5.6 est-elle compatible avec le reste de l'article ? (Castella)
4. Le Lemme 6.5 de CH dans les cas E2 et E3, et la récupération via Diamond 1997b ? Même question pour les ℓ ≥ 7 additifs (piste 2) et le Steinberg tordu. (Hsieh, Kim)
5. La tordue g_K aux premiers de D_K ? Obstruction : D_K premier impair est impossible avec des premiers « propres » (seule exception : ℚ(i), sans usage général). Existe-t-il un théorème de non-annulation pour D = −ℓ₁ℓ₂ dans un ensemble de Chebotarev ? (Burungale, Hsieh)

## 7. Documents
- `bsd/NEW_RESULTS_EN.pdf` : document à montrer (nouveautés seulement, 13 p.).
- `bsd/REPORT_EN.pdf` : rapport complet.
- `bsd/SPECIALISTES.md` : Wan (contacté, en attente), Hsieh, Castella, Kim ou Ota, Burungale. **Rien n'a été envoyé.**
- Détails : `bsd/lit/` (revérification, deux relectures adverses, vérifications web, lien HR-BSD).
- Scripts et résultats : `bsd/scripts/`, `bsd/results/`.

## 8. Suite possible
1. Attendre Wan, puis lui envoyer la Prop. V.
2. Envoyer ensuite `NEW_RESULTS_EN.pdf` aux autres spécialistes.
3. En option : Diamond 1997b, pour +0,4 point.
4. Au-delà de 79 % : voir `bsd/PLAN_AU_DELA_79.md` (spéculatif).
