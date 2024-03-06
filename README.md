# python
ECS32A Introduction to Programming 
## Table of Contents 
### Homework 1 Input Output
#### 
Problem 1: Fahrenheit to Celsius (10 points)

Here is an example temperature converter program you will modify.  

fahrenheit = 0
celsius = (fahrenheit - 32.0) * (5 / 9)
print(fahrenheit, "Fahrenheit is", celsius, "Celsius.")
In IDLE, create a new file and enter the three statements above.  Then run the program selecting ‘Run module’ under the Run menu. You will be asked to save the program.  When prompted, save the file as ‘fahr2cel.py’ in your HW1 folder. 

Next modify the first assignment statement of the program so that it converts 32 Fahrenheit to Celsius:

32 Fahrenheit is 0.0 Celsius.
Submit your finished program to Gradescope as fahr2cel.py

Problem 2: Celsius to Fahrenheit (10 points)

You should write a similar program ‘cel2fahr.py’ that converts a temperature given in Celsius to Fahrenheit.  For this part you will assign the variable celsius a value of 32 and the program should convert it to fahrenheit and print out this message exactly:

32 Celsius is 89.6 Fahrenheit.
Submit your finished program to Gradescope as cel2fahr.py

The following problems require user input.

Problem 3: Friendly Greeter (10 points)

Write a program that uses the input() function to prompt a user for their name and then welcome them. Below is a sample run illustrating how the program should work. (Note: a common convention we will use on assignments is to use blue for the output of your program and black to indicate what the user types when prompted for a particular example.) The user should be able to type any name.

What's your name?Nancy
Hi Nancy 
Submit your finished program to Gradescope as hello.py

Problem 4: Mad Libs (10 points)

Mad libsLinks to an external site. is a party game invented by Stern and Price in the 1950's. The party host solicits specific categories of words from guests and then uses them to complete a story to read aloud. You will write a computer program that plays Mad Libs using a fragment from a real Mad Libs game below.

Your program will be asking the user for

1. an adjective (e.g. nice)
2. a noun (e.g. book)
3. a plural noun
4. a place
5. a part of the body

And then fill them into numbered locations in the following template excerpted from BOOKish Mad Libs:

There are many <1> ways to choose a <2> to read. 
You could ask recommendations from your friends and <3>.
If they are no help, head to your local library or <4> and browse the shelves 
until something catches your <5>.
Below is a sample run of the completed program. The output should consist of five lines of questions, an intentionally blank line, followed by four lines of completed story. Try implementing your solution with one line of Python code for every line seen in the sample run below.

Enter an adjective:fun
Enter a noun:fish
Enter a plural noun:neighbors
Enter a place:store
Enter a part of the body:nose

There are many fun ways to choose a fish to read.
You could ask recommendations from your friends and neighbors.
If they are no help, head to your local library or store and browse the shelves
until something catches your nose.
Submit your finished program to Gradescope as mad.py

Problem 5: Body Mass Index (10 points)

The CDC gives a formulaLinks to an external site. on their website for calculating Body Mass Index or BMI given a height in inches and weight in pounds.

Write a program to calculate BMI given the inputs of height in inches and weight in pounds by translating the CDC formula into Python. Below is a sample run of the completed program. Test your program with these inputs and make sure your result matches exactly before uploading to Gradescope:

Enter height in inches:41.5
Enter weight in pounds:37.25
BMI: 15.204964436057484
Submit your finished program to Gradescope as bmi.py

Problem 6: Target Heart Rate (10 points)

While exercising, you can use a heart-rate monitor to see that your heart rate stays within a safe range suggested by your doctors and trainers. According to the American Heart Association (AHA), the formula for calculating your maximum heart rate in beats per minute is 220 minus your age in years. Your target heart rate is 50–85% of your maximum heart rate. Write a script that prompts for and inputs the user’s age and calculates and displays the user’s maximum heart rate and the range of the user’s target heart rate. [These formulas are estimates provided by the AHA; Your results may vary. Always consult a healthcare professional before beginning or modifying an exercise program.]

Hint: After your program gets the user's age, convert it to an integer using the int() function.

Below is a sample run with Python output in blue and user input in black.

Enter your age:77
Your maximum heart rate is 143 bpm
Your target heart rate is 71.5 - 121.55 bpm
Submit your finished program to Gradescope as heart.py

Problem 7: Paint Calculator (10 Points)

You have been hired by a local paint company to write coverage calculator for their website. A one gallon can of Monty's special Tru-Coat will cover 100 square ft. Your program will prompt the customer for the length, the width, and the average height of a rectangular room being painted in inches. Implement the following procedure to obtain the number of cans of paint to suggest.

Compute the area in square inches of the four walls to be covered
Compute the number of cans required as a floating point number.
Convert the floating point result to an integer and then add 1
Below is a sample run with Python output in blue and user input in black.

Paint coverage estimator
Length of room in inches:120
Width of room in inches:120
Average height of room in inches:96
You'll want 4 cans.
Submit your finished program to Gradescope as paint.py

Problem 8: Properties of a Circle (10 Points)

Write a program that prompts the user for a radius and then prints
the diameter, circumference, and the area of a circle with that radius.

Use 3.14159 for the value of pi.

Hint: After your program gets the radius, convert it to a floating point using the float() function.

Below is a sample run with Python output in blue and user input in black. The user should be able to type any radius.

Enter radius:2.5
Diameter 5.0
Circumference 15.70795
Area 19.6349375
Submit your finished program to Gradescope as circle.py

Problem 9: Whole number division (10 points)

Ask the user to enter two numbers.  Then use floor division to divide the first number by the second and also work out the remainder using the modulus operator and display the answer in a user-friendly way. 

Below is a sample run with Python output in blue and user input in black.

Enter a number:7
Enter a number to divide that by:2
7 divided by 2 is 3 with 1 remaining
Save and submit your program to Gradescope as divide.py

Problem 10: A look under the hood (10 points)

Under the hood, all Python data types need to be represented as binary integers to be understood by the computer's hardware. You will write a program to peek under the hood at the decimal and binary representation of characters. You will need two new Python functions to perform the conversion that work similar to the built in type conversion functions. The ord() function is used to convert a letter to an integer. The bin() function converts an integer to a string representation of a binary number. To see how these functions work you should play with these functions in the shell, as we do in this example:

>>> num = ord('A')
>>> print(num)
65

>>> binary = bin(65)
>>> print(binary)
0b1000001
Write a program that asks the user for a letter and prints out both the integer and binary representations of the letter.  It should ask the user for a character and then output the integer and binary representations of the character. Here is an example of what the output should look like if the user types the letter 'A' at the prompt:

Enter a character:A
A corresponds to the integer 65 which is 0b1000001 in binary.
Note in the output where we have inserted the character A and the decimal and binary representations of that character. You will need to write a print statement that includes all three as well as the intervening text.

Submit your finished program to Gradescope as converter.py

Challenge Problem: Cost of owning a Hybrid Car. (2 points)

Challenge problems are optional and for extra credit. You may skip this problem and still obtain full credit on the assignment. 

Write a program that helps a person decide whether to buy a hybrid car. Your program’s inputs should be:

The cost of the new car
The estimated resale value after five years
The estimated miles driven per year
The estimated average gas price over five years
The fuel efficiency in miles per gallon
Compute the total cost of owning the car for five years. For simplicity, the cost of owning the car will be comprised of two components 1) the five year cost to own the car which is its depreciation in value after 5 years and 2) the cost of gas to drive the car over the five year period. Here is an example of what the output should look like for an example set of inputs. Match this output exactly before submitting the program to Gradescope.

Cost of car:22000
Miles driven per year:15000
Cost of gas:5.50
Fuel efficiency (mpg):50
Estimated resale value after 5 years:16000
Five year gas cost: 8250.0
Five year car cost: 6000.0
Five year total cost: 14250.0
Submit your finished program to Gradescope as hybrid.py

### Homework 2 Trivial Pursuit
Part 1 Single question (20pts)

Write a program that prints the following question to the screen:

ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso
It will then immediately prompt the user to

Enter your choice:
If the user answers ‘a’ your program will respond 

Correct!
Otherwise your program will respond

The correct answer was a
Here is how your screen should look when you enter a correct answer (in black):

ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso
Enter your choice:a
Correct!
Here is how your screen should look when you enter anything other than 'a' (in black):

ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso
Enter your choice:d
The correct answer was a
Save this and submit it to gradescope as quiz_part1.py

Part 2 More questions (20pts)

Save your correct quiz_part1.py program as quiz_part2.py. Then extend it so that it asks the following questions (one from each category). Respond to each answer as you did for Part 1. The example below shows the case when only correct answers are given by the user. You should also handle the case when incorrect answers are given.

ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso
Enter your choice:a
Correct!
ENTERTAINMENT: How many oscars did Hitchcock win?
a. None
b. One
c. Two
Enter your choice:a
Correct!
SCIENCE: Which dinosaur is most closely related to the pelican?
a. Velociraptor
b. Stegosaurus
c. Pterodactyl
Enter your choice:a
Correct!
HISTORY: Which of the following was not invented in Baja California?
a. Margaritas
b. Chocolate
c. Caesar Salad
Enter your choice:b
Correct!
SCIENCE AND NATURE: Can pigs swim?
a. Yes
b. No
c. Only in salt water
Enter your choice:a
Correct!
SPORT AND LEISURE: What color is the middle Olympic ring?
a. Red
b. Blue
c. Black
Enter your choice:c
Correct!

Save this and submit it to gradescope as quiz_part2.py
Part 3 Tracking Score (15 pts)

The user should get one point for every question answered correctly. Think about how you will keep track of the score so that it can be printed out at the end. You will use a variable for this.

After all questions have been asked, print the following message given the appropriate total score from 0 to 6.

Your total score is 6
Submit this program as quiz_part3.py 

Part 4 Genius question (10pts)

Add a new GENIUS question to the end of your quiz with a more difficult to score answer.

GENIUS: In ancient Rome, what is L divided by X?
The Genius question is free response, so it will have the slightly modified prompt:

GENIUS: In ancient Rome, what is L divided by X?
Enter your answer:5
If the user answers the Roman numeral ‘V’ or the character ‘5’ (both are correct) your program will respond. 

Correct!
Otherwise your program will respond

Correct answers were 5 or V
Hint: Review logical operators to construct a Boolean expression that evaluates to True for either correct answer.

Submit this program as quiz_part4.py

Part 5 (20 points)

You will add a message to the end of the game interpreting what the score means:

If the total score is from 0 through 2 you will print

You were unlucky!
If the score is from 3 through 4 you will print

At least you did better than chance!
If the score is from 5 through 6 you will print

Excellent!
If the score is 7 you will print

Genius!
Save this and submit it to gradescope as quiz_part5.py

Part 6 Invalid Input (15 points)

You notice that users are entering upper case letters, complete responses, and other hard to deal with input. To help them out, you will extend your program so that if the user enters something other than 'a', 'b', or 'c' the program will immediately respond with

Invalid input! Enter a, b, or c next time.
Your program will go on to mark them incorrect.

This behavior will apply to the multiple choice questions only. Below is how your output should look for the first question:

ART: Who painted 'The Persistance of Memory'?
a. Dali
b. Munch
c. Picasso
Enter your choice:d
Invalid input! Enter a, b, or c next time.
The correct answer was a
Save this and submit it to gradescope as quiz_part6.py

Challenge Problem: Approximate Equality (2 points)

Challenge problems are optional and for extra credit. You may skip this problem and still obtain full credit on the assignment.

There are a number of ways to implement the functionality described in this problem and it can be done using only the language features described in lecture. Figuring out the implementation is a large part of the challenge. Another part will be figuring out how to give Gradescope exactly what it wants.

Often times two seemingly equivalent calculations will arrive at slightly different floating point results due to rounding errors inherent in the representation of these numbers in the computer.

>>> print("Weight on moon:", 100/6)
Weight on moon: 16.666666666666668
>>> print("Weight on moon:", 100*(1/6))
Weight on moon: 16.666666666666664
To circumvent this issue some sort of approximate equality is almost always used when comparing two floating point numbers. In this problem you will explore an implementation of approximate equality.

Two numbers are the same to 2 decimal places if the absolute value of their difference is less than 0.01. They are the same to 4 decimal places if the absolute value of their difference is less than 0.0001, and so on. 

You will write a program that takes two floating point numbers as input. If the numbers are identical then it will print "Those numbers are identical" as illustrated below.

Enter a number:3.14
Enter a number:3.14
Those numbers are identical 
If the numbers are the same to 2 - 9 decimal places, the program will print "Those numbers are the same to N decimal places" (where N is a number from 2 through 9) as illustrated below.

Enter a number:3.1415926
Enter a number:3.1415928
Those numbers are the same to 6 decimal places
If the numbers are the same to more than 9 decimal places the program will print "Those numbers are nearly identical" as illustrated below.

Enter a number:16.666666666666668
Enter a number:16.666666666666664
Those numbers are nearly identical 
If none of the previous categories apply because the numbers are the same to 1 or fewer decimal places, the program will print "Those numbers are different" as illustrated below.

Enter a number:3.14 
Enter a number:3
Those numbers are different 
approx.py

### Homework 3 Cents and $ensibility
Problem 1: (10 points) Pocket Change

This problem will get you acquainted with how to format a floating point number to a fixed number of decimal places.  In this case, the number of decimal places will be 2 for representing dollars and cents.

You will write a program that asks the user for a number of quarters, dimes, nickels, and pennies. Perhaps these coins are in their pocket. After obtaining those values, your program should compute and output the total number of dollars and cents.

To nicely format a floating point variable as a dollars and cents we will use:

formatted_str = "${:.2f}".format(amount)
The Python statement above converts the floating point value in the variable amount to a string and assigns it to a variable named formatted_str. The number 2 in the statement sets the precision. You should play with the statement first in the IDLE shell window using different values for the precision and  amount to see how the statement works. You ca place any text outside of the curly brackets. In this case, we are using a "$" to represent money.

Below is a sample run of the completed program.

Compute your pocket change!
Quarters?7
Dimes?6
Nickels?5
Pennies?4
The total is $2.64
Save and submit your completed program to Gradescope as pocket.py

Problem 2: (15 points) Making change

You will write a program that uses the // and % operators to figure out how to give change for a specified amount using the minimum number of coins (quarters, dimes, nickels, cents). You can assume that the user always enters a positive integer less than 100. The good news is that our currency is specifically designed to make the problem of using the fewest number of coins easy. For a given number of cents, first use as many quarters as possible, then as many dimes as possible, then as many nickels as possible. At each step use floor division to determine the number of (quarters, dimes, nickels) then use and modulus to determine the number of pennies left over. You should end up with four or fewer pennies after calculating the number of larger coins.

Below is an example of how your program should work. Just as before, in these examples your program should output the text in blue exactly when the user enters the text in black. If you add up the value of all the coins in the example it will total 66. This is also the smallest combination of coins that totals to 66.  

Enter cents:66
The minimum coins for 66 cents are:
2 Quarters
1 Dimes
1 Nickels
1 Pennies
Save and submit your program to Gradescope as change.py

Note: Use a while loop to solve for Problem 4 onward.

Problem 3 (15 points) : Dog Walking Intelligence

Write a Python program that provides personalized instructions on how to take a dog for a walk based on weather conditions and temperature.

The possible accepted values are:

Weather: rainy/sunny/snowy/cloudy

Temperature: any integer between -14 and 114

Your program should use conditional statements to generate a string with instructions. Here are the rules encoded in the flowchart below:

If the weather is "rainy," The dog should be taken for a short walk with an umbrella.
If the weather is "sunny" and the temperature is greater than 80 and less than or equal to 114 The dog should be taken for a walk in the shade and given water.
If the weather is "sunny" and the temperature is greater than 45 and less than or equal to 80 The dog can enjoy a regular walk.
If the weather is "sunny" and the temperature is greater than -14 and less than or equal to 45  Dress the dog warmly for a walk.
If the weather is "snowy," Take the dog for a short walk and ensure they stay warm.
If the weather is "cloudy," Enjoy a regular walk with your dog.
If the enters an invalid input, Invalid weather condition.
 

Untitled Diagram.drawio.png

 

Your program should ask the user to provide inputs for the weather condition and temperature if the weather is sunny, and then generate and display the appropriate instructions.

Enter weather condition (rainy/sunny/snowy/cloudy):sunny
Enter temperature:89
Instructions for the walk:
The dog should be taken for a walk in the shade and given water
Here is another example:

Enter weather condition (rainy/sunny/snowy/cloudy):rainy
Instructions for the walk:
The dog should be taken for a short walk with an umbrella.
Hints:

Use conditional statements (if, elif, else) to determine the instructions.
You may want to use nested conditionals (see taxes.py in Unit 3)
Ensure that the program asks for temperature only when it is sunny.
Generate a descriptive string with the appropriate instructions based on the provided inputs.
Save and submit your program to Gradescope as dog.py

Problem 4: (10 points) Tip table

You are prototyping more flexible tipping options for a mobile cash register app. Your customer wants the output screen to offer tipping options from 15% for mediochre service to 25% for great service. For this problem, you should use a loop where the iterator variable goes from 15 to 25,  and not a series of ten print statements. 

To demo the on screen text, you write a program that prompts the user for the total bill and prints a table of tip options. 

For example:

Enter total:123.42
A 15% tip is $18.51
A 16% tip is $19.75
A 17% tip is $20.98
A 18% tip is $22.22
A 19% tip is $23.45
A 20% tip is $24.68
A 21% tip is $25.92
A 22% tip is $27.15
A 23% tip is $28.39
A 24% tip is $29.62
A 25% tip is $30.86
For a starting point, see the multiplication table program in Unit 4. To format an integer or floating point variable pct as a percent value string you can use: 

formatted_str = "{:.0f}%".format(pct)
Save and submit your program to Gradescope as tip.py

Problem 5: Cash register (10 points)

Write a program that implements the behavior of a cash register. Your program will consist of an indefinite while loop that keeps asking the user for the price of an item. After the user enters the price the program will add it to a running total. When the user simply presses the enter key, exit the while loop and print the number of items entered and total price. Here is a transcript showing how the program should work:

Cash register (press enter to exit)
Enter item cost:23.99
Enter item cost:3.00
Enter item cost:1.43
Enter item cost:
You entered 3 items totaling $28.42
A good place to start would be to understand how the running sum works in the statistics.py program covered in Unit 4.

Account for 0 items as follows:

Cash register (press enter to exit)
Enter item cost:
You entered 0 items totaling $0.00
Save and submit your program to Gradescope as cash_register.py

Problem 6: How long to double your money - in a Roth IRA?  (15 points)

You will write a program that calculates the number of years it takes for an investment made in a Roth IRA to double in value. The program will prompt the user for an initial investment amount and an annual percent rate of return (APR). The investment will earn a yearly dividend which is automatically reinvested. Because it's a Roth, no taxes are paid on the investment income. You will use a while loop to implement the yearly calculation and value update.

The loop will terminate as soon as the deposit passes double its initial value. Print out the number of years it took for the initial deposit to double in value at the given rate of return. Here is a short transcript showing how the program would work using a 15% rate of return:

Enter an initial Roth IRA deposit amount:5000
Enter an annual percent rate of return:15
Value after year 1: $5750.00
Value after year 2: $6612.50
Value after year 3: $7604.38
Value after year 4: $8745.03
Value after year 5: $10056.79
It will take 5 years to double your investment with a 15% APR.
A good place to start would be to look at the compounded_yearly.py program from Unit 4.

Save and submit your program to Gradescope as roth.py

Problem 7: Guess the price of the car!?  (10 points)

You will implement a variant of the number guessing game we played in lecture. In this variant, you will ask the user to guess the price of a $44,500 car. Let's assume that the player knows the price of the car is rounded to the nearest $500.  If a player's guess is not exactly correct, your program will tell them they are either too high or too low.  The player will get as many guesses as they need to guess the price of the $44,500 car.  They need to guess correctly to finish the game, but they will only win the game if they used 5 or fewer guesses.

Here are two examples of how the program should work for both cases:

Guess the price and win the prize!
Enter your guess:50000
Too high!
Enter your guess:40000
Too low!
Enter your guess:45000
Too high!
Enter your guess:44500
It took 4 guesses.
You won the car!
Guess the price and win the prize!
Enter your guess:40000
Too low!
Enter your guess:41000
Too low!
Enter your guess:42000
Too low!
Enter your guess:43000
Too low!
Enter your guess:44000
Too low!
Enter your guess:45000
Too high!
Enter your guess:44500
It took 7 guesses.
Too many guesses!
A good place to start would be to understand the guess_big_num.py program covered in Unit 4.

Save and submit your program to Gradescope as car.py

Problem 8: Problem: Personal Fuel Economy Calculator (15 points)

You will write a program that calculates gas milage, also known as fuel economy. The program will use a while loop to repeatedly ask the user for the number of miles driven and gallons of gas used at their last fill up. On each iteration of the loop, your program will calculate the mileage for each fill up. The user will be able to exit the loop by pressing the enter key.  After the user exits the loop,  the program will print the cumulative gas mileage, by dividing the cumulative number of miles by the cumulative number of gallons.  The floating point output should be printed to one decimal place of precision.

Here is an example of how the program should work:

Your Personal Fuel Economy
Number of miles traveled (or enter to exit):380
Number of gallons needed:12
Mileage this tank = 31.7
Number of miles traveled (or enter to exit):235
Number of gallons needed:9
Mileage this tank = 26.1
Number of miles traveled (or enter to exit):
Average mileage = 29.3
The average mileage is always the total number of miles travelled over the total number of gallons used.

A good place to start would be to understand how a running sum works. This is covered in the reading. For another example see statistics.py in the Unit 4 slides. 

Save and submit your program to Gradescope as mileage.py

Challenge Problem: Approximating Pi (2 extra credit points)

You will write a program that approximates the value of the mathematical constant pi from the following infinite series.

 

Your program will prompt the number of terms in the series to use for the estimate. It will then approximate pi using exactly that many terms. To measure the approximation error, the program will also compute the difference between the approximation and the value of math.pi from the math module.  The output for both floating point values should be formatted to 9 decimal places.

When your program is run for 6 terms the output should be:

Number of terms:6
Estimate of pi: 2.976046176
Error: 0.165546478
When your program is run for 999 terms the output should be:

Number of terms:999
Estimate of pi: 3.142593654
Error: -0.001001001
Save and submit your program to Gradescope as pi.py

### Homework 4 Strings and Files 
Part 1 Strings
Problem 1: (10 points) The Shouting Parrot!

Write a simple parroting program that echos what the user types until they enter the word "quiet" in any capitalization. Start with the simple echo/parrot program from Unit 4. Modify the program so that your parrot SHOUTS back.  No matter what the input case is, the program output will be in uppercase. The program exits when the user enters "quiet" in any capitalization.

Below is an example of how your parrot program should work for a simple test case. It will prompt the user with a  single '>' and echo the capitalized user input.  Program output is in blue and user input is in black.

>This is NOT a dead parrot!    
THIS IS NOT A DEAD PARROT!
>Crackers anyone?
CRACKERS ANYONE?
>quiet
Save and submit your completed program to Gradescope as parrot.py

Problem 2: (15 points) Password Checker

You will modify the program word_stats.py in Unit 4 to create a password validator. Start by understanding the word_stats.py program from Unit 5. Your program based on that will ask the user to enter their password. Then it will print a message for each of five possible properties of the password.

Has length of at least 8 characters
Has at least one lower case character
Has at least one upper case character
Has at least one digit (0-9)
Has one of these six special characters: '!@#$%&'
The messages should appear in the order above.Below are two seperate examples of how your program should prompt the user and print the results when it is run:

Enter password:Special
Has lower case
Has upper case
Enter password:$pec1Alz
Has length
Has lower case
Has upper case
Has digit
Has special
Save and submit your completed program to Gradescope as password.py

Problem 3: (10 points) Phone Validator

Modify the phone_validator.py program given in Unit 5 to validate phone numbers of the form 1-(###)-###-####. If the phone number is in this form the program should print Valid otherwise it should print Invalid. Below are two examples of how your program should run with different inputs:

Enter number as ### ###-####:916 555-1212
Valid
Enter number as ### ###-####:530 555-SPAM
Invalid
Save and submit your completed program to Gradescope as phone.py

Problem 4: (10 points) Phone Number Extractor

Sometimes data is not always in the format we need it to be in. In this hypothetical situation, you are writing a program to load phone numbers into a database from user entered survey data. The 10 digit phone number will be stored in the database as an integer (e.g. 1234567890), however the user may enter the phone number in any format (e.g. 123-456-7890). You will write a program that creates a new string from the user entered number consisting of only the digits so it should have the same structure as word_quiz.py in the Unit 5 lecture slides. Below are two examples of how your program should run with different inputs:

Enter phone number:(530) 555-1212
Digit string: 5305551212

Enter phone number:916-123-4567
Digit string: 9161234567
There are a couple of ways you can implement this. Look at word_quiz.py from the lecture as one example of a program that creates a new string based on the characters in an input string.

Save and submit your completed program to Gradescope as digits.py

Problem 5: (15 points) Pig Latin Translator

This version of the made up language Pig Latin takes the first consonant of a word, moves it to the end of the word, and then adds an "ay" to the end of word. If a word begins with a vowel ("a","e","i","o","u") you just add "way" to the end of the word. Below are some examples of fruits in Pig Latin:

apple = apple + way = appleway
banana = anana + b + ay = ananabay
pear = ear + p + ay = earpay
fig = ig + f + ay = igfay
orange = orange + way = orangeway 
Write a Pig Latin translator. Your output will always be in lower case, so you should convert the input to lower case before translating the word. We will have seperate tests for cases that begin with a vowel and a consonant. You will get partial credit if your program implements one of the cases and full credit if your program implements both. You should review string slicing before tackling this problem.

Here is an example of how your program should prompt the user and print the result:

Enter a word:fig
fig in Pig Latin is igfay
Save and submit your completed program to Gradescope as translate.py

Part 2 Files
The Homework4 folder under Files for the files referenced in this section.

Problem 6:  (10 points) UNIX cat

You will implement a Python version of the UNIX filesystem utility cat which prints the content of a text file to the screen. The program cat is the starting point of many of the other UNIX file system utilities.

Your program will open a filename provided by the user and print every line of the opened file to the screen without modification.  In particular, make sure to suppress the newline character added by the print function. 

Here is an example of how your program should prompt the user for the filename and print the contents of the file. In this example the file is song.txt Download song.txtand it contains the first two lines of the infamous lumberjack song. 

Enter a file name to open:song.txt
I'm a lumberjack and I'm OK
I sleep all night, I work all day
Your program should work with any file and Gradescope will test your program using more than one file. You do not need to upload any files other than your completed program.

Use the examples for reading files in the Unit 5 lecture slides as a starting point.

Save and submit your completed program to Gradescope as cat.py

Problem 7: (10 points) Handling bad file names (10 points)

Now extend the previous version of your cat program from the previous problem. It will now add try and except in a loop to keep asking for the file name until it can be opened.

This is how your updated program should work:

Enter a file name to open:spam.txt
Could not open 'spam.txt'
Enter a file name to open:what was the name of that file?
Could not open 'what was the name of that file?'
Enter a file name to open:song.txt
I'm a lumberjack and I'm OK
I sleep all night, I work all day
For credit on this problem, extend your solution to problem 6 to add this functionality and re-submit the program to Gradescope with the same name: trycat.py

Problem 8: (10 points) Cash Register

Programmers often find themselves in the situation where they need to compute statistics from values in a file. You will write a program that implements the cash register from the previous assignment, except that your input will now come from a file. The first thing your program will do is prompt the user for the name of the file to open. You can assume the user will always enter the correct file name. You will then read each line of the file and convert the result to a floating point number. The input files will contain prices written without the dollar sign character, for example '3.95'. As before, your program will count and total the values.

The programs read_nums.py and statistics_file.py Download statistics_file.pyfrom lecture are good starting points for this problem.

Below is an example how the program should work for the file prices.txt Download prices.txt:

Automated cash register
Enter file of prices:prices.txt
File contained 4 items totaling $22.89
Important. Make sure you program works when no items are entered.

Save and submit your completed program to Gradescope as cash.py

Problem 9: (10 points) Handling extra characters in the input

Create a new version of your cash register program from the previous problem. The new version of the program should be able to handle input of the form '$3.95' by removing any leading dollar sign characters from the input. It should also be able to skip over lines of input that can not be converted to floating point numbers using try and except. We have provided test files dollars.txt Download dollars.txt and menu.txt Download menu.txt.

For example, the updated program should work the file menu.txt Download menu.txt.

spam
$4.95
eggs
$5.95
beans
$2.00
It should only add up the lines containing prices. The output should look exactly as follows:

Automated cash register
Enter file of prices:menu.txt
File contained 3 items totaling $12.90
Save and submit your completed program to Gradescope as cash2.py

Challenge Problem: (2 points) Credit Card Number Check

Challenge problems are optional and for extra credit. You may skip this problem and still obtain full credit on the assignment. 

The last digit of a credit card number is called the check digit. It can be used to verify a card number typed in is correct. The following method is used to verify actual credit card numbers but it has been simplified to 8 digits instead of 16:

Starting from the rightmost digit, form the sum of every other digit. For example, if the credit card number is 4358 9795, then you form the sum 5 + 7 + 8 + 3 = 23.
Double each of the digits that were not included in the preceding step. Add all digits of the resulting numbers. For example, with the number given above, doubling the digits, starting with the next-to-last one, yields 18 18 10 8. Adding all digits in these values yields 1 + 8 + 1 + 8 + 1 + 0 + 8 = 27.
Add the sums of the two preceding steps. If the last digit of the result is 0, the number is valid. In our case, 23 + 27 = 50, so the number is valid.
Write a program that implements this algorithm. The user should supply an 8-digit number, and you should print out whether the number is valid or not. If it is not valid, you should print the value of the check digit that would make it valid. The calculation is quite easy once you get the trick so part of the challenge is to figuring it out by yourself. Below are two examples for a valid and invalid card number.

Enter your 8-digit card number:4358 9795
Valid
Enter your 8-digit card number:4358 9796
Invalid
Check digit should be 5
Save and submit your completed program to Gradescope as check.py

### Homework 5 Temperature Anomaly 
In this assignment, we will look at climate change data from the National Oceanic and Atmospheric Administration. In particular, we will look at temperature anomaly over the last century. By "anomaly" the NOAA just means the difference between the annual temperature and the long term 20th century average temperature. The figure below from a recent article illustrates this data for Northern California. They used a popular statistical technique, a moving averageLinks to an external site., to filter out short term noise in the data so that the longer term trend is more apparent.

ExampleMovingAve.png  

Average July minimum temperatures (overnight lows) in California  (light orange line) from 1895–2018. The trend over the historical record is shown in dark orange, and the recent trend (2000-2018) is shown in red. The twentieth-century average is shown with a gray line. NOAA Climate.gov graph, based on data from NCEI's Climate at a GlanceLinks to an external site..

For this project you will analyze publicly available CSV formatted data for local July temperatures going back to the year 1880. First, you will write a program to compute basic statistics about the temperatures in the file. Then, you will write a program to compute a moving average and write that result to another CSV formatted file for plotting in a spreadsheet. 

We have broken this project down into separately graded incremental steps so you can iteratively develop and test each part.

Part 1: (15 points) Opening and Reading the Temperature File 

SacTemps.png  

July temperature anomaly data for Sacramento 1880-2018 plotted using Google sheets.

Download the temperature anomaly data file for our region from Canvas: SacramentoTemps.csv Download SacramentoTemps.csv. It's in the Homework5 folder under Files. Gradescope will also be testing your programs using a temperature anomaly data file for the Northern Hemisphere NorthernTemps.csv Download NorthernTemps.csv. You should look at these files in a text editor to see the format, rather than a spreadsheet which will import the data obscuring and possible changing the format.  Here are the first lines of SacramentoTemps.csv:

Year,Value
1880,-1.56
1881,-0.08
1882,-0.30
1883,-1.44
Your program will get a file name from the user and open it for reading. The first line is a column header that your program should read but ignore. Your program will then loop through the remaining lines of the file. In the block under the loop that reads the file, use the strip() string method to remove the newline character after each line of input and the split() string method to split on the comma to extract the year and the temperature into separate string variables. To test your code, add a print statement to print out the year and the temperature. The temperature should be changed to a floating point number to remove the trailing zeros and match the output expected by Gradescope.  The values should be separated by a space instead of the original comma.

The first lines of your programs output should look exactly like this:

Temperature anomaly filename:SacramentoTemps.csv
1880 -1.56
1881 -0.08
1882 -0.3
1883 -1.44
Submit your completed program to Gradescope as read_temp_file.py

Part 2 (20 points) Outlier Temperatures 

We are interested in finding outlier temperatures and comparing them to the long run average. 

Start a new program temp_file_stats.py from your working version of read_temp_file.py. Comment out the line that prints out the year and temperature for each year in the file. 

Add code to find the minimum and maximum  temperature for all of the years in the file and the years they occured in. You can base your solution on the starbucks_menu.py program we went over in lecture. Here is a transcript of how the program should work:

Temperature anomaly filename:SacramentoTemps.csv
Min temp: -2.32 in 1913
Max temp: 2.99 in 1889
Submit the completed program to Gradescope as temp_file_stats.py

Part 3 Reading the data into a list (15 points)

You are surprised that the hottest year on record in Sacramento was more than a century ago! You decide that you need to compute a moving average to observe the long term trend in the data.

Start a new program temp_list.py from your working version of read_temp_file.py. Comment out the line that prints out the year and temperature for each year in the file, and instead add the floating point temperatures one at a time to a growing Python list inside the for loop. Test your code by printing the list the loop that reads the file.

Below is an example of how your programs output should look:

Temperature anomaly filename:SacramentoTemps.csv
[-1.56, -0.08, -0.3, -1.44, ..., -0.06, -0.4, 0.48, 2.63, 0.18]
Submit the completed program to Gradescope as temp_list.py

Part 4 (15 points) Moving average part 1: first window

Start a new program first_ave.py from your working version of temp_list.py. Comment out the line that prints out the list of temperatures. 

For the moving average, we will let the user enter an integer k, then, for each year in our data file we will calculate the average of the k years before, the year itself, and the k years after that year. We can visualize this process as a window that slides across our temperature data. 

In the figure below the window is represented by the curly brackets. The window is centered on an index in the temperature list. We are interested in calculating the average temperature for the values in the window and the year on which the window is centered. The window slides across the temperature list, and at each new position we calculate the average and the year.

MovingAve.png  

Before starting the moving average calculation, you will first get the window size parameter k from the user.  You may assume that the user will always enter a valid integer between 0 and 60.  For example:

Enter window size:20
You can see in the figure that the moving average calculation is not valid for years near the ends of the list. We must have at least k years before and k years after the year we are computing the average for. In the first part we will focus on just calculating the average and the year for the first window.

Prototype the Calculation

We will start with implementing the first window to make sure the calculation works before moving to the more difficult problem of sliding the window.

For the first valid year in your temperature list, you will calculate the average of the k years before, the year itself, and the k years after. The easiest way to do this is using a list slice. The following three statements compute and print the year and the moving average for the first valid index in a list of temperatures called temps.

index = k
year = 1880 + index
ave = sum(temps[index-k:index+k+1]) / (2*k+1)
You should be able to insert these statements at the end of your program to calculate the year and the average. The output of your program for a window size of 20 will eventually look exactly like this:

Temperature anomaly filename:SacramentoTemps.csv
Enter window size:20
1900,-0.4171
Once you get the calculations for year and average working, format the output so that the values are separated by a comma and the average temperature is printed with exactly four decimal places using the format string method.

Submit the completed program to Gradescope as first_ave.py

Part 5 (10 points) Moving average part 2: slide the window. 

For this part, we move the window. Start a new program moving_ave.py from your working version of first_ave.py

We must have at least k years before and k years after the year we are computing the average for. You should write a loop that only calculates the average for valid list indices. This loop is after the loop that reads the data from the file into a list. The iteration variable will "move" from the lowest valid year to the highest valid year. In the body of the loop the program should calculate and print the year and the moving average.  In our example, the iteration variable is called index, the lowest valid list index is k, and the highest valid list index is len(temps) - 1 - k. 

Below is an outline of how the sliding window can be implemented using a for loop.  The call to the range function needs to be filled in so that it returns the sequence of integers from k to len(temps) - 1 - k. The calculation for year and ave given for the previous problem can be generalized (they should both be functions of index) and indented in the loop body to calculate the year and the moving average. 

# loop slides the window from index k to len(temps) - 1 - k
# for each index we calculate the corresponding year and 
# the average of the elements from temps[index-k] to temps[index+k] inclusive
for index in range(___________):
    # calculate year from index
    # calculate average for the window centered at index
    # print year,average
Here is a short example of how the output from your program look when the user chooses to average over a really long time scale of k = 60 years:

Temperature anomaly filename:SacramentoTemps.csv
Enter window size:60
1940,-0.2331
1941,-0.2169
1942,-0.2150
1943,-0.2228
1944,-0.2107
1945,-0.1796
1946,-0.1667
1947,-0.1582
1948,-0.1585
1949,-0.1492
1950,-0.1711
1951,-0.1688
1952,-0.1490
1953,-0.1556
1954,-0.1548
1955,-0.1580
1956,-0.1420
1957,-0.1101
1958,-0.1017
Submit the completed program to Gradescope as moving_ave.py

Part 6  (15 points) Create a .csv file 

Start a new program moving_ave_csv.py from your working version of moving_ave.py.

For the last program we will output a valid CSV file which you will always call MovingAve.csv.  

Change your program so that instead of printing the values to the screen (comment out the print statement) it writes the values to an output file that includes a simple one line header. For simplicity don't ask the user for the output file name, just call it MovingAve.csv. Finally, add a short column header to the output file: "Year,Value\n".

When you run your program with the following inputs it should produce this output:

Temperature anomaly filename:SacramentoTemps.csv
Enter window size:60

Opening the output  file in a text editor should look like this:

Year,Value
1940,-0.2331
1941,-0.2169
1942,-0.2150
1943,-0.2228
:
1955,-0.1580
1956,-0.1420
1957,-0.1101
1958,-0.1017
Submit the completed program to Gradescope as moving_ave_csv.py
Gradescope will look for the output file named MovingAve.csv and include its contents at the end of the expected output.

Part 7 Plotting the output (10 points)

To create a plot, run your program using a value for k equal to your current age on the data file SacramentoTemps.csv and make a nice plot in your favorite program (Excel, Sheets, Numbers, etc).  If you have never created a plot before, try Google sheets which was demonstrated in lecture. In Google sheets, import the file MovingAve.csv. Once the file has been imported,  select the data select Chart from the Insert menu. This will bring up a chart which you can label accordingly. Your plot should include a title and labels on both axes.

GoggleSheetsExamplePlot.png  

Upload a screenshot, image, or pdf of your plot (from a spreadsheet or your updated program) along with your submission. Name your file Plot. It should have an extension indicating what type of file it is (e.g. Plot.pdf) which should be visible in the upload dialog box.`

Submit the completed image/figure to Gradescope as Plot, Plot.png, Plot.pdf, Plot.jpg, etc. so the TAs can find it.

You will receive points after your submission has been manually graded by a TA. You will receive full credit if your figure includes the correct data, a title and labels on both axes.

Part 8: Extra Challenge (2 points) 

We posted a Jupyter notebook to on Canvas that includes examples of using the Python plotting library Matplotlib. Matplotlib_Examples.ipynb Download Matplotlib_Examples.ipynbStart a new program plot_moving_ave.py from your working version of moving_ave.py. Adapt the code in the time series example to automatically display the result of the moving average as a plot (see orange line below). If you cannot install Matplotlib on your own computer, you can test your program on Google Colab. Lookup the syntax for Matplotlib's plot function so that you can plot both the moving average smoothed (orange) and the original non-smoothed data (blue). Your result should look similar to the example below.

HW5 Challenge Problem

Note that there are actually two plots in the figure above. The smoothed temperatures are in orange and the original temperatures are in blue. In the example above, the original temperatures were only plotted for years where a smooth result could be computed, but plotting all data from the file is another option. Plotting two lines independently can be done with four lists (x1, y1, x2, y2) representing the x and y coordinates of the two lines (smoothed and raw). The syntax for plotting those lists using matplotlib's plot method is:

plot(x1, y1, x2, y2)

### Homework 6 Data Processing with Dictionaries and Functions 
The World Happiness Index 

In this homework assignment you will complete Python function definitions that  read a dataset into a dictionary, repeatedly query the dictionary to lookup values, and then use the dictionary to combine datasets from multiple sources to create a new dataset containing the information used to create the visualization below.

We will be looking at data from the World Happiness Report.Links to an external site. You have heard the saying that money doesn't buy happiness. While money only predicts a fraction of a countries happiness,  it clearly does help. We can visualize the relationship between money and happiness for large countries by analyzing public datasets. The relationship between these two attributes of a country are apparent, richer countries have a higher level of self reported happiness. Research also demonstrates that higher population density leads to less happiness. To simultaneously visualize population, the size of the bubbles on the plot below are drawn in proportion to the country's population.

BubblePlotEx.png

One goal of this project is to create a datafile of countries containing these three attributes of each country plotted in the figure above: 

1) Per capita GDP (i.e. Money) taken from the CIA World FactbookLinks to an external site..

2) Population taken from the CIA World FactbookLinks to an external site..

3) Happiness measured using survey data from the World Happiness ReportLinks to an external site.

It is common that data you want to analyze will come from multiple sources. The dictionary can be used as a tool for combining datasets based on a key that is shared between them. For this project it will be the name of the country.

To visualize the relationship between these attributes you can use a bubble plot like the one above. This plot can be created in Google Sheets from the output of your program. We will also provide a Jupyter notebook that creates bubble plots on the course Jupyter Hub. Submitting the final plot will not be required for this assignment.

To start this assignment: obtain the program  happy_stubs.py  along with the input files happiness.csv  and world_pop_gdp.tsv  from the Files/Homework6 directory on Canvas.  

For this assignment you will be filling out function stubs, similar to the way word_count.py and phone_dir.py were written in lecture. While the contents of the file happy_stubs.py may seem overwhelming at first, it is designed to guide you through this project. 

Note on Coding Style: This is the first assignment where you are writing functions. As described in Coding Style and Best Practices, for the function stubs provided add a comment just before the definition describing what the function does and, if it has a return value, what it returns.

Part 1 (20 points)  Read the happiness file

Start out by saving the file happy_stubs.py as happy1.py. Then fill in the function body of make_happy_dict() so that it opens and reads the input file happiness.csv which contains the country name, year the estimate was made, and a happiness index separated by commas. The function will return a dictionary mapping country names to their happiness index. The country names will be keys in the dictionary and the happiness index will be the value.

For this assignment you can just open the file happiness.csv, you will not need to ask the user for the file name.

The first five lines of the file happiness.csv look like this. Note there is a column header your program should read and ignore.

Country,Year of Estimate,Happiness Index
Afghanistan,2018,2.694303274
Albania,2018,5.004402637
Algeria,2018,5.043086052
Angola,2014,3.794837952
Then, write a loop that reads the open file line by line and adds key value pairs to a dictionary. Use the string methods split and strip to process each line, then extract the country name and the happiness index to string variables. You do not need to convert happiness index to a floating point value. .

To test that your code works, print  the country name and the happiness index to the screen.  The first five lines of the output will look like this:

Afghanistan 2.694303274
Albania 5.004402637
Algeria 5.043086052
Angola 3.794837952
Argentina 5.792796612
Finally, save each happiness index indexed by country to a dictionary you create. Modify the return statement so that the function make_happy_dict() returns the dictionary you created.

Save and submit the completed program to Gradescope as happy1.py.

Part 2 (10 points)  Test the dictionary you created

Save your completed program happy1.py as happy2.py. Inside the function make_happy_dict()  comment out the print statement and check that the function returns the dictionary you created in part 1. Note that the dictionary you return from make_happy_dict is saved to the variable happy_dict in main. To test that the dictionary was correctly constructed, uncomment the call to print_sorted_dictionary() in main(). This function is passed a dictionary argument and prints a sorted list of the key value pairs you added to the dictionary. The first five lines of the sorted output should now look like this:

Contents of dictionary sorted by key.
Key Value
Afghanistan 2.694303274
Albania 5.004402637
Algeria 5.043086052

Save and submit the completed program to Gradescope as happy2.py.

Part 3 (25 points)  Query the dictionary you created

Save your completed program happy2.py as happy3.py and comment out the call to the print_sorted_dictionary() in the main() function. The program reverse_lookup.py from Lecture 21 is a good template for the dictionary query pattern you will implement here.

You will complete the function lookup_happiness_by_country() that is passed the dictionary as an argument. Uncomment this function and complete the code so that your program uses an indefinite while loop to repeatedly ask the user for a country to look up in the dictionary. The input prompt is:

Enter a country to lookup or 'done' to exit:
If a country is in the dictionary your program will print the happiness index

Enter a country to lookup or 'done' to exit:Mexico
6.549578667
If a country is not in the dictionary, your program will print that country name was not found.

Enter a country to lookup or 'done' to exit:Atlantis
Atlantis not found
If the user just enters done, your program should simply return from the function call.

Enter a country to lookup or 'done' to exit:done
Below is an example of how your program should work. Make sure it matches this example before submitting it to Gradescope.

Enter a country to lookup or 'done' to exit:Taiwan
6.467004776
Enter a country to lookup or 'done' to exit:Brazil
6.190921783
Enter a country to lookup or 'done' to exit:Norway
7.444262028
Enter a country to lookup or 'done' to exit:Atlantis
Atlantis not found
Enter a country to lookup or 'done' to exit:done
When you are satisfied with how your program works, save and submit it to Gradescope as happy3.py.

Part 4 (20 points) Read the GDP file

Save your completed program happy3.py as happy4.py and comment out the call to the lookup_happiness_by_country() in the main() function. When you run the program it should have no output.

You will now start writing the function read_gdp_data() so that it reads the input file world_pop_gdp.tsv which contains the country name, population in millions, and the GDP per capita. The file contains a column header that should be ignored and looks like this:

Country Population in Millions GDP per Capita
China 1,394.02 $18,192.04
United States 332.64 $58,592.03
India 1,326.09 $7,144.29
Japan 125.51 $43,367.94
You will write a loop that reads the file and creates new comma separated output printed to the screen. The commas must be removed from the numbers in comma separated output. Also, because some plotting programs cannot deal with the $, that will also be removed from the output. Do that using string method calls.  

The first five lines of your programs printed comma separated output should look like this:

Country,Population in Millions,GDP per Capita
China,1394.02,18192.04
United States,332.64,58592.03
India,1326.09,7144.29
Japan,125.51,43367.94
When you are satisfied that your program works, save and submit it to Gradescope as happy4.py.

Part 5 (20 points) Add happiness data

Save your completed program happy4.py  as happy5.py

Next add code to the function read_gdp_data() so that it looks up the happiness index for each country in the dictionary. The dictionary is passed to the parameter variable happy_dict. Looking up the happiness index in the dictionary is done same way as in part 3. If the country does not exist in the dictionary, no output should be printed for that country. Finally, add a fourth column to your comma separated output that includes that happiness index. The first five lines of your updated programs output should look like this:

Country,Population in Millions,GDP per Capita,Happiness
China,1394.02,18192.04,5.131433964
United States,332.64,58592.03,6.882684708
India,1326.09,7144.29,3.818068743
Japan,125.51,43367.94,5.793575287
When you are satisfied your program works, save and submit this program to Gradescope as happy5.py.

Part 6 (10 points) Filter by population size

Save your completed program happy5.py  as happy6.py

Add code to the function read_gdp_data() so that if the population of a country is less than 100 million it is not included in the output. The complete output of your updated program should look like this:

Country,Population in Millions,GDP per Capita,Happiness
China,1394.02,18192.04,5.131433964
United States,332.64,58592.03,6.882684708
India,1326.09,7144.29,3.818068743
Japan,125.51,43367.94,5.793575287
Russia,141.72,28337.13,5.513500214
Indonesia,267.03,12171.08,5.340295792
Brazil,211.72,15341.31,6.190921783
Mexico,128.65,19145.03,6.549578667
Egypt,104.12,11563.09,4.005450726
Nigeria,214.03,5237.63,5.252288342
Pakistan,233.50,4543.88,5.471553802
Philippines,109.18,8034.38,5.869172573
Bangladesh,162.65,4244.06,4.499217033
Ethiopia,108.11,1855.46,4.379262447
When you are satisfied your program works, save and submit this program to Gradescope as happy6.py.

Challenge Problem: Plotting the Data (2 points):  

Submitting a plot for this assignment is not required. For students interested in creating the plot, you can plot the result in Google sheets or in Python using the Matplotlib module. A Jupyter notebook has been posted to the course Jupyter hub that plots the data using the. Matplotlib module.  

The plot below was created using Google sheets:

GoogleSheetsExampleBubblePlot.png

For 1 extra credit point submit a plot using Google Sheets or Microsoft Excel or Matplotlib. 

For 1 additional extra credit points modify your program from Part 6 to create a plot using matplotlib. See the Jupyter notebook of Matplotlib examples. Your code should plot the countries with populations over 10 million but only label the countries with populations over 100 million. 

Submit your plot (google sheets or matplotlib) to gradescope as Plot.pdf, Plot.png, etc. For the additional point, submit your updated code as happy_matplotlib.py. Extra credit will be manually graded after the submission deadline.
