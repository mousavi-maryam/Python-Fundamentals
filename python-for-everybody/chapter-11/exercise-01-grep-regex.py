"""
Chapter 11 - Exercise 1:
Objective:
Ask the user for a regular expression and count the lines in a text file that match it.

My Solution:
Used re.search() to test each line against the entered regular expression and counted the matching lines.
"""

import re

fname=input('Please enter a file name: ')
regular_expressiopn = input('Enter a regular expression: ')

count = 0

try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname,'does not exist')

for line in fhand:
    if re.search(regular_expressiopn, line):
        count += 1

print('mbox.txt had', count, 'lines that matched', regular_expressiopn)