# Hypothèse de Riemann et BSD : vérification sur sources (27 novembre 2026)

Contexte : l'annonce du 20/11/2026 (L. Alpöge avec Claude, preuve de RH et de GRH, **non vérifiée**). Sa portée exacte, en particulier si elle couvre les fonctions L de courbes elliptiques, n'est pas lue (texte original non consulté).

## Ce que disent les sources (ÉTABLI, articles ouverts)

1. **Young, arXiv math/0412464v3.**
   - §4.2 : « The 7/9 result leads to r ≤ 1/2 + 9/7 = 25/14 [...] the application of the bound (4) to an upper bound for r relies on the Generalized Riemann Hypothesis for all elliptic curve L-functions [...] The bound 25/14 is interesting because it demonstrates that a positive proportion of curves have either rank 0 or rank 1. »
   - Le Th. 1.1 (rang 0) suppose en plus la répartition régulière des signes.
2. **Fiorilli, arXiv 1403.7108.**
   - Hypothèses : **ECRH** (RH pour les fonctions L de courbes elliptiques), **plus** une hypothèse un peu plus forte sur les zéros non réels (Hyp. M pour les tordues ; Hyp. 1.12 pour toutes les courbes, « stronger than ECRH by only one logarithm »).
   - Th. 1.14 : sous ces hypothèses, le rang analytique moyen de toutes les courbes y² = x³ + ax + b vaut **exactement 1/2**.
   - p. 6 : « If one also assumes the widely believed conjecture that the root number is equidistributed in the family of all elliptic curves, then the analogue of Corollary 1.2 follows ». Le Cor. 1.2 est « the Birch and Swinnerton-Dyer Conjecture holds for almost all curves [...] one half [...] rank 0, and one half [...] rank 1 ».

## Correction de ma spéculation précédente

J'avais écrit que RH n'apportait « presque rien » au problème. C'est **faux dans sa forme forte**.
- **RH seule ne suffit pas.** Il faut RH pour les fonctions L de courbes elliptiques, l'hypothèse 1.12 de Fiorilli (un cran plus forte) et l'équirépartition des signes. Avec ces trois ingrédients, BSD (partie rang, Ш fini) vaut pour **100 %** des courbes.
- **GRH seule** donne un rang analytique moyen ≤ 25/14 (Young). On en tire seulement une proportion positive de rang 0 ou 1. DÉDUCTION : en majorant naïvement, x₀₊₁ ≥ 1 − 25/28 ≈ 11 %, bien en dessous des 67 % inconditionnels.
- **Ce qui reste vrai.** Nos problèmes A et B (p-adiques, inconditionnels) ne sont pas touchés. Notre borne est **inconditionnelle**, au sens où elle n'utilise pas RH, modulo la validation de A et B, et de BSTW et Castella.
