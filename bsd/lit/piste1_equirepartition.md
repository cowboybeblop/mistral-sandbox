# Piste 1 : équirépartition des signes dans la famille supersingulière

27 novembre 2026. Suite de `LISTE_GAINS.md`, piste 1. **Aucune preuve n'est annoncée.** Le chiffre obtenu est conditionnel aux mêmes hypothèses que 78,61 % (A et B, Wan, N6), plus ce qui est listé au §6.

**Sources ouvertes.**
- BSZ, arXiv 1407.1826 v2 : §2.3, §2.4 (Th. 13, 15, 16), §3.1, Th. 21, 23, 25, Cor. 26, §4.
- Bhargava–Shankar (BS), arXiv 1312.7859 v1 (seule version sur arXiv ; version publiée **non vérifiée**) : §5, Prop. 35, tables 3 et 4 (**lues sur l'image des pages 25-26**), Lemme 36, Prop. 37, (32).

**Scripts.**
- `scripts/local_signs.py` : signes locaux par cellule.
- `scripts/feq_check.py`, `scripts/feq_identity.py` : vérification indépendante par l'équation fonctionnelle.
- `scripts/bound_v4.py` : chiffrage de la piste 1.
- `scripts/bound_v5.py` : chiffrage des pistes 1 et 2 ensemble.

Résultats dans `results/`.

## 1. Ce que dit la littérature (ÉTABLI, lu)

- **BSZ Th. 25** : « Let F ⊂ S0(5) ∩ S1(5) be any finite union of large families [...] at least 19/24 [...] If, furthermore, root numbers are equidistributed in F, then at least 7/8 ».
  - La preuve de la seconde partie utilise seulement le Th. 13 (moyenne de Sel₅ égale à 6), le Th. 15 (parité, Dokchitser) et les réciproques en rang de Selmer 0 et 1.
- **BSZ Cor. 26** : on prend F′ fermée par torsion par −1 avec r(E) r(E₋₁) = −1, d'où 7/8 sur κ·µ et 19/24 sur le reste.
  - BSZ y imposent la condition de **signe de Δ** (F^± de BS), donc des conditions à l'infini, déjà dans le cas publié.
- **BS §5** : d(E) := r(E) r(E₋₁) = ∏_p d_p(E).
  - **Lemme 36** : pour p > 3, d_p(E) = −1 ssi réduction multiplicative et p ≡ 3 (mod 4).
  - F1 et F2 (Prop. 35) sont définies par congruences en 2 et 3 ; F3 et F4 (Prop. 37) par des conditions en p > 3 ; F^± est donné par (32).
  - Densités annoncées : F1 > 59,179 %, F2 > 40,32 %, F3 > 96,689 %, F4 > 3,26 %, F⁻ 58,534 %, F⁺ 40,914 %, d'où κ > 0,5501.
- **BSZ Th. 16** ne vise que des familles définies modulo des puissances de p ≡ 1 (mod 4). Notre famille (conditions en 2, 3 et ℓ ≥ 7) n'y entre pas : il faut **refaire la construction de BS**, pas citer le Th. 16.

## 2. Reformulation locale (PROUVÉ, calcul élémentaire)

On pose Δ = −4A³ − 27B² (la constante 16 ne change rien) et χ₄(u) = ±1 selon que u ≡ ±1 (mod 4). Alors :

d(E) = β₂(E) · β₃(E) · sgn(Δ) · ∏_{p > 3, p ≡ 3 (4)} α_p(E),

avec β₂ = d₂ · χ₄(Δ′₂), β₃ = d₃ · (−1)^{v₃(Δ)} et α_p = d_p · (−1)^{v_p(Δ)} (BS (31)).

*Preuve.* On écrit Δ = sgn · 2^a 3^b ∏_{p>3} p^{v_p}. Alors χ₄(Δ′₂) = sgn · (−1)^b · ∏_{p ≡ 3 (4)} (−1)^{v_p}. On multiplie par d = d₂ d₃ ∏_{p>3} d_p, et on utilise d_p = 1 pour p ≡ 1 (4) (Lemme 36). ∎

**Conséquences.**
- Chaque facteur est une fonction **locale** de (A, B). Chaque facteur est invariant par (A, B) ↦ (A, −B), puisque Δ est inchangé et que d_p est symétrique.
- Pour une famille F = ∏ Σ_v fermée par torsion par −1, posons C_v = P(β_v défini) et D_v = P(β_v = +1) − P(β_v = −1), conditionnellement à Σ_v. On note µ_∞(Δ < 0) = 4/5 (calcul : {−u³ > w²} dans [−1, 1]² a une aire relative 1/5). Alors

  **κ = ∏C/2 + (3/10)·∏D**,

  où κ est la proportion de F où d = −1. C'est une DÉDUCTION : produit des densités locales, BSZ §3.1 et [2, Th. 3.17].
- **Contrôle** (`bound_v4.py`). Avec les tables de BS telles qu'imprimées, la formule redonne **exactement** leurs nombres : F1 = 0,59179, F2 = 0,40320, F3 = 0,96689, F4 = 0,03261, F⁻ = 0,58534, F⁺ = 0,40915, κ = 0,55011.

## 3. Signes locaux en 2 et 3 : désaccord avec les tables de BS

Énumération exacte des cellules (A, B) mod ℓ^k avec PARI `ellrootno`. On teste la constance sur 2 ou 3 relèvements aléatoires. Les k testés sont k = 5, 8, 9 en 2 et k = 3, 5, 6 en 3.

| | C | D | BS (tables imprimées) |
|---|---|---|---|
| ℓ = 2 (k = 9) | 0,99908 | 0,24733 | C = 0,99560, D = 0,25122 |
| ℓ = 3 (k = 6) | 0,99976 | **0,84716** | C = 0,99939, D = **0,75069** |

Stabilité : D₂ vaut 0,24728 (k = 8) et 0,24733 (k = 9) ; D₃ vaut 0,84716 en k = 5 et en k = 6.

**Lignes des tables de BS en désaccord** (tirages Monte-Carlo `bs_rows2.py`, `bs_rows3.py`, puis tests ciblés) :

| Table | Ligne (v(A), v(B), condition) | BS imprimé | Trouvé |
|---|---|---|---|
| 4 (ℓ = 3) | (1, 0, v₃(Δ) = 3) | (3, 1) : 5/6 ; (3, −1) : 1/6 | (3, 1) : 1/3 ; (3, −1) : 2/3 |
| 4 | (1, 0, v₃(Δ) = 5) | (3, ±1) : 1/2 chacun | (3, −1) : 1 |
| 4 | (2, ≥ 3) | (1, −1) : 1 | (1, 1) : 1 |
| 3 (ℓ = 2) | (1, 2) | (1, ±1) : 1/2 chacun | (3, ±1) : 1/2 chacun (Δ′₂ ≡ 3 : calcul à la main, Δ = −16(2a′³ + 27b′²) avec a′, b′ impairs) |
| 3 | (2, 4, v₂(Δ) = 13) | (1, 1), (3, −1) | (3, 1), (1, −1) |

**Vérification indépendante (PROUVÉ numériquement, deux méthodes).**
1. `feq_check.py`, 31 courbes dans ces lignes. Pour E et E₋₁, le signe global est déterminé par l'équation fonctionnelle de L(E, s) (`lfuncheckfeq`, ε = ±1 : le bon signe donne une erreur ≈ 2⁻⁷⁰, le mauvais ≈ 1). L'autre petit premier est fixé dans une classe où BS et PARI s'accordent ; les p > 3 sont traités par le Lemme 36 (type de Kodaira). On en déduit d₃ ou d₂ : **31 accords sur 31 avec PARI**, et des désaccords avec BS sur les lignes ci-dessus.
2. `feq_identity.py` : 200 courbes aléatoires (|A|, B ≤ 300). L'identité du §2, avec des signes globaux venant de l'équation fonctionnelle, est **vraie pour les 200**.
3. Théorie pour la ligne (2, ≥ 3). E est la tordue par χ_{±3} d'une courbe de bonne réduction en 3. Donc r₃(E) = χ(−1) = (−1, ±3)₃ = −1, de même pour E₋₁, d'où d₃ = +1 (et non −1).

**Portée (DÉDUCTION).**
- F1 et F2 sont définies par leur **propriété**, pas par les tables : la construction de BS reste valable. Seules les densités imprimées sont touchées.
- Avec nos signes en 2 et 3 et la Prop. 37 de BS en p > 3, on trouve **κ = 0,5579 > 0,5501**. Les erreurs sont donc **sans danger** pour BS (Th. 6) et pour BSZ (66,48 %), et la vraie constante est même un peu meilleure. C'est à présenter prudemment (« we believe »), comme des coquilles de table.
- **Bonus pour la piste 4.** κ = 0,5579 au lieu de 0,5501 dans la base donne **≈ +0,05 pt** sur toute la borne. Non intégré aux scénarios ci-dessous.

## 4. Notre famille supersingulière

- **Famille F_ss** :
  - 5 | A, 5 ∤ B ;
  - en 2 et 3, les cellules admises (prudent : sans E1-E3 ni indéterminées ; optimiste : toutes) ;
  - semistable en ℓ ≥ 7, sans multiplicatif avec 5 | v_ℓ(Δ).
- **Fermeture par −1.**
  - En 5 et ℓ ≥ 7 : automatique (type et v(Δ) inchangés, χ₋₁ non ramifié).
  - En 3 : stable (E3 est symétrique en ±a₃).
  - En 2 : **pas exactement**. Une courbe de bonne réduction avec a₂ = ±2 a une tordue par −1 de type E3. Les cellules non fermées font 0,07 % ; elles sont mises dans la partie 19/24.
- **F′** est formée des patrons (classe en 2, classe en 3, ensemble S de premiers p ≡ 3 (4), 7 ≤ p < 10⁴, |S| ≤ 2, où α_p = −1, signe de Δ) tels que d = −1. Au-delà de 10⁴, on impose α_p = +1.
  - C'est une **réunion finie de familles larges** : en ℓ ≥ 10⁴, Σ_ℓ contient tous les ℓ² ∤ Δ.
  - Elle est fermée par −1, et H(E₋₁) = H(E). Les signes y sont donc équirépartis exactement.
- **En ℓ ≥ 7** : C = 0,999994, D = 0,939967.

**Résultat** (`bound_v4.py`, k = 9 en 2, k = 6 en 3) :

| Scénario | κ_ss | Borne | Écart |
|---|---|---|---|
| S4 prudent (S3 prudent + équirépartition) | 0,5682 | **79,30 %** | +0,69 pt |
| S4 optimiste (S3 optimiste + équirépartition) | 0,5585 | **79,73 %** | +0,71 pt |

79,73 % retrouve la prévision de BSZ §4 (« 79.7% »).

## 5. Ce qui n'est pas de nous
- La méthode : BSZ (Th. 25, Cor. 26) et BS (§5 : d(E), F1-F4, Lemme 36).
- Les signes locaux : PARI (`ellrootno`, d'après Halberstadt et Rizzo).

Notre apport : la reformulation locale (§2), l'application à notre famille, et le constat sur les tables 3 et 4.

## 6. Relecture adverse

1. **C — Le 7/8 demande-t-il plus que le 19/24 ?** Non. Les deux parties du Th. 25 utilisent les mêmes réciproques (rang de Selmer 0 ou 1 ⇒ rang analytique égal). Le 7/8 ajoute seulement le Th. 15, qui vaut pour toute E/ℚ. **Réglée.**
2. **C — Les signes de PARI sont-ils justes là où BS diffèrent ?** Vérifiés par l'équation fonctionnelle (31 cas ciblés, 200 cas aléatoires) et par la théorie sur une ligne. **Réglée.**
3. **I — F′ est-elle admissible pour le Th. 13 avec une condition sur sgn Δ ?** BSZ le font eux-mêmes au Cor. 26 (F^± de BS). **Héritée, réglée.**
4. **I — Cellules mal déterminées.** On utilise des relèvements aléatoires. 2 cellules (k = 8) et 4 cellules (k = 6) violent β(A, B) = β(A, −B), ce qui est impossible en théorie : ce sont des cellules non constantes non détectées. Effet < 10⁻⁵ sur κ, stabilité en k vérifiée. **Réglée** (au niveau de précision affiché).
5. **I — Indépendance du signe à l'infini et des conditions locales.** Elle est confirmée par la reproduction exacte de κ = 0,5501 à partir des données de BS. **Réglée.**
6. **M — Écarts entre les μ₂, μ₃ de `bound_v3` (graine 2) et les fractions conditionnelles (graine 7, R = 3).** Écart de l'ordre de 10⁻⁴ sur μ, sans effet visible sur les deux décimales. **Réglée.**
7. **I — Version publiée de BS non vérifiée.** Les tables ont peut-être été corrigées. Cela ne change rien à **notre** calcul, qui n'utilise pas ces tables. **Ouverte** (à vérifier avant tout contact).
8. **M — Rang 1 (N6).** Inchangé : le chiffre reste conditionnel à N6, comme 78,61 %.

**Bilan.** Aucune objection critique propre à la piste 1.

## 7. Brouillon de message (non envoyé, à décider par l'utilisateur)

Facultatif et à faible enjeu : les coquilles ne changent pas les théorèmes. On pourrait le signaler à Shankar (auteur correspondant plus jeune ; adresse à vérifier dans un article récent), par exemple :

« We believe a few entries of Tables 3 and 4 of arXiv:1312.7859 may be misprinted (e.g. Table 4, row v₃(A) = 2, v₃(B) ≥ 3: we find d₃ = +1, since E is a ramified quadratic twist of a curve with good reduction at 3). Recomputing the tables, we get κ ≈ 0.558, so Theorem 6 is unaffected. We checked the local root numbers against the functional equation. This computation was done with the help of an AI system. »
