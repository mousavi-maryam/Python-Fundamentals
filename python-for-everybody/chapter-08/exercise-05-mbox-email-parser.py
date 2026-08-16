"""
Chapter 8 - Exercise 5

Objective:
Read an MBOX file, extract the email addresses from lines beginning with "From ", and count the total number of emails.

My Solution:
Read the user-specified file, identified valid "From " lines, extracted and printed the sender's email address, 
and counted the messages. Added guards for incomplete lines and error handling for missing files.
"""

fname=input("Please enter a file name: ")

count=0

try:
    fhand=open(fname)
    for line in fhand:
        if line.startswith("From "):
            words=line.split()
            if len(words)>1:
                print(words[1])
                count+=1
    print("There were", count, "lines in the file with From as the first word")
 
except FileNotFoundError:
    print("File does not exist")
    exit()
