# Pistes 6, 7 et 4 (les plus faciles)

27 novembre 2026, soir. Suite de `LISTE_GAINS.md`.
- Scripts : `scripts/refine_cells.py` et `scripts/bound_v6.py`.
- Résultats : `results/refine_l2_k8_18.json`, `results/refine_l3_k5_11.json` et `results/bound_v6.json`.

**Aucune preuve n'est annoncée** ; les chiffres sont conditionnels comme 78,61 %.

## Chiffrage consolidé (`bound_v6.py`, recalculé de bout en bout)

| Étape (cumulée) | Prudent | Optimiste (E2, E3 admis) |
|---|---|---|
| v3 recalculé (contrôle : redonne 78,606 %) | 78,606 % | 79,025 % |
| + piste 6 (cellules indéterminées) | 78,611 % | 79,025 % |
| + piste 1 (équirépartition) | 79,306 % | 79,734 % |
| + piste 2 (additif en ℓ ≥ 7, ℓ ≢ ±1 mod 5) | 79,751 % | 80,195 % |
| + piste 7 (E1 admis si q ≢ 1 mod 5) | 79,752 % | 80,195 % |
| + piste 4 (κ de la base recalculé) | **79,810 %** | **80,253 %** |

P(ℓ ≥ 7) est maintenant le produit exact des mesures locales, et non plus P₇·(1 − ε) linéarisé. Pour v3, l'écart est inférieur à 10⁻⁵.

## Piste 6 : cellules indéterminées (faite, +0,005 pt)

- **Méthode.** On part des cellules mod 2⁸ (resp. 3⁵). Une cellule non constante sur 3 relèvements aléatoires mod ℓ^{k+6} est découpée en ℓ² sous-cellules, jusqu'à 2¹⁸ (resp. 3¹¹). Le critère porte sur le type, les signes et le type de la tordue par −1.
- **Résultat.** La part indéterminée tombe de 4·10⁻⁴ à **1,9·10⁻⁷** en 2, et de 6·10⁻⁵ à **6·10⁻⁸** en 3. On a μ₂ = 0,96818 (au lieu de 0,96783) et μ₃ = 0,99725 (au lieu de 0,99720).
- Le raffinement fait apparaître E1 en 2 (2,6·10⁻⁵) et E2 (2,3·10⁻⁵ en 2, 9,6·10⁻⁶ en 3). Les grandes classes sont inchangées au 5ᵉ chiffre près (par exemple sp_quadratique_nonmin = 0,0317693 en 2, identique). C'est un contrôle de stabilité de `local_types_v3`.

## Piste 7 : exclusion ε et E1 (DÉDUCTION, +0,001 pt)

- Voir `piste3_E1_E3.md` §2. E1 en q correspond à **m_q = 1** dans CH §6 (cas Σ ≠ ∅), traité par CH : L_q, les Lemmes 6.3, 6.4 et 6.6, le Cor. 6.7, et [Dia97b, Th. 2.4] pour la Prop. 6.8.
- Les conditions de CH sont « If m_q = 1, then q ≢ 1 (mod p) » et (CR⁺)(4). L'exclusion est donc nécessaire **seulement pour q ≡ 1 (mod 5)**.
- La substitution ordinaire → plate n'intervient qu'en p, dans (D3). Les Lemmes 6.3 à 6.6 et le Cor. 6.7 ne portent que sur q ≠ p ; c'est lu.
- **Statut.** DÉDUCTION, à condition :
  - (a) que la substitution ordinaire → plate soit acceptée (déjà la question 4 aux spécialistes) ;
  - (b) que la Prop. 6.8 de CH, qui cite [Dia97b] non consulté, soit correcte.
- **Gain** : négligeable (+0,001 pt). Le point est surtout « propre » : il retire une exclusion inutile.

## Piste 4 : κ (faite pour la partie abordable : +0,058 pt ; plafond atteint)

- Avec les signes recalculés en 2 et 3 et **tous** les types en p > 3, on a **κ = 0,55872**.
- Il entre dans la base (familles S0(5) ∩ S1′(5), conditions en 5 seulement, et d₅ = +1 puisque 5 ≡ 1 (mod 4)) : **+0,058 pt**.
- **Plafond (DÉDUCTION).** La méthode de BS ne met en famille équirépartie que des courbes avec d(E) = −1, la seule torsion qui préserve la hauteur étant celle par −1. Donc κ ≤ P(d = −1). Par la formule du §2 de `piste1_equirepartition.md`, P(d = −1) = (1 + (3/5)·∏D)/2 = **0,55873**, et notre κ l'atteint à 10⁻⁵ près.
  - « Affiner les classes en 2 et 3 » ou « ajouter des premiers ≡ 3 (mod 4) » ne peut plus rien apporter.
  - L'hypothèse de `LISTE_GAINS.md` (+0,05 sur κ par affinage) était fausse ; je la corrige ici.
- **Au-delà**, il faudrait l'équirépartition des signes dans une famille large sans passer par d(E). BSZ la conjecturent (« µequi(F) = µ(F) ») et la jugent « difficult to prove ». C'est hors de portée sans idée nouvelle.

## Relecture adverse (pistes 6, 7, 4)

1. **I — Piste 6 : le critère « constant sur 3 relèvements » peut accepter une cellule non constante.** On a fait des contrôles croisés : stabilité entre k = 8 et k = 18, et accord au 5ᵉ chiffre avec `local_types_v3`. L'erreur est de l'ordre des violations de symétrie observées (moins de 10⁻⁵). **Réglée** au niveau de précision affiché.
2. **I — Piste 7 : BSTW imposent-ils une condition de type BSZ Th. 9 (c)** (E[5] ramifiée en ℓ ‖ N, ℓ ≡ ±1 mod 5) ailleurs que dans CH ? À vérifier dans BSTW lors de la vérification finale. **Ouverte.**
3. **M — Piste 4 : base et S1(5).** BSZ intersectent F′ avec S1(5) (conditions en ℓ ≡ ±1 mod 5) au prix de 10⁻⁵ ; c'est inchangé. **Réglée.**
4. **M — Piste 4 : κ de la base est-il le même pour S0 ∩ S1′ que pour toutes les courbes ?** Oui : les conditions ne portent qu'en 5, et β₅ = 1. **Réglée.**
