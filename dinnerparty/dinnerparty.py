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
price = int(input('Enter the totat amount:\n'))
a = round(price/amount, 2)
for name in transactions:
    transactions[name] = a
print(transactions)

YoR = {'yes': True, 'no': False}

print('Do you want to use "who is lucky?" feature\n type yes/no')
lucky = YoR[input('>').lower()]
l_name = '_'
if lucky:
    l_name = random.choice(list(transactions.keys()))
    print(l_name, "is lucky today!")

