# NEON RONIN // HARDCORE

Mini-jeu navigateur dans l'esprit de Katana Zero : néon synthwave, one-hit-kill,
slow-mo, deflect de balles — en version **hardcore** (une mort = retour au SECTOR 01,
run chronométré, combos, records en localStorage).

## Lancer
Ouvrir `index.html` dans un navigateur (aucun serveur requis).

## Contrôles
| Action | Touche |
|---|---|
| Bouger | A/D ou ←/→ |
| Sauter | ESPACE / W / ↑ |
| Dash | SHIFT / K |
| Entailler (dévie les balles) | J / X / clic gauche |
| Slow-mo (maintenir) | L / clic droit |
| Relancer le run | R |
| Pause | ÉCHAP |
| Musique on/off | M |

## Règles
- Toi et les ennemis mourez en un coup.
- Atteins la porte rose pour valider le secteur (5 secteurs).
- Toute mort relance le run depuis le début. Le chrono ne tourne que en vie.
- Les balles déviées par ton sabre retournent contre les ennemis.
- Le meter de slow-mo se recharge lentement, et plus vite à chaque kill/deflect.

## Sprites
Le personnage est animé via la planche `assets/hero.png` (grille 4x3, cellules 256x256, fond transparent) :
- rangée 0 : idle (4 frames) · rangée 1 : course, dash, aura slow-mo, saut · rangée 2 : entaille horizontale, mort/hurt, entaille verticale, pose mur
Les sprites font face à droite ; le jeu les retourne horizontalement selon la direction.
Si l'image n'est pas chargée, le jeu retombe sur un rendu vectoriel de secours.

## 13 secteurs
Chaque secteur a son propre fond (`assets/bg/levelNN_*.jpg`, défilement parallaxe) et son thème de monstres (couleur + composition ennemis qui s'intensifie) :
CITY, APARTMENT, ALLEY, SEWERS, SUBWAY, PENTHOUSE, ZEN GARDEN, LAB, DOJO, DOCKS, TRAINYARD, NIGHTCLUB, OVERPASS.
Si un fond manque, le jeu retombe sur le décor procédural (skyline + soleil synthwave).
