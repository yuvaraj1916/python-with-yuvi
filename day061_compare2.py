# write a program that reads two words A, and B, and index I . check if B starts at index I in A.
A = input("Enter the first Word: ")
B = input("Enter the second Word: ")
I = int(input("Enter the index: "))
length_A = len(A)
length_B = len(B)
part = A[I:I+length_B]
print(part == B)
