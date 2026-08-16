"""
Chapter 8 - Exercise 2

Objective:
Identify the line that can cause an IndexError and modify the program to handle short or empty lines safely.

My Solution:
Added a check to ensure each line contains at least three words before accessing words[2].
"""

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) <3 : continue
    if words[0] != 'From' : continue
    print(words[2])