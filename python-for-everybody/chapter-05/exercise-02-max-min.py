"""
Chapter 5 - Exercise 2

Objective:
Prompt the user for numbers and find the maximum and minimum values without storing the numbers in a list.

My Solution:
Used None to initialize the minimum and maximum values, then updated them while iterating through the 
user's input. Added error handling for invalid input and stopped the loop when the user entered "done".
"""

maximum=None
minimum=None

while True:
    number=input('please enter a number:')
    if number=='done':
        break
    try:
        number=float(number)
        if minimum is None or number < minimum:
            minimum = number
        if maximum is None or number > maximum:
            maximum = number
    except ValueError:
        print('invalid data')
   
print('Max:', maximum, 'Min:',minimum)