# write a program that reads a string and a number n and prints the string from the nth character to the end of the string
# for example, if the input string is "Hello, World!" and n is 7, the output should be "World!"
string = input("Enter a string: ")
n = int(input("Enter a number: "))
updated_string = string[n:]
print(updated_string)
