#commented code is old code lol

while True:
    first_num = input("Enter your first number:") 

    try:
        first_num = float(first_num)
        print("your first number is" + " " + str(first_num))
        break

    except ValueError:
        print("Please enter a valid number")
        print( )




#first_num = int(input("Enter your first number:"))

#str1 = "your first number is: "


#print(str1 + str(first_num))

firstnumber = first_num

while True:
    second_num = input("Enter your second number:") 

    try:
        second_num = float(second_num)
        print("your second number is" + " " + str(second_num))
        break

    except ValueError:
        print("Please enter a valid number")
        print( )


#second_num = int(input("Enter your second number"))

#str2 = "your second number is: "

#print(str2 + str(second_num))

secondnumber = second_num

operator = str(input("What would you like to do with these numbers?" + " "))

if operator == "multiply":
    print(firstnumber * secondnumber)

if operator == "divide":
    print(firstnumber / secondnumber)

if operator == "add":
    print(firstnumber + secondnumber)

if operator == "subtract":
    print(firstnumber - secondnumber)