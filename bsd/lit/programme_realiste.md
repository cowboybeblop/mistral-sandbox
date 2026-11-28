# Programme réaliste (objectif ≈ 80,5 %, puis ≈ 81,7 %) : état et nouvelle idée

28 novembre 2026. **Aucune preuve n'est annoncée.**

## 1. Les quatre chantiers et ce qu'on peut faire nous-mêmes

| Chantier | Gain | Qui peut trancher | Ce qu'on peut faire ici |
|---|---|---|---|
| Valider A et B (Prop. V et R′, substitution ordinaire → plate) | condition de **tout** | Wan, Castella, Hsieh | Rien de nouveau. La relance à Wan est prête (`reponse_wan.md`), **à envoyer par l'utilisateur**. |
| N6 (rang 1, tordue g_K) | condition de **tout** | Burungale, Hsieh | Nouvelle idée de torsion (§2). Chao Li ne suffit pas en densité (`veille_28_11.md` §6). |
| E2/E3 en 2 et 3 (≈ +0,44 pt) | +0,44 | Hsieh, Kim | Même idée de torsion (§2). |
| p = 3 (≈ +1,2 pt) | +1,2 | — | Verrou (CR⁺)(1) de CH ; il faudrait une autre preuve de la comparaison des périodes. |

## 2. Nouvelle idée : la torsion par un caractère global (SPÉCULATION étayée)

**Constat.** Les trois cas bloquants ont la même forme locale en un premier q ≠ 5 : f est la tordue par un caractère quadratique χ, ramifié en q, d'une forme g « gentille » en q.
- **E3** (en q = 2, 3, ou ℓ ≥ 7 pour I₀*) : f = g ⊗ χ_d, avec g de **bonne réduction** en q et a_q(g) ≡ ±(q + 1) (mod 5).
- **E2** : f = g ⊗ χ_d, avec g **multiplicative** en q et ρ̄_g non ramifiée. C'est le cas E1 **pour g**, que CH traitent (m_q = 1, q ≢ 1 mod 5 : `piste3_E1_E3.md` §2).
- **N6** : g_K = g ⊗ χ_K en ℓ | D_K, avec g de bonne réduction en ℓ. C'est exactement E3 pour g_K, quand a_ℓ ≡ ±(ℓ + 1) ou ℓ ≡ ±1 (mod 5).

Pour d ∈ {−1, ±2} en q = 2 et d = −3 en q = 3, le caractère χ_d est **global** et ramifié seulement en q. Pour N6, χ_K est global.

**L'idée.** Ne pas travailler au niveau de f (ordre d'Eichler de niveau q² en q), mais transporter tout à g par multiplication par le caractère automorphe χ ∘ Nrd de B^×.
- En q, le vecteur v = (vecteur sphérique de g) vu dans π_f = π_g ⊗ (χ ∘ det) vérifie π_f(k)v = χ(det k)·v pour k ∈ GL₂(ℤ_q). C'est un vecteur « de type χ ∘ det au niveau maximal ».
- La multiplication par χ ∘ Nrd envoie l'espace des formes quaternioniques de ce type **isomorphiquement** sur l'espace des formes de g, non ramifiées en q. Elle est compatible aux opérateurs de Hecke (T_ℓ ↦ χ(ℓ)T_ℓ) et à l'accouplement (χ² = 1).
- **Conséquence attendue.** Les modules de congruence de f, **dans cet espace**, sont ceux de g en un niveau premier à q (E3, N6) ou de niveau q avec ρ̄ non ramifiée (E2 → E1). Il n'y a **plus de problème de type en q**. Les formes χ ⊗ St gênantes de E3 deviennent des formes Steinberg de niveau q pour g, absentes de l'espace de niveau premier à q.

**Ce qu'il faut vérifier** (étapes, chacune à faire) :
1. **Fonction L anticyclotomique.** L(f/L, ψ) = L(g/L, ψ·(χ ∘ N_{L/ℚ})). Comme χ ∘ N est trivial sur A_ℚ^×, c'est un caractère de classes d'anneau de conducteur q (DÉDUCTION, vérifiée sur le papier). La fonction L p-adique anticyclotomique de f est donc la **branche modérée de conducteur q** de celle de g.
   - CH ne traitent que des branches de Δ ⊂ Gal(K_{p^∞}/K), donc de conducteur une puissance de p (lu, §4.3).
   - Il faut les éléments thêta de conducteur q·p^n, avec des points CM de conducteur q·p^n, et **μ = 0** pour cette branche. La méthode de Vatsal et CH (équirépartition des points CM) devrait s'adapter, mais ce n'est **pas vérifié**. À chercher : Vatsal, Hsieh (1112.1574), Pollack–Weston, qui énoncent « for each ring class character ρ₀ of the torsion subgroup, μ = 0 » (cité par 1207.1673).
2. **Formule d'interpolation.** Il faut la période torique locale en q du vecteur « χ ∘ det-sphérique ». C'est la tordue du calcul non ramifié ; elle est explicite et non nulle (à écrire, dans l'esprit de la Prop. R′).
3. **Comparaison des périodes** Ω_{N⁻}(f) ~ Ω_can(f). Avec ce choix de vecteurs, elle se ramène à celle de g. Il faut vérifier que la normalisation de BSTW (Th. 10.5 : (L^{◦,ac}_p) = (∏ c_q · L°_W)) accepte ce changement de vecteur test : les facteurs locaux en q doivent être des **unités** mod 5.
4. **Signal d'alerte** (Böckle–Khare–Manning). Le passage au vecteur tordu évite justement l'algèbre de Hecke non Gorenstein du niveau q², car on reste dans l'espace de g. À confirmer.

**Gain si tout passe.** E2/E3 en 2 et 3 (+0,44 pt), I₀* et I_n* en ℓ ≥ 7 (déjà admis, devient plus sûr), **et N6** (condition de validité de toute la borne). On arriverait à ≈ 80,25 % (prudent + piste 3), avec N6 réglé.

**Statut.** SPÉCULATION étayée. Les étapes 1 à 3 sont du travail technique sur des objets connus (éléments thêta à conducteur modéré, périodes toriques locales). C'est le chantier le plus prometteur du programme réaliste. **Prochaine action** : lire les énoncés exacts sur μ = 0 avec conducteur modéré (Vatsal 2003, Hsieh 1112.1574, Pollack–Weston §2), puis écrire l'étape 2.

## 2 bis. Lecture de Pollack–Weston (math/0610694, §2.3-2.4, lu le 28/11)
- **ÉTABLI.** Th. 2.3 (Vatsal) : « µ(L_p(K∞, f)) = 0 » pour la normalisation quaternionique, et « µ(L_p(K∞, f)) = ord_p(η_f(N)/ξ_f(N⁺, N⁻)) » pour la période canonique. Th. 2.5 : idem dans le cas supersingulier ± (« The results of [32] extend easily to the supersingular case »).
- **Conséquence (DÉDUCTION).** Le problème B se réduit **exactement** à ord₅ η_f(N) = ord₅ ξ_f(N⁺, N⁻), au facteur ∏_{q|N⁻} c_q près. Les cas E2, E3 et N6 sont des premiers de N⁺ où cette égalité pourrait échouer.
  - PW conjecturent (formule (2)) ord_p η_f(aℓ, b) = t_f(ℓ) + ord_p η_f(a, ℓb), où t_f(ℓ) est un terme de Tamagawa. C'est le genre de formule qu'il faudrait démontrer en q.
  - L'idée de torsion (§2) revient à calculer ces congruences pour g plutôt que pour f.
- Le cas d'une branche modérée de conducteur q n'est pas traité dans les passages lus. C'est **toujours à chercher** (Vatsal 2003, Duke, non accessible depuis arXiv).

## 3. Questions à ajouter pour les spécialistes (brouillon, non envoyé)
- (Hsieh, Kim) « For f = g ⊗ χ with χ quadratic ramified at q and g unramified at q, can one run [CH, §6] with the χ∘det-spherical test vector at q, i.e. in the space of g twisted by χ∘Nrd, thereby avoiding the non-minimal configuration at q? Is μ = 0 known for the tame branch of conductor q? »
