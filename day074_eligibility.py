# Write a program that reads the marks in Maths M, Physics P, and Chemistry C, and checks if any of the condition is satisfied:
# 1. M > 80 and P > 80 and C > 80
# M + P + C > 240 
M = int(input("Enter marks in Maths M: "))
P = int(input("Enter marks in Physics P: "))
C = int(input("Enter marks in Chemistry C: "))
if (M > 80 and P > 80 and C > 80) or (M + P + C > 240):
    print("The student is eligible.")
else:
    print("The student is not eligible.")
