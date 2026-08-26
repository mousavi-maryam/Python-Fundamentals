"""
Chapter 9 - Exercise 2

Objective:
Read a MBOX file, find the "From" lines, extract the day of the week from each message, 
and count how many messages were sent on each day.

My Solution:
Processed the file line by line, extracted the day from each valid "From" line, and used a dictionary 
with .get() to maintain a running count for each day. Added a guard for short lines and handled missing 
files with FileNotFoundError.

"""

fname=input('Please enter the file name: ')

try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname, 'does not exist')
    exit()

day_count={}
for line in fhand:
    if line.startswith('From '):
        words=line.split()
        if len (words)>2:
            day=words[2]
            day_count[day] = day_count.get(day, 0) + 1

print(day_count)