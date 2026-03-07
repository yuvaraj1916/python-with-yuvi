# write a program that reads a number N and prints three lines with each line containing N asterisks (*)
N = int(input("Enter a number: "))
star = "*" 
for i in range(3):
    print(star * N)
