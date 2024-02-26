#Homework 4 Problem 5 translate.py
#Liana Williams
#
#Takes the first consonant of a word, moves it to the end of the word, and then adds an "ay" to the end of word. If a word begins with a vowel ("a","e","i","o","u") you just add "way" to the end of the word.


# Prompt the user for input
user_in = input("Enter a word:").lower()

# Translate the input using Pig Latin rules
if user_in[0] in "aeiou":
    result = user_in + "way"
else:
    result = user_in[1:] + user_in[0] + "ay"

# Display the result
print(f"{user_in} in Pig latin is {result}")
