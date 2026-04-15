# 🥊 Street Fighter-like

**Niveau / Level:** A déjà fait un projet Scratch / Has completed one Scratch project
**Durée / Duration:** 3 × 1h30
**Outil / Tool:** Scratch

> 📌 **Note prof / Instructor note:**
>
> 🇫🇷 Ce projet introduit deux concepts inhabituels pour des débutants : les hitboxes et le multiplayer local. Le plus gros défi n'est pas technique — c'est que les élèves doivent gérer **deux personnages en même temps** dans le même projet, avec des touches différentes. Prévoir du temps pour expliquer la séparation des contrôles avant de coder.
>
> 🇬🇧 This project introduces two concepts unusual for beginners: hitboxes and local multiplayer. The biggest challenge isn't technical — it's that students need to manage **two characters at the same time** in the same project, with different keys. Plan time to explain control separation before coding.

---

## 🕒 Session 1 — Movement & Attacks

**Objectif :** Un personnage se déplace, attaque, et inflige des dégâts.
**Goal:** One character moves, attacks, and deals damage.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Intro : regarder un extrait de Street Fighter, identifier les mécaniques. / Watch a Street Fighter clip, identify the mechanics. |
| 15 min | Explication : qu'est-ce qu'une hitbox ? Pourquoi le sprite visible ≠ la zone de collision. / What's a hitbox? Why the visible sprite ≠ the collision zone. |
| 25 min | Codage guidé : déplacement + animation d'attaque (changement de costume). / Guided coding: movement + attack animation (costume change). |
| 25 min | Codage guidé : variable HP + réduction au contact d'une attaque. / Guided coding: HP variable + reduction on attack contact. |
| 15 min | Test en solo + ajustements. / Solo testing + adjustments. |

### 📚 Concepts enseignés / Concepts taught
- **Attack animation** — alterner entre costume "neutre" et costume "attaque" avec un `attendre` court / alternate between "idle" and "attack" costume with a short `wait`
- **Hitbox concept** — sprite invisible positionné sur le poing/pied qui détecte le contact / invisible sprite positioned on the fist/foot that detects contact
- **Health variable** — variable `HP_joueur1` diminuée quand la hitbox touche l'adversaire / `HP_player1` variable decreased when hitbox touches opponent

### 🛠 Ce que les élèves construisent / Students build
- Un personnage avec déplacement gauche/droite et saut / A character with left/right movement and jump
- Une attaque basique avec animation / A basic attack with animation
- Un système HP affiché à l'écran / An HP system displayed on screen

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Dans Street Fighter, est-ce que le poing du personnage doit toucher exactement le pixel du corps adverse ? »*
> Laisser répondre → *« Non — il y a une zone invisible autour du personnage. Cette zone, c'est la hitbox. On va la créer avec un sprite transparent. »*
>
> 🇬🇧 *"In Street Fighter, does the character's fist need to touch the exact pixel of the opponent?"*
> Let them answer → *"No — there's an invisible zone around the character. That zone is the hitbox. We'll build it with a transparent sprite."*

> 🇫🇷 Sur les HP : *« Les points de vie c'est un nombre. Une attaque qui touche = on soustrait. Simple. Le jeu ne sait pas si c'est "juste" — il sait juste si la hitbox touche. »*
>
> 🇬🇧 On HP: *"Hit points are a number. A hit that connects = subtract. Simple. The game doesn't know if it's 'fair' — it just knows if the hitbox is touching."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Hitbox toujours active → dégâts infligés en permanence même sans attaquer / 🇬🇧 Hitbox always active → damage dealt constantly even without attacking
- 🇫🇷 Animation d'attaque trop longue → le personnage reste bloqué en pose d'attaque / 🇬🇧 Attack animation too long → character stays stuck in attack pose
- 🇫🇷 HP qui descend en dessous de 0 → ajouter `si HP < 0, mettre HP à 0` / 🇬🇧 HP going below 0 → add `if HP < 0, set HP to 0`

### 💡 Concept difficile / Hard concept
**La hitbox / The hitbox**

> 🇫🇷 Une hitbox c'est un sprite séparé, transparent, attaché au personnage. Elle n'existe que pendant l'animation d'attaque — elle apparaît, vérifie le contact, puis disparaît. Sans ça, la détection de collision se fait sur tout le corps en permanence.
>
> 🇬🇧 A hitbox is a separate, transparent sprite attached to the character. It only exists during the attack animation — it appears, checks for contact, then disappears. Without this, collision detection happens on the whole body at all times.

---

## 🕒 Session 2 — 2 Players & Controls

**Objectif :** Deux joueurs s'affrontent sur le même clavier.
**Goal:** Two players fight on the same keyboard.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 1 + démo. / Session 1 recap + demo. |
| 15 min | Explication : multiplayer local — deux sets de touches, deux sprites, deux HP. / Local multiplayer — two key sets, two sprites, two HP. |
| 30 min | Codage guidé : dupliquer le personnage + assigner les touches ZQSD au joueur 2. / Guided coding: duplicate character + assign WASD keys to player 2. |
| 25 min | Codage autonome : relier les hitboxes des deux joueurs. / Independent coding: connect both players' hitboxes. |
| 10 min | Premier vrai test à deux. / First real two-player test. |

### 📚 Concepts enseignés / Concepts taught
- **Local multiplayer** — deux sprites indépendants contrôlés par des touches différentes sur le même clavier / two independent sprites controlled by different keys on the same keyboard
- **Attack cooldown** — variable `cooldown` qui empêche le spam d'attaque / `cooldown` variable that prevents attack spamming — `attendre X secondes` après chaque attaque / `wait X seconds` after each attack
- **Damage logic** — chaque hitbox ne vérifie que le sprite adverse, pas le sien / each hitbox only checks the opponent sprite, not its own

### 🛠 Ce que les élèves construisent / Students build
- Joueur 1 : touches fléchées + une touche d'attaque / Player 1: arrow keys + one attack key
- Joueur 2 : ZQSD (ou WASD) + une touche d'attaque différente / Player 2: ZQSD (or WASD) + a different attack key
- Les deux HP affichés simultanément / Both HP bars displayed simultaneously

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment deux personnes jouent sur le même clavier sans se gêner ? »*
> Laisser répondre → *« Chacun a ses propres touches. Le jeu écoute les deux en même temps. C'est ça le multiplayer local — pas de réseau, juste deux sets de contrôles. »*
>
> 🇬🇧 *"How do two people play on the same keyboard without interfering?"*
> Let them answer → *"Each has their own keys. The game listens to both at the same time. That's local multiplayer — no network, just two sets of controls."*

> 🇫🇷 Sur le cooldown : *« Sans cooldown, le joueur le plus rapide pour spammer gagne toujours. Le cooldown force un rythme — comme dans un vrai jeu de combat. »*
>
> 🇬🇧 On cooldown: *"Without a cooldown, whoever spams fastest always wins. The cooldown forces a rhythm — like in a real fighting game."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Touches qui se chevauchent → joueur 1 et joueur 2 utilisent les mêmes touches / 🇬🇧 Overlapping keys → player 1 and player 2 using the same keys
- 🇫🇷 Hitbox du joueur 1 qui détecte le joueur 1 lui-même / 🇬🇧 Player 1's hitbox detecting player 1 themselves
- 🇫🇷 Pas de cooldown → spam d'attaque, HP tombe à 0 en 2 secondes / 🇬🇧 No cooldown → attack spam, HP hits 0 in 2 seconds

### 💡 Concept difficile / Hard concept
**Détection de coup équitable / Fair hit detection**

> 🇫🇷 Le problème classique : la hitbox détecte un contact alors que visuellement l'attaque n'a pas l'air de toucher — ou inversement. Deux causes fréquentes : la hitbox est mal positionnée par rapport au costume d'attaque, ou elle reste active trop longtemps. La solution : synchroniser précisément l'apparition de la hitbox avec la frame d'animation où le coup est censé porter.
>
> 🇬🇧 The classic problem: the hitbox detects contact when the attack visually doesn't look like it's connecting — or the opposite. Two frequent causes: the hitbox is misaligned with the attack costume, or it stays active too long. The fix: precisely synchronise the hitbox appearance with the animation frame where the hit is supposed to land.

---

## 🕒 Session 3 — Polish & Balance

**Objectif :** Le jeu est jouable, équilibré, et présentable.
**Goal:** The game is playable, balanced, and ready to show.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 2 + état des projets. / Session 2 recap + project status check. |
| 15 min | Débogage collectif : problèmes de hit detection remontés en session 2. / Collective debugging: hit detection issues from session 2. |
| 20 min | Codage guidé : condition de victoire + écran game over. / Guided coding: win condition + game over screen. |
| 25 min | Temps libre : équilibrage + stretch goals. / Free time: balancing + stretch goals. |
| 20 min | Tournoi rapide + démo finale. / Quick tournament + final demo. |

### 📚 Concepts revisités / Concepts revisited
- Cooldown et timing d'attaque / Attack cooldown and timing
- Gestion des états (combat en cours / game over) / State management (fighting / game over)
- Variables globales partagées entre sprites / Global variables shared between sprites

### 🛠 Ce que les élèves finissent / Students finish
- Condition de victoire quand un HP tombe à 0 / Win condition when one HP hits 0
- Écran de fin avec le gagnant affiché / End screen showing the winner
- Un jeu équilibré — ni trop lent ni trop facile à spammer / A balanced game — neither too slow nor too easy to spam

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment vous savez si votre jeu est équilibré ? Jouez-y. Si un joueur gagne systématiquement sans effort, quelque chose cloche — dégâts trop élevés, cooldown trop court, hitbox trop grande. »*
>
> 🇬🇧 *"How do you know if your game is balanced? Play it. If one player always wins effortlessly, something's off — damage too high, cooldown too short, hitbox too large."*

> 🇫🇷 Pour la démo finale : *« Expliquez une règle de votre jeu que vous avez dû ajuster. Pourquoi ? Qu'est-ce que vous avez changé ? »*
>
> 🇬🇧 For the final demo: *"Explain one rule in your game you had to adjust. Why? What did you change?"*

### 🎯 Stretch goals
- 🇫🇷 Barre de vie visuelle (sprite qui rétrécit) au lieu d'un simple nombre / 🇬🇧 Visual health bar (shrinking sprite) instead of a plain number
- 🇫🇷 Deuxième type d'attaque (coup bas, coup sauté) / 🇬🇧 Second attack type (low hit, jump attack)
- 🇫🇷 Effets sonores d'impact / 🇬🇧 Hit sound effects
- 🇫🇷 Animation de mort / 🇬🇧 Death animation
- 🇫🇷 Système de rounds (premier à 2 victoires) / 🇬🇧 Round system (first to 2 wins)

---
