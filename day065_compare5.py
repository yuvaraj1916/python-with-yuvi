# write a program that reads a string and a number N and checks if the first N characters of the string and the last N characters of the string are not same.
string = input("Enter a string: ")
N = int(input("Enter a number N: "))
first_N_characters = string[:N]
last_N_characters = string[-N:]
if first_N_characters != last_N_characters:
    print("The first N characters of the string and the last N characters of the string are not same.") 
else:
    print("The first N characters of the string and the last N characters of the string are same.")
