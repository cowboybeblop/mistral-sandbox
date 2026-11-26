# Note for a specialist: updating Bhargava–Skinner–Zhang's 66.48 %

*Draft, 26 November 2026. Written with the help of an AI model (Claude) and not reviewed by any number theorist. Computations: `bsd/scripts/bsz_bound.py`, `local_densities.py`, `local_types.py`, `check_deductions.py` (PARI/GP 2.15.4). We ask for a check of the four steps marked (★).*

## Claim (conditional)

When elliptic curves over ℚ are ordered by height, **at least 66.99 %** satisfy rank = analytic rank ≤ 1 with finite Ш, against 66.48 % in [BSZ, Cor. 26]. At least 20.90 % have algebraic and analytic rank 1 (BSZ: 20.68 %).

## Argument

We keep BSZ's framework unchanged: 5-Selmer average 6 in large families (Bhargava–Shankar), parity (Dokchitser²), root-number equidistribution on > 55.01 % of any large family defined by conditions at primes ≡ 1 mod 4 [BSZ Thm 16], and the combinatorics of [BSZ Thm 25, Cor. 26]. We only replace the rank-one converse [BSZ Thm 9]:

- **good ordinary reduction at 5**: [BSTW, arXiv 2409.01350, Thm 12.3]. p ∤ 2N ordinary, E[p] irreducible: corank Sel_{p^∞} = 1 and Ш[p^∞] finite ⇒ ord_{s=1} L = 1, with no hypothesis on the conductor for p ≥ 5;
- **multiplicative reduction at 5**: [Castella, arXiv 2409.01360, Thm 1.1]. Its hypotheses are (i) E[p] irreducible, (ii) non-split multiplicative reduction at some q ≠ p where E[p] is ramified, (iii) E(ℚ_p)[p] = 0. It removes BSZ's conditions on ord₅(Δ) and on the L-invariant.

The family where both converses apply becomes {5 ∤ A} minus {split multiplicative at 5 with 5 | ord₅ Δ}, of density (4/5 − 8/(25·3124))/(1 − 5⁻¹⁰) = 0.799898 (BSZ: 0.791805). It is defined by conditions at 5 only and is stable under the twist by −1. Hence

(7/8 · 0.5501 + 19/24 · 0.4499) · 0.799898 + 3/8 · 0.5501 · 0.000102 = **0.66994**.

The same script reproduces BSZ's 0.664817 from their inputs.

## Steps to check (★)

1. (★) *S₅(E) ≅ ℤ/5, E[5] irreducible ⇒ corank Sel_{5^∞} = 1 and Ш[5^∞] = 0* (Cassels–Tate). This is used by BSZ (Thm 9) and Castella (Cor. 1.2).
2. (★) *(iii) holds on the family.* For non-split reduction, E₀/E₁ ≅ the non-split torus, of order 6, and the component group has order ≤ 2. For split reduction with 5 ∤ k, a 5-torsion point of ℚ₅^×/q^ℤ forces 5 | j·k. Numerically: 600 random curves, no point of order 5 over ℚ₅, and a positive control on 11a1 and 11a3.
3. (★) *(ii) holds for 100 % of curves.* The density at ℓ ≥ 7 of "non-split, ord_ℓ Δ = 1" is exactly (ℓ − 1)²/(2ℓ³), checked for ℓ ≤ 29. The argument of [BSZ, Lemma 20] then applies.
4. (★) BSZ Thm 16 applies to the new family: conditions at 5 only, 5 ≡ 1 mod 4, and stability under the twist by −1.

## Where the real gain is, and a precise question

BSZ's projection of ≈ 80 % (§4) needs converses at **supersingular** p = 5 (the curves with 5 | A, 5 ∤ B, density 0.16). All supersingular results we found assume N square-free: BSTW Thms 1.3, 1.6, 10.1, 12.3; Sprung (arXiv 1610.10017, Thm 1.1); Castella–Wan (arXiv 1607.02019). Semistability at 2 has density only 3/1023 for short models, so they contribute 0.02 points.

In BSTW, the Euler-system divisibility (Thm 10.4) needs no hypothesis on N. The square-free hypothesis enters the Eisenstein-congruence divisibility (Thms 9.24 and 10.5). According to the proof of Thm 9.24, it is used "for explicit calculation of local triple product periods", and principal-series primes are already handled.

Our computation of local components of y² = x³ + Ax + B at 2, with conservative classes, gives:
- semistable: 0.3 %;
- twisted Steinberg: 0.1 %;
- principal series via a ramified quadratic twist: 6.5 %;
- other, mostly supercuspidal: **93.1 %**.

At 3, "other" (potentially good, non-quadratic) has density 32 %. Hence:

| Converses at supersingular 5 available when local components at 2 and 3 are | Bound |
|---|---|
| unramified or Steinberg (today) | 67.02 % |
| + principal series and twisted Steinberg | 67.55 % |
| any type at 2 and 3 (supercuspidal included) | **79.03 %** |
| no condition on N at all | 80.39 % |

**Question.** Can the local triple product periods entering [BSTW, Thm 9.24] (via [39, Thm 8.2.3] and [141]) be computed, or at least shown to be p-adic units or controlled, when the component at 2, or at 3, is supercuspidal? A positive answer, together with a check of the μ-invariant inputs ([116], [21] in BSTW) and of the choice of the auxiliary field, would raise the BSZ bound to about 79 %.

## References

[BSZ] Bhargava–Skinner–Zhang, arXiv 1407.1826. [BS] Bhargava–Shankar, arXiv 1312.7859. [BSTW] Burungale–Skinner–Tian–Wan, arXiv 2409.01350. [C] Castella, arXiv 2409.01360. [S] Sprung, arXiv 1610.10017. [CW] Castella–Wan, arXiv 1607.02019. [K] Kim, arXiv 2109.12344.
