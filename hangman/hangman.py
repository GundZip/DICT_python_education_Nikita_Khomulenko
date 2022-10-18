import random

print("HANGMAN")
print("The game will be available soon.")
WORLDS = ["python", "C++", "html", "javascript"]
play = True
while play:
    menu = input('Type "play" to play the game, "exit" to quit:\n>')
    while menu not in ["play", "exit"]:
        menu = input('Type "play" to play the game, "exit" to quit:\n>')
    if menu == "play":
        word = random.choice(WORLDS)
        remember_letters = []
        input_letters = []
        all_letters = list(set(word))
        words = "".join([i if i in remember_letters else "_" for i in word])
        print(words)
        life = 8
        while life > 0:
            letter = input("Input a letter:")
            if letter == letter.lower() and len(letter) == 1:
                if letter in word and letter not in remember_letters and letter not in input_letters:
                    remember_letters.append(letter)
                    all_letters.remove(letter)
                elif letter in remember_letters or letter in input_letters:
                    print("You've already guessed this letter")
                else:
                    print("That letter doesn't appear in the word")
                    life -= 1
                words = "".join([i if i in remember_letters else "_" for i in word])
                print(words)
                if len(all_letters) == 0:
                    print("You guessed the word\nYou survived!")
                    break
            elif letter != letter.lower():
                print("Please enter a lowercase English letter")
            elif len(letter) != 1:
                print("You should input a single letter")
        if len(all_letters) > 0:
            print("You lost!")
    else:
        exit = False
        break
print("thanks for playing\nWe'll see how well you did in the next stage")

#7/8-th stage completed





