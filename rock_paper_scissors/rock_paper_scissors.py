import random

print ("Welcome \n" \
       " Power by Stell! \n"
       "Select one: rock, paper, scissors ")

options = ["rock", "paper", "scissors"]

user_choice = input()

computer_choice = random.choice(options)

print("Computer chose", computer_choice)

if user_choice == computer_choice:
    print("There is a draw!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_choice == "paper" and computer_choice == "rock":
    print("You win!")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("Computer wins!")
print("Have a nice day!")