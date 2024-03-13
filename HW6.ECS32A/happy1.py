#Homework 6 Part 1 happy1.py
#Liana Williams
#
#Read the happiness file

def make_happy_dict():
    # Create an empty dictionary to store country names and happiness index
    happiness_dict = {}

    # Open and read the happiness.csv file
    with open('happiness.csv', 'r') as file:
        # Skip the header line
        file.readline()

        # Iterate through each line in the file
        for line in file:
            # Split the line by commas and strip whitespace
            country, year, happiness_index = map(str.strip, line.split(','))

            # Print country name and happiness index
            print(f"{country} {happiness_index}")

            # Save happiness index indexed by country to the dictionary
            happiness_dict[country] = happiness_index

    # Return the created dictionary
    return happiness_dict

# Test the function
make_happy_dict()

