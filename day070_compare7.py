# write a program that reads two numbers A and B , and checks if both numbers are greater than 20 or A is greater than B.
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
if (A > 20 and B > 20) or A > B:
    print("Both numbers are greater than 20 or A is greater than B.")
else:
    print("Both numbers are not greater than 20 and A is not greater than B.")
