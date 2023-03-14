import random

domino_set = [(i, j) for i in range(7) for j in range(i, 7)]

random.shuffle(domino_set)
player_pieces = domino_set[:7]
computer_pieces = domino_set[7:14]
stock_pieces = domino_set[14:]

domino_snake = None
for piece in domino_set[::-1]:
    if piece[0] == piece[1]:
        domino_snake = piece
        break
if domino_snake is None:
    random.shuffle(domino_set)
    player_pieces = domino_set[:7]
    computer_pieces = domino_set[7:14]
    stock_pieces = domino_set[14:]
    domino_snake = stock_pieces.pop()

if domino_snake[0] > domino_snake[1]:
    status = "computer"
else:
    status = "player"

print(f"Stock pieces: {len(stock_pieces)} кістянок в резерві")
print(f"Computer pieces: {len(computer_pieces)} кістянок")
print(f"Player pieces: {len(player_pieces)} кістянок")
print(f"Domino snake: {domino_snake} стартова кісточка")
print(f"Status: гравець {status} ходить першим")