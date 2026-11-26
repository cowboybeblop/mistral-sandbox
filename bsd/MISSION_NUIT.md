# Mission autonome (nuit du 26 au 27 novembre 2026)

Branche : `ccr-1b1ab8f4-2hr1mt`. **Lire d'abord** `bsd/lit/BILAN_26_11.md`, puis `bsd/lit/relecture_adverse.md`, `bsd/lit/probleme_A_note.md` (§9-13), `bsd/lit/probleme_B_redaction.md` et `bsd/lit/raccord_A_B.md`. Les PDF et les extractions texte des articles se trouvent dans le scratchpad (`papers/`, `user_pdfs/`). S'ils ont disparu, les retélécharger depuis arXiv.

**Règles (celles de l'utilisateur, non négociables).**
- Ouvrir chaque article avant de le citer.
- Étiqueter chaque énoncé ÉTABLI, DÉDUCTION, NON VÉRIFIÉ, CONJECTURE ou SPÉCULATION.
- Ne jamais annoncer une preuve.
- Faire une relecture adverse avant de rendre.
- S'arrêter sur un sujet si deux étapes de suite n'apportent rien, et passer au suivant.
- Ne pas écrire à des tiers et ne rien envoyer hors du dépôt : l'utilisateur décide des envois.
- Committer et pousser après chaque phase.

## Phase 1 : résoudre les objections restantes de `relecture_adverse.md`

Objections ouvertes : 4, 7, 8, 9 (partiel), 10, 11, 12, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25. Pour chacune : la traiter (lecture, calcul, test numérique) ou documenter précisément pourquoi elle reste ouverte. Priorités :
1. **8** : rédiger en entier la preuve de la Proposition R (`probleme_A_note.md` §13), surtout le point (3), « γ monomial ⇒ une seule couche ». Vérifier sur la formule de Hu (2.66) ou par l'équation fonctionnelle de Jacquet–Langlands.
2. **15** : rédiger ligne à ligne la version cristalline de la Prop. 6.8 de Chida–Hsieh, à partir de Taylor 2006 §2 (fichier `user_pdfs/774a6159-fm2.txt`).
3. **14** : identifier L°_W de BSTW avec la fonction L± de Darmon–Iovita (préprint McGill) ; vecteur-test aux ℓ² | N⁺ décomposés.
4. **4** : relire toute la chaîne BSTW Th. 1.6 / 12.3 → 10.1 → 10.5 et chasser toute hypothèse « square-free » cachée.
5. **7 et 12** : (L1) et appariement des indices ; familles non unitaires dans Ichino et la Prop. 7.11.3 de CLW.
6. **21 à 23** : valider la classification des types locaux sur des courbes de types connus (LMFDB si accessible, sinon familles explicites), augmenter k, recalculer ε proprement.
7. **9 et 10** : élargir les tests numériques (p = 2, conducteurs plus grands), et tester le cas supercuspidal si un modèle explicite est réalisable (niveau zéro en p = 3).

## Phase 2 : autocritique massive de la résolution

Écrire `bsd/lit/relecture_adverse_2.md`. Il s'agit d'une nouvelle relecture hostile de **tout** ce qui a été produit, y compris la Prop. R, la lecture (L1), le chiffrage à 79,02 % et l'élargissement de (5.6.12). Viser de nouvelles objections, les classer C/I/M, puis les traiter comme en phase 1. Recommencer tant que des objections critiques nouvelles apparaissent, en s'arrêtant si deux tours de suite n'apportent rien.

## Phase 3 : document final en anglais et choix de spécialistes

- Rédiger `bsd/REPORT_EN.md`, un document complet et autonome en anglais pour un spécialiste. Contenu : contexte (BSZ, BSTW, la borne), énoncés précis, Proposition R avec preuve, B avec preuve, raccord, chiffrage, vérifications numériques, liste honnête de ce qui reste à valider, références exactes.
- Proposer 3 à 5 spécialistes **pertinents**, avec la justification et la partie du document qui les concerne : Wan (CLW et §8D), Hsieh (Chida–Hsieh, Hsieh 2021), Chan-Ho Kim ou Ota (Kim–Ota), Pollack ou Weston, Castella, Fouquet. Indiquer les adresses telles qu'elles figurent dans les articles, à vérifier. **Ne rien envoyer.**
- Mettre à jour `bsd/lit/BILAN_*.md` avec un résumé final en français pour l'utilisateur.
