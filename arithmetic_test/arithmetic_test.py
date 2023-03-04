import random

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

if __name__ == '__main__':
    main()
