# write.a program that reads two numbers A and B and check if any one of the below condition is satisfied:
# 1. The sum of A and B is less than 10.
# The difference between A and B is less than 10.
# A is between 5 and 30. 
A = int(input("Enter number A: ")) 
B = int(input("Enter number B: ")) 
if (A + B < 10) or (A - B < 10) or (5 < A < 30):
    print("Condition is satisfied.")
else:
    print("Condition is not satisfied.") 
