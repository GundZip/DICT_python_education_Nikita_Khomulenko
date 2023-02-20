print('Made by GundZip')
print('Напиши "help" для списку команд ')

def plain():
    return input("Enter plain text (Звичайний текст) >")

def bold():
    return "**" + input("Enter bold text ( Жирний текст) >") + "**"

def italic():
    return "*" + input("Enter italic text ( Курсив)>") + "*"

def inline_code():
    return "`" + input("Enter inline-code text (Вбудований код) >") + "`"

def link():
    return "[" + input("Enter link label text >") + "]"\
           + "(" + input("Enter URL text >") + ")"

def header():
    return "#" * int(input("Enter header level (Введіть рівень заголовка)>")) + " " + input\
        ("Enter header text (Введіть текст заголовка) >")

def ordered_list():
    num_rows = int(input("Enter number of rows (Введіть кількість рядків) >"))
    return "\n".join([str(i+1) + ". " + input(f"Enter {i+1} row >") for i in range(num_rows)])

def unordered_list():
    num_rows = int(input("Enter number of rows (Введіть кількість рядків)>"))
    return "\n".join(["- " + input(f"Enter {i+1} row >") for i in range(num_rows)])

def newline():
    return "\n"



command_list = [
    "plain",
    "bold",
    "italic",
    "inline_code",
    "link",
    "header",
    "ordered_list",
    "unordered_list",
    "newline",
    "help",
    "save_and_done"
]


def help():
    print("Доступні команди > " + ", ".join(command_list))

def save_and_done():
    print("Дякуємо за використання, увесь текст збережено в 'output.md'!")


_final_text_ = ""
while True:
    user_command = input("Choose a formatter  > ")
    if user_command == "save_and_done":
        break
    elif user_command == "help":
        help()
    elif user_command in command_list:
        _final_text_ += eval(user_command)()
        print(_final_text_)
    else:
        print("Choose possible command")


with open("output.md", "w") as f:
    f.write( _final_text_ )
    save_and_done()