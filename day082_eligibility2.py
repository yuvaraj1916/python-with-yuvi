# write a program that reads the marks M in Maths, marks P in Physics and marks C in Chemistry and checks if any of the below conditions are satisfied:
# 1. M  >= 60 and P >= 50 and C >=45 and M + P + C >= 180.
# 2. M + P >= 120 or C + P >= 110.
M = int(input("Enter marks in Maths: "))
P = int(input("Enter marks in Physics: "))
C = int(input("Enter marks in Chemistry: "))
if (M >= 60 and P >= 50 and C >= 45 and M + P + C >= 180) or (M + P >= 120 or C + P >= 110):
    print("The student is eligible.")
else:
    print("The student is not eligible.")
