# write a program that reads a three digit number and check if each digit is greater than 4 or first digit is equal to 6.
number = input("Enter a three digit number: ")
a = int(number[0])
b = int(number[1])
c = int(number[2])
result_1 = (a > 4) and (b > 4) and (c > 4)
result_2 = (a == 6) 
if result_1 or result_2:
    print("Each digit is greater than 4 or first digit is equal to 6.")
else:
    print("Each digit is not greater than 4 and first digit is not equal to 6.")
