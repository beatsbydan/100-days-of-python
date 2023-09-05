import random

# Password generator
print("Welcome to the PyPassword Generator")

my_letters = [
    "A","B","C","D","E","F","G","H","I",
    "K","L","M","N","O","P","Q","R","S",
    "T","U","V","W","X","Y","Z"
]
my_numbers = ["0","1","2","3","4","5","6","7","8","9"]
my_symbols = ["!", "#", "$", "%", "&", "(",")", "*", "+"]

letters = int(input("How many letters would you like in your password? \n"))
symbols = int(input("How many symbols would you like in your password? \n"))
numbers = int(input("How many numbers would you like in your password? \n"))

password = ""
password_list = []

for i in range(1, letters + 1 ):
    random_letter = random.choice(my_letters)
    password_list.append(random_letter)
for i in range(1, symbols + 1 ):
    random_symbol = random.choice(my_symbols)
    password_list.append(random_symbol)
for i in range(1, numbers + 1 ):
    random_number = random.choice(my_numbers)
    password_list.append(random_number)
    
for letter in password_list:
    random_password = random.choice(password_list)
    password += random_password
print(f"Here is your password: {password}")