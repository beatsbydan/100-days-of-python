import random

cards = [11, 2, 3, 4, 5 , 6, 7, 8, 9, 10, 10, 10, 10]
def calc_score(my_cards) :
    if sum(my_cards) == 21 and len(my_cards) == 2:
        return 0
    if 11 in my_cards and sum(cards) > 21:
        my_cards.remove(11)
        my_cards.append(1)
        
    return sum(my_cards)

def compare_score (user, comp):
    if user == comp:
        return "Draw"
    elif comp == 0:
        return "You Lose, opponent has a BlackJack"
    elif user == 0:
        return "You Win with a BlackJack"
    elif user > 21: 
        return "You went over. You lose"
    elif comp > 21: 
        return "Opponent went over, You win"
    elif user > comp:
        return 'You win'
    else:
        return "You lose"
# Dealer
def deal_card ():
    card = random.choice(cards)
    return card

def play_game():
    game_over = False
    user_cards = []
    comp_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())
        
    while not game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"Your cards: {user_cards}, current_score: {user_score}")
        print(f"Computer's first card: {comp_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            new_deal = input("Type 'y' to get another card or 'n' to pass: ")
            if new_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calc_score(comp_cards)

    print(f"Your final hand: {user_cards}, score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, score: {comp_score}")

    print(compare_score(user=user_score, comp=comp_score ))

play_game()

if input("Do you wanna play again? 'y' or 'n': ") == 'y':
    play_game()
