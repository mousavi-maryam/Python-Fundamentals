""" 
Chapter 5 - Exercise 2

Objective:
Write a program that repeatedly prompts the user to enter numbers until `"done"` is entered. 
After the input is complete, display the minimum and maximum values from the valid numbers entered. 
The program should also handle invalid input using `try` and `except` without terminating.

My Solution:
Used a `while` loop to repeatedly prompt the user for input until `"done"` was entered. 
Stored each valid number in a list after validating the input with a `try`/`except` block. 
After the loop, used Python's built-in `min()` and `max()` functions to determine 
and display the minimum and maximum values. If no valid numbers were entered, 
the program displays an appropriate message."""


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
    print("Minimum:", min(numbers))
    print("Maximum:", max(numbers))
else:
    print("No numbers entered.")