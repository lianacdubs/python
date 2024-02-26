#Homework 3 Problem 6 compounded_yearly.py
#Liana Williams
#
#Calculates the number of years it takes for an investment in Roth IRA to double in value.

#Get user input for initial deposit and annual percent rate of return
int_deposit = float(input("Enter an initial Roth IRA deposit amount:"))
apr = int(input("Enter an annual percent rate of return:"))

#Initialize variables
current_value = int_deposit
years = 0

#while look calculates the value until it doubles
while current_value < int_deposit * 2:
    #calc yearly value and update current value
    current_value += current_value * (apr / 100)
    years += 1

    #display value after each year
    print(f"Value after year {years}: ${current_value:.2f}")
#display number of years it took to double the investment
print(f"It will take {years} years to double your investment with a {apr}% APR.")
