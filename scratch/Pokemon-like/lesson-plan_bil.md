# 🧢 Pokémon-like Game

**Niveau / Level:** A déjà fait un projet Scratch / Has completed one Scratch project
**Durée / Duration:** 4 × 1h30
**Outil / Tool:** Scratch

> 📌 **Note prof / Instructor note:**
>
> 🇫🇷 **La démo fournie est intentionnellement complexe** — elle montre le potentiel complet du projet, pas ce que les élèves doivent reproduire. Il est fortement conseillé aux enseignants de **recoder une version simplifiée** adaptée à leur groupe avant la première session. Quelques pistes : réduire la taille de la carte, limiter le système de combat à une seule action, supprimer les animations avancées.
>
> 🇫🇷 **Sprites :** pas d'assets imposés — cherchez des sprites simples libres de droits (itch.io, OpenGameArt) ou faites dessiner les élèves directement dans Scratch.
>
> 🇫🇷 **Besoin d'aide ?** Si vous souhaitez une correction live simplifiée basée sur une version que j'ai réalisée avec mes propres élèves, vous pouvez me contacter directement.
>
> ---
>
> 🇬🇧 **The provided demo is intentionally complex** — it shows the full potential of the project, not what students are expected to reproduce. Teachers are strongly encouraged to **recode a simplified version** suited to their group before the first session. Some suggestions: reduce the map size, limit the battle system to a single action, remove advanced animations.
>
> 🇬🇧 **Sprites:** no assets imposed — look for simple free-to-use sprites (itch.io, OpenGameArt) or have students draw directly in Scratch.
>
> 🇬🇧 **Need help?** If you'd like a simplified live correction based on a version I built with my own students, feel free to reach out directly.

---

## 🕒 Session 1 — Movement & Map

**Objectif :** Le joueur se déplace sur une carte avec des collisions.
**Goal:** The player moves around a map with collisions.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Intro : montrer un vrai jeu Pokémon, identifier les mécaniques visibles. / Show a real Pokémon game, identify visible mechanics. |
| 15 min | Explication : tile movement — pourquoi se déplacer case par case plutôt que pixel par pixel. / Tile movement — why move tile by tile instead of pixel by pixel. |
| 30 min | Codage guidé : déplacement dans les 4 directions + collision avec les murs. / Guided coding: 4-direction movement + wall collision. |
| 25 min | Codage autonome : dessiner sa propre carte simple (3-4 zones). / Independent coding: draw their own simple map (3-4 zones). |
| 10 min | Démo + questions. / Demo + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Tile movement** — se déplacer d'un nombre fixe de pas à chaque pression / move a fixed number of steps per keypress — grille cohérente / consistent grid
- **Collisions** — `touching color` sur les murs de la carte / `touching color` on map walls — même logique que Maze Game mais appliquée à une carte / same logic as Maze Game but applied to a map
- **Camera/scroll** — déplacer le décor au lieu du sprite joueur / move the backdrop instead of the player sprite

### 🛠 Ce que les élèves construisent / Students build
- Un personnage joueur qui se déplace case par case / A player character that moves tile by tile
- Une carte dessinée dans Scratch avec zones bloquantes / A map drawn in Scratch with blocking zones
- Une illusion de caméra basique / A basic camera illusion

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Dans Pokémon, est-ce que le personnage glisse ou se déplace case par case ? »*
> Laisser observer → *« Case par case. Ça veut dire qu'à chaque fois qu'on appuie sur une touche, il avance exactement d'une case — pas plus, pas moins. »*
>
> 🇬🇧 *"In Pokémon, does the character slide or move tile by tile?"*
> Let them observe → *"Tile by tile. That means every time we press a key, it moves exactly one tile — no more, no less."*

> 🇫🇷 Sur le scroll : *« Qui bouge vraiment dans Pokémon — le personnage ou la carte ? »*
> Laisser répondre → *« La carte ! Le personnage reste souvent au centre de l'écran. »*
>
> 🇬🇧 On scroll: *"Who actually moves in Pokémon — the character or the map?"*
> Let them answer → *"The map! The character usually stays near the center of the screen."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Mouvement pixel par pixel → collisions imprécises et jeu qui "glisse" / 🇬🇧 Pixel-by-pixel movement → imprecise collisions and "sliding" feel
- 🇫🇷 Carte trop grande → performances dégradées dans Scratch / 🇬🇧 Map too large → degraded performance in Scratch
- 🇫🇷 Oubli de bloquer le mouvement diagonal / 🇬🇧 Forgetting to block diagonal movement

---

## 🕒 Session 2 — Interactions & Triggers

**Objectif :** Le joueur peut interagir avec des objets et des personnages sur la carte.
**Goal:** The player can interact with objects and characters on the map.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 1 + démo d'un élève. / Session 1 recap + student demo. |
| 15 min | Explication : qu'est-ce qu'un trigger ? Proximité vs collision vs touche. / What's a trigger? Proximity vs collision vs keypress. |
| 30 min | Codage guidé : PNJ avec dialogue déclenché par la touche espace. / Guided coding: NPC with dialogue triggered by spacebar. |
| 25 min | Codage autonome : ajouter un objet interactif (coffre, panneau…). / Independent coding: add an interactive object (chest, sign…). |
| 10 min | Démo + questions. / Demo + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Triggers** — `si touching [PNJ]` + `si touche [espace]` → déclencher un événement / `if touching [NPC]` + `if key [space]` → trigger an event
- **Dialogues** — séquence de `dire` + `attendre` contrôlée par `envoyer message` / sequence of `say` + `wait` controlled by `broadcast`
- **État basique** — variable `en_dialogue` pour bloquer le mouvement pendant une conversation / `in_dialogue` variable to block movement during conversation

### 🛠 Ce que les élèves construisent / Students build
- Au moins un PNJ avec 2-3 lignes de dialogue / At least one NPC with 2-3 lines of dialogue
- Un objet interactif sur la carte / An interactive object on the map
- Le mouvement bloqué pendant les interactions / Movement blocked during interactions

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment le jeu sait que vous voulez parler à quelqu'un ? Deux conditions doivent être vraies en même temps : vous êtes proche du PNJ ET vous appuyez sur une touche. »*
>
> 🇬🇧 *"How does the game know you want to talk to someone? Two conditions must be true at the same time: you're close to the NPC AND you press a key."*

> 🇫🇷 Sur le blocage du mouvement : *« Qu'est-ce qui se passe si le joueur peut se déplacer pendant un dialogue ? »*
> Laisser répondre → *« Il peut fuir la conversation ou déclencher d'autres événements. Donc on bloque tout avec une variable. »*
>
> 🇬🇧 On blocking movement: *"What happens if the player can move during a dialogue?"*
> Let them answer → *"They can walk away or trigger other events. So we lock everything with a variable."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Dialogue déclenché en boucle → oubli de vérifier que le dialogue n'est pas déjà en cours / 🇬🇧 Dialogue triggering on loop → missing check that dialogue isn't already running
- 🇫🇷 Mouvement non bloqué → joueur qui parle et marche en même temps / 🇬🇧 Movement not blocked → player talking and walking simultaneously
- 🇫🇷 Trigger trop sensible → déclenché sans que le joueur ait voulu interagir / 🇬🇧 Trigger too sensitive → fires without player intending to interact

---

## 🕒 Session 3 — Simple Battle System

**Objectif :** Déclencher un combat au tour par tour basique.
**Goal:** Trigger a basic turn-based battle.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 2 + discussion : *"Comment Pokémon gère les combats ?"* / Session 2 recap + discussion: *"How does Pokémon handle battles?"* |
| 20 min | Explication : la notion d'état — mode carte vs mode combat. / State concept — map mode vs battle mode. |
| 30 min | Codage guidé : écran de combat + HP + attaque basique. / Guided coding: battle screen + HP + basic attack. |
| 20 min | Codage autonome : ajouter une deuxième action (défense ou soin). / Independent coding: add a second action (defense or heal). |
| 10 min | Démo + questions. / Demo + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Simple fight logic** — variable `HP` diminuée à chaque attaque / `HP` variable decreased each attack
- **Turn structure** — variable `tour` qui alterne entre joueur et ennemi / `turn` variable alternating between player and enemy
- **Battle screen** — cacher les sprites de la carte, montrer les sprites de combat / hide map sprites, show battle sprites

### 🛠 Ce que les élèves construisent / Students build
- Un écran de combat séparé de la carte / A battle screen separate from the map
- Un système HP joueur + ennemi / Player + enemy HP system
- Au moins deux actions disponibles (attaque + une autre) / At least two available actions (attack + one other)

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Le jeu Pokémon a deux "modes" : explorer la carte, et se battre. Ces deux modes ne peuvent pas être actifs en même temps. Comment on dit au jeu dans quel mode on est ? »*
> Laisser répondre → *« Une variable. `mode = carte` ou `mode = combat`. »*
>
> 🇬🇧 *"Pokémon has two 'modes': exploring the map, and battling. These two modes can't be active at the same time. How do we tell the game which mode we're in?"*
> Let them answer → *"A variable. `mode = map` or `mode = battle`."*

> 🇫🇷 Sur les HP : *« Les points de vie c'est juste un nombre. Attaquer = soustraire un nombre. Gagner = ce nombre tombe à 0 chez l'ennemi. »*
>
> 🇬🇧 On HP: *"Hit points are just a number. Attacking = subtracting a number. Winning = that number hits 0 on the enemy."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Sprites de la carte visibles pendant le combat / 🇬🇧 Map sprites still visible during battle
- 🇫🇷 HP qui descend en dessous de 0 → ajouter une condition `si HP < 0, mettre HP à 0` / 🇬🇧 HP going below 0 → add `if HP < 0, set HP to 0`
- 🇫🇷 Les deux joueurs attaquent en même temps → variable `tour` oubliée / 🇬🇧 Both sides attack simultaneously → `turn` variable forgotten

### 💡 Concept difficile / Hard concept
**Gestion des états / Managing states (map vs battle)**

> 🇫🇷 C'est le concept le plus difficile de tout le projet. Un état, c'est une variable qui dit au jeu ce qu'il est en train de faire. Tous les scripts vérifient cet état avant d'agir.
> Exemple concret : *« Le mouvement ne fonctionne QUE si `mode = carte`. Le combat ne fonctionne QUE si `mode = combat`. »*
>
> 🇬🇧 This is the hardest concept in the entire project. A state is a variable that tells the game what it's currently doing. All scripts check this state before acting.
> Concrete example: *"Movement only works if `mode = map`. Battle only works if `mode = battle`."*

---

## 🕒 Session 4 — Polish & Personal Touch

**Objectif :** Finir, stabiliser, et personnaliser le jeu.
**Goal:** Finish, stabilise, and personalise the game.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 3 + état des projets. / Session 3 recap + project status check. |
| 15 min | Débogage collectif : problèmes fréquents identifiés en session 3. / Collective debugging: common issues spotted in session 3. |
| 40 min | Temps libre guidé : finitions + stretch goals. / Guided free time: finishing touches + stretch goals. |
| 25 min | Démo finale devant le groupe + vote du jeu préféré. / Final demo in front of the group + vote for favourite game. |

### 📚 Concepts revisités / Concepts revisited
- Gestion des états / State management
- Broadcasts entre sprites / Broadcasts between sprites
- Variables globales / Global variables

### 🛠 Ce que les élèves finissent / Students finish
- Transition carte → combat → retour carte / Map → battle → back to map transition
- Condition de victoire ET de défaite / Win condition AND lose condition
- Un minimum de personnalisation visuelle / Minimum visual personalisation

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Un jeu qui crashe ou qui bug, c'est pas un jeu fini. Avant d'ajouter quoi que ce soit, vérifiez que ce que vous avez déjà fonctionne de A à Z. »*
>
> 🇬🇧 *"A game that crashes or bugs out isn't a finished game. Before adding anything new, make sure what you already have works from start to finish."*

> 🇫🇷 Pour la démo finale : *« Expliquez une chose que vous avez trouvée difficile et comment vous l'avez résolue. »*
>
> 🇬🇧 For the final demo: *"Tell us one thing you found hard and how you solved it."*

### 🎯 Stretch goals
- 🇫🇷 Plusieurs ennemis différents avec des HP différents / 🇬🇧 Multiple enemies with different HP values
- 🇫🇷 Système d'expérience / niveau / 🇬🇧 Experience / level system
- 🇫🇷 Musique différente en mode carte et en mode combat / 🇬🇧 Different music for map mode and battle mode
- 🇫🇷 Animation d'attaque (changement de costume) / 🇬🇧 Attack animation (costume change)
- 🇫🇷 Plusieurs zones sur la carte avec des ennemis différents par zone / 🇬🇧 Multiple map zones with different enemies per zone

---