# write a program that reads a string and number n and prints the first n characters of the word
string = input("Enter a string: ")
n = int(input("Enter a number: "))
updated_string = string[:n]
print(updated_string)
