# Write a program that reads a word and checks if the first letter and last letter of the word are not same.
word = input("Enter a word: ")
index_1 = word[0]
index_2 = word[-1]
if index_1 != index_2:
    print("The first and last letter of the word are not same.")
else:
    print("The first and last letter of the word are same.")

