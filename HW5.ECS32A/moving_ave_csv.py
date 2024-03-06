#Homework 5 moving_ave_csv.py
#Liana Williams
#
#From the last programm output a valid CSV file called MovingAve.csv
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

# Open the output file for writing
with open("MovingAve.csv", 'w') as output_file:
    # Write the header to the output file
    output_file.write("Year,Value\n")

    # Loop slides the window from index k to len(temps) - 1 - k
    for index in range(k, len(temperatures) - k):
        # Calculate year from index
        year = 1880 + index

        # Calculate average for the window centered at index
        ave = sum(temperatures[index - k : index + k + 1]) / (2 * k + 1)

        # Write year and average to the output file
        output_file.write(f"{year},{ave:.4f}\n")
