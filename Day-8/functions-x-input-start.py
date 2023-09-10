import math

def greet():
    print('Hi')
    print('Daniel')
    print('Onyeachonam')
    
greet()

def greet_anyone(name):
    print(f"Hi {name}")
greet_anyone("Daniel")

# Print_cans
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

def print_can (height, width, coverage):
    cans = math.ceil((height * width) / coverage)
    print(f"You need {cans} cans.")

print_can(height = test_h, width = test_w, coverage = coverage )


# Prime number checker
number = int("Input number to be checked: ")

def prime_checker(num):
    is_prime = False
    for i in range(2, num):
        if num % i != 0:
            is_prime = True
    if is_prime:  
        print(f"{num} is a prime number")  
    else:
        print(f"{num} is not a prime number")