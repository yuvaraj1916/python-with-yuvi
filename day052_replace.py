# Write a program that reads a word W, an index I, and a letter C, Print the word by replacing the the letter at index I with the letter C.
W = input("Enter a word: ")
I = int(input("Enter an index: "))
C = input("Enter a letter: ")
if 0 <= I < len(W):
    result = W[:I] + C + W[I+1:]
    print(result)
else:
    print("Index is out of range.")
