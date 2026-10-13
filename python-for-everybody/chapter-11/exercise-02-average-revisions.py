"""
Chapter 11 - Exercise 2:
Objective:
Use regular expressions and findall() to extract revision numbers from lines beginning with "New Revision:", 
then calculate and print their average as an integer.

My Solution:
Used re.findall() to identify the revision numbers, converted them to integers, and calculated the average 
using a running total and counter.
"""

import re

fname=input('Please enter a file name: ')

count = 0
total=0

try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname,'does not exist')

for line in fhand:
    number=re.findall('^New Revision: ([0-9]+)', line)
    if number:
        count += 1
        total += int(number[0])

print(int(total / count))

