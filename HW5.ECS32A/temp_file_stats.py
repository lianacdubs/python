#Homework 5 temp_file_stats.py
#Liana Williams
#
#Find the outlier temperature and compare them to the long run average.

file_name = input("Temperature anomaly filename:")

# Initialize variables for min and max temperature and their corresponding years
min_temp = float('inf')
max_temp = float('-inf')
min_year = None
max_year = None

# Open the file for reading
with open(file_name, 'r') as file:
    # Read and ignore the first line (column header)
    file.readline()

    # Loop through the remaining lines of the file
    for line in file:
        # Use strip() to remove newline character, and split() to extract year and temperature
        year, temperature = line.strip().split(',')

        # Convert temperature to floating point number
        temperature = float(temperature)

        # Update min and max temperature and corresponding years
        if temperature < min_temp:
            min_temp = temperature
            min_year = year
        if temperature > max_temp:
            max_temp = temperature
            max_year = year

        # Print the result in the desired format
        # print(f"{year} {temperature}")  # You can uncomment this line if you want to print each year's temperature

# Print the overall minimum and maximum temperature and their corresponding years
print(f"Min temp: {min_temp} in {min_year}")
print(f"Max temp: {max_temp} in {max_year}")
