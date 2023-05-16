import random
options = ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper',
           'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire']
def choose_option(options):
    return random.choice(options)
#----------------------------------------------------------------------------------------------------------------------#
print ("Welcome \n" \
       " Power by Stell! ")

user_name = input("Enter your name: ")
print("Hello, " + user_name)

user_score = 0

with open('rating.txt', 'r') as file:
    for line in file:
        name, score = line.split()
        if name == user_name:
            user_score = int(score)


print("Okay, let's start \n"
      "Select one choice :rock, gun, lightning, devil, dragon, water, air, paper,"
           "sponge, wolf, tree, human, snake, scissors, fire \n and !help")

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
        print(f"Your rating: {user_score}")
#----------------------------------------------------------------------------------------------------------------------#
    computer_choice = choose_option(options)
    if user_choice == computer_choice:
        print(f"There is a draw ({computer_choice})")
        user_score += 50
    elif user_choice == 'rock':
        if computer_choice in ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
    elif user_choice == 'gun':
        if computer_choice in ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
    elif user_choice == 'lightning':
        if computer_choice in ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'devil':
        if computer_choice in ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake',
         'scissors', 'fire', 'rock', 'gun']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'dragon':
        if computer_choice in ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors',
         'fire', 'rock', 'gun', 'lightning']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'water':
        if computer_choice in ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire',
         'rock', 'gun', 'lightning', 'devil']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'air':
        if computer_choice in ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock',
        'gun', 'lightning', 'devil', 'dragon']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'paper':
        if computer_choice in ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun',
        'lightning', 'devil', 'dragon', 'water']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'sponge':
        if computer_choice in ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning',
         'devil', 'dragon', 'water', 'air']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'wolf':
        if computer_choice in ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil',
         'dragon', 'water', 'air', 'paper']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'tree':
        if computer_choice in ['human', 'snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil',
        'dragon', 'water', 'air', 'paper', 'sponge']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'human':
        if computer_choice in ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water',
        'air', 'paper', 'sponge', 'wolf']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'snake':
        if computer_choice in ['scissors', 'fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air',
        'paper', 'sponge', 'wolf', 'tree']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'scissors':
        if computer_choice in ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge',
         'wolf', 'tree', 'human']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    elif user_choice == 'fire':
        if computer_choice in ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge',
         'wolf', 'tree', 'human', 'snake']:
            print(f"Well done. The computer chose {computer_choice} and failed")
            user_score += 100
    else:
            print(f"Sorry, but the computer chose {computer_choice}")
            print("Your rating:",user_score)
print("Have a nice day!")
#----------------------------------------------------------------------------------------------------------------------#
with open('rating.txt', 'r+') as file:
    data = file.read()
    file.seek(0)
    for line in data.split('\n'):
        if line.startswith(user_name):
            file.write(f"{user_name} : {user_score}\n")
        elif line:
            file.write(f"{line}\n")
    else:
        file.write(f"{user_name} : {user_score}\n")
