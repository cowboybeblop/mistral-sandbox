# Liste des pistes pour gagner des pourcentages (27 novembre 2026)

> **Mise à jour finale du 27/11 (nuit) : toutes les pistes examinées.** Chiffre consolidé : **79,81 %** (prudent), 80,25 % (optimiste), `scripts/bound_v6.py`. La vérification est dans `lit/verification_finale_27_11.md`.
> - Piste 6 faite (+0,005 pt) ; piste 7 faite (+0,001 pt) ; piste 4 faite pour la partie abordable (+0,06 pt). **Le plafond de la méthode de BS est atteint** (κ = P(d = −1) = 0,5587) ; les « +0,4 pt par +0,05 » ci-dessous étaient faux. Voir `lit/pistes_6_7_4.md`.
> - Piste 8 : réduite à un énoncé de non-annulation (D = −ℓ₁ℓ₂ à facteurs « propres »). Obstruction : D_K premier est impossible. Indication numérique favorable. **Ouverte.** Voir `lit/piste8_N6.md`.
> - Piste 5 : plafond corrigé à **≈ +1,5 pt** (et non 2,5) : presque aucune courbe n'est ordinaire en 3. Verrous : (CR⁺)(1) de CH exclut p = 3, et la minimalité pose problème partout. Voir `lit/piste5_p3.md`.
>
> **Mise à jour du 27/11 au soir (pistes 1, 2, 3 traitées).** Chiffres conditionnels, mêmes hypothèses que 78,61 % (`scripts/bound_v5.py`).
> - **Piste 1 : faite.** 78,61 → **79,30 %** (prudent), 79,03 → 79,73 % (optimiste). Les signes locaux en 2 et 3 sont vérifiés par l'équation fonctionnelle. Constat en passant : plusieurs entrées des tables 3 et 4 de Bhargava–Shankar semblent fausses, sans conséquence pour eux (κ vrai ≈ 0,558 > 0,5501). Voir `lit/piste1_equirepartition.md`.
> - **Piste 2 : faite (version prudente, ℓ ≢ ±1 mod 5).** +0,42 pt seule ; avec la piste 1, **79,75 %** (prudent) et 80,19 % (si la piste 3 aboutit). Voir `lit/piste2_additif_l7.md`.
> - **Piste 3 : partielle, bloquée.** E1 est couvert par CH §6 tel quel (gain négligeable). E2 et E3 demandent Diamond 1997a et 1997b (non accessibles). Voir `lit/piste3_E1_E3.md`.
> - **Piste 4 : bonus.** κ = 0,5579 avec les signes recalculés, soit ≈ +0,05 pt sur la base (non intégré).

À traiter une par une, dans de nouvelles conversations, avec le skill `chercheur`.

**Point de départ** : borne prudente 78,61 %, optimiste 79,03 % (`scripts/bound_v3.py`, formule `base + (19/24)·SS5·μ2·μ3·P7·(1−ε)`). Aujourd'hui, dans la littérature : 67,02 %.

**Statut des gains** : estimations grossières (DÉDUCTION ou SPÉCULATION), calculées avec les constantes de `bound_v3.py`. Elles ne sont pas additives quand deux pistes touchent la même partie de la famille.

| # | Piste | Gain estimé | Difficulté | Type de travail |
|---|---|---|---|---|
| 1 | Équirépartition des signes dans la famille supersingulière (**faite : +0,69 pt**) | ≈ +0,70 pt | moyenne | calcul (PARI) + lecture |
| 2 | Réduction additive en ℓ ≥ 7 (**faite, prudent : +0,42 pt**) | ≈ +0,63 pt max | moyenne | théorie (cas B) + calcul |
| 3 | Récupérer les cas non minimaux E1-E3 en 2 et 3 (**E1 fait ; E2, E3 bloqués**) | ≈ +0,42 pt | moyenne à élevée | théorie (Diamond 1997b) |
| 4 | Améliorer κ = 0,5501 (familles à signes équilibrés plus grandes) | ≈ +0,4 pt par +0,05 sur κ ; jusqu'à ≈ +3,6 pts si κ → 1 | élevée (κ → 1) ; abordable en partie | calcul (tables de signes) |
| 5 | Le premier p = 3 pour les courbes additives en 5 | jusqu'à ≈ +2,5 pts | élevée | gros chantier |
| 6 | Cellules indéterminées et troncature | ≈ +0,005 pt | facile | calcul |
| 7 | Exclusion ε (q ≥ 7 multiplicatif, 5 \| v_q(Δ)) | ≈ +0,0006 pt | moyenne | théorie (niveau non minimal) |
| 8 | **Sécuriser le rang 1** (tordue g_K, point N6) | aucun gain, mais condition de **validité** de toute la borne | élevée | théorie |
| 9 | Questions ouvertes sur CLW (vecteurs locaux, condition (4) en ℓ) | condition de validité | — | attendre Wan |

---

## 1. Équirépartition des signes dans la famille supersingulière (≈ +0,70 pt) — priorité 1

- **Idée.** Sur une sous-famille où les signes sont moitié +1, moitié −1, la méthode donne 7/8 au lieu de 19/24 (BSZ, Th. 25, seconde partie).
- **Sources (ÉTABLI).**
  - BSZ, arXiv 1407.1826, Th. 16 : énoncé pour des familles définies modulo des puissances de premiers p ≡ 1 (mod 4), avec κ ≥ 0,5501.
  - Bhargava–Shankar, arXiv 1312.7859, §5, Prop. 35 : on utilise d(E) = r(E)·r(E₋₁) ; les familles F₁ et F₂ en 2 et 3 sont fermées par la torsion par −1 ; leurs tables de signes locaux viennent de [31] (Rizzo).
- **Pourquoi c'est ouvert pour nous.** Nos conditions en ℓ ≥ 7 (semistable) et en 2, 3 (exclusions E1-E3) sortent du cadre du Th. 16. Nos bornes utilisent donc 19/24 partout.
- **Méthode.**
  1. Vérifier que nos conditions locales sont stables par (A, B) ↦ (A, −B). La semistabilité en ℓ impair l'est, puisque χ₋₁ est non ramifié en ℓ impair. E3 en 3 aussi : a₃ change de signe et la condition porte sur ±. En 2, c'est à étudier.
  2. Recalculer κ pour notre famille avec `ellrootno` (PARI) sur les cellules mod 2^k et 3^k, en reproduisant les tables 3 et 4 de Bhargava–Shankar.
  3. Mettre à jour `bound_v3.py`.
- **Cible** : ≈ 79,7 % en version optimiste, c'est-à-dire la prévision de BSZ §4, et ≈ 79,3 % en version prudente.

## 2. Réduction additive en ℓ ≥ 7 (≈ +0,63 pt au maximum)

- **Constat.** La famille impose la semistabilité en tout ℓ ≥ 7 (facteur P7 ≈ 0,9499). Environ 5 % de la famille supersingulière est donc exclue.
- **Côté A.** La Prop. R′ vaut pour toute π_v générique en place décomposée, quel que soit ℓ. On choisit ℓ décomposé dans L″. Il faut vérifier que c'est compatible avec les autres conditions.
- **Côté B.** C'est la question de minimalité, comme en 2 et 3.
  - Si ℓ ≢ ±1 (mod 5), les types inertiels ont une image d'ordre premier à 5 : partie modérée divisant ℓ² − 1, avec 5 ∤ ℓ² − 1. L'argument du Lemme 6.4 (`NEW_RESULTS_EN.tex`) s'applique, avec des exclusions de type E2/E3 à calculer.
  - Si ℓ ≡ ±1 (mod 5) : ces premiers sont « vexants », il y a des congruences à changement de type modéré, et il faut exclure ou traiter à part.
- **Méthode.** Densités locales par ℓ (`local_types_v3.py`, adapté à ℓ ≥ 7), puis somme sur ℓ.

## 3. Récupérer E1-E3 en 2 et 3 (≈ +0,42 pt)

- **Constat.** On exclut 3,18 % des courbes en 2 et 0,27 % en 3 (`results/local_types_v3_*.json`). Ces cas sont réellement non minimaux au sens de Kim–Ota, arXiv 1905.02926, Déf. 3.5.
- **Piste.** On tord par χ_d (d ∈ {−1, ±2} en 2, d = −3 en 3, ramifiés seulement en q). On se ramène ainsi aux cas non minimaux m_q ∈ {1, 2} de E ⊗ χ_d, que CH traitent par montée de niveau : CH Lemmes 6.3 et 6.4, Cor. 6.7, [Tay06 §3], et **Diamond 1997b, Th. 2.4** (Invent. Math. 128, DOI 10.1007/s002220050144, à se procurer). Il faut ensuite un argument d'invariance par torsion de Ω_{N⁻} ~ Ω^can.

## 4. Améliorer κ (≈ +0,4 pt par +0,05 sur κ)

- **Constat.** κ = 0,5501 vient de familles définies modulo des puissances de 2 et 3 (Bhargava–Shankar, Prop. 35, densités 59,179 % et 40,32 %). BSZ conjecturent que µ_equi(F) = µ(F), « difficult to prove ».
- **Piste abordable.** Affiner les classes de congruence en 2 et 3 (k plus grand), et ajouter des premiers ≡ 3 (mod 4), pour faire grossir la partie où l'on contrôle d(E) = −1. Tout gain sur κ profite à **toute** la borne (base + supersingulier), pas seulement à notre famille.
- **Gain** : +0,05 sur κ donne ≈ +0,4 pt ; κ → 1 donnerait ≈ +3,6 pts, ce qui est hors de portée sans idée nouvelle.

## 5. Le premier p = 3 (jusqu'à ≈ +2,5 pts)

- **Constat.** Les courbes de réduction additive en 5 (≈ 4 % des courbes) ne sont couvertes par aucun théorème en p = 5. BSZ §4 : « working also with the prime 3 would push this lower bound over 80% ».
- **Piste.**
  - Utiliser la moyenne de Sel₃, qui vaut 4, d'où au moins 5/8 de rang de Selmer ≤ 1.
  - Utiliser les réciproques en p = 3 : BSTW Th. 1.6 avec la condition (1.7), et le cas ordinaire.
  - Cela demanderait de refaire A et B pour p = 3, ainsi qu'un nouveau chiffrage.
- **Difficulté** : gros chantier, à découper.

## 6. Cellules indéterminées (≈ +0,005 pt)

0,04 % en 2 et 0,006 % en 3 (`local_types_v3`). On les résout en augmentant k (le run k = 10 en 2 a été interrompu) et le nombre de relèvements aléatoires.

## 7. Exclusion ε (≈ +0,0006 pt)

Il s'agit des premiers multiplicatifs q ≥ 7 avec 5 \| v_q(Δ), au niveau non minimal. On les récupère avec CH Σ ≠ ∅ et Diamond 1997b, comme au point 3. C'est négligeable, à faire seulement en passant.

## 8. Sécuriser le rang 1 : la tordue g_K aux premiers de D_K (N6)

- **Aucun gain, mais toute la borne en dépend**, puisque le facteur 19/24 exige les rangs 0 **et** 1.
- Le point est aussi ouvert dans BSTW (cas publié) : en ℓ \| D_K, ρ̄\|I_ℓ = χ_K ⊕ χ_K, avec des congruences possibles à changement de type.
- **Piste.**
  - Invariance par torsion des modules de congruence (g_K ↔ g au niveau N·D_K²).
  - Ou choisir K de façon que les ℓ \| D_K évitent les congruences : ℓ ≢ ±1 (mod 5) et a_ℓ ≢ ±(ℓ + 1) (mod 5). Il faudrait alors un théorème de non-annulation avec ces contraintes en plus de Bump–Friedberg–Hoffstein, ce qui est à chercher.

## 9. En attente de Wan

- Les vecteurs locaux de CLW sont-ils ceux du Lemme 8.17 ? (Prop. V)
- La condition (4) en ℓ auxiliaire.

Voir `lit/reponse_wan.md`.

---

**Ordre conseillé.**
1. **Piste 1** : la plus rentable et la plus « calculatoire ».
2. **Piste 6** : facile, pour se mettre en jambes.
3. **Piste 2.**
4. **Piste 4**, partie abordable.
5. **Piste 3**, si Diamond 1997b est trouvé.
6. **Piste 8** en parallèle, si un spécialiste s'y intéresse.
7. **Piste 5** en dernier.
