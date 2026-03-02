# write a program that reads a s string and a number n. Then print the last three characters os the string n times. 
string = input("Enter a string: ")
n = int(input("Enter a number: ")) 
last_three_characters = string[-3:] 
result = last_three_characters * n 
print(result)
