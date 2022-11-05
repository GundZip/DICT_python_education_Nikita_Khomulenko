

#print("Starting to make a coffee")
#print("Grinding coffee beans")
#print("Boiling water")
#print("Mixing boiled water with crushed coffee beans")
#print("Pouring coffee into the cup")
#ptint("Pouring some milk into the cup")
#print("Coffee is ready!")

n_water = 180
n_coffee = 15
n_milk = 55

water = int(input("Write how many ml of water the coffee machine has:\n>"))
coffee = int(input("Write how many ml of milk the coffee machine has :\n"))
milk = int(input("Write how many ml of milk the coffee machine has :\n"))
need_cups = int(input("Write how many cups of coffee will tou need :\n "))
cup_coffee = mun([water // n_water,milk // n_milk, coffee // n_coffee])
if cup_coffee == need_cups:
    print ("Yes, I can make that amount of coffee")
elif cup_coffee > need_cups:
    print("Yes, I can make that amount of coffee(and even", cup_coffee - need_cups, "more than that")
else:
    print("No, I can make only",cup_coffee,"cups of coffee")
