# write a program that reads a number N and prints three lines with each line containing N plus signs (+) 
N = int(input("Enter a number: "))
for _ in range(3):
    print("+" * N)
