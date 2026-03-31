# write a program that reads a selling price S and buying price B and calculates the profit or loss and prints it.
S = float(input("Enter the selling price: "))
B = float(input("Enter the buying price: "))
if S>B:
    profit = S - B
    print("The profit is:", profit)
elif S<B:
    loss = B - S 
    print("The loss is:", loss)
else:
    print("No profit no loss.")
