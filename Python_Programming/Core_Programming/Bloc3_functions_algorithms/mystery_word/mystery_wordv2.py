mystery_word = "python"

guess =input("Guess the word? ")
count = 0
for letter in guess:
    mystery_letter = list(mystery_word)#turn it into a list
    for i in mystery_letter:
        if i == letter:
            count += 1

print(count)