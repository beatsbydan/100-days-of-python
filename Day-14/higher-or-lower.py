import gamedata
from gamedata import data
import random

is_winning = True
score = 0
def compare(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        print("They have the same followers")

compare_param1 = random.choice(data)
print(compare_param1)
while is_winning:
    compare_param2 = random.choice(data)
    followers_1 = compare_param1['follower_count']
    followers_2 = compare_param2['follower_count']
    largest_followers = compare(followers_1, followers_2)
    print(f"Compare A, '{compare_param1['name']}' against B, '{compare_param2['name']}'")
    choice = input("Who has more followers? Type 'A' or'B': ")
    if choice == 'A':
        if largest_followers == followers_1:
            score += 1
            print(f"You're right! Current score: {score}")
            compare_param1 = compare_param1
        else:
            print(f"You're wrong! Current score: {score}")
            is_winning = False
    else:
        if largest_followers == followers_2:
            score += 1
            print(f"You're right!, Current score: {score}")
            compare_param1 = compare_param2
        else:
            print(f"You're wrong! Current score: {score}")
            is_winning = False