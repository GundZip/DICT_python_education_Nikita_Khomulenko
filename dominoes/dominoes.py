
print("="*70)
print(" "*30 + "SNAKE BONES GAME")
print("="*70)


stock_size = 20
computer_pieces = 0
print("Stock size:", stock_size)
print("Computer pieces:", computer_pieces)

snake = ["*"]
player_pieces = ["1", "2", "3", "4", "5"]
print("Snake:", " ".join(snake))
print("Your pieces:")
for i, piece in enumerate(player_pieces):
    print(i+1, "-", piece)

status = "computer"
if status == "computer":
    print("Status: Computer is about to make a move. Press Enter to continue...")
elif status == "player":
    print("Status: It's your turn to make a move. Enter your command.")