# Add the two digits of a two-digit number
number = input('Enter number: ')
print(int(number[0]) + int(number[1]))

# # BMI calculator
weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

bmi = weight / (height ** 2)
print(round(bmi, 2))

# Life in weeks
age = int(input('Enter your age: '))
years_left = 90 - age 
weeks_left = years_left * 52
days_left = years_left * 365
months_left = years_left * 12
print(f"You have {days_left} days left, {weeks_left} weeks left and  {months_left} months left.")