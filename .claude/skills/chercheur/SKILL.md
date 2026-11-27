---
name: chercheur
description: Méthode de recherche mathématique rigoureuse, apprise sur le programme BSD (novembre 2026). À utiliser dès que l'utilisateur veut étudier un problème de recherche (théorie des nombres ou autre), vérifier un résultat publié, trouver une faille ou une amélioration, chiffrer un gain, ou rédiger un rapport pour des spécialistes. Couvre les règles de rigueur, le déroulé en phases, les vérifications numériques, la relecture adverse, la rédaction LaTeX et le contact avec les auteurs.
---

# Skill « chercheur »

Méthode tirée du programme BSD (branche `ccr-1b1ab8f4-2hr1mt`, dossier `bsd/`). Elle a produit : une erreur trouvée dans un lemme publié (Wan, ANT 2020, Lemme 8.14), une intégrale locale démontrée nulle (Lemme 8.17), une réparation, un chiffrage conditionnel (67 % → 78,6 %), et une confirmation partielle par l'auteur. Le dossier `bsd/` sert d'exemple complet. Pour démarrer, lire `bsd/BILAN_FINAL.md`.

L'utilisateur est un amateur, francophone, curieux, qui travaille avec l'IA en toute transparence. On lui répond en français. On lui explique les choses simplement quand il le demande. Les documents destinés aux spécialistes sont en anglais.

## 1. Règles non négociables

1. **Ouvrir chaque article avant de le citer.** Citer l'énoncé exact (entre guillemets) et l'endroit (numéro, page). Rien de mémoire présenté comme source. Si une référence n'a pas été ouverte, l'écrire explicitement (« non consulté ») et la lister à part.
2. **Étiqueter chaque énoncé** : ÉTABLI (lu dans la source), PROUVÉ (argument complet donné ici), DÉDUCTION (esquisse complète, à faire vérifier), CONFIRMÉ (par l'auteur concerné), CONJECTURE, SPÉCULATION, OUVERT, NON VÉRIFIÉ.
3. **Ne jamais annoncer une preuve.** Si une route semble marcher : écrire la preuve complète, puis la liste des pas non justifiés, puis chercher un contre-exemple, numérique si possible. Un chiffre (« 78,6 % ») se présente toujours comme conditionnel, avec ses hypothèses.
4. **Relecture adverse avant de rendre** (voir §4).
5. **S'arrêter sur un sujet si deux étapes de suite n'apportent rien**, et passer au suivant.
6. **Ne rien envoyer hors du dépôt.** Mails, dépôts arXiv, contacts : on rédige des brouillons, c'est l'utilisateur qui envoie.
7. **Committer et pousser après chaque étape significative.** Les scripts sont versionnés avec leurs résultats (`scripts/`, `results/`).
8. **Corriger ouvertement ses erreurs.** Exemples vécus :
   - « S_A indépendant des séries principales » : faux pour le rang 1 ;
   - « l'argument de cohérence favorise (L2) » : faux ;
   - « RH n'apporte presque rien à BSD » : faux dans sa forme forte (Fiorilli).
   
   Les dire tout de suite, sans minimiser.

## 2. Déroulé type d'une recherche

**Phase 0 : cadrage.**
- Lire les notes existantes, et le fichier de mémoire s'il y en a.
- Formuler la question en une phrase.
- Trouver le chiffre ou l'énoncé visé dans la littérature. Exemple : BSZ §4 annonçait déjà 79,7 % si le cas supersingulier était traité.

**Phase 1 : localiser l'obstacle exactement.**
- Relire **toute la chaîne de preuve**, énoncé par énoncé, et noter chaque endroit où l'hypothèse gênante est utilisée. Exemple : « N sans facteur carré » n'intervenait qu'à deux endroits (A et B). BSTW le disaient eux-mêmes en note de bas de page.
- Chercher (grep) toutes les occurrences de l'hypothèse dans chaque article de la chaîne.
- Séparer les problèmes indépendants (A, B…) et le raccord entre eux.

**Phase 2 : littérature.**
- Télécharger depuis arXiv (`curl -sL https://arxiv.org/pdf/ID`), extraire avec `pdftotext`, chercher avec `grep -n`. Quand les formules sont illisibles dans le texte extrait, regarder **l'image de la page** (`pdftoppm`).
- Beaucoup d'éditeurs (Springer, Cambridge, MSP, GDZ, pages perso) sont bloqués depuis la session. Donner alors à l'utilisateur la **référence exacte** (auteurs, titre, revue, volume, pages, DOI) : il les télécharge et les dépose dans la conversation. Vérifier que le fichier reçu est le bon : premières lignes, titre, auteurs.
- **Vérifier la version publiée** quand on critique un article : elle peut différer de l'arXiv. Exemple : CLW publiée, condition (4) p. 39, inchangée.
- Chercher sur le web : erratum, travaux concurrents, amélioration déjà faite. En faire une passe dédiée avant de dire qu'un résultat est nouveau.
- Quand une référence clé est introuvable, chercher un **texte ouvert qui en cite le contenu exact**. Exemple : la définition « minimally ramified » trouvée dans Kim–Ota, Déf. 3.5, au lieu de Diamond 1997a.

**Phase 3 : calcul local et preuves.**
- Réduire chaque problème à un énoncé explicite et vérifiable.
- **Préférer un argument structurel à un calcul cellule par cellule.** Exemples :
  - invariance de l'intégrale + projection isotypique + théorie des formes nouvelles (Casselman) ⇒ annulation (Prop. V) ;
  - support dans le modèle de Kirillov ⇒ seule la double classe triviale contribue (Prop. R′).
- Chercher le critère général derrière un cas particulier (« le type de f_θ ⊗ f_h doit exister dans π au bon niveau »).
- Relire les **définitions exactes** des vecteurs et des conventions (orientation K₀ vs K₀ᵀ, indices 1/2, normalisations) sur les images des pages. Ce sont elles qui décident.

**Phase 4 : vérification numérique** (voir §3).

**Phase 5 : relecture adverse en tours successifs** (voir §4).

**Phase 6 : chiffrage.**
- Un script versionné, avec la formule explicite et la source de chaque constante.
- Toujours deux scénarios : **prudent** (on exclut tout ce qui n'est pas couvert) et **optimiste** (ce qu'on récupérerait avec tel ingrédient manquant).
- Calculer les densités locales par énumération exacte des cellules (A, B) mod ℓ^k avec PARI (cypari), avec un contrôle de stabilité : relèvements aléatoires, et k plus grand.

**Phase 7 : rédaction et diffusion** (voir §5).

## 3. Vérifications numériques

- **Au moins deux méthodes indépendantes** pour tout résultat surprenant. Exemple pour le Lemme 8.14 : intégration dans la carte n⁻ de B\G, somme exacte sur GL₂(ℤ/27), puis formule analytique. Elles doivent concorder exactement.
- Petits premiers (ℓ = 2, 3) : arithmétique exacte (`fractions.Fraction`), caractères modélisés modulo ℓ^M.
- Tester **les deux modèles** (induit et Kirillov) quand une preuve passe par l'un d'eux.
- Attention aux appariements : pour une induite non unitaire, il faut l'appariement avec la **contragrédiente**, pas ∫ f f̄. Une erreur de ce type a fait échouer un test Steinberg à tort.
- Prévoir l'ordre de grandeur de l'erreur de troncature et le comparer aux résidus.
- Si un test échoue : vérifier d'abord le test (définitions, normalisation), puis seulement conclure.
- Lancer les calculs longs en arrière-plan. En lancer une version courte en parallèle pour avoir un résultat utilisable vite.

## 4. Relecture adverse

- Écrire comme un rapporteur hostile : objections numérotées, gravité **C** (critique), **I** (importante) ou **M** (mineure), et pour chacune une piste pour la régler.
- Traiter chaque objection, avec l'un de ces statuts : réglée, caduque, réparée, en partie réglée, héritée (le même point existe dans la littérature publiée), ouverte.
- Refaire un tour complet sur **tout** ce qui a été produit, y compris les réparations et le chiffrage. S'arrêter quand un tour ne produit plus d'objection critique propre au travail.
- Questions qui ont été utiles :
  - « Le résultat dépend-il d'une lecture des conventions ? »
  - « Le cas publié est-il touché aussi ? »
  - « Le chiffre utilise-t-il un ingrédient non vérifié ? »
  - « Le rang 1 a-t-il besoin d'autre chose que le rang 0 ? »
  - « La définition standard (minimalité, etc.) coïncide-t-elle avec celle que j'utilise ? »
  - « Le premier auxiliaire ou la tordue posent-ils le même problème ? »
- Créditer ce qui n'est pas de nous, dans une section dédiée.

## 5. Rédaction et diffusion

- **Notes de travail** : en français, en Markdown, dans `lit/`. Une note par sujet, datée, avec les sources ouvertes listées en tête.
- **Documents pour spécialistes** : en anglais, en LaTeX `amsart` (style des articles du domaine), compilés en PDF. `pdflatex` s'installe avec `apt-get install texlive-latex-recommended texlive-latex-extra texlive-fonts-recommended texlive-science lmodern`. Trois niveaux :
  1. **Synthèse de recherche** (4-6 p.) : question, obstacle (schéma TikZ), problèmes détaillés, chemin de recherche en étapes (impasses comprises), tableau des résultats avec statut, scénarios chiffrés, questions précises. C'est le document à envoyer en premier.
  2. **Note « ce qui est nouveau »** : uniquement les apports nouveaux, avec les preuves et une section « ce qui n'est pas de nous ».
  3. **Rapport complet**, avec les annexes numériques.
- Une version française de la synthèse pour l'utilisateur, avec un **petit lexique**.
- Vérifier le rendu : convertir les pages en PNG et les regarder, corriger les débordements.
- **Contact** :
  - d'abord l'auteur du travail critiqué, en privé, par courtoisie ;
  - puis les coauteurs, puis les spécialistes du sujet ;
  - mail court, ton prudent (« we believe we noticed »), transparence sur l'usage de l'IA, pas de pièce jointe au premier contact ;
  - demander l'autorisation avant de citer une réponse privée ;
  - vérifier l'adresse dans les articles les plus récents ;
  - laisser 2-3 semaines avant une relance unique.
- **arXiv** : un premier dépôt en maths demande un parrainage personnel (règle de décembre 2025). L'auteur est entièrement responsable du contenu généré par IA, et une fausse référence peut valoir un bannissement. Viser d'abord une courte note sur le résultat le plus solide.

## 6. Organisation du dépôt (modèle)

```
<sujet>/
  BILAN_FINAL.md          # état, résultats et statuts, questions, suite
  SPECIALISTES.md         # qui contacter, pourquoi, adresses (sources)
  RESEARCH_SUMMARY_EN.tex/pdf, RESEARCH_SUMMARY_FR.tex/pdf
  NEW_RESULTS_EN.tex/pdf, REPORT_EN.tex/pdf
  lit/                    # notes : problème A, problème B, raccord,
                          # relectures adverses 1..n, vérifications web, réponses reçues
  scripts/                # un script par vérification, commentaire en tête
  results/                # sorties JSON/TXT des scripts
```

## 7. Pièges rencontrés

- Une **annonce médiatique** (ex. « Anthropic résout RH ») n'est pas une source. Chercher la portée exacte vérifiée et le texte original, sans s'avancer.
- Un **agent** (sous-tâche) qui a lu un article ne remplace pas une lecture directe pour une citation.
- La **mémoire** du modèle sur un énoncé ou une page est souvent approximative : toujours relire.
- Un « Yes you are right » d'un auteur répond aux questions posées, pas aux autres. Ne pas sur-interpréter.
- Les politesses mathématiques comptent : signaler une erreur à l'auteur d'abord, avec prudence.
