#Homework 5 first_ave.py
#Liana Williams
#
#Compute a moving average to observe the long term trend in hottest years on record in Sacramento
#For the moving average, we will let the user enter an integer k, then, for each year in our data file we will calculate the average of the k years before, the year itself, and the k years after that year.

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

# Calculate the moving average for the first valid window
index = k
year = 1880 + index
ave = sum(temperatures[index - k : index + k + 1]) / (2 * k + 1)

# Format and print the output
print(f"{year},{ave:.4f}")
