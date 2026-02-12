# write a program that reads a string and prints the first letter and remaining letters with (*)
word = input("Enter a word: ")
first_letter = word[0]
length = len(word)
remaining_letters = "*" * (length - 1)
result = first_letter + remaining_letters
print(result)
