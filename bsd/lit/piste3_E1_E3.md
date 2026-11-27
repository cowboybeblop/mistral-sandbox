# Piste 3 : récupérer E1-E3 en 2 et 3 (avancée partielle, bloquée par une référence)

27 novembre 2026. Suite de `LISTE_GAINS.md`, piste 3. **Aucune preuve n'est annoncée.**

**Source ouverte.** Chida–Hsieh (CH), arXiv 1204.2427, §6, p. 28-32 : Hypothèse (CR⁺), Prop. 6.1, §6.1 (N = N_∅ ∏ q^{m_q}, Σ, L_q), Lemmes 6.2 à 6.6, Cor. 6.7, début de la Prop. 6.8.

**Non accessibles.** Springer est bloqué depuis la session (HTTP 403) :
- Diamond 1997b, *The Taylor–Wiles construction and multiplicity one*, Invent. Math. 128 (1997), no. 2, 379–391, DOI 10.1007/s002220050144 ;
- Diamond 1997a, *An extension of Wiles' results*, in *Modular forms and Fermat's Last Theorem* (Boston, 1995), Springer 1997, Déf. 3.1.

## 1. Ce que dit CH (ÉTABLI, lu)

- **Structure du niveau.** Sous (CR⁺), N = N_∅ · ∏ q^{m_q}, avec N_∅ = N_{ρ₀}·N₁⁻ (le niveau minimal), et :
  - « m_q ≤ 2 » ;
  - « m_q = 0 unless q | N⁺ and q ∤ N_∅ » ;
  - « If m_q = 1, then q ≢ 1 (mod p) » ;
  - d'après [DT94].
- **Cas Σ ≠ ∅ (montée de niveau).** Il est traité par :
  - L_q (6.2) ;
  - le Lemme 6.3 ([Tay06, Lemme 3.1]) ;
  - le Lemme 6.4, qui donne ♯C(N_{Σ∪{q}}) = ♯C(N_Σ)·♯(O/(λ_∅(u_{∅,q})² − 1)) ;
  - le Cor. 6.7 ;
  - [Dia97b, Th. 2.4] : « The proposition follows from [Dia97b, Theorem 2.4] ».
- **(D2)** : « ρ is minimally ramified outside N₁⁻Σ in the sense of [Dia97a, Definition 3.1] ».
- **Lemme 6.5** (R_Σ → T_Σ surjectif) : la preuve ne traite que T_q (q ∤ N_Σ) et U_q (q ‖ N_Σ). Elle suppose implicitement que ρ_Σ vérifie (D2) aux q | N_∅.
- **Où sert « ordinaire »** dans cette partie : seulement dans (D3), en p. Les Lemmes 6.3, 6.4, 6.6 et le Cor. 6.7 portent sur q ≠ p.

## 2. Conséquence pour E1 (DÉDUCTION)

- E1 en q : multiplicatif, 5 | v_q(Δ), donc ρ̄ non ramifiée en q, q ‖ N et q ∤ N_{ρ₀}. On a donc **m_q = 1**, c'est exactement le cas Σ ≠ ∅ de CH.
- Les conditions de CH sont satisfaites :
  - (CR⁺)(4) demande q ≢ 1 (mod 5) : vrai pour q = 2 et 3 ;
  - (CR⁺)(5) aussi : q ∤ N_{ρ₀}.
- Avec la même substitution « ordinaire → plate » en p que dans le cas minimal (déjà DÉDUCTION, `probleme_B_note.md` §1), **E1 est couvert par la preuve publiée de CH**, qui repose sur [Dia97b] (cité, non ouvert).
- **Gain.** Négligeable : aucune cellule E1 n'est résolue en k ≤ 9. E1 tient dans les cellules indéterminées, soit au plus 0,04 % en 2 et 0,006 % en 3.
- **Même remarque pour la piste 7.** L'exclusion ε (q ≥ 7 multiplicatif, 5 | v_q) n'est nécessaire que pour q ≡ 1 (mod 5) ; le gain est ≈ +0,0005 pt. Non intégré.

## 3. E2 et E3 : pas de m_q > 0, le blocage est ailleurs (DÉDUCTION)

- En E2 (χ ⊗ St, 5 | v(j)) et en E3 (χ ⊕ χ avec a_q(E^d) ≡ ±(q + 1)), on a cond(ρ̄) = cond(ρ) en q, puisque χ est modéré ou de même conducteur. Donc **m_q = 0** et q | N_∅.
- Ce n'est **pas** le cas « montée de niveau » de CH. Le problème est que T(N_∅)_𝔪 contient des formes d'un **autre type inertiel** en q (E3), ou que f elle-même n'est pas minimalement ramifiée (E2). Le Lemme 6.5 ne s'applique donc pas tel quel.
- **La torsion ne règle pas tout.** f ⊗ χ_d est de niveau N/q² (E3) ou N/q (E2 → multiplicatif, E1 pour la tordue). Mais la période dont on a besoin est celle de f **au niveau N**. Il faut comparer les modules de congruence de f (niveau N, type χ en q) et de f ⊗ χ_d. La torsion par χ∘Nm ne préserve pas les ordres d'Eichler. C'est l'« argument d'invariance par torsion » de `LISTE_GAINS.md`, à faire. Je ne l'ai pas trouvé dans CH.
- **Voies possibles** (SPÉCULATION) :
  - (i) un système de Taylor–Wiles avec, en q, l'anneau de déformation « type χ ⊕ χ ou χ ⊗ St » (non minimal), via Diamond 1997b ou une approche à la Kisin ;
  - (ii) la comparaison par torsion.
  
  Les deux demandent une lecture qui n'est pas faisable sans Diamond 1997a et 1997b.

## 4. Bilan
- Gain potentiel : S3 optimiste − S3 prudent ≈ **+0,42 pt**, surtout E3 en 2 (3,18 % des courbes en 2). Avec les pistes 1 et 2, on passerait de 79,75 % à **80,19 %** (`bound_v5.py`).
- **Statut : bloqué par la référence.** À se procurer : Diamond 1997b et 1997a (références ci-dessus).
- **Question pour Hsieh** (à ajouter à la question 4 de `BILAN_FINAL.md`) : « In [CH, §6], can Lemma 6.5 be extended to primes q | N_∅ where T(N_∅)_𝔪 contains forms of type χ⊗St and χ⊕χ simultaneously (ρ̄|I_q = χ̄⊕χ̄), e.g. via [Dia97b] with non-minimal local conditions at q? »
