def get_operator():
    """Prompt the user to enter an arithmetic operator."""
    operators = ['+', '-', '*', '/', '**']
    while True:
        operator = input("Enter an arithmetic operator (+, -, *, /, **): ")
        if operator in operators:
            return operator
        else:
            print("Invalid operator. Please try again.")

def get_number(prompt):
    """Prompt the user for a number and ensure it's a valid float."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number. Please try again.")

def calculator():
    """A user-friendly calculator that asks for an operator and numbers to compute a simple arithmetic operation."""
    operator = get_operator()
    number_of_inputs = int(get_number("How many numbers do you want to operate on? "))
    
    if number_of_inputs < 2:
        print("Please enter at least two numbers for the operation.")
        return

    # Get the first number
    result = get_number("Enter number 1: ")

    # Perform the operation with the subsequent numbers
    for i in range(1, number_of_inputs):
        next_number = get_number(f"Enter number {i+1}: ")
        expression = f"({result}) {operator} ({next_number})"
        result = eval(expression)

    print(f"The result is: {result}")

calculator()