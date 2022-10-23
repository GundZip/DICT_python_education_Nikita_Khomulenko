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
#1-st stage completed
cost = int(input('Enter the totat amount:\n'))
#2-nd stage completed

YoR = {'yes': True, 'no': False}

print('Do you want to use "who is lucky?" feature\n type yes/no')
lucky = YoR[input('>').lower()]
l_name = '_'
if lucky:
    l_name = random.choice(list(transactions.keys()))
    print(l_name, "is lucky today!")
else:
    print('No one is going to be lucky')
# 3-rd stage completed

all_price  = round(cost / (amount - int(lucky)), 2)
for t in transactions.keys():
    transactions[t] = all_price
if lucky:
    transactions[l_name] = 0
print(transactions)
print('End DinnerParty')
#Final stage


