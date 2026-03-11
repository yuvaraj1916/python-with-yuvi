# write a program that reads 2 words w1 and w2. w1 contains two parts. The first part contains w2 and the second part contains the remaining letters in w1. Print w1 with the first part as stars (*).
w1 = input("Enter the first word (w1): ")
w2 = input("Enter the second word (w2): ")
length1 = len(w1)
length2 = len(w2)
star = length2 * "*"
part = w1[length2:]
result = star + part 
print(result)
