#Homework 6 Part 5 happy5.py
#Liana Williams
#
#Add Happiness Data
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

def read_gdp_data(happy_dict):
    # Open and read the file world_pop_gdp.tsv
    with open('world_pop_gdp.tsv', 'r') as file:
        # Read the first line (header) and print it as is
        header = file.readline().strip().replace('\t', ',') + ",Happiness"
        print(header)

        # Loop through each line in the file
        for line in file:
            # Split the line into a list using tabs as separators
            data = line.strip().split('\t')

            # Extract country name, population, and GDP per capita
            country = data[0].strip()
            population = data[1].replace(',', '')
            gdp_per_capita = data[2].replace('$', '').replace(',', '')

            # Look up happiness index in the dictionary
            happiness_index = happy_dict.get(country, None)

            # Print comma-separated output with happiness index
            if happiness_index is not None:
                print(f"{country},{population},{gdp_per_capita},{happiness_index}")

# Main function
def main():
    # Call the function and store the result in a variable
    result_dict = make_happy_dict()

    # Uncomment the call to read_gdp_data() for testing
    read_gdp_data(result_dict)

if __name__ == "__main__":
    main()
