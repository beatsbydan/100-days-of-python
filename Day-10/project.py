# Calculator App

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}

def calculator() :
    num1 = float(input("Enter the first number: "))
    for key in operations:
        print(key)
        
    still_calculating = True
    while still_calculating:
        operation = input("Enter Operation from operations above: ")
        num2 = float(input("Enter the next number: "))
        curr_func = operations[operation]
        answer = curr_func(num1, num2)
        print(f"{num1} {operation} {num2} = {answer}.")
        if input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calculation." == 'y'):
            num1 = answer
        else:
            still_calculating = False
            calculator()
            
calculator()