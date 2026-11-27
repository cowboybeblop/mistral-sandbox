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

---

## Traitement des objections restantes (27 novembre)

Sources rouvertes pour ce traitement :
- Wan 1408.4044, §8D ;
- CLW 2109.08375, §5.6 et p. 72 ;
- BSTW 2409.01350, §2.5, Th. 2.9, Th. 2.10, Lemme 2.13, §9.4, §10, Th. 12.3 ;
- Chida–Hsieh 1204.2427, §3.6 et §6 en entier ;
- Pollack–Weston math/0610694, §2 ;
- Taylor 2006, §2 ;
- Hsieh 1112.1580, Th. A et C ;
- Hu IMRN 2018, (2.63)-(2.65).

La revérification du 27/11 (`reverification_27_11.md`) change deux choses :
- La Prop. R a une preuve plus simple. Elle vaut pour toute π_v, avec A arbitraire (trivial compris).
- Côté A, **aucune classification des types locaux n'est plus nécessaire**.

| N° | Statut au 27/11 | Traitement |
|---|---|---|
| 4 | **RÉGLÉE** (lecture) | Dans la chaîne Th. 1.6 / 12.3 → 10.1 → 10.5, « square-free » sert seulement à quatre endroits. (a) Th. 9.24, pour le calcul des périodes locales du produit triple ; BSTW le disent en note 20. C'est le problème A. (b) Th. 10.5 : μ(L°_W) = 0 via [116] (PW, niveau sans facteur carré) et l'identité des périodes. C'est le problème B. (c) (2.16) « N_L squarefree », où N_L est la partie de N première à D_L : c'est trivial, puisque (D_L, N) = 1 par (9.9). (d) Th. 11.12 (formule de BSD), hors de la chaîne. Th. 2.9, Th. 2.10, Lemme 2.13, Th. 10.4, Prop. 10.7 et Prop. 12.1 n'ont pas cette hypothèse. Dans la preuve du Th. 10.1, « since g is semistable, there exists q \| N satisfying (ram) » est remplacé par le Lemme 20 de BSZ (100 % des courbes). |
| 7 | **CADUQUE** | La Prop. R′ fixe elle-même les données : f_θ et f_h de niveau t₁ = a, et (χ_hχ_θ^c)_𝔳·A non ramifié. La première clause de (iv) (χ_{θ,𝔳} non ramifié, ord cond χ_{θ,𝔳̄} ≥ 2c + 2) donne exactement cond(χ_{θ,1}χ_{θ,2}^{-1}) = a. La lecture littérale de FW Cor. 7.28 n'intervient plus. |
| 8 | **RÉGLÉE** (DÉDUCTION, preuve complète) | `reverification_27_11.md` §4. Le point (3) découle du support de Kirillov et du produit scalaire G-invariant (Hu (2.63)/(2.65)). On n'utilise plus γ monomial. |
| 9 | **RÉGLÉE** pour A, sauf un cas | Tests disponibles. Wan 8.13 en ℓ = 2 et 3. Wan 8.14 : trois couples (t, s) et la somme exacte sur GL₂(ℤ/27). Prop. R avec A ramifié : non ramifiée, Steinberg et série principale ramifiée, en ℓ = 2 et 3. Prop. R avec A trivial : non ramifiée (deux paramètres) et Steinberg, en ℓ = 3, dans le modèle induit. **Non testé numériquement : le cas supercuspidal**, faute de modèle explicite. La preuve n'y distingue cependant aucun cas. |
| 10 | **CADUQUE** | La formule (2.66) de Hu n'est plus utilisée. |
| 11 | **CADUQUE** | Le Lemme 6.8 de Hsieh n'est plus utilisé. |
| 12 | **RÉGLÉE** (DÉDUCTION) | Seule la double classe K_{t₁} contribue : I_v est une intégrale **finie**, dans laquelle les torsions non ramifiées de θ et h n'apparaissent pas. L'identité vaut donc pour toute spécialisation, unitaire ou non, et la question du prolongement ne se pose pas. π_v est fixée et unitaire (tempérée). |
| 13, 19 | **RÉPARÉES** (Prop. R′) | La cause est identifiée : la Prop. V (`reverification_27_11.md` §2). |
| 14 | **RÉGLÉE** (lecture) | BSTW appliquent [116, Th. 1.2] (PW) directement à L°_W, qui est donc la fonction de PW. Pour N⁺ quelconque, on prend la normalisation de CH (f primitive, période de Gross ⟨f, f⟩_R). CH ne supposent que **N⁻ sans facteur carré** (lu, p. 1 : « We assume that N⁻ is the square-free product of an odd number of primes »). Leur Prop. 3.8 donne la période locale en **tout** q \| N⁺, sans condition d'exposant : P(ς_q, φ_q, χ)·‖φ_π‖_q/(\|D_K\|^{1/2}ε(π)) = χ_q(N⁺) pour χ non ramifié en q. La preuve n'utilise que Ψ(1/2, W_π, χ) = L(1/2, π ⊗ χ) pour le vecteur nouveau. L'identité de BSTW devient (L^{◦,ac}_p) = (u·L°_W), avec u unité, par CH Prop. 6.1. |
| 15 | **RÉGLÉE pour la structure** (DÉDUCTION, table ci-dessous) ; une nouvelle objection en sort (N2) | Voir le tableau « Taylor §2 ». |
| 16 | **Largement RÉGLÉE** | Vatsal 2003 : inutile, la preuve du Lemme 5.4 de CH a été refaite le 26/11. Diamond 1997b : inutile si Σ = ∅, et les cas Σ ≠ ∅ sont exclus (N2). Carayol : remplacé par un argument direct, voir N2. DDT et [Dia] Th. 2.1 : utilisés seulement **à l'intérieur** de la preuve du Th. 2.6 de Taylor, qu'on prend comme énoncé publié. **Reste NON VÉRIFIÉ :** que la définition de Diamond 1997a, Déf. 3.1, citée par CH en (D2), coïncide avec la condition locale explicite qu'on utilise (relèvement rigide si p ∤ #ρ̄(I_q), type Steinberg sinon). |
| 17, 18 | **RÉGLÉES** (lecture) | PW, preuve du Th. 2.5 (lue) : « L_n is divisible by ω_n^ε where ε equals the sign of (−1)^{n−1}. For a fixed parity of n, factoring out these extra zeroes then produces the norm compatible sequence that yields L^ε_p ». Chaque signe utilise donc une parité de n. Notre étape 2 (CH Cor. 5.2) donne μ(θ_n) = 0 **pour tout** n > n₀, donc pour les deux parités, donc pour les deux signes. |
| 20 | **HÉRITÉE de BSTW** | Le choix du corps de Heegner L par [51] (Friedberg–Hoffstein) est celui de BSTW Th. 12.3. Les conditions locales demandées, à savoir (Heeg) (tout ℓ \| N décomposé, 2 compris), (2.15) et (9.9), sont les mêmes que dans le cas sans facteur carré, et [51] ne porte pas sur le conducteur. [51] n'a pas été ouvert (NON VÉRIFIÉ, comme chez BSTW). L″ existe par le théorème des restes chinois (raccord §2). |
| 21, 23 | **CADUQUES côté A** ; côté B, remplacées par N2 | Seuls les drapeaux « non minimal » de B demandent un calcul local (`local_types_v3.py`). |
| 22 | **INCHANGÉE** (M) | ε ≈ 5,3·10⁻⁵ (q ≥ 7). L'ordre de grandeur est sûr, puisque le terme q = 7, m = 5 domine. |
| 24 | **EN PARTIE** | Les points critiques (Lemme 8.14, Lemme 8.17, Prop. R′) ont maintenant des preuves analytiques **et** des vérifications numériques indépendantes. Restent la relecture par des spécialistes et une reproduction en Sage ou Magma (indisponibles ici). |
| 25 | **RÉGLÉE** | Document unique `bsd/REPORT_EN.tex` (pdf). |

### Taylor 2006 §2, étape par étape : ce qui dépend de la condition en p (objection 15)

| Étape (Taylor §2, lu) | Dépend de la condition en p ? | Version ordinaire de CH | Notre version (cristalline) |
|---|---|---|---|
| Foncteur D_∅ : déformations non ramifiées hors de l et Σ, det fixé, condition de Fontaine–Laffaille en x \| l | oui | (D3) ordinaire | celle de Taylor, inchangée |
| Lemme 2.1 : forme locale en x ∈ Q (premiers de Taylor–Wiles), structure de O[Δ]-module, surjection R_Q → h(U_{1,Q})_m | (3) : les ρ modulaires vérifient la condition en l | via Hida | via Taylor Lemme 1.4 : poids 2 ≤ l − 1, cristallin, dans l'image de M |
| Lemme 2.2 (isomorphisme α en x ∈ Q) | non | idem | idem |
| Lemme 2.3 et Cor. 2.4 (liberté sur O[Δ_Q]) | non. Demande l ∤ #(U ∩ xD^×x^{-1})/F^× | CH : ordres d'Eichler | groupes d'unités d'ordre divisant 12, premier à 5 |
| Borne locale en x \| l : #H¹_f \| #(O/λⁿ)#H⁰ | oui | borne ordinaire | celle de Taylor (p. 21), via Fontaine–Laffaille |
| Formule de Wiles ([DDT] Th. 2.19) : #Q + dim H¹_∅(ad⁰(1)) générateurs | non, une fois les bornes locales données | — | — |
| Lemme 2.5 (premiers de TW) | non. Demande ρ̄\|G_{F(√±l)} irréductible et l > 3 | (CR⁺)(2) | (CR⁺)(2), l = 5 |
| Th. 2.6 : R_∅ ≅ h(U₀)_m, S libre (par [Dia] Th. 2.1) | conséquence | — | — |
| Places q ≠ l de niveau (CH) : (D2) minimale ; (D5) sp en q \| N⁻ ; ♯L_q = ♯H⁰ | non | CH, [Ter03 §3.4] | idem. En q \| N⁺ avec p ∤ #ρ̄(I_q), ♯H¹(Ẑ, M) = ♯M^{Frob} = ♯H⁰ (calcul du 26/11, §9 de B) |

**Conclusion (DÉDUCTION).** La version cristalline de la Prop. 6.8 de CH, pour Σ = ∅, s'obtient en remplaçant (D3) par la condition de Taylor. Aucune autre étape ne voit la condition en p. La surjection R_∅ → T_∅ (CH Lemme 6.5) suppose toutefois que **toutes** les formes de T_∅ = T(N_∅)_m sont minimalement ramifiées. CH ne le vérifient pas explicitement en q \| N⁺ avec q² \| N_∅. C'est l'objet de la nouvelle objection N2 (`relecture_adverse_2.md`).
