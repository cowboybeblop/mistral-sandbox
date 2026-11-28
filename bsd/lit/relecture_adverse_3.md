# Relecture adverse n° 3 : « prouver que les pistes sont fausses »

27 novembre 2026, nuit. Posture : rapporteur hostile, qui cherche le point où chaque piste casse. Gravité : **C** (critique), **I** (importante), **M** (mineure). Statuts : réglée, réparée, héritée, ouverte.

**Nouvelles sources lues.**
- Terracini, *A Taylor–Wiles system for quaternionic Hecke algebras*, Compositio Math. 137 (2003) 23–47 (fourni par l'utilisateur) : résumé, introduction, §2-4 parcourus.
- BSTW (arXiv 2409.01350 v2) : (2.15) p. 23, Th. 10.5, §10.3, Th. 12.3.

**Nouveaux scripts.**
- `scripts/attack_kappa_global.py`, résultats dans `results/attack_kappa_*.txt`.
- `scripts/mc_check_23.py` et `scripts/mc_check_l7.py` (déjà au §2 de `verification_finale_27_11.md`).

## Attaque transversale : κ mesuré globalement (le test le plus dur)

Toute la piste 1 (et la piste 4) repose sur la formule κ = ∏C/2 + (3/10)∏D. Elle combine :
- les signes locaux de PARI en 2 et 3 (sur cellules) ;
- le Lemme 36 de BS ;
- le facteur 4/5 à l'infini ;
- l'indépendance des conditions locales ;
- une troncature (au plus 2 premiers exceptionnels sous 10⁴).

Une seule erreur dans cette chaîne fausserait κ. **Test indépendant** : on tire (A, B) uniformément dans la boîte de hauteur et on calcule d(E) = r(E)·r(E₋₁) avec le **signe global** (`ellrootno(E)`), sans aucune donnée locale.

| Famille | Tirages | P(d = −1) mesuré | Prévu | Écart |
|---|---|---|---|---|
| toutes les courbes (\|A\| ≤ 10⁶) | 400 000 | **0,5587 ± 0,0008** | 0,55872 | 0,0σ |
| supersingulière en 5, semistable en ℓ ≥ 7, sans 5 \| v_ℓ (\|A\| ≤ 3·10⁵) | 40 000 | **0,5569 ± 0,0025** | 0,5585 | −0,6σ |

**Conclusion.** La valeur de κ et toute la chaîne qui la produit sont confirmées globalement.
- Ce test ne « réfute » pas BS : leur 0,5501 est une **minoration** de la densité d'une sous-famille de {d = −1}, et la vraie valeur 0,5587 la respecte.
- Les coquilles de leurs tables restent établies par les tests ciblés (`feq_check.py`), pas par ce test.

## Piste 1 (équirépartition) : où cela pourrait-il casser ?

1. **C — Le 7/8 s'applique-t-il à F′ ?** Le Th. 25 (seconde partie) demande :
   - F′ réunion finie de familles larges : vrai, les conditions en p ≥ 10⁴ contiennent tous les p² ∤ Δ ;
   - la moyenne de Sel₅ égale à 6 dans F′ (Th. 13) ;
   - la parité (Th. 15) ;
   - des signes exactement équirépartis : vrai, par la bijection E ↔ E₋₁ qui préserve la hauteur, avec d = −1.
   
   Les courbes avec B = 0 (E₋₁ ≅ E) ont d = +1 et sont donc exclues d'office. **Réglée.**
2. **C — Les réciproques (rangs 0 et 1) valent-elles pour E₋₁ aussi ?** Oui : les cellules prudentes exigent E **et** E₋₁ dans la famille prudente. **Réglée.**
3. **I — Le test global ci-dessus porte sur le scénario optimiste.** Le κ prudent (0,5684) n'est pas testé globalement : il faudrait les drapeaux E1-E3 dans le tirage. La différence ne vient que de la restriction en 2 (D₂ conditionnel), vérifiée par le Monte-Carlo de `mc_check_23.py` (moins de 2σ). **Réglée** (indirectement).
4. **I — Conditions à l'infini et Th. 13.** BSZ eux-mêmes appliquent le Th. 25 à F^± (Cor. 26). **Héritée.**
5. **M — Les tables de BS ont-elles été mal lues ?** Elles ont été lues sur l'image des pages. Et surtout, **notre κ n'utilise pas ces tables** : il est confirmé globalement. **Réglée.**

**Verdict.** Je n'ai pas trouvé de faille. Le gain de 0,69 pt hérite seulement des conditions générales (A, B, N6).

## Piste 2 (additif en ℓ ≥ 7) : où cela pourrait-il casser ?

1. **C — Le Lemme types23 étendu.** Contre-exemple cherché : une forme congrue mod 5 de **type inertiel différent**, au même niveau, en ℓ ≢ ±1 (mod 5).
   - Le type modéré est d'ordre divisant ℓ² − 1, premier à 5. Une forme congrue à type différent demanderait un caractère modéré d'ordre 5, qui n'existe pas.
   - Un Steinberg tordu n'est congru que si ρ̄|I est scalaire : c'est le cas I₀*, exclu par E3, et I_n* avec 5 | n (E2).
   - Une forme de niveau **inférieur** en ℓ est impossible, car le conducteur de ρ̄ en ℓ (modéré, inertie d'ordre premier à 5) égale celui de ρ.
   
   **Pas de faille trouvée. DÉDUCTION maintenue.**
2. **I — Steinberg tordu (I_n*, 5 ∤ n) et la Déf. 3.5 (2) de Kim–Ota prise à la lettre.** Le quotient de rang 1 est χ, ramifié, donc **non minimal à la lettre**. Point hérité de « steinberg_tordu » en 2 et 3. Impact en ℓ ≥ 7 : moins de 10⁻⁶. Impact en 2 et 3 : μ(steinberg_tordu) ≈ 0,0010 en 2 et 0,0027 en 3, soit ≈ 0,05 pt au total si on devait l'exclure. **Ouverte, héritée** (question 4).
3. **I — Côté A, le support du Lemme 8.13 en ℓ ≥ 7.** Il n'a été vérifié numériquement qu'en 2 et 3. **Héritée.**
4. **M — Les densités.** Vérifiées par Monte-Carlo en ℓ = 7 et 13. **Réglée.**
5. **M — (Heeg) et L″ avec ℓ² | N.** Ce sont des conditions de décomposition en nombre fini. La Prop. 3.8 de CH (période locale) vaut en tout q | N⁺ sans condition d'exposant (`relecture_adverse.md`, objection 14). **Réglée.**

## Piste 3 et piste 7 (E1 via CH, cas Σ ≠ ∅) : où cela pourrait-il casser ?

1. **C — CH exige-t-il q ≢ 1 (mod p) partout où il sert ?** Les Lemmes 6.4 et 6.6 utilisent « q ≢ 1 (mod p) ». Nous excluons q ≡ 1 (mod 5). **Réglée.**
2. **I — Le Th. 2.4 de Diamond (cité par CH).** Son contenu est confirmé par Iyengar–Khare–Manning : un critère d'algèbre commutative. **Réglée.**
3. **I — Substitution ordinaire → plate dans le cas Σ ≠ ∅.** Les Lemmes 6.3 à 6.6 et le Cor. 6.7 ne portent que sur q ≠ p (lu). **Héritée** de la DÉDUCTION Σ = ∅.
4. **M — Terracini 2003 débloque-t-il E2 et E3 ?** **Non.** Son cadre est un « newform which is supercuspidal of type ω at ℓ », où ℓ est le premier des coefficients (« ℓ > 3 »), avec une représentation « semi-stable outside » (résumé). Le type est imposé en p, pas en q ≠ p. Il utilise [Diamond, Th. 2.1] et [CDT, Th. 5.4.2]. Nos cas E2/E3 (q ≠ p, type non semistable) **ne sont pas couverts**. Piste 3 : **ouverte**.

## Piste 4 (κ) : où cela pourrait-il casser ?

1. **C — « κ ≤ P(d = −1) » est-il un plafond absolu ?** **Non**, seulement pour la méthode de BS : appariement E ↔ E₋₁, seule torsion qui préserve la hauteur. Une autre source d'équirépartition (conjecture de BSZ, µ_equi = µ) n'est pas exclue. La note `pistes_6_7_4.md` le dit déjà ainsi (« La méthode de BS ne met en famille équirépartie que... ») ; formulation vérifiée. **Réglée.**
2. **I — Le κ de la base vaut-il pour S0(5) ∩ S1′(5) ?** Les conditions ne portent qu'en 5, où d₅ = +1. Le test global sur toutes les courbes vaut 0,5587. **Réglée.**

## Piste 5 (p = 3) : où cela pourrait-il casser ?

1. **I — « Presque aucune courbe ordinaire en 3. »** Preuve : j ≡ 0 (mod 3) si 3 ∤ A, puisque 1728 ≡ 0 et le dénominateur est une unité ; le Monte-Carlo le confirme. **Réglée.**
2. **I — « (CR⁺)(1) exclut p = 3. »** C'est lu mot pour mot (« The prime p > k + 1 »). Mais une autre preuve de la comparaison des périodes en p = 3 pourrait exister : le plafond d'environ +1,5 pt n'est donc qu'une estimation. **Formulation correcte** (« verrou », pas « impossible »).

## Piste 6 : où cela pourrait-il casser ?

Le critère « 3 relèvements » rate les sous-ensembles rares. Le Monte-Carlo indépendant (`mc_check_23.py`) donne un accord à moins de 2σ. **Réglée.**

## Piste 8 (N6) : où cela pourrait-il casser ? Deux erreurs trouvées et corrigées

1. **I — Erreur 1 : « D_K premier est impossible ».** C'est faux pour **D = −4** (K = ℚ(i)) : (−4/5) = +1. **Réparée** dans `piste8_N6.md` §2. L'exception reste sans usage général : il faut 2 ∤ N, a₂ ≠ ±2, et c'est un seul corps.
2. **I — Erreur 2 : « l'obstruction vaut pour Ono–Skinner ».** C'est faux si leurs tordues sont D₀·ℓ, qui n'est pas premier. **Réparée.** C'est à vérifier sur le texte d'Ono–Skinner (inaccessible).
3. **M — Seuil 10⁻⁸ sur les L(1) numériques.** C'est une indication, assumée comme telle.

## Bilan de la relecture 3

| Piste | Verdict |
|---|---|
| 1 | tient ; confirmée globalement (κ mesuré = κ calculé) |
| 2 | tient (DÉDUCTION) ; un point hérité (Steinberg tordu et Kim–Ota (2), ≈ 0,05 pt en jeu en 2 et 3) |
| 3 | E1 tient ; E2/E3 ouverts, Terracini ne les couvre pas |
| 4 | tient ; plafond bien limité à la méthode de BS |
| 5 | tient comme étude de faisabilité |
| 6 | tient |
| 7 | tient (DÉDUCTION, via CH et Diamond Th. 2.4 confirmé) |
| 8 | **deux erreurs corrigées** (D = −4 ; Ono–Skinner) ; reste ouverte |

**Chiffre inchangé : 79,81 %** (prudent), conditionnel à A, B, N6, BSTW et CLW. Aucune objection critique propre aux pistes ne subsiste.

**Point qui mériterait un 4ᵉ tour** (traité dans `relecture_adverse_4.md` §1 : réglé au niveau DÉDUCTION). Le Steinberg tordu (Kim–Ota (2)) est déjà présent dans 78,61 %. Si un spécialiste le jugeait non minimal, il faudrait retirer ≈ 0,05 pt et le traiter comme E2.
