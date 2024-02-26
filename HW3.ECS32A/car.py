#Homework 3 Problem 7 car.py
#Liana Williams
#
#Guess the price of a car game

# Set the target price of the car
target_price = 44500

# Initialize variables
num_guesses = 0


print("Guess the price and win the prize!")

#Loop
while True:
    guess = int(input("Enter your guess:"))

    # Increment the number of guesses
    num_guesses = num_guesses + 1

    # Check if the guess is correct
    if guess == target_price:
        if num_guesses <= 5:
            print("It took", num_guesses, "guesses.")
            print("You won the car!")
        else:
            print("It took", num_guesses, "guesses.")
            print("Too many guesses!")
        break
    elif guess < target_price:
        print("Too low!")
    else:
        print("Too high!")


