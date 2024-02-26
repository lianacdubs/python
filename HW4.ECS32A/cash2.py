#Homework 4 Problem 9 cash2.py
#Liana Williams
#
#Handle extra characters in the input

# Prompt the user for the name of the file
filename = input("Automated cash register\nEnter file of prices:")

# Initialize counters and total
item_count = 0
total_price = 0.0

# Open the file and process each line
with open(filename, 'r') as file:
    for line in file:
        try:
            # Remove leading dollar sign and convert the line to a floating-point number
            price = float(line.replace('$', '').strip())
            
            # Update counters and total
            item_count += 1
            total_price += price
        except ValueError:
            # Handle invalid input (non-numeric lines)
            pass  # Do nothing for invalid lines

# Display the result
print(f"File contained {item_count} items totaling ${total_price:.2f}")


