while True:
    language = input("Choose language (en,ua): ")
    if set(language) <= set("euua"):
        if language == "en":
            # English translations
            Hello = "Hello"
            player = "player"
            str_to_move1 = "It's your turn to make a move. Enter your command."
            str_to_move2 = "Computer is about to make a move. Press Enter to continue..."
            in_move = "Illegal move. Please try again."
            Stock_size = "Stock size"
            PC = "computer"
            us_com1 = "Invalid input.\nWrong input value range.\nPlease try again.\n> "
            us_com2 = "Invalid input.\nEnter only numbers!\nPlease try again."
            status_win = "Status: The game is over. You won!"
            status_lose = "Status: The game is over. The computer won!"
            status_draw = "Status: The game is over. It's a draw!"
            bye = "Have a nice day!"

        elif language == "ua":
            # Ukrainian translations
            Hello = "Вітаю"
            player = "Гравець"
            str_to_move1 = "Твоя черга зробити хід. Введіть свою команду"
            str_to_move2 = "Комп'ютер збирається здійснити рух. Натисніть Enter, щоб продовжити..."
            in_move = "Неможливий хід. Спробуйте ще раз"
            Stock_size = "Розмір запасу"
            PC = "комп'ютер"
            us_com1 = "Недійсне введення.\nНеправильний діапазон введених значень.\nСпробуйте ще раз.\n> "
            us_com2 = "Невірне введення.\nВведіть лише цифри!\nБудь ласка, спробуйте ще раз."
            status_win = "Статус: гра закінчена. Ви виграли!"
            status_lose = "Статус: гра закінчена. Комп’ютер переміг!"
            status_draw = "Статус: Гра завершена. Нічия!"
            bye = "Гарного дня!"
            break
            print("Ошибка! Введите только символы eu и ua.")




