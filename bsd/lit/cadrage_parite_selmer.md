# Cadrage : à quoi ressemblent le problème de parité et le problème de Sel₇, et ce qui est en jeu

28 novembre 2026. Suite 2 du plan. **Il s'agit d'un cadrage, pas d'une tentative de preuve.**

**Sources lues.**
- Helfgott math/0408141 (§1, annexe C) ;
- Teräväinen 2010.07924 (§2.3) ;
- BSZ §3 ;
- résumés de 2212.10373 (Browning–Sofos–Teräväinen), 2506.18065, 2610.34912 et 1811.00966 (Landesman).

**Script.** `scripts/parite_explore.py`, résultats dans `results/parite_explore.txt`.

---

## Partie I. Le problème de parité pour les signes

### 1. Ce qu'on veut exactement
On veut la Conjecture E (`enonce_conditionnel.md`) : dans toute famille large, la moitié des courbes a pour signe +1. Il suffirait de montrer que

  Σ_{H(E_{A,B}) ≤ X, (A,B) ∈ F} r(E_{A,B}) = o(X^{5/6})

pour toute famille F définie par des congruences en un nombre fini de premiers.

### 2. À quoi ressemble r(E) : du Möbius tordu (DÉDUCTION, avec vérification numérique)
- On a r(E) = −∏_p w_p(E). Pour p ≥ 5 :
  - en bonne réduction, w_p = +1 ;
  - en réduction **multiplicative**, w_p = −(−c₆ / p) (symbole de Legendre), puisque la réduction est déployée ssi −c₆ est un carré mod p. **Vérifié sur 3 003 cas sur 3 003** (`parite_explore.py` (a)). Ici c₆ = −864B.
  - en réduction additive, w_p ne dépend que de données locales (au plus p² | Δ).
- **Dans le cas « générique »** (Δ′ = 4A³ + 27B² sans facteur carré, hors de 2 et 3), toutes les mauvaises réductions sont multiplicatives et

  r(E) = ± ∏_{p | Δ′} (−(864B / p)) = ± μ(Δ′) · (864B | Δ′)  (symbole de Jacobi),

  où ± est un facteur local en 2, 3 et ∞.
- Par réciprocité quadratique, (B | 4A³ + 27B²) = ±(4A³ + 27B² | B) = ±(4A³ | B) = ±(A | B), aux signes de réciprocité près, qui sont des conditions de congruence.
- **Donc r(E) ≈ μ(4A³ + 27B²) · (A | B) · (facteurs de congruence).** La somme à contrôler est, à des familles de congruence près,

  **S(X) = Σ_{|A| ≤ X^{1/3}, |B| ≤ X^{1/2}} μ(4A³ + 27B²) · (A | B).**

  Avec Helfgott : le signe est la fonction de Möbius (ou de Liouville) sur les valeurs d'un polynôme à deux variables, **tordue par un symbole de Jacobi**. Le cas non générique (Δ′ avec facteurs carrés) se traite par crible, et la partie « crible sans facteur carré » est connue ici grâce aux estimations d'uniformité de Bhargava.
- **Numériquement** (`parite_explore.py` (b), 40 000 tirages par boîte) : les moyennes de r(E) et de μ(4A³ + 27B²) valent 0,000 ± 0,005 pour |A| ≤ 10⁴, 10⁶ et 10⁸. La compensation est donc bien là ; c'est la **preuve** qui manque.

### 3. Pourquoi c'est difficile (le « mur de la parité »)
- **Barrière de la parité** (Selberg). Les méthodes de crible ne distinguent pas les entiers ayant un nombre pair ou impair de facteurs premiers. Montrer que μ ou λ compense sur une suite « mince » est exactement ce qu'elles ne savent pas faire.
- **Ce que l'on sait faire** (ÉTABLI, d'après les sources lues) :
  - les formes binaires **homogènes de degré 3** (Helfgott) ;
  - les polynômes qui **se factorisent en facteurs linéaires** (Green–Tao–Ziegler), ou certains facteurs quadratiques (Frantzikinakis–Host) ;
  - « presque tous » les polynômes d'un degré donné, ordonnés par hauteur (Browning–Sofos–Teräväinen 2212.10373 : « averaged versions of [...] the polynomial Chowla conjecture ») ;
  - des formes binaires aléatoires (2506.18065) ;
  - beaucoup de variables (2610.34912, « Birch rank sufficiently large ») ;
  - **seulement des changements de signe** pour am² + bn³ (Teräväinen, Th. 2.12 : « unable to say anything about this much stronger mean 0 property »).
- **Notre polynôme n'entre dans aucune de ces cases.** 4A³ + 27B² est en deux variables, non homogène (poids 2 et 3), irréductible et fixé.
  - Pour A fixé, c'est une **norme** : u² + 12A³ = N(u + 2A√(−3A)) avec u = 9B (aux constantes près). Mais c'est une norme depuis un corps quadratique ℚ(√−3A) **qui varie avec A**.
  - C'est la structure du problème « x² + y³ ». Le problème voisin sur les premiers (Friedlander–Iwaniec pour x² + y⁴, Heath-Brown pour x³ + 2y³) a été résolu grâce à une **forme norme fixe**, ce que nous n'avons pas. Cette comparaison est une SPÉCULATION de ma part, à faire confirmer.
- **Formulation « en moyenne ».** Pour A fixé, B ↦ 27B² + 4A³ est un polynôme quadratique en B. Chowla pour un quadratique fixé est **ouvert** (« remains wide open for any f irreducible of degree ≥ 2 », d'après la veille). La moyenne sur A n'est pas une moyenne « sur tous les polynômes » à la Browning–Sofos–Teräväinen : les décalages 4A³ sont des **cubes**, une famille mince, de densité X^{1/3} parmi X.

### 4. Ce qui est en jeu
- **Résultat complet** (κ = 1) : borne ≈ **83,3 %** avec nos résultats actuels, et ≈ 85,3 % si tout le reste aboutit (`HORIZONS_85.md`).
- **Résultat partiel utile.** Un biais démontré, même petit. Si l'on montrait que parmi les courbes avec d(E) = +1, la proportion de signes +1 est ≤ 1/2 + δ dans une famille de densité ρ, on gagnerait environ (1/2 − δ)·ρ·0,083 pt par point de pourcentage de densité.
- **Sous-problèmes possibles, du plus abordable au plus dur** (tous OUVERTS) :
  - (a) compensation de μ(27B² + 4A³)·(A | B) en moyenne sur A **et** sur une famille de congruence supplémentaire, ce qui ajoute de la moyenne ;
  - (b) une version **logarithmique** ou pondérée (à la Tao), probablement insuffisante pour les densités de BSZ ;
  - (c) le cas complet.
- **Avis honnête.** C'est un problème de premier plan en théorie analytique des nombres, comparable aux grands résultats « premiers dans des suites minces ». Une contribution réaliste dans ce projet serait : une formulation propre de la réduction (§2) pour les spécialistes, des expériences numériques fines, et la recherche d'un cas particulier abordable (sous-famille où la norme devient fixe ?). **Point d'attaque concret à explorer** : les sous-familles où A est de la forme −3a² (alors ℚ(√−3A) = ℚ(√(9a²)) devient fixe et la forme se factorise), ou plus généralement A dans une classe de carrés fixée. On retrouverait une forme norme **fixe**, où les méthodes Friedlander–Iwaniec ou Heath-Brown pourraient s'appliquer. Mais une telle sous-famille est **mince** (densité nulle), donc sans effet direct sur la borne. À explorer seulement comme banc d'essai. SPÉCULATION.

---

## Partie II. Le problème de Sel₇

### 5. À quoi il ressemble
- **Méthode de Bhargava** (ÉTABLI, BS et BSZ). Les éléments de Sel_n sont représentés par des orbites entières d'une représentation **coregulière** (anneau d'invariants libre, avec des invariants qui redonnent A et B) :
  - n = 2 : formes quartiques binaires ;
  - n = 3 : formes cubiques ternaires ;
  - n = 4 : paires de formes quadratiques quaternaires ;
  - n = 5 : quintuplets de formes alternées 5 × 5.
  
  On compte ces orbites par géométrie des nombres.
- **Pour n = 7**, les 7-revêtements sont des courbes de genre 1 de degré 7 dans P⁶. **Aucune représentation coregulière adaptée n'est connue.** C'est la raison pour laquelle la méthode s'arrête à n = 5 (DÉDUCTION, d'après la littérature lue : rien au-delà de 5 sur ℚ).
- **Sur les corps de fonctions** (ÉTABLI, Landesman 1811.00966) : « in the large q limit, the average size of n-Selmer groups [...] over F_q(t) is the sum of the divisors of n », d'où « 100% [...] have rank 0 or 1 ». La méthode est géométrique (monodromie, grand q) et **ne se transpose pas à ℚ**.

### 6. Ce qui est en jeu
- Moyenne de #Sel₇ égale à 8 : ≈ 87 % (89,8 % avec κ = 1).
- Une **majoration** suffirait : #Sel₇ ≤ c en moyenne, avec c ≲ 9,9, battrait déjà 79,8 %.
- Il faudrait aussi des réciproques en p = 7 (BSTW couvre p ≥ 5 supersingulier semistable et l'ordinaire ; même verrou « sans facteur carré » que pour p = 5).
- **Avis honnête.** Il faudrait une idée nouvelle de paramétrisation, ou une majoration par une autre voie. Je ne vois pas d'angle d'attaque réaliste ici.

---

## 7. Recommandation
1. **Priorité au programme réaliste.** Le test de multiplicité un (`programme_realiste.md` §4) donne des résultats encourageants pour E3.
2. **Problème de parité.** Rédiger la réduction du §2 proprement, avec les signes exacts en 2, 3 et ∞, pour la proposer comme question à des spécialistes de théorie analytique (Teräväinen, Helfgott, Browning). En parallèle, des expériences numériques sur la sous-famille « norme fixe » comme banc d'essai.
3. **Sel₇.** Pas d'action, hors de portée.
