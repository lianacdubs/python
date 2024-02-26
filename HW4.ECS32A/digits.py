#Homework 4 Problem 4 digits.py
#Liana Williams
#
#Load phone numbers into a database from user entered survey data.

# Prompt the user for input
user_in = input("Enter phone number:")

# Initialize an empty string to store digits
digit_str = ""

# Iterate through each character in the input
for char in user_in:
    if char.isdigit():
        digit_str = digit_str + char

# Display the result
print(f"Digit string: {digit_str}")
