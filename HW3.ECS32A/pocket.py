#Homework 3 Problem 1 pocket.py
#Liana Williams


#Compute amount of dollars and cents in pocket

#Get the input from the user about pocket change 
print("Compute your pocket change!")
quarters = int(input("Quarters?"))
dimes = int(input("Dimes?"))
nickels = int(input("Nickels?"))
pennies = int(input("Pennies?"))

#Calculate amount of pocket change
total_coins = quarters * 25 + dimes * 10 + nickels * 5 + pennies * 1
total_dollars = total_coins / 100

#Format floating point # to fixed number of decimal places.
print(f"The total is ${total_dollars:.2f}") 
