# Relecture adverse de la stratégie A + B + raccord + chiffrage

26 novembre 2026. Rédigée « comme un rapporteur hostile ». Chaque objection a un numéro, une gravité et une piste pour la régler. Gravité : **C** = critique (peut tout faire tomber), **I** = importante (une étape à refaire ou à étayer), **M** = mineure (rédaction, chiffres).

## I. Cadre global (BSZ et BSTW)

1. **C — La famille est-elle « admissible » pour la méthode de BSZ ?** Notre famille impose des conditions en 2 et 3 (types non semistables) et la semistabilité en tout ℓ ≥ 7, ce qui fait une infinité de conditions de congruence. La méthode de BSZ (comptage de Bhargava–Shankar, Th. 16 et Th. 25) exige des familles « larges » avec des estimations d'uniformité. Le facteur 19/24, la constante κ et P₇ sont repris de l'analyse d'origine sans relecture de BSZ. *À régler : relire BSZ §3 (Th. 16, 21, 25, Cor. 26) et vérifier que la famille « supersingulière en 5 + type quelconque en 2 et 3 + semistable ailleurs » est couverte, avec le bon facteur.*
2. **C — Le point de départ est lui-même conditionnel.** 67,02 % et la base de 66,99 % reposent sur BSTW et Castella (réciproques ordinaires et multiplicatifs), marqués « conditionnels » dans le rapport d'origine. *À régler : relire `amelioration_BSZ.md` et lister ces conditions.*
3. **I — Existence du premier q (ram) pour des courbes non semistables.** Le Lemme 20 de BSZ est invoqué pour « 100 % des courbes », mais il n'a pas été relu, et sa preuve suppose peut-être une famille différente. Les conducteurs de la forme 2^a·3^b n'ont **aucun** premier multiplicatif : ils sont exclus d'office, ce qu'il faut chiffrer. *À régler : relire le Lemme 20 et calculer la densité des courbes sans premier multiplicatif (E[5] ramifiée) dans notre famille.*
4. **I — Les autres usages de « N sans facteur carré » chez BSTW.** On a conclu que seul le Th. 10.5 l'utilise, mais sans relire en entier les §9 à 12 ni les résultats intermédiaires (Prop. 9.18, Th. 9.21, Prop. 10.7 dans le cas ±, Th. 6.16 et 6.17 pour la tordue). *À régler : relire chaque énoncé de la chaîne Th. 1.6 / 12.3 → 10.1 → 10.5 et vérifier qu'aucun n'hérite d'une hypothèse cachée.*

## II. Problème A

5. **C — Les vecteurs choisis aux places décomposées sont-ils permis par la construction ?** CLW fixent ϕ dans l'espace (5.6.12), engendré par f^{GU(2)}_{χ_h} (le vecteur nouveau tordu par (5.6.10)) et par l'action de GU(ℚ_v) **aux seules places non décomposées**. Aux places décomposées, ϕ_v n'est donc **pas libre**. La lecture (L2) choisit un autre ϕ_v (une seule couche du modèle de Kirillov), et la lecture (L1) prend le vecteur nouveau sans torsion. Il faut montrer qu'on peut modifier la construction de CLW en v sans casser : (a) le calcul de Fourier–Jacobi (Wan, Lemme 6.20, « any ϕ invariant under Y », ce qui semble suffire) ; (b) le niveau K_v ; (c) l'indépendance en τ ; (d) les autres places, où ϕ_v intervient dans les sections de Siegel (§5.7.3). *À régler : réécrire le §5.6 de CLW avec ϕ_v libre en Σ_s et suivre chaque usage.*
6. **C — L'ambiguïté (L1)/(L2) n'est pas tranchée.** L'argument de cohérence en faveur de (L2) suppose que les résultats publiés de CLW et Wan sont justes, alors qu'on vient de trouver une erreur dans Wan (Lemme 8.14). *À régler : déterminer l'orientation par le calcul de la correspondance thêta locale (conventions (7.1.1) et (7.1.6) de CLW, modèles V et V⁻), ou par la réponse de Wan.*
7. **I — (L1) : compatibilité de FW avec CLW.** Si « conductors ℓ^{t₁} » s'applique aux **quatre** caractères (lecture littérale de FW Cor. 7.28), alors « χ_{θ,𝔳} non ramifié », imposé par CLW, est **incompatible**. Seule la lecture cond(χ₁χ₂^{-1}) = t₁ (question 2 à Wan) sauve (L1). *À régler : question 2, ou refaire FW Cor. 7.28 avec χ_{θ,1} non ramifié.*
8. **I — (L2) : la preuve est esquissée, pas écrite.** Points à justifier : l'identification de f_h avec un translaté par diag(ϖ^a, 1) du vecteur nouveau d'une tordue (relation d'Atkin–Lehner) ; la forme Rankin–Selberg Ψ (convergence, égalité avec ℓ à une constante non nulle près) ; l'existence et l'invariance par n⁻(ϖ^aO) du vecteur φ₀ porté par une seule couche. *À régler : rédiger complètement, puis vérifier numériquement (modèle de Kirillov d'une supercuspidale de niveau zéro en p = 3).*
9. **I — Vérifications numériques trop étroites.** Le Lemme 8.13 n'a été testé que pour p = 3, t = 2, un seul couple de caractères ; le Lemme 8.14 seulement pour p = 3, (t₁, s) = (1, 2) ; le critère isotypique seulement pour p = 3. Nos places sont ℓ = 2 et 3, avec de grands conducteurs. *À régler : étendre les tests à p = 2 et à des conducteurs plus grands.*
10. **I — La formule de Hu en p = 2.** La preuve de FW Prop. 7.27 utilise la formule (2.66) de Hu pour l'action de ω dans le modèle de Kirillov, reprise de « [14] » (non ouvert), et la normalisation n₁ = −c. Il faut vérifier qu'elle vaut pour p = 2 sans restriction. *À régler : ouvrir la référence [14] de Hu, ou démontrer (2.66) pour le vecteur nouveau.*
11. **M — Supercuspidales non minimales en 2.** La relation c(π ⊗ μ) = 2·cond(μ) (Hsieh, Lemme 6.8) est énoncée pour π minimale. Pour π = π₀ ⊗ χ₀, elle reste vraie si cond(μ) > cond(χ₀), ce qui est le cas ici puisque s est grand. *À écrire.*
12. **I — Familles non unitaires et formule d'Ichino.** La formule d'Ichino suppose des représentations unitaires. Dans les familles p-adiques, les tordues non ramifiées spécialisées peuvent ne pas l'être. CLW traitent la question par interpolation. Il faut vérifier que notre argument « non nul pour **toute** tordue non ramifiée » est bien ce qu'utilise leur Prop. 7.11.3, aux points arithmétiques.
13. **C — La portée du contre-exemple au Lemme 8.14.** Si (L1) est la bonne lecture, le cas semistable publié (BSTW Th. 1.6 et 12.3, via CLW) pourrait être atteint aux places Steinberg décomposées. Toute l'amélioration hérite de la validité de CLW. *À régler : c'est la question 3 à Wan, prioritaire.*

## III. Problème B

14. **I — Darmon–Iovita et l'identification avec L°_W de BSTW.** Darmon–Iovita n'a été lu que par un agent. BSTW définissent L°_W « based on the Waldspurger formula on the definite quaternion algebra (see also [137]) ». Il faut vérifier que c'est bien la fonction L± de Darmon–Iovita et Pollack–Weston, avec la même normalisation (période de Gross, vecteur primitif) et un vecteur-test **aux places ℓ² | N⁺** compatible avec le Th. 3.11 de CH, où aucun facteur local n'apparaît. *À régler : lire Darmon–Iovita (préprint McGill) et CH Prop. 3.8 et 3.10 pour ℓ² | N⁺ décomposé.*
15. **I — Étape 4 : combinaison inédite.** Taylor §2 est écrit sur un corps totalement réel de **degré pair**, avec D non ramifiée aux places finies et ρ̄ non ramifiée hors de l. CH l'adaptent à ℚ, avec ramification et condition **ordinaire**. Notre version combine l'adaptation de CH et la condition cristalline de Taylor : cette combinaison n'est écrite nulle part, seule la remarque de Kim–Ota l'affirme. Points à vérifier : les premiers de Taylor–Wiles sur ℚ (ℓ ≡ 1 mod 5^m, Frobenius à valeurs propres distinctes), le décompte de Wiles avec Fontaine–Laffaille en p = 5, la surjection R → T. *À régler : rédiger la preuve de la Prop. 6.8 de CH en version cristalline, ligne à ligne.*
16. **I — Références non ouvertes.** Carayol (conducteur et type inertiel), Darmon–Diamond–Taylor (déformations minimales), Diamond 1997a et 1997b, Vatsal 2003. *À régler : se les procurer et vérifier les énoncés cités.*
17. **M — μ = 0 « pour n ≫ 0 » et passage à L±.** μ(θ_n) = 0 pour n grand d'une parité donnée, avec la divisibilité par ω_n^±, d'après PW. Il faut vérifier que la parité de n et le signe ± se correspondent bien pour les deux signes.
18. **M — Les deux signes ±.** BSTW ont besoin des deux. L'argument est symétrique, mais c'est à dire explicitement.

## IV. Raccord

19. **I — La tordue g′ = g ⊗ χ_L.** Aux ℓ | D_L, g′ est une série principale ramifiée, ce qui renvoie à l'objection 13 et au point 2 du §3 du raccord. BSTW en dépendent aussi, mais si leur traitement est fautif, notre rang 1 l'est aussi. *À régler : comme 13.*
20. **M — Existence de L″.** Conditions locales à imposer simultanément en 5, 2, 3, q, aux autres premiers de N et aux premiers de D_L, plus la non-annulation L(1, g′) ≠ 0 pour L (Friedberg–Hoffstein [51]). Le résultat [51] porte sur le corps de Heegner L, pas sur L″. Il faut vérifier que [51] vaut en niveau non sans facteur carré.

## V. Chiffrage

21. **I — Classification des types locaux.** Il y a de l'échantillonnage (R = 2 relèvements aléatoires par cellule), une troncature (mod 2⁸ et 3⁵), et le critère « ps_sup » est déduit (abélianité de l'inertie détectée par deux ou trois corps tests). *À régler : valider sur des courbes de conducteur connu (LMFDB, types locaux répertoriés) et augmenter k.*
22. **M — ε approché.** La formule (q − 1)²/q^{m+2} pour la densité « multiplicative avec v_q(Δ) = m » n'a pas été vérifiée dans la normalisation de BSZ. L'effet est négligeable (10⁻⁴), mais c'est à écrire proprement.
23. **M — Les cellules indéterminées** (0,02 %) sont exclues : c'est prudent, mais à signaler.

## VI. Méthode

24. **I — Biais de confirmation.** Les vérifications ont été faites par la même personne qui a conçu les arguments, et certaines sources n'ont été lues que par des agents. *À régler : relecture indépendante (spécialistes), et reproduction des calculs par un autre code (Sage ou Magma).*
25. **M — Traçabilité.** Les étiquettes ÉTABLI, DÉDUCTION et NON VÉRIFIÉ doivent être homogènes entre `probleme_A_note.md`, `probleme_B_redaction.md` et `raccord_A_B.md`. *À régler : un document final unique.*

## Ordre de traitement proposé

1. **Objection 1** (admissibilité de la famille pour BSZ, facteur 19/24) : critique, réglable par simple lecture de BSZ.
2. **Objections 5 et 6** (liberté de ϕ_v aux places décomposées, orientation) : critiques pour A, travail de lecture et de calcul sur CLW.
3. **Objection 3** (Lemme 20 et courbes sans premier multiplicatif) : chiffrable.
4. **Objections 13 et 19** (Lemme 8.14, séries principales) : dépendent de Wan.
5. **Objections 14 et 15** (B, étapes 1 et 4) : rédaction ligne à ligne.
6. **Le reste** (vérifications numériques élargies, références, chiffrage).

---

## Traitement des objections 1 et 2 (26 novembre)

### Objection 1 : admissibilité de la famille pour BSZ, facteur 19/24. **RÉGLÉE (lecture de BSZ, arXiv 1407.1826, §2.3–3.5)**

- **« Large family » (ÉTABLI, BSZ §2.3).** C'est F_Σ avec Σ_ℓ fermé à bord de mesure nulle, tel que « for all sufficiently large primes ℓ, Σ_ℓ contains all E_{A,B} with ℓ² ∤ Δ(A, B) ». BSZ : « The family of all semistable elliptic curves is also large ».
  Notre famille est F = {5 | A, 5 ∤ B} ∩ {types admis en 2 et 3} ∩ {semistable en ℓ ≥ 7}, privée des multiplicatives en q ≥ 7 avec 5 | v_q(Δ). Les ensembles imposés en 2, 3 et 5 sont définis par des congruences sur des cellules mod ℓ^k, donc fermés à bord de mesure nulle. En ℓ ≥ 7, Σ_ℓ contient tous les (A, B) avec ℓ² ∤ Δ : les exclus ont v_ℓ(Δ) ≥ 5. **F est une large family (DÉDUCTION immédiate).** La densité est le produit des densités locales (BSZ §3.1, d'après [2, Thm 3.17]). C'est la formule de `bound_v2.py`.
- **Théorème 13 (ÉTABLI).** « When elliptic curves over Q in any large family are ordered by height, the average size of the p-Selmer group is p + 1 » (p ≤ 5).
- **Facteur 19/24 (ÉTABLI, BSZ Th. 25, première partie, preuve lue).** L'inégalité x_{0ou1} + p²(1 − x_{0ou1}) ≤ p + 1 donne x_{0ou1} ≥ 19/24 pour la proportion de **5-rang de Selmer** 0 ou 1. C'est du **pur comptage**, valable dans toute famille large sans équirépartition. BSZ appliquent ensuite leur Th. 9 (cas ordinaire et multiplicatif). Chez nous, on le remplace par :
  - **Rang de Selmer 0** (avec E(ℚ)[5] = 0, assuré par E[5] irréductible) : corang Sel_{5^∞} = 0. Les réciproques supersinguliers en rang 0 (BSTW Th. 1.6, étendu par A + B) donnent alors L(E, 1) ≠ 0, et Kolyvagin donne le rang 0.
  - **Rang de Selmer 1** : Sel_{5^∞}[5] = Sel_5 est de dimension 1, donc le corang r ≤ 1. La parité (Dokchitser–Dokchitser, BSZ Th. 15, et p-parité pour p^∞) donne r impair, donc r = 1, et la partie divisible de Ш[5^∞] est nulle, donc Ш[5^∞] est fini. BSTW Th. 12.3 (étendu) donne ord L = 1, puis Gross–Zagier–Kolyvagin donne le rang 1. C'est la déduction 5 de `amelioration_BSZ.md`, utilisée aussi par BSZ (Th. 9) et Castella.
  
  **Le facteur 19/24 s'applique donc (DÉDUCTION, structure identique à BSZ).**
- **Pas de 7/8.** Le Th. 16 (équirépartition des signes) demande des conditions modulo des puissances de premiers p ≡ 1 mod 4. Les conditions en 2, 3 et ℓ ≥ 7 l'excluent. On reste à 19/24, comme dans `gain_table.py` (ÉTABLI, BSZ Th. 16).
- **Lemme 20 (ÉTABLI, preuve lue).** Pour 100 % des courbes, E[p] est irréductible **et** « there exist at least two prime factors ℓ ‖ N(E), ℓ ≠ p, such that E[p] is ramified at ℓ ». Un ensemble de densité nulle l'est aussi dans F. **Cela règle aussi l'objection 3** : le premier q multiplicatif (ram) existe pour 100 % de F, et les conducteurs 2^a·3^b forment un ensemble de densité nulle. On en a même deux, ce qui laisse de la marge pour le choix de L″.
- **Reste (M).** La borne additionne la famille supersingulière (19/24) et la base de BSZ (familles en 5 disjointes : S₀(5) est {5 ∤ A}, la nôtre {5 | A, 5 ∤ B}). Les deux sont disjointes ✓, comme dans `bsz_bound.py`.

### Objection 2 : le point de départ est conditionnel. **CLARIFIÉE**

D'après `amelioration_BSZ.md` (branche d'origine), la base de 66,99 % repose sur :

| Brique | Statut |
|---|---|
| BSTW Th. 12.3, cas bon ordinaire en 5, **sans condition sur le conducteur** (« Either a_p(g) = 0 and N is square-free or λ ∤ a_p(g) ») | énoncé relu ici ✓. **Prépublication** (arXiv 2409.01350 v2, 11/09/2024), aucune référence de journal trouvée (recherche web du 26/11/2026). Le cas ordinaire passe par le Th. 9.21(c) (Skinner–Urban, Wan [140]), qui demande p ∤ 6N, vrai pour p = 5 |
| Castella Th. 1.1 (multiplicatif en 5 ; hypothèse (ii) : un premier q de réduction multiplicative **non déployée** avec E[5] ramifiée) | **Prépublication** (arXiv 2409.01360), aucune référence de journal trouvée. L'hypothèse (ii) est de densité 100 % par un argument de type Lemme 20, à vérifier |
| Déduction « E(ℚ₅)[5] = 0 sur S₁new » | DÉDUCTION vérifiée numériquement (600 courbes) |
| Déduction « S₅ ≅ ℤ/5 ⇒ corang 1, Ш[5^∞] = 0 » | standard (BSZ Th. 9, Cassels–Tate) |

**Conséquence.** Notre amélioration hérite de **deux couches de conditionnalité**. Il y a d'abord celle de la base (BSTW et Castella, prépublications non publiées). Il y a ensuite celle de A + B (nos adaptations). Le gain propre de A + B (≈ +10,7 points en S_A) ne dépend que de BSTW, déjà nécessaire pour la base, et de A + B. Il ne dépend **pas** de Castella : la famille supersingulière n'utilise que BSTW.

**Ce qu'il faudrait pour lever l'objection 2.** Attendre la publication de BSTW et de Castella, ou vérifier leurs preuves. C'est hors de notre portée et hors de notre contribution : on le signale comme hypothèse dans la formulation finale (« sous réserve de BSTW et Castella »).

### Objection 5 : liberté de ϕ_v aux places décomposées. **RÉGLÉE (DÉDUCTION, chaque usage de ϕ relu dans CLW)**

CLW fixent ϕ dans (5.6.12) = M_{GU(2)}(K_f^p GU(2)(ℤ_p); O_L) ∩ L[GU(2)(ℚ_{Σ_ns∪{ℓ′}})]·f^{GU(2)}_{χ_h}. On propose de **l'élargir** en
(5.6.12′) M_{GU(2)}(K′_f^p GU(2)(ℤ_p); O_L) ∩ L[GU(2)(ℚ_{Σ∪{ℓ,ℓ′}})]·f^{GU(2)},
c'est-à-dire d'autoriser l'algèbre de groupe aussi aux places décomposées, avec un niveau K′_v plus profond (c_v plus grand). Comme π_v est irréductible, tout ϕ_v ∈ π_v s'écrit Σ c_i π_v(g_i)f_v. Le vecteur φ₀ de la lecture (L2), comme le vecteur nouveau de la lecture (L1), est donc atteint.

Relevé **exhaustif** des usages de ϕ dans CLW (recherche du symbole ϕ dans tout le texte, 29 blocs, relus) :

| Usage | Où | Contrainte sur ϕ_v en v ∈ Σ_s | Avec (5.6.12′) |
|---|---|---|---|
| Famille de Klingen E^Kling_ϕ = ⟨E^Sieg⋆, ϕ⟩ | §5.10, (5.10.2)–(5.10.3) | ϕ fixe le long de la famille et sphérique en p | ✓ (ϕ_v fixé, indépendant de τ) |
| Semi-ordinarité | Prop. 5.10.1, p. 46 | « Here we use the condition that ϕ has **trivial central character** » | ✓ : tout vecteur de π (ω_π = 1) |
| Terme constant | Th. 6.1.1, (6.1.5) | Pour v ∈ Σ : Z_v = vol(Y_{c_v})·(…)·⟨ϕ_v, ϕ′_v⟩ « by [Wan20, Lemma 6.20] **for ϕ in the space (5.6.12)** ». Le lemme vaut pour tout ϕ_v invariant par Y_{c_v} ⊂ {k ≡ 1 mod q_v^{c_v}} | ✓ si c_v ≥ niveau de ϕ_v. (5.6.6) ne donne qu'une **borne inférieure** sur c_v, et K_v (5.6.7) suit c_v |
| Lien avec θ (7.5.8) | §7.5 | « our ϕ is assumed to have the trivial central character » | ✓ |
| Coefficient de Fourier–Jacobi et intégrale triple | Prop. 7.11.1–7.11.3 | ϕ et ϕ′ dans (5.6.12), des tenseurs purs ; intégrale locale en v | ✓ : c'est exactement le problème A, résolu en (L1) ou (L2) |
| Torsion (5.6.10) | p. 36, Rem. 5.6.2 | « to make the nebentypus match those of the auxiliary CM families θ and h » | remplacée par le choix isotypique de ϕ_v (type assorti à θ ⊗ h), qui joue le même rôle |

- **Fourier–Jacobi.** Le calcul (Wan, Lemmes 6.20–6.24, CLW §7.6) ne dépend que des sections de Siegel et des fonctions de Schwartz, pas du type de π_v. C'était déjà acquis au §5, point 2.
- **Effet de c_v plus grand.** c_v intervient dans la section de Siegel (5.7.1), dans Y_{c_v} et dans K_v. Le Lemme 6.24 de Wan demande cond(λ) < cond(χ_θ) < ord(yȳ) : augmenter c_v (et y) conserve ces inégalités. **Aucune borne supérieure sur c_v n'a été trouvée.**
- **Intégralité.** (5.6.12′) est intersecté avec les formes à valeurs dans O_L, comme (5.6.12). On multiplie par une constante si nécessaire.
- **Statut.** DÉDUCTION, avec relevé exhaustif. **Reste à faire relire :** que l'élargissement de l'algèbre de groupe aux places décomposées ne touche aucun argument de CLW §8 (preuve du théorème principal, réseaux, idéal d'Eisenstein). Je n'ai pas relu le §8 en détail, mais ϕ n'y figure plus (aucune occurrence après la ligne 5937 du texte extrait, qui correspond à la fin du §7).

### Objection 2 (fin) : conditions de la base

- **Castella Th. 1.1 (lu, arXiv 2409.01360 v1).** Hypothèses : (i) E[p] irréductible ; (ii) « E has nonsplit multiplicative reduction at some prime q ≠ p where E[p] is ramified » ; (iii) E(ℚ_p)[p] = 0. Pour (ii), on reprend la preuve du Lemme 20 de BSZ en ne gardant que les premiers **non déployés**. La densité locale de {v_q(Δ) = 1, non déployée} est d'ordre 1/(2q), et la somme diverge. La proportion de courbes sans tel q tend donc vers 0, et **(ii) vaut pour 100 %** (DÉDUCTION, même crible que BSZ). Castella n'intervient que dans la base, pas dans notre gain.
- **BSTW Th. 12.3, cas ordinaire.** Il passe par le Th. 9.21(c) : Skinner–Urban [131] (intégral, sous (ram)) et **Wan [140]** (*The Iwasawa main conjecture for Hilbert modular forms*, Forum Math. Sigma 2015) pour l'égalité dans Λ ⊗ ℚ_p. L'énoncé du Th. 9.21(c) demande seulement « p ∤ 6N ordinary such that (irr_ℚ) holds », **sans condition sur N** (ÉTABLI, énoncé lu). Les hypothèses de [140] n'ont pas été relues (NON VÉRIFIÉ).
- **Bilan.** La base est conditionnelle à **BSTW et Castella**, deux prépublications sans référence de journal au 26/11/2026, et à Wan [140], publié mais non relu. Notre gain n'ajoute que A + B. Formulation finale proposée : « Sous réserve de BSTW (arXiv 2409.01350) et Castella (arXiv 2409.01360), et des adaptations A et B, la proportion est au moins de 77,71 % (78,98 % si …) ».

### Objection 5 : relecture du §8 de CLW. **CLOSE**
§8.1 (Th. 8.1.1) et §8.2 n'utilisent ϕ qu'à travers E^Kling_ϕ : le terme constant (Th. 6.1.1, suite exacte du Th. 2.9.1) et « by Proposition 7.11.3 [...] l_θ(E^Kling_{ϕ,β,u})(g) ∉ P ». Le niveau modéré K_f^p y est quelconque (version Σ-primitive, facteurs d'Euler en Σ remis ensuite). Rien n'empêche d'approfondir K_v en v ∈ Σ_s. ✓

### Objection 6 : orientation. **TRANCHÉE en faveur de (L1)** (`probleme_A_note.md` §12)
θ et h₀ sont définis par la même application (7.1.6) avec des fonctions de Schwartz de même forme : ils ont la même orientation. Conséquences : A est résolu par la recette de FW (✓). En revanche, **la recette (iv) de CLW annule l'intégrale aux places décomposées ramifiées (Steinberg, séries principales ramifiées)**, d'après le critère du §4. C'est une lacune possible de CLW et BSTW, cohérente avec le contre-exemple au Lemme 8.14. **Nouvelle objection critique 26 :** le rang 1 passe par la tordue g′ = g ⊗ χ_L, qui est une série principale ramifiée aux ℓ | D_L. S_A dépend donc de ce cas pour le rang 1. À réparer (piste au §12.2, point 4) ou à faire confirmer par Wan.

### Objection 26 (rang 1 et séries principales ramifiées) : **RÉPARÉE** (`probleme_A_note.md` §13)
Proposition R : on prend pour ϕ_v le vecteur nouveau de π_v ⊗ A (f_{χ,ϑ} de Wan avec s = t au lieu de s > t), et des données auxiliaires de type assorti, avec L(π_v ⊗ A^{±1}) = 1. Seule la cellule n = 0 contribue : I_v est une constante non nulle indépendante de τ, pour **toute** π_v (supercuspidale, série principale ramifiée, Steinberg, Steinberg tordu). C'est vérifié numériquement (p = 3) pour les non ramifiées, les Steinberg et les séries principales quadratiques. Les objections 13 et 19 se trouvent du même coup **réparées** dans notre version, quelle que soit la réponse de Wan sur son Lemme 8.14. Reste à valider : la preuve de la Prop. R (point (3) : γ monomial ⇒ une seule couche) et l'extension des tests numériques à ℓ = 2.
