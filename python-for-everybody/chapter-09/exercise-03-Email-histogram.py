"""
Chapter 9 - Exercise 3
Objective:
Read through an MBOX mail log and use a dictionary to count how many messages were received from each 
email address.

My Solution:
Read the file line by line, identified valid "From " lines, extracted the sender's email address, 
and used a dictionary with .get() to maintain a running count for each sender. Added a guard for short 
lines and handled missing files.
"""

fname=input('please enter a file name: ')
try:
    fhand=open(fname)
except FileNotFoundError:
    print(fname, 'does not exist')
    exit()
mail_count={}
for line in fhand:
    line=line.strip()
    if line.startswith('From '):
        words=line.split()
        if len(words)>2:
            mail=words[1]   
            mail_count[mail] = mail_count.get(mail, 0) + 1

print(mail_count)