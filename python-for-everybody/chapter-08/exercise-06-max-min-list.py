"""
Chapter 8 - Exercise 6

Objective:
Prompt the user for numbers, store them in a list, and use max() and min() to find the largest and 
smallest values after the loop ends.

My Solution:
Used a loop to collect numbers into a list until the user enters "done". Added error handling for 
invalid input and handled the case where no numbers are entered.
"""

numbers=[]
while True:
    number=input("Enter a number (or type 'done' to finish):")
    if number=="done":
        break
    try:
        number=float(number)
        numbers.append(number)
    except ValueError:
        print("Invalid input. please enter a number or 'done' to finish.")

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
    
else:
    print("No numbers entered.")