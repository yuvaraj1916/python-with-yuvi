# write a program that reverse the digit of 2 digit number
number = int(input("Enter a 2 digit number: "))
string_number = str(number)
first_number = string_number[0]
second_number = string_number[1]
reverse_number = second_number + first_number 
print("The reverse number is: " + reverse_number)
