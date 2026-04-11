# 🧩 Maze Game — Basics & Sensors

**Niveau / Level:** Débutants complets / Complete beginners
**Durée / Duration:** 2 × 1h30
**Outil / Tool:** Scratch

---

## 🕒 Session 1 — Movement & Collision Basics

**Objectif :** Déplacer un personnage et l'empêcher de traverser les murs.
**Goal:** Move a character and block movement with walls.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Intro : montrer un vrai maze game, poser la question *"Comment le jeu sait que tu touches un mur ?"* / Show a real maze game, ask *"How does the game know you're touching a wall?"* |
| 15 min | Explication : les touches directionnelles + `avancer de X pas` / Directional keys + `move X steps` |
| 25 min | Codage guidé : déplacement dans les 4 directions. / Guided coding: movement in all 4 directions. |
| 25 min | Codage guidé : détection de collision + logique "reculer". / Guided coding: wall collision + "move back" logic. |
| 15 min | Codage autonome : tester et ajuster la vitesse. / Independent coding: test and adjust speed. |

### 📚 Concepts enseignés / Concepts taught
- **Arrow key input** — `si touche [flèche droite]` / `if key [right arrow] pressed`
- **Move steps** — `avancer de X pas` / `move X steps` — l'unité de déplacement / the movement unit
- **Wall collision** — `si touching color [mur]` / `if touching color [wall]`
- **"Move back" logic** — reculer du même nombre de pas pour bloquer / move back the same steps to block movement

### 🛠 Ce que les élèves construisent / Students build
- Un sprite qui se déplace dans les 4 directions / A sprite moving in 4 directions
- Un labyrinthe simple dessiné à la main dans Scratch / A simple maze hand-drawn in Scratch
- Une collision qui bloque le personnage sur les murs / Collision that stops the character at walls

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Qu'est-ce qui se passe si tu avances de 10 pas et que le mur est à 5 pas ? »*
> Laisser répondre → *« Tu passes à travers ! Donc après chaque mouvement, on vérifie — et si on touche, on recule exactement du même nombre de pas. »*
>
> 🇬🇧 *"What happens if you move 10 steps but the wall is only 5 steps away?"*
> Let them answer → *"You go through it! So after every move, we check — and if we're touching, we move back the exact same amount."*

> 🇫🇷 Sur la vitesse : *« Plus vous avancez de pas à chaque fois, plus votre perso est rapide — mais aussi plus il risque de sauter par-dessus un mur fin. »*
>
> 🇬🇧 On speed: *"The more steps you move each time, the faster your character — but also the more likely it is to skip right through a thin wall."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Vitesse trop élevée → le sprite "saute" par-dessus les murs / 🇬🇧 Speed too high → sprite "skips" through walls
- 🇫🇷 Oubli de réinitialiser la position au démarrage → le sprite commence n'importe où / 🇬🇧 Forgetting to reset position on start → sprite begins anywhere
- 🇫🇷 Collision codée sans le "reculer" → le perso se bloque dans le mur / 🇬🇧 Collision coded without "move back" → character gets stuck inside the wall

### 💡 Concept difficile / Hard concept
**Pourquoi la logique "reculer" ? / Why "move back" logic?**

> 🇫🇷 *« Scratch ne sait pas où est le mur exactement — il sait juste qu'il y a une collision après le mouvement. Donc on fait : avancer → vérifier → si touche, reculer. C'est une boucle de correction. »*
>
> 🇬🇧 *"Scratch doesn't know exactly where the wall is — it only knows there's a collision after the move. So we do: move → check → if touching, move back. It's a correction loop."*

> 💡 🇫🇷 *« Si tu vas trop vite, tu peux "sauter" la détection. Commence avec 3-4 pas maximum. »*
> 🇬🇧 *"If you go too fast, you might skip the wall detection entirely. Start with 3-4 steps max."*

---

## 🕒 Session 2 — Obstacles & Win Condition

**Objectif :** Ajouter des pièges et une zone de victoire.
**Goal:** Add traps and a goal zone.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 1 + démo d'un élève. / Session 1 recap + student demo. |
| 15 min | Explication : zone de victoire — c'est juste une autre couleur à détecter. / Win zone — it's just another color to detect. |
| 25 min | Codage guidé : zone d'arrivée + message de victoire + reset. / Guided coding: finish area + win message + reset. |
| 20 min | Codage autonome : ajouter des obstacles. / Independent coding: add obstacles. |
| 20 min | Stretch + démo. / Stretch + demo. |

### 📚 Concepts enseignés / Concepts taught
- **Win zone detection** — `si touching color [vert]` → déclencher la victoire / trigger win condition
- **Game reset** — réinitialiser position + variables au redémarrage / reset position + variables on restart
- **Simple game loop** — `quand drapeau cliqué` remet tout à zéro / `when flag clicked` resets everything

### 🛠 Ce que les élèves construisent / Students build
- Des obstacles fixes (couleur danger) / Fixed obstacles (danger color)
- Une zone d'arrivée qui déclenche un écran de victoire / A finish zone that triggers a win screen
- Un reset complet au redémarrage / A full reset on restart

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment le jeu sait que tu as gagné ? C'est pareil que pour les murs — une couleur. On choisit une couleur pour 'gagner' et une autre pour 'mourir'. »*
>
> 🇬🇧 *"How does the game know you've won? Same as the walls — a color. We pick one color for 'win' and another for 'lose'."*

> 🇫🇷 Sur le reset : *« Si le jeu ne se remet pas à zéro, les élèves vont se retrouver bloqués à l'écran de fin. Tout ce qui change dans le jeu doit revenir à son état de départ quand on clique sur le drapeau. »*
>
> 🇬🇧 On reset: *"If the game doesn't reset, students get stuck on the end screen. Everything that changes during the game must go back to its starting state when the flag is clicked."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Zone de victoire trop petite → impossible à atteindre / 🇬🇧 Win zone too small → impossible to reach
- 🇫🇷 Oubli du reset → le sprite réapparaît sur la zone de fin directement / 🇬🇧 Missing reset → sprite respawns directly on the finish zone
- 🇫🇷 Obstacle de la même couleur que le mur → collision gérée pareil, pas de différenciation / 🇬🇧 Obstacle same color as wall → treated as wall, no distinction

### 🎯 Stretch challenge
- 🇫🇷 Ajouter un obstacle qui se déplace (clone ou sprite avec `rebondir si au bord`) / 🇬🇧 Add a moving obstacle (clone or sprite with `if on edge, bounce`)
- 🇫🇷 Ajouter un compteur de temps / 🇬🇧 Add a timer
- 🇫🇷 Plusieurs niveaux avec `envoyer message "niveau 2"` / 🇬🇧 Multiple levels using `broadcast "level 2"`
