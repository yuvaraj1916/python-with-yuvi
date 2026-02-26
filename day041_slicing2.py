# write a program that reads a word and 2 indices (x,y) and print a part of the word from index x to index y
word = input("Enter a word: ")
x = int(input("Enter the first index: "))
y = int(input("Enter the second index: "))
y = y+1
part = word[x:y]
print(part)
