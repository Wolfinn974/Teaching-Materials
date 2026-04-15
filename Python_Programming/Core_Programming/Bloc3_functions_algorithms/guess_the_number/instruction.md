# 🎲 Guess the Number

**Bloc 3 — Functions & Algorithms**
**Difficulté / Difficulty:** ⭐⭐☆

---

## 🇫🇷 Énoncé

Écris un jeu où l'ordinateur choisit un nombre aléatoire entre 1 et 100, et le joueur doit le deviner. Après chaque tentative, le programme indique si le nombre cherché est plus grand ou plus petit.

**Exemple :**
```
Devinez le nombre (entre 1 et 100) : 50
Trop petit !

Devinez le nombre : 75
Trop grand !

Devinez le nombre : 63
Trop petit !

Devinez le nombre : 69
Bravo ! Vous avez trouvé en 4 tentatives.
```

**Contraintes :**
- Le nombre est généré avec `random.randint()`
- Tu dois écrire une fonction `check_guess(secret, guess)` qui retourne `"too low"`, `"too high"` ou `"correct"`
- Le programme compte et affiche le nombre de tentatives à la fin
- Le joueur a un nombre illimité de tentatives

**Stretch 🚀 :**  
Limite le joueur à 7 tentatives maximum. Si le joueur échoue, révèle le nombre secret et propose de rejouer.

---

## 🇬🇧 Instructions

Write a game where the computer picks a random number between 1 and 100, and the player must guess it. After each attempt, the program tells the player whether the secret number is higher or lower.

**Example:**
```
Guess the number (between 1 and 100): 50
Too low!

Guess the number: 75
Too high!

Guess the number: 63
Too low!

Guess the number: 69
Well done! You found it in 4 attempts.
```

**Constraints:**
- The number is generated with `random.randint()`
- You must write a `check_guess(secret, guess)` function that returns `"too low"`, `"too high"` or `"correct"`
- The program counts and displays the number of attempts at the end
- The player has unlimited attempts

**Stretch 🚀:**  
Limit the player to 7 attempts maximum. If the player fails, reveal the secret number and offer to play again.