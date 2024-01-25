#Homework 1 Problem 9 divide.py
#Liana Williams
#
#Floor division to divide two numbers = whole number

num1 = int(input("Enter a number:"))#input number 1 
num2 = int(input("Enter a number to divide that by:")) #input number two 
quotient = num1//num2 #floor division for whole number
remainder = num1 % num2 #modulus division for remainder
print(f"{num1} divided by {num2} is {quotient} with {remainder} remaining")
