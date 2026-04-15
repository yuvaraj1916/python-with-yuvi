# Write a program that reads two numbers A and B, and checks if both the sum and product of the given numbers have less than 3 digits.
A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
sum_result = A + B 
product_result = A * B 
result_1 = sum_result < 100 
result_2 = product_result < 100 
if result_1 and result_2:
    print("Both the sum and product of the given numbers have less than 3 digits.")
else:
    print("Either the sum or product of the given numbers has 3 or more digits.")
