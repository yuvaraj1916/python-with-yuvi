# write a program that reads a string and prints the first and last character of the string and (*) instead of remaining characters
word = input("Enter a word: ")
first_char = word[0]
last_char = word[-1]
middle = '*' * (len(word)-2)
print(first_char + middle + last_char)
