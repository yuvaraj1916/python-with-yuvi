# write a program that reads a number and convert it into positive if it is negative and print the result.
number = int(input("Enter a number: "))
if number < 0:
    number = -number 
print("The number is positive:", number)
