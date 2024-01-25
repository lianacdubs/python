#Homework 1 Problem 10 converter.py
#Liana Williams
#
#Print out letter in integer and binary representations

#The ord() function is used to convert a letter to an integer.
#The bin() function converts an integer to a string representation of a binary number.

character = input("Enter a character:")
integer = ord(character)
binary = bin(integer)
print(f"{character} corresponds to the integer {integer} which is {binary} in binary.")
