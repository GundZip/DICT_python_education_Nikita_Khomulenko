import random

print("Hello user \n Power by Stell" )

def generate_question():
    # генерація від 2 до 9
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(["+", "-", "*"])
    question = f"{num1} {operator} {num2} = "
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

def main():
    question, answer = generate_question()
    print(question)
    user_answer = int(input())
    if user_answer == answer:
        print("Right!")
    else:
        print("Wrong!")
def check_input(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        print("Incorrect format.")
        return False

def main():
    num_correct = 0
    for i in range(5):
        question, answer = generate_question()
        print(question)
        while True:
            user_answer = input()
            if check_input(user_answer):
                break
        if int(user_answer) == answer:
            print("Right!")
            num_correct += 1
        else:
            print("Wrong!")
    #  кількість правильних відповідей
    print(f"Your mark is {num_correct}/5.")
    print("Goodbye \n Have a nice day")
if __name__ == '__main__':
    main()

