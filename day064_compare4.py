# write a program that reads length and breadth of the rectangle and checks if area of rectangle is less than or equal to perimeter of rectangle.
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth 
perimeter = 2 * (length + breadth)
if area <= perimeter:
    print("The area of the rectangle is less than or equal to the perimeter of the rectangle.")
else:
    print("The area of the rectangle is greater than the perimeter of the rectangle.")
