from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_running = True
amount_held = 0.0
while is_running:
    response = input(f"What would you like? ({menu.get_items()}): ").lower()

    if response == "report":
        coffee_maker.report()
        money_machine.report()
    elif response == "off":
        is_running = False
    elif response == "espresso" or response == "latte" or response == "cappuccino":
        drink = menu.find_drink(response)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
    else:
        print("Invalid response.")