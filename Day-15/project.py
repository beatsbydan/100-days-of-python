flavours = [
    {
        'name': 'Espresso',
        'water': 50,
        'coffee': 18,
        'milk': 0,
        'price': 1.50
    },
    {
        'name': 'Latte',
        'water': 200,
        'coffee': 24,
        'milk': 150,
        'price': 2.50
    },
    {
        'name': 'Cappuccino',
        'water': 250,
        'coffee': 24,
        'milk': 100,
        'price': 3.00
    }
]
machine_resources = {
    'water': 300,
    'milk':200,
    'coffee':100,
    'money': 0
}
coins = {
        'pennies': 0.01,
        'dimes': 0.10,
        'nickles': 0.05,
        'quarters': 0.25
    }

making_coffee = True
to_produce = ''

def report():
    print(f"Water: {machine_resources['water']}ml\nMilk: {machine_resources['milk']}ml\nCoffee: {machine_resources['coffee']}g\nMoney: ${machine_resources['money']}")

def available_to_produce(coffee):
    if machine_resources['water'] > coffee['water']:
        if machine_resources['coffee'] > coffee['coffee']:
            if machine_resources['milk'] > coffee['milk']:
                return True
            else:
                return False
        else:
            return False
    else:
        return False
    
def produce(coffee):
    current_flavour = {}
    
    for i in range (0, len(flavours)):
        if flavours[i]['name'].lower() == coffee:
            current_flavour = flavours[i]
            
    print("Please insert coins")
    
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    
    total_quarters = quarters * coins['quarters']
    total_pennies = pennies * coins['pennies']
    total_nickles = nickles * coins['nickles']
    total_dimes = dimes * coins ['dimes']
    total_coins = round((total_quarters + total_dimes + total_nickles + total_pennies), 2)
    
    print(total_coins)
    
    if total_coins > current_flavour['price']:
        change = round(total_coins - current_flavour['price'], 2)
        if available_to_produce(current_flavour):
            
            machine_resources['water'] -= current_flavour['water']
            machine_resources['coffee'] -= current_flavour['coffee']
            machine_resources['milk'] -= current_flavour['milk']
            machine_resources['money'] += current_flavour['price']

            print(f"Here's ${change} change.\n Here's your {coffee}, enjoy!")
        
        else:
            print(f"Can't make your {coffee} right now.\nHere's a refund of ${total_coins}.")
    
    elif total_coins == current_flavour['price']:
        if available_to_produce(current_flavour):
            
            machine_resources['water'] -= current_flavour['water']
            machine_resources['coffee'] -= current_flavour['coffee']
            machine_resources['milk'] -= current_flavour['milk']
            machine_resources['money'] += current_flavour['price']
            
            print(f"Here's your {coffee}, enjoy!")
        
        else:
            print(f"Can't make your {coffee} right now.\nHere's a refund of ${total_coins}.")
    
    else:
        print(f"To get your {coffee} you need ${current_flavour['price']}.\nHere's a refund of ${total_coins}.")

while making_coffee:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'report':
        report()
    elif choice == 'espresso':
        to_produce = 'espresso'
        produce(to_produce)
    elif choice == 'latte':
        to_produce = 'latte'
        produce(to_produce)
    elif choice == 'cappuccino':
        to_produce = 'cappuccino'
        produce(to_produce)