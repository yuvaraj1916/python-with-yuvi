# write a program that reads three numbers A, B and C and checks if sum of any two numbers is always greater than 10.
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
C = int(input("Enter the third number: "))
result = (A + B > 10) and (B + C > 10) and (C + A > 10)
if result: 
    print("The sum of any two numbers is always greater than 10.")
else:
    print("The sum of any two numbers is not always greater than 10.")
