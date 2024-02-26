#Homework 3 Problem 4 tip.py
#Liana Williams
#
#Use looks to incorporate more flexible tipping options

#Get input for bill total
total_bill = float(input("Enter total:"))

#Print table of tip options from 15% to 25%
for tip_perc in range(15, 26):
    #Calc tip amount
    tip_amount = total_bill *(tip_perc / 100)
    #Format the tip percentage as a string
    formatted_percentage = "{:.0f}%".format(tip_perc)

    #Print tip info
    print(f"A {formatted_percentage} tip is ${tip_amount:.2f}")
