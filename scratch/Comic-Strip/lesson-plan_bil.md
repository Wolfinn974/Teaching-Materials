# 🎭 Comic Strip — Animation & Storytelling

**Niveau / Level:** A déjà fait un projet Scratch / Has completed one Scratch project
**Durée / Duration:** 2 × 1h30
**Outil / Tool:** Scratch

> 📌 **Note prof / Instructor note:**
> 🇫🇷 Aucun asset fourni — les élèves dessinent leurs propres personnages et décors directement dans Scratch. C'est voulu : l'imagination prime sur la technique ici.
> 🇬🇧 No assets provided — students draw their own characters and backgrounds directly in Scratch. This is intentional: imagination comes first here.

---

## 🕒 Session 1 — Scenes & Dialogue

**Objectif :** Raconter une histoire avec des personnages qui parlent et des scènes qui s'enchaînent.
**Goal:** Tell a story with talking characters and scene progression.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Intro : montrer une vraie BD, demander *"Comment on traduit ça dans Scratch ?"* / Show a real comic strip, ask *"How do we translate this into Scratch?"* |
| 15 min | Brainstorm : chaque élève écrit 3 lignes de son histoire (qui, quoi, où). / Brainstorm: each student writes 3 lines of their story (who, what, where). |
| 20 min | Codage guidé : créer un personnage + premier dialogue avec `dire` et `attendre`. / Guided coding: create a character + first dialogue with `say` and `wait`. |
| 25 min | Codage autonome : construire la scène 1 complète + transition vers scène 2. / Independent coding: build full scene 1 + transition to scene 2. |
| 20 min | Démo intermédiaire + discussion sur le séquençage. / Mid-session demo + discussion on sequencing. |

### 📚 Concepts enseignés / Concepts taught
- **"Say" blocks** — `dire [texte] pendant [X] secondes` / `say [text] for [X] seconds` — dialogue minuté / timed dialogue
- **Timing with wait** — `attendre X secondes` / `wait X seconds` — contrôler le rythme narratif / control narrative pacing
- **Scene changes** — changer de fond + cacher/montrer les sprites / switch backdrop + hide/show sprites

### 🛠 Ce que les élèves construisent / Students build
- Leurs propres personnages dessinés dans l'éditeur Scratch / Their own characters drawn in the Scratch editor
- Leurs propres décors / Their own backgrounds
- Une histoire en minimum 2 scènes avec dialogues / A story with at least 2 scenes and dialogue

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Dans une BD papier, les cases s'affichent toutes en même temps. Dans Scratch, elles s'affichent une par une — dans le temps. Comment on contrôle ça ? »*
> Laisser répondre → *« Avec `attendre`. C'est le secret du timing. »*
>
> 🇬🇧 *"In a paper comic, all panels are visible at once. In Scratch, they appear one by one — over time. How do we control that?"*
> Let them answer → *"With `wait`. That's the secret to timing."*

> 🇫🇷 Sur la liberté créative : *« Aujourd'hui il n'y a pas de 'bon' personnage ou de 'bon' décor. Il y a juste votre histoire. Dessinez ce qui vous parle. »*
>
> 🇬🇧 On creative freedom: *"Today there's no 'right' character or 'right' background. There's just your story. Draw what means something to you."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Tout se passe en même temps → les élèves ont oublié les `attendre` entre les dialogues / 🇬🇧 Everything happens at once → students forgot `wait` blocks between dialogues
- 🇫🇷 Sprites cachés qui ne réapparaissent pas → oubli de `montrer` au bon moment / 🇬🇧 Hidden sprites that never reappear → missing `show` at the right moment
- 🇫🇷 Histoire trop longue pour le temps dispo → les encourager à simplifier, 2 scènes suffisent / 🇬🇧 Story too long for the available time → encourage simplifying, 2 scenes is enough

### 💡 Concept difficile / Hard concept
**Séquençage vs événements / Sequencing vs events**

> 🇫🇷 *« En Scratch, par défaut tout part en même temps quand on clique le drapeau. Si le personnage A attend 3 secondes et que le personnage B attend 0 secondes, ils parlent en même temps. Il faut que chaque personnage sache exactement quand c'est son tour. »*
> Solution : utiliser `envoyer message` pour passer le relais entre personnages / use `broadcast` to pass the turn between characters.
>
> 🇬🇧 *"In Scratch, by default everything starts at the same time when you click the flag. If character A waits 3 seconds and character B waits 0 seconds, they talk simultaneously. Each character needs to know exactly when it's their turn."*
> Solution: use `broadcast` to hand off between characters.

> 💡 🇫🇷 *« Ne faites pas tout se passer en même temps. Un seul personnage parle à la fois — comme dans une vraie conversation. »*
> 🇬🇧 *"Don't make everything happen at the same time. Only one character speaks at a time — like a real conversation."*

---

## 🕒 Session 2 — Animations & Timing

**Objectif :** Donner vie aux personnages avec des animations, des effets et du son.
**Goal:** Bring characters to life with animations, effects, and sound.

### ⏱ Timing

| Durée / Duration | Activité / Activity |
|-------|----------|
| 10 min | Rappel session 1 + démo d'un élève volontaire. / Session 1 recap + volunteer student demo. |
| 20 min | Explication : les costumes — comment animer un personnage avec 2-3 dessins. / Costumes — how to animate a character with 2-3 drawings. |
| 25 min | Codage guidé : animation de marche + effet sonore. / Guided coding: walk animation + sound effect. |
| 25 min | Codage autonome : finir l'histoire + ajouter animations perso. / Independent coding: finish the story + add personal animations. |
| 10 min | Démo finale devant le groupe. / Final demo in front of the group. |

### 📚 Concepts enseignés / Concepts taught
- **Costumes** — chaque costume = une frame d'animation / each costume = one animation frame
- **Timing** — `attendre X secondes` entre les costumes pour contrôler la vitesse d'animation / `wait X seconds` between costumes to control animation speed
- **Sound** — `jouer son [X]` / `play sound [X]` — sons enregistrés ou de la bibliothèque Scratch / recorded sounds or Scratch library

### 🛠 Ce que les élèves construisent / Students build
- Un personnage avec au moins 2 costumes animés / A character with at least 2 animated costumes
- Un effet sonore ou une musique de fond / A sound effect or background music
- Une BD complète et présentable / A complete, presentable comic strip

### 🗣 Script indicatif / Teaching script
> 🇫🇷 *« Comment les dessins animés fonctionnent vraiment ? Des milliers d'images par seconde. Nous on va faire pareil — mais avec 2 ou 3 images. La clé c'est la vitesse de changement. »*
>
> 🇬🇧 *"How do cartoons actually work? Thousands of images per second. We'll do the same — but with 2 or 3 images. The key is how fast you switch."*

> 🇫🇷 Sur les émotions : *« Si votre personnage est en colère, à quoi ressemble son visage ? Dessinez ce costume. Si il est content, dessinez l'autre. Le code choisit lequel montrer selon la situation. »*
>
> 🇬🇧 On emotions: *"If your character is angry, what does their face look like? Draw that costume. If they're happy, draw the other. The code chooses which one to show depending on the situation."*

### ⚠️ Erreurs fréquentes / Common mistakes
- 🇫🇷 Animation trop rapide → `attendre` trop court, le personnage "tremble" / 🇬🇧 Animation too fast → `wait` too short, character "shakes"
- 🇫🇷 Son qui joue en boucle sans s'arrêter → utiliser `jouer son X jusqu'à la fin` / 🇬🇧 Sound looping endlessly → use `play sound X until done`
- 🇫🇷 Costumes dans le mauvais ordre → vérifier la numérotation dans l'éditeur de costumes / 🇬🇧 Costumes in wrong order → check numbering in the costume editor

### 🎯 Stretch challenge
- 🇫🇷 Exprimer des émotions via les costumes (joie, colère, surprise) / 🇬🇧 Express emotions through costumes (joy, anger, surprise)
- 🇫🇷 Ajouter une scène bonus secrète déclenchée par un clic / 🇬🇧 Add a secret bonus scene triggered by a click
- 🇫🇷 Faire parler le personnage avec un son enregistré (micro) / 🇬🇧 Make the character speak with a recorded sound (microphone)

