"""
Chapter 3-Exercise 1

Objective
Rewrite the pay computation program to calculate overtime pay. 
Employees earn their regular hourly rate for the first 40 hours and 1.5 times the hourly rate for any additional hours worked.

My Solution
Collected the number of working hours and the hourly pay rate from the user. 
Used an `if`/`else` statement to calculate regular pay or overtime pay, 
then displayed the final salary rounded to two decimal places.
"""

hours=float(input('please enter working hours:\n'))
pay_rate=float(input('please enter your pay rate:\n'))

if hours>40:
    pay=round((40*pay_rate)+((hours-40)*(pay_rate*1.5)),2)
else:
    pay=round((hours)*(pay_rate),2)

print('pay: ',pay)
