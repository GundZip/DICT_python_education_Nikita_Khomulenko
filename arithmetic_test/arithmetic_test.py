import random

print("Hello user "
      "\n Power by Stell" )
name = input("Enter your name: ")
def simple_operation(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 // num2

def square(num):
    return num * 2

def test():
    level = input("Choose the level of difficulty (1 or 2): ")
    while level not in ["1", "2"]:
        level = input("Incorrect format. Choose the level of difficulty (1 or 2): ")
    if level == "1":
        print("You chose level 1: simple operations with numbers 2-9.")
        operations = ["+", "-", "*", "/"]
        correct_answers = 0
        for i in range(5):
            num1 = random.randint(2, 9)
            num2 = random.randint(2, 9)
            operation = random.choice(operations)
            answer = input(f"{i+1}. {num1} {operation} {num2} = ")
            while not answer.isdigit():
                answer = input("Incorrect format. Enter again: ")
            if int(answer) == simple_operation(num1, num2, operation):
                print("Right!")
                correct_answers += 1
            else:
                print("Wrong!")
        print(f"Your mark is {correct_answers}/5.")
    elif level == "2":
        print("You chose level 2: squaring numbers from 11 to 29.")
        correct_answers = 0
        for i in range(5):
            num = random.randint(11, 29)
            answer = input(f"{i+1}. {num}^2 = ")
            while not answer.isdigit():
                answer = input("Incorrect format. Enter again: ")
            if int(answer) == square(num):
                print("Right!")
                correct_answers += 1
            else:
                print("Wrong!")
        print(f"Your mark is {correct_answers}/5.")
    save_result = input("Would you like to save your result to the file? Enter yes or no: ")
    if save_result.lower() == "yes" or save_result.lower() == "y""YES":
        name = input("Enter your name: ")
        print("you progress save a results.txt "
              "\n Process completed"
              " \n Have a nice day")
        level_description = "simple operations with numbers 2-9" if level == "1" else "squaring numbers from 11 to 29"
        with open("results.txt", "a") as f:
            f.write(f"{name}: {correct_answers}/5 in level {level} ({level_description}).\n")
    else:
        return

test()

