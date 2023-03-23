import random

print("Made by GundZip \n"
      "Hello")

def possible_moves(player_pieces, snake, game_status):
    moves = []
    left = snake[0][0]
    right = snake[-1][1]
    for i, piece in enumerate(player_pieces):
        if piece[0] == left:
            moves.append((i, "left"))
        if piece[0] == right:
            moves.append((i, "right"))
        if piece[1] == left:
            moves.append((i, "left_flip"))
        if piece[1] == right:
            moves.append((i, "right_flip"))
    if not moves:
        return [(None, None)]
    elif game_status == "player":
        return moves + [(len(player_pieces), "take")]
    else:
        return moves + [(None, None)]

stock = []
for i in range(7):
    for j in range(i, 7):
        stock.append([i, j])
random.shuffle(stock)

comp_pieces = []
player_pieces = []
for i in range(7):
    comp_pieces.append(stock.pop())
    player_pieces.append(stock.pop())

snake = [random.choice(player_pieces)]
status = "player"

# Етап 3: додано ігровий цикл для гри по черзі
game_over = False
while not game_over:
    print("=" * 70)
    print("Stock size:", len(stock))
    print("Computer pieces:", len(comp_pieces))
    print(snake)
    print("Your pieces:")
    for i, piece in enumerate(player_pieces, start=1):
        numbers = [2, 7, 13, 19]
        for i in range(len(numbers)):
            print(f"{i}:{numbers[i]}")


