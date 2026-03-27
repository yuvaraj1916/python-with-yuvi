# write a program that reads a two digit number and checks if the number is greater than 25 and first digit of that number is greater than the second digit of that number.
number = input("Enter a two digit number: ")
first_digit = int(number[0])
second_digit = int(number[1])
if int(number) > 25 and first_digit > second_digit:
    print("The number is greater than 25 and the first digit is greater than the second digit.")
else:
    print("The number does not meet the criteria.")

