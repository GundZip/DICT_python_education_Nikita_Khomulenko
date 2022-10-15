import random

print("HANGMAN")
print("The game will be available soon.")
WORLDS = ["python", "java", "php", "javascript"]
word = random.choice(WORLDS)
remember_letters = []
all_letters = list(set(word))
words =''.join([i if i in remember_letters else "_"for i in word])
print(words)
life = 8
while life > 0:
    letter = input("input a letter:")
    if letter in word and letter not in remember_letters:
        remember_letters.append(letter)
        all_letters.remove(letter)
    if letter not in word:
        life -= 1
        print("That letter doesn`s appear un the word")
    if letter  in remember_letters:
        print(" Cool")
    words = ''.join([i if i in remember_letters else "_" for i in word])
    print(words)
    if len(all_letters) == 0:
        break

print("thanks for playing\nWe'll see how well you did in the next stage")
#6-th stage completed




