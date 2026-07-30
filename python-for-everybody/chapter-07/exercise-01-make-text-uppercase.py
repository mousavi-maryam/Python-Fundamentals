"""
Chapter 7 - Exercise 1

Objective:
Write a program that prompts the user for a file name, reads the file line by line, 
and displays its contents in uppercase. The program should also handle the case 
where the specified file cannot be opened.

My Solution:
Prompted the user to enter a file name and used a `try`/`except` block to handle file-opening errors. 
Read the file one line at a time using a `for` loop, removed the trailing newline character 
with `rstrip()`, converted each line to uppercase using the `upper()` string method, and printed the result.
"""

fname=input('Please enter a file name:\n')
try:
    fhand=open(fname)
except FileNotFoundError:
    print('File cannot be opened:',fname)
    exit()

for line in fhand:
    print(line.rstrip().upper())