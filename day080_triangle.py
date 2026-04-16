# write a program that reads the three sides A, B, and C of a triangle, and checks if the sum of two sides is greater than the third side for all three combinations of sides.
A = float(input("Enter the length of side A: ")) 
B = float(input("Enter the length of side B: ")) 
C = float(input("Enter the length of side C: ")) 
result_1 = A + B > C 
result_2 = A + C > B 
result_3 = B + C > A 
if result_1 and result_2 and result_3:
    print("The given sides can form a triangle.")
else:
    print("The given sides cannot form a triangle.")
