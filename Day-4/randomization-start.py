import random

random_integer = random.randint(1,10)
print(random_integer)
random_float = random.random()
print(random_float)
random_float_between_zer_and_five = random.random() * 5

# Heads or Tails
random_choice = random.randint(0,1)
if random_choice == 1:
    print("Heads")
else:
    print("Tails")