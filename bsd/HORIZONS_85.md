# Horizons au-delà de 80 % : peut-on viser 85 % ? (28 novembre 2026)

Exécution de `PLAN_85.md`, étapes E0 à E6.

**Scripts.**
- `scripts/plafonds.py` → `results/plafonds.txt`
- `scripts/moments_lp.py` → `results/moments_lp.txt`
- calcul conditionnel → `results/borne_conditionnelle_parite.txt`

**Sources ouvertes.**
- BSZ (1407.1826) ; BS (1312.7859) §5 ;
- Helfgott, arXiv math/0408141 v3 : résumé, §1, **annexe C** ;
- Sawin–Sutherland, arXiv 2504.12295 v2 : résumé, §1 ;
- Teräväinen, arXiv 2010.07924 : §2.3, Th. 2.12 et remarques ;
- Bhargava–Shankar–Swaminathan, arXiv 2110.09063 : connu par le résumé seulement, **non ouvert** en détail.

## 1. Verdict

**85 % n'est pas accessible avec les outils connus.** Il faut un théorème nouveau en théorie analytique des nombres : l'équirépartition des signes (problème de parité), ou la moyenne de Sel₇.

| Hypothèse | Borne | Statut |
|---|---|---|
| Aujourd'hui | 79,81 % | conditionnel (A, B, N6, BSTW, CLW) |
| Toutes nos pistes p = 5 abouties (N6, E2/E3...), κ = 0,5587 | 80,5 % | recherche en cours |
| + p = 3 sur les courbes additives en 5 | 81,7 % | gros chantier (piste 5) |
| **Signes équirépartis dans toute famille large** (conjecture « µ_equi = µ » de BSZ), avec nos résultats actuels | **83,3 %** (prudent) / 83,8 % | conjecture ouverte |
| idem + p = 5 parfait + p = 3 | 85,3 % | conjecture + chantiers |
| Moyenne de #Sel₇ égale à 8 (Poonen–Rains), κ actuel / κ = 1 | 87,1 % / 89,8 % | ouvert, aucune approche connue |

85 % demande **κ ≥ 0,96**, contre 0,5587 aujourd'hui, **plus** tout le reste. C'est pratiquement la conjecture d'équirépartition.

## 2. Ce que la veille a établi (E1, E2)

- **Signes (ÉTABLI, lu).** Helfgott, annexe C : pour la famille (a, b) ↦ y² = x³ + ax + b, « the problem of averaging the root number over that family E seems to necessitate solving an open case of the parity problem; [...] we would in all likelihood need to show that λ(a² − b³) averages to zero [...] and thus remains open ».
  - Chez nous, le même problème porte sur λ(4A³ + 27B²), car c₄³ − c₆² = −27648·(4A³ + 27B²) avec c₄ = −48A et c₆ = −864B.
  - Teräväinen 2020, Th. 2.12 (ii) : λ(am² + bn^k) prend chaque signe une infinité de fois, ce qui couvre 27B² + 4A³. Mais « our methods are elementary and unable to say anything about this much stronger mean 0 property ».
  - Sawin–Sutherland 2025 : leur théorème inconditionnel porte sur ε(E)·a_n avec n de l'ordre de N(E), pas sur la moyenne de ε. Ils rappellent : « Showing cancellation in the sum of ε(E) [...] is equivalent to showing that the root number equidistributes [...] studied by Helfgott [...] proving conditional positive results ».
  - Aucun progrès inconditionnel trouvé pour 2023-2026.
- **Selmer.**
  - Second moment de #Sel₂ ≤ 15 (BSS, arXiv 2110.09063, d'après le résumé).
  - Rien pour Sel₆, Sel₇, ni pour les seconds moments de Sel₃ ou Sel₅.
  - Rien sur les lois jointes de Sel₃ et Sel₅.

## 3. Ce que les calculs ont établi (E3 à E5)

1. **Les moments supérieurs ne servent à rien** (E4, `moments_lp.py`, programme linéaire).
   - Avec des majorations E[#Sel_p^j] ≤ ∏_{i≤j}(p^i + 1) (valeurs de Poonen–Rains) jusqu'à j = 4, la borne reste **exactement** 19/24 (ou 7/8 avec équirépartition) pour p = 5, et de même pour p = 2, 3 et 7.
   - Raison : la loi extrémale (rangs de Selmer 0 et 2 seulement : 19/24 et 5/24) respecte tous ces moments. Par exemple, son second moment vaut 131 ≤ 156.
   - Même des **égalités** exactes ne donnent presque rien : +0,00003 pour le second moment de Sel₅, +0,002 avec le troisième sans équirépartition (au mieux +0,017 avec équirépartition).
   - Le second moment de Sel₂ (BSS) n'apporte rien non plus (p = 2 : 1/3 → 0,339).
2. **La parité est le vrai levier** (E0). La borne pour p = 5 vaut 19/24 si la proportion de signes +1 est inconnue, 7/8 si elle vaut 1/2, et **99,2 %** si tous les signes valent −1. Toute **majoration** de la proportion de signes +1 dans une famille large améliore directement le résultat.
3. **Familles biaisées construites par conditions locales : impossible par la méthode de BS** (E3, DÉDUCTION).
   - La torsion par d multiplie la hauteur par d⁶. La seule involution de la boîte de hauteur qui préserve la hauteur est (A, B) ↦ (A, −B).
   - Les conditions locales ne déterminent que d(E) = r(E)·r(E₋₁), jamais r(E) lui-même. Celui-ci dépend du produit de facteurs locaux en une infinité de premiers, d'où le problème de parité (Helfgott).
   - Le couplage « même parité pour Sel₃ et Sel₅ » (Dokchitser) ne suffit pas non plus : on peut placer les échecs de p = 3 et de p = 5 sur les mêmes courbes de parité paire. Il faut de vraies lois jointes.
4. **Sel₇** (E5). La moyenne de #Sel₇ est inconnue, et aucune majoration n'a été trouvée.
   - Pour battre 79,81 % avec p = 7 seul (signes inconnus, 98 % des courbes en bonne ou mauvaise réduction multiplicative en 7), il faudrait une majoration de la moyenne de **#Sel₇ ≤ 9,9** environ : 0,98·(49 − c)/48 > 0,798.
   - Aucune paramétrisation de type Bhargava n'est connue pour n = 7. C'est hors de portée.

## 4. Le « prochain résultat » qui débloquerait 83-85 %

**Problème cible (OUVERT).** Montrer que les signes r(E) sont équirépartis dans les familles larges de courbes ordonnées par hauteur, éventuellement en moyenne sur des progressions (conditions de congruence en un nombre fini de premiers).
- Helfgott le relie à la nullité en moyenne de λ(4A³ + 27B²) dans la boîte |A| ≤ X^{1/3}, |B| ≤ X^{1/2}, un cas ouvert du problème de parité. C'est une condition **probablement nécessaire**, selon Helfgott ; sa suffisance n'est pas démontrée ici. Il faut aussi tenir compte du caractère déployé ou non déployé aux premiers multiplicatifs.
- Les résultats connus voisins sont :
  - les formes cubiques binaires **homogènes** (Helfgott) ;
  - les polynômes qui se factorisent (Green–Tao–Ziegler, Frantzikinakis–Host) ;
  - les changements de signe seulement pour am² + bn³ (Teräväinen).
- Même une version **partielle** servirait. Par exemple, montrer que parmi les courbes avec d(E) = +1, la proportion de signes +1 est ≤ 1/2 + δ. Chaque point de κ entre 0,56 et 0,96 rapporte ≈ 0,083 pt de borne par 0,01 de κ.

## 5. Recommandation

1. **Programme réaliste (projet actuel).** Faire valider A et B (Wan), puis régler N6, E2/E3 et le Steinberg tordu (spécialistes) : environ **80,5 %**. Puis p = 3 sur les courbes additives en 5, en gros chantier : environ **81,7 %**.
2. **Énoncé conditionnel publiable** (DÉDUCTION). « Si les signes sont équirépartis dans toute famille large (conjecture de BSZ), alors au moins ≈ 83,3 % des courbes vérifient la conjecture de BSD (partie rang) », aux mêmes conditions que 79,81 %. C'est une remarque à ajouter à la note pour spécialistes.
3. **85 % et plus** demande un progrès sur le problème de parité pour λ(4A³ + 27B²), ou une moyenne de Sel₇. Ce sont des problèmes de premier plan : on les signale, on ne les attaque pas ici.

## 6. Relecture adverse de cette synthèse

1. **I — « La loi extrémale respecte tous les moments de Poonen–Rains. »** C'est vérifié numériquement jusqu'à j = 4. Pour tout j : 19/24 + (5/24)·p^{2j} ≤ ∏_{i≤j}(p^i + 1), puisque p^{2j} ≤ p^{j(j+1)/2}·(…) pour j ≥ 3, et c'est vérifié à la main pour j = 1, 2. **Réglée.**
2. **I — La borne conditionnelle de 83,3 % suppose κ = 1 dans la base et dans la famille supersingulière avec leurs conditions locales.** C'est la forme de la conjecture de BSZ (« for any large family F »). **Assumé, étiqueté CONJECTURE.**
3. **M — Le lien λ(a² − b³) ↔ λ(4A³ + 27B²).** Il passe par c₄, c₆, un sous-réseau ; c'est le même problème à changement de variables près. Formulé comme « même problème », sans affirmer d'équivalence exacte. **Réglée.**
4. **M — Le résultat de BSS n'a été vu que dans le résumé.** Il n'est utilisé que pour dire « n'aide pas », ce que le programme linéaire montre de toute façon. **Assumé.**
5. **I — Ai-je raté un levier ?** Les autres pistes envisagées et écartées :
   - d'autres ordres de comptage : la question porte sur l'ordre par hauteur ;
   - des familles minces avec point marqué : densité nulle ;
   - des moyennes sur des corps de nombres : hors sujet.
   
   **Pas d'autre levier identifié.**
