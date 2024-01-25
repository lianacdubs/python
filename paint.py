#Homework 1 Problem 7 paint.py
#Liana Williams
#
#Paint coverage calculator
print("Paint coverage estimator")

#variables in float
length = float(input("Length of room in inches:")) 
width = float(input("Width of room in inches:"))
height = float(input("Average height of room in inches:"))
#area formula to convert sqr inch to sqr ft 
area = ((length*height*2)+(height*width*2))/(144*100)
#convert floating point result to an integer and then add 1
paint_cans = int(area) + 1
print("You'll want", paint_cans, "cans.")
