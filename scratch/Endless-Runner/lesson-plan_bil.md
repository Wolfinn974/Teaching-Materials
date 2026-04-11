# 🏃 Endless Runner

**Niveau / Level:** Débutants complets / Complete beginners
**Durée / Duration:** 3 × 1h30
**Outil / Tool:** Scratch

---

## 🕒 Session 1 — Core Gameplay

**Objectif :** Le personnage se déplace en continu et peut sauter.
**Goal:** The character moves continuously and can jump.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Intro : qu'est-ce qu'un endless runner ? Montrer des exemples (Geometry Dash, Dino Chrome). / What's an endless runner? Show examples. |
| 15 min | Explication : l'illusion de mouvement — c'est le décor qui bouge, pas le personnage. / The scrolling illusion — the world moves, not the character. |
| 30 min | Codage guidé : sol qui défile + boucle infinie. / Guided coding: scrolling ground + infinite loop. |
| 25 min | Codage autonome : mécanique de saut. / Independent coding: jump mechanic. |
| 10 min | Démo + questions. / Demo + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Infinite loop** — `répéter indéfiniment` / `forever` pour faire défiler le sol / to scroll the ground
- **Scrolling illusion** — deux sprites de sol qui se relaient / two ground sprites alternating
- **Jump mechanic** — changer Y avec gravité simulée / changing Y with simulated gravity

### 🛠 Ce que les élèves construisent / Students build
- Un sol qui défile en boucle / A looping scrolling ground
- Un personnage qui saute quand on appuie sur espace / A character that jumps on spacebar

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Est-ce que le personnage bouge vraiment dans Geometry Dash ? »*
> Laisser répondre → *« Non ! C'est le monde qui se déplace. On va faire pareil. »*
>
> 🇬🇧 *"Does the character actually move in Geometry Dash?"*
> Let them answer → *"No! The world moves. We're going to do the same."*

> 🇫🇷 Avant le saut : *« Comment est-ce qu'on fait tomber quelque chose ? La gravité, c'est juste un nombre qu'on retire en boucle à la hauteur. »*
>
> 🇬🇧 Before the jump: *"How do we make something fall? Gravity is just a number we subtract from height in a loop."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Gravité trop forte → le saut est imperceptible / 🇬🇧 Gravity too strong → jump is barely visible
- 🇫🇷 Oubli de la condition « si touche le sol → stop gravité » → le perso tombe à l'infini / 🇬🇧 Missing "if touching ground → stop gravity" → character falls forever

---

## 🕒 Session 2 — Obstacles & Scoring

**Objectif :** Des obstacles apparaissent, le score monte, le jeu accélère.
**Goal:** Obstacles spawn, score increases, game speeds up.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 1 + démo d'un élève. / Session 1 recap + student demo. |
| 20 min | Explication : les clones — pourquoi ne pas faire 10 sprites obstacles ? / Clones — why not just make 10 obstacle sprites? |
| 30 min | Codage guidé : spawn de clones + compteur de score. / Guided coding: clone spawning + score counter. |
| 20 min | Codage autonome : accélération progressive. / Independent coding: speed increase. |
| 10 min | Démo + questions. / Demo + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Spawn clones** — `créer un clone de moi-même` / `create clone of myself` sur un timer / on a timer
- **Score counter** — variable globale incrémentée en boucle / global variable incremented in a loop
- **Speed increase** — variable `vitesse` / `speed` augmentée toutes les X secondes / increased every X seconds

### 🛠 Ce que les élèves construisent / Students build
- Des obstacles qui apparaissent depuis la droite / Obstacles spawning from the right
- Un score affiché à l'écran / A score displayed on screen
- Une vitesse qui augmente avec le temps / Speed that increases over time

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Si je dois créer 50 obstacles, je fais 50 sprites ? »*
> Laisser répondre → *« Non, on crée un seul sprite 'usine' qui fait des copies de lui-même. Ces copies, c'est des clones. »*
>
> 🇬🇧 *"If I need 50 obstacles, do I make 50 sprites?"*
> Let them answer → *"No — one 'factory' sprite makes copies of itself. Those copies are clones."*

> 🇫🇷 Sur la vitesse : *« Comment on rend un jeu plus difficile sans le recoder ? On change juste un nombre — la vitesse. C'est pour ça qu'on met ça dans une variable. »*
>
> 🇬🇧 On speed: *"How do we make the game harder without rewriting it? We just change one number — the speed. That's why it goes in a variable."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Oubli de `supprimer ce clone` → accumulation en mémoire, lag garanti / 🇬🇧 Missing `delete this clone` → memory build-up, guaranteed lag
- 🇫🇷 Variable vitesse non partagée entre les sprites → sol et obstacles désynchronisés / 🇬🇧 Speed variable not shared across sprites → ground and obstacles out of sync

> 💡 🇫🇷 *« Si votre jeu rame, regardez combien de clones existent. Probablement trop. Le clone doit se supprimer quand il sort de l'écran. »*
> 🇬🇧 *"If your game lags, check how many clones exist. Probably too many. A clone must delete itself when it leaves the screen."*

---

## 🕒 Session 3 — Polish

**Objectif :** Le jeu est complet, jouable, et présentable.
**Goal:** The game is complete, playable, and ready to show.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel + état des projets. / Recap + project status check. |
| 15 min | Codage guidé : game over + écran de restart. / Guided coding: game over + restart screen. |
| 20 min | Codage guidé : difficulté progressive (paliers). / Guided coding: difficulty ramp (stages). |
| 25 min | Temps libre : stretch goals + finitions perso. / Free time: stretch goals + personal touches. |
| 20 min | Démo des projets devant le groupe. / Project demos in front of the group. |

### 📚 Concepts enseignés / Concepts taught
- **Difficulty ramp** — paliers de vitesse toutes les N secondes / speed stages every N seconds
- **Game over** — `envoyer message "game over"` / `broadcast "game over"` + arrêt des scripts / stops all scripts
- **Restart** — réinitialisation des variables + `envoyer message "start"` / reset variables + `broadcast "start"`

### 🛠 Ce que les élèves construisent / Students build
- Un écran game over avec le score final / A game over screen with the final score
- Un bouton restart fonctionnel / A working restart button
- (stretch) Effets sonores, animations, thème perso / Sound effects, animations, custom theme

### 🗣 Script indicatif / Teaching script
> 🇫🇷 Avant le game over : *« Qu'est-ce qui doit s'arrêter quand le joueur meurt ? Tout. Alors on va envoyer un message que tout le monde écoute. »*
>
> 🇬🇧 Before game over: *"What needs to stop when the player dies? Everything. So we'll broadcast a message that everyone listens to."*

> 🇫🇷 Pour le restart : *« C'est quoi l'état du jeu au tout début ? Score à 0, vitesse à 1, personnage en position de départ. Le restart, c'est juste remettre tout ça. »*
>
> 🇬🇧 For restart: *"What does the game look like at the very start? Score at 0, speed at 1, character at starting position. Restarting just means putting everything back."*

### 🎯 Stretch goals
- 🇫🇷 Effets sonores (saut, mort, score) / 🇬🇧 Sound effects (jump, death, score)
- 🇫🇷 Sprite animé (marche, saut, mort) / 🇬🇧 Animated sprite (walk, jump, death)
- 🇫🇷 Thème visuel personnalisé / 🇬🇧 Custom visual theme
- 🇫🇷 Meilleur score sauvegardé / 🇬🇧 High score saved
