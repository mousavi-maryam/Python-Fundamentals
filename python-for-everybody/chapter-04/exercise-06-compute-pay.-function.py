""" 
Chapter 4 - Exercise 6

Objective:
Rewrite the pay calculation program by creating a function named `computepay()`
that accepts the number of hours worked and the hourly pay rate as parameters. 
The function should calculate the total pay, including overtime pay at 1.5 times the regular 
hourly rate for any hours worked over 40.

My Solution:
Defined a `computepay()` function that takes the number of working hours and the hourly pay rate
as parameters. Used conditional statements to determine whether overtime applies and calculated 
the total pay accordingly. Called the function with user-provided input and displayed the returned result.
"""

def computepay(hours,rate):
    if hours<=40:
        return hours * rate
    else:
        overtime=hours-40
        return ((40 * rate) +( overtime * 1.5 * rate))
    

hours=float(input('Please enter number of hours you have worked:\n'))
rate= float(input('Please rnter your pay rate:\n'))
pay= computepay(hours,rate)

print ('Pay:', pay)