import random
print ("Welcome \n" \
       " Power by Stell! ")

user_name = input("Enter your name: ")
print("Hello, " + user_name)

user_score = 0
with open('rating.txt', 'r') as f:
    for line in f:
        name, score = line.strip().split()
        if name == user_name:
            user_score = int(score)
            break

print("Okay, let's start \n"
      "Select one choice : rock, paper, scissors and !help")

while True:

    user_choice = input()
    if user_choice == "!exit":
        print("Bye!")
        break
    if user_choice == '!help':
         print("Available commands: ")
         print("!exit - quit the game")
         print("!rating - show your rating")
         continue

    elif user_choice == "!rating":
        print("Your rating:", user_score)

    elif user_choice in ["rock", "paper", "scissors"]:
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        if user_choice == computer_choice:
            print(f"There is a draw ({computer_choice})")
            user_score += 50

        elif (user_choice == "rock" and computer_choice == "scissors" or
              user_choice == "scissors" and computer_choice == "paper" or
              user_choice == "paper" and computer_choice == "rock"):
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
    else:
        print("Invalid input")

    print("Your rating:",user_score)

print("Have a nice day!")