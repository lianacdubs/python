#Homework 6 Part 2 happy2.py
#Liana Williams
#
#Test the dictionary

def make_happy_dict():
    # Create an empty dictionary to store country names and happiness indices
    happy_dict = {}

    # Open and read the file happiness.csv
    with open('happiness.csv', 'r') as file:
        # Read the first line (header) and ignore it
        file.readline()

        # Loop through each line in the file
        for line in file:
            # Split the line into a list using commas as separators
            data = line.strip().split(',')

            # Extract country name and happiness index
            country = data[0].strip()
            happiness_index = data[2].strip()

            # Add key-value pair to the dictionary
            happy_dict[country] = happiness_index

    # Return the dictionary
    return happy_dict

# Function to print sorted dictionary
def print_sorted_dictionary(happy_dict):
    print("Contents of dictionary sorted by key.")
    print("Key Value")
    for key, value in sorted(happy_dict.items()):
        print(f"{key} {value}")

# Call the function and store the result in a variable
result_dict = make_happy_dict()

# Uncomment the call to print_sorted_dictionary to test the constructed dictionary
print_sorted_dictionary(result_dict)
