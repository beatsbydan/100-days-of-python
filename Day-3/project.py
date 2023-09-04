# Treasure-Island
print("Welcome to Treasure Island. ")
print("Your mission is to find the treasure. ")
step_choice = input("We're at the beginning. Type left or right to continue: ").lower()
if step_choice == "right":
    print("Oops, You ran off a cliff. GAME OVER")
else:    
    swim_or_wait = input("Lovely! We're at a bridge. Do you wanna swim or wait? Type swim or wait: ").lower()
    if swim_or_wait == "swim":
        print("Oops, you drowned. GAME OVER")
    else:
        door = input("Hehe.. You made it to the other side. There are three rooms; one of which holds your treasure. Pick a door. Type blue, yellow or red: ").lower()  
        if (door == "red") or (door == "blue"): 
            print("Wrong move. Game Over")
        else:
            print("Congratulations! You win")