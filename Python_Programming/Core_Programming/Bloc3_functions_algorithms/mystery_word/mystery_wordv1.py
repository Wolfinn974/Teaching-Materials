import random

liste_mot = ["python", "robot", "algorithme", "ordinateur", "bug", "variable"]
mot = random.choice(liste_mot)
guess = ""

while guess != mot:
    guess = input("Devine le mot : ").lower()
    if guess == mot:
        print("Vous avez trouvez le mot mystère !")
    else:
        print("Raté ! Essaie encore")