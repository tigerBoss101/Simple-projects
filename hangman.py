#Random hangman project

import random
words = ['beneficiary', 'chimney', 'realize', 'word', 'harbor', 'infection', 'nationalist', 'breed', 'inflate', 'domination']
selected = random.choice(words)
lives = 7
wrong = correct = ""
while lives > 0:
    print("Lives: " + str(lives))
    print(" ".join([l if l in correct else "_" for l in selected]))
    print("Wrong: " + " ".join(list(wrong)))
    letter = input(">>")
    if len(letter) in range(2, len(selected)):
        print("Guess letters or the whole word only!")
        continue
    if letter == selected:
        break
    elif letter in set(selected):
        correct += letter
    else:
        lives -= 1
        if lives == 0:
            break
        if len(letter) == 1:
            wrong += letter if not (letter in wrong) else ""
    if set(correct) == set(selected):
        break
if lives == 0:
    print("Game over! The word is {}.".format(selected))
else:
    print("Congratulations! The word is {}.".format(selected))
input()