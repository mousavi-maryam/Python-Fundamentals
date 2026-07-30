"""
Chapter 5 - Exercise 1

Objective:
Write a program that repeatedly prompts the user to enter numbers until `"done"` is entered. 
The program should calculate and display the total, count, and average of all valid numbers entered. 
It should also handle invalid input using `try` and `except` without terminating the program.

My Solution:
Used a `while` loop to repeatedly prompt the user for input until `"done"` was entered. 
Applied a `try`/`except` block to validate numeric input, accumulated the total and count of valid numbers, 
and calculated the average after the loop finished. Invalid input is detected, an error message is displayed, 
and the program continues prompting the user for the next value.
"""

total = 0
count = 0
while True:
    number = input("Enter a number (or type 'done' to finish):")
    if number == "done":
        break
    try:
        number = float(number)
        total += number
        count += 1
    except ValueError:
        print("Invalid input. please enter a number or 'done' to finish.")

if count>0:
    average = total/count
    print(total, count, average)
else:
    print("No Numbers Entered")



   