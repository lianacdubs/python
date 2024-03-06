#Homework 5 moving_ave.py
#Liana Williams
#
#We must have at least k years before and k years after the year we are computing the average for. You should write a loop that only calculates the average for valid list indices. This loop is after the loop that reads the data from the file into a list. The iteration variable will "move" from the lowest valid year to the highest valid year. In the body of the loop the program should calculate and print the year and the moving average.  In our example, the iteration variable is called index, the lowest valid list index is k, and the highest valid list index is len(temps) - 1 - k.

file_name = input("Temperature anomaly filename:")

# Initialize an empty list to store temperatures
temperatures = []

# Open the file for reading
with open(file_name, 'r') as file:
    # Read and ignore the first line (column header)
    file.readline()

    # Loop through the remaining lines of the file
    for line in file:
        # Use strip() to remove newline character, and split() to extract year and temperature
        year, temperature_str = line.strip().split(',')

        # Convert temperature to floating point number
        temperature = float(temperature_str)

        # Add the temperature to the list
        temperatures.append(temperature)

# Get the window size parameter k from the user
k = int(input("Enter window size:"))

# Loop slides the window from index k to len(temps) - 1 - k
for index in range(k, len(temperatures) - k):
    # Calculate year from index
    year = 1880 + index

    # Calculate average for the window centered at index
    ave = sum(temperatures[index - k : index + k + 1]) / (2 * k + 1)

    # Print year and average
    print(f"{year},{ave:.4f}")

