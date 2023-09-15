import random

print("Welcome to the Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

random_num = random.randint(1, 100)
chances = 0
is_guessing = True
if difficulty == "easy":
    chances = 10
else:
    chances = 5
print(f"You have {chances} tries to guess this number. Let's go!")
while is_guessing and chances > 0:
    choice = int(input("Make a guess: "))
    if choice > random_num:
        print("Too high, make another guess.") 
        chances -= 1
        print(f"You have {chances} tries left.")
    elif choice < random_num:
        print("Too low, make another guess.")
        chances -= 1
        print(f"You have {chances} tries left.")
    else:
        print(f"You got it. The answer was {random_num}.") 
        is_guessing = False
if chances == 0:
    print("You lose")