#Homework 3 Problem 2 change.py
#Liana Williams
#
#Compute the amount of change for a specified amount

#Get user input for the amount of cents
cents_str = input("Enter cents:")
cents = int(cents_str)

#Calculate the minimum coins needed
quarters = cents // 25 #floor division returns the largest integer than is <= the result
cents %= 25 #take value of cents and divide it by 25 and assign the remainder to cents

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

#Display results
print("The minimum coins for {} cents are:".format(cents_str))
print("{} Quarters".format(quarters))
print("{} Dimes".format(dimes))
print("{} Nickels".format(nickels))
print("{} Pennies".format(pennies))
