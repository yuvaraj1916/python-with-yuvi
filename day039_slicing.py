# write a program that reads a word and prints the first 3 characters os the word 
word = input("Enter a word: ")
if len(word) >= 3:
    print(word[:3])
else:
    print("The word is too short to slice")
