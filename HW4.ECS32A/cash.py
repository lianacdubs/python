#Homework 4 Problem 8 cash.py
#Liana Williams
#
#implements the cash register from the previous assignment, except that your input will now come from a file.

# Prompt the user for the name of the file
filename = input("Automated cash register\nEnter file of prices:")

# Initialize counters and total
item_count = 0
total_price = 0.0

# Open the file and process each line
with open(filename, 'r') as file:
    for line in file:
        try:
            # Convert the line to a floating-point number
            price = float(line.strip())
            
            # Update counters and total
            item_count += 1
            total_price += price
        except ValueError:
            # Handle invalid input (non-numeric lines)
            print(f"Skipping invalid line: {line.strip()}")

# Display the result
print(f"File contained {item_count} items totaling ${total_price:.2f}")
