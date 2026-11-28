# Énoncé conditionnel : ≈ 83,3 % sous la conjecture d'équirépartition des signes

28 novembre 2026. Réponse au point 2 : **peut-on utiliser la conjecture, ou faut-il la prouver ?**

## 1. Réponse de principe
- On peut **utiliser** une conjecture pour énoncer un **théorème conditionnel** : « si la conjecture C est vraie, alors… ». C'est une pratique courante et honnête en théorie des nombres (par exemple les nombreux résultats « sous GRH »), à condition de l'écrire clairement.
- Mais cela **ne fait pas monter la borne inconditionnelle**. Le chiffre démontré reste 79,81 % (lui-même conditionnel à A, B, N6, BSTW, CLW).
- **Prouver** la conjecture, c'est le point 3 : le problème de parité. C'est un autre projet, d'une autre ampleur.

## 2. La conjecture utilisée (CONJECTURE, BSZ p. 7)
**Conjecture E** (BSZ : « We conjecture that for any large family F, we have µequi(F) = µ(F) »). Pour toute famille large F définie par des conditions de congruence en un nombre fini de premiers (et éventuellement à l'infini), et pour tout ε > 0, il existe une réunion finie F′ ⊂ F de familles larges, avec µ(F′) ≥ (1 − ε)µ(F), dans laquelle les signes sont équirépartis.

D'après Helfgott (annexe C), elle est liée à la nullité en moyenne de λ(4A³ + 27B²), un cas ouvert du problème de parité.

## 3. Énoncé (DÉDUCTION)
**Proposition C.** Supposons la Conjecture E, ainsi que les hypothèses du chiffre 79,81 % : A, B, N6, BSTW, CLW, et les exclusions prudentes. Alors au moins **83,30 %** des courbes elliptiques sur ℚ, ordonnées par hauteur, ont un rang algébrique égal au rang analytique, et ce rang vaut 0 ou 1.
- Avec la récupération de E2/E3 (piste 3), on obtient 83,77 %.

*Esquisse.* La structure est celle du Cor. 26 de BSZ avec κ = 1 − ε :
- la famille de base S0(5) ∩ S1(5) donne (7/8)·µ ;
- la famille supersingulière admise (SS5 · μ₂μ₃ · P) donne (7/8)·µ ;
- on fait ε → 0.

Le calcul est dans `results/borne_conditionnelle_parite.txt` : base(K = 1) + SS5·μ₂μ₃P·7/8. ∎

## 4. Relecture adverse
1. **I — La Conjecture E est-elle bien celle de BSZ ?** BSZ définissent µ_equi(F) comme le supremum des µ(F′) sur les réunions finies F′ ⊂ F de familles larges à signes équirépartis, et conjecturent µ_equi = µ. C'est exactement la forme utilisée. **Réglée.**
2. **M — Conditions à l'infini.** Les familles F^± de BS les utilisent déjà. La conjecture « for any large family » les inclut implicitement. **Assumé.**
3. **M — Plafond.** Même sous la Conjecture E, on reste sous 85 % sans p = 3 et sans p = 5 « parfait » (`HORIZONS_85.md`). **Noté.**
