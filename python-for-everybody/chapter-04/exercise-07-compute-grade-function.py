"""
Chapter 4 - Exercise 7

Objective:
Rewrite the grade calculation program by creating a function named `computegrade()` 
that accepts a score as its parameter and returns the corresponding letter grade. 
The program should also handle invalid or out-of-range input by returning an appropriate error message.

My Solution:
Defined a `computegrade()` function that takes a score as its parameter. 
Used a `try`/`except` block to validate that the input is numeric and 
checked whether the score falls within the valid range (0.0 to 1.0). 
Used conditional statements to determine the appropriate letter grade and returned the result as a string. 
Called the function with user input and displayed the returned value.
"""

def computegrade(score):
    if not 0<=score<=1:
        return "Bad score"
    elif score>=0.9:
        return "A"
    elif score>=0.8:
        return "B"
    elif score>=0.7:
        return "C"
    elif score>=0.6:
        return "D"
    else:
        return "F"   
score = input("Please enter your score: ")

try:
    score = float(score)
    print(computegrade(score))
except ValueError:
    print("Bad score")
