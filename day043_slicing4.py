# write a program that reads a string and prints the first half part of string 
string = input("Enter a string: ")
half_length = len(string) // 2 
updated_string = string[:half_length]
print(updated_string)
