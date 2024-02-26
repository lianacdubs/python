#Homework 3 Problem 5 cash_register.py
#Liana Williams
#
#Program that acts like a cash register

total_price = 0.0
item_count = 0

print("Cash register (press enter to exit)")

while True:
    item_cost_in = input("Enter item cost:")

    #check if user pressed 'enter' (this means no input)
    if not item_cost_in:
        break

    if item_cost_in.replace(".", "", 1).isdigit():
        item_cost = float(item_cost_in)
        total_price += item_cost
        item_count += 1
    else:
        print("Invalid input. Please enter a valid number.")
print(f"You entered {item_count} items totaling ${total_price:.2f}")
        
