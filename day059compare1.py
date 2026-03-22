# write a program that reads a 2 digit number and checks if the sum of the digits is greater than 7 or not.
number = input("Enter a 2 digit number: ")
digit_1 = int(number[0])
digit_2 = int(number[1])
sum_of_digits = digit_1 + digit_2 
if sum_of_digits > 7:
    print("The sum of the digits is greater than 7.")
else:
    print("The sum of the digits is not greater than 7.")
