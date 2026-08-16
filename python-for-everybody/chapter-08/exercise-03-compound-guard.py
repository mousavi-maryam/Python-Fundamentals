"""
Chapter 8 - Exercise 3

Objective:
Rewrite the guardian code using a single if statement with a compound logical expression and the or operator.

My Solution:
Combined the two separate if statements into one condition using the or operator.
"""

fhand = open('mbox-short.txt')
for line in fhand:
    words = line.split()
    if len(words) <3 or words[0] != 'From' :continue
    print(words[2])