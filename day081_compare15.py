# write a program that reads a number N and checks if the number N is between 50 and 100 or if the first digit of N is equal to 7.
N = int(input("Enter a number: "))
if (50 < N < 100) or (str(N)[0] == '7'):
    print("The number is between 50 and 100 or the first digit is 7.")
else:
    print("The number does not meet the conditions.")
