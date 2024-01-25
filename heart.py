#Homework 2 Problem 6 heart.py
#Liana Williams
#
#Gather inputs for age to get max and heart rate
age= int(input("Enter your age:"))
max_heart= int(220-age)
#formula for max_heart
print("Your maximum heart rate is", max_heart, "bpm")
target_heart= float(max_heart*(0.5))
#50% of max heart rate
target_heart2= float(max_heart*(0.85))
#85% of max heart rate
print("Your target heart rate is", target_heart, "-", target_heart2, "bpm")
