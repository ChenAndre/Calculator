while True:
    amount = input("Enter your first number:") 

    try:
        amount = float(amount)
        print("your first number is" + " " + str(amount))
        break

    except ValueError:
        print("Please enter a valid number")
        print( )

