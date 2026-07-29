"""Chapter 3 - Exercise 2

Objective:
Modify the pay calculation program to handle invalid user input using `try` and `except`. 
If the user enters a non-numeric value for the working hours or hourly pay rate, 
the program should display an error message instead of crashing.

My Solution:
Prompted the user to enter the number of working hours and the hourly pay rate. 
Used a `try`/`except` block to convert the inputs to floating-point numbers and calculate the salary. 
If either input is not numeric, the program catches the `ValueError` exception and displays an appropriate error message.
"""

try:
    hours=float(input('please enter working hours:\n'))
    pay_rate=float(input('please enter pay rate:\n'))
    if hours>40:
        pay=round((40*pay_rate)+((hours-40)*(pay_rate*1.5)),2)
    else:
        pay=round((hours)*(pay_rate),2)
    print('pay:', pay)
except ValueError:
    print('Error, please enter numeric input')