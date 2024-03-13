#Homework 6 Challenge Problem
#Liana Williams
#
#Plotting the data


import matplotlib.pyplot as plt

def make_happy_dict():
    happy_dict = {}
    with open('happiness.csv', 'r') as file:
        file.readline()  # Skip header
        for line in file:
            country, _, happiness_index = map(str.strip, line.split(','))
            happy_dict[country] = happiness_index
    return happy_dict

def read_gdp_data(happy_dict):
    # Lists to store data for plotting
    countries = []
    populations = []
    gdp_per_capita = []
    happiness_indices = []

    with open('world_pop_gdp.tsv', 'r') as file:
        # Skip the header
        file.readline()

        for line in file:
            data = line.strip().split('\t')
            country = data[0].strip()
            population = float(data[1].replace(',', ''))

            # Skip countries with a population less than 10 million
            if population < 10:
                continue

            gdp = float(data[2].replace('$', '').replace(',', ''))
            gdp_per_capita.append(gdp)

            # Look up happiness index in the dictionary
            happiness_index = happy_dict.get(country, None)
            if happiness_index is not None:
                countries.append(country)
                populations.append(population)
                happiness_indices.append(float(happiness_index))

    # Create a scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(populations, gdp_per_capita, c=happiness_indices, cmap='viridis', s=100)

    # Label countries with populations over 100 million
    for i, country in enumerate(countries):
        if populations[i] > 100:
            plt.text(populations[i], gdp_per_capita[i], country, fontsize=8, ha='right', va='bottom')

    # Set plot labels and title
    plt.xlabel('Population (Millions)')
    plt.ylabel('GDP per Capita')
    plt.title('GDP per Capita vs Population with Happiness Index Color Mapping')

    # Show colorbar
    cbar = plt.colorbar()
    cbar.set_label('Happiness Index')

    # Save the plot as an image
    plt.savefig('Plot.png')
    plt.show()

def main():
    happy_dict = make_happy_dict()
    read_gdp_data(happy_dict)

if __name__ == "__main__":
    main()
