from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

new_coffee_maker = CoffeeMaker()
new_menu = Menu()
new_menu_item = MenuItem()
new_money_machine = MoneyMachine()

is_on = True

while is_on:
    options = new_menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        new_coffee_maker.report()
        new_money_machine.report()
    else:
        drink = new_menu.find_drink(choice)
        if new_coffee_maker.is_resource_sufficient(drink) and new_money_machine.make_payment(drink.cost):
            new_coffee_maker.make_coffee(drink)