# write a program that reads a string and an integer number and prints the character at the index of the number
# constraints: 0 <= number < len(string)
string = input("Enter a string: ")
number = int(input("Enter an integer number: "))
if 0 <= number < len(string):
    print("The character at index", number, "is:", string[number])
else:
    print("Invalid index, please enter a number between 0 and", len(string)-1) 
