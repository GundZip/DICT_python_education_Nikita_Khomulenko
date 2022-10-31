board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']
currentPlayer = "X"
winner = None
gameRunning = True


def printBoard(board):
    print("=" * 9)
    print("|" + board[0] + " | " + board[1] + " | " + board[2] + "|" )
    print("-" * 9)
    print("|" + board[3] + " | " + board[4] + " | " + board[5] + "|" )
    print("-" * 9)
    print("|" + board[6] + " | " + board[7] + " | " + board[8] + "|" )
    print("=" * 9)


def playerInput(board):
    while True:
        if currentPlayer == "X":
            inp = int(input(f"Coordinates should be from 1 to 9! \033[1;35m Player (X) \033[0;0m : "))
        else:
            inp = int(input(f"This cell is occupied! Choose another one! \033[2;32m Player (0) \033[0;0m : "))
        if inp >= 1 and inp <= 9 and board[inp-1]  == "-":
            board[inp-1] = currentPlayer
            break
        else:
            if currentPlayer == "X":
                print(f"Coordinates should be from 1 to 9! - \033[1;35m Player (X) \033[0;0m ! ")
            else:
                print(f"This cell is occupied! Choose another one! - \033[2;32m Player (0) \033[0;0m ! ")
            printBoard(board)

def valid_coord(game, inp):
    try:
        c_x, c_y = get_coords(inp)
    except Exception:
        print("You should enter numbers!")
        return False

def checkHorizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-")\
            or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = currentPlayer
        return True
def checkRow(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-")\
            or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = currentPlayer
        return True
def checkDiagonal(board):
    global winner
    if (board[0] == board[4] == board[5] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = currentPlayer
        return True

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Draw")
        gameRunning = False

def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"{winner} Wins")


def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

while gameRunning:
    printBoard(board)
    if winner != None:
        break
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
