#Homework 4 Phone Validator phone.py
#Liana Williams
#
#Validate phone numbers of the form 1-(###)-###-####.

phone= input("Enter number as ### ###-####:")
valid = len(phone) == 12 #the length is one more than the last value starting from 0 
pos = 0

while valid and pos < 12:

    if pos == 3:
        valid = phone[pos] == " " #there needs to be a space here to fit the format
    elif pos == 7:
        valid = phone[pos] == "-" #there needs to be a line here to fit the format
    else:
        valid = phone[pos].isdigit()
    pos += 1

if valid:
    print("Valid")
else:
    print("Invalid")

  
  
