import random

print ("Welcome \n" \
       " Power by Stell! \n"
       "Select one: rock, paper, scissors ")

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Enter your move: ")

    if user_input == "exit":
        print("Bye!")
        break

    if user_input in options:
        computer_move = random.choice(options)
        if user_input == 'rock' and computer_move == 'paper' or \
                user_input == 'paper' and computer_move == 'scissors' or \
                user_input == 'scissors' and computer_move == 'rock':
            print(f"Lose -> Sorry, but the computer chose {computer_move}")
        elif user_input == computer_move:
            print(f"Draw -> There is a draw ({computer_move})")
        else:
            print(f"Win -> Well done. The computer chose {computer_move} and failed")
    else:
        print("Invalid input")
print("Have a nice day!")