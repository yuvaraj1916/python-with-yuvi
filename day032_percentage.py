# write a program that reads percentage of girls in the class and prints the percentage of boys 
# Note : Total percentage of Boys and Girls in a class is 100%
percentage_of_girls = float(input("Enter the percentage of girls: "))
percentage_of_boys = 100 - percentage_of_girls 
print("The percentage of boys is: " + str(percentage_of_boys) + "%")
