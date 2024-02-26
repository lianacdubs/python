#Homework 4 Problem 6 cat.py
#Liana Williams
#
#Open a filename provided by the user and print every line of the opened file to the screen without modification
#a Python version of the UNIX filesystem utility cat which prints the content of a text file to the screen

# Prompt the user for the filename
filename = input("Enter a file name to open:")

# Attempt to open the file in read mode
try:
    with open(filename, 'r') as file:
        # Read and print each line of the file without modifying
        for line in file:
            # Suppress newline character added by print function
            print(line, end='')
except FileNotFoundError:
    print(f"Enter a file name to open: File not found. Please make sure you entered the correct filename.")
except Exception as e:
    print(f"An error occurred: {e}")

