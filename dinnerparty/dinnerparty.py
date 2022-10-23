import random

amount = int(input("Enter the number of fiends joining (including you):\n>"))
if amount < 1:
    print('No one is joining for the party')
    exit()
transactions = {}
print ('Enter the name of every friend (including you), each on a new line')
for _ in range(amount):
    name = input(">")
    transactions[name] = 0
