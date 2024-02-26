#Homework 3 Challenge pi.py
#Liana Williams
#
#Write a program that approx value of pi from the infinite series.

import math

def estimate_pi(num_terms):
    pi_estimate = 0.0

    for k in range(num_terms):
        pi_estimate += (-1) ** k / (2 * k + 1)
    pi_estimate *= 4

    return pi_estimate
#Get user input for terms
num_terms = int(input("Number of terms:"))

#Estimate pi and compute the error
pi_approx = estimate_pi(num_terms)
pi_error = math.pi - pi_approx

#Display result formatted 9 decimal places
print(f"Estimate of pi: {pi_approx:.9f}")
print(f"Error: {pi_error:.9f}")
