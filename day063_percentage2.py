# Write a program that reads a percentage P and number N and checks is the percentage of 500 is equal to the number N.
percentage = float(input("Enter a percentage (P): "))
number = float(input("Enter a Number (N): "))
percentage_of_500 = (percentage / 100) * 500 
if percentage_of_500 == number:
    print("The percentage of 500 is equal to the number N.")
else:
    print("The percentage of 500 is not equal to the number N.")
