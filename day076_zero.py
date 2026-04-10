# write a program that reads a three-digit number and check if the given number contains 0.
number = input("Enter a three-digit number: ")
result = (int(number[0])==0 or int(number[1])==0 or int(number[2])==0) 
if result:
    print("The given number contains 0.")
else:
    print("The given number does not contain 0.")
