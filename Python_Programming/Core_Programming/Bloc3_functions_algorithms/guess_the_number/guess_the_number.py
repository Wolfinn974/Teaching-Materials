import random

num = random.randint(1, 100)
guess = None

while guess != num:
    guess = int(input("guess a number between 1 and 100: "))
    score = 0

    if guess == num:
        print("congratulations! you won! your score is :", score)
        break
    elif guess > num:
        print("+ petit")
        score += 1
    elif guess < num:
        print("plus grand")
        score += 1