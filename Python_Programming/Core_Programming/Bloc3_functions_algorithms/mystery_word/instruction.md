# 🕵️ Mystery Word

**Bloc 3 — Functions & Algorithms**
**Difficulté / Difficulty:** ⭐⭐☆

---

## 🇫🇷 Énoncé

Écris un jeu où l'ordinateur choisit un mot au hasard dans une liste, et le joueur doit le deviner lettre par lettre — comme un Pendu simplifié.

Le mot est affiché sous forme de tirets. À chaque bonne lettre proposée, les tirets correspondants sont révélés. Le joueur a 6 tentatives maximum.

**Exemple :**
```
Mot : _ _ _ _ _
Tentatives restantes : 6

Proposez une lettre : p
Mot : p _ _ _ _
Tentatives restantes : 6

Proposez une lettre : z
Lettre incorrecte.
Mot : p _ _ _ _
Tentatives restantes : 5

...

Mot : p y t h o n
Bravo ! Vous avez trouvé le mot.
```

**Contraintes :**
- La liste de mots est hardcodée (minimum 8 mots)
- Le mot est choisi avec `random.choice()`
- Tu dois écrire au moins deux fonctions :
  - une pour afficher l'état actuel du mot (`_ _ p _ _`)
  - une pour vérifier si la lettre proposée est dans le mot
- Les lettres déjà proposées doivent être mémorisées — pas de double comptage

**Stretch 🚀 :**  
Affiche les lettres déjà proposées à chaque tour.

---

## 🇬🇧 Instructions

Write a game where the computer picks a random word from a list, and the player must guess it letter by letter — like a simplified Hangman.

The word is displayed as dashes. Each time a correct letter is guessed, the matching dashes are revealed. The player has a maximum of 6 attempts.

**Example:**
```
Word: _ _ _ _ _
Attempts left: 6

Guess a letter: p
Word: p _ _ _ _
Attempts left: 6

Guess a letter: z
Wrong letter.
Word: p _ _ _ _
Attempts left: 5

...

Word: p y t h o n
Well done! You found the word.
```

**Constraints:**
- The word list is hardcoded (minimum 8 words)
- The word is chosen using `random.choice()`
- You must write at least two functions:
  - one to display the current state of the word (`_ _ p _ _`)
  - one to check if the guessed letter is in the word
- Already guessed letters must be remembered — no double counting

**Stretch 🚀:**  
Display the already guessed letters at each turn.