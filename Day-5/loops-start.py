fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

# Average Height
heights = input("Input a list of students height spaced: ").split()
for i in range(0, len(heights)):
    heights[i] = int(heights[i])
total_height = 0
for height in heights:
    total_height = total_height + height
avg_height = round(total_height / len(heights))
print(avg_height)

# Max Score
scores = input("Input a list of scores spaced: ").split()
highest_score = 0
for i in range(0, len(scores)):
    scores[i] = int(scores[i])
for score in scores:
    if score > highest_score :
        highest_score = score
print(highest_score)

# Adding even numbers
sum = 0
for i in range(0, 101):
    if (i % 2 == 0):
        sum += i
print(sum)

# Fizz Buzz
for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    if i % 3 == 0:
        print("Fizz")
    else:
        print(i)