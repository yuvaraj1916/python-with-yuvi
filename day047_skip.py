# write a program that reads a string and skip the 4 th character and print the remaining chracters.
string = input("Enter a string: ")
if len(string) < 4:
    print("String is too short.")
else:
    result = string[:3] + string[4:]
    print(result)
