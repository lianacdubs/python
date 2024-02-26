#Homework 4 Password Checker password.py
#Liana Williams
#
#Create a password validator.

#prompt for user input their password 
password_input = input("Enter password:")

#Check and print message for each of the five possible properties of the pw
if len(password_input) >= 8:
    print("Has length")
if any(char.islower() for char in password_input):
    print("Has lower case")
if any(char.isupper() for char in password_input):
    print("Has upper case")
if any(char.isdigit() for char in password_input):
    print("Has digit")
if any(char in '!@#$%&' for char in password_input):
    print("Has special")
