import re

print("Hello \n Power by Stell! \n write to start - !help")

while True:
    user_choice = input()

    if user_choice == "!exit":
        print("Done!")
        break

    if user_choice == "!example":
        print("Input: '\.$|end.' Output: True \n"
              " '3\+3|3+3=6' Output: True \n"
              " '\?|Is this working?' Output: True \n"
              " '\\|\' Output: True \n"
              "'colou\?r|color' Output: False \n"
              " 'colou\?r|colour' Output: False \n"
              "'^app|apple' Output: True \n"
              "'le$|apple' Output: True \n"
              " '^a|apple' Output: True \n"
              " '.$|apple' Output: True \n"
              " 'apple$|tasty apple' Output: True \n"
              " '^apple|apple pie' Output: True \n"
              " '^apple$|apple' Output: True \n"
              " '^apple$|tasty apple' Output: False \n"
              "^apple$|apple pie' Output: False \n"
              " 'app$|apple' Output: False \n"
              "^le|apple' Output: False")
        break

    if user_choice == '!help':
        print("Available commands: ")
        print("!example")
        print("!exit - quit the help")

        continue

if __name__ == "__main__":
    input_string = input()
    reg_ex = input()
    print(reg_ex + " | " + input_string + " OutPut: " + str(bool(re.search(reg_ex, input_string))))
    print("Bye!")