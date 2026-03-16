# write a program that reads two numbers and check which one is greater 
number = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
if number > number2:
    print("The first number is greater than the second number.")
elif number < number2:
    print("The second number is greater than the first number.")
else:
    print("Both numbers are equal.")
