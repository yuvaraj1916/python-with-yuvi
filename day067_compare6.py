# write a program that reads two strings A1 and A2 , check if A2 is the first part of A1.
A1 = input("Enter the first string: ")
A2 = input("Enter the second String: ")
length_of_A2 = len(A2)
if A1[:length_of_A2] == A2:
    print("A2 is the first part of A1.")
else:
    print("A2 is not the first part of A1.")
