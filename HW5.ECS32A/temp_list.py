#Homework 5 temp_list.py
#Liana Williams
#
#Compute a moving average to observe the long term trend in hottest years on record in Sacramento

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

        # Print the result in the desired format
        # print(f"{year} {temperature}")  # You can uncomment this line if you want to print each year's temperature

# Print the list of temperatures
print(temperatures)
