"""
Chapter 10 - Exercise 1
Objective:
Read an MBOX file, count messages from each mail address using a dictionary, then create a list of 
(count, mail) tuples and sort it in reverse order to find the person with the most messages.

My Solution:
Built a dictionary containing message counts for each mail address, converted the dictionary entries 
into (count, mail) tuples, sorted the list in reverse order, and printed the mail address with the 
highest message count.
"""

fname=input('Please enter a file name: ')
try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname,'does not exist')
    exit()

mail_count={}
for line in fhand:
    line=line.rstrip()
    if line.startswith('From '):
        words=line.split()
        if len (words)>2:
            mail=words[1]
            mail_count[mail] = mail_count.get(mail, 0) + 1

lst = []

for key, val in mail_count.items():
    lst.append((val, key))

lst.sort(reverse=True)

print(lst[0][1], lst[0][0])