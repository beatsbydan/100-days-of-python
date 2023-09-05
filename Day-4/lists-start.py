import random

my_list = ['Daniel']
my_list.append('Onyeachonam')
print(my_list)
my_list.extend(['aka', 'chonam', 'beatsbydan.dev'])
print(my_list)

# Banker - Roulette 
friends = input("Please enter the all the names in your friend group separated by a comma: \n")
friends_list = friends.split(', ')

position = random.randint(0, (len(friends_list) - 1))
print(f"{friends_list[position]} is going to buy the meal today!")

# Alternative code
person_to_pay = random.choice(friends_list)
print(f"{person_to_pay} is going to buy the meal today!")

# Treasure Map
row_1 = ["😌", "😌", "😌"]
row_2 = ["😌", "😌", "😌"]
row_3 = ["😌", "😌", "😌"]
map = [row_1, row_2, row_3]

# first digit is column, second is row
position = input("Where do you want to put the treasure? ")
col_position = int(position[0]) - 1
row_position = int(position[1]) - 1
map[row_position][col_position] = "X"
print(f"{row_1}\n{row_2}\n{row_3}")