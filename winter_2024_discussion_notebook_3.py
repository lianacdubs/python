# -*- coding: utf-8 -*-
"""Winter 2024 Discussion Notebook 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sNTeO5h-ISP6PXnEhjGKrhe6JMbd4f_0

# Midterm 1 Practice

### Question 1
Write a program to prompt the user for hours and rate per hour to compute gross pay.

Example
```text
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
```
"""

# Write your program here
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print("Pay:",hours * rate)

"""### Question 2
Update your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Example
```text
Enter Hours: 45
Enter Rate: 10
Pay: 475.0
```

"""

# Copy and paste your program from Question 1 and update it here
hours = int(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hours > 40:
    total = rate * 1.5 * (hours - 40) + 40 * rate
else:
    total = hours * rate
print("Pay:",total)

"""### Question 3

Consider the following program. How many lines of text are printed? For partial credit show your logic.
"""

# Question 3: How mamy line printed
i = 0
counter = 0
while i <= 10:
    j = 0
    while j <=10:
        print("I'm ok")
        counter = counter + 1
        j = j + 1
    i = i + 1

print(counter)

"""121 Times!
 The outer loop runs from i = 0 to i = 10, and the inner loop runs from j = 0 to j = 10 for each iteration of the outer loop. Inside the inner loop, the statement print("I'm ok") is executed, and the counter variable is incremented by 1 for each print statement.

  The outer loop runs from i = 0 to i = 10, and the inner loop runs from j = 0 to j = 10 for each iteration of the outer loop. Inside the inner loop, the statement print("I'm ok") is executed, and the counter variable is incremented by 1 for each print statement.

  # outer loop iterations(11) * inner loop iterations(11) = 121

#### Question 4
Given a total number of minutes that may be greater than 60. Write expressions for the whole number of hours and the remaining number of minutes that would complete this program:

```text
total = int(input("Enter total minutes:"))

minutes = _______________________

hours = _________________________

print("That is",hours,"hours and",minutes,"minutes")
```
"""

# Question 3: Give number of Hours and minutes when given number of minutes
total = int(input("Enter total minutes: "))
minutes = total%60
hours = total//60
print("that is", hours, "hours and", minutes, "minutes")

"""### Question 5

Complete the following name formatter program by filling in the blank. The program asks for your first and last name. It then prints your name as Last, First. For example, when Jane Doe runs the program it prints "Doe, Jane":

```text
First name:Jane
Last name:Doe
Doe, Jane
```
"""

# Question 4: name formater
first = input("First name:")
last = input("Last name:")
formatted = last + ", " +first
print(formatted)

"""### Question 6
Assume that the days of the week are coded as integers:

0 = Sunday,
1 = Monday,
2 = Tuesday,
 ...,
5 = Friday,
6 = Saturday.

Select four of the lines of code given to create a program fragment that updates the variable weekday to the next working day (Monday through Friday) assuming it has already been created and is currently assigned to some working day.

```text
if weekday < 6:
if weekday < 5:
if weekday <= 5:
weekday = 0
weekday = 1
weekday = 5
else:
weekday = weekday + 1
```
"""

weekday = int(input("Enter 0-6: "))

#Paste 4 lines here
if weekday < 5:
  weekday = weekday + 1
else:
  weekday = 1


print(weekday)

"""### Question 7
Fill in the blank to randomly print 'rock', 'paper', or 'scissors'.

```text
import random
pick = _______________
print("I choose", pick)
```
"""

import random
pick = random.choice(['rock', 'paper', 'scissors'])
print("I choose", pick)

"""### Question 8

Fill in the blank so that the following program prints: `Sales tax on pi day will be 3.1%`

```text
pi = 3.14159
formatted = _______.format(pi)
print("Sales tax on pi day will be", formatted)
```
"""

pi = 3.14159
# Fill in here
formatetd = "{:.1f}".format(pi)
print("Sales tax on pi day will be", formatetd)

"""### Question 9
Complete this program that computes the area and perimeter of a rectangle with given width and height. If a rectangle has width w and height h, then the area is wh, and the perimeter is 2(w + h). The program needs to work with any width and height. Your program should be able to accept decimal numbers.

```text
width = input("Enter width:")
height = input("Enter height:")

# Compute the area and perimeter of a rectangle
_________________
_________________
_________________
_________________

# The following instructions print out your results
print("Area: ", area)
print("Perimeter: ", perimeter)
```
"""

width = input("Enter width:")
height = input("Enter height:")

# Compute the area and perimeter of a rectangle
area = float(height)*float(width)
perimeter = 2*(float(height) + float(width))

# The following instructions print out your results
print("Area: ", area)
print("Perimeter: ", perimeter)

"""### Question 10
Complete the following fragment of a program that asks for an integer from 1 through 9 (including 1 and 9). Assume the user only enters integers. The program should keep asking until the user enters a number in range.

```text
while True:
    x = int(input("Enter a positive single digit integer:"))
    if _____________ :
        break
print("You chose", x)
```
"""

while True:
    x = int(input("Enter a positive single digit integer:"))
    # Fill in below
    if x>=1 and x<=9 :
        break
print("You chose", x)

"""### Question 11

The following program is supposed to print the even integer values from 2 to 100 (including both 2 and 100), but it contains three semmantic errors. Correct the errors so that program produces the correct results.

```text
n = 1
while n < 100 :
   print(n)
   n = n * 2
```
"""

# Fix the following code
n = 2 #this used to have 1 now it has 2
while n <= 100 : #This line had < instead of <=
   print(n)
   n = n + 2 #This line used to have * instead of +
#Semmantic error: text that is grammatically correct but doesn't make any sense.

"""### Question 12

Write a program which repeatedly reads numbers until the user enters "done". Once "done" is entered, print out the total, count, and average of the numbers.

Example:
```text
Enter a number: 1
Enter a number: 1
Enter a number: 3
Enter a number: 2
Enter a number: 5
Enter a number: done
total: 12, count: 5: average 2.4
```
"""

# Enter your code here
total = 0
avg = 0
count = 0
while True:
  user_input = input("Enter a number: ")
  if user_input == "done":
    break
  user_input = int(user_input)
  total = total + user_input
  count = count + 1
print("total: {}, count: {}, average: {}".format(total, count, total/count))