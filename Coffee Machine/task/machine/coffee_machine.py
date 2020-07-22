class CoffeeMachine:

    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.action = input("Write action (buy, fill, take, remaining, exit):\n")
        self.coffee_type = None

    def __str__(self):
        return "The coffee machine has:\n" \
               "{} of water\n" \
               "{} of milk\n" \
               "{} of coffe beans\n" \
               "{} of disposable cups\n" \
               "${} of money".format(self.water, self.milk, self.beans, self.cups, self.money)

    def to_buy(self):
        self.coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if self.coffee_type == "1":
            if self.water >= 250 and self.beans >= 16 and self.cups >= 1:
                self.water -= 250
                self.beans -= 16
                self.money += 4
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 250:
                print("Sorry, not enough water!\n")
            elif self.beans < 16:
                print("Sorry, not enough coffe beans!\n")
            elif self.cups == 0:
                print("Sorry, not enough cups!\n")
        elif self.coffee_type == "2":
            if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.cups >= 1:
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.money += 7
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 350:
                print("Sorry, not enough water!\n")
            elif self.milk < 75:
                print("Sorry, not enough milk!\n")
            elif self.beans < 20:
                print("Sorry, not enough beans!\n")
            elif self.cups == 0:
                print("Sorry, not enough cups!\n")
        elif self.coffee_type == "3":
            if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.cups >= 1:
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.money += 6
                self.cups -= 1
                print("I have enough resources, making you a coffee!\n")
            elif self.water < 200:
                print("Sorry, not enough water!\n")
            elif self.milk < 100:
                print("Sorry, not enough milk!\n")
            elif self.beans < 12:
                print("Sorry, not enough beans!\n")
            elif self.cups == 0:
                print("Sorry, not enough cups!\n")
        elif self.coffee_type == "back":
            self.action = input("Write action (buy, fill, take, remaining, exit):\n")


    def to_fill(self):
        self.add_water = int(input("Write how many ml of water do you want to add:\n"))
        self.add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        self.add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.add_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.water += self.add_water
        self.milk += self.add_milk
        self.beans += self.add_beans
        self.cups += self.add_cups

    def to_take(self):
        print("I gave you ${}".format(self.money))
        self.money = 0


coffee = CoffeeMachine()

while True:
    if coffee.action == "buy":
        coffee.to_buy()
    if coffee.action == "fill":
        coffee.to_fill()
    if coffee.action == "take":
        coffee.to_take()
    if coffee.action == "remaining":
        print(coffee)
    if coffee.action == "exit":
        break
    coffee.action = input("Write action (buy, fill, take, remaining, exit):\n")
