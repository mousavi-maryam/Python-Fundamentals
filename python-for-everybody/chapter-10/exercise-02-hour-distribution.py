"""
Chapter 10 - Exercise 2

Objective:
Read an MBOX file, extract the hour from each message's "From" line, count how many messages occurred 
during each hour, and print the counts in chronological order.

My Solution:
Extracted the time from each valid "From " line, separated the hour from the time string, and used a 
dictionary to count messages for each hour. Converted the dictionary into (hour, count) tuples, 
sorted them by hour, and printed the results.

"""

fname=input('Please enter a file neme: ')
try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname, 'does not exist')
    exit()
hour_count={}
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        if len (words)>5:
            time=words[5]
            hour=time.split(':')[0]
            hour_count[hour] = hour_count.get(hour, 0) + 1

lst = []

for key, val in hour_count.items():
    lst.append((key, val))
lst.sort()

for key, val in lst:
    print(key, val)