import random

print("HANGMAN")
print("The game will be available soon.")
# 1-st stage completed
WORLDS = ["python","java"]
word = random.choice(WORLDS)
a = input("Guess the word :\n"">")
while True:
    if a == word:
        print("You survived")
        break
    else:
        print("You lost")
    break
# 2-nd stage completed
lenght = '_' * len(word)
a = input("Guess the word :" + word [:3] + "-".join([''for _ in range (len(word)-3)])+ "-\n>")
if a == word:
    print("You survive!")
else:
    print("You lose!")
#3-rd stage completed

