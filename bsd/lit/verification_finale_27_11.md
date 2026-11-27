# Vérification finale des pistes 1 à 8 (recherche et autocritique)

27 novembre 2026, nuit. Ce document vérifie l'ensemble du travail du soir : pistes 1, 2, 3 (partielle), 4, 5 (cadrage), 6, 7 et 8 (réduction). La piste 9 attend la réponse de Wan.

## 1. Chiffre final (conditionnel)

`scripts/bound_v6.py`, `results/bound_v6.json` :

| Scénario | Borne |
|---|---|
| Littérature (BSZ, BSTW) | 67,02 % |
| Avant ce soir (S3 prudent) | 78,61 % |
| **Prudent, pistes 1, 2, 4, 6, 7** | **79,81 %** |
| Optimiste (E2, E3 récupérés, piste 3 bloquée) | 80,25 % |
| Plafond avec p = 3 (piste 5, si BSTW s'étendait en p = 3 supersingulier) | ≈ 81,3 % |

Le chiffre prudent reste conditionnel à :
- (a) A et B (Prop. V et R′, la question à Wan, la substitution ordinaire → plate dans CH) ;
- (b) **N6** (rang 1, piste 8), ouvert, comme pour BSTW eux-mêmes ;
- (c) BSTW et CLW (prépublication et article publié, tels que lus) ;
- (d) l'extension du Lemme types23 aux ℓ ≥ 7 (piste 2) et la lecture de Kim–Ota pour le Steinberg tordu.

## 2. Vérifications numériques indépendantes ajoutées

| Vérification | Méthode | Résultat |
|---|---|---|
| Signes locaux en 2 et 3 (piste 1) | équation fonctionnelle (`feq_check.py`, `feq_identity.py`) | 31/31 et 200/200 |
| μ₂, μ₃, classes de signes (pistes 1, 6) | Monte-Carlo mod ℓ⁴⁰ sans cellules (`mc_check_23.py`) | toutes les quantités à moins de 2σ des cellules (σ ≈ 5·10⁻⁴ à 1,4·10⁻³) |
| Densités de Kodaira en ℓ = 7 et 13 (piste 2) | Monte-Carlo (`mc_check_l7.py`) + test ciblé I₀* | accord ; un écart de −2,4σ sur I₀* (12 occurrences) relevait du bruit : 0,8567 contre 0,8572 sur 50 000 tirages ciblés |
| Types en 3 (piste 5) | Monte-Carlo (`p3_montecarlo.py`) | a₃ = 0 : 0,4428 (théorie 4/9) |
| Reproduction des nombres de BS (piste 1) | formule κ = ∏C/2 + 0,3∏D | 6 nombres sur 6 retrouvés exactement |
| Recalcul de v3 (`bound_v6`) | contrôle de non-régression | 78,606 % retrouvé |

## 3. Recherches web (27/11, nuit)

1. **Amélioration de 66,48 % / 67,02 % déjà publiée ?** Aucune trouvée. Un article de janvier 2026 (arXiv 2601.16044) cite encore « at least 66% ». Les seules nouveautés pertinentes repérées (arXiv 2604.16978, 2512.16120) portent sur d'autres questions (corps globaux généraux, familles à torsion).
2. **Version publiée ou erratum de BS (1312.7859) ?** Rien trouvé. Seule la v1 arXiv existe. La version publiée reste **non vérifiée** avant tout contact.
3. **Moyennes jointes Sel₃ / Sel₅ (piste 5) ?** Rien trouvé. Seule existe la conjecture de Bhargava–Kane–Lenstra–Poonen–Rains (moyenne σ(n)). Les curbes « Sel₅ de rang ≥ 2 » ne sont donc pas récupérables par p = 3, comme supposé.
4. **p = 3 supersingulier, conducteur non sans facteur carré ?** Rien trouvé. Castella–Wan (1506.02538) et Burungale–Kobayashi–Ota (2310.06813) supposent un conducteur sans facteur carré ou semistable. La piste 5 reste ouverte.
5. **Non-annulation avec des facteurs premiers de D restreints (piste 8) ?**
   - Coates–Li–Tian–Zhai (arXiv 1312.3884, Th. 1.1) donnent, pour k ≥ 2, « infinitely many square free integers M having exactly k prime factors such that L(E^(M), s) does not vanish at s = 1 ». C'est sous l'hypothèse (1) f([0]) ∉ 2E(ℚ), qui échoue dès que E(ℚ) n'a pas de 2-torsion, c'est-à-dire typiquement dans notre famille. **Non applicable en général.**
   - Aucun énoncé « tous les facteurs premiers de D dans un ensemble de Chebotarev » n'a été trouvé.
6. **Contenu de Diamond 1997b, Th. 2.4.** Il est confirmé par une source ouverte, Iyengar–Khare–Manning (arXiv 2206.08212 v3, p. 2-3) : « Diamond [23, Theorem 2.4] developed the results of Wiles and Lenstra by proving a numerical criterion for freeness of R-modules M finite flat over O, in terms of an augmentation λ : R → O supported on M », en termes du module cotangent p/p² et du module de congruence. C'est un critère d'algèbre commutative sans hypothèse de type. Cela **consolide la piste 7** (E1 via CH, cas Σ ≠ ∅), mais ne débloque pas E2 et E3 (piste 3), où le problème est la surjection R → T avec des conditions locales non minimales.
7. **Piste pour la piste 3.** Terracini, *A Taylor–Wiles system for quaternionic Hecke algebras*, Compositio Math. (2003), cité par CH pour (D5). Il n'est pas sur arXiv et l'hôte iris.unito.it est bloqué. **À se procurer**, en plus de Diamond 1997a et 1997b.

## 4. Autocritique : erreurs et corrections

1. **Défaut méthodologique** (constaté pendant la piste 5). Le critère « constant sur 3 relèvements aléatoires » (`local_types_v3`, `local_signs`, `refine_cells`) **ne voit pas les sous-ensembles rares d'une cellule**. Il a entièrement raté la classe « ordinaire en 3 » (≈ 2·10⁻⁵). Pour nos quantités, le Monte-Carlo indépendant (§2) borne l'effet à ≈ 10⁻³ en mesure, soit ≈ 0,01 pt sur la borne. **Pas d'impact sur les chiffres affichés à 0,01 pt près**, mais les scripts de cellules ne doivent plus être utilisés pour des classes de mesure inférieure à 10⁻³ sans contrôle Monte-Carlo.
2. **Estimation erronée de `LISTE_GAINS.md`, piste 4** : « ≈ +0,4 pt par +0,05 sur κ » par affinage. C'est **faux** : la méthode de BS est plafonnée par P(d = −1) = 0,55873, déjà atteint.
3. **Estimation erronée de `LISTE_GAINS.md`, piste 5** : « jusqu'à ≈ +2,5 pts ». Elle supposait implicitement des courbes ordinaires en 3. Le plafond réaliste est **≈ +1,5 pt**.
4. **Tables 3 et 4 de BS** : désaccords confirmés par l'équation fonctionnelle, sans effet sur leurs théorèmes. Ce n'est pas une erreur de notre part, mais c'est à présenter avec prudence. La version publiée n'est pas vérifiée.
5. **Objection ouverte de la piste 7** (condition de type BSZ Th. 9 (c) chez BSTW) : **réglée** par lecture. BSTW Th. 10.5 et §10.3 n'imposent que (ram), (def)/(indef), (2.15) et (irr_L). Le produit des nombres de Tamagawa ∏_{q|N⁻} c_q(g) ne porte que sur N⁻, pas sur les premiers E1 de N⁺.
6. **Obstruction de la piste 8** : vérifiée sur le texte. BSTW Th. 12.3 : « Let L be an imaginary quadratic field satisfying (2.15), (9.9) and (Heeg) », et (2.15) : « p splits in L ». Donc D_L premier est impossible avec des premiers propres.
7. **Non-additivité.** Les gains ont été recalculés ensemble (`bound_v6`), jamais additionnés à la main. Par exemple, la piste 2 fait baisser κ_ss de 0,0003.

## 5. Ce qui n'est pas de nous
- La méthode : BSZ et BS.
- Les réciproques : Skinner–Urban, BSTW, CLW, Wan.
- La comparaison des périodes : Chida–Hsieh.
- Le critère numérique : Diamond.
- Les signes locaux : PARI (Halberstadt, Rizzo).

## 6. Questions mises à jour pour les spécialistes
- **Question 4** (Hsieh, Kim) : E2 et E3 en 2 et 3, la même question en ℓ ≥ 7 additif (piste 2), le Steinberg tordu et Kim–Ota (2).
- **Question 5** (Burungale, Hsieh) : N6, avec en plus l'obstruction « D_K premier impossible » et la question d'un théorème de non-annulation pour D = −ℓ₁ℓ₂ à facteurs premiers dans un ensemble de Chebotarev.
- **Facultatif** (Shankar) : les coquilles des tables 3 et 4 (brouillon dans `piste1_equirepartition.md` §7, **non envoyé**).
