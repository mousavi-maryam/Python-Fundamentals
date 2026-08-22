"""
Chapter 9 - Exercise 4
Objective:
Determine which email address appears most frequently in an MBOX file and find the number of messages
sent by that person.

My Solution:
Built a dictionary containing the number of messages from each email address, then used a maximum loop 
to find the email address with the highest message count. Also extended the program to find the email 
address with the fewest messages.
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
max_count = None
max_email = None
for mail, count in mail_count.items():
     if max_count is None or count > max_count:
        max_count = count
        max_email = mail

print(max_email, max_count)



