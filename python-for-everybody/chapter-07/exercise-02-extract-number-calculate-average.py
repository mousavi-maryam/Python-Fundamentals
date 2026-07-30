"""
Chapter 7 - Exercise 2

Objective:
Write a program that prompts the user for a file name, reads the file line by line, 
extracts the spam confidence values from lines beginning with `"X-DSPAM-Confidence:"`, 
and calculates the average of those values. The program should also handle the case where the specified file cannot be opened.

My Solution:
Prompted the user to enter a file name and used a `try`/`except` block to handle file-opening errors. 
Read the file line by line and identified lines starting with `"X-DSPAM-Confidence:"`. 
Extracted the numeric value from each matching line using the `split()` method, converted it to a floating-point number, 
and accumulated the total and count. After processing the file, calculated and displayed the average spam confidence value. 
If no matching lines were found, the program displayed an appropriate message.
"""

fname=input("Please enter a file name: ")
try:
    fhand=open(fname)
except FileNotFoundError:
    print('File cannot be opened:',fname)
    exit()

total=0
count=0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence:"):
        confidence=float(line.split(':')[1])
        total+=confidence
        count+=1
if count>0:
    average=total/count
    print("Average spam confidence:", average)
else:
    print("X-DSPAM-Confidence: not found")
