#Homework 2 Trivial Pusuit quiz_part1.py
#Liana Williams
#
#Print a Question. Get an answer. Print answer. Conditional Logic.

print("ART: Who painted 'The Persistance of Memory'?")
print("a. Dali")
print("b. Munch")
print("c. Picasso")


#This code assigns the variable (letter) to the name of the painter

correct_ans = 'a'#assigns the correct answer to a 

choice = input("Enter your choice:")
if choice == correct_ans:
    print("Correct!")
    #If the user answers 'a' your program will respond.
else:
    print(f"The correct answer was {correct_ans}")
    #Otherwise this is how program responds.
    
