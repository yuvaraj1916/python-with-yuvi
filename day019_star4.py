# Write a Python program to display a word with stars on both sides. The count of stars should match the length of the word.
word = input("Enter a word: " )
length = len(word)
stars = length * "*"
print(stars + " " + word + " " + stars)