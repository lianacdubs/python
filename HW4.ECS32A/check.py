#Homework 4 Challenge Prob
#Liana Williams
#
#Credit Card Number Check

# Prompt the user for input
user_input = input("Enter your 8-digit card number:")

# Remove spaces and reverse the digits
card_number = user_input.replace(" ", "")[::-1]

# Step 1: Sum every other digit starting from the rightmost
step1_sum = sum(int(card_number[i]) for i in range(0, len(card_number), 2))

# Step 2: Double each of the remaining digits and add the resulting numbers
step2_sum = sum(int(digit) if int(digit) < 5 else int(digit) - 9 for i in range(1, len(card_number), 2) for digit in str(2 * int(card_number[i])))

# Step 3: Add the sums of the two preceding steps
total_sum = step1_sum + step2_sum

# Check if the number is valid
if total_sum % 10 == 0:
    print("Valid")
else:
    # Calculate the correct check digit that would make it valid
    check_digit = (10 - total_sum % 10) % 10
    print(f"Invalid\nCheck digit should be {check_digit}")
