first_num = int(input("Enter your first number:"))

str1 = "your first number is: "


print(str1 + str(first_num))

firstnumber = first_num

second_num = int(input("Enter your second number"))

str2 = "your second number is: "

print(str2 + str(second_num))

second_number = second_num

operator = str(input("What would you like to do with these numbers?" + " "))

if operator == "multiply":
    print(first_num * second_num)

if operator == "divide":
    print(first_num / second_num)

if operator == "add":
    print(first_num + second_num)

if operator == "subtract":
    print(first_num - second_num)
