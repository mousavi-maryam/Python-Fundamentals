"""
Chapter 9 - Exercise 5
Objective:
Read an MBOX file and create a dictionary that counts how many messages were sent from each email domain.

My Solution:
Read the file line by line, extracted the sender's email address from each "From " line, separated the 
domain from the email address, and used a dictionary with .get() to count messages from each domain.
"""


fname = input("Please enter a file name: ")

try:
    fhand = open(fname)
except FileNotFoundError:
    print(fname, 'does not exist')
    exit()

domain_counts = {}

for line in fhand:
    line = line.rstrip()

    if line.startswith('From '):
        words = line.split()

        if len(words) > 1:
            email = words[1]
            domain = email.split("@")[1]
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

print(domain_counts)