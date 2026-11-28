# Relecture adverse n° 4

28 novembre 2026. Suite de `relecture_adverse_3.md`. Même posture : chercher où cela casse.

**Sources nouvelles.** Kim–Ota, arXiv 1905.02926 : Hypothèse 2.1, Remarque 2.2, §3.2.4 (Déf. 3.5), Hyp. 3.6 et Déf. 3.7, lus.

**Scripts.**
- `scripts/attack_kappa_prudent.py`, résultats dans `results/attack_kappa_prudent.txt` ;
- `results/check_ss5.txt` (énumération mod 125).

## 1. Le point fragile du tour 3 : Steinberg tordu et Kim–Ota (2)

**Objection (I).** Pour une courbe de type I_n* en ℓ (ou « steinberg_tordu » en 2 et 3), avec 5 ∤ n, on a ρ̄|I_ℓ = χ̄ ⊗ (1 *; 0 1), avec χ quadratique ramifié et * ≠ 0. Alors 5 divise #ρ̄(I_ℓ). Prise à la lettre, la Déf. 3.5 (2) de Kim–Ota (« ρ|I_ℓ has unramified quotient of rank one ») n'est pas satisfaite par la forme de la courbe, dont le quotient est χ, ramifié.

**Analyse.**
1. **ÉTABLI (lu).** Kim–Ota, Remarque 2.2 : « Due to the argument in [DFG04, §1.7.1], we may assume that all the newforms in this article have minimal conductor among its twist ». Au §3.2.4 : « Suppose that p | #ρ(I_ℓ). Then the minimally ramified liftings coincide with [Tay03, E3] » (le type Steinberg). Leur définition est donc écrite **pour des formes minimales parmi leurs tordues**. Une forme de type χ ⊗ St avec χ ramifié ne l'est pas.
2. **PROUVÉ (élémentaire).** Prise à la lettre dans notre cas, (2) n'est satisfaite par **aucun** relèvement. Un relèvement avec quotient non ramifié aurait ρ|I ~ (ψ *; 0 1), et sa réduction aurait pour semi-simplifiée ψ̄ ⊕ 1. Or celle de ρ̄|I est χ̄ ⊕ χ̄, avec χ̄ ≠ 1. La lecture littérale donnerait donc un problème de déformation **vide**, ce qui ne peut pas être l'intention. La bonne condition est la tordue par χ de [Tay03, E3]. Le déterminant est préservé, puisque χ² = 1, et ad⁰ est inchangé par torsion, donc le calcul local de Selmer l'est aussi.
3. **PROUVÉ (élémentaire). Tous les relèvements au même niveau sont de ce type, en ℓ ≢ 1 (mod 5).**
   - Un relèvement à inertie finie d'ordre premier à 5 (série principale ou supercuspidale) a une réduction semi-simple sur I_ℓ (Maschke), alors que ρ̄|I_ℓ ne l'est pas (* ≠ 0).
   - Un relèvement de type χ′ ⊗ St doit avoir χ′ ≡ χ (mod λ). Si ℓ ≢ 1 (mod 5), il n'existe pas de caractère modéré d'ordre 5, donc χ′ = χ.
   - Il n'y a donc pas de forme d'un autre type dans T(N_∅)_𝔪, et la surjection du Lemme 6.5 de CH tient avec la condition tordue.
4. **Piège réel, mais déjà évité.** Si ℓ ≡ 1 (mod 5), on peut avoir χη ⊗ St, avec η modéré d'ordre 5 : même conducteur ℓ², même réduction, **type différent**. C'est une vraie congruence à changement de type. Elle est déjà exclue :
   - en 2 et 3, aucun premier n'est ≡ 1 (mod 5) ;
   - en ℓ ≥ 7, la piste 2 exclut ℓ ≡ ±1 (mod 5) ;
   - en ℓ ≡ 1 (mod 5) multiplicatif (St non tordu, conducteur ℓ), η ⊗ St a pour conducteur ℓ² : ce n'est pas le même niveau.

**Statut.** **Réglée au niveau DÉDUCTION.** La lecture littérale de Kim–Ota est vide de sens pour ces types, et leur Remarque 2.2 montre qu'ils travaillent à torsion près. Les ≈ 0,05 pt en jeu sont maintenus.
- Le seul reste est la Déf. 3.1 de Diamond 1997a, utilisée par CH dans (D2), que nous n'avons pas pu lire. Il faudrait confirmer qu'elle est formulée à torsion près ; c'est très probable, mais NON VÉRIFIÉ.
- La question est conservée pour Hsieh et Kim, avec cette analyse.

## 2. Tests globaux supplémentaires

| Test | Résultat | Prévu | Verdict |
|---|---|---|---|
| κ **prudent** de la famille supersingulière (30 000 courbes ; drapeaux E1-E3 calculés sur la courbe elle-même ; signe global) | 0,5709 ± 0,0029 | 0,5687 | +0,8σ, confirmé |
| « 5 \| A et 5 ∤ B ⟺ bonne réduction supersingulière en 5 » (énumération mod 125) | 2 500/2 500 dans un sens, 0 cas contraire | — | confirmé (SS5 = 4/25 correct) |

Avec le tour 3 (κ global 0,5587 ± 0,0008, κ optimiste supersingulier 0,5569 ± 0,0025), **les trois valeurs de κ utilisées sont confirmées globalement**.

## 3. Autres attaques de ce tour

1. **I — La famille supersingulière vérifie-t-elle les hypothèses des réciproques BSTW au-delà de A et B ?**
   - Th. 12.3 : (irr_Q), (ram) si p = 3, « a_p = 0 » (automatique en p = 5) ;
   - Th. 10.1 : (ram) ;
   - p ∤ 2N : bonne réduction en 5.
   
   (irr_Q) vaut pour 100 % des courbes (image surjective). **Réglée.**
2. **I — (CR⁺)(3) de CH (q | N⁻, q ≡ ±1 mod 5 ⇒ ρ̄ ramifiée en q).** N⁻ = q est le premier (ram), donc ρ̄ est ramifiée. **Réglée.**
3. **M — Double comptage base / famille supersingulière.** La base vit sur S0(5) (ordinaire ou multiplicative en 5), la famille SS sur la réduction supersingulière : elles sont disjointes. Les courbes U de la piste 5 sont hors des deux. **Réglée.**
4. **M — Effet de la piste 2 sur κ** (α des additifs III et III* en ℓ ≡ 3 mod 4) : −0,0003 prévu, sous la résolution des tests globaux. Non testé directement. **Assumé.**

## 4. Bilan du tour 4

- Aucune nouvelle erreur trouvée.
- Le point fragile (Steinberg tordu) est réglé au niveau DÉDUCTION, et un piège réel (ℓ ≡ 1 mod 5) est identifié et déjà exclu.
- Tous les κ sont confirmés globalement.
- **Chiffre inchangé : 79,81 %** (prudent), conditionnel à A, B, N6 (ouvert), BSTW, CLW, et à la Déf. 3.1 de Diamond 1997a (forme « à torsion près », non lue).
- **Critère d'arrêt** (skill §4) : deux tours de suite (3 et 4) sans objection critique propre au travail ; le tour 3 avait seulement corrigé deux imprécisions de rédaction sur N6. On peut s'arrêter ici.
