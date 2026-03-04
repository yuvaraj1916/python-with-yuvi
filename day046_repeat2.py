# write a program that reads a string and prints the first 2 and last 2 characters and remaining with stars.
string = input("Enter a string: ")
if len(string) < 4:
    print("String is too short.")
else:
    first_two = string[:2]
    last_two = string[-2:]
    middle_stars = "*" * (len(string)-4)
    result = first_two + middle_stars + last_two 
    print(result)
    