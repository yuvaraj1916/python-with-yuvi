# Write a program that reads a word and a number n  and prints the word repeated n times
word = input("Enter a word: ")
n = int(input("Enter a number: "))
if n >= 0:
    print(word * n)
else:
    print("please enter a non-negative number")
