# BSD en rang analytique 2 : ce qui est solide, ce qui est numérique, ce qui manque

Rapport du programme « Programme de recherche BSD pour Opus », session du 26 novembre 2026. Calculs : Python 3.13, PARI 2.15.4 (cypari 2.5.7), 4 cœurs, 15 Go. Tout est reproductible avec les scripts de `bsd/scripts/` (voir la section 7).

Étiquettes : **ÉTABLI** (référence ouverte dans cette session), **VÉRIFIÉ NUMÉRIQUEMENT** (script nommé), **CONDITIONNEL** (déduction rigoureuse à partir d'énoncés de la littérature dont je n'ai pas relu la preuve), **CONJECTURE**, **SPÉCULATION**.

## 1. Résumé

1. **Littérature.** Les trois pistes (Kolyvagin, Darmon–Rotger, Perrin-Riou) produisent des classes de **Selmer**, pas des points rationnels, et aucune ne relie une construction à L″(E, 1). Le verrou décrit dans le document est confirmé tel quel. Deux corrections au document : BCGS est une prépublication dont le cas inconditionnel dépend de deux autres prépublications, et arXiv 2601.16044 ne porte pas sur le comptage 97,78 % (qu'il cite en introduction). Détails : `lit/cartographie.md`.
2. **BSD p-adique en rang 2.** Sur 151 courbes de rang 2 (N < 10 000) et 433 couples (E, p), Ш_p ≡ 1 = Ш partout, sans aucun désaccord modulo p, avec 2 à 16 chiffres p-adiques d'accord. Pour les 433 couples, ord_T L_p ≤ 2 est démontré par une borne d'erreur exacte ; pour 429 d'entre eux (151 courbes sur 151), E[p] est irréductible, d'où, conditionnellement à Wan (via BCGS) et au théorème de contrôle de Mazur, Ш(E/ℚ)[p^∞] fini.
3. **Ш non trivial en rang 2.** Sur les 42 courbes de rang 2 avec Ш = 4 et N < 500 000 : rang = 2 démontré, Ш(E)[2^∞] ≅ (ℤ/2)² démontré par 2-descente, Ш analytique = 4,000000 par deux voies, et dans les 42 cas une unique courbe 2-isogène E′ avec Ш(E′) = 1 et Ш(E′)[2] = 0.
4. **Conjectures.** Trois énoncés testés ; un est soutenu sur 151 courbes, un sur 3 millions de courbes (avec un contre-exemple à sa forme naïve, trouvé dans la LMFDB), un est réfuté hors du rang 2 (352 contre-exemples en rang 1).

## 1 bis. Barre d'évaluation

**Référence.** Note d'Anthropic du 10 août 2026 (anthropic.com/research/riemann-zeta, ouverte le 26 novembre 2026) : une version de recherche de Claude a fait passer le minorant de la proportion des zéros non triviaux de ζ situés sur la droite critique de 41,6 % à 67,2 %. Le résultat a été validé par deux mathématiciens d'Anthropic, relu par B. Conrey et D. Goldston, et formalisé en Lean. Ce chiffre sert de barre parce qu'il est démontré, qu'il porte sur **tous** les zéros et qu'il était bloqué depuis longtemps.

**Équivalent BSD.** Bhargava–Skinner–Zhang (arXiv 1407.1826, résumé ouvert) : plus de 66 % des courbes, classées par hauteur, vérifient la partie « rang » de BSD.

| Niveau | Critère | Ce programme |
|---|---|---|
| A. Densité démontrée | faire monter une proportion démontrée sur toutes les courbes (66 % de BSZ, ou proportion de rang 2 avec Ш[p^∞] fini) | **aucun progrès** |
| B. Démontré courbe par courbe | rang = 2 | 151/151 (2-descente, r = R = 2) et 42/42 |
| | Ш(E)[p^∞] fini pour au moins un p | 151/151, CONDITIONNEL (Wan via BCGS, contrôle de Mazur) |
| | Ш(E)[2^∞] déterminé | 42/42 courbes à Ш = 4 : (ℤ/2)² |
| | BSD complète (formule exacte) | **0/193** |
| C. Vérifié numériquement | accord avec les prédictions | 433/433 couples p-adiques ; 42/42 Ш = 4,000000 |

Jugé à cette barre, le travail est aux niveaux B et C. Il ne déplace aucun chiffre comparable au 67,2 %, et le niveau B reproduit en principe une méthode connue.

## 2. Mission 1 : cartographie (synthèse)

| Piste | Ce qui est prouvé | Hypothèses principales | Ce que ça ne donne pas |
|---|---|---|---|
| Kolyvagin (Zhang 2014 ; Sweeting 2012.11771 ; BCGS 2312.09301) | classes κ_n non toutes nulles ; max(r⁺, r⁻) = ord(κ) + 1 | p bon ordinaire, Heegner ; BCGS : p décomposé dans K, conjecture principale anticyclotomique (connue si p > 3 et E[p] irréductible) | ni points rationnels, ni lien avec L″(E, 1) |
| Darmon–Rotger (Castella–Hsieh 1809.09066 ; Castella 2204.09608) | κ ≠ 0 ⇒ dim Sel(ℚ, V_pE) = 2 ; réciproques partielles | forme auxiliaire thêta d'un caractère d'anneau de classes ; ρ̄ irréductible ; cas CM complet chez Castella (p ≥ 5) | des classes de Selmer, pas des points (Castella–Hsieh, Question 1.1) |
| Perrin-Riou (BDV) | log(res_p ζ^Kato) = log²(P), P d'ordre infini ⇔ zéro simple | A semistable en p impair | en rang ≥ 2, P est de torsion : ζ^Kato est localement nul en p |

**SPÉCULATION.** Pour l'inégalité « rang ≤ ordre », l'outil disponible le plus direct n'est pas un système d'Euler nouveau : c'est la conjecture principale cyclotomique, déjà connue rationnellement quand E[p] est irréductible (BCGS, Thm 3.2.6, citant Wan). Elle ramène la borne sur le Selmer à un calcul de l'ordre de L_p en s = 0. La mission 2 exploite exactement cela, courbe par courbe ; ça ne donne rien de général sur L(E, s) complexe.

## 3. Mission 2 : BSD p-adique en rang 2

**Méthode.** `ellpadicL` et `mspadicinit` de PARI demandent O(N²(n+k)²p) mémoire (documentation PARI). Mesuré : débordement de 6 Go à N = 9003 même à précision 5³. J'ai donc programmé les sommes de Riemann de Mazur–Tate–Teitelbaum sur le seul symbole modulaire x⁺ de E (`scripts/mtt.gp`) :
μ(b + pⁿℤ_p) = α⁻ⁿ [b/pⁿ]⁺ − α⁻⁽ⁿ⁺¹⁾ [b/pⁿ⁻¹]⁺, avec α la racine unité de X² − a_pX + p.
Coût : pⁿ évaluations de `mseval`, ~80 µs pièce à N ≈ 9000. La seule limite mémoire rencontrée est `msfromell` : 2 Go ne suffisent pas pour 12 conducteurs très composés, 6 Go suffisent (voir Échecs).

**Calibration (VÉRIFIÉ NUMÉRIQUEMENT, `scripts/calib.py`).** Sur 389a, 433a, 37a et 11a, p = 5 et 7, les dérivées obtenues coïncident chiffre à chiffre avec `ellpadicL` de PARI à toute la précision de PARI.

**Prédiction testée (Mazur–Tate–Teitelbaum, p bon ordinaire, réduction non multiplicative déployée).**
(1 − 1/α)⁻² · L*_p = c_∞ · ∏c_v · #Ш · Reg_p / #E(ℚ)²_tors,
où L*_p est le coefficient de s² (variable cyclotomique, T = (1+p)^s − 1). Le facteur c_∞ (composantes réelles) vient de ce que x⁺ est normalisé par Ω⁺ = `E.omega[1]` ; c'est le « facteur 2 » observé à la session précédente.

**Échantillon.** 150 courbes de rang 2 tirées au hasard (graine 20261126, `random.Random`) parmi les 1969 classes de rang 2 de conducteur < 10 000 (première courbe de chaque classe). 433a1 faisait partie du tirage ; 389a1 a été ajoutée, soit 151 courbes. Pour chaque courbe, les 3 premiers premiers bons ordinaires parmi 3, 5, 7, 11, 13, aux niveaux n = 11, 8, 6, 5, 4 respectivement, et au niveau n − 1 pour estimer la précision.

**Résultats (VÉRIFIÉ NUMÉRIQUEMENT, `results/m2_padic_rank2.jsonl`).**
| p | couples | chiffres d'accord avec Ш = 1 (min / médiane / max) | désaccord mod p | p anormal (a_p ≡ 1) |
|---|---|---|---|---|
| 3 | 66 | 7 / 10 / 16 | 0 | 46 |
| 5 | 98 | 5 / 7 / 9 | 0 | 19 |
| 7 | 119 | 2 / 5 / 7 | 0 | 5 |
| 11 | 96 | 3 / 4 / 6 | 0 | 3 |
| 13 | 54 | 2 / 3 / 4 | 0 | 0 |

Total : 433 couples sur 151 courbes, conducteurs de 389 à 9936. 75 courbes ont au moins un p avec ≥ 8 chiffres d'accord. Côté réel : Ш analytique = 1 par les deux voies pour les 151 courbes, égal à la colonne de Cremona, régulateurs égaux à ceux de Cremona à 10⁻⁸ près (relatif). Le régulateur p-adique est non nul pour les 433 couples (conjecture de Schneider vérifiée numériquement dans ces cas).

**Certification de ord_T L_p ≤ 2 (CONDITIONNEL, `scripts/mission2_certify.py`).**
La somme de niveau n est l'image **exacte** de L_p dans Λ/ω_{n−1}, avec ω_{n−1} = (1+T)^{p^{n−1}} − 1. Comme L_p ∈ D⁻¹Λ (D = dénominateur du symbole x⁺), l'erreur sur les coefficients c_0, c_1, c_2 de T⁰, T¹, T² est de valuation ≥ n − 1 − v_p(D), car les coefficients binomiaux C(p^{n−1}, k) ont valuation n − 1 pour k = 1, 2 et p impair. Si v_p(c_2) est strictement en dessous, le vrai c_2 est non nul, donc ord_T L_p ≤ 2. Ceci ne dépend que d'arithmétique rationnelle exacte (le vecteur propre x⁺ est exact) et ne dépend pas de la normalisation des périodes.
Ensuite, si E[p] est irréductible, la conjecture principale rationnelle (BCGS Thm 3.2.6(ii), qui l'attribue à Wan) donne ord_T char X(E/ℚ_∞) = ord_T L_p ≤ 2. Le théorème de contrôle de Mazur (manuel, non rouvert ici) donne corang Sel_{p^∞}(E/ℚ) ≤ rang de X/TX ≤ ord_T char X. Avec deux points indépendants, on obtient rang E(ℚ) = 2 et **Ш(E/ℚ)[p^∞] fini**.
Résultat (`results/m2_certify*.jsonl`) : la borne est satisfaite pour les **433 couples sur 433**. Dénominateurs D : 1 (67 courbes), 2 (83), 6 (1), donc v_p(D) = 0 pour p ≥ 5, et pour p = 3 seulement sur une courbe. E[p] est irréductible pour 429 couples ; les 4 exceptions sont p = 3 pour 1862a1, 2666e1, 2738d1 et 6293f1 (isogénie de degré 3). Les 151 courbes ont toutes au moins un premier certifié avec E[p] irréductible.
Je crois que cet argument est celui de Stein–Wuthrich, mais je n'ai pas pu ouvrir leur article : ce n'est donc pas une source ici. Le résultat n'est pas nouveau en principe. Ce qui est fait ici, c'est son exécution sur cet échantillon avec un code indépendant de Sage.

**Limites.**
- **Biais de l'échantillon.** Toutes les courbes de rang 2 de conducteur < 194 040 ont Ш = 1 (mission 3). Le test confirme donc Ш_p = 1, mais ne peut pas détecter une erreur de formule qui ne se manifesterait qu'avec Ш non trivial. Tentative de lever ce biais sur 194766c4 (rang 2, Ш = 4, p = 5 et 7) : **échec**. `msfromell` dépasse la pile PARI de 10 Go à N = 194 766, sur une machine de 15 Go (`results/m3_padic_194766c4_echec.log`). Le test p-adique d'un Ш non trivial en rang 2 reste à faire : il faut soit plus de mémoire, soit un calcul du seul symbole de E qui évite l'espace complet de niveau N.
- **Précision.** L'accord entre niveaux n et n − 1 surestime parfois la précision (3328f1, p = 7 : 8 chiffres d'accord entre niveaux, 5 avec la valeur 1). Je rapporte donc l'accord avec Ш = 1, pas l'accord entre niveaux.
- **Cible ≥ 8 chiffres p-adiques.** Atteinte pour p = 3 seulement. À p = 5, 7, 11, 13, la limite est le coût en pⁿ.
- **Échecs.** 12 courbes sur 151 ont fait déborder la pile de 2 Go de PARI dans `msfromell` (conducteurs très composés, de 7668 à 9390). Elles sont comptées comme échecs dans la première passe (`results/m2_padic_rank2.jsonl`), puis relancées avec 6 Go (`scripts/mission2_rerun.py`, `results/m2_padic_rank2_pass2.jsonl`) : les 12 passent, avec 30 couples, tous en accord avec Ш = 1.

## 4. Mission 3 : Ш = 4 en rang 2

**Données.** Fichiers `allbsd` de Cremona (dépôt ecdata), conducteurs < 500 000 : 348 672 courbes de rang 2, dont 42 avec Ш = 4, aucune avec Ш > 4. 9487 courbes de rang 3, toutes avec Ш = 1.

**Recalcul (VÉRIFIÉ NUMÉRIQUEMENT, `scripts/mission3_sha4.py`, `results/m3_sha4_rank2.jsonl`).** Pour les 42 :
- modèle minimal et conducteur confirmés ; L″(E, 1)/2 de PARI égal à celui de Cremona à 4·10⁻¹⁵ près (relatif) ;
- générateurs trouvés par notre propre recherche (`ellrank`, effort 4), saturés jusqu'à 200, régulateur égal à celui de Cremona ;
- Ш analytique = 4,000000 par les deux voies (`ellbsd` ; Ω, Tamagawa, torsion à la main), écart < 10⁻¹².

**Démontré par 2-descente (ÉTABLI au sens du calcul, sous réserve de la correction de `ellrank` ; formule C = T + R + S de la documentation PARI).** Pour chacune des 42 courbes : borne supérieure de rang R = 2 et deux points indépendants, donc rang E(ℚ) = 2 ; dim Ш(E)[2] = S = 2 ; et s = rang de Ш[2]/2Ш[4] = 2 = S, d'où Ш[4] = Ш[2] et **Ш(E)[2^∞] ≅ (ℤ/2)²**. La partie impaire de Ш reste non démontrée (prédite triviale par Ш analytique = 4).

**Isogénie (VÉRIFIÉ NUMÉRIQUEMENT).** Chacune des 42 courbes a exactement une courbe 2-isogène E′ (`ellisomat`). Les points de E poussés par l'isogénie sont sur E′ ; après saturation, Ш analytique(E′) = 1,000000. La 2-descente sur E′ donne r = R = 2 et s = 0, donc Ш(E′)[2] = 0. Le quotient Ш(E)/Ш(E′) = 4 est compensé par Ω, Tamagawa, torsion et régulateurs : ∏c(E′)/∏c(E) ∈ {8, 32, 64}, torsion (2, 4) ou (4, 8), Reg(E′)/Reg(E) ∈ {1/4, 1}. Exemple, 194040co6 : torsion 2, ∏c = 4, Ш = 4 ; son voisin 194040co4 : torsion 4, ∏c = 128, Ш = 1.

| Courbe | tors | ∏c | Ш (2 voies) | s(E) | E′ : ∏c, tors, Ш, s |
|---|---|---|---|---|---|
| 194040co6 | 2 | 4 | 4,000000 / 4,000000 | 2 | 128, 4, 1,000000, 0 |
| 194766c4 | 2 | 2 | 4,000000 / 4,000000 | 2 | 64, 4, 1,000000, 0 |
| 226005g3 | 4 | 8 | 4,000000 / 4,000000 | 2 | 64, 8, 1,000000, 0 |
| 226920a6 | 2 | 2 | 4,000000 / 4,000000 | 2 | 64, 4, 1,000000, 0 |
| 245310bs8 | 2 | 8 | 4,000000 / 4,000000 | 2 | 256, 4, 1,000000, 0 |

(Les 37 autres lignes sont dans le fichier de résultats ; aucune n'a de valeur différente de 4, 2, 1 ou 0 dans les colonnes Ш et s.)

## 5. Mission 4 : conjectures

**Conjecture 1 (Mazur–Tate–Teitelbaum et Schneider, rang 2 ; conjecture connue, pas nouvelle).** Pour E/ℚ de rang 2 et p ≥ 3 bon ordinaire, ord_T L_p(E, T) = 2, Reg_p ≠ 0, et (1 − 1/α)⁻² L*_p = c_∞ ∏c_v #Ш Reg_p / #tors².
Test : 433 couples (E, p) sur 151 courbes, tous en accord (section 3), Reg_p ≠ 0 dans les 433 cas, ord_T L_p ≤ 2 démontré dans les 433 cas. L'égalité ord_T L_p = 2 est CONDITIONNELLE : elle suit de la conjecture principale rationnelle et du corang ≥ 2 du Selmer (deux points indépendants). Échantillon biaisé : Ш = 1 partout.

**Conjecture 2 (effet de la 2-torsion, nouvelle sous cette forme ; `scripts/stats_sha_torsion.py`).** Notons ρ_r(X) le rapport entre la proportion de Ш ≠ 1 chez les courbes de rang r à torsion paire et la même proportion à torsion impaire, pour N < X. Alors ρ_r(X) croît avec r pour X fixé grand.
Données (N < 500 000, 3 064 704 courbes) :

| rang | torsion paire : Ш ≠ 1 | torsion impaire : Ш ≠ 1 | ρ |
|---|---|---|---|
| 0 | 134 285 / 555 350 (24,2 %) | 88 637 / 615 526 (14,4 %) | 1,7 |
| 1 | 16 896 / 663 782 (2,55 %) | 3 667 / 871 887 (0,42 %) | 6,1 |
| 2 | 42 / 108 558 (0,039 %) | **0 / 240 114** | ∞ ; ρ ≥ 31 environ (borne de Poisson à 95 %, en traitant la proportion à torsion paire comme exacte) |
| 3 | 0 / 986 | 0 / 8 501 | indéterminé |

Si le rang 2 suivait le rapport du rang 1 (6,1), on attendrait ≈ 15 courbes à torsion impaire et Ш ≠ 1 ; en observer 0 a une probabilité ≈ e⁻¹⁵ sous un modèle de Poisson.
**Contre-exemple à la forme naïve** (« en rang 2, Ш ≠ 1 implique de la 2-torsion ») : la LMFDB contient 53295337.a1, de rang 2, de torsion triviale et avec Ш = 9, et d'autres à conducteur premier > 5·10⁷ (requête API, avant que le site n'impose un CAPTCHA). La conjecture 2 porte donc sur des fréquences, pas sur une implication.
**Biais possible non contrôlé :** la 2-torsion et Ш sont tous deux corrélés au conducteur et à la taille du régulateur ; l'effet pourrait venir de ce que les courbes à 2-torsion atteignent un grand Ш analytique à plus petit conducteur.

**Conjecture 3 (absorption par 2-isogénie ; réfutée hors du rang 2).** Énoncé testé : si E a de la 2-torsion et un Ш pair, sa classe d'isogénie contient une courbe avec v_2(Ш) plus petit (`scripts/test_absorption.py`).
- rang 0 : 80 546 / 106 326 (75,8 %) ; contre-exemple 1443d (deux courbes, Ш = 4 toutes deux) ;
- rang 1 : 16 122 / 16 474 (97,9 %) ; **352 contre-exemples**, dont 103525b ;
- rang 2 : 42 / 42.
Au taux du rang 1, on attendrait 0,9 contre-exemple parmi 42 : l'absence observée n'est **pas** significative (probabilité ≈ 0,4). La question reste ouverte en rang 2 ; il faudrait des courbes de rang 2 avec Ш[2] ≠ 0 au-delà de 500 000.

## 6. Relecture adverse

Ce qu'un rapporteur hostile attaquerait, et la réponse :

1. **« Votre fonction L p-adique maison est fausse. »** Elle coïncide avec `ellpadicL` chiffre à chiffre là où celui-ci tourne. Au-delà, l'indicateur est Ш_p ≡ 1 mod p^k pour 433 couples : un code faux donnerait une unité p-adique quelconque, pas 1 à 3–16 chiffres. Ça ne prouve pas l'absence d'un facteur constant égal à 1 modulo p partout ; le calibrage sur petits conducteurs, où ce facteur serait visible, l'exclut.
2. **« La précision est surestimée. »** Oui pour l'accord entre niveaux ; d'où le choix de l'accord avec 1. La certification utilise une borne démontrée (n − 1 − v_p(D)), pas l'accord.
3. **« La certification repose sur des boîtes noires. »** Oui : le théorème de contrôle de Mazur (non rouvert), la conjecture principale rationnelle telle qu'énoncée par BCGS (preuve attribuée à Wan, non ouverte), et la correction de PARI. C'est pourquoi elle est étiquetée CONDITIONNEL.
4. **« Ш(E)[2^∞] ≅ (ℤ/2)² dépend de `ellrank`. »** Oui, sans second logiciel indépendant (mwrank n'est pas installé). Recoupements : Ш analytique = 4 calculé indépendamment de la descente, et Ш(E′)[2] = 0 du côté isogène, cohérent avec le quotient 4 de la formule de Cassels.
5. **« Le rang analytique 2 n'est que numérique. »** Le signe est +1 pour les 193 courbes (`ellrootno`, vérifié), ce qui annule les dérivées impaires. L(E, 1) = 0 est numérique dans la mission 3, exact dans la mission 2 (symbole modulaire x⁺(0) = 0). L″(E, 1)/2 est loin du bruit : au moins 0,759 (389a1) dans la mission 2, au moins 7,5 dans la mission 3, pour une précision de 38 chiffres.
6. **« Les conjectures 2 et 3 sont de la statistique de données biaisées. »** Oui, et c'est dit. La conjecture 3 est présentée comme réfutée hors du rang 2.
7. **« Rien de tout cela n'approche une preuve de BSD en rang 2. »** Exact. Le programme localise le verrou et produit des vérifications. Aucune preuve n'est annoncée.

## 7. Reproduire

```
pip install cypari
bash bsd/scripts/fetch_allbsd.sh            # depuis bsd/data, 309 Mo
python3 bsd/scripts/calib.py                # calibration contre ellpadicL
python3 bsd/scripts/mission2_padic.py bsd/results/m2_padic_rank2.jsonl 150 20261126
python3 bsd/scripts/mission2_certify.py bsd/results/m2_padic_rank2.jsonl bsd/results/m2_certify.jsonl
python3 bsd/scripts/analyse_m2.py bsd/results/m2_padic_rank2.jsonl bsd/results/m2_certify.jsonl
python3 bsd/scripts/mission3_sha4.py bsd/results/m3_sha4_rank2.jsonl
python3 bsd/scripts/stats_sha_torsion.py ; python3 bsd/scripts/test_absorption.py
```
Les fichiers de données (`bsd/data/`) et les PDF (`bsd/lit/raw/`) ne sont pas versionnés.
