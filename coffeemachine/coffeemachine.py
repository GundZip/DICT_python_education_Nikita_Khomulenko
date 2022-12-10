
print("Hello user")
print("In a Machine = 1000-water , 540-milk , 120-coffee , 9-cups")
class Machine:
    grn = 1100
    water = 1000
    milk = 540
    coffee = 120
    cups = 9
    counter = 0
    status = "wait"

    def action(self, command):
        if command == "buy":
            self.status = "make"
        elif command == "fill":
            self.status = "fill"
            self.counter = 0
        elif command == "take":
            print(f"I gave you {self.grn}")
            self.grn = 0
        elif command == "remaining":
            print("The coffee machine has:")
            print(f"{self.water} of water")
            print(f"{self.milk} of milk")
            print(f"{self.coffee} of coffee")
            print(f"{self.cups} of disposable cups")
            print(f"{self.grn} of money")
        elif self.status == "make":
            try:
                type = int(command)
            except:
                type == 4
            if type == 4:
                self.status = "wait"
                return
            if type == 1:
                self.m_coffee(4, 250, 16) #espresso
            elif type == 2:
                self.m_coffee(7, 350, 20, 75) #latte
            elif type == 3:
                self.m_coffee(6, 200, 10, 100) #cappuccino
            self.status = "wait"
        elif self.status == "fill":
            v = int(command)
            if self.counter == 0:
                self.water += v
            elif self.counter == 1:
                self.coffee += v
            elif self.counter == 2:
                self.milk += v
            elif self.counter == 3:
                self.cups += v
            elif self.counter == 4:
                self.grn += v
                self.status = "wait"
                self.counter = -1
            self.counter += 1
        else:
            self.status = "wait"
    def m_coffee(salf, take_grn, n_water, n_coffee, n_milk = 0):
        if salf.water < n_water:
            print("Sorry, not enough water!")
        elif salf.coffee < n_coffee:
            print("Sorry, not enough coffee!")
        elif salf.milk < n_milk:
            print("Sorry, not enough milk!")

        else:
            print("I have enough resources, making you a coffee!")
            salf.water -= n_water
            salf.coffee -= n_coffee
            salf.milk -= n_milk
            salf.cups -= 1
            salf.grn += take_grn


coffee_machine = Machine()
while True:
    action = input("Write action (buy, fill, take, remaining, exit):\n>")
    coffee_machine.action(action)
    if action == "buy":
        type_of_coffee = input("What do you want to buy?  1- espresso, 2 - latte, 3 - cappuccino , 4 - back for menu "
                               ":\n>")
        coffee_machine.action(type_of_coffee)
    elif action == "fill":
        water = input("Write how many ml of water you want to add:\n>")
        coffee_machine.action(water)
        milk = input("Write how many ml of milk you want to add:\n>")
        coffee_machine.action(milk)
        coffee = input("Write how many grams of coffee beans you want to add:\n>")
        coffee_machine.action(coffee)
        cups = input("Write how many disposable coffee cups you want to add:\n>")
        coffee_machine.action(cups)
        grn = input("Write how many money you want to add:\n>")
        coffee_machine.action(grn)
    elif action == "exit":

        break
print("Have a nice day!")



