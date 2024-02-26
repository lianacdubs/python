#Homework 4 Problem 7
#Liana Williams
#
#Handling Bad File Names

while True:
    # Prompt the user for the filename
    filename = input("Enter a file name to open:")

    try:
        # Attempt to open the file in read mode
        with open(filename, 'r') as file:
            # Read and print each line of the file without modifying
            for line in file:
                # Suppress newline character added by print function
                print(line, end='')
        
        # If the file is successfully opened, break out of the loop
        break

    except FileNotFoundError:
        print(f"Could not open '{filename}'")

    except Exception as e:
        print(f"Could not open '{filename}'")
        break




