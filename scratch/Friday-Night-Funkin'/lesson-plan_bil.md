# 🎵 Rhythm Game (FNF-like)

**Niveau / Level:** A déjà fait un projet Scratch / Has completed one Scratch project
**Durée / Duration:** 4 × 1h30
**Outil / Tool:** Scratch

> 📌 **Note prof / Instructor note:**
>
> 🇫🇷 Ce projet est l'un des plus difficiles techniquement — la synchronisation audio dans Scratch est imprécise par nature. La S4 est une séance de finition : les élèves qui arrivent avec un jeu fonctionnel peaufinent, les autres terminent le core gameplay. **Ne pas chercher la perfection du timing** — un jeu qui "sent" le rythme vaut mieux qu'un jeu bloqué sur la précision à la milliseconde.
>
> 🇬🇧 This is one of the most technically challenging projects — audio sync in Scratch is inherently imprecise. S4 is a finishing session: students who arrive with a working game polish it, others finish the core gameplay. **Don't chase timing perfection** — a game that "feels" rhythmic is worth more than one stuck on millisecond precision.

---

## 🕒 Session 1 — Notes & Timing

**Objectif :** Des notes défilent et le joueur appuie sur les bonnes touches au bon moment.
**Goal:** Notes scroll down and the player presses the right keys at the right time.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Intro : montrer FNF, identifier les mécaniques — notes, timing, feedback. / Show FNF, identify mechanics — notes, timing, feedback. |
| 15 min | Explication : comment simuler des beats sans hardcoder chaque note. / How to simulate beats without hardcoding every note. |
| 30 min | Codage guidé : une note qui descend + détection de touche directionnelle. / Guided coding: one falling note + directional key detection. |
| 25 min | Codage autonome : 4 colonnes de notes (haut/bas/gauche/droite). / Independent coding: 4 note columns (up/down/left/right). |
| 10 min | Test + questions. / Test + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Sync input with beats** — utiliser `minuterie` / `timer` comme référence temporelle plutôt que des `attendre` fixes / use `timer` as time reference instead of fixed `wait` blocks
- **Directional inputs** — 4 touches = 4 colonnes = 4 sprites de notes indépendants / 4 keys = 4 columns = 4 independent note sprites
- **Clone spawning** — un sprite "générateur" crée des clones à intervalles réguliers / one "generator" sprite creates clones at regular intervals

### 🛠 Ce que les élèves construisent / Students build
- 4 colonnes de notes qui défilent vers le bas / 4 note columns scrolling downward
- Une zone de frappe en bas de l'écran / A hit zone at the bottom of the screen
- Détection basique : touche appuyée = note disparaît / Basic detection: key pressed = note disappears

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment FNF sait quand spawner une note ? Est-ce que quelqu'un a écrit à la main "note à 2.34 secondes, note à 2.68 secondes"... pour toute la chanson ? »*
> Laisser répondre → *« Parfois oui — c'est ce qu'on appelle un beatmap. Mais on peut aussi utiliser un timer et spawner à intervalle régulier. C'est plus simple et ça suffit pour commencer. »*
>
> 🇬🇧 *"How does FNF know when to spawn a note? Did someone manually write 'note at 2.34 seconds, note at 2.68 seconds'... for the whole song?"*
> Let them answer → *"Sometimes yes — that's called a beatmap. But we can also use a timer and spawn at regular intervals. It's simpler and good enough to start."*

> 🇫🇷 Sur les clones : *« Si chaque note est un sprite différent, combien de sprites il vous faut pour une chanson de 2 minutes ? Des centaines. Les clones règlent ce problème — un seul sprite qui se duplique à la volée. »*
>
> 🇬🇧 On clones: *"If every note is a different sprite, how many sprites do you need for a 2-minute song? Hundreds. Clones solve this — one sprite that duplicates itself on the fly."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Notes hardcodées avec des `attendre` → impossible à modifier, désynchronisé dès que la musique change / 🇬🇧 Notes hardcoded with `wait` blocks → impossible to edit, desyncs as soon as music changes
- 🇫🇷 Oubli de `supprimer ce clone` → accumulation, lag / 🇬🇧 Forgetting `delete this clone` → buildup, lag
- 🇫🇷 Une seule touche détectée pour les 4 colonnes → tout se déclenche en même temps / 🇬🇧 One key detected for all 4 columns → everything triggers simultaneously

---

## 🕒 Session 2 — Feedback & Scoring

**Objectif :** Le jeu récompense la précision et affiche un score.
**Goal:** The game rewards precision and displays a score.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 1 + démo. / Session 1 recap + demo. |
| 15 min | Explication : timing windows — qu'est-ce que "Perfect", "Good", "Miss". / Timing windows — what "Perfect", "Good", "Miss" mean. |
| 30 min | Codage guidé : fenêtres de timing + feedback visuel (couleur/texte). / Guided coding: timing windows + visual feedback (color/text). |
| 25 min | Codage autonome : système de score + multiplicateur de combo. / Independent coding: score system + combo multiplier. |
| 10 min | Test + questions. / Test + Q&A. |

### 📚 Concepts enseignés / Concepts taught
- **Timing windows** — mesurer la distance entre la note et la zone de frappe au moment de l'appui / measure distance between note and hit zone at the moment of keypress
- **Feedback** — changer la couleur du sprite ou afficher un texte selon la précision / change sprite color or display text based on precision
- **Score system** — variable `score` augmentée selon la qualité du coup / `score` variable increased based on hit quality — Perfect > Good > Miss

### 🛠 Ce que les élèves construisent / Students build
- 3 niveaux de précision : Perfect / Good / Miss / 3 precision levels: Perfect / Good / Miss
- Feedback visuel immédiat à chaque note / Immediate visual feedback on each note
- Score affiché en temps réel + combo counter / Real-time score + combo counter

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment le jeu sait si vous avez appuyé "à temps" ? Il mesure la distance entre la note et la ligne de frappe. Si la distance est petite → Perfect. Un peu plus grande → Good. Trop grande → Miss. »*
>
> 🇬🇧 *"How does the game know if you pressed 'on time'? It measures the distance between the note and the hit line. Small distance → Perfect. A bit larger → Good. Too large → Miss."*

> 🇫🇷 Sur le combo : *« Pourquoi les jeux de rythme ont des combos ? Parce que rater une note doit faire mal. Si le score monte pareil que vous ratiez ou non, il n'y a plus de tension. »*
>
> 🇬🇧 On combo: *"Why do rhythm games have combos? Because missing a note should hurt. If the score goes up the same whether you miss or not, there's no tension."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Fenêtre de timing trop stricte → jouable seulement par des robots / 🇬🇧 Timing window too strict → only playable by robots
- 🇫🇷 Fenêtre de timing trop large → tout est Perfect, aucun challenge / 🇬🇧 Timing window too large → everything is Perfect, no challenge
- 🇫🇷 Feedback qui reste affiché trop longtemps → l'écran devient illisible / 🇬🇧 Feedback displayed too long → screen becomes unreadable

### 💡 Concept difficile / Hard concept
**Synchronisation avec la musique / Sync with music**

> 🇫🇷 Scratch ne garantit pas que la musique joue exactement en même temps que le code s'exécute. La solution : ne jamais se fier aux `attendre` pour synchroniser — toujours utiliser `minuterie` comme référence. Spawner les notes en fonction du temps écoulé depuis le début de la chanson, pas en fonction de l'ordre d'exécution des blocs.
>
> 🇬🇧 Scratch doesn't guarantee that music plays at exactly the same time as the code executes. The fix: never rely on `wait` blocks for sync — always use `timer` as the reference. Spawn notes based on elapsed time since the song started, not based on block execution order.

> 💡 🇫🇷 *« Ne hardcodez pas les beats. Utilisez le timing. Un `attendre` qui dérive de 0.1 seconde sur 50 notes = votre jeu est désynchronisé au bout de 5 secondes. »*
> 🇬🇧 *"Don't hardcode beats. Use timing. A `wait` that drifts by 0.1 seconds over 50 notes = your game is desynced after 5 seconds."*

---

## 🕒 Session 3 — Music & Full Loop

**Objectif :** La musique joue, les notes sont synchronisées, le jeu a un début et une fin.
**Goal:** Music plays, notes are synced, the game has a start and an end.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 2 + état des projets. / Session 2 recap + project status check. |
| 20 min | Codage guidé : lancer la musique + synchroniser le spawn des notes sur le timer. / Guided coding: start music + sync note spawn to the timer. |
| 25 min | Codage guidé : écran de début + écran de fin avec score final. / Guided coding: start screen + end screen with final score. |
| 25 min | Codage autonome : ajuster le timing + tester sur la vraie musique. / Independent coding: adjust timing + test on actual music. |
| 10 min | Test collectif — chaque élève fait jouer son jeu à un voisin. / Collective test — each student has a neighbour play their game. |

### 📚 Concepts enseignés / Concepts taught
- **Full game loop** — écran titre → jeu → écran fin → restart / title screen → game → end screen → restart
- **Timer-based spawn** — `si minuterie mod [intervalle] < 0.05` pour spawner à rythme régulier / `if timer mod [interval] < 0.05` to spawn at regular rhythm
- **Music start sync** — `jouer son X` déclenché exactement quand le timer est remis à zéro / `play sound X` triggered exactly when timer resets

### 🛠 Ce que les élèves construisent / Students build
- Un jeu complet avec musique synchronisée / A complete game with synced music
- Écran de début + écran de fin / Start screen + end screen
- Score final affiché + possibilité de rejouer / Final score displayed + option to replay

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Votre jeu doit pouvoir être joué par quelqu'un qui ne l'a jamais vu. Est-ce qu'il sait quoi faire en arrivant sur l'écran de titre ? Est-ce qu'il sait que c'est fini quand la musique s'arrête ? »*
>
> 🇬🇧 *"Your game needs to be playable by someone who's never seen it. Do they know what to do on the title screen? Do they know it's over when the music stops?"*

> 🇫🇷 Test croisé : *« Donnez votre jeu à votre voisin sans rien expliquer. Regardez où il bloque. C'est là que votre jeu a besoin de travail. »*
>
> 🇬🇧 Cross-test: *"Give your game to your neighbour without explaining anything. Watch where they get stuck. That's where your game needs work."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Musique qui démarre avant que les notes apparaissent → décalage ressenti dès le début / 🇬🇧 Music starting before notes appear → offset felt from the very beginning
- 🇫🇷 Pas d'écran de fin → le jeu boucle indéfiniment ou freeze / 🇬🇧 No end screen → game loops endlessly or freezes
- 🇫🇷 Timer non remis à zéro au restart → notes spawnent immédiatement dès la 2ème partie / 🇬🇧 Timer not reset on restart → notes spawn immediately on 2nd playthrough

---

## 🕒 Session 4 — Finish Line

**Objectif :** Tout le monde repart avec un jeu jouable et présentable.
**Goal:** Everyone leaves with a playable, presentable game.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Bilan honnête : qui a quoi de fonctionnel ? Prioriser ce qui manque. / Honest check-in: who has what working? Prioritise what's missing. |
| 20 min | Débogage ciblé : problèmes de sync remontés en S3. / Targeted debugging: sync issues flagged in S3. |
| 30 min | Temps libre : finitions + stretch goals selon avancement. / Free time: finishing touches + stretch goals based on progress. |
| 30 min | Démo finale + discussion : *"C'est quoi le truc le plus dur que vous avez résolu ?"* / Final demo + discussion: *"What's the hardest thing you solved?"* |

### 📚 Concepts revisités / Concepts revisited
- Synchronisation timer / Timer sync
- Clone lifecycle / Clone lifecycle
- Gestion des états (titre / jeu / fin) / State management (title / game / end)

### 🛠 Priorités de finition / Finishing priorities
1. Musique + notes synchronisées / Music + notes synced *(non-négociable / non-negotiable)*
2. Score fonctionnel / Working score
3. Écran de fin / End screen
4. *(stretch)* Feedback visuel Perfect/Good/Miss / Visual feedback Perfect/Good/Miss

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« On ne rajoute rien aujourd'hui si le core ne marche pas. Un jeu avec une mécanique qui fonctionne bien vaut 10 fois plus qu'un jeu avec 5 mécaniques cassées. »*
>
> 🇬🇧 *"We're not adding anything today if the core doesn't work. A game with one mechanic that works well is worth 10 times more than a game with 5 broken mechanics."*

> 🇫🇷 Pour la démo : *« Jouez votre jeu devant le groupe. Pas besoin que ce soit parfait — montrez ce qui marche et expliquez ce que vous auriez voulu finir. »*
>
> 🇬🇧 For the demo: *"Play your game in front of the group. It doesn't need to be perfect — show what works and explain what you wished you'd finished."*

### 🎯 Stretch goals
- 🇫🇷 Animations du personnage (FNF-style, costumes selon la direction) / 🇬🇧 Character animations (FNF-style, costumes per direction)
- 🇫🇷 Plusieurs chansons sélectionnables / 🇬🇧 Multiple selectable songs
- 🇫🇷 Écran de résultats avec grade (S/A/B/C) / 🇬🇧 Results screen with grade (S/A/B/C)
- 🇫🇷 Effets visuels sur les Perfect (flash, particules) / 🇬🇧 Visual effects on Perfects (flash, particles)
- 🇫🇷 Barre de vie qui descend sur les Miss / 🇬🇧 Health bar that drops on misses

---
