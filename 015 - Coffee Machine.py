MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def give_report(current_resources, current_amount_held):
    """Takes a dictionary of resources and money_amount as input and prints the current amount of those resources on
    the console"""
    print(f"Water: {current_resources['water']}ml")
    print(f"Milk: {current_resources['milk']}ml")
    print(f"Coffee: {current_resources['coffee']}g")
    print(f"Money: ${current_amount_held}")


def are_resources_sufficient(req_ingredients, available_resources):
    """Takes requirements for a coffee type and currently available resources as input and returns True if resources
    are sufficient or False otherwise"""
    for key in req_ingredients:
        if available_resources[key] < req_ingredients[key]:
            print(f"Sorry, there's not enough {key}.")
            return False
    return True


def process_coins(money, coffee_type, cost):
    """Processes if coins inserted are sufficient to cover the coffee cost or not, also returns the money received"""
    input_amount = int(input("How many Quarters? ")) * 0.25
    input_amount += int(input("How many Dimes? ")) * 0.1
    input_amount += int(input("How many Nickels? ")) * 0.05
    input_amount += int(input("How many Pennies? ")) * 0.01
    if input_amount >= cost:
        input_amount -= cost
        money += cost
        print(f"Here is ${round(input_amount, 2)} in change.")
        print(f"Here is your {coffee_type} 🍮 Enjoy!")
        return money, True
    else:
        print("Sorry, that's not enough amount. Money refunded.")
        return money, False


def deduct_resources(current_resources, req_ingredients):
    """Deducts the resources required to make the coffee and returns the remaining resources"""
    for key in req_ingredients:
        current_resources[key] -= req_ingredients[key]
    return current_resources


amount_held = 0.0
is_running = True
while is_running:
    response = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if response in MENU:
        coffee_ingredients = MENU[response]["ingredients"]
        coffee_cost = MENU[response]["cost"]

        if are_resources_sufficient(coffee_ingredients, resources):
            amount_held, is_transaction_successful = process_coins(amount_held, response, coffee_cost)
            if is_transaction_successful:
                resources = deduct_resources(resources, coffee_ingredients)
    elif response == "report":
        give_report(resources, amount_held)
    elif response == "off":
        is_running = False
    else:
        print("Invalid choice.")
