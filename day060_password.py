# write a program that reads a string and checks if it is a valid password or not. A valid password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, and one digit.
password = input("Enter a password: ")
if len(password) < 8:
    print("Password must be at least 8 characters long.")
elif not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter.")
elif not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter.")
elif not any(char.isdigit() for char in password):
    print("Password must contain at least one digit.")
else:
    print("Password is valid.")
