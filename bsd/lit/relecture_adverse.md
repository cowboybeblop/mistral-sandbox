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
