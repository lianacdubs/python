#Homework 5 read_temp_file.py
#Liana Williams
#
#Get a file name from the user and open it for reading

#This project I will analyze publicly available CSV formatted data from local
#July temperatures going back to 1880.
#PART1: Write a program to compute basic statistics about temp in the file.


file_name = input("Temperature anomaly filename:")

# Open the file for reading
with open(file_name, 'r') as file:
    # Read and ignore the first line (column header)
    file.readline()

    # Loop through the remaining lines of the file
    for line in file:
        # Use strip() to remove newline character, and split() to extract year and temperature
        year, temperature = line.strip().split(',')

        # Convert temperature to floating point number and print the result in the desired format
        print(f"{year} {float(temperature)}")

