#Homework 6 Part 4 happy4.py
#Liana Williams
#
#Read the GDP file
def read_gdp_data():
    # Open and read the file world_pop_gdp.tsv
    with open('world_pop_gdp.tsv', 'r') as file:
        # Read the first line (header) and print it as is
        header = file.readline().strip().replace('\t', ',')
        print(header)

        # Loop through each line in the file
        for line in file:
            # Split the line into a list using tabs as separators
            data = line.strip().split('\t')

            # Extract country name, population, and GDP per capita
            country = data[0].strip()
            population = data[1].replace(',', '')
            gdp_per_capita = data[2].replace('$', '').replace(',', '')

            # Print comma-separated output to the screen
            print(f"{country},{population},{gdp_per_capita}")

# Main function
def main():
    # Uncomment the call to read_gdp_data() for testing
    read_gdp_data()

if __name__ == "__main__":
    main()

