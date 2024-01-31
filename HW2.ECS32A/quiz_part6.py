#Homework 2 Trivial Pusuit quiz_part6.py
#Liana Williams
#
#Invalid Input 

#Make an if statement that checks if the statement is invalid then goes into if else loop
score = 0
    
print("ART: Who painted 'The Persistance of Memory'?")
print("a. Dali")
print("b. Munch")
print("c. Picasso")

#This code assigns the variable (letter) to the name of the painter

correct_ans = 'a'#assigns the correct answer to a


choice = input("Enter your choice:")
if choice not in ['a','b','c']: #everything that is not those choices is wrong
    print("Invalid input! Enter a, b, or c next time.")
    print(f"The correct answer was {correct_ans}")
elif choice == correct_ans:
    print("Correct!")
    #If the user answers 'a' your program will respond.
    score += 1 #Increase the score by one if the answer is correct. 
else:
    print(f"The correct answer was {correct_ans}")
    #Otherwise this is how program responds.

#
print("ENTERTAINMENT: How many oscars did Hitchcock win?")
print("a. None")
print("b. One")
print("c. Two")


#This code assigns the variable (letter) to the amount of oscars

correct_ans1 = 'a'#assigns the correct answer to a 

choice = input("Enter your choice:")
if choice not in ['a','b','c']: #everything that is not those choices is wrong
    print("Invalid input! Enter a, b, or c next time.")
    print(f"The correct answer was {correct_ans1}")
elif choice == correct_ans1:
    print("Correct!")
    #If the user answers 'a' your program will respond.
    score += 1 #Increase the score by one if the answer is correct.
else:
    print(f"The correct answer was {correct_ans1}")
    #Otherwise this is how program responds.

# 
print("SCIENCE: Which dinosaur is most closely related to the pelican?")
print("a. Velociraptor")
print("b. Stegosaurus")
print("c. Pterodactyl")


#This code assigns the variable (letter) to the dinosaur

correct_ans2 = 'a'#assigns the correct answer to a 

choice = input("Enter your choice:")
if choice not in ['a','b','c']: #everything that is not those choices is wrong
    print("Invalid input! Enter a, b, or c next time.")
    print(f"The correct answer was {correct_ans2}")
elif choice == correct_ans2:
    print("Correct!")
    #If the user answers 'a' your program will respond.
    score += 1 #Increase the score by one if the answer is correct.
else:
    print(f"The correct answer was {correct_ans2}")
    #Otherwise this is how program responds.

# 
print("HISTORY: Which of the following was not invented in Baja California?")
print("a. Margaritas")
print("b. Chocolate")
print("c. Caesar Salad")


#This code assigns the variable (letter) to the amount of oscars

correct_ans3 = 'b'#assigns the correct answer to b

choice = input("Enter your choice:")
if choice not in ['a','b','c']: #everything that is not those choices is wrong
    print("Invalid input! Enter a, b, or c next time.")
    print(f"The correct answer was {correct_ans3}")
elif choice == correct_ans3:
    print("Correct!")
    #If the user answers 'a' your program will respond.
    score += 1 #Increase the score by one if the answer is correct.
else:
    print(f"The correct answer was {correct_ans3}")
    #Otherwise this is how program responds.


# 
print("SCIENCE AND NATURE: Can pigs swim?")
print("a. Yes")
print("b. No")
print("c. Only in salt water")


#This code assigns the variable (letter) to the amount of oscars

correct_ans4 = 'a'#assigns the correct answer to a 

choice = input("Enter your choice:")
if choice not in ['a','b','c']: #everything that is not those choices is wrong
    print("Invalid input! Enter a, b, or c next time.")
    print(f"The correct answer was {correct_ans4}")
elif choice == correct_ans4:
    print("Correct!")
    #If the user answers 'a' your program will respond.
    score += 1 #Increase the score by one if the answer is correct.
else:
    print(f"The correct answer was {correct_ans4}")
    #Otherwise this is how program responds.

# 
print("SPORT AND LEISURE: What color is the middle Olympic ring?")
print("a. Red")
print("b. Blue")
print("c. Black")


#This code assigns the variable (letter) to the amount of oscars

correct_ans5 = 'c'#assigns the correct answer to c

choice = input("Enter your choice:")

if choice not in ['a','b','c']: #everything that is not those choices is wrong
    print("Invalid input! Enter a, b, or c next time.")
    print(f"The correct answer was {correct_ans5}")
elif choice == correct_ans5:
    print("Correct!")
    #If the user answers 'a' your program will respond.
    score += 1 #Increase the score by one if the answer is correct.
else:
    print(f"The correct answer was {correct_ans5}")
    #Otherwise this is how program responds.



print("GENIUS: In ancient Rome, what is L divided by X?")
response = input("Enter your answer:")
if response == 'V' or response =='5': 
    print("Correct!")
    score += 1
else:
    print("Correct answers were 5 or V")


print(f"Your final score is {score}")
# print the final score before the interpretation

if score >= 0 and score <= 2:
    print("You were unlucky!")
#If the total score is from 0 through 2 it prints 
elif score >= 3 and score <= 4:
    print("At least you did better than chance!")
#If the score is from 3 through 4 it prints 
elif score >= 5 and score <= 6:
    print("Excellent!")
#If the score is from 5 through 6 it prints 
elif score == 7:
    print("Genius!")

