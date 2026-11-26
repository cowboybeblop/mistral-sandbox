# Bilan du 26 novembre 2026 (branche ccr-1b1ab8f4-2hr1mt)

**Statut : rien n'est démontré au sens d'une preuve validée.** Tout ce qui suit est **conditionnel** : à la validation par des spécialistes (Wan, Hsieh ou Kim), et à BSTW et Castella pour la base.

## Où on en est

| Élément | Statut | Document |
|---|---|---|
| A (places décomposées, toute π_v) | Proposition R : preuve courte, vérifiée numériquement en ℓ = 2 et 3 pour les non ramifiées, Steinberg et séries principales ramifiées ; FW démontré pour les supercuspidales | `probleme_A_note.md` §9-13 |
| Lecture des vecteurs de θ et h | (L1), même orientation (CLW (7.1.6)) | §12 |
| Lemme 8.14 de Wan | faux tel qu'énoncé (deux méthodes numériques indépendantes) ; la recette (iv) de CLW annulerait les intégrales aux places décomposées ramifiées ; la Prop. R répare | §9.3, §10, §12 |
| B (μ = 0 et périodes, N⁺ quelconque) | rédigé ; étapes vérifiées sur Taylor 2006, Cornut–Vatsal, Chida–Hsieh et Kim–Ota | `probleme_B_redaction.md` |
| Raccord (corps auxiliaire, tordue g′) | fait | `raccord_A_B.md` |
| Relecture adverse | 26 objections ; 1, 2, 3, 5, 6, 26 traitées ; 13 et 19 réparées par la Prop. R | `relecture_adverse.md` |
| Borne | **79,02 %** si tout est validé (aujourd'hui 67,02 %) | `raccord_A_B.md` §7, `bound_v2.py` |

## À faire ensuite

1. **Réponse de Wan.** Lui proposer la Prop. R comme correction du §8D.
2. **Faire relire** la Prop. R, en particulier le point (3) : γ monomial ⇒ une seule couche.
3. **Objections restantes** : 7, 8, 9 (partiellement fait), 10, 14 à 18, 21 à 25.
4. **Rédiger un document final unique**, en anglais, pour un spécialiste.
