#Homework 4 Problem 1 parrot.py
#Liana Williams
#
#Echos the user types

while True:
    user_in = input(">")
#The program exits
    if user_in.lower() == "quiet":
        break
    else:
#echos what the user types in capitalization
        print(user_in.upper())
