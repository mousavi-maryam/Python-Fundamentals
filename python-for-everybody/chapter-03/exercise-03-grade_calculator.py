"""Chapter 3 - Exercise 3

Objective:
Write a program that prompts the user for a score between 0.0 and 1.0. 
Display the corresponding letter grade based on the given grading scale, 
and handle invalid or out-of-range input by printing an appropriate error message.

My Solution:
Prompted the user to enter a score and used a `try`/`except` block to validate that the input is numeric. 
Checked whether the score falls within the valid range (0.0 to 1.0) before using nested `if`/`elif`/`else` 
statements to determine and display the corresponding letter grade. 
Printed `"Bad Score"` for invalid or out-of-range input.
"""

score=input('please enter your score: ')
try:
    score=float(score)
    if 0<=score<=1:
        if score>=0.9:
            print ('grade: A')
        elif score>=0.8:
            print('grade: B')
        elif score>=0.7:
            print('grade: C')
        elif score>=0.6:
            print('grade: D')
        else:
            print('grade: F')   
    else:
        print('Bad score')
except ValueError:
    print('Bad score')