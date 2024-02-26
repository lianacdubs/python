#Homework 3 Problem 3 dog.py
#Liana Williams
#
#Instructions to take a dog on a walk depending on the weather

#Get input from user about weather
weather = input("Enter weather condition (rainy/sunny/snowy/cloudy):").lower()

#Conditional statements to determine instructions based on weather
if weather == "rainy":
    instructions = "The dog should be taken for a short walk with an umbrella."
elif weather == "sunny":
    # Get user input for temp only if the weather is sunny
    temperature = int(input("Enter temperature:"))

    #Use nested conditionals based on temp
    if temperature > 80 and temperature <= 114:
        instructions = "The dog should be taken for a walk in the shade and given water."
    elif temperature > 45 and temperature <= 80:
        instructions = "The dog can enjoy a regular walk."
    elif temperature > -14 and temperature <= 45:
        instructions = "Dress the dog warmly for a walk."
    else:
        instructions = "Invalid weather condition."
elif weather == "snowy":
    instructions = "Take the dog for a short walk and ensure they stay warm."
elif weather == "cloudy":
    instructions = "Enjoy a regular walk with your dog."
else:
    instructions = "Invalid weather condition."

#Display instructions
print("Instructions for the walk:")
print(instructions)
