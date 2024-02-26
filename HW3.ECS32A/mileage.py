#Homework 3 Question 8 mileage.py
#Liana Williams
#
#Calculate gas mileage (fuel economy)

# Initialize variables
total_miles = 0
total_gallons = 0

print("Your Personal Fuel Economy")

# Use a while loop to repeatedly ask for input
while True:
    # Get user input for miles traveled
    miles_in = input("Number of miles traveled (or enter to exit):")

    # Check if the input is empty (user pressed enter)
    if not miles_in:
        break

    # Check if miles_input is a valid float
    if not miles_in.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter valid numbers.")
        continue

    # Get user input for gallons needed
    gallons_in = input("Number of gallons needed:")

    # Check if gallons_input is a valid float
    if not gallons_in.replace('.', '', 1).isdigit():
        print("Invalid input. Please enter valid numbers.")
        continue

    # Convert input to float
    miles = float(miles_in)
    gallons = float(gallons_in)

    # Update total miles and total gallons
    total_miles += miles
    total_gallons += gallons

    # Calculate and print mileage for this tank
    mileage = miles / gallons
    print(f"Mileage this tank = {mileage:.1f}")

# Calculate and print average mileage
if total_gallons > 0:
    average_mileage = total_miles / total_gallons
    print(f"Average mileage = {average_mileage:.1f}")
else:
    print("No mileage data entered.")
