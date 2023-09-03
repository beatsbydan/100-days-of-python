# Tip-Calculator

print('Welcome to the tip calculator!')
total_bill = float(input('What is the total bill to be paid? '))
percentage_tip = float(input('What percentage tip would you like to give? '))
number_of_persons = int(input('How many people are to split the bill? '))

tip = (percentage_tip / 100) * (total_bill)
tipped_bill = tip + total_bill
bill_per_person = round((tipped_bill / number_of_persons), 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_amount}")