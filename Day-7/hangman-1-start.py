# Hangman - game

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

display = []

for letter in chosen_word:
    display.append("_")
    
not_complete =  True
lives = 6

while not_complete:
    user_guess = input("Guess a letter: ").lower()
    
    if user_guess in display:
        print(f"You already guessed the letter {user_guess}.")        
    
    for i in range(0, len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = user_guess
            
    if user_guess not in chosen_word:
        print(f"You guessed '{user_guess}' and it isn't in the word")
        lives -= 1
        print(f"You have {lives} attempts remaining")
        if lives == 0:
            not_complete = False
            print("Sorry, You_lose!")
    
    if "_" not in display:
        not_complete = False
        print('You win!')
        
    print(display)
