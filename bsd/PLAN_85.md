# Plan : explorer de nouveaux horizons pour dépasser 85 % (28 novembre 2026)

## 0. Carte des plafonds (FAIT : `scripts/plafonds.py`, `results/plafonds.txt`)

| Ingrédients supposés | Borne |
|---|---|
| Aujourd'hui (prudent) | 79,81 % |
| p = 5 parfait (aucune exclusion, N6 réglé), κ = 0,5587 | 80,47 % |
| + p = 3 sur les courbes additives en 5 | 81,70 % |
| p = 5 parfait, **κ = 1** (conjecture µ_equi = µ de BSZ) | 84,00 % |
| + p = 3, κ = 1 | 85,33 % |
| **moyenne de Sel₇ = 8** (ouvert), κ = 0,5587 | 87,09 % |
| moyenne de Sel₇ = 8 et κ = 1 | 89,80 % |

**Conséquence (DÉDUCTION).** Aucune combinaison des outils actuels ne dépasse 81,7 %. Pour 85 %, il faut **κ ≥ 0,96**, plus tout le reste. Or la méthode de BS plafonne à κ = P(d = −1) = 0,5587. Il faut donc une **nouvelle idée** d'un des types suivants :
- (H1) équirépartition des signes au-delà de l'astuce d(E) ;
- (H2) des moyennes (ou majorations) de Sel_n pour un n ≥ 6 nouveau, ou des seconds moments ;
- (H3) une autre information sur la parité ou la distribution des groupes de Selmer.

**Observation utile** (borne en fonction de la proportion ρ de signes +1). Pour p = 5, la borne vaut 19/24 si ρ est inconnu, 7/8 si ρ = 1/2, et **≈ 99 %** si tous les signes valent −1. Tout résultat qui **majore** la proportion de signes +1 dans une famille vaut donc de l'or.

## Étapes (enchaînées automatiquement)

- **E1 — Veille « signes ».** Progrès 2023-2026 sur la moyenne des signes de courbes ordonnées par hauteur. Hasard de Möbius sur 4A³ + 27B², Helfgott et suites, parité dans des familles larges, biais de signe.
- **E2 — Veille « Selmer ».** Moyenne ou majoration de Sel_n pour n ∉ {2, 3, 4, 5} (6, 7, 15...), seconds moments (Sel₂, Sel₃), distributions jointes, réciproques en p = 2 et p = 7.
- **E3 — Idée « familles biaisées »** (théorie). Peut-on construire, par conditions locales, une famille large où la proportion de signes −1 dépasse 1/2 de façon démontrable ? Ou démontrer que c'est impossible par la seule méthode de BS ?
- **E4 — Idée « seconds moments »** (calcul). Si E[#Sel₂²] (ou un moment de Sel₃) est connu, que donne le programme linéaire avec deux moments ? Quelles réciproques en p = 2 (ou 3) faudrait-il ? Gain plafond.
- **E5 — Idée « Sel₇ partiel »** (calcul). Quelle majoration de la moyenne de Sel₇ suffirait pour gagner quelque chose ? Existe-t-il des majorations connues ?
- **E6 — Synthèse.** `HORIZONS_85.md` : ce qui est atteignable, ce qui demande un théorème nouveau, avec le meilleur « prochain résultat » à viser. Relecture adverse, commit.

Règles inchangées (skill `chercheur`) : chaque source est ouverte avant d'être citée, chaque énoncé est étiqueté, et rien n'est envoyé hors du dépôt.
