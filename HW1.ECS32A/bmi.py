#Homework 1 Problem 5 bmi.py
#Liana Williams
#
#Calculate BMI given the inputs of height in inches and weight in pounds by translating the CDC formula into Python.
height= float(input("Enter height in inches:"))
weight= float(input("Enter weight in pounds:"))
bmi= weight/((height)**2)*703 #formula for BMI
print("BMI:", bmi)
