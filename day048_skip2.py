# write a program that reads a string and an index and prints the string without the character at the given index.
string = input("Enter a string: ")
index = int(input("Enter an index to skip: "))
if index < 0 or index >= len(string):
    print("Index is out of range.")
else:
    result = string[:index] + string[index+1:]
    print(result)
