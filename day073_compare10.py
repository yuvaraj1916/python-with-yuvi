# write a program that reads an age A, and guardian status S, and checks if the age between 12 and 60 if the guardian status S is equal to yes.
A = int(input("Enter age A: "))
S = input("Enter guardian status S (yes/no): ")
if 12 <= A <=60 and S.lower() == "yes":
    print("The age is between 12 and 60 and the guardian status is yes.")
else:
    print("The age is not between 12 and 60 or the guardian status is not yes.")
