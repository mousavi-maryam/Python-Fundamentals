"""
Chapter 7 - Exercise 3

Objective:
Modify the file-processing program to include an Easter Egg that displays a humorous message 
when the user enters the exact file name `"na na boo boo"`. For all other input, 
the program should behave normally by counting the number of subject lines in the specified 
file while handling file-opening errors gracefully.

My Solution:
Prompted the user to enter a file name and first checked whether the input matched the Easter 
Egg phrase `"na na boo boo"`. If it did, the program displayed a humorous message and terminated. 
Otherwise, it attempted to open the specified file using a `try`/`except` block. 
The program then read the file line by line, counted the lines beginning with `"Subject:"`, 
and displayed the total number of subject lines found.
"""

fname=input('please enter your file name:\n')
if fname=="na na boo boo":
    print("you have been punk'd")
    exit()
try:
    fhand=open(fname)
except FileNotFoundError:
    print('File cannot be opened:',fname)
    exit()
count=0
for line in fhand:
    if line.startswith('Subject:'):
        count=count+1
print('There were',count,'subject lines in', fname)