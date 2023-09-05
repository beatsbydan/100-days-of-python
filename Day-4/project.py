# Rock - Paper - Scissors

import random

print("Welcome to Rock-Paper-Scissors")
user_choice = int(input('Make a choice; 0 = Rock, 1 = Paper, 2 = Scissors: '))
choices = [0, 1, 2]
elements = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
print(f"Computer chose {elements[computer_choice]}")
if(user_choice > 2 or computer_choice < 0):
    print("Invalid number.")
elif user_choice == computer_choice :
    print("You made the same choice as the computer. It's a draw!")
elif user_choice > computer_choice:
    print("You win!")
elif user_choice < computer_choice:
    print("You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose")