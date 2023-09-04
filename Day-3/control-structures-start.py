print('Welcome to the rollercoaster')
height = float(input('What is your height in cm? '))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Children tickets are $5.')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    else:
        bill = 12
        print('Adult tickets are $12')
    wants_photo = input("Do you want your photo taken? yes or no: ")
    if(wants_photo == 'yes'):
        bill += 3
    print(f"Your bill is ${bill}.")
else:
    print('Sorry, you have to grow taller before you can ride')

# Odd-or-even
number = int(input('Enter number: '))
if number % 2 == 0:
    print('Number is even.')
else:
    print('Number is odd.')

# BMI 2.0
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight / (height ** 2), 1)
print(bmi)
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
elif bmi < 35:
    print("You are Obese.")
else:
    print("You are clinically Obese.")

# Leap year- A year is a leap year if it is evenly divisible by 4 and 400 but not 100
year = int(input('Enter year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Year is a leap year.")
        else:
            print("Year is not a leap year")
    else:
        print('Year is a leap year.')
else:
    print("Year is not a leap year")
    

# Pizza-Order
print("Welcome to Python Pizza Deliveries")
pizza_size = input("What size of pizza do you want? S, M or L: ")
pepperoni_choice = input("Do you want pepperoni? Y or N: ")
extra_cheese_choice = input("Do you want extra cheese? Y or N: ")

small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

pepperoni_small_price = 2
pepperoni_medium_or_large_price = 3
extra_cheese_price = 1

if pizza_size == "S":
    if pepperoni_choice == "Y":
        if extra_cheese_choice == "Y":
            print(f"Your final bill is ${small_pizza_price + pepperoni_small_price + extra_cheese_price }")   
        else:
            print(f"Your final bill is ${small_pizza_price + pepperoni_small_price}")   
    else:
        if extra_cheese_choice == "Y":
            print(f"Your final bill is ${small_pizza_price + extra_cheese_price }")   
        else:
            print(f"Your final bill is ${small_pizza_price}")
elif pizza_size == "M":
    if pepperoni_choice == "Y":
        if extra_cheese_choice == "Y":
            print(f"Your final bill is ${medium_pizza_price + pepperoni_medium_or_large_price + extra_cheese_price }")   
        else:
            print(f"Your final bill is ${medium_pizza_price + pepperoni_medium_or_large_price}")   
    else:
        if extra_cheese_choice == "Y":
            print(f"Your final bill is ${medium_pizza_price + extra_cheese_price }")   
        else:
            print(f"Your final bill is ${medium_pizza_price}")
else:
    if pepperoni_choice == "Y":
        if extra_cheese_choice == "Y":
            print(f"Your final bill is ${large_pizza_price + pepperoni_medium_or_large_price + extra_cheese_price }")   
        else:
            print(f"Your final bill is ${large_pizza_price + pepperoni_medium_or_large_price}")   
    else:
        if extra_cheese_choice == "Y":
            print(f"Your final bill is ${large_pizza_price + extra_cheese_price }")   
        else:
            print(f"Your final bill is ${large_pizza_price}")    