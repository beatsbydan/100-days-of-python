print('Welcome to the rollercoaster')
height = float(input('What is your height in cm? '))
bill = 0
if height >= 120:
    print('You can ride the rollercoaster')
    age = int(input('What is your age? '))
    if age < 12:
        bill = 5
        print('Children tickets are $5.')
    elif age <= 18:
        bill = 7
        print('Youth tickets are $7.')
    elif age >=45 and age <= 55:
        print("Everything is going to be okay. Have a free ride on us!")
    else:
        bill = 12
        print('Adult tickets are $12')
    wants_photo = input("Do you want your photo taken? yes or no: ")
    if(wants_photo == 'yes'):
        bill += 3
    print(f"Your bill is ${bill}.")
else:
    print('Sorry, you have to grow taller before you can ride')

# Love-Calculator
print("Welcome to Love Calculator!")
lover_1 = input("What is your name? \n")
lover_2 = input("What is their name? \n")

joint_names = lover_1 + lover_2
lower_case_lovers = joint_names.lower()

t_count = lower_case_lovers.count('t')
r_count = lower_case_lovers.count('r')
u_count = lower_case_lovers.count('u')
e_count = lower_case_lovers.count('e')

true_count = int(t_count + r_count + u_count + e_count)

l_count = lower_case_lovers.count('l')
o_count = lower_case_lovers.count('o')
v_count = lower_case_lovers.count('v')
e_count = lower_case_lovers.count('e')

love_count = int(l_count + o_count + v_count + e_count)
love_percent =int(str(true_count) + str(love_count))

if (love_percent < 10) or (love_percent > 90):
    print(f"Your score is {love_percent}%, you go together like coke and mentos.")
elif (love_percent >= 40) & (love_percent <= 50):
    print(f"Your love score is {love_percent}%, you are alright together.")
else:
    print(f"Your love score is {love_percent}%")